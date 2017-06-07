# coding = utf-8

class DistinctError(Exception):
    pass


class distinctdict(dict):
    def __setitem__(self, key, value):
        try:
            value_index = self.values().index(value)

        except ValueError:
            pass
