import urllib
import re

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
  while True:
    req = urllib.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+nothing)
    text = req.read()
    pattern = re.compile(r'[0-9]+$')
    nextNum = ''.join(pattern.findall(text))
    if not nextNum:
      return text
    nextNum = str(int(nextNum) / 2) if (int(nextNum) == 16044) else nextNum
    nothing = nextNum
  return nothing

print level4()
