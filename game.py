
#imports
import pygame , sys, random, time, os, imagesize, ast, csv
from pygame.locals import *
pygame.init()


#CONTROL BINDING
binds = []
with open('Settings/controls.txt','r') as data: #open the 'binds' file
    csv_reader = csv.reader(data)
    for row in csv_reader:
        binds.append(row)
    data.close()
defaultbinds = [
    ('w','a','s','d','1','2','3','4'),
    ('up','left','down','right','o','p','[',']') # just incase there is an error
                ]

#MAPS
maplist = os.listdir('Maps')
maps=[]
for mapp in maplist[1:]:
    maps.append(pygame.image.load('Maps/'+str(mapp)))


#MOVEKIT
movesets = [('Bow Kid',
             [('Ranger',
               [('Description', '+ 10% Extra movement speed'),
                ('Boost', 'Movement'),
                ('Amount', 10),
                ('Stats', [
                    ('Health', 100),
                    ('Speed', 5)])
                 ]
                 ),
              ("Death's Whisper",
               [('Description','Launch an arrow which deals ( 1 ) damage'),
                ('Damage', '1'),
                ('Cooldown', '3'),
                ('Effects', 'None'),
                    ('Velocity','20'),
                ]
                 ),
              ('Midge, Curve of Blessings',
               [
                ('Description','Fire a bolt which stuns the enemy when hit'),
                ('Damage','3'),
                ('Cooldown','20'),
                ('Effects','Stun'),
                ('Velocity', '10')
                ]
                  ),
              ('Flux, Skewer of Pride',
               [('Description','Yeet an arrow at high velocity dealing ( 5 ) damage'),
                ('Damage','5'),
                ('Cooldown','13'),
                ('Effects','None'),
                ('Velocity', '30')]
                  ),
              ('Enduring Fall of Harmonic Illusions',
               [('Description','Launch a super large balistic bolt dealing ( 40 ) damage and stunning the enemy'),
                ('Damage','40'),
                ('Cooldown','40'),
                ('Effects','Stun'),
                ('Velocity','100')]
               )]),
           ('Paniemo',
             [('Blessing of the ocean',
               [('Description', 'When an enemy is hit heal for one health point.'),
                ('Boost', 'Heal on hit'),
                ('Amount', 1),
                ('Stats', [
                    ('Health', 80),
                    ('Speed', 30)])
                ]
                 ),
              ("Shifting Tides",
               [('Description','Create a mystical water bolt which deals ( 2 ) damage.'),
                ('Damage', '2'),
                ('Cooldown', '3'),
                ('Effects', 'None'),
                    ('Velocity','10'),
                ]
                 ),
              ('Etheral Glacier',
               [
                ('Description','Fire a magical etheral bolt which deals ( 2 ) damage to the enemy'),
                ('Damage','2'),
                ('Cooldown','6'),
                ('Effects','None'),
                ('Velocity', '10')
                ]
                  ),
              ('Cryogenic Overflow',
               [('Description','Blast the enemy with a high velocity frozen ball Dealing ( 6 ) damage.'),
                ('Damage','6'),
                ('Cooldown','13'),
                ('Effects','None'),
                ('Velocity', '10')]
                  ),
              ('Skyshattering Overload',
               [('Description','Shatter the sky and absorb the essence of wind and water itself dealing ( 20 ) damage and healing ( 20 ) health.'),
                ('Damage','20'),
                ('Cooldown','40'),
                ('Effects','SelfHeal'),
                ('Velocity','20')]
               )])]




#gamevar
width = 1280
height= 720
clock = pygame.time.Clock()
started=0

#MUSIC
#music = pygame.mixer.music.load('Creo - Reflections.mp3')
#pygame.mixer.music.play(-1)
#pygame.mixer.music.set_volume(0.6)

#MAIN

