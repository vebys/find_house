import os


def start():
    project_path = os.path.abspath(os.path.dirname(os.getcwd()))
    os.system('/usr/bin/uwsgi  -i %s/conf/uwsgi.ini' % project_path)


if __name__ == '__main__':
    start()
