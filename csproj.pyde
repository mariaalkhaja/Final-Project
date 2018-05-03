add_library('sound')

import os

class Game:
    def __init__(self):
        self.w = 550
        self.h = 550
        self.g = 630
        self.paused = False
        self.state = 'menu'
        self.score = 0 
        self.x=0
        
    
        
        
    def createGame(self):
        self.cnt = 0
        self.time = 60
        self.y = 0
        self.n = 0
        self.platforms = []
        self.coins = []
        
        # self.pauseSound=SoundFile(this, path+"/pause.mp3")
    
        self.b1 = loadImage('burj2.png')
        self.b2 = loadImage('an.png')
        self.b2.resize(550,550)
            
            
        
        self.girl = Characters(50,50,30,self.g,"girl11.png",5)
        
        
        self.platforms.append(Platform(200,340,85,37,'platform.png',5))
        self.platforms.append(Platform(310,290,85,37,'platform.png',5))
        self.platforms.append(Platform(30,270,85,37,'platform.png',5))
        self.platforms.append(Platform(100,200,85,37,'platform.png',5))
        self.platforms.append(Platform(320,150,85,37,'platform.png',5)) 
        self.platforms.append(Platform(200,100,85,37,'platform.png',5)) 
        self.platforms.append(Platform(150,0,85,37,'platform.png',5))  
        self.platforms.append(Platform(330,-50,85,37,'platform.png',5)) 
        self.platforms.append(Platform(220,-90,85,37,'platform.png',5)) 
        self.platforms.append(Platform(100,-100,85,37,'platform.png',5))
        self.platforms.append(Platform(300,-150,85,37,'platform.png',5)) 
        self.platforms.append(Platform(300,-200,85,37,'platform.png',5)) 
        self.platforms.append(Platform(230,-280,85,37,'platform.png',5)) 
        self.platforms.append(Platform(340,-258,85,37,'platform.png',5)) 
        self.platforms.append(Platform(160,-330,85,37,'platform.png',5)) 
        self.platforms.append(Platform(140,-400,85,37,'platform.png',5)) 
        self.platforms.append(Platform(240,-450,85,37,'platform.png',5)) 
        self.platforms.append(Platform(200,-500,85,37,'platform.png',5)) 
        self.platforms.append(Platform(330,-550,85,37,'platform.png',5))
        self.platforms.append(Platform(240,-610,85,37,'platform.png',5))
        self.platforms.append(Platform(299,-660,85,37,'platform.png',5))
        self.platforms.append(Platform(240,-700,85,37,'platform.png',5))
        self.platforms.append(Platform(180,-770,85,37,'platform.png',5))
        self.platforms.append(Platform(299,-799,85,37,'platform.png',5))
        self.platforms.append(Platform(260,-860,85,37,'platform.png',5))
        self.platforms.append(Platform(190,-930,85,37,'platform.png',5))
        self.platforms.append(Platform(310,-980,85,37,'platform.png',5))
        self.platforms.append(Platform(200,-1040,85,37,'platform.png',5))
        self.platforms.append(Platform(243,-1120,85,37,'platform.png',5))
        self.platforms.append(Platform(250,-1220,85,37,'platform.png',5))
        self.platforms.append(Platform(200,-1270,85,37,'platform.png',5))
        self.platforms.append(Platform(260,-1360,85,37,'platform.png',5))
        self.platforms.append(Platform(225,-1445,85,37,'platform.png',5))
        self.platforms.append(Platform(235,-1500,85,37,'platform.png',5))
        self.platforms.append(Platform(243,-1590,85,37,'platform.png',5))
        self.platforms.append(Platform(220,-1640,85,37,'platform.png',5))
        self.platforms.append(Platform(250,-1700,85,37,'platform.png',5))
        self.platforms.append(Platform(240,-1780,85,37,'platform.png',5))
        self.platforms.append(Platform(243,-1840,85,37,'platform.png',5))
        
        
        for i in range(100):
            r = random(0, 550)
            c = random(-2500, 550)
            self.coins.append(Coin(r,c,15,self.g,"coin.png",2))
        
         
    
    def display(self):
        self.cnt  = (self.cnt + 1)%60
        if self.cnt == 0:
            self.time -= 1
        
        
        self.y += 0.5
        image(self.b2,0,self.y%self.h,self.w,self.h-self.y%self.h,0,0,self.w,int(self.h-self.y%self.h))
        image(self.b2,0,0,self.w,self.y%self.h,0,int(self.h-self.y%self.h),self.w,self.h)        
        
  
        if self.n == 0:
            self.n += 4100
        else: 
            image(self.b1,0,0,self.w,self.h,0,int(7500-self.h-self.n),self.w,int(7500-self.n))
            self.n += 0.5
        
        
        fill(255)
        text(str(self.score), 10, 25)
        text(str(self.time), 10, 50)
        
        self.girl.display()
        
        for p in self.platforms:
            p.display()
            
        for c in self.coins:
            c.display()
            
            
        fill(255)
        text(str(self.score), 10, 25)
        

        
        
