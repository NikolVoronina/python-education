def string_to_number(s):
    return int(s)  #int - count numbers

def boolean_to_string(b):
    return str (b) #str - leters values

def check(seq, elem):  #return examples
    if elem in seq:
        return True
    else:
        return False


def summation(num):    #sum funktion
    result = sum(range(1, num + 1))
    return result

def grow(arr):    #multiplication
    result = 1
    for i in arr:
        result *= i
    return result
