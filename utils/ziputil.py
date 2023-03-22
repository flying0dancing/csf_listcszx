import zipfile
'''
@return the file names in zip file
'''
def getNamesOfZipFile(zipFile):
    nameList=[]
    zip_file=zipfile.ZipFile(zipFile)
    if zipfile.is_zipfile(zipFile):
        for name in zip_file.namelist():
            nameList.append(name)
    zip_file.close()
    return nameList

'''
@return True if the file satisfied the identicators
'''
def filterZipFile(file,identicators):
    if identicators is None:
        return True
    flag=False
    try:
        zip_file = zipfile.ZipFile(file)
        if zipfile.is_zipfile(file):
            for name in zip_file.namelist():
                if name in identicators:
                    flag=True
                    break
        zip_file.close()
    except zipfile.BadZipFile as e:
        print('bad zip file {0}',file)
    return flag

def getRefsFromZipFile(zipFile,acqCatalogsDict):
    acqIdentifiers=[]
    zip_file=zipfile.ZipFile(zipFile)
    if zipfile.is_zipfile(zipFile):
        for name in zip_file.namelist():
            name_lower=name.lower()
            if 'multiviews_' in name_lower and '.bin' in name_lower:
                #test.log(name)
                catalogId=name_lower.replace('.bin','').replace('multiviews_','')

                catalogStr=acqCatalogsDict.get(catalogId)
                if catalogId in acqCatalogsDict.keys() and catalogStr not in acqIdentifiers:
                    acqIdentifiers.append(catalogStr)
            # if 'shadeLibraries.bin' in name.lower():
            #     acqIdentifiers.append('shade')

    return acqIdentifiers

