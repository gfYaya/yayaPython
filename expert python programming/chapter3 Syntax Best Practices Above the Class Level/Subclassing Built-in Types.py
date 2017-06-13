# coding = utf-8

class DistinctError(Exception):
    pass


class distinctdict(dict):
    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)
            existing_key = self.keys()[value_index]
            if existing_key != key:
                raise DistinctError(("This value already exists for '%s'") % str(self[existing_key]))

        except ValueError:
            pass

        super(distinctdict, self).__setitem__(key, value)


my = distinctdict()
my['key'] = 'value'
# my['other_key'] = 'value' # AttributeError: 'dict_values' object has no attribute 'index'
my['other_key'] = 'value2'
print(my)
