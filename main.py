text, qnt = input('Text: '), int(input('Number of letters to return (a number): '))
if qnt > 26 or qnt < 0:
    print('Must be a number less than 26 or greater than 0!')
    exit()

print(str(list(map((lambda letter: ('abcdefghijklmnopqrstuvwxyz'['abcdefghijklmnopqrstuvwxyz'.find(letter) - qnt]) if letter in 'abcdefghijklmnopqrstuvwxyz' else letter), text))).replace("', '", '')[2:-2])

''' Breaking the previous line (without lambda):

alphabet = 'abcdefghijklmnopqrstuvwxyz'
final = ''

for index in range(len(text)):
    if text[index] in alphabet:
        letterIndex = alphabet.find(text[index])
        final += alphabet[letterIndex - qnt]
    else:
        final += text[index]

print(final)

'''