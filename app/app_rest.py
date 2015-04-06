# -*- coding:utf-8 -*-
#!/usr/bin/env python
#
# Author: promisejohn
# Email: promise.john@gmail.com
#
from flask import Flask
from flask_restful import Resource, Api, reqparse, fields, marshal
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()

tasks = [
    {
        'id': 1,
        'title': u'学习 python',
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

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}

@auth.get_password
def getPassword(username):
    if username == 'hello':
        return 'python'
    return None


class Hello(Resource):
    def get(self):
        return {'hello':'world'}

class TaskListAPI(Resource):
    decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, required = True, 
            help = 'No task title provided', location = 'json')
        self.reqparse.add_argument('description', type = str, default = "", location = 'json')
        super(TaskListAPI, self).__init__()

    def get(self):
        return {'tasks':map(lambda t: marshal(t,task_fields),tasks)}

    def post(self):
        task = {
            'id': tasks[-1]['id'] + 1,
            'done': False,
        }
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                task[k] = v
        tasks.append(task) 
        return {'task':task} ,201

class TaskAPI(Resource):
    decorators = [auth.login_required]

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type = str, location = 'json')
        self.reqparse.add_argument('description', type = str, location = 'json')
        self.reqparse.add_argument('done', type = bool, location = 'json')
        super(TaskAPI, self).__init__()

    def get(self,id):
        task_list = filter(lambda t: t['id'] == id, tasks)
        if len(task_list) == 0:
            abort(404)
        return {'task':task_list[0]}

    def put(self,id):
        task_list = filter(lambda t: t['id'] == id, tasks)
        if len(task_list) == 0:
            abort(404)
        task = task_list[0]
        args = self.reqparse.parse_args()
        for k, v in args.iteritems():
            if v != None:
                task[k] = v
        return { 'task': marshal(task, task_fields) }

    def delete(self,id):
        task_list = filter(lambda t: t['id'] == id, tasks)
        if len(task_list) == 0:
            abort(404)
        tasks.remove(task_list[0])
        return {'result':True}

api.add_resource(Hello,'/')
api.add_resource(TaskListAPI,'/todo/api/v1.0/tasks',endpoint='tasks')
api.add_resource(TaskAPI,'/todo/api/v1.0/task/<int:id>',endpoint='task')


if __name__ == '__main__':
    app.run(debug=True)