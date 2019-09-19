#imports
import pygame , sys, random
pygame.init()

#gamevar
width = 1280
height= 720
clock = pygame.time.Clock()

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
            if mouse[0] == 1:
                pygame.quit()   
                sys.exit()
                return False
            else:
                return True
        elif 300 < v[0]  < 905 and 502 < v[1] < 530:
            if mouse[0] == 1:
                return False
                print('started')
            else:
                return True
        else:
            frame.update(items,win,0,0,particles,pa)
            return True
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
            clock.tick(120)
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
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.display.update()
                        pygame.quit()
                        sys.exit()
                    mouse = pygame.mouse.get_pressed()
                    frame.update(items,win,0,0,particles,pa)
                
                    pos = pygame.mouse.get_pos()
                    running = frame.check(mouse,pos,top2,win,top,items,particles,pa)
    def game(player1,player2):
        return
                    




                    



               
                
        
#init
if __name__ == '__main__':
    game.main()



