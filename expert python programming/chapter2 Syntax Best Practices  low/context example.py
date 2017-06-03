# coding = utf-8

from contextlib import contextmanager


@contextmanager
def logged(klass, logger):
    # logger
    def _log(f):
        def __log(*args, **kw):
            logger(f, args, kw)
            return f(*args, **kw)

        return __log

    # let's equip the class
    for attribute in dir(klass):
        if attribute.startswith('_'):
            continue
        # Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
        element = getattr(klass, attribute)
        setattr(klass, '__logged_%s' % attribute, element)
        setattr(klass, attribute, _log(element))

    # let's work
    yield klass

    # let's remove the logging
    for attribute in dir(klass):
        if not attribute.startswith('__logged_'):
            continue
        element = getattr(klass, attribute)
        setattr(klass, attribute[len('__logged_'):], element)
        setattr(klass, attribute)
