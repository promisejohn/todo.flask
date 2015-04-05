# -*- coding:utf-8 -*-
#!/usr/bin/env python
#
# Author: promisejohn
# Email: promise.john@gmail.com
#

from flask import Flask, jsonify, abort, make_response, request, url_for

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/",methods=["GET"])
def index():
	return "Hello World!"

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({"error":"Not Found."}),404)

def makePublicTask(task):
	new_task = {}
	for field in task:
		if field == 'id':
			# _external=True means add Domain and ports to the URL generated.
			new_task['uri'] = url_for('getTask',task_id=task['id'],_external=True)
		else:
			new_task[field] = task[field]
	return new_task

@app.route("/todo/api/v1.0/tasks",methods=["GET"])
def getTasks():
	return jsonify({'tasks':map(makePublicTask,tasks)})

@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["GET"])
def getTask(task_id):
	task_list = filter(lambda t: t['id'] == task_id, tasks)
	if len(task_list) == 0:
		abort(404)
	return jsonify({'task':task_list[0]})

@app.route("/todo/api/v1.0/tasks",methods=["POST"])
def createTask():
	if not request.json or not 'title' in request.json:
		abort(400)
	task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
	tasks.append(task)
	return jsonify({"task":task}),201

@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=['PUT'])
def updateTask(task_id):
	task_list = filter(lambda t: t['id'] == task_id, tasks)
	if len(task_list) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'title' in request.json and type(request.json['title']) != unicode:
		abort(400)
	if 'description' in request.json and type(request.json['description']) is not unicode:
		abort(400)
	if 'done' in request.json and type(request.json['done']) is not bool:
		abort(400)
	task = task_list[0]
	task['title'] = request.json.get('title',task['title'])
	task['description'] = request.json.get('description',task['description'])
	task['done'] = request.json.get('done',task['done'])
	return jsonify({'task':task})

@app.route("/todo/api/v1.0/tasks/<int:task_id>",methods=["DELETE"])
def deleteTask(task_id):
	task_list = filter(lambda t: t['id'] == task_id, tasks)
	if len(task_list) == 0:
		abort(404)
	tasks.remove(task_list[0])
	return jsonify({'result':True})

if __name__ == '__main__':
	app.run(debug=True)