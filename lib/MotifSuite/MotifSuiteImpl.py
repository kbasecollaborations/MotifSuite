# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
from multiprocessing import Process
from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.MotifFindermfmdClient import MotifFindermfmd
from installed_clients.MotifFinderHomerClient import MotifFinderHomer
from installed_clients.MotifFinderMEMEClient import MotifFinderMEME
from installed_clients.MotifFinderGibbsClient import MotifFinderGibbs
from installed_clients.MotifEnsembleClient import MotifEnsemble
from MotifSuite.Utils.MotifSuiteUtil import MotifSuiteUtil
from pprint import pprint, pformat
import shutil, sys  
#END_HEADER


class MotifSuite:
    '''
    Module Name:
    MotifSuite

    Module Description:
    A KBase module: MotifSuite
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://github.com/man4ish/MotifSuite.git"
    GIT_COMMIT_HASH = "82094eec2bf903033ea232dbe9ff1062ea119bb2"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_MotifSuite(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of type "motifsuite_seq_input" -> structure:
           parameter "workspace_name" of String, parameter "genome_ref" of
           String, parameter "SS_ref" of String, parameter "promoter_length"
           of Long, parameter "motif_min_length" of Long, parameter
           "motif_max_length" of Long, parameter "obj_name" of String,
           parameter "prb" of Double, parameter "motif_length" of Long,
           parameter "background" of Long, parameter "mask_repeats" of Long,
           parameter "background_group" of mapping from String to String,
           parameter "threshold" of Double, parameter "proportion" of Double
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_MotifSuite
        report = KBaseReport(self.callback_url)
        mfmd_obj = MotifFindermfmd(self.callback_url)
        homer_obj = MotifFinderHomer(self.callback_url)
        meme_obj =  MotifFinderMEME(self.callback_url)
        gibbs_obj = MotifFinderGibbs(self.callback_url)
        ensemble_obj = MotifEnsemble(self.callback_url)

        p1 = Process(target=homer_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p1.start()
        p2 = Process(target=mfmd_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p2.start()
        p3 = Process(target=meme_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p3.start()
        p4 = Process(target=gibbs_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p4.start()
 
        p1.join()
        p2.join()
        p3.join()
        p4.join()

        MSU=MotifSuiteUtil()
        params['motifset_refs']= MSU.get_obj_refs()

        result = ensemble_obj.MotifEnsemble(params)
        print('Ensemble RESULT:')
        print(result)


        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': params['workspace_name']},
                                                'workspace_name': params['workspace_name']})
 
        output = {
            'report_name': params,
            'report_ref': report_info['ref'],
        }
        '''report = KBaseReport(self.callback_url)
        mfmd_obj = MotifFindermfmd(self.callback_url)
        homer_obj = MotifFinderHomer(self.callback_url)
        meme_obj =  MotifFinderMEME(self.callback_url)
        gibbs_obj = MotifFinderGibbs(self.callback_url)
        ensemble_obj = MotifEnsemble(self.callback_url)

        p1 = Process(target=homer_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p1.start()
        p2 = Process(target=mfmd_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p2.start()
        p3 = Process(target=meme_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p3.start()
        p4 = Process(target=gibbs_obj.DiscoverMotifsFromSequenceSet, args=(params,))
        p4.start()
        
        p1.join()
        p2.join()
        p3.join()
        p4.join()

        
        
        
        MSU=MotifSuiteUtil()
        params['motifset_refs']= MSU.get_obj_refs()

        result = ensemble_obj.MotifEnsemble(params)
        print('Ensemble RESULT:')
        print(result)
        

    
        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': params['workspace_name']},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }'''
        #END run_MotifSuite

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_MotifSuite return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
