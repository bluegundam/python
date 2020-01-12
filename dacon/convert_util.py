def convE2Float(value):
    result = ''
    # print("str 타입비교 =>", str(type(value)) == "<class 'float'>")
    # print("type(value) : " , str(type(value)))

    if str(type(value)) == "<class 'float'>":
        if 'e' in str(value)  :
            result = format(float(value), '.20f')
        else : 
            result = value
    else :
        result = value 

    return result
