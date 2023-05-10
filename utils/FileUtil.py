import os.path, re
import datetime,logging
from utils import ZipUtil, Logger, DicomUtil, XmlUtil
from utils.AcronymCatalogs import AcronymCatalogs

logger=logging.getLogger('utils.fileutil')
'''
@return files total size.
'''
@DeprecationWarning
def traverseFolder(searchFolder,identicators, list1,list0):
    size=0
    starttime = datetime.datetime.now()
    subFiles=os.listdir(searchFolder)

    for subFile in subFiles:
        subFullName = os.path.join(searchFolder, subFile)
        if os.path.isdir(subFullName):
            size += traverseFolder(subFullName,identicators,list1,list0)
        else:
            if subFile.endswith('.cszx') and ZipUtil.filterZipFile(subFullName,identicators):
                algoFile=os.path.splitext(subFile)[0]+'_records.zip'
                algoFullName=os.path.join(searchFolder,algoFile)
                print(subFullName+" "+str(round(os.path.getsize(subFullName)/1024/1024,2)))
                size += round(os.path.getsize(subFullName)/1024/1024,2)
                if os.path.isfile(algoFullName):
                    size += round(os.path.getsize(algoFullName)/1024/1024,2)
                    print(algoFullName + " " + str(round(os.path.getsize(algoFullName) / 1024 / 1024, 2)))
                    list1.append(subFullName)
                else:
                    list0.append(subFullName)
    endtime = datetime.datetime.now()
    print("search folder {} used time {} ms".format(searchFolder, round((endtime - starttime).microseconds / 1000, 2)))
    return size

'''
@return files total size.
'''
@DeprecationWarning
def traverseFolder1(searchFolder, identicators, list1, list0):
    size = 0
    starttime = datetime.datetime.now()
    for root,dirs,files in os.walk(searchFolder):
        for name in dirs:
            pass
            #print('-'*8+'dir'+'-' * 8 )
            #file_name=os.path.join(root,name)
        for name in files:
            #print('-' * 8 + 'file'+'-' * 8 )
            file_name=os.path.join(root,name)
            mask = oct(os.stat(file_name).st_mode)[-3:]
            #print("File permission mask:", (mask,file_name))
            if str(mask)!=str(666):
                continue
            if name.endswith('.cszx') and ZipUtil.filterZipFile(file_name, identicators):
                algoFile = find_algo_name(root, os.path.splitext(name)[0], '_records.zip')
                if algoFile is None:
                    list0.append(file_name)
                else:
                    print(file_name + " " + str(round(os.path.getsize(file_name) / 1024 / 1024, 2)))
                    print(algoFile + " " + str(round(os.path.getsize(algoFile) / 1024 / 1024, 2)))
                    size += round(os.path.getsize(file_name) / 1024 / 1024, 2)
                    size += round(os.path.getsize(algoFile) / 1024 / 1024, 2)
                    list1.append(file_name)


    endtime = datetime.datetime.now()
    print("search folder {} used time {} ms".format(searchFolder,round((endtime - starttime).microseconds/1000,2)))
    return size
