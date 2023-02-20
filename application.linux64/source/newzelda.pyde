add_library('minim')

import os 
import time
from ddf.minim import Minim


path = os.getcwd()

minim = Minim(this)


door = minim.loadFile(path+"/sound/door.wav")
sword  = minim.loadFile(path+"/sound/sword.wav")
hit_enemy  = minim.loadFile(path+"/sound/hit_enemy.wav")
hit_player = minim.loadFile(path+"/sound/hit_player.wav")
keyfx  = minim.loadFile(path+"/sound/key.wav")
switch  = minim.loadFile(path+"/sound/switch.wav")
pot=minim.loadFile(path+"/sound/pot.mp3")
music=minim.loadFile(path+"/sound/music.mp3")


music.play()
music.loop()


class Creature:
    def __init__(self,x,y,r,g,img,w,h,num_slices):
        self.x = x
        self.y = y 
        self.scale = 3
        self.r = r*self.scale
        self.g = g
        self.vy = 0
        self.vx = 0
        self.img = loadImage(path+ "/graphics/"+ img)
        self.img_w = w
        self.img_h = h
        self.slices_row = num_slices
        self.row = 0
        self.col = 0
        self.ismoving = False
        
        self.newdungeon = False
        self.canmove = True
        self.actual_w=w*self.scale
        self.actual_h=h*self.scale
    
        
        self.direction = RIGHT
        
    def update(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
    def display(self):
        self.update()
        image(self.img,game.dungeon.x+self.x,game.dungeon.y+self.y,self.img_w *self.scale,self.img_h*self.scale, self.row*self.img_w, (self.col * self.img_h),(self.row + 1)*self.img_w, (self.col + 1) * self.img_h)
    
class Player(Creature):
    def __init__(self,x,y,r,g,player_w,player_h):
        Creature.__init__(self,x,y,r,g,"character_updated.png",player_w,player_h,4)
        self.key_handler = {LEFT:False ,RIGHT:False, UP:False ,DOWN:False , "SPACE":False}
        self.sword = Sword(self.x,self.y,30,30)
        self.health = 100
        self.takingdamage = False
      
        
    def update(self):
        if(self.x < 20 and ( self.y < 410 and self.y > 300) and game.dungeon.dooropen == True ):
            self.ismoving = True
            if(game.dungeon.x < 800):
                game.dungeon.x += 20
                self.x -=10
            else:
                self.x = 740
                game.dungeon.__init__(0,0,100,100)
            print("Left Door")
        if(self.x > 740 and ( self.y < 410 and self.y > 300) and game.dungeon.dooropen == True ) :
            print("Right Door")
            self.ismoving = True
            if(game.dungeon.x > -800):
                game.dungeon.x -= 20
                self.x +=10
            else:
                self.x = 20
                game.dungeon.__init__(0,0,100,100)
        if(self.y < 20 and ( self.x < 410 and self.x > 330) and game.dungeon.dooropen == True ) :
            self.ismoving = True
            print("Up Door")
            if(game.dungeon.y < 800):
                game.dungeon.y += 20
                self.y -=10
            else:
                self.y = 670
                game.dungeon.__init__(0,0,100,100)
        if(self.y > 700 and ( self.x < 410 and self.x > 330)and game.dungeon.dooropen == True ):
            self.ismoving = True
            if(game.dungeon.y > -800):
                game.dungeon.y -= 20
                self.y +=10
            else:
                self.y = 40
                game.dungeon.__init__(0,0,100,100)
            print("Down Door")
               
        if self.key_handler[RIGHT] == True and self.ismoving == False and self.x < 750 and self.canmove == True:
            self.vx = 5
            self.col = 1 
            self.ismoving = True
            self.direction = RIGHT
        elif self.key_handler[LEFT] == True and self.ismoving == False and self.x > 0 and self.canmove == True:
            self.vx = -5
            self.col = 3
            self.ismoving = True
            self.direction = LEFT
        elif self.key_handler[UP] == True and self.ismoving == False and self.y > 0 and self.canmove == True:
            self.col = 2
            self.vy = -5
            self.ismoving = True
            self.direction = UP
        elif self.key_handler[DOWN] == True and self.ismoving == False and self.y < 710 and self.canmove == True:
            self.col = 0
            self.vy = 5
            self.ismoving = True
            self.direction = DOWN
        else:
            
            '''if self.key_handler['SPACE']==True:
                sword.play()
                sword.rewind()'''
            
            if(self.direction == DOWN):
                if self.key_handler["SPACE"] == True:
                    self.col = 4
                    self.sword.x = self.x +5
                    self.sword.y = self.y+70
                    self.sword.display()
                    self.sword.update()
                    if frameCount % 5 == 0:
                        self.row = (self.row + 1) % self.slices_row
                else:
                    self.col = 0
            if(self.direction == UP):
              
                if self.key_handler["SPACE"] == True:
                    self.sword.x = self.x +5
                    self.sword.y = self.y-5
                    self.sword.display()
                    self.sword.update()
                    self.col = 5
                  
                    if frameCount % 5 == 0:
                        self.row = (self.row + 1) % self.slices_row
                else:
                    self.col = 2
            if(self.direction == RIGHT):
                if self.key_handler["SPACE"] == True:
                    self.col = 6
                    self.sword.x = self.x +30
                    self.sword.y = self.y+40
                    self.sword.display()
                    self.sword.update()
                    if frameCount % 5 == 0:
                        self.row = (self.row + 1) % self.slices_row
                else:
                    self.col = 1
            if(self.direction == LEFT):
                if self.key_handler["SPACE"] == True:
                    self.col = 7
                    self.sword.x = self.x -10
                    self.sword.y = self.y+40
                    self.sword.display()
                    self.sword.update()
                    if frameCount % 5 == 0:
                        self.row = (self.row + 1) % self.slices_row
                else:
                    self.col = 3
                    self.sword.x = 0
                    self.sword.y = 0
            
                
            self.vx = 0
            self.vy = 0
            self.ismoving = False
        
        if frameCount % 5 == 0 and (self.vx != 0 or self.vy != 0):
            self.row = (self.row + 1) % self.slices_row
        
    
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
    def display(self):
        self.update()
        if self.takingdamage == True :
            if frameCount % 2 == 0:
                image(self.img,self.x,self.y,self.img_w *self.scale,self.img_h*self.scale, self.row*self.img_w, (self.col * self.img_h),(self.row + 1)*self.img_w, (self.col + 1) * self.img_h)
            if frameCount % 100 == 0:
                self.takingdamage = False 
        else:
            image(self.img,self.x,self.y,self.img_w *self.scale,self.img_h*self.scale, self.row*self.img_w, (self.col * self.img_h),(self.row + 1)*self.img_w, (self.col + 1) * self.img_h)
        
class Enemy(Creature):
    def __init__(self,x,y,r,g,player_w,player_h):
        Creature.__init__(self,x,y,r,g,"entities.png",player_w,player_h,3)
        self.x=x
        self.y=y
        choices=[(0,0),(0,9),(4,0),(4,3),(4,6),(4,9)]
        chose=choices[int(random(0,len(choices)))]
        self.initial_x= chose[0]
        self.initial_y= chose[1]
        self.row = self.initial_x
        self.col = self.initial_y
        #self.vx = 1
        self.speed=1
        self.randomx = random(400,800)
        #self.col = 2
        self.w = self.img_w*2
        self.h = self.img_h*2
        self.moving=[self.initial_y,self.initial_y+1,self.initial_y+2]
        self.ind=0
        self.paths=[1,1,1,1]
        self.isdead = False
        self.force=False
    def update(self):
               
        '''if self.x < self.randomx :
            self.vx = self.vx * 1
            if(self.x < 0):
                self.vx = self.vx * -1
                self.col = 2
        if self.x > self.randomx :
            self.vx = self.vx * -1
            self.col = 1'''
           
            
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        '''if frameCount % 10 == 0:
            self.row = (self.row + 1) % self.slices_row'''
            
            
        ##Enemy Checking for sword collision
        self.swordcollision()
        #AABB Collision with the enemy############
        if game.player.x > self.x + self.w:
            game.player.canmove = True
            return False
        if game.player.x + 48 < self.x:
            game.player.canmove = True
            return False
        if game.player.y > self.y-60  + self.h:
            game.player.canmove = True
            return False
        if game.player.y + 48 < self.y-30:
            game.player.canmove = True
            return False
        
        game.player.canmove = False
        game.player.health-=5
        hit_player.play()
        hit_player.rewind()
        game.player.takingdamage = True
        print(str(game.player.health))
        
        if game.player.y > self.y-48:
            game.player.y += 15
        if game.player.y < self.y:
            game.player.y -=10
            
        if game.player.x > self.x:
            game.player.x +=10
        
        if game.player.x < self.x:
            game.player.x -=10
    
        return True
    
    
            
     

    def swordcollision(self):
        if game.player.sword.x > self.x + self.w:
            return False
        if game.player.sword.x +  game.player.sword.w < self.x:
            return False
        if game.player.sword.y > self.y + self.h:
            return False
        if game.player.sword.y +  game.player.sword.h < self.y:
            return False
        self.isdead = True
        game.mana+=5
        hit_enemy.play()
        hit_enemy.rewind()
        print("Enemy Colliding with sword")
        game.player.canmove = True
        return True
    
    def check_paths(self):
        self.paths=[1,1,1,1]
        if self.x+2*self.actual_w>=800:
            self.paths[0]=0
        elif self.x-self.actual_w<=0:
            self.paths[1]=0
        if self.y+2*self.actual_h>=800:
            self.paths[2]=0
        elif self.y-self.actual_h<=0:
            self.paths[3]=0 
            
            
        for pot in game.dungeon.pots:
            if self.y>=pot.y-self.actual_h-5 and self.y<=pot.y+pot.h+self.actual_h+5:
                self.force=True
                if self.x>=pot.x-self.actual_w and self.x<=pot.x:
                    print('a')
                    self.paths[0]=0
                elif self.x>=pot.x+pot.w and self.x<=pot.x+pot.w+self.actual_w:
                    print('b')
                    self.paths[1]=0
                    
            elif self.x>=pot.x-self.actual_w-5 and self.x<=pot.x+pot.w+self.actual_w+5:
                self.force=True
                if self.y>=pot.y-2*self.actual_h and self.x<=pot.y+5:
                    print('c')
                    self.paths[2]=0
                elif self.y>=pot.y+pot.h-5 and self.y<=pot.y+pot.h+2*self.actual_h:
                    print('d')
                    self.paths[3]=0
                    
            
        
        
    def roll(self):
        if frameCount%60==0 or self.force:
            self.check_paths()
            empty=[]
            for i in range(len(self.paths)):
                if self.paths[i]==1:
                    empty.append(i)
                    
            if len(empty)==0:
                empty.append(0)
            num=int(random(len(empty)))
            
            
            
            orientation=empty[num]
           
                
            
            self.vx=0
            self.vy=0
            if orientation==0:
                self.vx=self.speed
                self.row=self.initial_x+2
            elif orientation==1:
                self.vx=-self.speed
                self.row=self.initial_x+1
            elif orientation==2:
                self.vy=self.speed
                self.row=self.initial_x
            else:
                self.vy=-self.speed
                self.row=self.initial_x+3
                
            
                
    def move(self):
        if frameCount%10==0 or self.force:
            self.col=self.moving[self.ind]
            self.ind=(self.ind+1)%2
            self.force=False
                
                
                
        
    def display(self):
        self.roll()
        self.update()
        image(self.img,self.x,self.y,self.img_w *self.scale,self.img_h*self.scale, self.col*self.img_w, (self.row * self.img_h),(self.col + 1)*self.img_w, (self.row + 1) * self.img_h)
        self.move()
       
        
    
        
class Dungeon():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tilesprite = loadImage(path+ "/graphics/Tiles.png")
        self.row = 0
        self.col = 0
        self.tilewidth = 10
        self.tileheight = 10
        #self.rand = random(0,600)
        self.dooropen = False
        self.switch = Switch(0,0,50,50)
        self.pots = []
        self.noofpots = 10
        self.noofenemies = 10
        self.keytoswitch = Key(100,100,40,20)
        self.foundkey = False;
        self.keyequipped = False
        
        
        
        self.enemies = []
        self.enemy = Enemy(100,100,5,1,16,16)
       
  

        #Spawn the pots in the dungeons
        for i in range(self.noofpots):
            self.randx = random(100,600)
            self.randy = random(100,600)
            self.pots.append(Pot(self.randx,self.randy,48,48))
            
        self.check_availability()
        
        
        #Spawn the enemies in the dungeon
        for i in range(self.noofenemies):
            self.randx = random(100,500)
            self.randy = random(100,600)
            self.enemies.append(Enemy(-self.x+self.randx,-self.y+self.randy,5,1,16,16))
        
        self.pots[0].haskey = True
            

        
        
        self.moving = False
        
      
        
        self.doorup = loadImage(path+ "/graphics/DoorUp.png")
        self.doordown = loadImage(path+ "/graphics/DoorDown.png")
        self.doorleft = loadImage(path+ "/graphics/DoorLeft.png")
        self.doorright = loadImage(path+ "/graphics/DoorRight.png")
        
        
    def check_availability(self):
        for pot in self.pots:
            while True:
                collision=0
                
                switch_center_x=self.switch.x+self.switch.w/2
                switch_center_y=self.switch.y+self.switch.h/2
                switch_r=self.switch.w/2
                
                pot1_center_x=pot.x+pot.w/2
                pot1_center_y=pot.y+pot.h/2
                pot1_r=pot.w/2
                
                if sqrt((pot1_center_x-switch_center_x)**2+(pot1_center_y-switch_center_y)**2)<=pot1_r+switch_r:
                    continue
                
                
                
                for p in self.pots:
                                    
                    pot2_center_x=p.x+p.w/2
                    pot2_center_y=p.y+p.h/2
                    pot2_r=p.w/2
                    
                    
                    
                    if sqrt((pot1_center_x-pot2_center_x)**2+(pot1_center_y-pot2_center_y)**2)<=pot1_r+pot2_r and pot!=p:
                        collision+=1
                if collision==0:
                    break
                
                pot.x=random(100,600)
                pot.y=random(100,600)
      
    
    def display(self):
      
        for i in range(8):
            for j in range(8):
                image(self.tilesprite,self.x + (100* i),self.y + (100*j), 100, 100)
                
        #########################################################       
        #This is dungeon on the right side which will move left##
        #########################################################
        
        for i in range(8):
            for j in range(8):
                image(self.tilesprite,900 + self.x + (100* i),self.y + (100*j), 100, 100)
        image(self.doorup,900+self.x+350,self.y +0,120,60,30,0,60,20)
        image(self.doordown,900+self.x+350,self.y+740,120,60,30,0,60,20)
        image(self.doorright,900+self.x+740,self.y+350,60,120,0,30,20,60)
        image(self.doorleft,900+self.x,self.y+350,60,120,0,30,20,60)
        
        ##########################################################
        # This is dungeon on the left side which will move right##
        ##########################################################
        
        for i in range(8):
            for j in range(8):
                image(self.tilesprite, -900 + self.x + (100 * i),self.y + (100*j), 100, 100)
        image(self.doorup,-900+self.x+350,self.y +0,120,60,30,0,60,20)
        image(self.doordown,-900+self.x+350,self.y+740,120,60,30,0,60,20)
        image(self.doorright,-900+self.x+740,self.y+350,60,120,0,30,20,60)
        image(self.doorleft,-900+self.x,self.y+350,60,120,0,30,20,60)
        
         ##########################################################
         #This is dungeon on the up side which will move down#####
         ##########################################################
         
        for i in range(8):
            for j in range(8):
                image(self.tilesprite,  self.x + (100 * i),900 + self.y + (100*j), 100, 100)
        image(self.doorup,self.x+350,900+self.y +0,120,60,30,0,60,20)
        image(self.doordown,self.x+350,900+self.y+740,120,60,30,0,60,20)
        image(self.doorright,self.x+740,900+self.y+350,60,120,0,30,20,60)
        image(self.doorleft,self.x,900+self.y+350,60,120,0,30,20,60)
        
         ##########################################################
         # This is dungeon on the down side which will move up####
        ##########################################################
        
        for i in range(8):
            for j in range(8):
                image(self.tilesprite,  self.x + (100 * i),-900 + self.y + (100*j), 100, 100)
        image(self.doorup,self.x+350,-900+self.y +0,120,60,30,0,60,20)
        image(self.doordown,self.x+350,-900+self.y+740,120,60,30,0,60,20)
        image(self.doorright,self.x+740,-900+self.y+350,60,120,0,30,20,60)
        image(self.doorleft,self.x,-900+self.y+350,60,120,0,30,20,60)
        
        if self.dooropen == True:
            image(self.doorup,self.x+350,self.y +0,120,60,30,0,60,20)
            image(self.doordown,self.x+350,self.y+740,120,60,30,0,60,20)
            image(self.doorright,self.x+740,self.y+350,60,120,0,30,20,60)
            image(self.doorleft,self.x,self.y+350,60,120,0,30,20,60)
        else:
            image(self.doorup,self.x+350,self.y +0,120,60,0,0,30,20)
            image(self.doordown,self.x+350,self.y +740,120,60,0,0,30,20)
            image(self.doorright,self.x+740,self.y+350,60,120,0,0,20,30)
            image(self.doorleft,self.x,self.y+350,60,120,0,0,20,30)
        #rect(self.rand,self.rand,100,100)
        
        self.switch.display()
        self.switch.update()
        
       
        
        if(self.foundkey == True):
            self.keytoswitch.update()
            self.keytoswitch.display()
        
        for pot in self.pots:
            pot.update()
            if pot.destroyed == False:
                pot.display()
                
        for enemy in self.enemies:
            if enemy.isdead == False:       
                enemy.display()
            
            
               
         
        
                  
        
class Game():
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.player = Player(100,100,5,1,16,32)
        self.dungeon = Dungeon(0,0, 100, 100)
        self.enemieskilled = 0
        self.mana = 0
        self.healthtext = "Health: "
        self.keytext = "Key: none"
        self.manatext = "Mana: "
        self.gameover = False
        self.gamewon=False
        self.gameoverimg = loadImage(path+ "/graphics/gameoverbackground.png")
        self.gamewonimg = loadImage(path+ "/graphics/gamewon.png")
        self.healthbar=HealthBar(30,30,100,20)
        self.manabar=ManaBar(670,30,100,20)
        
     

    def display(self):
        if game.player.health <= 0:
            self.gameover = True
            
        if self.gameover == False:
            self.dungeon.display()
            self.player.display()
            if(self.mana >= 100):
                self.gamewon=True
                image(self.gamewonimg,0,0,800,800)
        else:
            image(self.gameoverimg,0,0,800,800)
       
        self.RenderUI()
      
        
    def RenderUI(self):
        #fill(255,255,255)
        #textSize(20)
        #textAlign(LEFT)
        self.healthbar.display()
        textSize(20)
        fill(255)
        text(self.keytext,150,20)
        self.manabar.display()
        
        
class Switch():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.switch = loadImage(path+ "/graphics/switches.png")
        self.state = False
        self.rand = random(100,600)
    
    
    
    def update(self):
        if(abs(self.rand - game.player.x) < 20 and abs(self.rand-40 - game.player.y) < 20 and self.state == False and game.dungeon.keyequipped == True):
            print("Collision is happening") 
            self.state = True
            switch.play()
            switch.rewind()
            door.play()
            door.rewind()
            game.dungeon.dooropen = True
            
        
        
    def display(self):
        if self.state == True:
            image(self.switch,game.dungeon.x +self.rand,game.dungeon.y +self.rand,self.w,self.h,0,0,16,18)
        else:
            image(self.switch,game.dungeon.x +self.rand,game.dungeon.y+self.rand,self.w,self.h,16,0,32,18)
            
       
class Pot():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pot = loadImage(path+ "/graphics/Pot.png")
        self.destroyed = False
        self.haskey = False;
    
    def __del__(self):
        print "deleted"
    
    def update(self):
        if(self.destroyed == False):
        ######Check Collision With Player#############
            self.swordcollision()
            if game.player.x > self.x + self.w:
                game.player.canmove = True
                return False
            if game.player.x + 48 < self.x:
                game.player.canmove = True
                return False
            if game.player.y > self.y-60  + self.h:
                game.player.canmove = True
                return False
            if game.player.y + 48 < self.y-30:
                game.player.canmove = True
                return False
            
            game.player.canmove = False
            if game.player.y > self.y-48:
                game.player.y += 2
            if game.player.y < self.y:
                game.player.y -=1
                
            if game.player.x > self.x:
                game.player.x +=1
            
            if game.player.x < self.x:
                game.player.x -=1
           
            return True    
    
    ######Check Collision With Sword#############
    def swordcollision(self):
        if game.player.sword.x > self.x + self.w:
            return False
        if game.player.sword.x +  game.player.sword.w < self.x:
            return False
        if game.player.sword.y > self.y + self.h:
            return False
        if game.player.sword.y +  game.player.sword.h < self.y:
            return False
        
        if(self.haskey == True):
            game.dungeon.foundkey = True;
            game.dungeon.keytoswitch.x = self.x
            game.dungeon.keytoswitch.y = self.y
            
        temp=self.destroyed
        
        print("Sword Colliding")
        self.destroyed = True
        
        if temp!=self.destroyed:
            pot.play()
            pot.rewind()
        game.player.canmove = True
        return True
        
      
        
    def display(self):
        image(self.pot,game.dungeon.x +self.x,game.dungeon.y +self.y,self.w,self.h)

class Sword():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.pot = loadImage(path+ "/graphics/Pot.png")

    def update(self):
        pass
        
            
    def display(self):
        pass
        #rect(self.x,self.y,self.w,self.h)  
        
    def __del__(self):
        print "sword deleted"
    def test(self):
        print "test" 
        
class Key():
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.keysprite = loadImage(path+ "/graphics/key.png")

    def update(self):
        if game.player.x > self.x + self.w:
            return False
        if game.player.x + 48 < self.x:
            return False
        if game.player.y > self.y-60  + self.h:
            return False
        if game.player.y + 48 < self.y-30:
            return False
        print("Key Collsion Happening")
      
        prev=game.dungeon.keyequipped
        game.dungeon.keyequipped = True
        
        if prev!=game.dungeon.keyequipped:
            keyfx.play()
            keyfx.rewind()
        
        game.keytext = "Key:"
        print(game.dungeon.keyequipped)
        return True
        
            
    def display(self):
        if(game.dungeon.keyequipped == False):
            image(self.keysprite,game.dungeon.x +self.x,game.dungeon.y +self.y,self.w,self.h)
        else:
            image(self.keysprite,200,5,self.w,self.h)
            
            
class HealthBar:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def display(self):
        fill(255,255,255)
        textSize(20)
        text('Health',self.x,self.y-10)
        noFill()
        rect(self.x,self.y,self.w,self.h)
        fill(255,0,0)
        rect(self.x,self.y,self.w*float(float(game.player.health)/100),self.h)
        
        
class ManaBar:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        
    def display(self):
        fill(255,255,255)
        textSize(20)
        text('Mana',self.x,self.y-10)
        noFill()
        rect(self.x,self.y,self.w,self.h)
        fill(0,0,255)
        rect(self.x,self.y,self.w*float(float(game.mana)/100),self.h)

        
            
       
        
game = Game(800,800)
caninput = True 
        

        
def setup():
    size(game.w,game.h)
    background(255,255,255)
    
def draw():
    background(0,0,0)
    game.display()
 
    
def keyPressed():
    if keyCode == UP:
        game.player.key_handler[UP] = True
    elif keyCode == DOWN:
        game.player.key_handler[DOWN] = True
    elif keyCode == RIGHT:
        game.player.key_handler[RIGHT] = True
    elif keyCode == LEFT:
        game.player.key_handler[LEFT] = True
    elif key == ' ':
        sword.play()
        sword.rewind()
        game.player.key_handler["SPACE"] = True
    
    
       
        
def keyReleased():
    if keyCode == UP:
        game.player.key_handler[UP] = False
    elif keyCode == DOWN:
        game.player.key_handler[DOWN] = False
    elif keyCode == RIGHT:
        game.player.key_handler[RIGHT] = False
    elif keyCode == LEFT:
        game.player.key_handler[LEFT] = False
    elif key == ' ':
        game.player.key_handler["SPACE"] = False
        
        
def mouseClicked():
    if game.gameover==True or game.gamewon==True:
 
        global game
        game=Game(800,800)
      
    
        
    
