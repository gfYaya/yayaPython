# coding = utf-8

# Example 5-10. tag generates HTML; a keyword-only argument cls is used to pass
#   “class” attributes as a workaround because class is a keyword in Python

def tag(name, *content, cls=None, **attrs):
    """Generates on or more HTML Tag"""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


# Example 5-11. Some of the many ways of calling the tag function from Example 5-10

print(tag('br'))
print(tag('p'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name="img"))
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))
