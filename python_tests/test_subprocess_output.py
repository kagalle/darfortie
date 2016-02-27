# results of test:
#   ken@asus ~/darfortie_script $ ./test_subprocess_output.py > 1.out
#   test going into stderr
#   ken@asus ~/darfortie_script $ ./test_subprocess_output.py 2> 2.out
#   test going to stdout
#   ken@asus ~/darfortie_script $ cat 1.out 
#   test going to stdout
#   ken@asus ~/darfortie_script $ cat 2.out
#   test going into stderr
#   ken@asus ~/darfortie_script $
#
# The output to both stdout and stderr get passed though the python script
# into the shell as you would hope for, without doing anything special
# with subprocess.call().

#!/usr/bin/python
import subprocess
return_code = subprocess.call('./test_stdout_stderr.py', shell=False)

