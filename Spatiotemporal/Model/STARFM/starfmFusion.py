# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：starfmFusion.py
@Author  ：Xin Zheng
@Date    ：2022/4/6 15:06 
'''

import dask.array as dask
import numpy as np
import zarr
from dask.diagnostics import ProgressBar
from parameters import (windowSize, path)

class starfmFusionModel:
    def __init__(self):

        pass

    ''' '''
    def partitoin(self, image, folder):
        #对array进行分块and填充
        imageDask = dask.from_array(image, chunks = (windowSize, image.shape[1]))
        imagePad = dask.pad(imageDask, windowSize//2, mode="constant")

        for i in range(windowSize):
            row = str(i)
            block_i = imagePad[i:,:]  #i-n行，所有列
            block_iDask = dask.rechunk(block_i, chunks = (windowSize, imagePad.shape[1]))
            block_iDask.map_blocks(self.__blockToRow, dtype = int, row = row, folder = folder).compute()

        pass

    '''将 数据块 展开'''
    def __blockToRow(self, array, row, folder, blockId=None):
        if array.shape[0] == windowSize:
            nameString = str(blockId[0] + 1)
            m,n = array.shape
            u = m + 1 - windowSize
            v = n + 1 - windowSize

            # 开始的的索引
            startIndices = np.arange(u)[:, None]*n + np.arange(v)

            #获得偏移量索引
            offsetIndices = np.arange(windowSize)[:, None]*n + np.array(windowSize)

            #获得所有的索引并输入、
            flatArray = np.take(array, startIndices.ravel()[:, None] + offsetIndices.ravel())

            #以.zarr格式存储
            fileName = path + folder + nameString + 'r' + row + '.zarr'
            zarr.save(fileName, flatArray)
        pass