y=int(input())
def leap_year(y):
    if (y%4==0) and not (y%100==0) or (y%400==0):
        a="True"
    else:
        a="False"
    return a

print(leap_year(y))
