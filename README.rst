darfortie
=========

Darfortie is a front-end for the dar (Disk ARchive) utility
(http://dar.linux.free.fr/). It adds functionality to the dar utility
and makes it simpler to use for creating incremental backups. It is
meant to facilitate a more convienent backup strategy, typically one run
periodically by a cron task.

The utility can be run repeatedly with the same parameters, and each run
will generate a new incremental archive based on the last one created.
It will search the directory where the current archive is being created
for past reference archives, or a directory can be specified to search
in (-I).

The first backup is created without the incremental option (-i).

Further incremental backups are created using the -i option and the
**same** (base) name. Darfortie adds the date/time to the final name to
make it unique. It relies on this naming convention to find the most
recent reference backup it should use.

--------------

It is suggested that for the base name you adopt a convention such as:

    ``machine_daily``

where “``machine``” is the machine name being backed up, and “``daily``”
is for daily incremental backups. The end result would result in names
like:

-  ``machine_daily_20160228T0352UTC.1.dar``
-  ``machine_daily_20160228T0403UTC_based_on_20160228T0352UTC.1.dar``

--------------

A configuration file can be passed through to dar by using the -c
switch. If not specified, dar will search for and use any dar
configuration file it normally would (ie. /etc/darrc, ~/.darrc). See the
dar man page for details on its structure (“CONDITIONAL SYNTAX”).

It also allows you to pass thru dar prune paths.

--------------

The Python version is in the “darfortie” directory and is the newest
version and most feature rich.

Darfortie can be run by calling:

    ``python [path-leading-to-darfortie/]darfortie``

for a complete list of options:

    ``python darfortie --help``

| Two packaged versions, done according to
| http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html
| have also been made:

darfortie.zip can be run by calling:

    ``python darfortie.zip``

The Python executable bin/darfortie can be run by calling:

    ``python bin/darfortie``

--------------

This is BETA software. Use at your own risk. Please:

#. Test for suitability before using for “real” data.
#. During testing, use “dar -d …” to compare the created backup against
   the filesystem.
#. For testing, do a complete restore to a separate filesystem and
   compare results.

--------------

There is an older bash-based version in the “bash\_version” directory,
kept ONLY for historical reasons.

--------------

There is currently no restore option - use the dar utility directly to
do restores.

--------------