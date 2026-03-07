def fun(a :int,b : int) -> int:
    value_min =int((21*a*30)*b/60)
    value_sec = ((21*a*30)*b)%60
    return str(value_min)+" minute" +" and "+str(value_sec)+" seconds"




print(fun(8,7))
print(fun(0,0))
print(fun(7,9))