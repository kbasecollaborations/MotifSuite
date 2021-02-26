from installed_clients.DataFileUtilClient import DataFileUtil
from copy import deepcopy

class DownloadMotifSets:
  def __init__(self):
      pass

  def DownloadMotifSet(self, refList,callback):
      '''

      :param refList:
      :param callback:
      :return:
      '''
      MotifSetDict = {}
      dfu = DataFileUtil(callback)
      for ref in refList:
          get_objects_params = {'object_refs' : [ref]}
          MotifSet = dfu.get_objects(get_objects_params)['data'][0]['data']
          MotifSetDict[ref] = deepcopy(MotifSet)
      return MotifSetDict
