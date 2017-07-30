# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:12:40 2016

@author: FANG
"""
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''


import pickle
shoplistfile='shoplist.data'
shoplist=['apple','mango','carrot']

f=open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close

del shoplist

f=open(shoplistfile,'rb')
storedlist=pickle.load(f)
print(storedlist)

import io
f=io.open("abc.txt","wt",encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text=io.open("abc.txt",encoding="utf-8").read()

print(text)