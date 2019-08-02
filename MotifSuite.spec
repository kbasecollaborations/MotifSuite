/*
A KBase module: MotifSuite
*/

module MotifSuite {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;
     
    typedef structure{
        string workspace_name;
        string genome_ref;
        string SS_ref;
        int promoter_length;
        int motif_min_length;
        int motif_max_length;
        string obj_name;
        float prb;
        int gibbs;
        int meme;
        int homer;
        int mdscan;
        int motifsampler;
        int mfmd;
        int motif_length;
        int background;
        int mask_repeats;
        mapping<string, string> background_group;
        float threshold;
        float proportion;        
      } motifsuite_seq_input;
        
 
    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_MotifSuite(motifsuite_seq_input params) returns (ReportResults output) authentication required; 
    /*funcdef run_MotifSuite(mapping<string, motifsuite_seq_input> params) returns (ReportResults output) authentication required;*/

};
