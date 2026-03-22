def roman_to_int(s):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer_value = 0
    for i in range(len(s)):
        if s[i] not in roman_numerals:
            return None  # invalid Roman numeral
        if i > 0 and roman_numerals[s[i]] > roman_numerals[s[i - 1]]:
            integer_value += roman_numerals[s[i]] - 2 * roman_numerals[s[i - 1]]
        else:
            integer_value += roman_numerals[s[i]]
    return integer_value

def is_valid_roman(s):
    roman_numerals = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    i = 0
    while i < len(s):
        if s[i] not in roman_numerals:
            return False
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        if count > 3 or (count > 1 and s[i] in ['V', 'L', 'D']):
            return False
        i += 1
    return True

def valid_roman_to_int(s):
    if not is_valid_roman(s):
        return None
    return roman_to_int(s)

print(valid_roman_to_int("III"))  # 3
print(valid_roman_to_int("IV"))   # 4
print(valid_roman_to_int("IX"))   # 9
print(valid_roman_to_int("LVIII"))  # 58
print(valid_roman_to_int("MCMXCIV"))  # 1994