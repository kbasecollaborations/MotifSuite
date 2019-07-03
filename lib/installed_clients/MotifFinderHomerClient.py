# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except ImportError:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class MotifFinderHomer(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://ci.kbase.us/services/auth/api/legacy/KBase/Sessions/Login',
            service_ver='dev',
            async_job_check_time_ms=100, async_job_check_time_scale_percent=150, 
            async_job_check_max_time_ms=300000):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms,
            async_job_check_time_scale_percent=async_job_check_time_scale_percent,
            async_job_check_max_time_ms=async_job_check_max_time_ms)

    def find_motifs(self, params, context=None):
        """
        :param params: instance of type "find_motifs_params" (SS_ref -
           optional, used for exact genome locations if possible) ->
           structure: parameter "workspace_name" of String, parameter
           "fastapath" of String, parameter "motif_min_length" of Long,
           parameter "motif_max_length" of Long, parameter "SS_ref" of
           String, parameter "obj_name" of String
        :returns: instance of type "extract_output_params" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.run_job('MotifFinderHomer.find_motifs',
                                    [params], self._service_ver, context)

    def BuildFastaFromSequenceSet(self, params, context=None):
        """
        :param params: instance of type "BuildSeqIn" -> structure: parameter
           "workspace_name" of String, parameter "SequenceSetRef" of String,
           parameter "fasta_outpath" of String
        :returns: instance of type "BuildSeqOut" -> structure: parameter
           "fasta_outpath" of String
        """
        return self._client.run_job('MotifFinderHomer.BuildFastaFromSequenceSet',
                                    [params], self._service_ver, context)

    def ExtractPromotersFromFeatureSetandDiscoverMotifs(self, params, context=None):
        """
        :param params: instance of type "extract_input" -> structure:
           parameter "workspace_name" of String, parameter "genome_ref" of
           String, parameter "featureSet_ref" of String, parameter
           "promoter_length" of Long, parameter "motif_min_length" of Long,
           parameter "motif_max_length" of Long, parameter "obj_name" of
           String
        :returns: instance of type "extract_output_params" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.run_job('MotifFinderHomer.ExtractPromotersFromFeatureSetandDiscoverMotifs',
                                    [params], self._service_ver, context)

    def DiscoverMotifsFromFasta(self, params, context=None):
        """
        :param params: instance of type "discover_fasta_input" -> structure:
           parameter "workspace_name" of String, parameter "fasta_path" of
           String
        :returns: instance of type "extract_output_params" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.run_job('MotifFinderHomer.DiscoverMotifsFromFasta',
                                    [params], self._service_ver, context)

    def DiscoverMotifsFromSequenceSet(self, params, context=None):
        """
        :param params: instance of type "discover_seq_input" -> structure:
           parameter "workspace_name" of String, parameter "genome_ref" of
           String, parameter "SS_ref" of String, parameter "promoter_length"
           of Long, parameter "motif_min_length" of Long, parameter
           "motif_max_length" of Long, parameter "obj_name" of String,
           parameter "background" of Long, parameter "mask_repeats" of Long,
           parameter "background_group" of mapping from String to String
        :returns: instance of type "extract_output_params" -> structure:
           parameter "report_name" of String, parameter "report_ref" of String
        """
        return self._client.run_job('MotifFinderHomer.DiscoverMotifsFromSequenceSet',
                                    [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.run_job('MotifFinderHomer.status',
                                    [], self._service_ver, context)
