#conding=utf8
from myConfig import *
from myUtils import *
import xml.etree.ElementTree as ET
import os
from transform import *


def getSign(s1, s2, sign):
    list1 = path(getInfo(s1))
    list2 = unbeautifySmooth(path(getInfo(s2)))
    if len(list1)!=len(list2):
        return sign
    a = -1
    b = -1
    num = int(s1.split('_')[0].split('/')[-1])
    mp = {}
    for i in range(len(list1)):
        if list1[i][0] == 'q':
        	if list2[i][0] != 'q':
        		continue
        	dx = int(list1[i][3])
        	dy = int(list1[i][4])
        	ddx = int(list2[i][1]) - int(list1[i][1]) - 1
        	ddy = int(list2[i][2]) - int(list1[i][2]) - 1
        	if (dx // alpha) != 0:
        		a = ddx / (dx // alpha)
        	if (dy // alpha) != 0:
        		b = ddy / (dy // alpha)
    n = (len(sign) / 2)
    if a != -1:
        sign[int(num % n)] = hex(int(a))[2:]
    if (b != -1):
        sign[int(num % n + n)] = hex(int(b))[2:]
    if sign[35]=='6':
        print(s1,s2)
    return sign



def oneByoneGetAllSign(sign,filename):
    inPath=svg_path+'/'+filename
    outPath=svg_ver_path+'/'+filename
    tree = ET.parse(outPath)
    root = tree.getroot()
    if ('d' not in root[0].attrib.keys()):
        return -1    #num
    getSign(inPath,outPath,sign)
    if (sign.count("?") == 0):  #TODO maybe after
        return ''.join(sign) #str
    else:
        return sign #list
