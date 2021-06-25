#!/usr/bin/python3
# AUTHOR: Edson manners
# TODO: Use an array for systems on the subnet for beginners we can add a DB later
#
# MAC DB: https://macaddress.io/database-download

import os
import subprocess
#--
#-----------------------------------------------------
#import Host
class Host:
  def __init__(self, name, ip, mac):
    self.name = name
    self.ip = ip
    self.mac = mac
  def print(self):
    print(self.name, self.ip, self.mac, sep='=')
#-----------------------------------------------------
#import Ip
class Ip:
  def __init__(self, ip, mask):
    self.ip = ip
    self.mask = mask
#-----------------------------------------------------

# TODO: Need ot strip brackets from ip
def runCommand(cmd):
  result = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  output,err = result.communicate()
  output = str(output).split('\\n')
  del output[-1]
  return output

#------------------------------MAIN---------------------------------
print('Welcome to HiveClone')

hosts = []

command = '/usr/sbin/arp -a | sort'
arpEntries = runCommand(command)

for line in arpEntries:
  hosts.append( Host(line.split(' ')[0], line.split(' ')[1][:-1][1:], line.split(' ')[3]) )

for host in hosts:
  host.print()
