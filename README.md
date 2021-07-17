# Loops_Jogo_Advinhacao_Invertido
Assessment activity of the 1º period of IT Bachelor on Loops in Python / Atividade avaliativa do 1º periodo do Bacharelado em TI sobre Laços em Python

## Jogo da Advinhação Invertido

### Goal / Objetivo

Let's reverse the roles of that Guessing Game where we had to figure out a number that the computer randomly picked. In other words, let's choose a number and the computer will have to guess. So, write a program that asks the user to "think" of an integer between 0 and 10 and enter that number. The computer must draw a number between 0 and 10 until it hits the number thought by the user. The program must "help the computer" in the same way as the "human" version of the game, that is, for each wrong attempt, adjust the new random choice, observing if the number thought is smaller or larger than the one informed by the user. The program should be in a loop until the computer hits the number chosen by the user, showing at the end how many guesses were needed to get it right.
To choose a random number between 0 and 10, use the random.randint(0, 10) function after importing the random library. 

Vamos inverter os papéis daquele Jogo da Advinhação em que tínhamos que descobrir um número em que o computador escolhia aleatoriamente. Ou seja, vamos escolher um número e o computador terá que advinhar. Assim, escreva um programa que pede ao usuário para "pensar" em um número inteiro entre 0 e 10 e informar este número. O computador deverá sortear um número entre 0 e 10 até que ele acerte qual foi o número pensado pelo usuário. O programa deverá "ajudar o computador" da mesma forma que a versão "humana" do jogo, isto é, para cada tentativa errada, ajustar a nova escolha aléatória observando se o número pensado é menor ou maior que o informado pelo usuário. O programa deverá ficar em loop até que o computador acerte o número escolhido pelo usuário, mostrando no final quantos palpites foram necessários para acertar.
Para escolher um número aleatório entre 0 e 10, use a função random.randint(0, 10) depois de importar a biblioteca random.

1. Exemple / Exemplo
```py

Escolha um número entre 0 e 10, que o computador tentará adivinhar: 5
Palpite do computador: 8
Menor... Tente novamente.
Palpite do computador: 2
Maior... Tente novamente.
Palpite do computador: 7
Menor... Tente novamente.
Palpite do computador: 5
Acertou com 4 tentativas. Parabéns!
```
