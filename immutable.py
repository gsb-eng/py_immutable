"""
Immutable list with hash function overrided.
"""


class Immutable(object):

    def _immutable(self, *arg, **kw):
        raise TypeError("%s object is immutable" % self.__class__.__name__)

    __delitem__ = __setitem__ = __setattr__ = _immutable


class ImmutableList(Immutable, list):

    def __init__(self, list_val, *arg, **kwargs):
        if not isinstance(list_val, list):
            raise ValueError('%s shold be of list' % str(list_val))
        super(ImmutableList, self).__init__(*arg, **kwargs)
        for val in list_val:
            self.append(val)

    def __new__(self):
        self.append = self._immutable

    def __hash__(self):
        return hash(tuple(self))


if __name__ == '__main__':
    c = ImmutableList([1, 123, 345])

    print(c)
    print(dir(c))
    try:
        c[1] = 11111
    except TypeError:
        print('Type Error')

    d = {c: c}
    print(d[c])
    c.append(321)
    print(d[c])
