import random
import time
import road

# --- НАЗВАНИЯ И КОНСТАНТЫ ---
GAS_NAME = "споры токсичной плесени"

# Списывает еду и воду по числу людей, проверяет проигрыш
def pfw():
    global inventory
    inventory["food"] = inventory["food"] - inventory["people"]
    inventory["water"] = inventory["water"] - inventory["people"]
    if inventory["people"] <= 0:
            print("Вы проиграли (не осталось живых людей)")
            exit()
    if inventory["water"] <= 0:
            print("Вы проиграли (закончилась вода)")
            exit()
    if inventory["food"] <= 0:
            print("Вы проиграли (закончилась еда)")
            exit()
    print(f'Люди: {inventory["people"]}    Еда: {inventory["food"]}      Вода: {inventory["water"]}')

# Проверяет условие победы: вентиляции и водопровод починены, свет есть
def pp():
    global built
    if built["g1"] == False and built["g2"] == False and built["wp1"] == True and built["e1"] == True:
        print("Вы полностью восстановили бункер, вы прожили в нём 5 лет, и радиация исчезла. Вы победили!!!!!!!!!!!")
        exit()

# Ресурсы выживших
inventory = {"food": 20, "water": 12, "people": 2}
# Что уже собрано в бункере
loot = {"l1": False, "l2": False, "l3": False, "l4": False, "l5": False,}

# Что построено/починено: e1 — свет, wp1 — водопровод, g1 и g2 — вентиляции
built = {"e1": False, "wp1": False, "g1": True, "g2": True}

p = False

# Встреча с тремя людьми по дороге к бункеру
def take_people():
    global inventory
    time.sleep(3)
    road.road_animation(9)
    print(f'Люди: {inventory["people"]}    Еда: {inventory["food"]}      Вода: {inventory["water"]}')
    print("Вы встречаете 3 человека. Взять их: да или нет?")
    ans1 = input("Введите да или нет: ")
    if ans1 == "да":
        inventory["people"] = inventory["people"] + 3
        pfw()
        enter_in_bunker()
    elif ans1 == "нет":
        inventory["people"] = inventory["people"] + 0
        pfw()
        enter_in_bunker()
    else:
        print("Ответ введён неверно, введите ответ заново")
        take_people()

# Выбор дороги и первая битва с монстрами перед входом в бункер
def enter_in_bunker():
    global inventory
    print("Вы едете дальше")
    time.sleep(3)
    road.road_animation(9)
    c_moncters1 = random.randint(2,3)
    print(f"Перед вами выбор: поехать по короткой дороге с {c_moncters1} монстрами или в долгий объезд")
    ans2 = input("Введите длинная или короткая: ")
    if ans2 == "длинная":
        road.road_animation(7)
        print("Вы не успели доехать и взорвались")
        exit()
    elif ans2 == "короткая":
        road.road_animation(6)
        print(f"Вы доехали до места битвы, и вам кажется, что кроме этих {c_moncters1} тут есть ещё монстры. Вы оглядываетесь и")
        c_moncters2 = random.randint(0,2)
        print(f"видите ещё {c_moncters2} монстров")
        print("Состоялась битва, и некоторые пали в бою")
        inventory["people"] = inventory["people"] - c_moncters1 - c_moncters2
        pfw()
        print(f'Вы победили монстров!!! Оставшиеся {inventory["people"]} выживших заходят в бункер и закрывают дверь, сразу прогремел взрыв, вы выжили и попали в бункер!!!!!!!!!')
        room_podezd()
    else:
        print("Ответ введён неверно, введите ответ заново")
        enter_in_bunker()

