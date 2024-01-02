import random
from pyDes import des, CBC, PAD_PKCS5
import binascii


def des_encrypt(s, KEY):
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s.encode(), padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode()


def des_descrypt(s, KEY):
    secret_key = KEY
    iv = secret_key
    k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode()


def cut(list0):
    cutresult = []
    for i in list0:
        list1 = i.split()
        cutresult.append(list1)
    return cutresult


if __name__ == '__main__':
    key0 = []
    key = []
    result = []
    res_key = 'admin123'
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
            key0.append(j)

    print("输入关键词：" + str(key0))
    # key0 = input("输入关键字：")
    # key0 = key0.split()
    for i in key0:
        key.append(des_encrypt(i, res_key))

    for i in key:
        content = des_descrypt(i, res_key)
        for j in range(len(way)):
            if content in way[j]:
                if str(j) not in result:
                    result.append(str(j))

    print("搜索结果在以下文档中：")
    for k in result:
        print(k + "  " + bookfile[int(k)])
