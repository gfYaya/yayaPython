# coding = utf-8

# Example 7-1. A decorator usually replaces a function with a different one

def deco(func) -> 'this is a decorator':
    def inner():
        print('running inner')

    return inner


@deco
def target():
    print("running target")


target()
print(target)  # Inspection reveals that target is a now a reference to inner.

test = target()
# print(test()) # decorators can be executed immediately when a module is loaded
