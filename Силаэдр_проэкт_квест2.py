import random
import time
import road
def pfw():
    global people
    global water
    global food
    food = food - people
    water = water - people
    if people <= 0:
            print("Вы проиграли(не осталось живых людей)")
            exit()
    if water <= 0:
            print("Вы проиграли(закончилась вода)")
            exit()
    if food <= 0:
            print("Вы проиграли(закончилась еда)")
            exit()
    print(f"люди:{people}    еда:{food}      вода:{water}")

def pp():
    global g1
    global g2
    global wp1
    global e1
    if g1 == False and g2 == False and wp1 == True and e1 == True:
        print("Вы полностью восстановили бункер, вы прожили в нём 5 лет и радиация исчезла. Вы победили!!!!!!!!!!!")
        exit()

people = 2
food = 20
water = 12
l1 = False
l2 = False
l3 = False
l4 = False
l5 = False

e1 = False
wp1 = False

g1 = True
g2 = True
g3 = True

p = False

def take_people():
    global people
    global food
    global water
    time.sleep(3)
    road.road_animation(9)
    print(f"люди:{people}    еда:{food}      вода:{water}")
    print(f"Вы встречайте 3 человека взять их: да или нет?")
    ans1 = input("Введите да или нет:")
    if ans1 == "да":
        people = people + 3
        pfw()
        enter_in_bunker()
    elif ans1 == "нет":
        people = people + 0
        pfw()
        enter_in_bunker()
    else:
        print("Ответ введён неверно, введите ответ заново")
        take_people()





def enter_in_bunker():
    global people
    global food
    global water
    print("Вы едите дальше")
    time.sleep(3)
    road.road_animation(9)
    c_moncters1 = random.randint(2,3)
    print(f"Перед вами выбор: поехать по короткой дороги с {c_moncters1} монстрами или в долгий объезд")
    ans2 = input("Введите длинная или короткая:")
    if ans2 == "длинная":
        road.road_animation(7)
        print("Вы не упели доехать и взорвались")
        exit()
    elif ans2 == "короткая":
        road.road_animation(6)
        print(f"Вы доехали до места битвы и вам кажется что ,кроме этих {c_moncters1} тут есть ещё монстры вы оглядываетесь и")
        c_moncters2 = random.randint(0,2)
        print(f"видите ещё {c_moncters2} монстров")
        print("Состоялась битва и некоторые пали в бою")
        people = people - c_moncters1 - c_moncters2
        pfw()
        print(f"Вы победили монстров!!! Оставшиися {people} выжившие заходят в бункер и закрывают дверь, сразу прогремел взрыв, вы выжили и попали в бункер!!!!!!!!!")
        room_podezd()
    else:
        print("Ответ введён неверно, введите ответ заново")
        enter_in_bunker()




def room_podezd():
    global people
    global food
    global water
    print("Вы в комнате подъезд(без газов грибочков), вы читаете справочник и находите там что в этом бункере хранились глюциагенные грибочки и их газы распостронились по комната и вокруг бункера из-за неисправной вентиляции")
    print("Вы смотрити на улицу и видети что убили не монстров, а людей, которые пытались вас остановить:(")
    print("У вас есть выбор: открыть гиганскую вентиляцию и проветрить все помещения или не проветривать?")
    ans3 = input("Выберите: открыть или не открыть ")
    
    if ans3 == "открыть":
        print("Гулюциагенный газ вышел, но залетела радиация, вы умерли :(")
        exit()
    elif ans3 == "не открыть":
        print("Вы оборачиветесь и видите два прохода")
        print("Вы можете пойти пешком по леснице и устаните или поедите на лифте и отдохнёте?")
        
        ans4 = input("Выберите: лифт или лестница ")
        if ans4 == "лифт":
            print("Вы доехали и заодно отдохнули")
            room_zal()
        elif ans4 == "лестница":
            print("Вы пошли пешком по леснице и сильно устали")
            food = food - people
            water = water - people
            pfw()
            room_zal()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_podezd()
    else:
        print("Ответ введён неверно, введите ответ заново")
        room_podezd()




