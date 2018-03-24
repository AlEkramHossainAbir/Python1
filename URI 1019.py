#program name: URI 1019 Time Conversion
#author name: Al- Ekram Hossain Abir
"""
hour=int(0)
sec=int(input())
minute=int(0)
if sec>=60:
    minute=sec//60;    
    sec=sec%60
    if minute>=60:
        hour=minute//60;
        minute=minute%60
    print("{}:{}:{}".format(hour,minute,sec))
else:
     print("{}:{}:{}".format(hour,minute,sec))
   
 """
a= int(input())
hour=a//3600
m=a%3600
minute=m//60
sec=m%60
print(hour,minute,sec)

print("{}:{}:{}".format(hour,minute,sec))
