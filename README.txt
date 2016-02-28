This is BETA software.  Use at your own risk.  Please:
  1.  Test for suitability before using for "real" data.
  2.  During testing, use "dar -d ..." to compare the created backup against the filesystem.
  3.  For testing, do a complete restore to a separate filesystem and compare results.
  
This is only a front-end for the dar utility (http://dar.linux.free.fr/).
It is meant to facilitate a more convienent backup strategy, typically one run periodically by a cron task.

The Python version is in the "darfortie" directory and is the newest version and most feature rich.
This can be run by calling:
  python [path-leading-to-darfortie/]darfortie

There is an older bash version in the "bash_version" directory, kept for historical reasons.

Two packaged versions, done according to
http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html
have also been made:

darfortie.zip can be run by calling:
  python darfortie.zip
  
python executable bin/darfortie can be run by calling:
  python bin/darfortie
  
----------------------
  
The first backup is created without the incremental option (-i).
Further incremental backups are created using the -i option and the SAME (base) name.  
  Darfortie adds the date/time to the final name to make it unique.
  It relies on this naming convension to find the reference backup it should use.
  
----------------------

It is suggested that for the base name you adopt a convension such as:
  machine_daily
where "machine" is the machine name being backed up, and "daily" is for daily incremental backups.
The end result would be a names such as:
  machine_daily_20160228T0352UTC.1.dar
  machine_daily_20160228T0403UTC_based_on_20160228T0352UTC.1.dar
