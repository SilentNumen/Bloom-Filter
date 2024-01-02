import random


def cut(list0):
    cutresult = []
    for i in list0:
        list1 = i.split()
        cutresult.append(list1)
    return cutresult

if __name__ == '__main__':
    key = []
    bloomresult = []
    bookfile = ['In 1977 Dalenius articulated a desideratum for statistical databases : nothing about an individual '
                'should be learnable from then database that cannot be learned without access to the database . ',
                'We give a general impossibility result showing that a formalization of Dalenius’ goal along the '
                'lines of semantic security cannot be achieved . ',
                'Contrary to intuition , a variant of the result threatens the privacy even of someonethe database.',
                'This state of affairs suggests a new measure, differential privacy, which, intuitively, captures the '
                'increased risk to one’s privacy incurred by participating in a database . ',
                'In many cases, extremely accurate information about the database can be provided while simultaneously'
                ' ensuring very high levels of privacy .',
                'The techniques developed in a sequence of papers , culminating in those described can achieve any '
                'desired level of privacy under this measure .']

    way = cut(bookfile)
    for i in range(5):
        r = random.sample(way[i], 4)
        for j in r:
            key.append(j)

    print("输入关键词：" + str(key))
    # key0 = input("输入关键字：")
    # key = key0.split()
    print("搜索结果在以下文档中：")
    for i in key:
        print("\n关键词：" + i)
        for j in range(len(way)):
            if i in way[j]:
                print(str(j) + "  " + bookfile[j])