class frame():
    def update(items,win,x,y,v,par):
        for overlay in items:
            win.blit(overlay, (x,y))
        for particle in v:
            win.blit(par, v.get(particle))
        pygame.display.update()
    def check(mouse,v,i2,win,i,items,particles,pa):
        if 6 < v[0] < 64 and 6 < v[1] < 28:
            frame.update([items[0],i2],win,0,0,particles,pa)
            if mouse[0] == 1 :
                pygame.quit()   
                sys.exit()
                return False
                time.sleep(0.1)
            else:
                return True
        elif 300 < v[0]  < 905 and 502 < v[1] < 530:
            if mouse[0] == 1:
                game.game(0,0,1,win,items,particles,'newfunkcity')
                return False
                
            else:
                return True
        else:
            frame.update(items,win,0,0,particles,pa)
            return True
    def clearupdate(elements,win):
        pygame.draw.rect(win,(0,0,0),(0,0,1280,720))
        win.blit(elements[0],(0,0))
        win.blit(elements[1],(0,0))
        pygame.display.update()
    def load(elements,win,overlays):
        p1=[]
        p2=[]
        del elements[1][2]
        for v in elements:
            p1 = elements[0]
            p2 = elements[1]
        for i in p1:
            v = pygame.image.load(i)
            win.blit(v,(430,300))
        for c in p2:
            v = pygame.image.load(c)
            win.blit(v,(850,300))
        listofoverlays = []
        for c in overlays[0]:
            listofoverlays.append(pygame.image.load(overlays[3]+'/'+c))
        for i in range(0,int(overlays[2])):
            win.blit(listofoverlays[i],(int(overlays[1][i][0]),int(overlays[1][i][1])))
        pygame.display.update()


        
    
