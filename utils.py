# кстати я только сейчас понял что можно было делать .join()


def show_list(input_list) -> str:
    to_return = ''
    for item in input_list:
        to_return += item+'; '
    return to_return
