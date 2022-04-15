# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：Entity.py
@Author  ：Xin Zheng
@Date    ：2022/4/12 22:01 
'''

import os
from osgeo import gdal

'''
遥感数据的对象类
读取、写出
'''
class RSData:

    def __init__(self):

        pass

    def readTIF(self, pathRSImg):
        self.pathRSImg = pathRSImg
        '''打开波段x'''
        self.rsdata = gdal.Open(self.pathRSImg)
        self.in_band = self.rsdata.GetRasterBand(1)
        pass


    def writeFIF(self):

        pass