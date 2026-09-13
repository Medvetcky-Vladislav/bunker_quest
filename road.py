import time
import random
def road_animation(pyi):
    random_road_animation2 = {1:"#", 2:",", 3:".", 4:"-", 5:" "}
    for i in range(pyi):
        random_road_animation = []
        for j in range(4):
            random_road_animation.append(random_road_animation2[random.randint(1, 5)])
        print(f"|     I  {random_road_animation[0]}  |")
        print(f"|     I     |")
        print(f"|  {random_road_animation[1]}  I     |") 
        print(f"|     I  {random_road_animation[2]}  |") 
        print(f"|{random_road_animation[3]}    I     |")
        time.sleep(0.4)

if __name__ == "__main__":
    road_animation(5)