#dict_popitem
#popitem类似于list.pop,后者会返回列表的最后一个元素，但不同的是，popitem返回的是随机项。
#因为字典没有顺序的概念和所谓的“最后的元素”。

d={'adam':89,'lisa':67,'bart':27,'paul':56,'name':'dcy','age':67}
print(len(d))
while len(d)!=0:
    key,value=d.popitem()#调用popitem方法随机删除键-值对（项）并以元组的形式返回,将其直接赋值给key和value。
    print(key,value)
    print(d.keys())#keys()方法将字典中的键以列表的形式返回，iterkeys则返回针对键的迭代器。
    print(d.values())#values方法以列表的形式返回字典中的值，itervalues返回值得迭代器。
print(d)
x={'names':'hadescat'}
d.update(x)#利用一个字典项更新另外一个字典，提供的字典中的项会被添加到旧的字典中，若有相同的键则会进行覆盖。
print(d)

pass

pass
