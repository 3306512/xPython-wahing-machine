import time
from colorama import Fore, Back, Style
from settings import *
from utils import show_list
# Fun fact: я пишу docstring-и для оценки pylint-а
# Your code has been rated at 9.17/10 (previous run: 9.17/10, +0.00)

# Здесь могла быть ваша реклама
# © 2024 https://github.com/3306512 (Program author) - All Rights Reserved.


def start_simulation() -> dict:
    """
    В зависимости от выбора пользователя возвращает настройки базовые или кастомные
    :return:
        dict: new_settings || settings
    """
    while True:
        basic_survey = input(Fore.GREEN + '> do you prefer to use base settings, or you want to change it? '
                                          '(choose between "base" and "change")' + Style.RESET_ALL)
        if basic_survey.strip() == 'base':
            return settings
        if basic_survey.strip() == 'change':
            new_settings = change_settings(settings)
            return new_settings
        print(Fore.RED + 'please choose between "base" and "change"' + Style.RESET_ALL)
        continue


def change_settings(in_settings: dict) -> dict:
    """
    :param in_settings: dict - Базовые настройки которые в процессе будут изменены
    :return:
        dict: to_return - изменённые настройки
    """
    to_return = in_settings
    while True:
        try:
            mode = input(Fore.GREEN + f'> mode num ({show_list(allowed_modes[: -1])} or leave blank to use default)'
                         + Style.RESET_ALL)
            if mode.strip() in allowed_modes_nums:
                if mode.strip() == '':
                    mode = to_return['mode']
            else:
                print(Fore.RED + f'use one of these {show_list(allowed_modes)}' + Style.RESET_ALL)
                continue
        except ValueError as _:
            print(Fore.RED + 'use numbers' + Style.RESET_ALL)
            continue
        print(Fore.GREEN + 'saving...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('success' + Style.RESET_ALL)
        time.sleep(0.5)
        to_return = {
            'mode': mode
        }
        return to_return


def chose() -> list:
    """
    Функция для выбора одежды которую нужно постирать
    :return:
        list: list_of_clothes - Лист с одеждой которая нуждается в стирке
    """
    list_of_clothes = []
    while True:
        cloth = input(Fore.GREEN + '> your clothes goes here (type "quit" if you want to quit)' + Style.RESET_ALL)
        list_of_clothes.append(cloth)
        if cloth.strip() == '':
            list_of_clothes.pop(-1)
            print(Fore.RED + 'can`t be hollow' + Style.RESET_ALL)
        if cloth.strip().lower() == 'quit':
            list_of_clothes.pop(-1)
            return list_of_clothes


def wash(timeout: int, clothes_to_wash: list) -> list:
    """

    :param timeout: int - имитирует задержку в процессе мытья
    :param clothes_to_wash: list - лист с одеждой которая нуждается в стирке
    :return:
        list: finished - лист с чистой одеждой
    """
    finished = []
    for i in clothes_to_wash:
        print(Fore.CYAN + f"washing {i}" + Style.RESET_ALL)
        time.sleep(timeout)
        print(Back.LIGHTCYAN_EX + Fore.BLACK + 'washed!' + Style.RESET_ALL)
        finished.append(i)
    return finished


def main() -> None:
    """
        Главная функция, вызывается в точке входа
    :return: None
    """
    settings_ = start_simulation()
    timeout = MODES_VALUES[settings_['mode']]
    print(Fore.LIGHTGREEN_EX + 'accepted')
    print('_____________________________')
    print('now choose what clothes you want to wash')
    clothes = chose()
    print(Fore.LIGHTGREEN_EX + f'your clothes to wash {show_list(clothes)}')
    print('accepted')
    print('_____________________________')
    clean_clothes = wash(timeout=timeout+BASE_TIMEOUT, clothes_to_wash=clothes)
    print(Fore.LIGHTGREEN_EX + f'your clean clothes: {show_list(clean_clothes)},'
                               f' used mode - {MODES_DECRYPTION[settings_['mode']]}' + Style.RESET_ALL)


if __name__ == '__main__':
    main()
