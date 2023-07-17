#Module
import random
import string


#Assembling the password code
def password_generator(comprimento_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options


#User response
    password_user = ""


#Assembling the password code
    for i in range(0, comprimento_pass):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user


#Response to user
choice_user = input("Quantos digitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entada invalida!")
    quit()

response = password_generator(comprimento_pass = choice_user)
print(f"Senha gerada:\n{response}")
