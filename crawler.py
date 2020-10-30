    
    def __init__(self):

        self.player = Player()
        self.monster = Monster()
        self.basket = Basket()
        self.egg1 = Egg()
        self.egg2 = Egg()
        self.egg3 = Egg()
        self.door = Door()
        self.obj_on_map = [self.monster, self.basket,self.egg1, self.egg2, self.egg3,self.door]
        self.cells = [
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
            ]

    def drawMap(self):
        from IPython.display import clear_output
        l=0
        j=0 #xval
        k=0#yval
        clear_output()
        mapstring=''
        for i in range(0,len(self.cells)):
            if(j>4):
                mapstring+=" \n"
                j=0
                k+=1
                
            if(k==self.player.x and j==self.player.y):
                mapstring+='[P]'
            else:
                mapstring+='[ ]'
            j+=1

        print (mapstring)
        invstring=''
        for item in set(self.player.items):
             invstring+=f"{item} x {self.player.items.count(item)} "
        print(f"Your Inventory: {invstring}")

    def init_game(self):
        while(not self.player.gameOver):
            
            self.drawMap()
            
            for obj in self.obj_on_map:
                print(f"{obj.name} x: {obj.x} y:{obj.y}")
            print(f"player x:{self.player.x} y: {self.player.y}")
                      
            self.player.move()
            self.player.look_in_room(self.obj_on_map)
            self.monster.move()
        again=input("Do you want to play again? Y/N ").capitalize()
        if(again=="Y"):Game.play_game()
    
    @classmethod
    def play_game(cls):
        game=Game()
        game.init_game()



class Token:
    
    def __init__(self):
        import random
        self.x = random.randint(0, 4)
        self.y = random.randint(0, 4)


class Player(Token):

    def __init__(self):
        super().__init__()
        self.items = []
        self.gameOver = False

    def move(self):
        
        s = input("Which way to you want to go? N,S,E,W? ").capitalize()
        if (s =="N"):
            if(self.x-1 <0):
                print("You hit a wall, move again")
            else:
                self.x -= 1
        if (s =="E"):
            if(self.y+1 >4):
                print("You hit a wall, move again")
            else:
                self.y += 1
        if (s =="S"):
            if(self.x+1 >4):
                print("You hit a wall, move again")
            else:
                self.x += 1
        if (s =="W"):
            if(self.y-1 <0):
                print("You hit a wall, move again")
            else:
                self.y -= 1

    def look_in_room(self, obj_on_map):
        for obj in obj_on_map:
            if obj.x ==self.x and obj.y==self.y:
                if obj.name =="Egg":
                    if not obj.picked_up:
                        print("You Found an Egg")
                        if("Basket" in self.items):
                            self.items.append("Egg")
                            print("You put the egg in you basket")
                            obj.picked_up=True
                        else:
                            print("You need a Basket to gather the egg")
                if obj.name =="Monster":
                    print("You have been eaten by the Monster")
                    self.gameOver = True
                if obj.name =="Basket":
                    if not obj.picked_up:
                        print("You Found a Basket")
                        self.items.append("Basket")
                        obj.picked_up=True
                if obj.name =="Door":
                    print("You Found an Door")
                    if(self.items.count("Egg") ==3):
                        print("You made it out alive!")
                        self.gameOver = True


class Monster(Token):
    def __init__(self):
        super().__init__()
        self.name="Monster"

    def move(self):
        import random
        newx = self.x
        newy = self.y
        newx += random.randint(-1, 1)
        newy += random.randint(-1, 1)
        if(newx >4 or newy>4 or newx < 0 or newy < 0):
            self.move()
        else:
            self.x = newx
            self.y = newy


class Egg(Token):
    def __init__(self):
        super().__init__()
        self.name="Egg"
        self.picked_up=False

class Basket(Token):
    def __init__(self):
        super().__init__()
        self.name="Basket"
        self.picked_up=False


class Door(Token):
    def __init__(self):
        super().__init__()
        self.name="Door"
       
Game.play_game()