# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
# 　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 1.程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊
# 　　　　　　情况，闰年且输入月份大于3时需考虑多加一天。

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
time = input('input year/month/day:')
# year = int(input('input year:'))
# month = int(input('input month:'))
# day = int(input('input day:'))
# print(type(time),type(time[0:4]))
year = int(time[0:4])
month = int(time[4:6])
day = int(time[6:8])
month = month - 1
sum = months[month] + day
if(year % 400 ==0 or (year % 4 ==0) and (year % 100 != 0)):
    sum = sum + 1
print('day is:',sum)