@DeprecationWarning
def traverse_cszxFolder(searchFolder,searchStartDate,searchEndDate, dict):
    size = 0
    starttime = datetime.datetime.now()
    for root,dirs,files in os.walk(searchFolder):
        for name in dirs:
            pass
        for name in files:
            file_name=os.path.join(root,name)
            mask = oct(os.stat(file_name).st_mode)[-3:]

            if str(mask)!=str(666):
                continue
            if name.endswith('.cszx'):#and ziputil.filterZipFile(file_name, identicators)
                key = generate_foldername(name).lower() #TODO expand
                if key =='':
                    continue
                created = getDateByFileSuffix(name) #TODO expand
                if created <= searchEndDate and created >= searchStartDate:
                    pass
                else:
                    #file is out of searched date
                    continue
                identifierStr = str.join('_', ZipUtil.getRefsFromZipFile(file_name, AcronymCatalogs.acqCatalogs()))
                # if identifierStr=='':
                #      continue
                print("folder:{}".format(key))
                print("  identifier:{}".format(identifierStr))
                newname = generate_cszxname(name, identifierStr).lower()
                print("  newname:{}".format(newname))
                print("  created:{}".format(created))
                name_size = round(os.path.getsize(file_name) / 1024 / 1024, 2)
                size += name_size
                print("  fullpath: {}, size: {} MB".format(file_name,name_size))
                algoFile = find_algo_name(root, os.path.splitext(name)[0], '_records.zip')
                if algoFile is None:
                    appendToDict(dict, key, newname)
                else:
                    algo_name = os.path.basename(algoFile)
                    algo_newname = generate_newname_with_acronyn(algo_name).lower()
                    print("  newname:{}".format(algo_newname))
                    name_size = round(os.path.getsize(algoFile) / 1024 / 1024, 2)
                    size += name_size
                    print("  fullpath: {}, size: {} MB".format(algoFile, name_size))
                    appendToDict(dict, key, newname,algo_newname)
    endtime = datetime.datetime.now()
    print("search folder {} used time {} ms".format(searchFolder,round((endtime - starttime).microseconds/1000,2)))
    return size
@DeprecationWarning
def traverse_videoFolder(searchFolder,searchStartDate,searchEndDate, dict):
    size = 0
    starttime = datetime.datetime.now()
    for root, dirs, files in os.walk(searchFolder):
        for name in dirs:
            pass
        for name in files:
            file_name = os.path.join(root, name)
            mask = oct(os.stat(file_name).st_mode)[-3:]
            if str(mask) != str(666):
                continue
            if name.endswith('.mp4'):
                key = generate_foldername(name).lower()
                if key =='':
                    continue
                created=getDateByFileSuffix(name)
                if created<=searchEndDate and created>=searchStartDate:
                    pass
                else:
                    continue
                newname=generate_newname_with_acronyn(name).lower()
                print("folder:{}".format(key))
                print("  newname:{}".format(newname))
                print("  created:{}".format(created))
                name_size=round(os.path.getsize(file_name) / 1024 / 1024, 2)
                size += name_size
                print("  fullpath: {}, size: {} MB".format(file_name,name_size))
                appendToDict(dict,key,newname)
    endtime = datetime.datetime.now()
    print("search videoFolder {} used time {} ms".format(searchFolder, round((endtime - starttime).microseconds / 1000, 2)))
    return size

@DeprecationWarning
def traverse_cszxmp4zip(searchFolder, suffix, dict):
    size = 0
    starttime = datetime.datetime.now()
    for root,dirs,files in os.walk(searchFolder):
        for name in dirs:
            pass
        for name in files:
            file_name=os.path.join(root,name)
            mask = oct(os.stat(file_name).st_mode)[-3:]

            if str(mask)!=str(666):
                continue
            if name.endswith(suffix):#and ziputil.filterZipFile(file_name, identicators)
                key = generate_foldername(name)
                print(key+" "+file_name + " " + str(round(os.path.getsize(file_name) / 1024 / 1024, 2)))
                size += round(os.path.getsize(file_name) / 1024 / 1024, 2)
                appendFileToDict(dict, key.lower(), file_name.lower())
    endtime = datetime.datetime.now()
    print("search {} folder {} used time {} ms".format(suffix,searchFolder,round((endtime - starttime).microseconds/1000,2)))
    return size

