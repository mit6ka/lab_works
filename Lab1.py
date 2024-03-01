def reverse_number(n):
    return n[::-1]

def is_uniform(n):
    return all(digit == n[0] for digit in n)

def process_lexeme(lexeme):

    if not lexeme.isalnum():
        return

    if lexeme.isdigit():
        if is_uniform(lexeme):
            digit_word = {
                '0': 'нулей',
                '1': 'единиц',
                '2': 'двоек',
                '3': 'троек',
                '4': 'четверок',
                '5': 'пятерок',
                '6': 'шестерок',
                '7': 'семерок',
                '8': 'восьмерок',
                '9': 'девяток'
            }
            digit = lexeme[0]
            print(f"{len(lexeme)} {digit_word.get(digit, 'единиц')}")
        else:
            print(reverse_number(lexeme))
    else:

        if not any(char.isdigit() for char in lexeme):
            return
        print(lexeme)

def read_and_process_file(filename):
    lexeme_buffer = ''
    with open(filename, 'r') as f:
        while True:
            block = f.read(1024)
            if not block:
                break

            lexeme_buffer += block
            words = lexeme_buffer.split(' ')
            lexeme_buffer = words.pop()

            for word in words:
                process_lexeme(word)

    if lexeme_buffer:
        process_lexeme(lexeme_buffer)

read_and_process_file('inputs.txt')