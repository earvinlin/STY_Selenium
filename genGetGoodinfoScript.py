"""
功能說明：
產生抓取Goodinfo網站資料的script

程式執行傳入參數說明：
取得資料種類：dividend / salemon
腳本執行平台：_win.bat (windows) / _imac.sh (imac) / _linux.sh (linux)
"""
from datetime import datetime
import sys
import os 
import time

insertCnt = 0 
isFirstLine = True

try:
	print("[genGetGoodinfoScript.py] 開始執行時間：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

	if len(sys.argv) < 5 :
		print("You need input two parameter(fmt : 取得資料種類 腳本執行平台 theStockCode theDate)")
		print("syntax : C:\python FormatStocksSaleMonData.py dividend imac 2002 20220420")
		sys.exit()

	thePython = "python"
	theDataType = sys.argv[1]
	thePlatform = sys.argv[2]
	theProgram = sys.argv[3]
	theDate = sys.argv[4]  
	inputFileName = "STOCKS_LIST.txt"
	
	outputFileName = ""
	if theDataType == "_win" :
		outputFileName = "_get_" + theDataType + thePlatform + ".bat"
	elif theDataType == "_imac" :
		outputFileName = "_get_" + theDataType + thePlatform + ".sh"
	else :
		outputFileName = "_get_" + theDataType + thePlatform + ".sh"
	
	outfile = open(outputFileName, 'w')

	inputFile = open(inputFileName, 'r')
	for line in inputFile:
		theStockNoA = line
		theOutputString = thePython + theProgram + outputFileName + theStockNoA + theDate
		outfile.write(");\n")



	outfile.close()
	
except IOError as err :
	print('File error : ' + str(err))

print("資料處理完成!! 共 " + str(insertCnt) + " 筆。")
print("[genGetGoodinfoScript.py] 結束執行時間：" + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

