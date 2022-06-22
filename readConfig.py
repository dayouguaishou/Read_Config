import os
import configparser

# 读取配置文件
def getConfig(filename, section):
    """
    :param filename 文件名称
    :param section: 服务
    :return:返回配置信息(config_dic)
    """
 	 # 获取当前目录路径
    if "/" in filename or "\\" in filename:
        proDir = filename
    else:
        proDir = os.path.split(os.path.realpath(__file__))[0]

    # 拼接路径获取完整路径
    configPath = os.path.join(proDir, filename)

    # 创建ConfigParser对象
    conf = configparser.ConfigParser()

    # 读取文件内容
    conf.read(configPath)

    config = conf.items(section)

    config_dic = {}
    for tups in config:
        config_dic.update({tups[0]:tups[1]})
    return config_dic


if __name__ == '__main__':
    print(getConfig("Config.ini", 'mysql'))
