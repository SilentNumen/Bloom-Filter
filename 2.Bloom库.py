from pybloom_live import BloomFilter
import mmh3,jieba,random
from bitarray import *
import

allfile='''In 1977 Dalenius articulated a desideratum for statistical databases: nothing about an individual should be learnable from then database that cannot be learned without access to the database. 

We give a general impossibility result showing that a formalization of Dalenius’ goal along the lines of semantic security cannot be achieved. 

Contrary to intuition, a variant of the result threatens the privacy even of someone not in the database. 

This state of affairs suggests a new measure, differential privacy, which, intuitively, captures the increased risk to one’s privacy incurred by participating in a database. 

The techniques developed in a sequence of papers , culminating in those described in , can achieve any desired level of privacy under this measure.

In many cases, extremely accurate information about the database can be provided while simultaneously ensuring very high levels of privacy.'''

ban=['',' ','.','\n',':',',']
slist=list(filter(None, allfile.split('\n'))) #文章变list

bflist = [] #用于存放每个文件对应的bloom对象实例
for ss in slist:
    bf = BloomFilter(capacity=50)
    jiebalist = list(filter(lambda x: x not in ban, jieba.lcut(ss)))#jieba分词
    for word in jiebalist:
        bf.add(word) #每个单词都添加到改bloom里面
    bflist.append(bf)

inputkey=input("输入关键词:")
inputkey=list(filter(lambda x: x not in ban, jieba.lcut(inputkey)))
print("关键词分割结果:{}".format(inputkey))

for key in inputkey:
    for filebf in bflist:
        if key in filebf:#通过库函数自带的in 判断是否在该bloom过滤器中
            print("关键词{}出现在{}".format(key,bflist.index(filebf)))
