import os
import sys
from osgeo import ogr
import ospybook as pb
from ospybook.vectorplotter import VectorPlotter




def readShp():
    fn = r"E:\data\arcgis\osgeopy-data\osgeopy-data\global\ne_50m_populated_places.shp"
    ds = ogr.Open(fn, 0)         #打开数据源,
    if ds is None:
        sys.exit("Could nit open {0}:" .format(fn))

    layer = ds.GetLayer(0)   #获得数据层

    #遍历
    #layer中每个空间对象都是一个feature,在循环中获取每个对象的空间信息和属性信息
    i = 0
    for feature in layer:
        pt = feature.geometry()
        #获取坐标
        x = pt.GetX()
        y = pt.GetY()
        name = feature.GetField("NAME")     #通过GetField获取属性
        kind = feature.GetField("sov0name")
        print(name, kind, x, y)
        i += 1
        if i == 10:
            break

    #访问特定元素
    num_features = layer.GetFeatureCount() #获取要素个数
    last_feature = layer.GetFeature(num_features - 1)
    print("last_feature: ",last_feature.name)

    del ds

#使用ospybook
def ospybookTest():
    #查看相关属性
    fn = r"E:\data\arcgis\osgeopy-data\osgeopy-data\global\ne_50m_populated_places.shp"
    #pb.print_attributes(fn)   #查看全部,属性表存在空属性会报错，建议指定属性名称
    pb.print_attributes(fn, 3, ['NAME', 'FEATURECLA']) #查看前三个， 指定属性，geom为false不显示几何类型， reset为false为不重置到第一条
    #绘制
    os.chdir(r"E:\data\arcgis\osgeopy-data\osgeopy-data\global")   #更改文件目录，可直接使用目录下的文件
    vp = VectorPlotter(True)  #创建一个绘图板
    vp.plot('ne_50m_admin_0_countries.shp', fill = False)
    vp.plot('ne_50m_populated_places.shp', 'bo')
    vp.draw()



if __name__ == "__main__":
    #readShp()
    ospybookTest()