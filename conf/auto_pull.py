import os


def pull():
    euid = os.geteuid()
    print(euid)
    project_path = os.path.abspath(os.path.dirname(os.getcwd()))
    print('当前路径：',project_path)

    os.system('git pull origin master')
    print('拉取完成')


if __name__ == '__main__':
    pull()
