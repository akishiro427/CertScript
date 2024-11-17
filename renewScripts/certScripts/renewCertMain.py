import argparse
import getLatestCertDate as cDate
import renewCert as rCert


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



#
# main
#


# Check args
action, application, domain = chkArgs()

if (action == "check"):
    code, msg = cDate.getLatestCertDate('localhost:8080', application, domain).getLatestCertDate()
else:
    code, msg = rCert.renewCert('localhost:8080', application, domain).renew()

print(msg)
exit(code)

