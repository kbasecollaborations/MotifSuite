# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

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
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

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
        :param params: instance of mapping from String to unspecified object
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

        result = homer_obj.DiscoverMotifsFromSequenceSet(params)
        print('Homer RESULT:')
        pprint(result)
     
        '''if os.path.exists('/kb/module/work/homer_out'):
           shutil.rmtree('/kb/module/work/homer_out')
        shutil.copytree('/kb/module/work/tmp/', '/kb/module/work/homer_out/')
        '''
        result = meme_obj.DiscoverMotifsFromSequenceSet(params)
        print('MEME RESULT:')
        pprint(result)

        result = mfmd_obj.DiscoverMotifsFromSequenceSet(params)
        print('MFMD RESULT:')
        pprint(result)

        result = ensemble_obj.MotifEnsemble(params)
        print('Ensemble RESULT:')
        print(result)

        '''
        if os.path.exists('/kb/module/work/meme_out'):
           shutil.rmtree('/kb/module/work/meme_out')
        shutil.copytree('/kb/module/work/tmp/', '/kb/module/work/meme_out/')

        result = gibbs_obj.ExtractPromotersFromFeatureSetandDiscoverMotifs(params)
        print('Gibbs RESULT:')
        pprint(result)
        if os.path.exists('/kb/module/work/gibbs_out'):
           shutil.rmtree('/kb/module/work/gibbs_out')
        shutil.copytree('/kb/module/work/tmp/', '/kb/module/work/gibbs_out/')

        #fix issue for MotifFindermfmd in catalogue  
        result = mfmd_obj.DiscoverMotifsFromSequenceSet(params)
        print('MFMD RESULT:')
        pprint(result)
        
        MSU=MotifSuiteUtil()
        params['motifset_refs']= MSU.get_obj_refs()

        result = ensemble_obj.MotifEnsemble(params)
        print('Ensemble RESULT:')
        print(result)
        '''
    
        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': params['workspace_name']},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
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
