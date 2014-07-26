import optparse
import logging

# provides:
#   config parameter string
#   prune parameter string
#   incremental boolean
def parse(log):
    usageString = "usage: %prog [options] <source_path> <dest_path_and_base_name>"
    descriptionString = "A front-end for dar that supports incremental backups based on " + \
    "the existing backups found in the destination folder.  <source_path> is the " + \
    "root path to back up (dar -R).  <dest_path_and_base_name> is the dar base name.  This " + \
    "may include an optional path.  This program will supply date strings to the final " + \
    "name and dar itself will supply slice numbers to form the complete filename."
    epilogString = "Based on http://dar.linux.free.fr/doc/mini-howto/dar-differential-backup-mini-howto.en.html"
    p = optparse.OptionParser(usage=usageString, description=descriptionString, epilog=epilogString)
    
    # -c --config: specify .dar config file --> conf
    p.add_option("-c", "--config", action="store", dest="conf", metavar="config_filespec",
        help="filespec of dar config file to use instead of .darrc or etc/darrc.")
    
    # -P --prune: add dar prune paths --> prune
    p.add_option("-P", "--prune", action="append", dest="prune", metavar="prune_path",
        help="dar -P (prune) paths to add to call to dar. Path should be relative to " +
        "<source_path>.  This option can be repeated as needed.")
    
    # -i --incremental: enable incremental (dar -A) mode
    p.add_option("-i", "--incremental", action="store_true", dest="incremental", default=False, 
        help="search for previous backup to use for incremental backup (dar -A).  " +
        "Finds most recent like-named backup in destination folder.")
    
    # parse command line
    opts, args = p.parse_args()
    
    # define config parameter string
    if opts.conf is None:
      conf = ""
    else:
      conf = "--noconf --batch " + opts.conf + " "
    log.info("conf=" + str(conf))
    
    # define prune paramter string
    prune = ""
    for onePath in opts.prune:
      prune = prune + "-P " + onePath + " "
    log.info("prune=" + prune)
    
    #define incremental parameter string
    incremental = opts.incremental
    log.info("incremental=" + str(incremental))
    
    if len(args) != 2:
        p.print_usage()
        exit()
    
    source_path = args[0]
    log.info("source_path=" + source_path)
    dest_path_and_base_name = args[1]
    log.info("dest_path_and_base_name=" + dest_path_and_base_name)

    # need to gather up 
    return (conf, prune, incremental, source_path, dest_path_and_base_name)

