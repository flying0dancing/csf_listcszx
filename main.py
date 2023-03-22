# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import utils.fileutil
import datetime
def verify(cszx_folder,video_folder,verify_folder):
    # Use a breakpoint in the code line below to debug your script.
    print('=' * 10+'begin searching'+'=' * 10)
    dict_result = {}
    starttime = datetime.datetime.now()
    totalsize = utils.fileutil.traverse_cszxFolder(cszx_folder, dict_result)
    totalsize = totalsize + utils.fileutil.traverse_videoFolder(video_folder, dict_result)
    endtime = datetime.datetime.now()
    print("totoal size: {} MB, used time: {} ms.".format(round(totalsize, 2), round((endtime - starttime).microseconds/1000,2)))
    print('=' * 10+'end searching'+'=' * 10)
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
    print('')

    print('=' * 10 + 'start printing result' + '=' * 10)
    for k,v in dict_result.items():
        print("[{}]".format(k))
        for value in v:
            print("    {}".format(value))
    print('=' * 10 + 'end printing result' + '=' * 10)
    print('')
    utils.fileutil.verifyResult(verify_folder, dict_result)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cszx_folder=r'D:\patient_data\c478435cf52e4dd3ab6f8ae6254f936b'
    video_folder=r'D:\patient_data'
    verify_folder = r'D:\patient_data'
    verify(cszx_folder,video_folder,verify_folder)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
