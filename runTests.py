import subprocess as sp
import os.path
import sys

runPath = "../"
ignore = ["README.md",".git",".gitignore","runTests.py"]

if __name__ == "__main__":
  
  testPath = os.getcwd() + "/" + sys.argv[0][:-11]
  os.chdir(testPath)
  os.chdir(runPath)
  
  files = os.listdir(testPath)
  ignored = []
  incorrect = []
  badformat = []
  correct = 0
  for fl in files:
    flst = fl.strip().split('.')
    if flst[0] == "valid":
      p = sp.Popen("./simple < " + testPath + fl + " > /dev/null", shell=True, stdout=sp.PIPE, stderr = sp.STDOUT)
      line = p.stdout.readline()
      if line == "":
        print '.',
        correct += 1
      else:
        print 'x',
        incorrect.append("Got the error: <" + line[:-1] +  "> for the valid file: " + fl)
    elif flst[0] == "invalid":
      p = sp.Popen("./simple < " + testPath + fl + " > /dev/null", shell=True, stdout=sp.PIPE, stderr = sp.STDOUT)
      line = p.stdout.readline()
      if line == "":
        print 'x',
        incorrect.append("Got no error for the invalid file: " + fl)
      elif flst[1].isdigit():        
        ln = line.strip().split()
        if ln[-1].isdigit():
          if ln[-1] == flst[1]:
            print '.',
            correct += 1
          else:
            print 'x',
            incorrect.append("Error line number in message: <" + line[:-1] + "> doesn't match with that expected by file: " + fl)
        else:
          print '~',
          badformat.append("Error message: <" + line[:-1] + "> doesn't end with the line number")
      else:
        print '~',
        badformat.append("File : <" + fl + "> doesn't have the expected format : \"invalid.error_line_number.name\" (eg: invalid.1.func_error)")
    else:
      if not fl in ignore:
        ignored.append("File: <" + fl + "> was ignored as it didn't begin with valid or invalid")

  print "\nCorrect: " + str(correct) + "; Incorrect: " + str(len(incorrect)) + "; Format errors: " + str(len(badformat)) + "; Ignored: " + str(len(ignored)) + "\n"

  for f in incorrect:
    print f
  if len(incorrect) > 0:
    print "------------------"

  for f in badformat:
    print f
  if len(badformat) > 0:
    print "------------------"
  for f in ignored:
    print f
