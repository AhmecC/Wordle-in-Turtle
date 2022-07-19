from turtle import Turtle
BLUE = "#234C63"
BLACK = "#1B2430"
GREY = "#EEEEEE"


class Squares(Turtle):
    def __init__(self):
        super(). __init__()
        self.alpha_list = []
        self.alpha_cords = []



        self.squares_list = []
        self.cords_list = []
        self.create_square()
        self.create_keyboard()

    def create_square(self):
        y = 270
        for _ in range(0,6):
            x = -135
            for _ in range(0,5):
                bola = Turtle(shape="square")
                bola.color(BLUE,"black")
                bola.shapesize(stretch_wid=3, stretch_len=3)
                bola.penup()
                bola.goto(x,y)
                bola.stamp()
                x+=70
                self.squares_list.append(bola)
                self.cords_list.append(bola.pos())
            y-=70
        print(self.cords_list)

    def create_keyboard(self):
        alphabet = ["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
        count = 0
        x = -135
        y=-200
        for _ in range(0,10):
            bola = Turtle(shape="square")
            bola.color(BLUE,GREY)
            bola.shapesize(stretch_wid=1.5, stretch_len=1.5)
            bola.penup()
            bola.goto(x,y)
            bola.stamp()
            bola.color(BLUE)
            bola.ht()
            self.alpha_list.append(bola)
            self.alpha_cords.append(bola.pos())
            bola.goto(x, y - 25 / 2)
            bola.write(f"{alphabet[count]}", True, align="center", font=('ariel', 15, 'bold'))
            count+=1
            x+=30

        x = -125
        y=-230
        for _ in range(0,9):
            bola = Turtle(shape="square")
            bola.color(BLUE, GREY)
            bola.shapesize(stretch_wid=1.5, stretch_len=1.5)
            bola.penup()
            bola.goto(x, y)
            self.alpha_list.append(bola)
            self.alpha_cords.append(bola.pos())
            bola.stamp()
            bola.color(BLUE)
            bola.ht()

            bola.goto(x, y - 25 / 2)
            bola.write(f"{alphabet[count]}", True, align="center", font=('ariel', 15, 'bold'))
            count += 1
            x += 30

        x = -95
        y = -260
        for _ in range(0, 7):
            bola = Turtle(shape="square")
            bola.color(BLUE, GREY)
            bola.shapesize(stretch_wid=1.5, stretch_len=1.5)
            bola.penup()
            bola.goto(x, y)
            bola.stamp()
            bola.color(BLUE)
            bola.ht()
            self.alpha_list.append(bola)
            self.alpha_cords.append(bola.pos())
            bola.goto(x, y - 25 / 2)
            bola.write(f"{alphabet[count]}", True, align="center", font=('ariel', 15, 'bold'))
            count += 1
            x += 30

    def word(self,word):
        bola = Turtle()
        bola.color("white")
        bola.ht()
        bola.penup()
        bola.goto(0,300)
        bola.write(f"{word.upper()}", True, align="center", font=('ariel', 15, 'bold'))

    def congrats(self):
        bola = Turtle()
        bola.color("white")
        bola.ht()
        bola.penup()
        bola.goto(0,300)
        bola.write(f"WELL DONE", True, align="center", font=('ariel', 15, 'bold'))

