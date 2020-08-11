import os
import shutil

conf_path = os.getcwd()
newconf_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'conf.d')
setting_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'find_house')
print('conf路径：', conf_path)
print('conf.d路径', newconf_path)
files = os.listdir(conf_path)
if not os.path.exists(newconf_path):
    os.makedirs(newconf_path)
# for f in files:
#     print('正在复制', f)
#     shutil.copy(f, newconf_path)
os.system('cp %s/* %s/' % (conf_path, newconf_path))
os.system('chmod +x  %s/*' % newconf_path)
# os.system('cp %s/settings_pro.py %s/settings.py' % (setting_path, setting_path))
# os.system('git checkout .')
print('初始化完成')
