import sys
import os
import json
import subprocess

class MotifSuiteUtil:
  def __init__(self):
      pass
  def get_obj_refs(self):
      #path="/home/manish/Desktop/reorganization/MotifSuite/test_local/workdir/"
      path="/kb/module/work/"
      obj_refs = []
      memef = open(path+"meme_out/obj.name", "r")
      obj_refs.append((memef.readline()).rstrip())
      memef.close()

      homerf = open(path+"homer_out/obj.name", "r")
      obj_refs.append((homerf.readline()).rstrip())
      homerf.close()

      gibbsf = open(path+"gibbs_out/obj.name", "r")
      obj_refs.append((gibbsf.readline()).rstrip())
      gibbsf.close()

      return obj_refs

MSU=MotifSuiteUtil()
print(MSU.get_obj_refs())

      
