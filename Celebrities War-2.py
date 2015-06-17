# -*- coding: utf-8 -*-
import pygame
from random import randint
pygame.init()
def cartajogada():
    global comm
    global cem
    global teste
    global ud
    global cd
    for i in cem:
        if i in teste:
            if i != "Chuck Norris":
                del teste[i]
    for i in comm:
        if i in teste:
            if i != "Chuck Norris":
                del teste[i]
    for i in ud:
        if i in teste:
            if i != "Chuck Norris":
                del teste[i]
    for i in cd:
        if i in teste:
            if i != "Chuck Norris":
                del teste[i]
    carta=""
    valor=0
    v=""
    if len(cd)>0:
        for i in cd:
            comm[i]=cd[i]
            v=i
        del cd[v]
    cont=0
    for i in comm:
        for j in teste:
            valor1=0
            for k in range(5):
                valor1+=comm[i][k]-teste[j][k]
            if valor1>valor:
                valor=valor1
                carta=i
            if cont==0:
                valor=valor1
                carta=i
            cont+=1
    return carta
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
jogadores=dict()
jogadores2=dict()
jogadores2["Karl Marx"]=pygame.image.load("Karl Marx.jpg")
jogadores2["Willian Bonner"]=pygame.image.load("Willian Bonner.jpg")
jogadores2["Ze Gotinha"]=pygame.image.load("Ze Gotinha.jpg")
jogadores2["Papa Franscisco"]=pygame.image.load("Papa Franscisco.jpg")
jogadores2["Joanna D'Arc"]=pygame.image.load("Joanna D'Arc.jpg")
jogadores2["Dilma"]=pygame.image.load("Dilma.jpg")
jogadores2["catra"]=pygame.image.load("MR CATRA.jpg")
jogadores2["catra"]=pygame.image.load("MR CATRA.jpg")
jogadores2["hulk"]=pygame.image.load("HULK.jpg")
jogadores2["Carl Johnson"]=pygame.image.load("cj.jpg")
jogadores2["Einstein"]=pygame.image.load("Einstein.jpg")
jogadores2["Jimmy Neutron"]=pygame.image.load("Jimmy Neutron.jpg")
jogadores2["Loro Jose"]=pygame.image.load("Loro Jose.jpg")
jogadores2["doly"]=pygame.image.load("DOLLYNHO.jpg")
jogadores2["obama"]=pygame.image.load("OBAMA.jpg")
jogadores2["BILL"]=pygame.image.load("BILL.jpg")
jogadores2["BIN LADEN"]=pygame.image.load("BIN LADEN.jpg")
jogadores2["PIKACHU"]=pygame.image.load("PIKACHU.jpg")
jogadores2["RONALDINHO"]=pygame.image.load("RONALDINHO.jpg")
jogadores2["RYU"]=pygame.image.load("RYU.jpg")
jogadores2["SILVIO SANTOS"]=pygame.image.load("SILVIO SANTOS.jpg")
jogadores2["VEGETA"]=pygame.image.load("VEGETA.jpg")
jogadores2["YUGI"]=pygame.image.load("YUGI.jpg")
jogadores2["BUZZ"]=pygame.image.load("BUZZ.jpg")
jogadores2["CAPITAO AMERICA"]=pygame.image.load("CAPITAO AMERICA.jpg")
jogadores2["CAPITAO NAS"]=pygame.image.load("CAPITAO NAS.jpg")
jogadores2["FAUSTAO"]=pygame.image.load("FAUSTAO.jpg")
jogadores2["GOKU"]=pygame.image.load("GOKU.jpg")
jogadores2["HOMEM ARANHA"]=pygame.image.load("HOMEM ARANHA.jpg")
jogadores2["JESUS"]=pygame.image.load("JESUS.jpg")
jogadores2["MAJIN BOO"]=pygame.image.load("MAJIN BOO.jpg")
jogadores2["MARIO BROS"]=pygame.image.load("MARIO BROS.jpg")
jogadores2["PELE"]=pygame.image.load("PELE.jpg")

habi=0
valid=dict()
teste=dict()
usu=dict()#carta do usuario
com=dict()#carta do computador
usum=dict()#carta do usuario na mao
comm=dict()#carta do computador na mao 
valor=0
pusu=40#pontos
pcom=40

cem=dict()
venc=0
ud=dict()
cd=dict()
vs=pygame.image.load("vs.jpg")
cat=pygame.image.load("cat.jpg")
hab=pygame.image.load("hab.jpg")
inte=pygame.image.load("inte.jpg")
inf=pygame.image.load("inf.jpg")
alt=pygame.image.load("alt.jpg")
fora=pygame.image.load("for.jpg")
display_width = 1310
display_height = 670
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 40)
greatfont = pygame.font.SysFont("comicsansms", 80)


