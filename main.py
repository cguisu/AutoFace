import os
import shutil
import random
import sys
import time
import pickle
import shutil
import re

sys.path.append("DeepFaceLab\\")

# 确定训练代数
iter = input('Please input the iterations\n')

# 添加或改动必要文件
orgpath = 'subfile'
newpath = 'DeepFaceLab'
shutil.copy(os.path.join(orgpath, 'extract1.bat'), os.path.join(newpath, 'extract1.bat'))
shutil.copy(os.path.join(orgpath, 'extract2.bat'), os.path.join(newpath, 'extract2.bat'))
shutil.copy(os.path.join(orgpath, 'extract3.bat'), os.path.join(newpath, 'extract3.bat'))
shutil.copy(os.path.join(orgpath, 'extract4.bat'), os.path.join(newpath, 'extract4.bat'))
shutil.copy(os.path.join(orgpath, 'extract1.txt'), os.path.join(newpath, 'extract1.txt'))
shutil.copy(os.path.join(orgpath, 'extract2.txt'), os.path.join(newpath, 'extract2.txt'))
shutil.copy(os.path.join(orgpath, 'train.txt'), os.path.join(newpath, 'train.txt'))
shutil.copy(os.path.join(orgpath, 'train.txt'), os.path.join(newpath, 'extract1.txt'))
shutil.copy(os.path.join(orgpath, 'ModelBase.py'), os.path.join('DeepFaceLab\_internal\DeepFaceLab\models', 'ModelBase.py'))

with open(os.path.join(orgpath, 'Trainer.py'), 'r') as f:
    with open(os.path.join('DeepFaceLab\_internal\DeepFaceLab\mainscripts', 'Trainer.py'), 'w') as fd:
        fd.write(re.sub(r'model.target_iter = 100000', 'model.target_iter = %s' % iter, f.read()))



# 读取模特视频
model_vedios = []
for filename in os.listdir(r'model_vedio/'):
    model_vedios.append(filename)

# 读取学生视频
student_vedios = []
for filename in os.listdir(r'student_vedio/'):
    student_vedios.append(filename)

# 如果当前工作目录已存在
if os.path.exists('DeepFaceLab/workspace'):

    # 读取标签
    if os.path.exists('DeepFaceLab/workspace/flag'):
        with open('DeepFaceLab/workspace/flag', 'r') as f:
                name = f.readline()
        print(name)
        # 切换工作目录
        os.chdir("DeepFaceLab\\")

        # 执行主程序
        os.system("extract1.bat<extract1.txt")
        os.system("extract2.bat<extract2.txt")
        os.system("echo .|extract3.bat")
        os.system("echo .|extract4.bat")
        os.system("train.bat<train.txt")

        # 重命名
        os.rename('workspace', 'workspace_'+name)

        # 换回工作目录
        os.chdir("..\\")
    else:
        shutil.rmtree('DeepFaceLab/workspace')


for student_vedio in student_vedios:
    # 如果已有目录则继续训练
    if os.path.exists('DeepFaceLab/workspace_%s' % student_vedio[:-4]):
        os.rename('DeepFaceLab/workspace_'+student_vedio[:-4], 'DeepFaceLab/workspace')

    # 否则建立新的工作目录并放入视频
    else:
        # 建立工作目录
        shutil.copytree('DeepFaceLab/workspace_base', 'DeepFaceLab/workspace')

        # 随机选择模特
        model_vedio = random.choice(model_vedios)

        # 放入视频
        shutil.copyfile('student_vedio/' + student_vedio, 'DeepFaceLab/workspace/data_src.mp4')
        shutil.copyfile('model_vedio/' + model_vedio, 'DeepFaceLab/workspace/data_dst.mp4')

    # 切换工作目录
    os.chdir("DeepFaceLab\\")

    # 放入标签
    with open('workspace\\flag', 'w') as f:
        f.write(student_vedio[:-4])

    # 执行主程序
    os.system("extract1.bat<extract1.txt")
    os.system("extract2.bat<extract2.txt")
    os.system("echo .|extract3.bat")
    os.system("echo .|extract4.bat")
    os.system("train.bat<train.txt")

    # 重命名
    os.rename('workspace', 'workspace_'+student_vedio[:-4])

    # 换回工作目录
    os.chdir("..\\")

    time.sleep(1)