@DeprecationWarning
def verifyResult1(searchFolder,dict):#using with traverse_videoFolder() traverse_cszxFolder()
    starttime = datetime.datetime.now()
    files = os.listdir(searchFolder)
    passcount=0
    failcount=0
    missscount=0
    filecount=0
    size=0
    for name in files:
        file_name = os.path.join(searchFolder, name)
        if os.path.isdir(file_name):
            list_ver=dict.get(name.lower())
            if list_ver is None:
                logger.info('fail: folder {} is not covered in testing scope.'.format(name))
                #missscount=missscount+1
            else:
                logger.info('[{}]'.format(name))
                subfiles=os.listdir(file_name)
                for subfile in subfiles:
                    subfile_name=os.path.join(file_name, subfile)
                    if os.path.isfile(subfile_name):
                        name_size = round(os.path.getsize(subfile_name) / 1024 / 1024, 2)
                        size += name_size
                        filecount+=1
                        subfile_lower=subfile.lower()
                        if subfile_lower in list_ver:
                            logger.info('pass: {}'.format(subfile))
                            list_ver.remove(subfile_lower)
                            passcount=passcount+1
                        else:
                            logger.info('fail: {} not covered in testing scope, details: full name:{}'.format(subfile, subfile_name))
                            missscount = missscount + 1
                dict[name]=list_ver
        else:
            logger.info('fail: folder{} is not covered in testing scope.'.format(name))
            #missscount = missscount + 1
    for k, v in dict.items():
        for value in v:
            logger.info("fail:miss {} in [{}]".format(value,k))
            failcount = failcount + 1
    endtime = datetime.datetime.now()
    logger.info("verify folder {} total files:{}, size: {} MB, used time {} ms".format(searchFolder,filecount, round(size,2),
                                                    round((endtime - starttime).microseconds / 1000, 2)))
    logger.info("verify totoal:{}, pass:{}, fail:{}, miss:{}".format(passcount+failcount+missscount,passcount,failcount,missscount))
    return (passcount,failcount,missscount, size)


@DeprecationWarning
def appendFileToDict(dict, key,value):
    list_exist = dict.get(key)
    if list_exist is None:
        dict[key] = [value]
    else:
        if value not in list_exist:
            list_exist.append(value)
        dict[key] = list_exist

@DeprecationWarning
def appendToDict(dict, key,*values):
    list_exist=dict.get(key)
    if list_exist is None:
        dict[key] = list(values)
    else:
        for value in values:
            if value not in list_exist:
                list_exist.append(value)
        dict[key]=list_exist

@DeprecationWarning
def generate_cszxname(fname,identifierStr):
    pics_fname=os.path.splitext(fname)
    result = pics_fname[0]
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',1)
        if identifierStr=='':
            result = acronyn_name(fname) + '[' + pics_f[1] + pics_fname[1]
        else:
            result=acronyn_name(fname)+'['+pics_f[1]+"_"+identifierStr+pics_fname[1]
    return result
@DeprecationWarning
def generate_newname_with_acronyn(fname):
    pics_fname=os.path.splitext(fname)
    result = pics_fname[0]
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',1)
        result=acronyn_name(fname)+'['+pics_f[1]+pics_fname[1]
    return result
@DeprecationWarning
def acronyn_name(fname): #get First_Last return FL
    result = ''
    pics_fname = os.path.splitext(fname)
    if '[' in pics_fname[0]:
        pics_f = pics_fname[0].split('[', 1)
        if '_' in pics_f[0] and len(pics_f[0])>=3:
            pics_p = pics_f[0].split('_')
            result = pics_p[0][0] + pics_p[1][0]
    return result

@DeprecationWarning
def generate_foldername(fname): #FL_YYYYMMDD
    pics_fname=os.path.splitext(fname)
    result = pics_fname[0]
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',2)
        dateStr = pics_f[1].replace('-','')
        result=acronyn_name(fname)+'_'+dateStr[:8]
    else:
        result=''
    return result

@DeprecationWarning
def find_algo_name(fpath,prefix,suffix):
    falgo=None
    files=os.listdir(fpath)
    for fl in files:
        if prefix in fl and suffix in fl:
            falgo=os.path.join(fpath, fl)
            break
    return falgo

'''
return None if the fname doesn't match cszx/mp4's name rule
'''

