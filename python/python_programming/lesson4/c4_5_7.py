"""Exception"""
l = [1, 2, 3]
i = 5
try:
    () + l
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print(ex)
except Exception as ex:
    print("other:{}".format(ex))