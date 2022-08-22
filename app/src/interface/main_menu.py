from exceptions.generic_exception import GenericException
from constants.data_type import INT, FLOAT, STR
from keyboard.input import keyboard_input

def menu():
    while True:
        try:
            chosen_option = keyboard_input(STR,
                'Tecle sua opção:\n'
                'n - Nova requisição\n'
                'c - Colections\n'
                's - Configurações\n'
                'q - Sair'
            )
        except:
            print('Caractere inválido')
