import os
import shutil
try:
    import xml.etree.cElementTree as et
except ImportError:
    import xml.etree.ElementTree as et

xmlFile = r'C:\ProgramData\DEXIS IS\ScanFlow\preference.xml'

def getSetting(xmlfile,sectionname,tagname,attrdict):
    tree=et.parse(xmlfile)
    root = tree.getroot()
    flag = False
    result=''
    for classChild in root:
        if classChild.attrib=={'key': sectionname}:
            for child in classChild:
                if child.tag == tagname and child.attrib['key']==attrdict['key']:
                    result=str(child.attrib['value'])
                    print(child.attrib['key']+': '+result)
                    flag=True
                    break
        if flag==True:
            break

    return result

def getVideoFolder():
    return getSetting(xmlFile,'GENERAL','option',{'key': 'AUTO_SAVE_VIDEO_FOLDER'})

def getRawDataFolder():
    flag=getSetting(xmlFile, 'GENERAL', 'option', {'key': 'INSTALLATION_TYPE'})
    if flag=='1':
        result=getSetting(xmlFile, 'GENERAL', 'option', {'key': 'AUTO_SAVE_CSZ_FOLDER'})
    else:
        if flag=='2':
            result=getSetting(xmlFile, 'GENERAL', 'option', {'key': 'PATIENT_DATA_PATH'})
    print(result)
    return result

if __name__=='__main__':
    getSetting(xmlFile, 'GENERAL','option', {'key': 'AUTO_SAVE_VIDEO_FOLDER'})
    getSetting(xmlFile, 'GENERAL', 'option', {'key': 'AUTO_SAVE_VIDEO'}) #true
    getSetting(xmlFile, 'GENERAL', 'option', {'key': 'AUTO_SAVE_CSZ'}) #true
    getSetting(xmlFile, 'GENERAL', 'option', {'key': 'AUTO_SAVE_CSZ_FOLDER'})
    getSetting(xmlFile, 'GENERAL', 'option', {'key': 'PATIENT_DATA_PATH'})
    getSetting(xmlFile, 'GENERAL', 'option', {'key': 'INSTALLATION_TYPE'})

    '''
    standalone
AUTO_SAVE_VIDEO_FOLDER: C:\ProgramData\DEXIS IS\ScanFlow\video2\
AUTO_SAVE_VIDEO: true
AUTO_SAVE_CSZ: true
AUTO_SAVE_CSZ_FOLDER: C:\ProgramData\DEXIS IS\ScanFlow\data2\
PATIENT_DATA_PATH: D:\patient_data
INSTALLATION_TYPE: 2

    integrated:DTX
AUTO_SAVE_VIDEO_FOLDER: C:\ProgramData\DEXIS IS\ScanFlow\video2\
AUTO_SAVE_VIDEO: true
AUTO_SAVE_CSZ: true
AUTO_SAVE_CSZ_FOLDER: C:\ProgramData\DEXIS IS\ScanFlow\data2\
PATIENT_DATA_PATH: D:\patient_data
INSTALLATION_TYPE: 1
    '''