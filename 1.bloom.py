from bitarray import bitarray
import mmh3


def cut(list0):
    cutresult = []
    for i in list0:
        list1 = i.split()
        cutresult.append(list1)
    return cutresult


class bloom_filter(object):
    def __init__(self, size, hash_count):
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)
        self.size = size
        self.hash_count = hash_count

    def add(self, item):
        for i in range(self.hash_count):
            index = (mmh3.hash(item, i) % self.size)
            self.bit_array[index] = 1
        return self

    def contains(self, item):
        out = True
        for i in range(self.hash_count):
            index = (mmh3.hash(item, i) % self.size)
            if self.bit_array[index] == 0:
                out = False
        return out


def get_bloom(num, list0, list1):
    bloomfile = bloom_filter(1000, 3)
    for j in list0:
        bloomfile.add(j)
    print("文件 "+str(num)+" ："+str(bloomfile.bit_array)+"  关键词是否在该数组中：", end='')
    for k in list1:
        if bloomfile.contains(k):
            print("YES!")
            return True
    print("NO!")
    return False


if __name__ == '__main__':
    bloomresult = []
    bookfile = ['In 1977 Dalenius articulated a desideratum for statistical databases : nothing about an individual should be learnable from then database that cannot be learned without access to the database .',
                'We give a general impossibility result showing that a formalization of Dalenius ’ goal along the lines of semantic security cannot be achieved .',
                'Contrary to , a variant of the result threatens the privacy even of someonenot in the database . ',
                'This state of affairs suggests a new measure , differential privacy , which , intuitively , captures the increased risk to one ’ s privacy incurred by participating in a database .',
                'The techniques developed in a sequence of papers , culminating in those describedin , can achieve any desired level of privacy under this measure .',
                'In many cases , extremely accurate information about the database can be provided while simultaneously ensuring very high levels of privacy .']

    key0 = input("输入关键词：")
    key = key0.split()

    cutresult = cut(bookfile)
    for i in range(len(cutresult)):
        if get_bloom(i, cutresult[i], key):
            bloomresult.append(str(i))
    print("搜索结果在以下文档中：")
    for k in bloomresult:
        print(k+"  "+bookfile[int(k)])
