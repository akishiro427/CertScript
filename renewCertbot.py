#!/usr/bin/python3

import os
import paramiko
import subprocess
import sys

APPLICATION = ""
CERTBOT='/usr/bin/certbot'
CERT_DIR_BASE='/etc/letsencrypt/live'
CERT_FILES=("fullchain.pem","privkey.pem")
DOMAIN = ""
RENEW_OPT='renew'
RENEW_TEST_OPT="'--dry-run','renew'"

def chkArgs():
    global APPLICATION
    global DOMAIN

    # check arg count 
    if len(sys.argv) == 3:
        APPLICATION = sys.argv[1]
        DOMAIN = sys.argv[2]
        return True 
    else:
        return False


# cert renew precheckn
def renewPreCheck():
    ret = subprocess.run( [CERTBOT, '--dry-run', 'renew'], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if (ret.returncode == 0):
        return(True)
    else:
        return(False)

# cert renew
def renew():
        ret = subprocess.run( [CERTBOT, 'renew'], 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if (ret.returncode == 0):
            return(True)
        else:
            return(False)

# check cert file
def chkCertFile():
    for file in CERT_FILES:
        if (not os.path.isfile(CERT_DIR_BASE + "/" + DOMAIN + "/" + file)):
            return(False, file + " not found.")

    return(True, "exist cert files.")



#
# main
#


# Check args
if (not chkArgs()):
    print("usage: renewCertbot.py <application> <domain>")
    exit(1)

if (renewPreCheck()):
    if (not renew()):
        # renewPrecheck ok. but failed renew
        print("failed renew")
        exit(1)
else:
    # renewPrecheck NG.
    print("failed renew precheck")
    exit(1)

# Check certfile
ret, msg = chkCertFile()
if (not ret):
    print(msg)
    exit(1)



