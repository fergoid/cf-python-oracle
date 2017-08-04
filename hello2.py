"""
A first simple Cloud Foundry Flask app

Author: Ian Huston
License: See LICENSE.txt

"""
import os

myfile = open(os.environ['FILE_LOCATION'] + '/readme.md')
sf = str(myfile)
home = str(os.environ['HOME'])
listing = os.listdir(os.environ['HOME'])
listing2 = os.listdir(os.environ['ORACLE_HOME'])

print "hello world!"
print sf
print home
print os.getcwd()
print listing
print listing2