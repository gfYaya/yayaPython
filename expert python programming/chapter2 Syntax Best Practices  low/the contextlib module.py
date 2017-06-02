# coding = utf-8

from contextlib import contextmanager


# from __future__  import with_statement

# @contextmanager is a decorator that enchances a generator that provides both __enter__ and
#    __exit__ parts,separated by a yield statement
@contextmanager
def context():
    print('entring then zone')
    try:
        yield
    # except Exception, e:
    except Exception as e:
        print('with an error %s' % e)
        raise e
    else:
        print('with no error')
