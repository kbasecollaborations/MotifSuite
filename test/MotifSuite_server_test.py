# -*- coding: utf-8 -*-
import os
import time
import unittest
from configparser import ConfigParser

from MotifSuite.MotifSuiteImpl import MotifSuite
from MotifSuite.MotifSuiteServer import MethodContext
from MotifSuite.authclient import KBaseAuth as _KBaseAuth

from installed_clients.WorkspaceClient import Workspace


class MotifSuiteTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = os.environ.get('KB_AUTH_TOKEN', None)
        config_file = os.environ.get('KB_DEPLOYMENT_CONFIG', None)
        cls.cfg = {}
        config = ConfigParser()
        config.read(config_file)
        for nameval in config.items('MotifSuite'):
            cls.cfg[nameval[0]] = nameval[1]
        # Getting username from Auth profile for token
        authServiceUrl = cls.cfg['auth-service-url']
        auth_client = _KBaseAuth(authServiceUrl)
        user_id = auth_client.get_user(token)
        # WARNING: don't call any logging methods on the context object,
        # it'll result in a NoneType error
        cls.ctx = MethodContext(None)
        cls.ctx.update({'token': token,
                        'user_id': user_id,
                        'provenance': [
                            {'service': 'MotifSuite',
                             'method': 'please_never_use_it_in_production',
                             'method_params': []
                             }],
                        'authenticated': 1})
        cls.wsURL = cls.cfg['workspace-url']
        cls.wsClient = Workspace(cls.wsURL)
        cls.serviceImpl = MotifSuite(cls.cfg)
        cls.scratch = cls.cfg['scratch']
        cls.callback_url = os.environ['SDK_CALLBACK_URL']
        suffix = int(time.time() * 1000)
        cls.wsName = "test_ContigFilter_" + str(suffix)
        ret = cls.wsClient.create_workspace({'workspace': cls.wsName})  # noqa

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'wsName'):
            cls.wsClient.delete_workspace({'workspace': cls.wsName})
            print('Test workspace was deleted')

    # NOTE: According to Python unittest naming rules test method names should start from 'test'. # noqa
    def test_your_method(self):
        # Prepare test objects in workspace if needed using
        # self.getWsClient().save_objects({'workspace': self.getWsName(),
        #                                  'objects': []})
        #
        # Run your method by
        # ret = self.getImpl().your_method(self.getContext(), parameters...)
        #
        # Check returned data with
        # self.assertEqual(ret[...], ...) or other unittest methods
        params = {
            'workspace_name': 'man4ish_gupta:narrative_1559788829014',
            'genome_ref': '29476/2/1',
            'SS_ref' : '29476/5/1',
            'featureSet_ref': '29476/36/2',
            'promoter_length':100,
            'motif_min_length':8,
            'motif_max_length':16,
            'motif_length':10,
            'prb':0.05,
            'mask_repeats' : 1,
            'background_group': {'background' : 0, 'genome_ref' : '29476/2/1'},
            'obj_name':'gibbs_obj',
            'motifset_refs' : ['29476/42/15','28598/32/31','29476/83/56'],
            'threshold' : .6,
            'proportion':.66,
        }

        ret = self.serviceImpl.run_MotifSuite(self.ctx, params)
 
        #ret = self.serviceImpl.run_MotifSuite(self.ctx, {'workspace_name': self.wsName,
        #                                                     'parameter_1': 'Hello World!'})