def getDateByFileSuffix(fname):
    pics_fname = os.path.splitext(fname)
    #print(pics_fname[0])
    if pics_fname[1]=='.mp4':
        format="%Y%m%d%H%M%S%f"
    else:
        format = "%Y-%m-%dT%H-%M-%S"
    if '[' in pics_fname[0]:
        pics_f = pics_fname[0].split('[', 2)
        datetime_str = pics_f[1].replace(']','')
        if 'T' in datetime_str:
            format = "%Y-%m-%dT%H-%M-%S"
        datetime_result=datetime.datetime.strptime(datetime_str,format).date()
    else:
        datetime_result=None
    return datetime_result


@DeprecationWarning
def getTimeByName(fname,format="%Y-%m-%dT%H-%M-%S"):
    pics_fname = os.path.splitext(fname)
    print(pics_fname[0])
    if '[' in pics_fname[0]:
        pics_f = pics_fname[0].split('[', 2)
        datetime_str = pics_f[1].replace(']','')
        print(datetime_str)
        #format="%Y-%m-%dT%H-%M-%S"
        datetime_result=datetime.datetime.strptime(datetime_str,format)
        print(datetime_result)
        print(type(datetime_result))
    return datetime_result
@DeprecationWarning
def getDateByName(fname,format="%Y-%m-%dT%H-%M-%S"):
    pics_fname = os.path.splitext(fname)
    #print(pics_fname[0])
    if '[' in pics_fname[0]:
        pics_f = pics_fname[0].split('[', 2)
        datetime_str = pics_f[1].replace(']','')
        #print(datetime_str)
        #format="%Y-%m-%dT%H-%M-%S"
        datetime_result=datetime.datetime.strptime(datetime_str,format)
        #print(datetime_result.date())
        #print(type(datetime_result))
    return datetime_result.date()
@DeprecationWarning
def generate_cszxname_bak(fname,identifierStr=''):
    result=fname
    pics_fname=os.path.splitext(fname)
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',1)
        if '_' in pics_f[0]:
            pics_p=pics_f[0].split('_')
            result=pics_p[0][0]+pics_p[1][0]+'['+pics_f[1]+identifierStr
    return result
@DeprecationWarning
def generate_foldername_bak(fname):
    result=fname
    pics_fname=os.path.splitext(fname)
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',2)
        dateStr = pics_f[1].split('T')[0]
        if '_' in pics_f[0]:
            pics_p=pics_f[0].split('_')
        result=pics_p[0][0]+pics_p[1][0]+dateStr
    return result


def searchDcmByUID(fname):
    result=''
    fname=os.path.basename(fname) #1.2.528.56.1005.202303281335082956875216.cszx
    pics_fname = os.path.splitext(fname) #[1.2.528.56.1005.202303281335082956875216,.cszx]

    if pics_fname[1].lower()=='.zip':
        key=pics_fname[0].lower().replace('_records','')
    else:
        key=pics_fname[0]

    Scanflow_UserData=XmlUtil.getRawDataFolder()
    files = os.listdir(Scanflow_UserData)

    for name in files:
        flag=False
        sub_file = os.path.join(Scanflow_UserData, name)
        if os.path.isdir(sub_file) and name.lower().endswith(key):

            dicom_files=os.listdir(sub_file)
            for dicom_name in dicom_files:
                if dicom_name.endswith('.dcm'):
                    result=os.path.join(sub_file, dicom_name)
                    flag=True
                    break
        if flag==True:
            break
    #print(result)
    return result
