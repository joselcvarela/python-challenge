import urllib
import re
import pickle
import zipfile

def level0():
  data = ""
  with open('00.txt', 'r') as f:
    data = f.read()
  return eval(data)

def level1():
  text = ""
  with open('01.txt', 'r') as f:
    text = f.read()
  res = ""
  for l in text:
    if ord(l) < ord('a') or ord(l) > ord('z') :
      res += l
    else:
      res += chr(ord(l) + 2)
  return res

def level2():
  text = ""
  with open('02.txt', 'r') as f:
    text = f.read()
  pattern = re.compile(r'[A-Za-z]', re.IGNORECASE)
  return ''.join(pattern.findall(text))

def level3():
  text = ""
  with open('03.txt', 'r') as f:
    text = f.read()
  pattern = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
  return ''.join(pattern.findall(text))

def level4():
  nothing = "12345"
  pattern = re.compile(r'[0-9]+$')
  while True:
    req = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothing)
    text = req.read()
    nextNum = ''.join(pattern.findall(text))
    if not nextNum:
      return text
    nextNum = str(int(nextNum) / 2) if (int(nextNum) == 16044) else nextNum
    nothing = nextNum
  return nothing

def level5():
  res = ""
  obj = pickle.load(open('05.p', 'rb'))
  for i in obj:
    res += ''.join(char * n for char, n in i) + '\n'
  return res

def level6():
  folder = zipfile.ZipFile('06.zip', 'r')
  nextFile = '90052'
  pattern = re.compile(r'[0-9]+$')
  res = ''
  finalres = ''
  char = ''
  while True:
    char = folder.getinfo(nextFile + '.txt').comment
    res += char
    if ord(char) > ord('A') and ord(char) < ord('z') and char not in finalres:
      finalres += char
    ff = folder.read(nextFile + '.txt')
    nextFile = ''.join(pattern.findall(ff))
    if not nextFile:
      print res
      return finalres
  return res

print level6()
