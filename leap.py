y=int(input(""))
if(y%400==0 & y%100==0 or y%4==0):
    print(y,"is Leap year")
else:
    print(y,"not a leap year")