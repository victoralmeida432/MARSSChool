#Editado ultima vez dia: 27/06/2018
#usando a biblioteca pygame tem que baixar ela!, usando pyserial também!
#Código em Python!
#vale lembrar que os audios precisam estar salvos na pasta do python e precisam estar com os mesmos nomes -CaseSensitive-
import pygame
import serial
import time
pygame.mixer.init()
conexao = serial.Serial('COM3', 9600)
#porta 'COMX' determinada na IDE do Arduino

#primeira Função para escolher qual modo vai ser usado
def historia():
    pygame.mixer.music.load("historia.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()
    conexao.write('5'.encode())
    a=conexao.read()
    b=int(a)
    while b==3 or b==4:
     conexao.write('5'.encode())   
     a=conexao.read()
     b=int(a)
    while True :
        if b==0:
           inicio()
        if b==1 or b==2:
           apresentacao()
        break
def apresentacao():
    pygame.mixer.music.load("apresentacao.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()

    pygame.mixer.music.load("python e arduino.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()
    
    conexao.write('5'.encode())
    a=conexao.read()
    b=int(a)
    while b==3 or b==4:
     conexao.write('5'.encode())
     a=conexao.read()
     b=int(a)
    while True :
        if b==0:
           inicio()
        if b==1:
           python()
        if b==2:
           arduino()
        break
def python():
    pygame.mixer.music.load("python.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()
    conexao.write('5'.encode())
    a=conexao.read()
    b=int(a)
    while b==3 or b==4:
     conexao.write('5'.encode())
     a=conexao.read()
     b=int(a)
    while True :
        if b==0:
           inicio()
        if b==1:
           arduino()
        if b==2:
           pesquisa()
        
        break
def arduino():
    pygame.mixer.music.load("arduino.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()
    conexao.write('5'.encode())
    a=conexao.read()
    b=int(a)
    while b==3 or b==4:
     conexao.write('5'.encode())
     a=conexao.read()
     b=int(a)
    while True :
        if b==0:
           inicio()
        if b==1:
           pesquisa()
        if b==2:
           python()
        break
def pesquisa():
    pygame.mixer.music.load("pesquisa.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()  
    
     
def pause():
    while pygame.mixer.music.get_busy():
         if conexao.inWaiting():
            a=conexao.read()
            b=int(a)
            if b==0:
               inicio()
            if b==1 or b==2:
               a=conexao.read()
               b=int(a)
            if b==3:
               pygame.mixer.music.pause()         
            if b==4:
               pygame.mixer.music.unpause()     
            
        
def inicio():
       
    pygame.mixer.music.load("ola.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()

    pygame.mixer.music.load("o grupo.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()

    pygame.mixer.music.load("botoes.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()

    pygame.mixer.music.load("escolha.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)
    pause()
    
    conexao.write('5'.encode())
    a=conexao.read()
    b=int(a)
    while b==3 or b==4:
        conexao.write('5'.encode())
        a=conexao.read()
        b=int(a)
    while True :
        if b==0:
            inicio()        
        if b==1:
            apresentacao()
        if b==2:
            historia()
        break
def start():
    a=conexao.read()
    b=int(a)
    while b!=0:
        a=conexao.read()
        b=int(a)
    if b==0:
        inicio()
if __name__ == '__main__': 
    start()
