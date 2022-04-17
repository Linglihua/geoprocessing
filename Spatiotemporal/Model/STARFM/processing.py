# -*- coding: UTF-8 -*-
'''
@Project ：geoprocessing 
@File    ：processing.py
@Author  ：Xin Zheng
@Date    ：2022/4/16 22:22 
'''

import dask.array as dask
import numpy as np
import zarr
from dask.diagnostics import ProgressBar
from ..STARFM.parameters import (windowSize, path)

class Processing:
    def __init__(self):

        pass

    ''' '''
    def partitoin(self, image, folder):
        #对array进行分块and填充
        imageDask = dask.from_array(image, chunks = (windowSize, image.shape[1])) #按照windowSize大小按列分
        imagePad = dask.pad(imageDask, windowSize//2, mode="constant") #对边缘进行填充

        #目的是让影像上部边缘部分也能被计算到
        for i in range(windowSize):
            row = str(i)
            print(i)
            block_i = imagePad[i:,:]  #i-n行，所有列
            block_iDask = dask.rechunk(block_i, chunks = (windowSize, imagePad.shape[1]))
            block_iDask.map_blocks(self.__blockToRow, dtype = int, row = row, folder = folder).compute()

        pass

    '''将 数据块 展开   获取索引值'''
    def __blockToRow(self, array, row, folder, block_id=None):
        if array.shape[0] == windowSize:
            nameString = str(block_id[0] + 1)
            m,n = array.shape
            u = m + 1 - windowSize
            v = n + 1 - windowSize

            # 开始的的索引
            startIndices = np.arange(u)[:, None]*n + np.arange(v)   #None追加一层维度

            #获得偏移量索引      获得每个数据块各个像素的位置索引(下标)
            offsetIndices = np.arange(windowSize)[:, None]*n + np.arange(windowSize)

            #获得所有的索引并输入 take表示按照索引取值
            # a.take(m,1)表示取每一行的第m个值，即m列；a.take(m,0)表示取第m行
            #.ravel()将数组多维度拉成一维数组
            #该步骤获得了横向，纵向所有的移动窗口中像素的索引
            flatArray = np.take(array, startIndices.ravel()[:, None] + offsetIndices.ravel())

            #以.zarr格式存储
            fileName = path + folder + nameString + 'r' + row + '.zarr'
            zarr.save(fileName, flatArray)

        return array
        pass