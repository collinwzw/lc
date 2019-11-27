import collections

o_d = collections.OrderedDict()

o_d.update({'banana': 3})
o_d.update({'apple': 4})
o_d.update({'pear': 1})
o_d.update({'orange': 2})

print(o_d.popitem(last = False))