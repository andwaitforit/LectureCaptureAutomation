# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 13:26:12 2018

@author: ahorgan
"""
 
from datetime import datetime
import os, re, csv  
    
def courseReturn(name, recTime, day):
    with open('U:/projects/pythonspring20test/COURSE COUNTS 20SP.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if name in row:
                endTime = int((row[20])[8:10])
                if endTime == recTime -1 or endTime == recTime + 1 or endTime == recTime:
                    if day in row[19]:
                        return(row[4])                 

def main():
    scriptDir = os.getcwd()
    for file in os.listdir(scriptDir):
        try:
            
            if file.endswith('.mp4'):
                fileNameStrip = re.sub(r'\d+', '', file.split("_", 1)[0])
                fileNaming = fileNameStrip[0].upper() + fileNameStrip[1:].capitalize()
                fileSearch = fileNameStrip[1].upper() + fileNameStrip[2:]+ ", " + fileNameStrip[0].upper()
                filePath = os.path.realpath(file)
                
                fileTime = datetime.fromtimestamp(os.path.getmtime(filePath))
                days = ["M", "T", "W", "TH", "F", "SAT", "SUN"]
                day = days[fileTime.weekday()]
                recTime = int(fileTime.strftime("%H"))
                fileDate = fileTime.strftime("%b%d%Y")
                if recTime > 12:
                    recTime = recTime - 12
                course = courseReturn(fileSearch, recTime, day)
                newFileName = fileNaming + "_" + re.sub(r'-', '', course)+ "_" + fileDate
                os.rename(file, newFileName + ".mp4")

        except:
            print("Not a file")

      
main()
