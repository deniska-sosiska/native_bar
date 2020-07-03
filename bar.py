import random

users = 10
# users = int(input("Сколько человек будет играть?: "))

professionThatWas = ['none\n']
healthThatWas = ['none\n']
baggageThatWas = ['none\n']
hobbyThatWas = ['none\n']
phobiasThatWas = ['none\n']
humanQualityThatWas = ['none\n']
additionalInfoThatWas = ['none\n']
actionThatWas = ['none\n']

#===================Создание катастрофы======================================
def catastrophe():
    with open('files/Катастрофы.txt') as  fileThatOpen:
        exitFromCreateCatastrophe = True
        while exitFromCreateCatastrophe:
            fileThatOpen.seek(0)
            lines = 0
            for i in fileThatOpen:
                lines += 1
            needCatastr = (random.randrange(1, lines, 2))
            fileThatOpen.seek(0)
            fileThatChecking = open('Карточки/!Катастрофа.txt', 'r+')
            catastropheThatWas = (fileThatChecking.readline())
            fileThatChecking.seek(0)
            for i in range(lines):
                if (i + 1 == needCatastr):
                    forNameCatastrophe = fileThatOpen.readline()
                    forDescriptionCatastrophe = fileThatOpen.readline()
                    if (catastropheThatWas == forNameCatastrophe):
                        fileThatChecking.close()
                    else:
                        nameCatastrophe  = forNameCatastrophe
                        descriptionCatastrophe = forDescriptionCatastrophe
                        fileThatChecking.write(nameCatastrophe)
                        fileThatChecking.write(descriptionCatastrophe)
                        exitFromCreateCatastrophe = False
                fileThatOpen.readline()

    return nameCatastrophe, descriptionCatastrophe


# допол карты навыков
# спец условия

class Card():
    def __init__(self, profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality, additionalInfo, action, nameCatastrophe, descriptionCatastrophe):
        self.__profession = profession
        self.__health = health
        self.__biologicalCharacterization = biologicalCharacterization
        self.__baggage = baggage
        self.__hobby = hobby
        self.__phobias = phobias
        self.__humanQuality = humanQuality
        self.__additionalInfo = additionalInfo
        self.__action = action

    def output(self, numberUsers):
        with open('Карточки/' + numberUsers + '.txt', 'w') as fileU: #file users
            fileU.write('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Катастрофа~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
            fileU.write('                                            ')
            fileU.write(nameCatastrophe)
            fileU.write('        ')
            fileU.write(descriptionCatastrophe)
            fileU.write("\n\n")
            fileU.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Характеристики~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
            fileU.write('                   Профессия:                     ')
            fileU.write(self.__profession)
            fileU.write('                   Здоровье:                      ')
            fileU.write(self.__health)
            fileU.write('                   Биологическая характерист-ка:  ')
            fileU.write(str(self.__biologicalCharacterization))
            fileU.write('\n')
            fileU.write('                   Багаж:                         ')
            fileU.write(self.__baggage)
            fileU.write('                   Хобби:                         ')
            fileU.write(self.__hobby)
            fileU.write('                   Фобии:                         ')
            fileU.write(self.__phobias)
            fileU.write('                   Качество человека:             ')
            fileU.write(self.__humanQuality)
            if self.__additionalInfo == 'none':
                pass
            else:
                fileU.write('\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Доп. характеристики~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
                fileU.write('                   Дополнительная информация:     ')
                fileU.write(self.__additionalInfo)
            if self.__action == 'none':
                pass
            else:
                fileU.write('\n\n\n\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Cпециальные условия(меняет ход игры)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
                fileU.write('                   Карта действия:             ')
                fileU.write(self.__action)


def nonRepeat(forAttribute, array):
    rangeArray  = range(len(array))
    for i in rangeArray:
        if i == 0:
            attribute = 'Not this!!!'
            continue
        else:
            if (forAttribute == array[i]+'\n') or (forAttribute == array[i]):
                array.pop(0)
                attribute = 'Not this!!!'
                exitFromCreateAtribute = True
                break
            else:
                attribute = forAttribute
                exitFromCreateAtribute = False

    return attribute, exitFromCreateAtribute

def get_info(nameFile):
    with open('files/' + nameFile + '.txt', 'r') as fileThatOpen:
        exitFromCreateAtribute = True
        while exitFromCreateAtribute:
            fileThatOpen.seek(0)
            lines = 0
            for i in fileThatOpen:
                lines += 1
            needChar = (random.randint(1, lines - 1))
            fileThatOpen.seek(0)
            for i in range(lines):
                if (i + 1 == needChar):
                    forAttribute = fileThatOpen.readline()
                    if (nameFile == 'Профессии'):
                        professionThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, professionThatWas)
                    elif (nameFile == 'Болезни'):
                        healthThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, healthThatWas)
                    elif (nameFile == 'Багаж'):
                        baggageThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, baggageThatWas)
                    elif (nameFile == 'Хобби'):
                        hobbyThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, hobbyThatWas)
                    elif (nameFile == 'Фобии'):
                        phobiasThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, phobiasThatWas)
                    elif (nameFile == 'Качество человека'):
                        humanQualityThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, humanQualityThatWas)
                    elif (nameFile == 'Дополнительная информация'):
                        additionalInfoThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, additionalInfoThatWas)
                    elif (nameFile == 'Карты действия'):
                        actionThatWas.insert(0, forAttribute)
                        attribute, exitFromCreateAtribute = nonRepeat(forAttribute, actionThatWas)
                    break

                fileThatOpen.readline()

    return attribute


#============================получаю атрибуты================================
nameCatastrophe, descriptionCatastrophe = catastrophe()

for user in range(users):
    profession = get_info('Профессии')
    forHealth = random.randint(0, 3)
    if (forHealth == 3):
        health = 'Полностью здоров\n'
    else:
        health = get_info('Болезни')
    baggage = get_info('Багаж')
    hobby = get_info('Хобби')
    forPhobias = random.randint(0, 3)
    if (forPhobias == 3):
        phobias = 'Фобий нету\n'
    else:
        phobias = get_info('Фобии')
    humanQuality = get_info('Качество человека')
    forSex = random.randint(0, 2)
    if forSex == 1:
        sex = 'Женщина'
    else:
        sex = 'Мужчина'
    #=====получаю возраст
    age = random.randint(18, 63)
    #=====получаю чайлдфри
    forChildfree = random.randint(0, 4)
    if forChildfree == 4:
        biologicalCharacterization = [sex , age, 'Чайлдфри' ]
    else:
        biologicalCharacterization = [sex , age]
    #=====получаю допю информацию
    forAdd = random.randint(0, 3)
    if forAdd == 2:
        additionalInfo = get_info('Дополнительная информация')
    else:
        additionalInfo = 'none'
    #=====получаю карту действия
    forAction = random.randint(0, 3)
    if forAction == 3:
        action = get_info('Карты действия')
    else:
        action = 'none'


    card = Card(profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality, additionalInfo, action, nameCatastrophe, descriptionCatastrophe)
    card.output('user' + str(user + 1))


print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n\n\n\n\n\n')
print('                                    Успешно!                                      \n\n\n\n\n\n\n\n')
input('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#end
