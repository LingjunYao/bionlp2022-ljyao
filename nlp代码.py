
import time
import requests
from concurrent import futures
import requests
from urllib.request import urlopen
import urllib3
from multiprocessing import Pool
import time
import requests
import urllib.request
import re
'''
file=open('D:\\pubmed1.txt')
pmid=file.readlines()
file2=open('D:\\test.txt','a')
def get_url():
    url_list=[]
    for i in pmid:
        url='https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids='+str(i)
        url_list.append(url)
    return url_list

def get_data(url):
    data=urllib.request.urlopen(url).read()
    data=data.decode("utf-8")
    file2.write(data)
    return 1

s=time.time()
urls=get_url()
executor = futures.ThreadPoolExecutor(max_workers=100)
fs=[]
i=0
for url in urls:
    f=executor.submit(get_data, url)
    fs.append(f)
    i=i+1
    print(i)
futures.wait(fs)

print(time.time()-s)
'''
'''


import requests
from urllib.request import urlopen
from multiprocessing import Pool
import time
import urllib.request
import re
from requests_html import HTMLSession

file=open('d:\\pubmed1.txt')
file2=open('D:\\test.txt','w')
i=0
for line in file.readlines():
    i=i+1
    line=line.strip('\n')
    url='https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids='+str(line)
    data=urllib.request.urlopen(url).read()
    data=data.decode("utf-8")  
    file2.write(data)
    print(i)
file2.close()

'''
'''
#整合文件代码
# -*- coding:utf-8*-
import sys
import os
import os.path
import time
time1=time.time()



##########################合并同一个文件夹下多个txt################
def MergeTxt(filepath,outfile):
    k = open(filepath+outfile, 'a+')
    for parent, dirnames, filenames in os.walk(filepath):
        for filepath in filenames:
            txtPath = os.path.join(parent, filepath)  # txtpath就是所有文件夹的路径
            f = open(txtPath)
            ##########换行写入##################
            k.write(f.read()+"\n")

    k.close()

    print ("finished")
()

if __name__ == '__main__':
    filepath="D:/r/r"
    outfile="result.txt"
    MergeTxt(filepath,outfile)
    time2 = time.time()
    print (u'总共耗时：' + str(time2 - time1) + 's')
'''


import requests
from urllib.request import urlopen
from multiprocessing import Pool
import time
import urllib.request
import re
from requests_html import HTMLSession

file2=open('D:\\test.txt')
disease=open('D:\\disease.txt','w')
gene=open('D:\\gene.txt','w')
chemical=open('D:\\chemical.txt','w')
mutation=open('D:\\mutation.txt','w')
species=open('D:\\species.txt','w')
cellline=open('D:\\cellline.txt','w')


Species = re.compile('Species'+'\t')
Disease = re.compile('Disease'+'\t')
Chemical = re.compile('Chemical'+'\t')
Mutation = re.compile('Mutation'+'\t')
Gene = re.compile('Gene'+'\t')
Cellline = re.compile('Cellline'+'\t')

for line in file2.readlines():
    if(re.search(Species, line, flags=0)):
        species.write(line)
    if(re.search(Disease, line, flags=0)):
        disease.write(line)
    if(re.search(Chemical, line, flags=0)):
        chemical.write(line)
    if(re.search(Mutation, line, flags=0)):
        mutation.write(line)
    if(re.search(Gene, line, flags=0)):
        gene.write(line)
    if(re.search(Cellline, line, flags=0)):
        cellline.write(line)
    
disease.close()
gene.close()
chemical.close()
mutation.close()
species.close()
cellline.close()
