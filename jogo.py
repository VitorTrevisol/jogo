from graphics01 import *
from random import*
arquivo = open('pontos.txt', 'r+')
arquivo = arquivo.read()
arquivo = arquivo.split(';')
pontos = 0
win = GraphWin("Meu Campo", 1300, 650, autoflush=False)
velocidade = 30
while True:
    x = 1
    listaIdle = []
    listaJump = []
    listaWalk = []
    listaRun = []
    listaDead = []
    pontos = 0
    ceu = (Image(Point(570,325), 'City3.png'))
    ceu2 = (Image(Point(1726,325), 'City3.png'))
    ceu3 = (Image(Point(2882,325), 'City3.png'))
    calçada = (Image(Point(570,325), 'calçada.png'))
    calçada2 = (Image(Point(1726,325), 'calçada.png'))
    calçada3 = (Image(Point(2882,325), 'calçada.png'))
    caixa = (Image(Point(1400,560), 'caixa.png'))
    caixa1 = (Image(Point(1400,560), 'caixa.png'))
    caixa2 = (Image(Point(1400,560), 'caixa.png'))
    caixa3 = (Image(Point(1400,560), 'caixa.png'))
    rect1 = Rectangle(Point(145, 490), Point(195, 597))
    rect1.setWidth(0) 
    rect2 = Rectangle(Point(1366, 522), Point(1436, 590))
    rect2.setWidth(0)
    rect3 = Rectangle(Point(1366, 522), Point(1436, 590))
    rect3.setWidth(0)
    rect4 = Rectangle(Point(1366, 522), Point(1436, 590))
    rect4.setWidth(0)
    rect5 = Rectangle(Point(1366, 522), Point(1436, 590))
    rect5.setWidth(0)
    texto_pontos = Text(Point(650, 97), "max:  " + str(arquivo[1]))
    texto_pontos.setSize(30)
    texto_pontos.setTextColor('White')
    rect = Rectangle(Point(475, 70), Point(850, 120))
    rect.setFill('Black')
    anterior = arquivo[0].split(';')
    anterior = anterior[0]
    texto_pontos1 = Text(Point(650, 155), "Anterior: " + anterior)
    texto_pontos1.setSize(30)
    texto_pontos1.setTextColor('White')
    rect0 = Rectangle(Point(475, 130), Point(850,180))
    rect0.setFill('Black')
    obstaculo = 0
    na_tela = [True,False,False,False]
    continua = True
    caixas = [caixa.getAnchor(),caixa1.getAnchor(),caixa2.getAnchor(),caixa3.getAnchor()]
    confirma = True
    for cont in range(1,16):
        listaRun.append(Image(Point(200,550), 'flatboy\Run ('+str(cont)+').png'))
        listaJump.append(Image(Point(200,550), 'flatboy\Jump ('+str(cont)+').png'))
        listaDead.append(Image(Point(200,550), 'flatboy\Dead ('+str(cont)+').png'))
    def desenhaf():
        ceu.draw(win)
        ceu2.draw(win)
        ceu3.draw(win)
        rect1.draw(win)
        texto_pontos.setText(pontos)
        rect.draw(win)
        texto_pontos.draw(win)
        if na_tela[0]:
            rect2.draw(win)
            caixa.draw(win)
            rect2.move(-10,0)
            caixa.move(-10,0)
        if na_tela[1]:
            rect3.draw(win)
            caixa1.draw(win)
            rect3.move(-10,0)
            caixa1.move(-10,0)
        if na_tela[2]:
            rect4.draw(win)
            caixa2.draw(win)
            rect4.move(-10,0)
            caixa2.move(-10,0)
        if na_tela[3]:
            rect5.draw(win)
            caixa3.draw(win)
            rect5.move(-10,0)
            caixa3.move(-10,0)
        ceu.move(-10,0)
        ceu2.move(-10,0)
        ceu3.move(-10,0)
        meio = [ceu.getAnchor(),ceu2.getAnchor(),ceu3.getAnchor()]
        if meio[1].getX() == 576:
            ceu.move(3460,0)
        if meio[2].getX() == 582:
            ceu2.move(3460,0)
        if meio[0].getX() == 570:
            ceu3.move(3460,0)
    def verifica_colisao(rect1, rect2, rect3, rect4, rect5):
        x1, y1, x2, y2 = rect1.getP1().getX(), rect1.getP1().getY(), rect1.getP2().getX(), rect1.getP2().getY()
        x3, y3, x4, y4 = rect2.getP1().getX(), rect2.getP1().getY(), rect2.getP2().getX(), rect2.getP2().getY()
        x5, y5, x6, y6 = rect3.getP1().getX(), rect3.getP1().getY(), rect3.getP2().getX(), rect3.getP2().getY()
        x7, y7, x8, y8 = rect4.getP1().getX(), rect4.getP1().getY(), rect4.getP2().getX(), rect4.getP2().getY()
        x9, y9, x0, y0 = rect5.getP1().getX(), rect5.getP1().getY(), rect5.getP2().getX(), rect5.getP2().getY()
        if (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1) and (x2 <x5 or x6 <x1 or y2 <y5 or y6 < y1) and (x2 <x7 or x8 <x1 or y2 <y7 or y8 < y1) and (x2 <x9 or x0 <x1 or y2 <y9 or y0 < y1) :
            return True
        else:
            time.sleep(0.1)
            return False
    def apagaf():
        ceu.undraw()
        ceu2.undraw()
        rect1.undraw()
        ceu3.undraw()
        rect.undraw()
        texto_pontos.undraw()
        if na_tela[0]:
            rect2.undraw()
            caixa.undraw()
        if na_tela[1]:
            rect3.undraw()
            caixa1.undraw()
        if na_tela[2]:
            rect4.undraw()
            caixa2.undraw()
        if na_tela[3]:
            rect5.undraw()
            caixa3.undraw()
    obstaculo = 0
    def objeto(obstaculo):
        caixas = [caixa.getAnchor(),caixa1.getAnchor(),caixa2.getAnchor(),caixa3.getAnchor()]
        if caixas[0].getX() == -100:
            caixa.move(1500,0)
            rect2.move(1500,0)
            rect2.undraw()
            caixa.undraw()
            na_tela[0] = False
        if caixas[1].getX() == -100:
            caixa1.move(1500,0)
            rect3.move(1500,0)
            caixa1.undraw()
            rect3.undraw()
            na_tela[1] = False
        if caixas[2].getX() == -100:
            caixa2.move(1500,0)
            rect4.move(1500,0)
            caixa2.undraw()
            rect4.undraw()
            na_tela[2] = False    
        if caixas[3].getX() == -100:
            caixa3.move(1500,0)
            rect5.move(1500,0)
            caixa3.undraw()
            rect5.undraw()
            na_tela[3] = False   
        cont = obstaculo
        aleatorio = 0
        if obstaculo > 29:
            aleatorio = randint(0,2)
            cont = 0 
        cont += 1
        if aleatorio == 0:
            return cont
        else:
            if not na_tela[0]:
                na_tela[0] = True
            elif not na_tela[1]:
                na_tela[1] = True
            elif not na_tela[2]:
                na_tela[2] = True
            elif not na_tela[3]:
                na_tela[3] = True
            aleatorio = 0
            return cont
    

    ceu.draw(win) 
    ceu2.draw(win)
    ceu3.draw(win)
    rect.draw(win)
    texto_pontos.draw(win)
    rect0.draw(win)
    texto_pontos1.draw(win)
    começa = win.getKey()
    ceu.undraw()
    ceu2.undraw()
    ceu3.undraw()
    texto_pontos.undraw()
    rect.undraw()
    rect0.undraw()
    texto_pontos1.undraw()
    velocidade = 35
    print(começa)
    if começa == 'Escape':
        win.close()
        break

    cont = 0
    cont2 = 0
    aumenta = 200
    while verifica_colisao(rect1, rect2, rect3, rect4, rect5):
        pontos += 1
        
        aleatorio = 0
        desenhaf() 
        obstaculo = objeto(obstaculo)
        listaRun[cont].draw(win)
        tecla = win.checkKey()
        update(30)
        listaRun[cont].undraw()
        apagaf()
        caixa1.undraw()
        cont+=1
        if cont == 15:
            cont = 0
        if tecla != '':
            confirma = False
            cont = 0
        contm = 0
        confirma = True
        if tecla == 'space':
            while verifica_colisao(rect1, rect2, rect3, rect4, rect5) and confirma:
                pontos +=1
                obstaculo = objeto(obstaculo)
                if cont<11:
                    for x in listaJump:
                        x.move(0,-12)
                    rect1.move(0,-12)
                elif cont<12:
                    rect1.move(0,0)
                elif cont>18:
                    for x in listaJump:
                        x.move(0,12)
                    rect1.move(0,12)
                desenhaf()
                listaJump[contm].draw(win)
                update(30)
                apagaf()
                listaJump[contm].undraw()
                cont+=1
                contm +=1
                if cont == 15: 
                    contm = 0
                if cont == 30:
                    confirma = False
                    z = ''
            cont = 0
        tecla = ''
        confirma = True
        primeiro = 0
        contm = 0
    arquivo[0] = str(pontos) + ';'
    if arquivo[0] > arquivo[1]:
        arquivo[1] = str(pontos)
    arquivo1 = open('pontos.txt', 'w')
    arquivo1.write(arquivo[0] + arquivo[1])
