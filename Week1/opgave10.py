import re
stringtest = 'atgtcgggctaaattagagccagtcacacttagaataagtagattgatagggaccatctcaactctaaatgtatccattgtgtag'
#atg = 'atg'
#tag = 'tag'
#tta = 'tta'
#tga = 'tga'
#
##for c in str:
#
#
#print(str.find(atg))
#print(str.find(tag))
#print(str.find(tta))
#print(str.find(tga))

#proberen om te laten zien hoeveel van elk er is

test = re.match(r'(?=atg)',stringtest)
if test:
    print('atg: found', test.group())
else:
    print('no')



#line = "Cats are smarter than dogs"

#matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

#if matchObj:
#   print("matchObj.group() : ", matchObj.group())
 #  print ("matchObj.group(1) : ", matchObj.group(1))
  # print ("matchObj.group(2) : ", matchObj.group(2))
#else:
 #  print ("No match!!")