def room_zal():
    global food
    global water
    global people
    global l1
    if l1 == False:
        print("Вы в зале тут 1 человек с 6 воды и 4 еды, он идёт с вами")
        l1 = True
        people = people + 1
        water = water + 6
        food = food + 4
    if g1 == True:
        g11 = "с газами грибочков"
    else:
        g11 = "Без газов грибочков"
    print(f"Вы в зале. Вы пойдёте в комату хранилище({g11}) вы видите там много еды и воды или в комнату гениратор там ничего нет но есть генератор электричиства(без газов грибочков) и странная электрическая дверь")
    ans5 = input("Введите: хранилище или генератор ")
    if ans5 == "генератор":
        pfw()
        room_generator()
    elif ans5 == "хранилище":
        pfw()
        room_hranilishe()
    else:
        print("Ответ введён неверно, введите ответ заново")
        room_zal()


def room_hranilishe():
    global food
    global water
    global people
    global l2
    global g1
    global g2
    global wp1
    global e1
    if l2 == False:
        print("Вы в зале тут 8 воды и 12 еды, вы берёте их")
        l2 = True
        water = water + 8
        food = food + 12
    if g1 == True:
        print("Нехотите ли вы поченить вентиляцию в этой комнате за ",7-people,"еды и",6-people ,"воды (чем больше людей тем дешевле строительство), чтобы газ пропал")
        ans6 = input("Введите да или нет ")
        if ans6 == "да":
            print("газа в этой комнате больше нет")
            g1 = False
            water = water - (6 - people)
            food = food - (7 - people)
            pp()
        elif ans6 =="нет":
            print("газ в этой комнате остался")
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_hranilishe()
        if g1 == True:
            print("Вы видите монстров пойти сражаться или попробовать обойтись мирно")
            ans7 = input("Введите бой или мир ")
            if ans7 == "бой":
                print("Вы начали бой, но потом понимайте что на вас действуе галюцинногенный газ и вы дерётесь, не с монстрами, а между собой, но уже позно, вы проиграли")
                exit()
            elif ans7 == "мир":
                print("Через какой-то время вы понимайте, что это не монстры ,а другая часть ваших выживших ,из-за того что на вас действовал галюциногенный газ и вы продолжаете дорогу")
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_hranilishe()

    print(f"Вы в хранилище. Вы пойдёте в комату зал(без газов) или в комнату гениратор там ничего нет но есть генератор электричиства(без газов грибочков) и странная электрическая дверь или в комнату с запасами водой(без газов)")
    ans8 = input("Введите: вода или генератор или зал")
    if ans8 == "генератор":
        pfw()
        room_generator()
    elif ans8 == "вода":
        pfw()
        room_water()
    elif ans8 == "зал":
        pfw()
        room_zal()
    else:
        print("Ответ введён неверно, введите ответ заново")
        room_hranilishe()




