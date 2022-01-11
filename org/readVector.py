# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：readVector.py
@Author  ：Xin Zheng
@Date    ：2021/11/15 22:14 
'''

import sys
from osgeo import ogr


def writeVecctor():
    dir = r"E:\data\arcgis\osgeopy-data\osgeopy-data\global"
    ds = ogr.Open(dir, 1)  # 打开要写入的数据源
    if ds is None:
        sys.exit("Could not open folder.")
    in_lyr = ds.GetLayer('ne_50m_populated_places')  # 获取shp文件

    if ds.GetLayer("capital _cities"):
        ds.DeleLayer("capital_cities")




if __name__ == "__main__":
    writeVecctor()