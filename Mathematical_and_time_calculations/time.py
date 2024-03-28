
def second(times):
    t={}
    t['h']=int(times/3600)
    times=times%3600
    t['m']=int(times/60)
    t['s']=int(times%60)
    return t

def time(h,m,s):
    h=h*3600
    m=m*60
    r=h+m+s
    return r

def summation(h,m,s,hh,mm,ss):
    h = h * 3600
    m = m * 60
    hh=hh*3600
    mm=mm*60
    r = h + m + s+hh+mm+ss
    return r


def Subtraction(h,m,s,hh,mm,ss):
    h = h * 3600
    m = m * 60
    hh = hh * 3600
    mm = mm * 60
    r =( h + m + s )- (hh + mm + ss)
    return r



def menu():
    op=int(input('Time calculations:\n1 sum of two time\n2 Subtraction of two time\n3 Convert seconds to time\n4 Convert time to seconds\n5 exit\n---------------------\n Enter one of top Options:\n'))
   
    if op==1:
        print('Please enter two times:\n')
        hour = int(input("enter first  hour : "))
        minute = int(input("enter first Minutes : "))
        second = int(input("enter first Seconds :"))
        hh = int(input("enter second hour : "))
        mm = int(input("enter secound Minutes : "))
        ss = int(input("enter enter seconds:"))
        print("sum of two time: ", summation(hour, minute, second,hh,mm,ss))
        menu()

    elif op==2:
        print('Please enter two times:\n')
        hour = int(input("enter first  hour : "))
        minute = int(input("enter first Minutes : "))
        second = int(input("enter first Seconds :"))
        hh = int(input("enter second hour : "))
        mm = int(input("enter secound Minutes : "))
        ss = int(input("enter second Seconds :"))
        print("Subtraction of two time: ", Subtraction(hour, minute, second, hh, mm, ss))
        menu()

    elif op==3:
        times=int(input('Please enter time in seconds:'))
        c=second(times)
        print(c['h'],':',c['m'],':',c['s'])
        menu()

    elif op==4:
        print('Please enter the following times:')
        hour=int(input("hour : "))
        minute=int(input("Minutes : "))
        second=int(input("Seconds :"))
        print("Time in seconds : ",time(hour,minute,second))
        menu()

    else:
        exit()

menu()
