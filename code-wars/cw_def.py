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

def count_sheeps(sheep): #counting sheep

    count = 0
    for i in sheep:
        if i == True:
            count += 1
    return count

def get_grade(s1, s2, s3): #overage grates
    average = (s1 + s2 +s3)/3
    if average >= 90:
        return "A"
     
    elif average >=80:
        return "B"
    elif average >=70:
        return "C"
    elif average >=60:
        return "D"
    else:
        return "F"
    
def remove_char(string):
    if (len(string)== 2):
        return ""
    else:
        return string [1:-1]