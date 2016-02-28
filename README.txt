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
  
  
The first backup is created without the incremental option (-i).
Further incremental backups are created using the -i option and the SAME (base) name.  
  Darfortie adds the date/time to the final name to make it unique.
  It relies on this naming convension to find the reference backup it should use.
  
