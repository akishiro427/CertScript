!/usr/bin/python3

import argparse
import os
import requests
import subprocess
import sys


BASE_URL="http://<IP>"

def chkArgs():
    """
    - parsing args
      - args
        - action args: -c(heck) or -r(enew)
        - require args: -a(--aplication) <application name>, -d(--domain) <domain name> 
      - returns 
        - <action>   # <action> will be returned "check" or "renew"
        - <applicaation name> 
        - <domain name>
    """


    # required options
    parser = argparse.ArgumentParser(description='Certification renew and latest certification check script')
    parser.add_argument('-a', '--application',required=True)
    parser.add_argument('-d', '--domain', required=True)

    # exclusive options
    argument_group = parser.add_argument_group("action")
    exclusive_group = argument_group.add_mutually_exclusive_group(required=True)
    exclusive_group.add_argument('-c', action='store_true')
    exclusive_group.add_argument('-r', action='store_true')

    args = parser.parse_args()
    if (args.c):
      return 'check', args.application, args.domain
    else:
      return 'renew', args.application, args.domain


# cert renew precheckn
def renewPreCheck():
    ret = subprocess.run( [CERTBOT, '--dry-run', 'renew'], 
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if (ret.returncode == 0):
        return(True)
    else:
        return(False)



def getLatestCertificateDate(application, domain):
    API_URL=BASE_URL + '/certs/latest'

 
    data={'application':application,'domain':domain}
    res=requests.get(API_URL, params=data)
 
    print(res.json())
    pass


def renew_certificate(application, domain):
    CERT_DIR_BASE='/etc/letsencrypt/live'
    CERT_FILES=("fullchain.pem","privkey.pem")
    CERTBOT='/usr/bin/certbot'
    RENEW_TEST_OPT="'--dry-run','renew'"
    pass

#
# main
#


# Check args
action, application, domain = chkArgs()

if (action == "check"):
  getLatestCertificateDate(application, domain)
else:
  renew_certificate(application, domain)

exit(0)
