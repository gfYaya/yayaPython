# coding = utf-8

''' UserDict is not the subclass of dict.It’s preferable to subclass from UserDict rather than from dict
is that the built-in has some implementation shortcuts that end up forcing us to override
methods that we can just inherit from UserDict with no problems.'''

# Example 3-8. StrKeyDict always converts non-string keys to str—on insertion, update , and lookup.
