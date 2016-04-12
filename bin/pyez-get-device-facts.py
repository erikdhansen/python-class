from jnpr.junos import Device
import sys
import getpass

print('If in doubt, use the following:')
print('host=10.0.0.60 password=Password!')
print
host = raw_input('Enter hostname/IP: ')
passwd = getpass.getpass('Password: ')


dev = Device(host, user='root', password=passwd) 
try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

print dev.facts


dev.close()
