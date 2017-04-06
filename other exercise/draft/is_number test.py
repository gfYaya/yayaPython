# coding=utf-8

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    # 个人认为,可写可无
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


print(is_number("NULL"))
