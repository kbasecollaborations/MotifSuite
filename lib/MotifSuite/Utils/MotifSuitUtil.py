import sys
import os
import json
import subprocess

class MotifSuiteUtil:
  def __init__(self):
      pass
  def get_obj_refs(self):
      obj_refs = []
      memef = open("meme_out/obj.name", "r")
      obj_refs.append((memef.readline()).rstrip())
      memef.close()

      homerf = open("homer_out/obj.name", "r")
      obj_refs.append((homerf.readline()).rstrip())
      homerf.close()

      gibbsf = open("gibbs_out/obj.name", "r")
      obj_refs.append((gibbsf.readline()).rstrip())
      gibbsf.close()

      return obj_refs

MSU=MotifSuiteUtil()
print(MSU.get_obj_refs())

      
