# -*- coding: utf-8 -*-
import os

def get_project_path():
    """
    os.path.dirname(__file__)：当前文件夹的目录：C:/qkex20230901/base
    os.path.dirname(os.path.dirname(__file__))：获取 os.path.dirname(__file__)的上级目录：C:/qkex20230901
    :return: 项目的根目录:C:/qkex20230901
    """
    return os.path.dirname(os.path.dirname(__file__)).replace('/', '\\')