def room_water():
    global food
    global water
    global people
    global l3
    global g1
    global g2
    global wp1
    if l3 == False:
        print("Вы в хранилище воды(без газов) тут 7 воды, вы берёте их")
        l3 = True
        water = water + 7
        print("Вы видите монстров пойти сражаться или попробовать обойтись мирно")
        ans8 = input("Введите бой или мир ")
        if ans8 == "бой":
            print("Вы начали бой, пал 1 человек, это были настоящие монстры!")
            people = people - 1
            if g1 == True:
                g11 = "с газами грибочков"
            else:
                g11 = "Без газов грибочков"
            if g2 == True:
                g21 = "с газами грибочков"
            else:
                g21 = "Без газов грибочков"
            if wp1 == False:
                print("Нехотите ли вы поченить водопровод в этой комнате за ",7-people,"еды и",6-people ,"воды (чем больше людей тем дешевле строительство)")
                ans16 = input("Введите да или нет ")
                if ans16 == "да":
                    print("Вы поченили водопровод")
                    wp1 = True
                    water = water - (6 - people)
                    food = food - (7 - people)
                    pp()
                    print(f"Вы в хранилище c водой. Вы пойдёте в комату хранилище({g11}) или в комнату родник({g21})  или в комнату с теплицей(без газов)")
                    ans8 = input("Введите: хранилище или родник или теплица")
                    if ans8 == "хранилище":
                        pfw()
                        room_hranilishe()
                    elif ans8 == "родник":
                        pfw()
                        room_rodnik()
                    elif ans8 == "теплица":
                        pfw()
                        room_teplica()
                    else:
                        print("Ответ введён неверно, введите ответ заново")
                        room_water()
                elif ans16 =="нет":
                    print("Вы продолжаете путь")
                    print(f"Вы в хранилище c водой. Вы пойдёте в комату хранилище({g11}) или в комнату родник({g21})  или в комнату с теплицей(без газов)")
                    ans8 = input("Введите: хранилище или родник или теплица")
                    if ans8 == "хранилище":
                        pfw()
                        room_hranilishe()
                    elif ans8 == "родник":
                        pfw()
                        room_rodnik()
                    elif ans8 == "теплица":
                        pfw()
                        room_teplica()
                    else:
                        print("Ответ введён неверно, введите ответ заново")
                        room_water()
                else:
                    print("Ответ введён неверно, введите ответ заново")
                    room_water()
            else:
                print(f"Вы в хранилище c водой. Вы пойдёте в комату хранилище({g11}) или в комнату родник({g21})  или в комнату с теплицей(без газов)")
                ans8 = input("Введите: хранилище или родник или теплица")
                if ans8 == "хранилище":
                    pfw()
                    room_hranilishe()
                elif ans8 == "родник":
                    pfw()
                    room_rodnik()
                elif ans8 == "теплица":
                    pfw()
                    room_teplica()
                else:
                    print("Ответ введён неверно, введите ответ заново")
                    room_water()
        elif ans8 == "мир":
            print("Это были настоящие монстры они вас убили, вы проиграли!")
            exit()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_water()
    else:
        if g1 == True:
            g11 = "с газами грибочков"
        else:
            g11 = "Без газов грибочков"
        if g2 == True:
            g21 = "с газами грибочков"
        else:
            g21 = "Без газов грибочков"
        if wp1 == False:
            if g1 == True:
                g11 = "с газами грибочков"
            else:
                g11 = "Без газов грибочков"
            if g2 == True:
                g21 = "с газами грибочков"
            else:
                g21 = "Без газов грибочков"
            print("Нехотите ли вы поченить водопровод в этой комнате за ",7-people,"еды и",6-people ,"воды (чем больше людей тем дешевле строительство)")
            ans16 = input("Введите да или нет ")
            if ans16 == "да":
                print("Вы поченили водопровод")
                wp1 = True
                water = water - (6 - people)
                food = food - (7 - people)
                pp()
                print(f"Вы в хранилище c водой. Вы пойдёте в комату хранилище({g11}) или в комнату родник({g21})  или в комнату с теплицей(без газов)")
                ans8 = input("Введите: хранилище или родник или теплица")
                if ans8 == "хранилище":
                    pfw()
                    room_hranilishe()
                elif ans8 == "родник":
                    pfw()
                    room_rodnik()
                elif ans8 == "теплица":
                    pfw()
                    room_teplica()
                else:
                    print("Ответ введён неверно, введите ответ заново")
                    room_water()
            elif ans16 =="нет":
                print("Вы продолжаете путь")
                print(f"Вы в хранилище c водой. Вы пойдёте в комату хранилище({g11}) или в комнату родник({g21})  или в комнату с теплицей(без газов)")
                ans8 = input("Введите: хранилище или родник или теплица")
                if ans8 == "хранилище":
                    pfw()
                    room_hranilishe()
                elif ans8 == "родник":
                    pfw()
                    room_rodnik()
                elif ans8 == "теплица":
                    pfw()
                    room_teplica()
                else:
                    print("Ответ введён неверно, введите ответ заново")
                    room_water()
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_water()
        else:
            print(f"Вы в хранилище c водой. Вы пойдёте в комату хранилище({g11}) или в комнату родник({g21})  или в комнату с теплицей(без газов)")
            ans8 = input("Введите: хранилище или родник или теплица")
            if ans8 == "хранилище":
                pfw()
                room_hranilishe()
            elif ans8 == "родник":
                pfw()
                room_rodnik()
            elif ans8 == "теплица":
                pfw()
                room_teplica()
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_water()

