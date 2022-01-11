# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：meta.py
@Author  ：Xin Zheng
@Date    ：2021/11/15 21:50 
'''
import os
from osgeo import ogr


#读取元数据
def readMete():
    fn = r"E:\data\arcgis\osgeopy-data\osgeopy-data\Washington\large_cities.geojson"
    ds = ogr.Open(fn)  # 打开数据源
    lyr = ds.GetLayer(0)
    extent = lyr.GetExtent()  #最小外接矩形
    print(extent)
    print(lyr.GetSpatialRef())   #空间参考

    #获取属性字段
    for field in lyr.schema:
        print(field.name, field.GetTypeName())



if __name__ == "__main__":
    readMete()
