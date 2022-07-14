
text = "gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado… -agrega el comentarista"

lines = text.split("&")

line_1, line_2, line_3, line_4 = lines

print(f'{line_1.capitalize()}...')
print(f'- {line_2.capitalize().replace("j", "J").replace("c", "C")}.')
print(f'- {line_3.capitalize().replace("t", "T")}.')
print(f'- {line_4.capitalize()}.')

line_1 = line_1.capitalize() + '... \n'
line_2 = '- ' + line_2.capitalize().replace('j', 'J').replace('c', 'C') + '. \n'
line_3 = '- ' + line_3.capitalize().replace('t', 'T') + '. \n'
line_4 = '- ' + line_4.capitalize() + '.'

print(line_1, line_2, line_3, line_4)

text_1  = text.replace("&", "\n")

text_2 = text_1.split("\n")

for index, string in enumerate(text_2) :    
    if index == 0 :
        print(f"{string.capitalize()}...")
    elif index == 1 :
        print(f"- {string.capitalize().replace('j', 'J').replace('c', 'C')}.")
    elif index == 2 :
        print(f"- {string.capitalize().replace('t', 'T')}.")
    else :
        print(f"- {string.capitalize()}.")

