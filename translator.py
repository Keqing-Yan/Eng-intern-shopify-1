char_to_braille = {
    'a': "O.....", 'b': "O.O...", 'c': "OO....", 'd': "OO.O..",
    'e': "O..O..", 'f': "OOO...", 'g': "OOOO..", 'h': "O.OO..",
    'i': ".OO...", 'j': ".OOO..", 'k': "O...O.", 'l': "O.O.O.",
    'm': "OO..O.", 'n': "OO.OO.", 'o': "O..OO.", 'p': "OOO.O.",
    'q': "OOOOO.", 'r': "O.OOO.", 's': ".OO.O.", 't': ".OOOO.",
    'u': "O...OO", 'v': "O.O.OO", 'w': ".OOO.O", 'x': "OO..OO",
    'y': "OO.OOO", 'z': "O..OOO"
}
specialchar_to_braille={
    '.': "..OO.O",  ',': "..O..",
    '?': "..O.OO", '!': "..OOOO", ':': "..OO..", ';': "..O.O.",
    '-': "....OO", '/': ".O..O.", '<': ".OO..O", '>': "O..OO.",
    '(': "O.O..O", ')': ".O.OO."
}

num_to_brialle={
    '1': "O.....", '2': "O.O...", '3': "OO....", '4': "OO.O..",
    '5': "O..O..", '6': "OOO...", '7': "OOOO..", '8': "O.OO..",
    '9': ".OO...", '0': ".OOO..", '.': "..OO.O"
 }

braille_to_char={ v:k for k, v in char_to_braille.items()}
braille_to_num={ v:k for k, v in num_to_brialle.items()}
braille_to_specchar={v:k for k, v in specialchar_to_braille.items()}

space="......"
capital_follow=".....O"
decimal_follow=".O...O"
number_follow=".O.OOO"

def translate_to_brialle(text):
    result=[]
    isNum=False
    for char in text:
        if char ==" ":
            result.append(space)
            isNum=False
        elif char.isdigit():
            if not isNum:
                result.append(number_follow) 
                isNum= True
            result.append(num_to_brialle[char])
        elif char.isalpha():
            if char.isupper():
                result.append(capital_follow)
                char=char.lower()
            result.append(char_to_braille[char])
            isNum=False
        elif char in char_to_braille:
            result.append(char_to_braille[char])
        elif char in specialchar_to_braille:
            result.append(specialchar_to_braille[char])
        else:
            result.append("??????")
    return "".join(result)

def translate_to_eng(text):
    length = 6
    result = []
    isNum = False
    i = 0

    while i < len(text):
        braille_word = text[i:i + length]
        i += length
        if braille_word == number_follow:
            isNum = True
        elif braille_word == decimal_follow:
            isNum = True
        elif braille_word == space:
            result.append(' ')
            isNum = False
        elif isNum:
                result.append(braille_to_num[braille_word])
        elif not isNum:
                if braille_word == capital_follow:
                    braille_word = text[i:i + length]
                    i += length
                    result.append(braille_to_char[braille_word].upper())
                elif braille_word in braille_to_char :
                    result.append(braille_to_char[braille_word])
                elif braille_word in braille_to_specchar:
                    result.append(braille_to_specchar[braille_word])
                else:
                    result.append(braille_to_specchar[braille_word])
                isNum = False

    return "".join(result)




def isbraille(text):
    braille_char={'O',"."}
    if not all(char in braille_char for char in text):
        return False
    elif len(text)%6!=0:
        return False
    else:
        return True   

def main():
    User_input= input("Please enter text you wish to translate: ")
    if isbraille(User_input):
        result = translate_to_eng(User_input)
    else:
      result=translate_to_brialle(User_input) 

    print(result) 

    


if __name__ == "__main__":
    main()