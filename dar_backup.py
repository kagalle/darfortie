import subprocess
import logging
import glob
import os
import dar_backup_params
import datetime
import dar_backup_previous_file

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('dar_backup')

# params to directly use in the call to dar
params = {}

# get params
# this works, but on second thought I would rather keep the dar switches
# explicitly on the dar command line instead of buried in variables.
# so the params{} dictionary is fine, but without putting in, e.g. -R, etc.
(params['config'], params['prune'], params['incremental'], source_path, 
    dest_path_and_base_name) = dar_backup_params.parse(log)



# get the current date/time in a string usage as a suffix to the filename
date_now = datetime.datetime.utcnow()
date_string = date_now.strftime("%Y%m%d_%H%M") + "UTC"
log.info("date_string=" + date_string)

# create the destination basename (includes path, if any)
destination_basename = dest_path_and_base_name + "_" + date_string
log.info("destination_basename=" + destination_basename)

prev = ""
if incremental:
    # get list of files and dates, sort and take newest one
    # strip of .xx.dar
    full_previous_file = dar_backup_previous_file.get_previous_file(dest_path_and_base_name)
    log.info("full_previous_file=" + full_previous_file)
    previous_file = dar_backup_previous_file.remove_slice_number_and_extension(full_previous_file)
    log.info("previous_file=" + previous_file)
    
#
  
  

