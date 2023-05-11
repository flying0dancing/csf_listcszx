# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import datetime,logging
from utils import FileUtil,Logger,XmlUtil
logger=logging.getLogger('main')
def verify(cszx_folder,video_folder,verify_folder,start_date,end_date):
    # Use a breakpoint in the code line below to debug your script.
    logger.info('=' * 10+'begin searching'+'=' * 10)
    logger.info('search cszx and algo folder: {}'.format(cszx_folder))
    logger.info('search video folder: {}'.format(video_folder))
    dict_result = {}
    starttime = datetime.datetime.now()
    totalsize = FileUtil.traverse_Folder(cszx_folder,start_date,end_date, dict_result)
    totalsize = totalsize + FileUtil.traverse_Folder(video_folder,start_date,end_date, dict_result)
    endtime = datetime.datetime.now()

    logger.info('=' * 10+'end searching'+'=' * 10)
    '''
    比较慢
    dict_result1={}
    starttime1 = datetime.datetime.now()
    totalsize1=traverse_cszxmp4zip(cszx_folder,'_records.zip',dict_result1)
    totalsize1=totalsize1+traverse_cszxmp4zip(cszx_folder,'.cszx',dict_result1)
    totalsize1=totalsize1+traverse_cszxmp4zip(video_folder,'.mp4',dict_result1)
    endtime1= datetime.datetime.now()

    '''
    # print("totoal1 size: {}, used time1: {} ms.".format(totalsize1,(endtime1-starttime1).microseconds))
    printExpectedResult(dict_result)
    FileUtil.verifyResultFolderCount(verify_folder)
    trup=FileUtil.verifyResult(verify_folder, dict_result)
    logger.info("searched total size: {} MB, used time: {} ms.".format(round(totalsize, 2),
                                                               round((endtime - starttime).microseconds / 1000, 2)))

    return trup
def printExpectedResult(dict_result):
    logger.info('')

    logger.info('=' * 10 + 'start printing expected result' + '=' * 10)
    filecount = 0
    for k, v in dict_result.items():
        logger.info("[{}]".format(k))
        for key, val in v.items():
            filecount = filecount + 1
            logger.info("    {} {}, size {} MB".format(filecount, key, val))
    logger.info('expected total files:{}'.format(filecount))
    logger.info('=' * 10 + 'end printing expected result' + '=' * 10)
    logger.info('')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #cszx_folder=r'D:\patient_data'
    #video_folder=r'C:\ProgramData\DEXIS IS\ScanFlow\data'
    verify_folder = r'D:\dc_wr\New folder (3)'
    start_date=FileUtil.getDateByFileSuffix('1.0.8_d133[2023-02-10T12-34-48][1.0.8.201].cszx')
    end_date=datetime.date.today()
    resultcount=verify(XmlUtil.getRawDataFolder(),XmlUtil.getVideoFolder(),verify_folder,start_date,end_date)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
