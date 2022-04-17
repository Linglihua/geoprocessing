# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：init.py
@Author  ：Xin Zheng
@Date    ：2022/4/13 16:37 
'''

import os
from Model.STARFM.starfmFusion import StarfmFusionModel




if __name__ == "__main__":
    #影像根目录
    os.chdir(r"E:\code\python\geoprocessing\Spatiotemporal\Tests\Test_3")
    #影像名称
    pathFineResT0 = "sim_Landsat_t1.tif"
    pathCoarseResT0 = "sim_MODIS_t1.tif"
    pathCoarseResT1 = "sim_MODIS_t4.tif"

    #初始化starfm模型并开始计算
    starFM = StarfmFusionModel(pathFineResT0, pathCoarseResT0, pathCoarseResT1)
    starFM.start()













