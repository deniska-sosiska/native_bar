import random

users = 10
# users = int(input("Сколько человек будет играть?: "))
cards = []


#===================Создание катастрофы======================================
with open('files/Катастрофы.txt') as  fileThatOpen:
    lines = 0
    for i in fileThatOpen:
        lines += 1
    needCatastr = (random.randrange(1, lines, 2))
    fileThatOpen.seek(0)
    fileThatCreate = open('Карточки/!Катастрофа.txt', 'w')
    for i in range(lines):
        if (i + 1 == needCatastr):
            fileThatCreate.write('Катастрофа: ')
            fileThatCreate.write(fileThatOpen.readline())
            fileThatCreate.write('Описание: ')
            fileThatCreate.write(fileThatOpen.readline())
        fileThatOpen.readline()
    fileThatCreate.close()



# допол карты навыков
# спец условия

class Card():

    def __init__(self, profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality):
        # self.profession = get_info("Профессии.txt")
        self.__profession = profession
        self.__health = health
        self.__biologicalCharacterization = biologicalCharacterization
        self.__baggage = baggage
        self.__hobby = hobby
        self.__phobias = phobias
        self.__humanQuality = humanQuality

    def output(self, numberUsers):
        with open('Карточки/' + numberUsers + '.txt', 'w') as fileU:
            fileU.write('Профессия:                     ')
            fileU.write(self.__profession)
            fileU.write('Здоровье:                      ')
            fileU.write(self.__health)
            fileU.write('Биологическая характерист-ка:  ')
            fileU.write(str(self.__biologicalCharacterization))
            fileU.write('\n')
            fileU.write('Багаж:                         ')
            fileU.write(self.__baggage)
            fileU.write('Хобби:                         ')
            fileU.write(self.__hobby)
            fileU.write('Фобии:                         ')
            fileU.write(self.__phobias)
            fileU.write('Качество человека:             ')
            fileU.write(self.__humanQuality)




def get_info(nameFile):
    with open('files/' + nameFile + '.txt', 'r') as fileThatOpen:
        lines = 0
        for i in fileThatOpen:
            lines += 1
        needChar = (random.randint(1, lines))
        fileThatOpen.seek(0)
        # fileThatCreate = open('files/'+ nameFile+ '!' +'.txt', 'w')
        for i in range(lines):
            if (i + 1 == needChar):
                attribute = fileThatOpen.readline()
                # fileThatCreate.write(qwe)
            fileThatOpen.readline()
        # fileThatCreate.close()
        return attribute


#============================получаю атрибуты================================

for user in range(users):
    profession = get_info("Профессии")
    forHealth = random.randint(0, 3)
    if (forHealth == 3):
        health = 'Полностью здоров\n'
    else:
        health = get_info("Болезни")
    baggage = get_info("Багаж")
    hobby = get_info("Хобби")
    forPhobias = random.randint(0, 3)
    if (forPhobias == 3):
        phobias = 'Фобий нету\n'
    else:
        phobias = get_info("Фобии")
    humanQuality = get_info('Качество человека')
    forSex = random.randint(0, 1)
    if forSex == 1:
        sex = 'Мужчина'
    else:
        sex = 'Женщина'
    #=====получаю возраст
    age = random.randint(18, 89)
    #=====получаю чайлдфри
    forChildfree = random.randint(0, 4)
    if forChildfree == 4:
        childfree = 'Чайлдфри'
        biologicalCharacterization = [sex , age, childfree ]
    else:
        biologicalCharacterization = [sex , age]


    card = Card(profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality)
    card.output('user' + str(user + 1))













#
