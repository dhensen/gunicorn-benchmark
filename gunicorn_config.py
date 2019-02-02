# from eventlet import monkey_patch


# def on_starting(server):
#     monkey_patch()


backlog = 10240

workers = 9
worker_connections = 1000
worker_class = 'eventlet'

bind = '0.0.0.0:8001'
reload = True