#def game
class game():
    def main():
        pygame.display.get_init()
        icon = pygame.image.load('overlay1.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Augmented Ascension')
        win = pygame.display.set_mode((width,height), flags=pygame.NOFRAME)
        notrunning = 'Talse'
        top2 = pygame.image.load('aatopbar.png') #load images
        ov = pygame.image.load('ov.png')
        pa = pygame.image.load('particle.png')
        top = pygame.image.load('aatopbar2.png')
        particles = {}
        a=[]
        val=0
        newitem = 0
        items = [ov,top]
        running = True
        loadingback = True
        pygame.display.update()
        while running and loadingback:
            clock.tick(60)
            if newitem == 0:
                val +=1
                newitem = 1
                particles[str(val)] = (-20,random.randint(0,720))
            if newitem in range(0,15):
                newitem +=1
            else:
                newitem = 0
            for particle in particles:
                if particles.get(particle)[0] > 1280:
                    a.append(particle)
                else:
                    particles[str(particle)] = (particles.get(particle)[0]+2,int(particles.get(particle)[1])) 
            if len(a) > 0:
                for v in a:
                    del particles[v]
            a = []              
            if pygame.display.get_active() == True:
                for event in pygame.event.get():
                    pygame.event.poll()
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.display.update()
                        pygame.quit()
                        sys.exit()
            mouse = pygame.mouse.get_pressed()
            frame.update(items,win,0,0,particles,pa)
                
            pos = pygame.mouse.get_pos()
            running = frame.check(mouse,pos,top2,win,top,items,particles,pa)
    def game(player1,player2,mapselected,win,items,particles,mapselectedd):
        left = 'left'
        right = 'right'
        dir1 = right
        dir2 = left
        moveright1 = False
        settings = [False,False] #first one is gravity acceleration
        attacks = {'p1': [],'p2': []}
        moveleft1 = False
        jump1 = 0
        jumping = False
        delay = 0
        previously = {'p1': 1, 'p2': 1}
        moveright2 = False
        moveleft2 = False
        jump2 = 0
        jumping2 = False
        delay2 = 0
        p1m = movesets[player1]
        print(p1m[1][1])
        top = pygame.image.load('aatopbar2.png')
        top2 = pygame.image.load('aatopbar.png')
        p2m = movesets[player2]
        hp1 = int(p1m[1][0][1][3][1][0][1])
        hp2 = int(p2m[1][0][1][3][1][0][1])
        p1mspeed = int(p1m[1][0][1][3][1][1][1])
        p2mspeed = int(p2m[1][0][1][3][1][1][1])
        health = {'p1': hp1,'p2': hp2}
        healthbars = {'p1': pygame.Rect(213,120,100,10),'p2': pygame.Rect(639,120,100,100)}
        frame.clearupdate([pygame.image.load('Maps/'+mapselectedd+'.png'),top],win)
        gravity = 9
        p1listasset = os.listdir(p1m[0])
        p1characterassets = [pygame.image.load(p1m[0]+'/'+'front.png'),pygame.image.load(p1m[0]+'/'+'back.png')]
        p2characterassets = [pygame.image.load(p2m[0]+'/'+'front.png'),pygame.image.load(p1m[0]+'/'+'back.png')]
        folderoverlays = os.listdir('Overlays')
        overlays = os.listdir('Overlays/'+str(mapselectedd))
        itemzz  = overlays.index('.DS_Store')
        del overlays[itemzz]
        overlaynames=[]
        ovamount = 0
        for i in overlays:
            overlaynames.append(ast.literal_eval(os.path.splitext(i)[0]))
            ovamount+=1
        p1assets=[]
        for c in p1listasset[1:]:
            value = p1m[0]+'/'+c
            p1assets.append(value)
        p2listasset = os.listdir(p2m[0])
        p2assets=[]
        for c in p2listasset[1:]:
            value = p1m[0]+'/'+c
            p2assets.append(value)
        frame.load([p1assets,p2assets],win,[overlays,overlaynames,ovamount,'Overlays/'+mapselectedd])
        running = True
        locations = {'p1': (300,400) ,'p2': (850,300)}
        healthbars = {'p1': pygame.Rect(213,120,200,30),'p2': pygame.Rect(639,120,100,100)}
        p1assetstemp=[]
        p2assetstemp=[]
        width1,height1=imagesize.get(p1m[0]+'/'+'front.png')
        width2,height2=imagesize.get(p2m[0]+'/'+'front.png')
        hitbox1 = pygame.Rect(430, 300, width1, height1)
        hitbox2 = pygame.Rect(850, 300, width2, height2)
        pygame.display.update()
        hitboxes = [hitbox1,hitbox2]
        obstacles = []
        obstaclenames = []
        font = pygame.font.Font("Demonized.ttf",64)
        font2 = pygame.font.Font("Fox Cavalier.otf",32)
        jumpheight = int(gravity)-round(int(gravity)/2) 
        for i in range(0,ovamount):
            widthtemp,heighttemp = imagesize.get('Overlays/'+mapselectedd+'/'+str(overlays[i]))
            lefttemp = overlaynames[i][0]
            toptemp = overlaynames[i][1]
            obstacle = pygame.Rect(int(lefttemp),int(toptemp),int(widthtemp),int(heighttemp))
            obstaclenames.append([int(lefttemp),int(toptemp),int(widthtemp),int(heighttemp)])
            obstacles.append(obstacle)
        for i in p1assets:
            p1assetstemp.append(pygame.image.load(i))
        for i in p2assets:
            p2assetstemp.append(pygame.image.load(i))
        p1assets = p1assetstemp
        p2assets = p2assetstemp
        movable = {}
        p1characterasset = [p1characterassets[0]]
        p2characterasset = [p2characterassets[0]]
        while running:
            clock.tick(120)
            if pygame.display.get_active() == True:
                mouse = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                movable = {}
                hitboxes = []
                hitbox1 = pygame.Rect(locations.get('p1')[0], locations.get('p1')[1], width1, height1)
                hitbox2 = pygame.Rect(locations.get('p2')[0], locations.get('p2')[1], width2, height2)
                hitboxes = [hitbox1,hitbox2]
                for hit in hitboxes:
                    hitleft = hit.midleft
                    hitright = hit.midright
                    hittop = hit.midtop
                    hitbot = hit.midbottom
                    botleft = hit.bottomleft
                    topleft = hit.topleft
                    topright = hit.topright
                    botright = hit.bottomright
                    for ob in obstacles:
                        ml = True
                        mr = True
                        mt = True
                        mb = True
                        if str(ob.collidepoint(hitbot[0],hitbot[1]+5)) == '1':
                            mb = False
                        if str(ob.collidepoint(botleft[0],botleft[1]+5)) == '1':
                            mb = False
                        if str(ob.collidepoint(botright[0],botright[1]+5)) == '1':
                            mb = False
                        if str(ob.collidepoint((botright[0]+1,botright[1]-5))) == '1':
                            mr = False
                        if str(ob.collidepoint((botleft[0]-5,botleft[1]-5))) == '1':
                            ml = False
                        if str(ob.collidepoint((topright[0]+5,topright[1]+5))) == '1':
                            mr = False
                        if str(ob.collidepoint((topleft[0]-5,topleft[1]+10))) == '1':
                            ml = False
                        if str(ob.collidepoint((topright[0]-5,topright[1]))) == '1':
                            mt = False
                        if str(ob.collidepoint((topleft[0]+5,topleft[1]))) == '1':
                            mt = False
                        if str(ob.collidepoint(hittop)) == '1':
                            mt = False
                        if str(ob.collidepoint(hitright)) == '1':
                            mr = False
                        if str(ob.collidepoint(hitleft)) == '1':
                            ml = False
                        if not mb and not ml and not mr:
                            if hit == hitboxes[0]:
                                loc = locations.get('p1')
                                locations['p1'] = (int(loc[0]),(int(ob.topleft[1])-int(hit.height)))
                            elif hit == hitboxes[1]:
                                loc = locations.get('p2')
                                locations['p2'] = (int(loc[0]),(int(ob.topleft[1])-int(hit.height)))
                        movable[str(hit)+str(ob)] = ml,mr,mt,mb
                locations,previously = update.gravity(locations,gravity,hitboxes,movable,obstacles,previously,settings)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.display.update()
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[0][3]:
                            moveright1 = True
                            for ob in obstacles:
                                move = movable.get(str(hitboxes[0])+str(ob))
                                if not move[1]:
                                    moveright1 = False
                    if event.type == KEYUP:
                        if str(pygame.key.name(event.key)) == binds[0][3]:
                            moveright1 = False
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[0][4]:
                            if dir1 == 'left':
                                img = pygame.image.load(str(p1m[0])+'/attack1left.png')
                                attack1 = (img,p1m[1][1],(locations.get('p1'),dir1),img.get_rect()); attakk = attacks.get("p1"); attakk.append(attack1); attacks['p1'] = attakk 
                            if dir1 == 'right':
                                img = pygame.image.load(str(p1m[0])+'/attack1right.png')
                                attack1 = (img,p1m[1][1],(locations.get('p1'),dir1),img.get_rect()); attakk = attacks.get("p1"); attakk.append(attack1); attacks['p1'] = attakk
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[0][5]:
                            if dir1 == 'left':
                                img = pygame.image.load(str(p1m[0])+'/attack2left.png')
                                attack1 = (img,p1m[1][2],(locations.get('p1'),dir1),img.get_rect()); attakk = attacks.get("p1"); attakk.append(attack1); attacks['p1'] = attakk 
                            if dir1 == 'right':
                                img = pygame.image.load(str(p1m[0])+'/attack2right.png')
                                attack1 = (img,p1m[1][2],(locations.get('p1'),dir1),img.get_rect()); attakk = attacks.get("p1"); attakk.append(attack1); attacks['p1'] = attakk
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[1][4]:
                            if dir2 == 'left':
                                img = pygame.image.load(str(p2m[0])+'/attack1left.png')
                                attack1 = (img,p2m[1][1],(locations.get('p2'),dir2),img.get_rect()); attakk = attacks.get("p2"); attakk.append(attack1); attacks['p2'] = attakk 
                            if dir2 == 'right':
                                img = pygame.image.load(str(p2m[0])+'/attack1right.png')
                                attack1 = (img,p2m[1][1],(locations.get('p2'),dir2),img.get_rect()); attakk = attacks.get("p2"); attakk.append(attack1); attacks['p2'] = attakk 
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[1][5]:
                            if dir2 == 'left':
                                img = pygame.image.load(str(p2m[0])+'/attack2left.png')
                                attack1 = (img,p2m[1][2],(locations.get('p2'),dir2),img.get_rect()); attakk = attacks.get("p2"); attakk.append(attack1); attacks['p2'] = attakk 
                            if dir2 == 'right':
                                img = pygame.image.load(str(p2m[0])+'/attack2right.png')
                                attack1 = (img,p2m[1][2],(locations.get('p2'),dir2),img.get_rect()); attakk = attacks.get("p2"); attakk.append(attack1); attacks['p2'] = attakk 
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[0][1]:
                            moveleft1 = True
                            for ob in obstacles:
                                move = movable.get(str(hitboxes[0])+str(ob))
                                if not move[0]:
                                    moveleft1 = False
                    if event.type == KEYUP:
                        if str(pygame.key.name(event.key)) == binds[0][1]:
                            moveleft1 = False
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[0][0] and delay not in range(1,(10*int(jumpheight))):
                            for ob in obstacles:                                
                                move = movable.get(str(hitboxes[0])+str(ob))
                                if not move[3]:
                                    jumping = True
                    if event.type == KEYUP:
                        if str(pygame.key.name(event.key)) == binds[0][0]:
                            jumping = False
                            delay = 10*int(jumpheight)
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[1][3]:
                            moveright2 = True
                            for ob in obstacles:
                                move = movable.get(str(hitboxes[1])+str(ob))
                                if not move[1]:
                                    moveright2 = False
                    if event.type == KEYUP:
                        if str(pygame.key.name(event.key)) == binds[1][3]:
                            moveright2 = False
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[1][1]:
                            moveleft2 = True
                            for ob in obstacles:
                                move = movable.get(str(hitboxes[1])+str(ob))
                                if not move[0]:
                                    moveleft2 = False
                    if event.type == KEYUP:
                        if str(pygame.key.name(event.key)) == binds[1][1]:
                            moveleft2 = False
                    if event.type == pygame.KEYDOWN:
                        if str(pygame.key.name(event.key)) == binds[1][0] and delay2 not in range(1,(10*int(jumpheight))):
                            for ob in obstacles:                                
                                move = movable.get(str(hitboxes[1])+str(ob))
                                if not move[3]:
                                    jumping2 = True
                    if event.type == KEYUP:
                        if str(pygame.key.name(event.key)) == binds[1][0]:
                            jumping2 = False
                            delay2 = 10*int(jumpheight)
                p1characterasset=p1characterasset
                p2characterasset=p2characterasset
                if moveright1:
                    moveright1 = True
                    for ob in obstacles:
                        move = movable.get(str(hitboxes[0])+str(ob))
                        if not move[1]:
                            moveright1 = False
                    p2loc = locations.get('p2')
                    location = locations.get('p1')
                    newlocation = location[0]+p1mspeed
                    locations = {}
                    locations['p1'] = (newlocation,location[1])
                    locations['p2'] = p2loc
                    p1characterasset=[p1characterassets[0]]
                    dir1 = right
                if moveleft1:
                    moveleft1 = True
                    for ob in obstacles:
                        move = movable.get(str(hitboxes[0])+str(ob))
                        if not move[0]:
                            moveleft1 = False
                    p2loc = locations.get('p2')
                    location = locations.get('p1')
                    newlocation = location[0]-p1mspeed
                    locations = {}
                    locations['p1'] = (newlocation,location[1])
                    locations['p2'] = p2loc
                    p1characterasset=[p1characterassets[1]]
                    dir1 = left
                movablei = True
                for ob in obstacles:
                    move = movable.get(str(hitboxes[0])+str(ob))
                    if not move[2]:
                        movablei = False
                if jumping or delay in range(1,(10*int(jumpheight))) and movablei == True:
                    p2loc = locations.get('p2')
                    location = locations.get('p1')
                    newlocation = location[1]-(round(int(gravity)*2))
                    locations = {}
                    locations['p1'] = (location[0],newlocation)
                    locations['p2'] = p2loc
                    jumping = False
                    delay = delay+1
                else:
                    jumping = False
                if delay in range(1,(10*int(jumpheight))) and movablei == True:
                    delay+=1
                else:
                    delay=0
                if moveright2:
                    moveright2 = True
                    for ob in obstacles:
                        move = movable.get(str(hitboxes[1])+str(ob))
                        if not move[1]:
                            moveright2 = False
                    p1loc = locations.get('p1')
                    location = locations.get('p2')
                    newlocation = location[0]+p2mspeed
                    locations = {}
                    locations['p2'] = (newlocation,location[1])
                    locations['p1'] = p1loc
                    p2characterasset=[p2characterassets[0]]
                    dir2 = right
                if moveleft2:
                    moveleft2 = True
                    for ob in obstacles:
                        move = movable.get(str(hitboxes[1])+str(ob))
                        if not move[0]:
                            moveleft2 = False
                    p1loc = locations.get('p1')
                    location = locations.get('p2')
                    newlocation = location[0]-p2mspeed
                    locations = {}
                    locations['p2'] = (newlocation,location[1])
                    locations['p1'] = p1loc
                    p2characterasset=[p2characterassets[1]]
                    dir2 = left
                movablei = True
                for ob in obstacles:
                    move = movable.get(str(hitboxes[1])+str(ob))
                    if not move[2]:
                        movablei = False
                if jumping2 or delay2 in range(1,(10*int(jumpheight))) and movablei:
                    p1loc = locations.get('p1')
                    location = locations.get('p2')
                    newlocation = location[1]-(round(int(gravity)*2))
                    locations = {}
                    locations['p1'] = p1loc
                    locations['p2'] = (location[0],newlocation)
                    jumping2 = False
                    delay2 = delay2+1
                else:
                    jumping = False
                if delay2 in range(1,(10*int(jumpheight))) and movablei == True:
                    delay2+=1
                else:
                    delay2=0
                update.update(locations,[p1characterasset,p2characterasset],win,[pygame.image.load('Maps/'+mapselectedd+'.png'),top],mouse,pos,top2,[overlays,overlaynames,ovamount,'Overlays/'+str(mapselectedd)],health,healthbars,[hp1,hp2],font,font2,[p1m[0],p2m[0]],settings)
                health = update.elements(attacks,win,obstacles,hitboxes,health)
                    
                

                    
            
            
                    



