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

def digitize(n):  #int - tall, str - value
    dig = [int(num) for num in str(n)][::-1]
    return dig

def area_or_perimeter(l , w):
    if l == w: 
        return l*w
    else:
        return 2*(l+w)
      #Here I used the formula of Perimeter, like l*w...

def past(h, m, s):
    # here is the formula I found in the Inthernet: (h * 3600 + m * 60 + s) * 1000
    ms_in_h = 3600 * 1000
    ms_in_m = 60 * 1000
    ms_in_s = 1000

    return h * ms_in_h + m * ms_in_m + s * ms_in_s

def array(string):  #Remove First and Last Character Part Two
    if string == "": #check: is it empty?
        return None
    items = string.split (',')
    sliced = items [1:-1]
    
    if not sliced : 
        return None
    return " ".join(sliced)

def count_positives_sum_negatives(arr):  #Count of positives / sum of negatives
    if not arr :
        return []

    positive = 0
    negative = 0
    
    for number in arr :
        if number > 0 :
            positive +=1
        elif number < 0 :
            negative +=number
        
    return [positive, negative]