class Creature:
    def __init__(self,x,y,r,g,imgName,F):
        self.x = x
        self.y = y
        self.r = r
        self.w = self.r*2
        self.h = self.r*2
        self.vx = 0
        self.vy = 0
        self.F = F 
        self.f = 0 
        self.g = g
        self.dir = 1
        self.img = loadImage(imgName)
        self.jump = 0
        
    def gravity(self):
        if self.y+self.r < self.g:
            self.vy+=0.1
            
            if self.y+self.r+self.vy > self.g:
                self.vy = self.g-self.y-self.r
        else:
            self.vy=0
            self.jump=0
        
        
        
        for p in game.platforms:
            if self.x+self.r >= p.x and self.y+self.r  and self.x-self.r <= p.x+p.w <= p.y:
                self.g = p.y
                p.y += 0.5
                break
            else:
                self.g=game.g
                
    def update(self):        
        self.gravity()
        self.x+=self.vx
        self.y+=self.vy
        
       
        
    def display(self):
        self.update()
        
        if self.vy != 0:
            self.f = (self.f+0.1)%self.F
            
        stroke(0,255,0)
        noFill()
        ellipse(self.x-game.x,self.y,self.r*2,self.r*2)
        stroke(255,0,0)
        line(self.x-self.r-game.x,self.g,self.x+self.r-game.x,self.g)
        
        if self.dir > 0:
            image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,int(self.h))
        else:
            image(self.img,self.x-self.r-game.x,self.y-self.r,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
         
         
         
         
         
class Characters(Creature):
    def __init__(self,x,y,r,g,imgName,F):
        Creature.__init__(self,x,y,r,g,imgName,F)
        
        self.keyHandler={LEFT:False,RIGHT:False,UP:False}

    
    def update(self):  
        self.gravity()   
        
    
        if self.keyHandler[LEFT]:
            self.vx = -2
            self.dir = -1
            
        elif self.keyHandler[RIGHT]:
            self.vx = 2
            self.dir = 1
            
        else:
            self.vx = 0
            
        if self.keyHandler[UP] and self.jump < 2 and self.vy >= 0:
            self.vy = -3.8
            # self.jumpSound.play()
            self.jump+=1
    
        
        self.x+=self.vx
        self.y+=self.vy 
        
        for c in game.coins:
            if self.distance(c) < self.r+c.r:  
                game.coins.remove(c)
                del c 
                game.score += 10
                
    def distance(self,other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
        
class Platform:
    def __init__(self,x,y,w,h,img,m):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.img = loadImage(path+'/'+img)
        self.m = m
    
    def display(self):
        image(self.img, self.x, self.y+game.y)
        


        
class Coin(Creature):
    def __init__(self,x,y,r,g,imgName,F):
        Creature.__init__(self,x,y,r,g,imgName,F)  
        self.vy = 1        
        
       
game = Game()

def setup():
    global path
    path = os.getcwd()
    print path
    size(game.w,game.h)
    background(0)
    game.createGame()
    

def draw():
    background(0)
    game.display()

    
def keyPressed():
    print (keyCode)
    game.girl.keyHandler[keyCode]=True
    
        
def keyReleased():
    game.girl.keyHandler[keyCode]=False
    
def mouseClicked():
    game.state='play'
    
    
