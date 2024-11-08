#!/usr/bin/python3

import paramiko
import subprocess
import sys


CERTBOT='/usr/bin/certbot'
CERT_DIR_BASE='/etc/letsencrypt/live/'
RENEW_OPT='renew'
RENEW_TEST_OPT="'--dry-run','renew'"

def argCheck():
    # check arg count 
    if len(sys.argv) == 4:
        APPLICATION = sys.argv[1]
        DOMAIN = sys.argv[2]
        CERTFILE = sys.argv[3]
        return True
    else:
        return False 


# cert renew precheckn
def renewPreCheck():
    ret = subprocess.run( [CERTBOT, '--dry-run', 'renew'], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if (ret.returncode == 0):
        return(0)
    else:
        return(1)

# cert renew
def renew():
        ret = subprocess.run( [CERTBOT, 'renew'], 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if (ret.returncode == 0):
            return(0)
        else:
            return(1)


#
# main
#


# argCheck
if (not argCheck()):
    print("usage: renewCertbot.py <application> <domain> <certfile_path>")
    exit(1)

# renew 
if (renewPreCheck()):
    if !(renew()):
        # renewPrecheck ok. but failed renew
        print("failed renew")
        exit(1)
else:
    # renewPrecheck NG.
    print("failed renew precheck")
    exit(1)


