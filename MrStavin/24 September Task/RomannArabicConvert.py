#Create a roman numeral coverter to arabic vice versa
#max 20 
num = {'I':1, 'V':5, 'X':10}

def convert_roman(input_number):
    range_flag = None
    for symbol, integer in num.items():
        if integer == input_number: return symbol
        if input_number > integer:
            range_flag = symbol
    
    leftover = input_number - num[range_flag]
    return range_flag + convert_roman (leftover)

print(convert_roman(19))
        

#Convert roman to arabic

def roman_to_arabic(s):
    int_val = 0
    for i in range(len(s)):
        if i > 0 and num[s[i]] > num[s[i - 1]]:
            int_val += num[s[i]] - 2 * num[s[i - 1]]
        else:
            int_val += num[s[i]]
    return int_val
    
print((roman_to_arabic('II')))




