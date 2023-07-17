#Start of the question

print("Seja muito bem vindo ao quiz do Ze ! \n")
answer_user = input("Gostaria de começar agora? (S/N) ")


#Finalizing the code
if answer_user != "S":
    quit()


#Starting the code
print("Começando... \n")


#Score
score = 0


#First question
print(" 1) Qual linguagem que mais cresceu nos ultimos anos? \n (A) Python \n (B) C++ \n (C) Java \n (D) Java Script \n (E) outro \n")
answer_question1 = input("Resposta: ")

if answer_question1 == "A":
    print("Correto! \n")
    score = score + 1
else:
    print("Errado! \n")


#Second question
print(" 2) Qual das seguintes linguagens de programação é frequentemente usada para análise de dados? \n (A) Java \n (B) C# \n (C) Python \n (D) Ruby Script \n")
answer_question2 = input("Resposta: ")

if answer_question2 == "C":
    print("Correto!\n")
    score = score + 1
else:
    print("Errado! \n")


#Third question
print(" 3) Qual das linguagens de programação a seguir é mais frequentemente usada para desenvolvimento de aplicativos para dispositivos? \n (A) Swift \n (B) C++ \n (C) Ruby \n (D) JavaScript  \n")
answer_question3 = input("Resposta: ")

if answer_question3 == "A":
    print("Correto!\n")
    score = score + 1
else:
    print("Errado! \n")


#Fourth question
print(" 4) Qual das seguintes linguagens de programação é uma linguagem de script usada principalmente para desenvolvimento web front-end? \n (A) Swift \n (B) PHP \n (C) Ruby \n (D) JavaScript  \n")
answer_question4 = input("Resposta: ")

if answer_question4 == "D":
    print("Correto!\n")
    score = score + 1
else:
    print("Errado! \n")


#Ending Quiz
print("Finalizando... \n")


#Final Score
print(f"Pontuação: {score}/4")
    