def room_rodnik():
    global food
    global water
    global people
    global g2
    global wp1
    if g2 == True:
            print("Нехотите ли вы поченить вентиляцию в этой комнате за ",7-people,"еды и",6-people ,"воды (чем больше людей тем дешевле строительство), чтобы газ пропал")
            ans9 = input("Введите да или нет ")
            if ans9 == "да":
                print("газа в этой комнате больше нет")
                g2 = False
                water = water - (6 - people)
                food = food - (7 - people)
                pp()
                print(f"Вы в роднике. Вы можете набрать за каждую 1 еду 3 воды или пойти обратно в комнату хранилище с водой (без газов)")
                ans10 = input("Введите: набрать воды или пойти обратно")
                if ans10 == "пойти обрано":
                    pfw()
                    room_water()
                elif ans10 == "набрать воды":
                    ans11 = input("Введите сколько еды вы хотите обменять на воду")
                    if ans11.isdigit() == True:
                        ans11 = int(ans11)
                        print(f"Вы обменял {ans11} еды на {ans11 * 3} воды")
                        food = food - ans11
                        water = water + ans11 * 3
                        room_rodnik
                    else:
                        print("Ответ введён неверно, введите ответ заново")
                        room_rodnik()
                else:
                    print("Ответ введён неверно, введите ответ заново")
                    room_rodnik()
            elif ans9 =="нет":
                print("газ в этой комнате остался")
                print("Тут слишком много газа, вы не можите зайти сюда, вы возвращайтесь обратно в хранилище воды")
                room_water()
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_hranilishe()
    else:
        print(f"Вы в роднике. Вы можете набрать за каждую 1 еду 3 воды или пойти обратно в комнату хранилище с водой (без газов)")
        ans10 = input("Введите: набрать воды или пойти обратно")
        if ans10 == "пойти обрано":
            pfw()
            room_water()
        elif ans10 == "набрать воды":
            ans11 = input("Введите сколько еды вы хотите обменять на воду")
            if ans11.isdigit() == True:
                ans11 = int(ans11)
                print(f"Вы обменял {ans11} еды на {ans11 * 3} воды")
                food = food - ans11
                water = water + ans11 * 3
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_rodnik()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_rodnik()


def room_teplica():
    global food
    global water
    global people
    print(f"Вы в теплице. Вы можете набрать за каждую 1 воду 2 еды или пойти в комнату хранилище с водой (без газов) или пойти в комнату генератор (без газов)")
    ans12 = input("Введите: набрать еды или хранилище с водой или генератор ")
    if ans12 == "хранилище с водой":
        pfw()
        room_water()
    elif ans12 == "генератор":
        pfw()
        room_generator()
    elif ans12 == "набрать еды":
        ans13 = input("Введите сколько воды вы хотите обменять на еду")
        if ans13.isdigit() == True:
            ans13 = int(ans13)
            print(f"Вы обменял {ans13} воды на {ans13 * 2} еды")
            food = food + ans13 * 2
            water = water - ans13
            room_teplica()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_teplica()
    else:
        print("Ответ введён неверно, введите ответ заново")
        room_teplica()



def room_generator():
    global food
    global water
    global people
    global l5
    global e1
    global g1
    if e1 == False:
        print("Нехотите ли вы поченить генератор электричества в этой комнате за ",8-people,"еды и",7-people ,"воды (чем больше людей тем дешевле строительство)")
        ans13 = input("Введите да или нет ")
        if ans13 == "да":
            print("Свет включился")
            e1 = True
            water = water - (7 - people)
            food = food - (8 - people)
            pp()
            print("Вы видете записку и читаете, что чтобы вижить в этом бункере вам надо его восстановить. Чтобы его восстановить вам надо: починить все вентиляции, починить водопровод, починить свет")
        elif ans13 =="нет":
            print("свет остался выключенный")
            print("Тут больше нечего нет идите дальше")
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_generator()
    if e1 == True and l5 == False:
        print("В бункере есть электричество, значит вы можете открыть электрическую дверь, хотители вы её открыть?")
        ans15 = input("Введите да или нет ")
        if ans15 == "да":
            print("Вы открыли дверь там 2 человека 12 воды и 14 еды, вы берёте их.")
            food = food + 14
            water = water + 12
            people = people + 2
            l5 = True
        elif ans15 == "нет":
            print("Вы продолжаете путь")
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_generator()
    if g1 == True:
        g11 = "с газами грибочков"
    else:
        g11 = "Без газов грибочков"
    print(f"Вы в комнате генератор электричества. Вы пойдёте в комату хранилище({g11}) или в комнату зал(без газов) или в комнату теплица(без газов грибочков)")
    ans14 = input("Введите: хранилище или теплица или зал")
    if ans14 == "хранилище":
        pfw()
        room_hranilishe()
    elif ans14 == "теплица":
        pfw()
        room_teplica()
    elif ans14 == "зал":
        pfw()
        room_zal()
    else:
        print("Ответ введён неверно, введите ответ заново")
        room_generator()







random_road_animation2 = {1:"#", 2:",", 3:".", 4:"-", 5:" "}
print("Началась ядерная война и кто-то запустил бомбу на вас, вам надо добраться до спасительного бункера")
friend_name = input("Напишите имя своего друга:")
if friend_name == "Вова":
    print(friend_name, "устал и не стал вас довозить и вы взорвались :(")
    exit()
else:
    print("Вы и",friend_name, "поехали к бункеру на машине")
    take_people()