# import re
# stringtest = 'atgtcgggctaaattagagccagtcacacttagaataagtagattgatagggaccatctcaactctaaatgtatccattgtgtag'
#atg = 'atg'
#tag = 'tag'
#tta = 'tta'

#
##for c in str:
#
#
#print(str.find(atg))
#print(str.find(tag))
#print(str.find(tta))
#print(str.find(tga))

#proberen om te laten zien hoeveel van elk er is


tga = 'tgatgatga'
import random

def naam():
    for x in range (0,1):
        print("atg", end="", flush=True)
        for x in range(0,100):
            genes = ["a", "t", "g", "c"]
            print(random.choice(genes), end="",flush=True)
    return

print(naam().find(tga))

#
# test = re.match(r'(?=atg)',stringtest)
# if test:
#     print('atg: found', test.group())
# else:
#     print('no')



#line = "Cats are smarter than dogs"

#matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

#if matchObj:
#   print("matchObj.group() : ", matchObj.group())
 #  print ("matchObj.group(1) : ", matchObj.group(1))
  # print ("matchObj.group(2) : ", matchObj.group(2))
#else:
 #  print ("No match!!")