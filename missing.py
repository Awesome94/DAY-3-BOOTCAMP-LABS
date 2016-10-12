def find_missing(alist1, alist2):
    if len(alist1) == 0 and len(alist2) == 0:
        return 0
    elif len(alist1) == len(alist2): #comparing length of both list
        for num in alist1: #if a number is in list one and two, return 0 no missing number
            if num in alist2:
                return 0
    else:
        if len(alist1) < len(alist2): #however is lenght list one is less than list two,
            for num in alist2:
                if num not in alist1: #and a number is in list 2 and not in one return that number
                    return num
                elif len(alist2) < len(alist1): #the same thing is done for list two
                    for num in alist1:
                        if num not in alist2:
                            return num
