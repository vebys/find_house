import os

project_path = os.path.abspath(os.path.dirname(os.getcwd()))
os.system('/usr/bin/uwsgi  --stop %s/conf.d/uwsgi.pid' % project_path)
