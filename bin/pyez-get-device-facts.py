from jnpr.junos import Device
import sys

dev = Device('172.16.1.50', user='root', password='hollywd1')

try:
    dev.open()
except Exception as err:
    print "Unable to connect to host:", err
    sys.exit(1)

print dev.facts


dev.close()
