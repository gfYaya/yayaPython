# coding = utf-8

class Chainer(object):
    def __init__(self, methods, callback=None):
        self._methods = methods
        self._callback = callback

    def __get__(self, instance, owner):
        if instance is None:
            # only for instances
            return self

        results = []
        for method in self._methods:
            results.append(method(instance))
            if self._callback is not None:
                if not self._callback(instance, method, results):
                    break
        return results


class TextProcessor():
    def __init__(self, text):
        self.text = text

    def normalize(self):
        """
        Return whether an object is an instance of a class or of a subclass thereof.

        A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
        check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
        or ...`` etc.
        """
        if isinstance(self.text, list):
            self.text = [t.lower() for t in self.text]
        else:
            self.text = self.text.lower()

    def split(self):
        if not isinstance(self.text, list):
            self.text = self.text.split()

    def treshold(self):
        if not isinstance(self.text, list):
            if len(self.text) < 2:
                self.text = ''

        self.text = [w for w in self.text if len(w) > 2]


def logger(instance, method, results):
    print("calling s%" % method._name_)
    return True


def add_sequence(name, sequence):
    # setattr(x, 'y', v) is equivalent to ``x.y = v''
    setattr(TextProcessor, name, Chainer([getattr(TextProcessor, n) for n in sequence], logger))
