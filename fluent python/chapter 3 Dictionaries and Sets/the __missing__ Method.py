# coding = utf-8

# Example 3-7. StrKeyDict0 converts nonstring keys to str on lookup

class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):  # If str(k) is not an existing key, we’d have an infinite recursion.
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d[2])  # two   => __getitem__ -> __missing__
print(d.get(2))  # two  => get()
print(2 in d)  # True  => __contains__
