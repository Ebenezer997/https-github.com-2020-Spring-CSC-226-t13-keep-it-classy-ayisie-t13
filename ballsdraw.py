
from nim_class import Nim
import turtle

class BallsDraw():
    """

    """

    def __int__(self):
        """
        Initializes new BallsDraw object. All the drawing occurs an instantiation
        :param: A ball object
        """
        self.turt = None
        self.x = -180                                     # Creating turtle screen
        self.dele = None

        self.wn = turtle.Screen()
        self.wn.onkey(self.quit_program,"q")               # it  joins the quit event handler
        self.wn.listen()



    def draw_balls(self,n):
        """
        A turtle object that drawn the number of balls
        :return: None
        """
        self.turt = turtle.Turtle()               # draw balls in the screen
        self.turt.hideturtle()
        self.turt.pensize(15)
        self.turt.color("blue")                 # Set turtle color
        self.turt.penup()
        self.x = -180
        self.y = -180                           # position of turtle


        for i in range(int(n)):
            self.turt.goto(self.x,-180)
            self.turt.pencolor("yellow")
            self.turt.pendown()
            self.turt.speed(15)
            self.turt.hideturtle()
            self.turt.pencolor("yellow")
            self.turt.begin_fill()
            self.turt.circle(3)
            self.turt.fillcolor("white")
            self.turt.end_fill()
            self.x = self.x + 50
            self.turt.hideturtle()
            self.turt.penup()
        self.turt.goto(0,150)

        self.x = -180
        self.y = -180

    def delete_turt(self,n):
        self.dele.pensize(15)
        self.dele.hideturtle()      # deleting balls
        self.dele.color("white")
        self.dele.shape("circle")
        self.dele.penup()
        print(n)

        for i in range(int(n)):
            self.dele.penup()
            self.dele.goto(self.x,-180)
            self.dele.pendown()
            self.dele.speed(0)
            # self.dele.hideturtle()
            self.dele.pencolor("white")
            self.dele.begin_fill()
            self.dele.circle(3)
            self.dele.fillcolor("white")
            self.dele.end_fill()
            self.x += 50


    def exit_game(self):
        """ Function exit the game
        :return: None
        """
        self.wn.bye()
def main():
    g = Nim()
    g.begin_game()
    t = BallsDraw()
    t.dele = turtle.Turtle()


    t.draw_balls(g.remainder)
    # wn = turtle.Screen()
    # wn.colormode(255)
    # t.draw_balls(g.remainder)
    # g.user_remove()
    # t.delete_turt(g.com_remove)
    while g.remainder > 0:
        g.user_remove()
        print("The remainder is", g.remainder)
        t.delete_turt(g.user_removed)


        print("This is the first take")
        selection = g.remainder      # Player balls taken
        if selection < 1:
            self.write_text = turtle.Turtle()
            self.write_text.write("You are the winner .Congratulations")
            g.wn.exitonclick()


        if g.remainder > 0:
            g.comp_removed()
            print("The computer took", g.com_remove)
            print("The number of balls")
            t.delete_turt(g.com_remove)
            if g.remainder < 1:
                write_text = turtle.Turtle()                      # write text on turtle window
                write_text.color("orange")
                write_text.write("Computer is the winner")
                g.wn.exitonclick()

    # wn.exitonclick()



if __name__ == "__main__":
    main()





