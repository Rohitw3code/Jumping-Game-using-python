import pygame
import random
import math
pygame.init()

screen=pygame.display.set_mode((1400,800))
#-----Title----------------------------------
pygame.display.set_caption("Python Game")
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
NJump = pygame.font.Font('freesansbold.ttf', 64)

#--Player----------------------------------------
playerImg=pygame.image.load("Run/4.png")

playerX=50
playerY=300

Object=['back','back','sun','house1','house2','house3','house6','tree2','road','road','boy']
objX=[ 0     ,1400  ,1300 , 500    , 1000   , 1500   ,2000    , 10    ,0     ,2500  , 1500]
objY=[0      ,0     ,50   ,300     , 300    , 400    ,100     ,10     ,680   ,680   ,400  ]
objV=[4     ,4    ,1    ,4       ,4       ,4       ,4       ,4      ,10     ,10     ,12    ]
vel=3
OVel=30
score=50
Pname=[]
num=1
times=0

for m in range(1,20):
   for j in range(5):
      Pname.append(m)
# define and load Image
for i in Object:
   globals()[i]=pygame.image.load(f"{i}.png")

# Set Player Image   
def player(name):
   global playerX,playerY,playerImg,tree
   screen.blit(pygame.image.load(name),(playerX,playerY))
   
def SetObjects(objX,obY):
   global Object
   no=0
   for i in Object:
      screen.blit(eval(i),(objX[no],objY[no]))
      no+=1
def life(score,jps):
    global over_font,NJump
    over_text = over_font.render("Life "+str(score), True, (255, 255, 255))
    jump_text = NJump.render("Jump "+str(jps), True, (255, 255, 255))
    screen.blit(over_text, (20,20))
    screen.blit(jump_text, (1000,20))
SCORE_CHANGE=1

# Check Collision od Player with Obstecle
def isCollision(OX, OY, playerX, playerY):
   global num,times,score,jps,SCORE_CHANGE
   if OX<70 and playerY>450:
      if times<=12:
         life(score,jps)
         times=1
         score-=SCORE_CHANGE
         return True
      times+=1
# score to Display
jps=0
isJump=False
jumpCount=0
cnt=True
m=0
OX=800
OY=600
Owidth=20
Oheight=500

# no of jump
number_of_jump=0
ObjInc=0
obstacle=['wood','rocks','mount','wbox']
obst=obstacle[random.randint(0,2)]
index=0
running=True
while running:
#   pygame.time.delay(1)
   for event in pygame.event.get():
      if event.type==pygame.QUIT:
         running=False
   keys= pygame.key.get_pressed()
   
   if keys[pygame.K_LEFT]:
      for i in range(len(Object)):
         objX[i]+=objV[i]
         if ObjInc==1:
            objV[i]+=0.5
      ObjInc=0
   # Display BackGround image one by one
   for i in range(len(Object)):
      objX[i]-=objV[i]
      if Object[i]=='back':
         if objX[i]<-1500:
            if i==1:
               objX[1]=objX[0]+1444
            if i==0:
               objX[0]=objX[1]+1444
   # Display Road image one by one
      elif Object[i]=='road':
         m=Object.index('road')
         if objX[i]<-2660:
            if i==m+1:
               objX[m+1]=objX[m]+1444
            if i==m:
               objX[m]=objX[m+1]+1444
               
   # Display Other Obstecle image one by one
      else:
         if objX[i]<-1100:
            objX[i]=1550

   if OX<-500:
      OX=1600
      Owidth=random.randint(20,200)
      Oheight=random.randint(100,500)
      obst=obstacle[random.randint(0,3)]
      if obst=='wood':
         OY=650
      else:
         OY=600
# Jumping of player
   if not(isJump):      
      if keys[pygame.K_SPACE]:
         isJump=True
         number_of_jump+=1
         jps+=1
         if number_of_jump==4:
            OVel+=5
            number_of_jump=0
            ObjInc=1
   else:
      if jumpCount>=-10:
         neg=1
         if jumpCount<0:
            neg=-1
         playerY-=(jumpCount**2)*0.5*neg
         jumpCount-=0.9
         playerY+=0.5
#--------------------------------------------------
## 1.         index=15
         #hide comment this and comment out above (1) to show static move
         if index<=len(Pname)-1:
            index+=1
         else:
            index=0
#---------------------------------------------------
      else:
         isJump=False
         jumpCount=10
         index=0

# To Stop the Game
   if score==0:
      vel=0
      OVel=0
      for i in range(len(objV)):
         objV[i]=0

      SCORE_CHANGE=0

      
   screen.fill((10,10,20 ))
   SetObjects(objX,objY)
   life(score,jps)
   name=f"Run/{Pname[index]}.png"
   player(name)

   wood=pygame.image.load(f"{obst}.png")
   screen.blit(wood,(OX,OY))

   pygame.display.update()
   OX-=OVel
   collision=isCollision(OX, OY, playerX, playerY)

         
pygame.quit()
