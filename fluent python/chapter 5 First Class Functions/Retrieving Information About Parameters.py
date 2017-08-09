# coding = utf-8

# Example 5-15. Function to shorten a string by clipping at a space near the desired length

def clip(text: str, max_len: 'int>0' = 80) -> str:
    """Return text clipped at the last space before or after max_len"""
    end = None
    if len(text) > max_len:
        # return the highest index in the string where substring `sub` is found, such that `sub` is contained
        #    within [`start`, `end`].
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after

    if end is None:  # # no spaces were found
        end = len(text)
    return text[:end].rstrip()


# Example 5-19. Annotated clip function
print(clip.__annotations__)

# Example 5-16. Extracting information about the function arguments

print(clip.__defaults__)
print(clip.__code__)  # doctest: +ELLIPSIS
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

# Example 5-17. Extracting the function signature

from inspect import signature

# Get a signature object for the passed callable.
sig = signature(clip)
print(sig)
print(str(sig))
for name, params in sig.parameters.items():
    print(params.kind, ':', name, '=', params.default)


# supplement
def f(a, *, b):
    return a + b


f_sig = signature(f)
for name, params in f_sig.parameters.items():
    print(params.kind, ':', name, '=', params.default)

    # POSITIONAL_OR_KEYWORD : a = <class 'inspect._empty'>
    # KEYWORD_ONLY : b = <class 'inspect._empty'>
