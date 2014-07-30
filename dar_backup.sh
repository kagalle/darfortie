#!/bin/bash
# dar_diff_backup.sh
# Modified from http://dar.linux.free.fr/doc/mini-howto/dar-differential-backup-mini-howto.en.html

# Exit with exit status on the first thing that errors -
#   ie. don't test archive, if archive create failed.
set -e
# Fail if there is an attempt made to use an uninitialized variable.
set -u

# Best to not put trailing slashes on paths.

# Example "slice base name":   asus_root_gentoo_system_daily
#                             <host><user><task name><frequency>

# test run (last one done): ./dar_backup.sh -i -c /home/ken/dar_backup_script/dar_backup.conf -P ignore 
#       /home/ken/dar_backup_script /home/ken/dar_backup_script/destination asus_root_system_daily
#
#    ./test.sh
#    ./destination
#    ./destination/asus_root_system_daily_20130101_0000UTC.1.dar*  (fake archive)
#    ./destination/asus_root_system_daily_20131227_0252UTC.1.dar*
#    ./destination/asus_root_system_daily_20131227_0254UTC.1.dar*
#    ./destination/asus_root_system_daily_20131227_0257UTC.1.dar*+
#    ./int.sh
#    ./ignore*
#    ./ignore/ignore.txt*
#    ./test2.sh
#    ./dar_backup.sh~
#    ./dar_backup.sh
#    ./quote.sh
#    ./dar_backup.conf
#
#  * = these don't get added to archive.
#  + = these are incremental

useage="Useage: dar_backup.sh [-c <config filespec>][-i] [-P <prune directory relative to -R>]... \n\t\t<source path> <destination path> <slice base name>\n -i == incremental backup" 

incremental=0
prune=""
CONF=""
while getopts ":c:iP:" opt; do
	case $opt in
	c )	if ! [ -z $OPTARG ] ; then
			CONF="--noconf --batch $OPTARG"
		fi ;;
	i )	incremental=1 ;;
	P )	if ! [ -z $OPTARG ] ; then
			prune="$prune -P $OPTARG"
		fi ;;
	\? )	echo -e $useage 
		exit 1 ;;
	esac		
done
shift $(($OPTIND - 1))

if ! [ -z $1 ] ; then
	SOURCE_PATH=$1
else
	echo -e $useage
	exit 1
fi

if ! [ -z $2 ] ; then
	DESTINATION_PATH=$2
else
	echo -e $useage
	exit 1
fi

if ! [ -z $3 ] ; then
	SLICE_BASE_NAME=$3
else
	echo -e $useage
	exit 1
fi

DATE_STRING=$(/bin/date -u +%Y%m%d_%H%M%Z)
FILE="${DESTINATION_PATH}/${SLICE_BASE_NAME}_${DATE_STRING}"

if [ $incremental -ne 0 ] ; then
	PREV=$(/bin/ls $DESTINATION_PATH/$SLICE_BASE_NAME*.dar|/usr/bin/tail -n 1)
	PREV="-A ${PREV%%.*}"
fi


# echo SOURCE_PATH $SOURCE_PATH
# echo DESTINATION_PATH $DESTINATION_PATH
# echo SLICE_BASE_NAME $SLICE_BASE_NAME
# echo DATE_STRING $DATE_STRING
# echo FILE $FILE
# echo PREV $PREV
# echo PRUNE $prune
echo command: /usr/bin/dar $CONF -R $SOURCE_PATH -c $FILE $PREV $prune -X ${SLICE_BASE_NAME}*.*.dar

# Commands
/usr/bin/dar $CONF -R $SOURCE_PATH -c $FILE $PREV $prune -X ${SLICE_BASE_NAME}*.*.dar
# .... > /dev/null
/usr/bin/dar -t $FILE
# .... > /dev/null
#/usr/bin/find $DIR -type f -exec chmod 400 \{\} \;




