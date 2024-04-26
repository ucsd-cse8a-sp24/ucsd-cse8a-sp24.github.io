def is_palindrome(data):
    data_str = str(data)
    start = 0
    end = len(data_str) - 1
    for i in range(len(data_str)):
        if data_str[start].lower() != data_str[end].lower():
            return False
        start += 1
        end -= 1

    #the str is a palindrome!!
    return True
        

print("maxbm = " + str(is_palindrome("maxbm")))
print("Madam = " + str(is_palindrome("Madam")))
print("MaDAm = " + str(is_palindrome("MaDAm")))

print(is_palindrome("madam"))
print(is_palindrome(121))
print(is_palindrome("rosey"))
print(is_palindrome("sandiego"))
