from turtle import *
from random import *
from math import *
#Google검색 Keyword - python, turtle, tree
#https://www.programmersought.com/article/52275503406/ 링크를 참조
#랜덤분기 프렉탈 나무
def tree(x, y):
    pendown() 
    t = cos(radians(heading() + 45)) / 8 + 0.25 #음영구현
    pencolor(t, 0.4, t) #G는 0.4로 고정하여 약간 녹색빛을 띄게 하였음
    pensize(x / 3)
    forward(y)
    if x > 0:
        #랜덤각도 분기 생성
        b = random() * 15 + 10#랜덤각도
        c = random() * 15 + 10
        d = y * (random() * 0.35 + 0.6) #랜덤길이
        right(b)
        tree(x - 1, d) #분기될수록 얇게
        left(c)
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

def treeright(x, y):
    pendown() 
    t = cos(radians(heading() + 45)) / 8 + 0.25 #음영구현
    pencolor(t-0.1, 0.3, t-0.1) #Right는 조금 어둡게 하였음
    pensize(x / 3)
    forward(y)
    if x > 0:
        #랜덤각도 분기 생성
        b = random() * 15 + 10#각도
        c = random() * 15 + 10
        d = y * (random() * 0.35 + 0.6) #길이
        #분기 각을 같은쪽으로 휘게하였음
        left(b)
        treeright(x - 1, d)
        right(c)
        treeright(x - 1, d)
        left(c)
    else:
        #분기의 끝에 작은 원 그리기
        right(90)
        x = cos(radians(heading() - 45)) / 4 + 0.5
        #살짝 밝게 하였음
        pencolor(x+0.1, x+0.1, x+0.1)
        #채워보니 아니다싶어서 빈 원으로 그림
        #fillcolor(1, 1, 1)
        # begin_fill()
        circle(3)
        # end_fill()
        left(90)
    pu()
    backward(y)

#Non Random 프렉탈 나무 - 가지 만들때 쓰기위해 만들었음
def tree2(x, y):
    pendown()  # 그리기 시작
    t = cos(radians(heading() + 45)) / 8 + 0.25 #음영 구현
    #갈색빛 구현
    pencolor(0.5, t, 0.3)
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
        #갈색빛 구현
        pencolor(x-0.05, x-0.1, x-0.1)
        circle(4)
        left(90)
    penup()
    backward(y)

#장식함수 - 어울리지않아서 쓰진않았음
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

#잎 표현 함수 5개 - 풍성해보이기위해 분기나무표현모듈을 5개에서 1개까지 중첩하는 모듈
def leaf5(backmove, angle, treediver, treesize, yesright = 1) :
    for x in range(-2,3) :
        home()
        right(90)
        backward(backmove)
        right(x*angle)
        if yesright == 1 :
                tree(treediver, treesize)
        else :
            treeright(treediver, treesize)

def leaf4(backmove, angle, treediver, treesize, yesright = 1) :
    for x in range(-3,4,2) :
        home()
        right(90)
        backward(backmove)
        right(x*0.5*angle)
        if yesright == 1 :
                tree(treediver, treesize)
        else :
            treeright(treediver, treesize)

def leaf3(backmove, angle, treediver, treesize, yesright = 1) :
    for x in range(-1,2) :
        home()
        right(90)
        backward(backmove)
        right(x*angle)
        if yesright == 1 :
                tree(treediver, treesize)
        else :
            treeright(treediver, treesize)

def leaf2(backmove, angle, treediver, treesize, yesright = 1) :
    for x in range(-1,1) :
        home()
        right(90)
        backward(backmove)
        right(x*0.5*angle)
        if yesright == 1 :
                tree(treediver, treesize)
        else :
            treeright(treediver, treesize)

def leaf1(backmove, treediver, treesize, yesright = 1,rightr =0, forw = 0) :
    home()
    right(90)
    backward(backmove)
    right(rightr)
    forward(forw)
    if yesright == 1 :
                tree(treediver, treesize)
    else :
        treeright(treediver, treesize)

#사전설정
title("KT AIVLE DX - GanghyunPark")
bgcolor(0.1, 0.1, 0.1)  # 배경색
ht()  # 거북이 숨기기
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
#마지막 꾸미기
leaf1(-100,8,40,rightr =30, forw= 40)
leaf1(-100,8,40,rightr =-30, yesright=0, forw= 40)
leaf1(-80,8,40,rightr =30, forw= 40)
leaf1(-80,8,40,rightr =-30, yesright=0, forw= 40)
leaf1(-80,8,40,rightr =15, forw= 30)
leaf1(-80,8,35,rightr =-15, yesright=0, forw= 30)
# 14층
leaf5(-80, 35, 8, 40)
#leaf5(-80, 35, 8, 40, yesright=0)
# 13층
leaf5(-60, 30, 8, 40)
#leaf5(-60, 30, 8, 40, yesright=0)
# 12층
leaf5(-40, 30, 8, 40)
leaf5(-40, 30, 8, 40, yesright=0)
# 11층
leaf4(0,30, 8, 35)
leaf4(0,30, 8, 35, yesright=0)
# 10층
leaf4(40,20, 8, 35)
#leaf4(40,20, 8, 35,yesright=0)
# 9층
leaf4(80,20, 7, 30)
leaf4(80,20, 7, 30, yesright=0)
# 8층
leaf3(120, 15, 7, 25)
leaf3(120, 15, 7, 25,yesright=0)
# 7층
leaf3(160, 15, 7, 25)
#leaf3(160, 15, 7, 25, yesright=0)
# 6층
leaf3(180, 15, 7, 20)
leaf3(180, 12, 7, 20, yesright=0)
# 5층
leaf3(200, 15, 6, 20)
leaf3(200, 12, 6, 20, yesright=0)
# 4층
leaf2(220, 10, 6, 15)
leaf2(220, 10, 6, 15, yesright=0)
# 3층
leaf2(240, 10, 6, 15)
leaf2(240, 10, 6, 15, yesright=0)
# 2층
leaf1(260, 6, 15)
leaf1(260, 6, 15, yesright=0)
# 1층
leaf1(260, 6, 10)
leaf1(260, 6, 10, yesright=0)

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
