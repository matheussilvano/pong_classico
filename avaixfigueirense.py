# Esse código se trata um jogo no estilo "pong", do clássico de Florianópolis Avaí x Figueirense

import turtle

# janela e background (campo)
campo = turtle.Screen()
campo.title('Pong by Matheus Silvano')
campo.bgcolor('#006400')
campo.setup(width=800, height=600)
campo.tracer(0)

# score
score_avai = 0
score_figueirense = 0

# Jogador Avaí
jogador_avai = turtle.Turtle()
jogador_avai.speed(0)
jogador_avai.shape('square')
jogador_avai.color('white', 'blue')
jogador_avai.shapesize(stretch_wid=5, stretch_len=1)
jogador_avai.penup()
jogador_avai.goto(-350, 0)

# Jogador Figueirense
jogador_figueirense = turtle.Turtle()
jogador_figueirense.speed(0)
jogador_figueirense.shape('square')
jogador_figueirense.color('white', 'black')
jogador_figueirense.shapesize(stretch_wid=5, stretch_len=1)
jogador_figueirense.penup()
jogador_figueirense.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape('circle')
bola.color('black', 'white')
bola.penup()
bola.goto(0, 0)
bola.dx = 0.3
bola.dy = 0.3

# Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color('white')
placar.penup()
placar.hideturtle()
placar.goto(0,260)
placar.write('AVAÍ: 0     FIGUEIRENSE: 0', align='center', font=('Arial', 24, 'bold'))



# Funções jogador Avaí
def jogador_avai_up():
    y = jogador_avai.ycor()
    y += 20
    jogador_avai.sety(y)
def jogador_avai_down():
    y = jogador_avai.ycor()
    y -= 20
    jogador_avai.sety(y)

# Funções jogador Figueirense
def jogador_figueirense_up():
    y = jogador_figueirense.ycor()
    y += 20
    jogador_figueirense.sety(y)
def jogador_figueirense_down():
    y = jogador_figueirense.ycor()
    y -= 20
    jogador_figueirense.sety(y)

# Compatibilidade com o teclado
campo.listen()
campo.onkeypress(jogador_avai_up, 'w')
campo.onkeypress(jogador_avai_down, 's')
campo.onkeypress(jogador_figueirense_up, 'Up')
campo.onkeypress(jogador_figueirense_down, 'Down')

# loop do jogo
while True:
    campo.update()

    # movimento da bola
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # rebote da bola
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_avai += 1
        placar.clear()
        placar.write(f'AVAÍ: {score_avai}     FIGUEIRENSE: {score_figueirense}', align='center', font=('Arial', 24, 'bold'))
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_figueirense += 1
        placar.clear()
        placar.write(f'AVAÍ: {score_avai}     FIGUEIRENSE: {score_figueirense}', align='center', font=('Arial', 24, 'bold'))


    # colisão da bola com os jogadores
    if (bola.xcor() > 340 and bola.xcor() < 350 and (bola.ycor() < jogador_figueirense.ycor() + 40 and bola.ycor() > jogador_figueirense.ycor() -40)):
        bola.setx(340)
        bola.dx *= -1
    if (bola.xcor() < -340 and bola.xcor() > -350 and (bola.ycor() < jogador_avai.ycor() + 40 and bola.ycor() > jogador_avai.ycor() -40)):
        bola.setx(-340)
        bola.dx *= -1