# Подъезд: проветривать или нет, затем лифт или лестница
def room_podezd():
    global inventory
    print(f"Вы в комнате подъезд (без газов), вы читаете справочник и находите там, что в этом бункере хранились споры токсичной плесени, и их газы распространились по комнатам и вокруг бункера из-за неисправной вентиляции")
    print("Вы смотрите на улицу и видите, что убили не монстров, а людей, которые пытались вас остановить:(")
    print("У вас есть выбор: открыть гигантскую вентиляцию и проветрить все помещения или не проветривать?")
    ans3 = input("Выберите: открыть или не открыть ")
    
    if ans3 == "открыть":
        print("Газ вышел, но залетела радиация, вы умерли :(")
        exit()
    elif ans3 == "не открыть":
        print("Вы оборачиваетесь и видите два прохода")
        print("Вы можете пойти пешком по лестнице и устанете или поехать на лифте и отдохнёте?")
        
        ans4 = input("Выберите: лифт или лестница ")
        if ans4 == "лифт":
            print("Вы доехали и заодно отдохнули")
            room_zal()
        elif ans4 == "лестница":
            print("Вы пошли пешком по лестнице и сильно устали")
            inventory["food"] = inventory["food"] - inventory["people"]
            inventory["water"] = inventory["water"] - inventory["people"]
            pfw()
            room_zal()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_podezd()
    else:
        print("Ответ введён неверно, введите ответ заново")
        room_podezd()

# Зал: развилка в хранилище или к генератору
def room_zal():
    global inventory
    global built
    global loot
    if loot["l1"] == False:
        print("Вы в зале, тут 1 человек с 6 воды и 4 еды, он идёт с вами")
        loot["l1"] = True
        inventory["people"] = inventory["people"] + 1
        inventory["water"] = inventory["water"] + 6
        inventory["food"] = inventory["food"] + 4
    if built["g1"] == True:
        g11 = f"с газами {GAS_NAME}"
    else:
        g11 = "без газов"
    print(f'Вы в зале. Вы пойдёте в комнату хранилище ({g11}), вы видите там много еды и воды, или в комнату генератор, там ничего нет, но есть генератор электричества (без газов) и странная электрическая дверь')
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

# Хранилище: ресурсы, починка вентиляции, возможная битва с монстрами
def room_hranilishe():
    global inventory
    global loot
    global built
    if loot["l2"] == False:
        print("Вы в зале, тут 8 воды и 12 еды, вы берёте их")
        loot["l2"] = True
        inventory["water"] = inventory["water"] + 8
        inventory["food"] = inventory["food"] + 12
    if built["g1"] == True:
        price_food = 7 - inventory["people"]
        price_water = 6 - inventory["people"]
        print(f"Не хотите ли вы починить вентиляцию в этой комнате за {price_food} еды и {price_water} воды (чем больше людей, тем дешевле строительство), чтобы газ пропал")
        ans6 = input("Введите да или нет ")
        if ans6 == "да":
            print(f"Газа {GAS_NAME} в этой комнате больше нет")
            built["g1"] = False
            inventory["water"] = inventory["water"] - (6 - inventory["people"])
            inventory["food"] = inventory["food"] - (7 - inventory["people"])
            pp()
        elif ans6 =="нет":
            print(f"Газ {GAS_NAME} в этой комнате остался")
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_hranilishe()
        if built["g1"] == True:
            print("Вы видите монстров. Пойти сражаться или попробовать обойтись мирно?")
            ans7 = input("Введите бой или мир ")
            if ans7 == "бой":
                print("Вы начали бой, но потом понимаете, что на вас действует галлюциногенный газ, и вы дерётесь не с монстрами, а между собой, но уже поздно, вы проиграли")
                exit()
            elif ans7 == "мир":
                print("Через какое-то время вы понимаете, что это не монстры, а другая часть ваших выживших, из-за того что на вас действовал газ, и вы продолжаете дорогу")
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_hranilishe()

    print(f'Вы в хранилище. Вы пойдёте в комнату зал (без газов) или в комнату генератор, там ничего нет, но есть генератор электричества (без газов) и странная электрическая дверь, или в комнату с запасами воды (без газов)')
    ans8 = input("Введите: вода или генератор или зал ")
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

# Общий блок выбора следующей комнаты из хранилища воды
def water_choose_next(g11, g21):
    print(f'Вы в хранилище с водой. Вы пойдёте в комнату хранилище ({g11}) или в комнату родник ({g21}), или в комнату с теплицей (без газов)')
    ans8 = input("Введите: хранилище или родник или теплица ")
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
        water_choose_next(g11, g21)


