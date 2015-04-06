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


可能用到的类库：
flask
flask-restful
flask-login
flask-openid
flask-mail
flask-sqlalchemy
sqlalchemy-migrate
flask-whooshalchemy
flask-wtf
flask-babel
guess_language
flipflop
coverage

todo:
Add database support
Add Multi-User support
Add tox build support