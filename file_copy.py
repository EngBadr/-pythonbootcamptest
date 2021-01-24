#writen By Badr Alharbi For SEU Python Bootcamp
import os
import datetime
wrk_dir=os.path.dirname(__file__)
newContents=[]
def fileCopy():
    try:    
            sourceFile=open(wrk_dir+'/source.txt')            
            i=0
            timeNow=datetime.datetime.now()
            fDay=timeNow.strftime('%d')+'_'
            fmnt=timeNow.strftime('%m')+'_'
            fyr=timeNow.strftime('%Y')+'_'
            fTime=timeNow.strftime('%X')
            fTime=fTime.replace(':','_')

            dirName=wrk_dir+'/'+fDay+fmnt+fyr+fTime
            if not os.path.exists(dirName):
                os.makedirs(dirName)
            destFile=open(dirName+'/'+'destenation.txt','w')
            for lines in sourceFile:
                destFile.write(str(i+1)+': '+lines)
                newContents.append(lines.strip('\n'))
                i+=1
            
            print(newContents)
            
    except:
       print('Somthing goes wrong or srouce file doesn\'t')
    else:
        print('File successfuly copied!')

fileCopy()