def identifyFile(fname,searchStartDate,searchEndDate):
    folder_name=''
    patientname = None
    brief_patientname=None
    created=None
    format = "%Y%m%d%H%M%S"
    matchX=re.match(r'^\d\.\d\.\d{3,}\.\d{2,}\.\d{4,}\.(\d{8})(\d{6})\d*.*\.(cszx?|mp4|zip)$',fname,re.IGNORECASE) # 1.2.528.56.1005.202303281335082956875216.cszx
    if matchX:
        dateStr=matchX.group(1)
        created = datetime.datetime.strptime(dateStr+matchX.group(2), format).date()
        if created <= searchEndDate and created >= searchStartDate:
            dicomfullname = searchDcmByUID(fname)
            brief_patientname = DicomUtil.getBriefPatientNameFromDicom(dicomfullname).lower()
            folder_name = dateStr + '_' + brief_patientname
        else:
            logger.info('file name[{}] is out of searched date, please check.'.format(fname))
    else:
        matchX1=re.match(r'^(.*)_(.*)\[(\d{4}-?\d{2}-?\d{2})T?(\d{2}-?\d{2}-?\d{2}).*\].*\.(cszx?|mp4|zip)$',fname,re.IGNORECASE|re.UNICODE) #UserStory_AI[2023-04-18T17-15-14][1.0.9.201][Res].cszx
        if matchX1:
            dateStr=matchX1.group(3).replace('-','')
            created = datetime.datetime.strptime(dateStr + matchX1.group(4).replace('-', ''), format).date()
            if created <= searchEndDate and created >= searchStartDate:
                patientname=matchX1.group(1) + '_' + matchX1.group(2)
                brief_patientname = matchX1.group(1)[0] + matchX1.group(2)[0]
                folder_name = dateStr + '_' + brief_patientname
            #else:
                #logger.info('file name[{}] is out of searched date, please check.'.format(fname))
        #else:
            #logger.info('file name[{}] is no match regular format, please check.'.format(fname))
    #print('folder_name', folder_name)
    #print('date_created', created)
    #return [folder_name,created,patientname,brief_patientname]
    return {'key':folder_name,'created':created,'patient_name':patientname,'brief_patient_name':brief_patientname}



def generate_newname(fname,patientname,brief_patientname,identifierStr):
    if patientname is not None:
        newname=fname.replace(patientname,brief_patientname)
    else:
        newname=brief_patientname+'_'+fname
    pics_fname=os.path.splitext(newname)
    extension = pics_fname[1]
    if extension == '.cszx' and identifierStr!='':
        newname=pics_fname[0] + '_' + identifierStr + extension
    #print("newname:",newname)
    return newname.lower()

def traverse_Folder(searchFolder,searchStartDate,searchEndDate, dict):
    size = 0
    starttime = datetime.datetime.now()
    for root,dirs,files in os.walk(searchFolder):
        for name in dirs:
            pass
        for name in files:
            file_name=os.path.join(root,name)
            mask = oct(os.stat(file_name).st_mode)[-3:]

            if str(mask)!=str(666):
                continue
            identify_result=identifyFile(name.lower(),searchStartDate,searchEndDate) #{'key':folder_name,'created':created,'patient_name':patientname,'brief_patient_name':brief_patientname}
            key = identify_result['key']
            if key =='':
                continue
            else:
                identifierStr=''
                if name.endswith('.cszx'):
                    identifierStr = str.join('_', ZipUtil.getRefsFromZipFile(file_name, AcronymCatalogs.acqCatalogs()))
                print("folder: {}".format(key))
                print("  identifier: {}".format(identifierStr))
                print("  created: {}".format(identify_result['created']))
                newname = generate_newname(name.lower(),identify_result['patient_name'],identify_result['brief_patient_name'],identifierStr)
                print("  patient name: {}".format(identify_result['patient_name']))
                print("  brief patient name: {}".format(identify_result['brief_patient_name']))
                print("  newname: {}".format(newname))

                name_size = round(os.path.getsize(file_name) / 1024 / 1024, 2)
                size += name_size
                print("  origin file: {}, size: {} MB".format(file_name,name_size))
                appendDictToDict(dict, key, {newname:name_size})
    endtime = datetime.datetime.now()
    print("search folder {} used time {} ms".format(searchFolder,round((endtime - starttime).microseconds/1000,2)))
    return size

def appendDictToDict(dict, key,values):
    sub_exist_dict=dict.get(key)
    if sub_exist_dict is None:
        dict[key] = values
    else:
        for k,v in values.items():
            if k not in sub_exist_dict.keys():
                sub_exist_dict[k]=v
                #dict[key] = sub_exist_dict

