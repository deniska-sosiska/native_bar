import random
cards = 10


#===================Создание катастрофы======================================
with open('files/Катастрофы.txt') as  fileThatOpen:
    fileThatOpen.seek(0)
    lines = 0
    for i in fileThatOpen:
        lines += 1
    needCatastr = (random.randrange(1, lines, 2))
    fileThatOpen.seek(0)
    fileThatCreate = open('files/!Катастрофа.txt', 'w')
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

class card():

    def __init__(self, profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality):
        # self.profession = get_info("Профессии.txt")
        self.__profession = profession
        self.__health = health
        self.__biologicalCharacterization = biologicalCharacterization
        self.__baggage = baggage
        self.__hobby = hobby
        self.__phobias = phobias
        self.__humanQuality = humanQuality

    def output(self):
        print('Профессия:                     ',self.__profession, end = '')
        print('Здоровье:                      ',self.__health, end = '')
        print('Биологическая характерист-ка:  ',self.__biologicalCharacterization)
        print('Багаж:                         ',self.__baggage, end = '')
        print('Хобби:                         ',self.__hobby, end = '')
        print('Фобии:                         ',self.__phobias, end = '')
        print('Качество человека:             ',self.__humanQuality)




def get_info(nameFile):
    with open('files/' + nameFile + '.txt', 'r') as fileThatOpen:
        lines = 0
        for i in fileThatOpen:
            lines += 1
        needChar = (random.randint(0, lines))
        fileThatOpen.seek(0)
        # fileThatCreate = open('files/'+ nameFile+ '!' +'.txt', 'w')
        for i in range(lines):
            if (i == needChar):
                attribute = fileThatOpen.readline()
                # fileThatCreate.write(qwe)
            fileThatOpen.readline()
        # fileThatCreate.close()
        return attribute


#============================получаю атрибуты================================
profession = get_info("Профессии")
health = get_info("Болезни")
baggage = get_info("Багаж")
hobby = get_info("Хобби")
phobias = get_info("Фобии")
humanQuality = get_info('Качество человека')

#=====получаю пол
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


#====================================создаю класс====================================
cards = card(profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality)
cards.output()










#
