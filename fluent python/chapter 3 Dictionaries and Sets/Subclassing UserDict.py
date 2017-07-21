# coding = utf-8

''' UserDict is not the subclass of dict.It’s preferable to subclass from UserDict rather than from dict
is that the built-in has some implementation shortcuts that end up forcing us to override
methods that we can just inherit from UserDict with no problems.'''

# Example 3-8. StrKeyDict always converts non-string keys to str—on insertion, update , and lookup.

import collections


class StrKeyDict(collections.UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item


d = StrKeyDict([('2', 'two'), ('4', 'four')])
print(d[2])  # two   => __getitem__ -> __missing__
print(d.get(2))  # two  => get()
print(2 in d)  # True  => __contains__

print(d['2'])  # 未执行 __missing__
print(d[3])
