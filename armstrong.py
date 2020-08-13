def arm_num(numstr):
    if 'int' in str(type(numstr)):
        numstr = str(numstr)
    if 'str' in str(type(numstr)):
        pass
    if 'list' in str(type(numstr)) or 'tuple' in str(type(numstr)):
        a=''
        for i in range(len(numstr)):
            a+=str(numstr[i])
        numstr=a
        del a
    n = len(numstr)
    result = ''
    for i in range(n):
        result += str(int(numstr[i])**n)+'+'
    result = result[0:len(result)-1]
    if str(eval(result)) == numstr:
        return True
    else:
        return False
print(arm_num(1634))
print(arm_num('1634'))
print(arm_num((1,6,3,4)))
print(arm_num([1,6,3,4]))
