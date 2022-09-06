from operator import truediv


def find_one(list,needle):
    """
    devuelve true si encuentra una o mas ocurrencia de needle en list
    """
    return find_n( list, needle, 1)

def find_n(list, needle, n):
    """
    devulve tru si en list hay n o mas ocurrencias de needle
    flase si hay menos o si n<0
    """

    if n >= 0:
        index = 0
        count = 0
        while count < n and index < len(list):
            if needle == list[index]:
                count += 1
            index += 1
        return count >= n
    else:
        return False

def find_streak(list, needle, n):
    """
    devuelve true si en la lista hay n o mas needles seguidos
    y false para todo lo demas
    No es la misma que la que hace el profe
    """
    if n == 1:
        return find_n( list, needle, 1)
    
    elif n > 1:
        index = 0
        streak = False
        while index < (len(list)-n + 1):
            if needle == list[index]:
                    streak = True
                    count_streak = 1
                    while streak == True and count_streak < n: 
                        if needle != list[index + count_streak]:
                            streak = False
                            count_streak = 0
                        count_streak = count_streak + 1
                    if streak == True and count_streak == n:
                        return True
            index += 1
        return False
    else:
        return False
            