class update():
    def gravity(locations,gravity,hitboxes,movable,obstacles,prev,settings):
        newloc = {}
        stay=[]
        downmove = []
        previously = {}
        for hit in hitboxes:
            moveabledirectionz = True
            for ob in obstacles:
                move = movable.get(str(hit)+str(ob))
                if not move[3]:
                    moveabledirectionz = False
            if moveabledirectionz:
                a = hitboxes.index(hit)+1
                downmove.append('p'+str(a))
            else:
                a = hitboxes.index(hit)+1
                stay.append('p'+str(a))
        if len(stay) > 1:
            if stay[0] == stay[1]:
                stay = [str(stay[0]),'p'+str(int(stay[1][1])+1)]
        if len(downmove) > 1:
            if downmove[0] == downmove[1]:
                stay = [str(downmove[0]),'p'+str(int(downmove[1][1])+1)]
        for v in stay:
            val2 = locations.get(str(v))
            newloc[v] = (val2)
            if settings[0]:
                previously[v] = 1
        for c in downmove:
            valuu = locations.get(str(c))
            if settings[0] and prev.get(str(c)) != None:
                newloc[c] = (valuu[0],valuu[1]+int(gravity)+prev.get(c))
                if int(prev.get(str(c))) < 30:
                    previously[c] = prev.get(c)+1
                else:
                    previously[c] = prev.get(c)
            else:
                newloc[c] = (valuu[0],valuu[1]+int(gravity))
        return newloc,previously
            
                
                
    def update(locations,assets,win,elements,mouse,pos,top2,overlays,health,healthbars,maxhealth,font,font2,selected,settings):
        if settings[1]:
            print(mouse,pos)
        xy=[]
        for element in elements:
            win.blit(element,(0,0))
        if 6 < pos[0] < 64 and 6 < pos[1] < 28:
            win.blit(top2,(0,0))    
            if mouse[0] == 1:
                pygame.quit()   
                sys.exit()
                return False
                time.sleep(0.1)
        val = locations.get('p1')
        val2 = locations.get('p2')
        win.blit(assets[0][0],val)
        win.blit(assets[1][0],val2)
        listofoverlays = []
        for c in overlays[0]:   
            listofoverlays.append(pygame.image.load(overlays[3]+'/'+c))
        for i in range(0,int(overlays[2])):
            win.blit(listofoverlays[i],(int(overlays[1][i][0]),int(overlays[1][i][1])))
        mapbox = pygame.Rect(0,-300,1280,720)
        if not -500 < int(locations.get('p1')[1]) < 720:
            health['p1'] = 0
        elif not -500 < int(locations.get('p2')[1]) < 720:
            health['p2'] = 0
        healthperc = {'p1':health.get('p1')/maxhealth[0]*100,'p2':health.get('p2')/maxhealth[1]*100}
        if len(str(healthperc.get('p2'))) == 2:
            healthperc['p2'] = ' '+str(healthperc.get('p2'))
        if len(str(healthperc.get('p2'))) == 1:
            healthperc['p2'] = '  '+str(healthperc.get('p2'))
        text = font.render(str(round(healthperc.get('p1'),1))+'%',True,(255,255,255))
        text2 = font.render(str(round(healthperc.get('p1'),1))+'%',True,(114,137,218))
        text3 = font2.render(selected[0],True,(255,255,255))
        text4 = font2.render(selected[0],True,(114,137,218))
        win.blit(text, (283,720-120))
        win.blit(text2, (281,720-122))
        win.blit(text3, (283,690-121))
        win.blit(text4, (281,690-123))
        text = font.render(str(round(healthperc.get('p2'),1))+'%',True,(255,255,255))
        text2 = font.render(str(round(healthperc.get('p2'),1))+'%',True,(218,114,137))
        text3 = font2.render(selected[1],True,(255,255,255))
        text4 = font2.render(selected[1],True,(218,114,137))
        win.blit(text, (765,720-120))   
        win.blit(text2, (768,720-122))
        win.blit(text3, (823,690-121))
        win.blit(text4, (825,690-123))
        
        pygame.display.update()
        
        return health
    def elements(attacks,win,obstacles,hitboxes,health):
        newattacks1 = []
        newhealth = {}
        newattacks2 = []    
        for attack in attacks.get('p1'):
            doable = True
            for ob in obstacles:
                if ob.colliderect(attack[3]):
                    doable = False
            if hitboxes[1].colliderect(attack[3]):
                damage = int(attack[1][1][1][1])
                doable = False
                if newhealth.get('p2') == None:
                    newhealth['p2'] = health.get('p2')-damage
                else:
                    newhealth['p2'] = newhealth.get('p2')-damage
            else:
                if newhealth.get('p2') == None:
                    newhealth['p2'] = health.get('p2')
                else:
                    newhealth['p2'] = newhealth.get('p2')
            if doable:
                if attack[2][1] == 'right':
                    velocity = int(attack[1][1][4][1])
                else:
                    velocity = -int(attack[1][1][4][1])
                win.blit(attack[0],attack[2][0])
                val = (attack[0],attack[1],((int(attack[2][0][0])+velocity,attack[2][0][1]),attack[2][1]),pygame.Rect(attack[2][0],(attack[0].get_width(),attack[0].get_height())))
                newattacks1.append(val)
        for attack in attacks.get('p2'):
            doable = True
            for ob in obstacles:
                if ob.colliderect(attack[3]):
                    doable = False
            if hitboxes[0].colliderect(attack[3]):
                damage = int(attack[1][1][1][1])
                doable = False
                if newhealth.get('p1') == None:
                    newhealth['p1'] = health.get('p1')-damage
                else:
                    newhealth['p1'] = newhealth.get('p1')-damage
            else:
                if newhealth.get('p1') == None:
                    newhealth['p1'] = health.get('p1')
                else:
                    newhealth['p1'] = newhealth.get('p1')
            if doable:
                if attack[2][1] == 'right':
                    velocity = int(attack[1][1][4][1])
                else:
                    velocity = -int(attack[1][1][4][1])
                win.blit(attack[0],attack[2][0])
                val = (attack[0],attack[1],((int(attack[2][0][0])+velocity,attack[2][0][1]),attack[2][1]),pygame.Rect(attack[2][0],(attack[0].get_width(),attack[0].get_height())))
                newattacks2.append(val)
        if newhealth.get('p1') == None:
            newhealth['p1'] = health.get('p1')
        if newhealth.get('p2') == None:
            newhealth['p2'] = health.get('p2')
        attacks['p1'] = newattacks1; attacks['p2'] = newattacks2
        pygame.display.update()
        return newhealth



        
#init
if __name__ == '__main__':
    game.main()
        


