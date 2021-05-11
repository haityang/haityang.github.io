# -*- coding: utf-8 -*-
import sys
import xdrlib
import xlrd
import os
import shutil
##########################################################
reload(sys)
sys.setdefaultencoding('utf-8')

##########################################################
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)

##########################################################
def main(argv):
    data = open_excel(sys.argv[1])
    if data:
        table = data.sheets()[0]
        colnames = table.row_values(0) #第一行数据
        colKeys = table.col_values(0) #第一列key数据
        nrows = len(colKeys) #总行数
        ncols = len(colnames) #总列数

        #语言列表
        languageList = []
        #国际化文件名列表
        fileNameList = []

        parent = os.path.dirname(os.path.realpath(__file__))
        dirPath =  parent + '/localize'
        if not os.path.exists(dirPath):
            os.mkdir(dirPath)

        for indexCol in range(1,ncols):
            list = []
            
            colValues = table.col_values(indexCol)
            fileNameList.append(colValues[0] + '.strings')
            for indexRow in range(1,nrows):
                
                value = colValues[indexRow]
                key = colKeys[indexRow]
    
                keyValue = '"' + key + '"' + ' = ' + '"' + value + '"' + ';\n'
                list.append(keyValue)

            languageList.append(''.join(list))

        for index in range(len(languageList)):
            fileName = dirPath + '/' + fileNameList[index]
            os.system(r'touch %s' % fileName)
            
            fp = open(fileName,'wb+')
            fp.write(languageList[index])
            fp.close()


    else :
                print "can not open file"

if __name__=="__main__":
    main(sys.argv[1])
