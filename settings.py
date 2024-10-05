BASE_TIMEOUT = 1

settings = {
    'mode': '',
}

allowed_modes = ['Normal cycle', 'Quick Wash', 'Rinse and Spin', 'Delicate wash', 'Permanent press cycle',  '']
allowed_modes_nums = ['1', '2', '3', '4', '5',  '']

# расшифровка названий режимов (очень странная идея)
MODES_DECRYPTION = {
    '': 'Normal cycle',
    '1': 'Quick Wash',
    '2': 'Rinse and Spin',
    '3': 'Heavy wash',
    '4': 'Delicate wash',
    '5': 'Permanent press cycle',
}


# значения для time.sleep() как секунды, я тупо сделал чтобы каждый режим добавлял времени к таймауту,
# а сколько именно он добавляет прописано здесь
MODES_VALUES = {
    '': 0,
    '1': 20,
    '2': 30,
    '3': 40,
    '4': 50,
    '5': 60,
}