gameDisplay = pygame.display.set_mode((display_width,display_height))
#plataforma de uso

pygame.display.set_caption('CELEBRITIES WAR')
game_exit = False

def msg_to_button(msg,color, buttonx, buttony,buttonwidth,buttonheight,size="small"):
    textsurf, textrect = text_objects(msg,color,size)    
    textrect.center = buttonx+(buttonwidth/2),buttony+(buttonheight/2)
    gameDisplay.blit(textsurf, textrect)

def message_screen(msg,color, y, x ,y_dispace=0, size="small"):
    
    textsurf, textrect = text_objects(msg,color,size)    
    textrect.center = (x), (y) + y_dispace
    gameDisplay.blit(textsurf, textrect)
    
def text_objects(text,color,size):
    
    if size == "small":
        textsurface = smallfont.render(text, True, color)
    elif size == "med":
        textsurface = medfont.render(text, True, color)    
    elif size == "great":
        textsurface = greatfont.render(text, True, color)   
         
    return textsurface, textsurface.get_rect()
    

def button1(x,y,width,height,inactive1,active1,i, action1):
    cur = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(jogadores2[i],(x,y,width,height))
        if click1[0] == 1 and action1 != None:
            gameDisplay.fill(white)
            battleloop(x,y,width,height,inactive1,active1,i, action1,randint(0,4))
    else:
        gameDisplay.blit(pygame.image.load("fundo.jpg"),(x,y,width,height))
    pygame.display.update()
def botao(x,y,width,height,inactive1,active1):
    cur = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(active1,(x,y,width,height))
        if click1[0] == 1 and active1 != None:
            gameDisplay.fill(white)
            gameloop()
    else:
        gameDisplay.blit(active1,(x,y,width,height))
    pygame.display.update()
def botao1(x,y,width,height,inactive1,active1):
    cur = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(active1,(x,y,width,height))
        if click1[0] == 1 and active1 != None:
            gameDisplay.fill(white)
            fim()
    else:
        gameDisplay.blit(active1,(x,y,width,height))
    pygame.display.update()
def botao2(x,y,width,height,inactive1,active1):
    cur = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(active1,(x,y,width,height))
        if click1[0] == 1 and active1 != None:
            start()
    else:
        gameDisplay.blit(active1,(x,y,width,height))
    pygame.display.update()
def sair(x,y,width,height,inactive1,active1):
    cur = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(active1,(x,y,width,height))
        if click1[0] == 1 and active1 != None:
            pygame.quit()
    else:
        gameDisplay.blit(active1,(x,y,width,height))
