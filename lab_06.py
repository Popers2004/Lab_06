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

def decode(encoded_password):
    result = ""
    for digit in encoded_password:
        # decode digit by subtracting 3 from encoded digit
        decoded_digit = str((int(digit) - 3))
        result += decoded_digit
        # add decoded digit to result and return decoded password
    return result


continue_password = True
while continue_password:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    option = int(input('Please enter an option: '))
    if option == 1:
        password = str(input('Please enter your password to encode: '))
        # input in string format of password
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
    if option == 2:
        # Paul - Added decode function
        decoded_password = decode(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password} ')
    if option == 3:
        continue_password = False
