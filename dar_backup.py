import subprocess
import logging
import glob
import os
import dar_backup_params
import datetime
import dar_backup_previous_file

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('dar_backup')

# build up a list of strings to send into the subprocess
process_strings = []
process_strings.append('/usr/bin/dar')

# params to directly use in the call to dar
params = {}

# get params
params = dar_backup_params.parse(log)

# define config parameter string
if params['config'] is not None:
    process_strings.append('--noconf --batch ')
    process_strings.append(params['config'])

# source (root) path
process_strings.append('-R')
process_strings.append(params['source_path'])

# get the current date/time in a string usage as a suffix to the filename
date_now = datetime.datetime.utcnow()
date_string = date_now.strftime("%Y%m%d_%H%M") + "UTC"
log.info("date_string=" + date_string)

# create the destination basename (includes path, if any)
destination_basename = dest_path_and_base_name + "_" + date_string
log.info("destination_basename=" + destination_basename)

# archive to create
process_strings.append('-c')
process_strings.append(destination_basename)

# incremental
if params['incremental']:
    # get list of files and dates, sort and take newest one
    # strip of .xx.dar
    full_previous_file = dar_backup_previous_file.get_previous_file(params['dest_path_and_base_name'])
    log.info("full_previous_file=" + full_previous_file)
    previous_file = dar_backup_previous_file.remove_slice_number_and_extension(full_previous_file)
    log.info("previous_file=" + previous_file)
    process_strings.append('-A')
    process_strings.append(previous_file)

# define prune paramter string
for onePath in params['prune']:
    process_strings.append('-P ')
    process_strings.append(onePath)

# exclude the destination archive(s) in case they are being created somewhere in the source directory path
process_strings.append('-X')
process_strings.append('<destination filename without the path>' + '*.*.dar'

# log values from process_strings

# make call to dar
return_code = subprocess.call(process_strings, 
    stdout=subprocess.STDOUT,
    stderr=subprocess.STDOUT,
    shell=False)
    
# log return value

# if not error, then continue on to test

# test
  

