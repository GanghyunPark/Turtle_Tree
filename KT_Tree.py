from turtle import *
from random import *
from math import *

#랜덤분기 프렉탈 나무
def tree(x, y):
    pendown() 
    t = cos(radians(heading() + 45)) / 8 + 0.25 #음영구현 범위형 나무색
    pencolor(t, 0.4, t)
    pensize(x / 3)
    forward(y)
    if x > 0:
        #랜덤각도 분기 생성
        b = random() * 15 + 10# 랜덤 각도
        c = random() * 15 + 10
        d = y * (random() * 0.35 + 0.6) #랜덤 길이
        right(b)
        tree(x - 1, d)
        left(b + c)
        tree(x - 1, d)
        right(c)
    else:
        #분기의 끝에 원 그리기
        right(90)
        x = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(x+0.1, x+0.1, x+0.1)
        #fillcolor(1, 1, 1)
        # begin_fill()
        circle(3)
        # end_fill()
        left(90)
    pu()
    backward(y)

#Non Random 프렉탈 나무
def tree2(x, y):
    pendown()  # 그리기 시작
    t = cos(radians(heading() + 45)) / 8 + 0.25 #음영 구현 Right 쪽은 약간 어둠게
    pencolor(0.5, t, 0.3) #Right 쪽은 약간 어둠게
    pensize(x / 4)
    forward(y)
    if x > 0:
        #고정각도 분기
        b = 10
        c = 10
        d = y * 0.6
        right(b)
        tree2(x - 1, d)
        left(b + c)
        tree2(x - 1, d)
        right(c)
    else:
        right(90)
        x = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(x-0.05, x-0.1, x-0.1)
        circle(4)
        left(90)
    penup()
    backward(y)

#장식함수
def fractal(x, y, zz, color):
    r, g, b = color, 0, 0
    home()
    goto(x, y)
    pd()
    for x in range(155*2):
        colormode(255)
        pencolor(r, g, b)
        if x < 155 // 3:
            g += 3
        elif x < 155*2 // 3:
            pass
        elif x < 155:
            pass
        elif x < 155*4 // 3:
            g -= 3
        elif x < 155*5 // 3:
            pass
        else:
            pass
        fd(30+zz*x)
        rt(91)
    pu()
    colormode(1)

#잎 표현 함수 5개
def leaf5(backmove, angle, treediver, treesize) :
    for x in range(-2,3) :
        home()
        right(90)
        backward(backmove)
        right(x*angle)
        tree(treediver, treesize)

def leaf4(backmove, angle, treediver, treesize) :
    for x in range(-3,4,2) :
        home()
        right(90)
        backward(backmove)
        right(x*0.5*angle)
        tree(treediver, treesize)

def leaf3(backmove, angle, treediver, treesize) :
    for x in range(-1,2) :
        home()
        right(90)
        backward(backmove)
        right(x*angle)
        tree(treediver, treesize)

def leaf2(backmove, angle, treediver, treesize) :
    for x in range(-1,1) :
        home()
        right(90)
        backward(backmove)
        right(x*0.5*angle)
        tree(treediver, treesize)

def leaf1(backmove, treediver, treesize) :
    home()
    right(90)
    backward(backmove)
    tree(treediver, treesize)

#사전설정
title("KT AIVLE DX - GanghyunPark")
bgcolor(0.1, 0.1, 0.1)  # 배경색
#ht()  # 거북이 숨기기
speed(0)  # 거북이 속도
tracer(0)  # 그리는 과정 표시
pu()

#나무 줄기
for x in range(30):
    home()
    right(90)
    forward(x*10)
    tree2(4, 10+4*(x-20))
    # else:
    #     home()
    #     right(90)
    #     forward(x*10)
    #     tree2(4, 10)

pencolor(1, 1, 1)

# 13층
leaf5(-80, 20, 8, 40)
# 12층
leaf5(-40, 20, 8, 40)
# 11층
leaf4(0,20, 8, 40)
# 10층
leaf4(40,20, 8, 35)
# 9층
leaf4(80,20, 7, 30)
# 8층
leaf3(120, 15, 7, 25)
# 7층
leaf3(160, 15, 7, 25)
# 6층
leaf3(180, 15, 7, 20)
# 5층
leaf3(200, 15, 7, 20)
# 4층
leaf2(220, 30, 6, 15)
# 3층
leaf2(240, 30, 6, 15)
# 2층
leaf1(260, 6, 10)
# 1층
leaf1(260, 6, 10)

# 장식
#넣으니 괴리가 조금 있음
# fractal(300, -300, 0.2, 100)
# fractal(0, 260, 0.05,100)
# fractal(80, -330, 0.1,100)
# fractal(-50, -340, 0.2,100)
# fractal(-200, -300, 0.05,100)
# fractal(-300, -310, 0.2,100)

# 눈 내리는 표현
pencolor(0.4, 0.4, 0.4)
for x in range(200):
    home()
    goto(randint(-450, 450), randint(-400, 400))
    pd()
    fillcolor(0.8, 0.8, 0.8)
    begin_fill()
    circle(randint(1, 4))
    end_fill()
    pu()

#글자쓰기
pencolor(0.7, 0.7, 0.7)
goto(0,250)
write("X-MAS with KT AIVLE",align="center", font=("맑은 고딕", 40, "bold"), move=True)
goto(0,248)
pencolor(0.8, 0.1, 0.1)
write("X-MAS with KT AIVLE",align="center", font=("맑은 고딕", 40, "bold"), move=True)

done()
