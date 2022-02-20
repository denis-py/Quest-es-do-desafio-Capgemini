word = input('Digite uma palavra: ')
new_word = []
cont = 1
cont_i = 1
cont_f = len(word)
cont_j = 0
anagrama = 0
aux = []
aux2 = []
str1 = []
str2 = []

for i in range(0, len(word)):
        new_word.append(word[0:cont])
        cont = cont + 1
        if i == len(word) - 1:
            cont = cont - 1
            for q in range(0, len(word)-1):
                    for j in range(0, len(word) - 1):
                        if (cont_i < cont_f):
                            new_word.append(word[cont_i:cont_f])
                            cont_f = cont_f - 1
                    cont_i = cont_i + 1
                    cont_f = len(word)

for j in range(0, len(new_word)):
    for i in range(j+1, len(new_word)):
        if len(new_word[i]) == len(new_word[j]):
                if i != j:
                    aux2 = sorted(new_word[j])
                    str2 = ''.join(aux2)
                    aux = sorted(new_word[i])
                    str1 = ''.join(aux)
                    cont_j = cont_j + 1
                    if str1 == str2:
                        anagrama = anagrama + 1






print('A palavra que você digitou tem {0} anagramas'.format(anagrama))