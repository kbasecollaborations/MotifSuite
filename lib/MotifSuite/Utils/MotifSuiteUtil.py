import sys
import os
import json
import subprocess

class MotifSuiteUtil:
  def __init__(self):
      pass

  def get_obj_refs(self):
      '''

      :return:
      '''
      path="/kb/module/work/tmp/"
      obj_refs = []
      #print(path + "meme_out/meme_obj.txt")
      if(os.path.isfile(path + "meme_out/meme_obj.txt")):
         print("yes")
         memef = open(path+"meme_out/meme_obj.txt", "r")
         obj_refs.append((memef.readline()).rstrip())
         memef.close()

      if(os.path.isfile(path + "homer_out/homer_obj.txt")):
         homerf = open(path+"homer_out/homer_obj.txt", "r")
         obj_refs.append((homerf.readline()).rstrip())
         homerf.close()
     
      if(os.path.isfile(path + "gibbs/gibbs_obj.txt")):
         gibbsf = open(path+"gibbs/gibbs_obj.txt", "r")
         obj_refs.append((gibbsf.readline()).rstrip())
         gibbsf.close()

      if(os.path.isfile(path + "mfmd_out/mfmd_obj.txt")):
         mfmdf = open(path+"mfmd_out/mfmd_obj.txt", "r")
         obj_refs.append((mfmdf.readline()).rstrip())
         mfmdf.close()   

      if(os.path.isfile(path + "mdscan_out/mdscan_obj.txt")):
         mdscanf = open(path+"mdscan_out/mdscan_obj.txt", "r")
         obj_refs.append((mdscanf.readline()).rstrip())
         mdscanf.close() 
  
      if(os.path.isfile(path + "sampler_out/sampler_obj.txt")):
         samplerf = open(path+"sampler_out/sampler_obj.txt", "r")
         obj_refs.append((samplerf.readline()).rstrip())
         samplerf.close()   

      return obj_refs

MSU=MotifSuiteUtil()
print(MSU.get_obj_refs())

      