def battleloop(x,y,width,height,inactive1,active1,i, action1, habi):
    battle = False
    y=i
    global pusu
    global pcom
    carta=cartajogada()
    if valid[carta][habi]<valid[y][habi]:
        pcom-=abs(valid[carta][habi]-valid[y][habi])
    else:
        pusu-=abs(valid[carta][habi]-valid[y][habi])
    gameDisplay.blit(jogadores2[y],(10,50,315,516))
    gameDisplay.blit(vs,(600,50,118,81))
    gameDisplay.blit(jogadores2[carta],(10+315+10+315+10+10+315,50,315,516))
    gameDisplay.blit(cat,(400,200,232,48))
    while battle == False:
        
        p=cartajogada()
        sair(700,600,98,39,black,pygame.image.load("sair.jpg"))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if habi==0:
                gameDisplay.blit(hab,(700,200,195,37))
            elif habi==1:
                gameDisplay.blit(fora,(700,200,113,41))
            elif habi==2:
                gameDisplay.blit(inte,(700,200,213,41))
            elif habi==3:
                gameDisplay.blit(inf,(700,200,182,35))
            elif habi==4:
                gameDisplay.blit(alt,(700,200,182,37))
            if valid[carta][habi]>valid[y][habi]:
                if valid[carta][habi]-valid[y][habi]==1:
                    gameDisplay.blit(pygame.image.load("1.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==2:
                    gameDisplay.blit(pygame.image.load("2.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==3:
                    gameDisplay.blit(pygame.image.load("3.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==4:
                    gameDisplay.blit(pygame.image.load("4.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==5:
                    gameDisplay.blit(pygame.image.load("5.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==6:
                    gameDisplay.blit(pygame.image.load("6.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==7:
                    gameDisplay.blit(pygame.image.load("7.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==8:
                    gameDisplay.blit(pygame.image.load("8.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==9:
                    gameDisplay.blit(pygame.image.load("9.jpg"),(450,300,182,37))
                if y in usum:
                    com[y]=usum[y]
                    del usum[y]
                    if len(usu)>0:
                        h=randint(0,len(usu)-1)
                        cont=0
                        t=""
                        for r in usu:
                            if cont==h:
                                usum[r]=usu[r]
                                t=r
                            cont+=1
                        del usu[t]
                    if carta==p and len(com)>0:
                        h=randint(0,len(com)-1)
                        cont=0
                        t=""
                        for i in com:
                            if cont==h:
                                comm[i]=com[i]
                                t=i
                            cont+=1
                        del com[t]
                        com[carta]=comm[carta]
                        del comm[carta]
            if valid[carta][habi]==valid[y][habi]:
                gameDisplay.blit(pygame.image.load("empate.jpg"),(450,300,182,37))
            if valid[carta][habi]<valid[y][habi]:
                if valid[carta][habi]-valid[y][habi]==-1:
                    gameDisplay.blit(pygame.image.load("11.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-2:
                    gameDisplay.blit(pygame.image.load("22.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-3:
                    gameDisplay.blit(pygame.image.load("33.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-4:
                    gameDisplay.blit(pygame.image.load("44.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-5:
                    gameDisplay.blit(pygame.image.load("55.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-6:
                    gameDisplay.blit(pygame.image.load("66.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-7:
                    gameDisplay.blit(pygame.image.load("77.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-8:
                    gameDisplay.blit(pygame.image.load("88.jpg"),(450,300,182,37))
                elif valid[carta][habi]-valid[y][habi]==-9:
                    gameDisplay.blit(pygame.image.load("99.jpg"),(450,300,182,37))
                if carta==p:
                    usu[p]=comm[p]
                    del comm[p]
                    if len(com)>0:
                        h=randint(0,len(com)-1)
                        cont=0
                        t=""
                        for r in com:
                            if cont==h:
                                comm[r]=com[r]
                                t=r
                            cont+=1
                        del com[t]
                    if y==i and len(usu)>0:
                        h=randint(0,len(usu)-1)
                        cont=0
                        t=""
                        for i in usu:
                            if cont==h:
                                usum[i]=usu[i]
                                t=i
                            cont+=1
                        del usu[t]
                        usu[y]=usum[y]
                        del usum[y]
            message_screen( "Você tem " + str(pusu) + " pontos", black, 20, 150)
            message_screen( "Oponente tem " + str(pcom) + " pontos", black, 20, 1140)
            if len(usum)>0 and len(comm)>0 and pusu>0 and pcom>0:
                botao(250,600,316,51,black,pygame.image.load("ro.jpg"))
            else:
                botao1(250,600,195,44,black,pygame.image.load("cont.jpg"))
        
        
def fim():
    battle = False
    global pusu
    global pcom
    global comm
    global usum
    while battle == False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if pcom<1:
                gameDisplay.blit(pygame.image.load("ga.jpg"),(100,200,543,118))
            elif pusu<1:
                gameDisplay.blit(pygame.image.load("per.jpg"),(450,300,503,207))
            elif len(comm)==0:
                gameDisplay.blit(pygame.image.load("ga.jpg"),(100,200,543,118))
            elif len(usum)==0:
                gameDisplay.blit(pygame.image.load("per.jpg"),(450,300,503,207))
            botao2(250,600,195,44,black,pygame.image.load("cont.jpg"))
            sair(700,600,98,39,black,pygame.image.load("sair.jpg"))
def gameloop():
    global habi
    global valor
    global usu
    global com
    global pusu
    global pcom
    global venc
    global ud
    global cd
    global cem
    global jogadores
    global jogadores2
    global teste
    global valid
    global usum
    global com
    battle = False
    message_screen( "Você tem " + str(pusu) + " pontos", black, 20, 150)
    message_screen( "Oponente tem " + str(pcom) + " pontos", black, 20, 1140)
    if len(comm)<4 and len(com)>0:
        k=randint(0,len(com)-1)
        cont=0
        for i in com:
            if cont==k:
                comm[i]=com[i]
                o=i
            cont+=1
        del com[o]
    if len(usum)<4 and len(usu)>0:
        k=randint(0,len(usu)-1)
        cont=0
        for i in usu:
            if cont==k:
                usum[i]=usu[i]
                o=i
            cont+=1
        del usu[o]
    ii=0
    while battle == False:
        
        for event in pygame.event.get():
            if ii==0:
                gameDisplay.blit(pygame.image.load("AZUL.jpg"),(0,0,1310,670))
                ii=1
                message_screen( "Você tem " + str(pusu) + " pontos", white, 20, 150)
                message_screen( "Oponente tem " + str(pcom) + " pontos", white, 20, 1140)
            if event.type==pygame.QUIT:
                pygame.quit()
            cont=0
            for i in usum:
                if cont==0:
                    button1(10,50,315,516,black,jogadores2[i],i, i)
                elif cont==1:
                    button1(10+315+10,50,315,516,black,jogadores2[i],i, i)
                elif cont==2:
                    button1(10+315+10+315+10,50,315,516,black,jogadores2[i],i,i)
                else:
                    button1(10+315+10+315+10+10+315,50,315,516,black,jogadores2[i],i, i)
                cont+=1
            sair(700,600,98,39,black,pygame.image.load("sair.jpg"))
def start():
            global habi
            global valor
            global pusu
            global pcom
            global venc
            global ud
            global cd
            global cem
            global usum
            global comm
            global jogadores
            global jogadores2
            global teste
            global valid
            global usu
            global com
            habi=0
            valid=dict()
            teste=dict()
            usu=dict()#carta do usuario
            com=dict()#carta do computador
            usum=dict()#carta do usuario na mao
            comm=dict()#carta do computador na mao 
            valor=0
            pusu=25#pontos
            pcom=25
            jogadores=dict()
            jogadores["Karl Marx"]=([8,2,8,9,7])
            jogadores["Willian Bonner"]=([6,4,8,7,5])
            jogadores["Ze Gotinha"]=([2,1,5,6,9])
            jogadores["hulk"]=([6,10,7,4,5])
            jogadores["Papa Franscisco"]=([6,2,5,8,10])
            jogadores["doly"]=([3,1,4,2,3])
            jogadores["PIKACHU"]=([8,6,1,1,6])
            jogadores["RONALDINHO"]=([9,3,2,8,5])
            jogadores["RYU"]=([10,8,3,2,1])
            jogadores["SILVIO SANTOS"]=([6,2,5,7,8])
            jogadores["VEGETA"]=([9,9,6,3,3])
            jogadores["YUGI"]=([9,2,6,5,4])
            jogadores["Einstein"]=([6,2,10,8,9])
            jogadores["Jimmy Neutron"]=([8,1,10,2,6])
            jogadores["Joanna D'Arc"]=([7,6,7,9,10])
            jogadores["Dilma"]=([4,4,6,7,4])
            jogadores["Carl Johnson"]=([6,7,4,5,1])
            jogadores["catra"]=([8,4,2,6,7])
            jogadores["Loro Jose"]=([1,1,1,1,6])
            jogadores["obama"]=([4,3,8,10,9])
            jogadores["BILL"]=([8,1,10,6,6])
            jogadores["BIN LADEN"]=([4,3,6,9,1])
            jogadores["BUZZ"]=([7,2,6,2,7])
            jogadores["CAPITAO AMERICA"]=([7,7,4,8,9])
            jogadores["CAPITAO NAS"]=([6,3,7,2,4])
            jogadores["FAUSTAO"]=([6,2,5,5,8])
            jogadores["GOKU"]=([9,10,5,5,8])
            jogadores["HOMEM ARANHA"]=([7,6,8,2,2])
            jogadores["JESUS"]=([7,1,6,10,8])
            jogadores["MAJIN BOO"]=([10,10,1,1,8])
            jogadores["MARIO BROS"]=([8,3,2,7,5])
            jogadores["PELE"]=([10,3,3,10,8])
            k=len(jogadores)/2
            for i in jogadores:
                valid[i]=jogadores[i]
            for i in jogadores:
                teste[i]=jogadores[i]
            for i in range(int(k)):
                j=randint(0,len(jogadores)-1)
                atual=0
                v=""
                for a in jogadores:
                    if atual==j:
                        usu[a]=jogadores[a]
                        v=a
                    atual+=1
                del jogadores[v]
                j=randint(0,len(jogadores)-1)
                atual=0
                v=""
                for a in jogadores:
                    if atual==j:
                        com[a]=jogadores[a]
                        v=a
                    atual+=1
                del jogadores[v]
            for i in range(4):
                j=randint(0,len(usu)-1)
                atual=0
                for a in usu:
                    if atual==j:
                        usum[a]=usu[a]
                        v=a
                    atual+=1
                del usu[v]
                j=randint(0,len(usu)-1)
                atual=0
                for a in com:
                    if atual==j:
                        comm[a]=com[a]
                        v=a
                    atual+=1
                del com[v]
            cem=dict()
            venc=0
            ud=dict()
            cd=dict()
            gameDisplay.fill(white)
            gameloop()
def inicio(x,y,width,height,active1):
    cur = pygame.mouse.get_pos()
    click1 = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(pygame.image.load("iniciar.jpg"),(111,111,543,69))
        if click1[0] == 1 and active1 != None:
            start()
    else:
        gameDisplay.blit(pygame.image.load("iniciar.jpg"),(111,111,543,69))
        
def ini():
    battle=False
    while battle == False:
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT:
                pygame.quit()
            sair(700,600,98,39,black,pygame.image.load("sair.jpg"))
            inicio(111,111,543,69,pygame.image.load("iniciar.jpg"))
gameDisplay.fill(white)
ini()