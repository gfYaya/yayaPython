try:
    raise NameError("HiThere")
except NameError as ne_err:
    print("An exception flew by")
    # 'raise' here,the aim is to re_raise the exception
    raise
