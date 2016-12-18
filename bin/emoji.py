"""
emoji.py

This serves as the main file for the emoji interpreter.
@author Jen Lamere & Nick Rabb
"""

import sys
import getopt
import urllib2

mode = ""

def main():
  """The main function of the program."""
  files = []
  try:
    opts, args = getopt.getopt(sys.argv[1:], "h", ["help"])
  except getopt.error, msg:
    print msg
    print "for help use --help"
    sys.exit(2)
  # process options
  # valid options: -h, -c
    for o, a in opts:
        if o in ("-h", "--help"):
          print __doc__
          sys.exit(0)
        elif o in ("-c", "--compile"):
          mode = "c"
  # process arguments
  for arg in args:
    process_arg(arg, files)
  # check for updates
#TODO: Figure out if we want people to be able to get updates automatically
  #check_updates()

def process_arg(arg, files):
  """Process an argument passed to the program."""
  #TODO: Implement
  print "Processed arg %s" % arg
  if mode == "c":
    files.append(arg)

def check_updates():
  filecontents = urllib.urlopen("https://github.com/RickNabb/emoji-interpreter/blob/installation/bin/emoji.py").read()
