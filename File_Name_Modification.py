import os
import glob
def File_name_Modi(path):
    '''
    :param path: 文件夹的地址，修改多个文件夹下的文件
    :return:
    '''
    path = path
    files = glob.glob(os.path.join(path, '*'))
    for file in files:
        file_id = file.split('\\')[-1]
        for filename in os.listdir(file):
            newname = file_id + '_' + filename
            os.rename(file + "\\" + filename, file + "\\" + newname)

def File_name_Modifi(path):
    '''
    :param path: 文件夹的地址,只修改一个文件夹下的文件
    :return:
    '''
    path = path
    for filename in os.listdir(path):
        image_name = filename.split('_')[-1]
        newname = '016_' + image_name
        os.rename(path + "\\" + filename, path + "\\" + newname)

path = r'E:\系统文件\桌面\demo'
File_name_Modi(path)