def verifyResultFolderCount(searchFolder):
    logger.info('')
    logger.info('=' * 10 + 'start printing actual result' + '=' * 10)
    filecount = 0
    starttime = datetime.datetime.now()
    for root, dirs, files in os.walk(searchFolder):
        if dirs:
            logger.info('-' * 8 + 'folders' + '-' * 8)
            for name in dirs:
                logger.info("[{}]".format(name))
            logger.info('')
        if files:
            logger.info('-' * 15 + 'files' + '-' * 15)
            for name in files:
                filecount=filecount+1
                logger.info("    {} file:{}".format(filecount, name))
    endtime = datetime.datetime.now()
    logger.info("actual result folder {} (contains files {}) used time {} ms".format(searchFolder, filecount, round((endtime - starttime).microseconds / 1000, 2)))
    logger.info('=' * 10 + 'end printing actual result' + '=' * 10)
    logger.info('')
    return filecount


def verifyResult(searchFolder,dict):
    starttime = datetime.datetime.now()
    files = os.listdir(searchFolder)
    passcount=0
    failcount=0
    missscount=0
    filecount=0
    size=0
    for name in files:
        name=name.lower()
        file_name = os.path.join(searchFolder, name)
        #name=name.lower()
        if os.path.isdir(file_name):
            expected_sub_dict=dict.get(name)
            if expected_sub_dict is None:
                logger.info('  fail: folder {} is not covered in testing scope.'.format(name))
                #missscount=missscount+1
            else:
                logger.info('[{}]'.format(name))
                subfiles=os.listdir(file_name)
                for subfile in subfiles:
                    subfile=subfile.lower()
                    subfile_name=os.path.join(file_name, subfile)
                    if os.path.isfile(subfile_name):
                        name_size = round(os.path.getsize(subfile_name) / 1024 / 1024, 2)
                        size += name_size
                        filecount+=1

                        if subfile in expected_sub_dict.keys():
                            if abs(expected_sub_dict[subfile]-name_size)==0:
                                logger.info('  pass: {}'.format(subfile))
                                passcount=passcount+1
                            else:
                                logger.info('  fail: {} size = {} MB is not same with expected[], details: full name:{}'.format(subfile,name_size,expected_sub_dict[subfile],subfile_name))
                                missscount = missscount + 1
                            expected_sub_dict.pop(subfile)
                        else:
                            logger.info('  fail: {} not covered in testing scope, details: full name:{}'.format(subfile, subfile_name))
                            missscount = missscount + 1
                #dict[name]=expected_sub_dict
        else:
            logger.info('  fail: folder{} is not covered in testing scope.'.format(name))
            #missscount = missscount + 1
    for k, v in dict.items():
        for key,val in v.items():
            logger.info("  fail: miss file = {} size = {} MB in [{}]".format(key,val,k))
            failcount = failcount + 1
    endtime = datetime.datetime.now()
    logger.info("verify folder {} total files: {}, size: {} MB, used time {} ms".format(searchFolder,filecount, round(size,2),
                                                    round((endtime - starttime).microseconds / 1000, 2)))
    logger.info("verify totoal:{}, pass:{}, fail:{}, miss:{}".format(passcount+failcount+missscount,passcount,failcount,missscount))
    return (passcount,failcount,missscount, size)



if __name__=='__main__':
    #searchDcmByCszxName(r'C:\ProgramData\DEXIS IS\ScanFlow\data1\1.2.528.56.1005.202303281335082956875216.cszx')
    #identifyFile('C:\ProgramData\DEXIS IS\ScanFlow\data\Jean_Dupont[2023-03-24T13-15-07][1.0.8.432][Ortho].cszx')
    generate_newname('ScanFlow_Hardening Test[2023-02-06T13-51-07][1.0.9.101].cszx','scanflow_hardening test','sh','')
    verifyResultFolderCount(r'D:\dc_wr\New folder (3)')
