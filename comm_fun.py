# coding=utf-8



# 冒泡排序
def bubble_sort(alist):
    for i in range(1, len(alist)):
        for j in range(len(alist) - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    print('冒泡排序：', end=' ')
    print(alist)
    return alist

# dict1 = {'a':'A','b':'B','c':'C','d':'C'}
# newdict = {}
# for key, value in dict1.items():
#     newdict[value] = key
#
# print(newdict)


# g = (x*3 for x in range(10))
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print('没有更过元素了')
#         break

import tkinter
import time

root = tkinter.Tk()
root.geometry('320x320')
msg1 = tkinter.Message(root, text='''我的水平起始位置环境的黄金客户尽快回家共和国好尴尬相对窗口0.2''',
                       font=('黑体',18), relief='sunken')
msg1.place(relx=0.2, y=80, relheight=0.4, width=200)
root.mainloop()
