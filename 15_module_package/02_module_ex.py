# import show_info
# show_info.show_name()
# show_info.show_phone()


# from show_info import show_name, show_phone
# show_name()
# show_phone()


import show_info as si
si.show_name()
si.show_phone()


from show_info import *
show_name()


from show_info import show_phone as sp
sp()
show_phone()

sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break