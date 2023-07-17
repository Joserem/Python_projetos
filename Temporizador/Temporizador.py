#Module
import time


#Starting the code
tempo = input("Digite o tempo (em segundos): ")


#Number check
if tempo.isdigit():
    tempo = int(tempo)
else:
    print("Entrada invalida!")
    quit()


'''
120/ 60 = 2
150/ 60 = 2 | 30

'''

#timer code
while tempo:
    minutes, seconds = divmod(tempo, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    tempo = tempo - 1


#Ending Temporizador
print("TEMPO TERMINOU!")
