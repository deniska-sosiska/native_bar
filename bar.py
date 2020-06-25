import random

users = 10
# users = int(input("Сколько человек будет играть?: "))
professionThatWas = ['none\n']
healthThatWas = []
baggageThatWas = []
hobbyThatWas = []
phobiasThatWas = []

# print(professionThatWas)

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
            # print(needCatastr)
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

    def __init__(self, profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality, nameCatastrophe, descriptionCatastrophe):
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
            fileU.write(nameCatastrophe)
            fileU.write(descriptionCatastrophe)
            fileU.write("\n\n")
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


# def poisk(forAttribute):
#     # attribute = '1'
#     x = 0
#     for i in professionThatWas:
#         print('forAttribute:', forAttribute, end='')
#         print('i:', i, end='')
#         print('professionThatWas:',professionThatWas[0], end='\n')
#         x += 1
#         if  i == professionThatWas[0]:
#             print('from if:', x, end='\n\n')
#             attribute = forAttribute
#         else:
#             if i == forAttribute:
#                 print('from elif:', x, '\n\n\n')
#                 attribute = '123'
#                 # break
#             else:
#                 print('from else:', x, end='\n\n')
#                 attribute = forAttribute
#                 exitFromCreateAtribute = False
#                 break
#
#     return attribute

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
                        # attribute = poisk(forAttribute)
                    # else:
                        # attribute = forAttribute
                        # exitFromCreateAtribute = False
                    break

                fileThatOpen.readline()

            # if attribute == '123':
            #     exitFromCreateAtribute = True
            # else:
            #     exitFromCreateAtribute = False


            #=====================================
            if (nameFile == 'Профессии'):
                print("То что проверяю: ", forAttribute)
                x  = range(len(professionThatWas))
                # print(x)
                for i in x:
                    print("профессия итерация: ", i, '-', professionThatWas[i])
                    if i == 0:
                        print('from if')
                        continue
                    else:
                        # print(forAttribute, ' : ', professionThatWas[i])
                        if (forAttribute == professionThatWas[i]+'\n') or (forAttribute == professionThatWas[i]):
                            print('from elif')
                            professionThatWas.pop(0)
                            exitFromCreateAtribute = True

                            break
                        else:
                            print('from else')

                            attribute = forAttribute
                            exitFromCreateAtribute = False
                            # break
                print('\n\n\n')


            else:
                attribute = forAttribute
                exitFromCreateAtribute = False

    return attribute


                    # if (nameFile == 'Болезни'):
                    #     professionThatWas.append(forAttribute)
                    # if (nameFile == 'Багаж'):
                    #     professionThatWas.append(forAttribute)
                    # if (nameFile == 'Хобби'):
                    #     professionThatWas.append(forAttribute)
                    # if (nameFile == 'Фобии'):
                    #     professionThatWas.append(forAttribute)
                    #     # print(professionThatWas)


#============================получаю атрибуты================================
nameCatastrophe, descriptionCatastrophe = catastrophe()


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
    age = random.randint(18, 63)
    #=====получаю чайлдфри
    forChildfree = random.randint(0, 4)
    if forChildfree == 4:
        biologicalCharacterization = [sex , age, 'Чайлдфри' ]
    else:
        biologicalCharacterization = [sex , age]


    card = Card(profession, health, biologicalCharacterization, baggage, hobby, phobias, humanQuality, nameCatastrophe, descriptionCatastrophe)
    card.output('user' + str(user + 1))






print(professionThatWas)







#
