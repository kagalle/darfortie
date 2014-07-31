# Script Name: dar_backup.py
# Author: Ken Galle
# Description: Adds functionality to the dar utility and in the process makes it
#    simpler to use, although to do this it does make some assumptions and hides
#    some functionality (which comes from the enormous list of dar switches).
#    Note however that a configuration file can be passed thru to dar.  See the
#    dar man page for details on its structure ("CONDITIONAL SYNTAX").
#    It manages the creation of incremental backups based on the most recent
#    available dar file with the same base name in a given directory.
#    It provides a way to specify a configuration file for dar without worrying
#    about the current environment (/etc/darrc, ~/.darrc).
#    It also allows you to pass thru dar prune paths.
# Note on destination naming convensions:  TODO
#TODO    Return values:
#      1xx, where xx is any error value returned from dar during archive creation.
#      2yy, where yy is any error value returned from dar during archive testing.
#        dar return values range from 1 to 11 (see dar man page, "EXIT CODES")
#      Returns 0 on success (both create and test succeeded).
# TODO:  I need to test for "None" return values in the incremental section.
# TODO: test for existance of dar and if not found exit with error code.
# TODO: exit with code if command line params are not correct (in addition to printing usage information)
# TODO: add support for restoring a batch of archives
# TODO: packaging: http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html
# Version: 1.0
# Revision History: 
#       22.08.2005 - Creation

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
destination_name_without_path = os.path.basename(destination_basename);
process_strings.append('-X')
process_strings.append(destination_name_without_path + '*.*.dar'

# log values from process_strings
i = 1
for process_string in process_strings:
    log.info(str(i) + ' : ' + process_string)
del(i)

# make call to dar
return_code = subprocess.call(process_strings, shell=False)
    
# log return value
log.info('dar create archive return value=' + str(return_code))

# if not error, then continue on to test
if return_code = 0:
    test_process_strings = []
    test_process_strings.append('/usr/bin/dar')
    # test archive just created
    test_process_strings.append('-t')
    test_process_strings.append(destination_basename)    
    # make call to dar
    test_return_code = subprocess.call(test_process_strings, shell=False)
    # log return value
    log.info('dar test archive return value=' + str(test_return_code))
  

