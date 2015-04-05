# todo.flask
Todo sample webapp's backend with flask.

Arch: Restful with json

HTTP方法	| URI	                                            | 动作
------- | ------------------------------------------------- | --------
GET	    | http://[hostname]/todo/api/v1.0/tasks	|检索任务清单 |
GET	    | http://[hostname]/todo/api/v1.0/tasks/[task_id]	| 检索一个任务
POST	| http://[hostname]/todo/api/v1.0/tasks	            | 创建一个新任务
PUT	    | http://[hostname]/todo/api/v1.0/tasks/[task_id]	| 更新一个已存在的任务
DELETE	| http://[hostname]/todo/api/v1.0/tasks/[task_id]	| 删除一个任务


$ flask/bin/pip install flask
$ flask/bin/pip install flask-login
$ flask/bin/pip install flask-openid
$ flask/bin/pip install flask-mail
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install sqlalchemy-migrate
$ flask/bin/pip install flask-whooshalchemy
$ flask/bin/pip install flask-wtf
$ flask/bin/pip install flask-babel
$ flask/bin/pip install guess_language
$ flask/bin/pip install flipflop
$ flask/bin/pip install coverage