######################################################################


import random
import turtle

class Nim:
    # class variables

     def __int__(self, init_balls = 0, user_re = 0, comp_rem = 0, remainder = 0):

        self.init_ball = init_balls
        self.user_removed = user_re
        self.com_remove = comp_rem
        self.remainder = remainder
        self.wn = None
        self.write_text = None


     def begin_game(self):


        self.init_ball = int(input("How many balls would you like to begin with? Remember it should be 15 or higher.\n"))
        while self.init_ball < 15:                                                                      # checks if number of balls is required
            self.init_ball = int(input("Number must be 15 or higher.\n"))
        print("let's begin the game. Remember you should start first.\n")
        self.remainder = self.init_ball
        self.wn = turtle.Screen()
        return self.init_ball



     def user_remove(self):
         """ It checks the number of balls user has taken. which supposed to be between 1 to 4.
             Deduct the user selction from the total balls
             :return: Balls remaining after user selection"""

         # print("How many balls would you like to take?", end='')

         self.user_removed = self.wn.numinput("WELCOME TO NIM GAME", "How many balls do you want to select?",0, minval=1, maxval=4)
         while self.user_removed < 1 or self.user_removed > 4:
             print("\nNumber must be between 1 and 4.\n")
             self.user_removed = self.wn.numint(input())             # User removed balls
             print("Window removed",self.wn.numinput())

         self.remainder = self.remainder - self.user_removed
         print('You take', self.user_removed,'balls')               # calculating remaining balls



     def comp_removed(self):
         """
         Functions makes computer select random number of balls between 1 to 4.
         subtract from the remaining balls
         Checks is the remaining balls after computer selection is zero"""
         self.com_remove = self.remainder % 5
         if self.com_remove == 0:
             self.com_remove = random.randint(1,4)
         self.remainder= self.remainder - self.com_remove
         print('Computer takes',self.com_remove, 'balls.')
         print(self.remainder, 'balls remaining. \n')
         if self.remainder == 0:                           # checks the winner when balls are zero
             print("Computer  won")
             return self.remainder


     def end_game(self):
        # self.init_ball = begin_game()
        while self.remainder > 0:
            choice = self.remainder    # user_balls_remove()
            if choice < 1:
                print("You win the Game.Congratulations!!!")
                break
            if self.remainder <1:
                print("The computer wins!!! Better luck next time.")
                break
def main():
    """

    :return:
    """
    g = Nim()
    g.begin_game()
    g.user_remove()
    g.comp_removed()
    while g.remainder >0:
        print("The remainder is", g.remainder)
        g.user_remove()
        if g.remainder > 0:
            g.comp_removed()


if __name__ == "__main__":
    main()

