from H5_maker import * 


parser = OptionParser()
parser.add_option("-f", "--flag", dest = "flag", default = -1234, type=int, help="Flag to label what type of process this is (QCD, ttbar, signal, etc)")
parser.add_option("--sys", default = False, action = 'store_true', help="Add additional info the h5's for systematics")
parser.add_option("--top_ptrw", default = False, action = 'store_true', help="Include ttbar top pt reweighting factors")
parser.add_option("--ttbar", default = False, action = 'store_true', help="Semi leptonic ttbar version of h5 maker (different preselection)")
parser.add_option("--fTree", dest = "friend_tree", default = '', help="Friend tree with extra branches for systematics")
parser.add_option("--sample_type", default = "MC", help="MC or data")
parser.add_option("-i", "--input", dest = "fin", default = '', help="Input file name")
parser.add_option("-o", "--output", dest = "fout", default = 'test.h5', help="Output file name")
parser.add_option("-j", "--json", default = '', help="Json file name")
parser.add_option("-y", "--year", type=int, default = 2016, help="Year the sample corresponds to")
parser.add_option("-n", "--nEvents",  type=int, default = -1, help="Maximum number of events to output (-1 to run over whole file)")
parser.add_option("--gen", default = "",  help="Save gen level info for this signal (options are: Qstar, Wkk, Wp, XYY, ZpToTpTp, YtoHH)")

options, args = parser.parse_args()

if options.friend_tree=="null":
    friend_tree_args = []
else:
    friend_tree_args = [options.friend_tree]


if(options.flag == -1234):
    print("No --flag option set. You must specify what type of process this is! \n" )
    exit(1)

if(options.ttbar):
    NanoReader(options.flag, inputFileNames = [options.fin], outputFileName = options.fout, json = options.json, year = options.year, 
        nEventsMax = options.nEvents, include_systematics = options.sys, do_top_ptrw = options.top_ptrw, sampleType = options.sample_type,friend_trees=friend_tree_args, gen_label = options.gen)
else:

    NanoReader(options.flag, inputFileNames = [options.fin], outputFileName = options.fout, json = options.json, year = options.year, 
        nEventsMax = options.nEvents, include_systematics = options.sys, do_top_ptrw = options.top_ptrw, sampleType = options.sample_type,friend_trees=friend_tree_args, gen_label = options.gen)