# Общий блок починки водопровода
def water_repair_pipe(g11, g21):
    price_food = 7 - inventory["people"]
    price_water = 6 - inventory["people"]
    print(f"Не хотите ли вы починить водопровод в этой комнате за {price_food} еды и {price_water} воды (чем больше людей, тем дешевле строительство)")
    ans16 = input("Введите да или нет ")
    if ans16 == "да":
        print("Вы починили водопровод")
        built["wp1"] = True
        inventory["water"] = inventory["water"] - (6 - inventory["people"])
        inventory["food"] = inventory["food"] - (7 - inventory["people"])
        pp()
        water_choose_next(g11, g21)
    elif ans16 == "нет":
        print("Вы продолжаете путь")
        water_choose_next(g11, g21)
    else:
        print("Ответ введён неверно, введите ответ заново")
        water_repair_pipe(g11, g21)


# Хранилище воды: ресурсы, возможная битва, починка водопровода
def room_water():
    global inventory
    global loot
    global built
    if loot["l3"] == False:
        print("Вы в хранилище воды (без газов), тут 7 воды, вы берёте их")
        loot["l3"] = True
        inventory["water"] = inventory["water"] + 7
        print("Вы видите монстров. Пойти сражаться или попробовать обойтись мирно?")
        ans8 = input("Введите бой или мир ")
        if ans8 == "бой":
            print("Вы начали бой, пал 1 человек, это были настоящие монстры!")
            inventory["people"] = inventory["people"] - 1
            if built["g1"] == True:
                g11 = f"с газами {GAS_NAME}"
            else:
                g11 = "без газов"
            if built["g2"] == True:
                g21 = f"с газами {GAS_NAME}"
            else:
                g21 = "без газов"
            if built["wp1"] == False:
                water_repair_pipe(g11, g21)
            else:
                water_choose_next(g11, g21)
        elif ans8 == "мир":
            print("Это были настоящие монстры, они вас убили, вы проиграли!")
            exit()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_water()
    else:
        if built["g1"] == True:
            g11 = f"с газами {GAS_NAME}"
        else:
            g11 = "без газов"
        if built["g2"] == True:
            g21 = f"с газами {GAS_NAME}"
        else:
            g21 = "без газов"
        if built["wp1"] == False:
            water_repair_pipe(g11, g21)
        else:
            water_choose_next(g11, g21)

# Родник: обмен еды на воду, починка вентиляции
def room_rodnik():
    global inventory
    global built
    if built["g2"] == True:
            price_food = 7 - inventory["people"]
            price_water = 6 - inventory["people"]
            print(f"Не хотите ли вы починить вентиляцию в этой комнате за {price_food} еды и {price_water} воды (чем больше людей, тем дешевле строительство), чтобы газ пропал")
            ans9 = input("Введите да или нет ")
            if ans9 == "да":
                print(f"Газа {GAS_NAME} в этой комнате больше нет")
                built["g2"] = False
                inventory["water"] = inventory["water"] - (6 - inventory["people"])
                inventory["food"] = inventory["food"] - (7 - inventory["people"])
                pp()
                print(f'Вы в роднике. Вы можете набрать за каждую 1 еду 3 воды или пойти обратно в комнату хранилище с водой (без газов)')
                ans10 = input("Введите: набрать воды или пойти обратно ")
                if ans10 == "пойти обратно":
                    pfw()
                    room_water()
                elif ans10 == "набрать воды":
                    ans11 = input("Введите, сколько еды вы хотите обменять на воду ")
                    if ans11.isdigit() == True:
                        ans11 = int(ans11)
                        print(f"Вы обменяли {ans11} еды на {ans11 * 3} воды")
                        inventory["food"] = inventory["food"] - ans11
                        inventory["water"] = inventory["water"] + ans11 * 3
                        room_rodnik()
                    else:
                        print("Ответ введён неверно, введите ответ заново")
                        room_rodnik()
                else:
                    print("Ответ введён неверно, введите ответ заново")
                    room_rodnik()
            elif ans9 =="нет":
                print(f"Газ {GAS_NAME} в этой комнате остался")
                print("Тут слишком много газа, вы не можете зайти сюда, вы возвращаетесь обратно в хранилище воды")
                room_water()
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_rodnik()
    else:
        print(f'Вы в роднике. Вы можете набрать за каждую 1 еду 3 воды или пойти обратно в комнату хранилище с водой (без газов)')
        ans10 = input("Введите: набрать воды или пойти обратно ")
        if ans10 == "пойти обратно":
            pfw()
            room_water()
        elif ans10 == "набрать воды":
            ans11 = input("Введите, сколько еды вы хотите обменять на воду ")
            if ans11.isdigit() == True:
                ans11 = int(ans11)
                print(f"Вы обменяли {ans11} еды на {ans11 * 3} воды")
                inventory["food"] = inventory["food"] - ans11
                inventory["water"] = inventory["water"] + ans11 * 3
            else:
                print("Ответ введён неверно, введите ответ заново")
                room_rodnik()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_rodnik()

