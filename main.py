def encode_to_morse(n):
    data = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
            'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2':
                '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..',
            '9': '----.', 'А': '.-', 'Б': '-...', 'В': '-.-.', 'Г': '-..', 'Д': '-..', 'Е': '.',
            'Ж': '...-', 'З': '--..', 'И': '..',
            'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--',
            'Н': '-.', 'О': '---', 'П': '.--.',
            'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
            'Ф': '..-.', 'Х': '....', 'Ц': '-.-.',
            'Ч': '---.', 'Ш': '-----', 'Щ': '--.-', 'Ъ': '.--.-.', 'Ы': '-.--',  'Ь': '-..-', 'Э': '...-...',
            'Ю': '..--', 'Я': '.-.-', 'а': '.-', 'б': '-...', 'в': '-.-.', 'г': '-..', 'д': '-..', 'е': '.',
            'ж': '...-', 'з': '--..', 'и': '..',
            'й': '.---', 'к': '-.-', 'л': '.-..', 'м': '--',
            'н': '-.', 'о': '---', 'п': '.--.',
            'р': '.-.', 'с': '...', 'т': '-', 'у': '..-',
            'ф': '..-.', 'х': '....', 'ц': '-.-.',
            'ч': '---.', 'ш': '-----', 'щ': '--.-', 'ъ': '.--.-.', 'ы': '-.--',  'ь': '-..-', 'э': '...-...',
            'ю': '..--', 'я': '.-.-'}
    n = n.split()
    for i in n:
        t = list()
        for j in list(i):
            t.append(data[j])
        print(*t, sep=' ')
    print()


def decode_from_morse(n: object) -> object:
    data = {
        '.-': 'a',
        '-...': 'b',
        '-.-.': 'c',
        '-..': 'd',
        '.': 'e',
        '..-.': 'f',
        '--.': 'g',
        '....': 'h',
        '..': 'i',
        '.---': 'j',
        '-.-': 'k',
        '.-..': 'l',
        '--': 'm',
        '-.': 'n',
        '---': 'o',
        '.--.': 'p',
        '--.-': 'q',
        '.-.': 'r',
        '...': 's',
        '-': 't',
        '..-': 'u',
        '...-': 'v',
        '.--': 'w',
        '-..-': 'x',
        '-.--': 'y',
        '--..': 'z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0',
    }
    n = n.split(' ')
    for i in n:
        print(data[i], end='')
    print()


def main():
    print('1: encodings', '2: decode', sep='\n')
    m = input()
    if m == '1':
        encode_to_morse(input().upper())
    elif m == '2':
        decode_from_morse(input())


if __name__ == '__main__':
    main()