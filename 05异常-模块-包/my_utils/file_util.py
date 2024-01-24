# -*- encoding: utf-8 -*-
# File : file_util.py
# Author : YinhuKang
# E-mail : kangyinhunnu@gmail.com
# Date:2024/01/24 15:55

# 接收传入文件的路径 打印文件的全部内容 
# 如果文件不存在则捕获异常 输出提示信息 finally关闭文件对象
def print_file_info(file_name: str):
    """
    将给定路径的文件内容输出到控制台
    :param file_name: 即将读取文件的路径
    :return: None
    """
    try:
        f = open(file_name, 'r', encoding= 'UTF-8')
        print('Open File Successfully!')
        content = f.readlines()
        print(content)
    except Exception as e:
        print(f'您输入文件的路径为{file_name}, 该文件不存在!')
    else:
        print(f'打印完成, 共计{len(content)}字节')
    finally:
        f.close()

# 接收文件路径以及传入数据 将数据追加写入到文件中
def append_to_file(file_name: str, data: str):
    fw = open(file_name, 'a', encoding= 'UTF-8')
    fw.write(data)
    fw.flush()

if __name__ == '__main__':
    print_file_info('./05异常-模块-包/test.txt')