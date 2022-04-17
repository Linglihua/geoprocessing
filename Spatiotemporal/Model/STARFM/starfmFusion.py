# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：starfmFusion.py
@Author  ：Xin Zheng
@Date    ：2022/4/6 15:06 
'''



import os
from Spatiotemporal.Entity.RSData import RSData
from ..STARFM.processing import Processing




class StarfmFusionModel:
    def __init__(self, pathFineResT0, pathCoarseResT0, pathCoarseResT1):
        self.pathFineResT0 = pathFineResT0
        self.pathCoarseResT0 = pathCoarseResT0
        self.pathCoarseResT1 = pathCoarseResT1

        pass

    def start(self):
        # 存储临时数据的文件夹
        pathTemFineResT0 = "Temporary/Tiles_fineRes_t0/"
        pathTemCoarseResT0 = "Temporary/Tiles_coarseRes_t0/"
        pathTemCoarseResT1 = "Temporary/Tiles_coarseRes_t1/"

        print("开始初始化数据")
        '''初始化数据'''
        # Landsat-like  time=T0
        #pathFineResT0 = "sim_Landsat_t1.tif"
        fineResT0 = RSData().readTIF(self.pathFineResT0)
        # Modis-like  time=T0
        #pathCoarseResT0 = "sim_MODIS_t1.tif"
        coarseResT0 = RSData().readTIF(self.pathCoarseResT0)
        # Modis-like  time=T1
        pathCoarseResT1 = "sim_MODIS_t4.tif"
        coarseResT1 = RSData().readTIF(self.pathCoarseResT1)

        print("开始分块并建立索引")
        '''分块并建立索引'''
        partitionFineResT0 = Processing().partitoin(fineResT0, pathTemFineResT0)
        partitionCoarseResT0 = Processing().partitoin(coarseResT0, pathTemCoarseResT0)
        partitionCoarseResT1 = Processing().partitoin(coarseResT1, pathTemCoarseResT1)
