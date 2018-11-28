# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:46:16 2018

@author: yiching
"""
import os

from MyQR import myqr

thisDir = 'jade'
letter = 'A'
if not os.path.exists('qr'+thisDir):
    os.makedirs('qr'+thisDir)
    
file = open(thisDir + '/address.txt', 'r')
all_address = file.read()
address = all_address.split(',')

def createQR(path):
    i = 0
    for fname in os.listdir(path):
        print(str(path + fname))
        if(os.path.splitext(path + fname)[-1] == '.jpg'):
            left = fname.split('.')[0]
            num = left.split(letter)[1]
            version, level, qr_name = myqr.run(
            	address[int(num)-1],
                version=6,
                level='L',
                picture=path + fname,
                colorized=True,
                contrast=1.0,
                brightness=1.0,
                save_name='D:\\pythonWork\\qr'+thisDir+'\\'+fname + '.png',
                save_dir=os.getcwd()
            	)
            i+=1
        
createQR('D:/pythonWork/'+thisDir+'_new/')