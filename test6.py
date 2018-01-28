# 【程序5】
# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
# 1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 　　　　　　然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

x = int(input('input first no:'))
y = int(input('input second no:'))
z = int(input('input third no:'))
# if(x < y):
#     if(x < z):
#         if(y < z):
#             print(x,y,z)
#         else: print(x,z,y)
#     else:
#         print(z,x,y)
# else:
#     if(y < z):
#         if( x < z):
#             print(y,x,z)
#         else: print(y,z,x)
#     else:
#         print(z,y,x)




