import os
from copy import deepcopy
from Bio import motifs
from Bio import SeqIO
from Bio.Alphabet import IUPAC
from io import StringIO
import math

class FastaUtils:
  def __init__(self):
      pass

  def merge(self, motifs,MSD):
      for motif in motifs:
          newMotif = deepcopy(MSD[motif[0]]['Motifs'][motif[1]])
          break;
      return newMotif


  def ParseTomTom(self, path):

      pval = 0.0
      with open(path + '/tomtom.tsv','r') as tomtomfile:
          header = tomtomfile.readline()
          results = tomtomfile.readline()
          if len(results.split('\t')) == 1:
              return 1.0
          elems = results.split('\t')
          pval = float(elems[3])

      return pval

  def RunTomTom(self,path1,path2,outpath):
      tomtom_command ='/kb/deployment/bin/meme/bin/tomtom -oc ' + outpath + ' ' + path1 + ' ' + path2
      os.system(tomtom_command)
      return

  def WriteMotifAsMEME(self, motif,path):
      tempAlph = ['A','C','G','T']
      MEMEText = 'MEME version 4\n\n'
      sortedAlph = tempAlph
      alphStr = ''.join(sortedAlph)
      MEMEText += alphStr + '\n'
      MEMEText += '\n'
      MEMEText += 'strands: + -\n\n'
      MEMEText += 'Background letter frequencies\n'
      for letter in sortedAlph:
          MEMEText += letter + ' ' + str(.25) + ' '
      MEMEText += '\n\n'
      MEMEText += 'MOTIF ' + motif['Iupac_sequence'] + '\n'
      MEMEText += 'letter-probability matrix: alength= 4 w= '
      MEMEText += str(len(motif['Iupac_sequence'])) + ' nsites= '
      if motif['Motif_Locations'] is not None:
          MEMEText += str(len(motif['Motif_Locations']))
      else:
          MEMEText += '0'
      MEMEText += ' E= 0.0\n'
    
      for i in range(0,len(motif['Iupac_sequence'])):
          for letter in sortedAlph:
              try:
                  MEMEText += str(motif['PWM'][letter][i]) + ' '
              except IndexError:
                  print('ERROR FOR MOTIF')
                  print(motif['Iupac_sequence'])
                  print(motif['PWM'])
          MEMEText += '\n'
      MEMEText += '\n'
      with open(path,'w') as motifFile:
          motifFile.write(MEMEText)

      return

  def PWMtoPSSM(self, BPmotif,motif):
      background = {'A':0.25,'C':0.25,'G':0.25,'T':0.25}

      pssm = BPmotif.pwm.log_odds(background)
      alph = ['A','C','G','T']
      replace = 0.0
      for l in alph:
          for i,val in enumerate(pssm[l]):
              if math.isnan(val):
                  pssm[l][i] = replace
              if math.isinf(val):
                  if val > 1:
                      pssm[l][i] = 10
                  else:
                      pssm[l][i] = -10

      return pssm

  def MotifToBP(self, motif, name):
      motifStr = '>' + name + '\n'
      motifStr += 'A ' + str(motif['PWM']['A']).replace(',','') + '\n'
      motifStr += 'C ' + str(motif['PWM']['C']).replace(',','') + '\n'
      motifStr += 'G ' + str(motif['PWM']['G']).replace(',','') + '\n'
      motifStr += 'T ' + str(motif['PWM']['T']).replace(',','') + '\n'

      handle = StringIO(motifStr)
      motif = motifs.read(handle, 'jaspar')
      return motif

  def CompareMotifsBP(self, motif1, motif2, threshold):
      BPmotif1 = self.MotifToBP(motif1,'motif1')
      BPmotif2 = self.MotifToBP(motif2,'motif2')

      if str(BPmotif1.degenerate_consensus) == str(BPmotif2.degenerate_consensus):
          print('FOUND Sequence MATCH FOR')
          print(BPmotif1.degenerate_consensus)
          print(BPmotif2.degenerate_consensus)
          return True

      pssm1 = self.PWMtoPSSM(BPmotif1,motif1)
      pssm2 = self.PWMtoPSSM(BPmotif2,motif2)

      distance,offset = pssm1.dist_pearson(pssm2)

      thresh = .3
      thresh = 1 - threshold
      if distance <= thresh:
          if abs(offset) > len(BPmotif1.degenerate_consensus)/2:
              return False
          print('FOUND MATCH FOR')
          print('with distance ' + str(distance) + ' and offset ' + str(offset))
          print(BPmotif1.degenerate_consensus)
          print(BPmotif2.degenerate_consensus)
          return True
      return False

  def CompareMotifs(self, motif1, motif2):

      pvalThresh = 1.0e-10
      path1 = '/kb/module/work/tmp/motif1.txt'
      path2 = '/kb/module/work/tmp/motif2.txt'
      WriteMotifAsMEME(motif1,path1)
      WriteMotifAsMEME(motif2,path2)

      tomtompath = '/kb/module/work/tmp/tomtom_out'
      RunTomTom(path1,path2,tomtompath)

      pval = ParseTomTom(tomtompath)

      os.remove(path1)
      os.remove(path2)
      if pval <= pvalThresh:
          return True

      return False
