"""
Immutable list with hash function overrided.
"""


class Immutable(object):

    def _immutable(self, *arg, **kw):
        raise TypeError("%s object is immutable" % self.__class__.__name__)

    __delitem__ = __setitem__ = __setattr__ = _immutable


class ImmutableList(list):

    def __init__(self, *arg, **kwargs):
        super(ImmutableList, self).__init__(*arg, **kwargs)

    def __hash__(self):
        return hash(tuple(self))


c = ImmutableList()
c.append(1)
c.append(123)
c.append(345)
print('Printing')
print(c)

try:
    c[1] = 11111
except TypeError:
    print('Type Error')

d = {c: c}
print(d)
