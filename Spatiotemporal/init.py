# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：init.py
@Author  ：Xin Zheng
@Date    ：2022/4/13 16:37 
'''

import Entity.RSData as RSImg
import os



if __name__ == "__main__":
    #根目录
    os.chdir(r"E:\code\python\geoprocessing\Spatiotemporal\Tests\Test_4")

    '''初始化数据'''
    #Landsat-like  time=T0
    pathFineResT0 = "L72000306_SZ_B432_30m.tif"
    fineResT0 = RSImg.RSData()
    fineResT0.readTIF(pathFineResT0)
    #Modis-like  time=T0
    pathCoarseResT0 = "MOD09_2000306_SZ_B214_250m.tif"
    coarseResT0 = RSImg.RSData()
    coarseResT0.readTIF(pathCoarseResT0)
    #Modis-like  time=T1
    pathCoarseResT1 = "MOD09_2002311_SZ_B214_250m.tif"
    coarseResT1 = RSImg.RSData()
    coarseResT0.readTIF(pathCoarseResT1)





