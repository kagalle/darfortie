import glob
import os.path
from operator import itemgetter

# returns previous filename 
def get_previous_file(dest_path_and_base_name):
    retval = None
    filelist = glob.glob(dest_path_and_base_name + "*.1.dar")
    if len(filelist) > 0:
        filedata = []
        for onefile in filelist:
            # get the last modified datetime for each file
            filedata.append( (onefile, os.path.getmtime(onefile)) )
        
        # sort the list by the date
        sorted_list = sorted(filedata, key=itemgetter(1), reverse=True)
        retval = sorted_list[0][0]
    return retval
    
def remove_slice_number_and_extension(full_previous_file):
    retval = None
    # I know the slice number will be 1 and the extension will be 'dar'
    index = full_previous_file.rfind(".1.dar", 0)
    if index > 0:
        retval = full_previous_file[0:index]
    return retval
    

