# coding = utf-8

# Example 7-23. To accept parameters, the new register decorator must be called as a function

registry = set()


def register(active=True) -> 'parameter':
    def decorate(func) -> 'function':
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func

    return decorate


# @register(active=False)
@register(False)  # The @register factory must be invoked as a function, with the desired parameters.
def f1():
    print('f1')


@register()
def f2():
    print('f2')


def f3():
    print('f3')


@register
def f4():
    print('f4')


# Example 7-24. Using the registration_param module listed in Example 7-23
#  function currying like js?

print(registry)
print(register()(f3))
print(register(True)(f3))
print(register(active=False)(f2))
print(registry)
