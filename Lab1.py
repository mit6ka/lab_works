# Вариант 10.
# Натуральные числа. Выводить, меняя порядок цифр в них на обратный.
# Для чисел, состоящих из одинаковых цифр вывод должен иметь вид – « 120 единиц».'''

def reverse_digits(number):
    return int(str(number)[::-1])


def number_to_words(len_number, number):
    words_dict = {
        '0': 'ноль',
        '1': 'единиц',
        '2': 'двоек',
        '3': 'троек',
        '4': 'четверок',
        '5': 'пятерок',
        '6': 'шестерок',
        '7': 'семерок',
        '8': 'восемерок',
        '9': 'девяток'
    }
    return words_dict.get(str(number), str(len_number))


def process_sequence(sequence):
    lexemes = sequence.split()
    for lexeme in lexemes:
        if lexeme.isdigit():
            num = int(lexeme)
            reversed_num = reverse_digits(num)
            if reversed_num == num:
                print(f"{len(lexeme)} {number_to_words(len(lexeme), lexeme[0])}")
            else:
                print(reverse_digits(num))
        else:
            pass


try:
    with open("input.txt", "r") as file:
        data = file.read(1024)
        data = data.split()
        if data:
            filtered_data = ''.join(filter(lambda x: x.isdigit() or x.isspace(), data))
            process_sequence(filtered_data)
        else:
            print('Файл пуст')
        data = file.read(1024)
except FileNotFoundError:
    print("Файл input.txt не найден.")
