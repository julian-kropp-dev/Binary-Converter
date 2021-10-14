#converter written by Julian Kropp, 2021

def binary_to_decimal(user_input_int): #function converts binary number to decimal
    num = user_input_int
    try:
        y = int(num, 2)
        print(y)
    except:
        print("invalid input. Please enter a valid number.")


def decimal_to_binary(user_input_int): #function converts decimal number to binary
    num = int(user_input_int)
    try:
        x = bin(num)[2:]
        print(x)
    except:
        print("invalid input. Please enter a valid number.")

if __name__ == "__main__":
    user_input= input("Do you want to convert from binary to decimal (A) or from decimal to binary (B)?").upper()

    if user_input == "A" or user_input == "B":
        user_input_int = input("What's your input number?")
        if user_input == "A":
            binary_to_decimal(user_input_int)
        if user_input == "B":
            decimal_to_binary(user_input_int)
    else:
        print("invalid user input.")