# Теплица: обмен воды на еду
def room_teplica():
    global inventory
    print(f'Вы в теплице. Вы можете набрать за каждую 1 воду 2 еды или пойти в комнату хранилище с водой (без газов), или пойти в комнату генератор (без газов)')
    ans12 = input("Введите: набрать еды или хранилище с водой или генератор ")
    if ans12 == "хранилище с водой":
        pfw()
        room_water()
    elif ans12 == "генератор":
        pfw()
        room_generator()
    elif ans12 == "набрать еды":
        ans13 = input("Введите, сколько воды вы хотите обменять на еду ")
        if ans13.isdigit() == True:
            ans13 = int(ans13)
            print(f"Вы обменяли {ans13} воды на {ans13 * 2} еды")
            inventory["food"] = inventory["food"] + ans13 * 2
            inventory["water"] = inventory["water"] - ans13
            room_teplica()
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_teplica()
    else:
        print("Ответ введён неверно, введите ответ заново")
        room_teplica()

# Генератор: починка электричества, открытие электрической двери
def room_generator():
    global inventory
    global loot
    global built
    if built["e1"] == False:
        price_food = 8 - inventory["people"]
        price_water = 7 - inventory["people"]
        print(f"Не хотите ли вы починить генератор электричества в этой комнате за {price_food} еды и {price_water} воды (чем больше людей, тем дешевле строительство)")
        ans13 = input("Введите да или нет ")
        if ans13 == "да":
            print("Свет включился")
            built["e1"] = True
            inventory["water"] = inventory["water"] - (7 - inventory["people"])
            inventory["food"] = inventory["food"] - (8 - inventory["people"])
            pp()
            print("Вы видите записку и читаете, что чтобы выжить в этом бункере, вам надо его восстановить. Чтобы его восстановить, вам надо: починить все вентиляции, починить водопровод, починить свет")
        elif ans13 =="нет":
            print("Свет остался выключенным")
            print("Тут больше ничего нет, идите дальше")
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_generator()
    if built["e1"] == True and loot["l5"] == False:
        print("В бункере есть электричество, значит, вы можете открыть электрическую дверь. Хотите ли вы её открыть?")
        ans15 = input("Введите да или нет ")
        if ans15 == "да":
            print("Вы открыли дверь, там 2 человека, 12 воды и 14 еды, вы берёте их.")
            inventory["food"] = inventory["food"] + 14
            inventory["water"] = inventory["water"] + 12
            inventory["people"] = inventory["people"] + 2
            loot["l5"] = True
        elif ans15 == "нет":
            print("Вы продолжаете путь")
        else:
            print("Ответ введён неверно, введите ответ заново")
            room_generator()
    if built["g1"] == True:
        g11 = f"с газами {GAS_NAME}"
    else:
        g11 = "без газов"
    print(f'Вы в комнате генератор электричества. Вы пойдёте в комнату хранилище ({g11}) или в комнату зал (без газов), или в комнату теплица (без газов)')
    ans14 = input("Введите: хранилище или теплица или зал ")
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

# Запуск игры
print("Началась ядерная война, и кто-то запустил бомбу на вас, вам надо добраться до спасительного бункера")
friend_name = input("Напишите имя своего друга: ")
if friend_name == "Вова":
    print(f"{friend_name} устал и не стал вас довозить, и вы взорвались :(")
    exit()
else:
    print(f"Вы и {friend_name} поехали к бункеру на машине")
    take_people() 