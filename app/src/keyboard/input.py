from constants.data_type import INT, FLOAT, STR
from exceptions.generic_exception import GenericException


def keyboard_input(data_type, message=None):
    try:
        if data_type == INT:
            return int(input(message))
        elif data_type == FLOAT:
            return float(input(message))
        elif data_type == STR:
            return input(message)
    except:
            raise GenericException('Caracter inválido')