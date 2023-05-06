import os
import pydicom
import re

def readDicom():
    folder_path=r'C:\ProgramData\DEXIS IS\ScanFlow\data\20230328_1.2.528.56.1005.202303281335082956875216'
    file_name='85e2399e-b6f0-491a-b897-e6324629ca01_Orthodontics.dcm'
    file_path=os.path.join(folder_path,file_name)
    ds=pydicom.dcmread(file_path,force=True)
    print(ds.get(0x00080070))
    print(ds.get(0x00081090).name) #Manufacturer's Model Name
    print(ds.get(0x00081090).value) #IS 3800
    #  [0008,1090] 	LO	8 	Manufacturer's Model Name	CS 3600
    #  [0010,0010] 	PN	8 	Patient's Name	l2^f2^m2
    print(ds.get(0x00100010))
    print(ds.get(0x00100010).name)
    print(ds.get(0x00100010).value)
    brief_patientname=str(ds.get(0x00100010).value)
    print(brief_patientname.replace("^","_"))
    #TODO

def getBriefPatientNameFromDicom(fname):
    brief_patientname='dcm_notfile'
    if fname!='' and os.path.isfile(fname) :
        ds = pydicom.dcmread(fname, force=True)
        patientname = str(ds.get(0x00100010).value)
        matchX=re.match(r'^(\w*)\^(\w*)\^.*',patientname)
        if matchX:
            #print('matchX.group()',matchX.group())
            #print('matchX.group()', matchX.group(1))
            #print('matchX.group()', matchX.group(2))
            brief_patientname = matchX.group(2)[0] + matchX.group(1)[0]
        else:
            #print('no match')
            brief_patientname='dcm_notmatch'

    #print(brief_patientname)
    return brief_patientname




if __name__=='__main__':
    #readDicom()
    folder_path = r'C:\ProgramData\DEXIS IS\ScanFlow\data\20230328_1.2.528.56.1005.202303281335082956875216\85e2399e-b6f0-491a-b897-e6324629ca01_Orthodontics.dcm'
    file_name = '85e2399e-b6f0-491a-b897-e6324629ca01_Orthodontics.dcm'
    getBriefPatientNameFromDicom(folder_path)
