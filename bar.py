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




file = open('Катастрофы.txt')

lines = 0
for i in file:
    lines += 1


needCatastr = (random.randrange(1, lines, 2))
print(needCatastr)

# for catastrophe in file:
#     if int(catastrophe) == needCatastr:
#         print(catastrophe)

file.close()
