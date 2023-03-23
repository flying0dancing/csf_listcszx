import os.path
import datetime,logging
from utils import ziputil,Logger
from utils.acronymcatalogs import AcronymCatalogs
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
            if subFile.endswith('.cszx') and ziputil.filterZipFile(subFullName,identicators):
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
            if name.endswith('.cszx') and ziputil.filterZipFile(file_name, identicators):
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

def traverse_cszxFolder(searchFolder, dict):
    size = 0
    starttime = datetime.datetime.now()
    for root,dirs,files in os.walk(searchFolder):
        for name in dirs:
            pass
        for name in files:
            file_name=os.path.join(root,name)
            mask = oct(os.stat(file_name).st_mode)[-3:]
            list1=[]
            if str(mask)!=str(666):
                continue
            if name.endswith('.cszx'):#and ziputil.filterZipFile(file_name, identicators)
                key = generate_foldername(name)
                identifierStr = str.join('_', ziputil.getRefsFromZipFile(file_name, AcronymCatalogs.acqCatalogs()))
                if identifierStr=='':
                    continue
                print("folder:{}".format(key))
                print("  identifier:{}".format(identifierStr))
                newname = generate_cszxname(name, identifierStr)
                print("  newname:{}".format(newname))
                name_size = round(os.path.getsize(file_name) / 1024 / 1024, 2)
                size += name_size
                print("  fullpath: {}, size: {} MB".format(file_name,name_size))
                algoFile = find_algo_name(root, os.path.splitext(name)[0], '_records.zip')
                if algoFile is None:
                    appendToDict(dict, key, newname)
                else:
                    algo_name = os.path.basename(algoFile)
                    algo_newname = generate_newname_with_acronyn(algo_name)
                    print("  newname:{}".format(algo_newname))
                    name_size = round(os.path.getsize(algoFile) / 1024 / 1024, 2)
                    size += name_size
                    print("  fullpath: {}, size: {} MB".format(algoFile, name_size))
                    appendToDict(dict, key, newname,algo_newname)
    endtime = datetime.datetime.now()
    print("search folder {} used time {} ms".format(searchFolder,round((endtime - starttime).microseconds/1000,2)))
    return size

def traverse_videoFolder(searchFolder, dict):
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
                key = generate_foldername(name)
                newname=generate_newname_with_acronyn(name)
                print("folder:{}".format(key))
                print("  newname:{}".format(newname))
                name_size=round(os.path.getsize(file_name) / 1024 / 1024, 2)
                size += name_size
                print("  fullpath: {}, size: {} MB".format(file_name,name_size))
                appendToDict(dict,key,newname)
    endtime = datetime.datetime.now()
    print("search videoFolder {} used time {} ms".format(searchFolder, round((endtime - starttime).microseconds / 1000, 2)))
    return size

def traverse_cszxmp4zip(searchFolder, suffix, dict):
    size = 0
    starttime = datetime.datetime.now()
    for root,dirs,files in os.walk(searchFolder):
        for name in dirs:
            pass
        for name in files:
            file_name=os.path.join(root,name)
            mask = oct(os.stat(file_name).st_mode)[-3:]
            list1=[]
            if str(mask)!=str(666):
                continue
            if name.endswith(suffix):#and ziputil.filterZipFile(file_name, identicators)
                key = generate_foldername(name)
                print(key+" "+file_name + " " + str(round(os.path.getsize(file_name) / 1024 / 1024, 2)))
                size += round(os.path.getsize(file_name) / 1024 / 1024, 2)
                appendFileToDict(dict, key, file_name)
    endtime = datetime.datetime.now()
    print("search {} folder {} used time {} ms".format(suffix,searchFolder,round((endtime - starttime).microseconds/1000,2)))
    return size

def verifyResult(searchFolder,dict):
    starttime = datetime.datetime.now()
    files = os.listdir(searchFolder)
    passcount=0
    failcount=0
    missscount=0
    for name in files:
        file_name = os.path.join(searchFolder, name)
        if os.path.isdir(file_name):
            list_ver=dict.get(name)
            if list_ver is None:
                logger.info('fail: folder{} is not covered in testing scope.'.format(name))
                missscount=missscount+1
            else:
                logger.info('[{}]'.format(name))
                subfiles=os.listdir(file_name)
                for subfile in subfiles:
                    subfile_name=os.path.join(file_name, subfile)
                    if os.path.isfile(subfile_name):
                        if subfile in list_ver:
                            logger.info('pass: {}'.format(subfile))
                            list_ver.remove(subfile)
                            passcount=passcount+1
                        else:
                            logger.info('fail: {} not covered in testing scope, details: full name:{}'.format(subfile, subfile_name))
                            missscount = missscount + 1
                dict[name]=list_ver
        else:
            logger.info('fail: folder{} is not covered in testing scope.'.format(name))
            missscount = missscount + 1
    for k, v in dict.items():
        for value in v:
            logger.info("fail:miss {} in [{}]".format(value,k))
            failcount = failcount + 1
    endtime = datetime.datetime.now()
    logger.info("search folder {} used time {} ms".format(searchFolder,
                                                    round((endtime - starttime).microseconds / 1000, 2)))
    logger.info("verify totoal:{}, pass:{}, fail:{}, miss:{}".format(passcount+failcount+missscount,passcount,failcount,missscount))


def appendFileToDict(dict, key,value):
    list_exist = dict.get(key)
    if list_exist is None:
        dict[key] = [value]
    else:
        if value not in list_exist:
            list_exist.append(value)
        dict[key] = list_exist

def appendToDict(dict, key,*values):
    list_exist=dict.get(key)
    if list_exist is None:
        dict[key] = list(values)
    else:
        for value in values:
            if value not in list_exist:
                list_exist.append(value)
        dict[key]=list_exist


def generate_cszxname(fname,identifierStr):
    pics_fname=os.path.splitext(fname)
    result = pics_fname[0]
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',1)
        result=acronyn_name(fname)+'['+pics_f[1]+"_"+identifierStr+pics_fname[1]
    return result

def generate_newname_with_acronyn(fname):
    pics_fname=os.path.splitext(fname)
    result = pics_fname[0]
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',1)
        result=acronyn_name(fname)+'['+pics_f[1]+pics_fname[1]
    return result

#get First_Last return FL
def acronyn_name(fname):
    result = ''
    pics_fname = os.path.splitext(fname)
    if '[' in pics_fname[0]:
        pics_f = pics_fname[0].split('[', 1)
        if '_' in pics_f[0]:
            pics_p = pics_f[0].split('_')
            result = pics_p[0][0] + pics_p[1][0]

    return result

#FL_YYYYMMDD
def generate_foldername(fname):
    pics_fname=os.path.splitext(fname)
    result = pics_fname[0]
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',2)
        dateStr = pics_f[1].split('T')[0]
        result=acronyn_name(fname)+'_'+dateStr.replace('-','')
    return result


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
        datetime_result=datetime.datetime.strptime(datetime_str,format).date()
    else:
        datetime_result=None
    return datetime_result



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

def generate_cszxname_bak(fname,identifierStr=''):
    result=fname
    pics_fname=os.path.splitext(fname)
    if '[' in pics_fname[0]:
        pics_f=pics_fname[0].split('[',1)
        if '_' in pics_f[0]:
            pics_p=pics_f[0].split('_')
            result=pics_p[0][0]+pics_p[1][0]+'['+pics_f[1]+identifierStr
    return result
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



