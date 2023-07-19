# Abigail Pope
def encode(password):
# this is the define method for encoding the password
    result = ""
# string format of the password
    for digit in password:
        encoded_digit = str((int(digit) + 3) % 10)
        result += encoded_digit
# funtion for the password encoding
    return result
# return password after encoding
password = str(input())
# input in string format of password
encoded_password = encode(password)
print(encoded_password)
