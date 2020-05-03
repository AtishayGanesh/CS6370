from bs4 import BeautifulSoup
import re
import pickle
a = open('Wikipedia-20200423172415.xml','rb')
soup = BeautifulSoup(a,'html.parser')
l = list(soup.find_all('text',attrs={"xml:space":"preserve"} ))
print(len(l))
l_new = []
for s0 in l:
	s = re.sub('==.*==','',s0.text)
	s = re.sub('<ref.*?</ref>','',s)
	s = re.sub('<mat.*?</math>','',s,flags=re.DOTALL)

	s = re.sub('\{\{.*?\}\}','',s)
	s = re.sub('\*\[htt.*','',s)
	s = s.replace('Category:','')
	s = re.sub('\[\[File:.*','',s)
	s = s.replace("|",' ')
	s = s.replace('[','')
	s = s.replace(']','')
	s = s.replace("'''",'')
	s = re.sub(r'\n+','\n',s)
	if len(s)>=75:
		l_new.append(s)

print(len(l_new),l_new[2])
f = open('Wikipedia_cleaned.dat','wb')
pickle.dump(l_new,f)
f.close()
# s = re.sub('===*===','',s)
