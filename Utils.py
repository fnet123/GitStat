import subprocess
import time
import sys
import platform
import os

def getPipOutput(cmds, quiet = False):
    start = time.time()
    if not quiet and os.isatty(1):
        # print('>> ' + ' | '.join(cmds))
        sys.stdout.flush()
    p = subprocess.Popen(cmds[0], stdout = subprocess.PIPE, shell = True)
    processes=[p]
    for x in cmds[1:]:
        p = subprocess.Popen(x, stdin = p.stdout, stdout = subprocess.PIPE, shell = True)
        processes.append(p)
    output = p.communicate()[0]
    for p in processes:
        p.wait()
    end = time.time()
    if not quiet:
        if os.isatty(1):
            # print('\r')
            pass
        print('[%.5fs] >> %s' % (end - start, ' | '.join(cmds)))

    return output.decode('UTF-8').rstrip('\n')