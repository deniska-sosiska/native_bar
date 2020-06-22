import random
cards = 10


# допол карты навыков
# спец условия

# class card():
#     profession = 'none'
#     health = 'none'
#     biologicalCharacterization = ['пол', 0, 'чайлдфри']
#     baggage = 'none'
#     hobby = 'none'
#     phobias = 'phobias'
#     humanQuality = 'none'



with open('Катастрофы.txt') as file:
    file.seek(0)
    lines = 0
    for i in file:
        lines += 1
    needCatastr = (random.randrange(1, lines, 2))
    print(needCatastr)
    file.seek(0)
    for i in range(lines):
        if i == (needCatastr-1):
            print('Катастрофа: ', file.readline(), end = '')
            print('Описание: ', file.readline())
        file.readline()



# file.readline()
# for line in file:
#     print(line, end = '')
#     # print('hi')

file.close()















#
