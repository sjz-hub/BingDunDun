# Author:孙建钊
# StartTime:2022/02/14 15:29
# EndTime:
# content:使用python绘制一个冰墩墩

import turtle as t
import math

def numTwo(proportion=1):

    t.seth(45)
    t.fd(2*proportion)
    t.seth(0)
    t.fd(2*proportion)
    t.seth(-45)
    t.fd(2*proportion)
    t.seth(-90)
    t.fd(3*proportion)
    t.seth(-150)
    t.fd(6*proportion)
    t.seth(-90)
    t.fd(1*proportion)
    t.seth(0)
    t.fd(6*proportion)


def lineWidth(length,width):
    for i in range(width):
        if i % 2 == 0:
            t.fd(length)
            pos = t.pos()
        else:
            t.fd(-length)
        t.right(90)
        t.fd(1)
        t.left(90)
    t.goto(pos)

def ellipse(a,s=0.2,maxn=72):
    # t.seth(-45)
    # sum = 0
    for i in range(maxn):
        if 0 <= i < maxn/4 or maxn/2 <= i < maxn*3 / 4:  # 控制a的变化
            a = a + s
            t.lt(360/maxn)  # 向左转3度
            t.fd(a)  # 向前走a的步长
        else:
            a = a - s
            t.lt(360/maxn)
            t.fd(a)



# 弧形
# 长度为length，角度为extent的弧形
# 每次角度为singleExtent
def arc(length,extent,singleExtent):
    n = math.floor(extent/singleExtent)
    n = abs(n)
    singleLength = length / n
    for i in range(n):
        t.fd(singleLength)
        t.left(singleExtent)


# 绘制最外面的轮廓
# 当前状态为画笔放下，坐标原点，方向x轴正方向
# 结束状态 画笔放下，坐标远点，方向x轴正方向
def firstEdge(proportion=1):
    # 此时在坐标远点，面向x轴正方向
    # 移动到坐标原点的左下方位置的（-200p,-200p）  面向x轴正方向
    t.penup()  # 提取画笔之后进行移动，不会绘制图形
    t.backward(200 * proportion)  # 向x轴辅方向移动200p  此时状态（-200p,0） x轴正方向
    t.right(90)  # 顺时针旋转90°
    t.forward(200 * proportion)  # 向y轴负方向移动200p
    t.left(90)  # 逆时针旋转90°
    t.pendown()  # 放下画笔，移动时会绘制图形




    t.fd(25*proportion)
    # t.left(90)
    t.circle(5*proportion,90)
    # print(t.heading())
    t.fd(15*proportion)
    t.circle(-8*proportion,90)
    t.fd(5*proportion)
    t.circle(-8*proportion,90)
    t.fd(15*proportion)
    # print(t.heading())
    t.circle(5*proportion,90)
    t.fd(45*proportion)
    t.circle(8*proportion,90)
    t.fd(40*proportion)

    t.circle(-8*proportion,30)
    # t.fd(70*proportion)
    arc(90*proportion,30,10)

    t.circle(-5*proportion,45)

    arc(80*proportion,30,10)

    # print(t.heading())
    t.circle(20*proportion,90)
    t.circle(30*proportion,70)
    t.circle(10*proportion,35)
    # print(t.heading())
    t.fd(2*proportion)

    t.seth(90)

    arc(35*proportion,40,10)
    t.seth(90)
    t.fd(5*proportion)
    arc(20*proportion,10,1)

    t.seth(90)
    t.circle(20*proportion,90)
    t.circle(15*proportion,60)
    t.circle(10*proportion,30)
    # print("头右",t.heading())
    # 头顶弧
    t.seth(150)
    t.circle(100*proportion,60)
    # print(t.heading())

    t.seth(90)

    t.circle(10*proportion,30)
    t.circle(15*proportion,60)
    t.circle(20*proportion,90)

    arc(25*proportion,20,10)

    t.seth(-120)
    # print(t.heading())
    arc(80*proportion,36,10)

    t.seth(-130)

    arc(70*proportion,30,10)

    t.seth(-110)

    t.circle(10*proportion,60)
    t.fd(15*proportion)

    t.circle(10*proportion,120)
    # print(t.heading())

    t.seth(60)
    arc(25*proportion,10,10)
    t.seth(-70)
    arc(60*proportion,30,10)

    t.seth(-70)

    t.circle(-10*proportion,20)

    # print(t.pos())
    t.fd(46*proportion)

    t.seth(-90)
    t.fd(0.42*proportion)
    t.circle(10*proportion,90)
    # print(t.pos())

    t.seth(0)
    t.fd(23.3*proportion)
    print(t.pos())

    t.penup()
    t.goto(0,0)
    t.seth(0)
    t.pendown()


# 当前状态坐标原点，方向x轴正方向
# 结束状态坐标原点，方向x轴正方向
def neiEr(proportion):

    # 左内耳
    t.penup()
    t.goto(-231*proportion,49*proportion)
    t.pendown()

    t.fillcolor('black')
    t.begin_fill()
    # t.circle(10)
    print(t.pos())
    t.seth(45)
    t.fd(30*proportion)

    t.left(90)
    t.circle(13*proportion,70)
    t.circle(18*proportion,90)
    print(t.pos())
    t.seth(0)
    t.fd(2.18*proportion)
    t.seth(90)
    t.fd(0.12*proportion)
    print(t.pos())

    t.end_fill()

    t.seth(0)

    # 右内耳
    t.penup()
    t.fd(150*proportion)
    t.pendown()
    # t.circle(10)
    print(t.pos())

    t.fillcolor('black')
    t.begin_fill()
    t.seth(133)
    t.fd(30*proportion)
    t.seth(40)
    t.circle(-15*proportion,80)
    print(t.heading())
    t.circle(-16*proportion,90)
    # print(t.pos())
    t.seth(0)
    t.fd(-0.8*proportion)
    t.seth(90)
    t.fd(0.6*proportion)
    print(t.pos())

    t.end_fill()

    # 右手
    t.penup()
    t.seth(0)
    t.goto(-58*proportion,5*proportion)
    t.pendown()
    print(t.pos())
    # t.circle(10)

    t.fillcolor('black')
    t.begin_fill()

    t.seth(55)
    t.fd(20*proportion)
    t.circle(-7*proportion,90)
    print(t.heading())
    # t.circle(-10*proportion,40)
    t.seth(0)
    t.circle(-25*proportion,55)
    # arc(20*proportion,30,-5)

    print(t.heading())
    t.seth(-120)
    arc(68*proportion,20,-5)

    print(t.pos())
    t.seth(0)
    t.fd(-0.5*proportion)
    t.seth(90)
    t.fd(46.25*proportion)
    print(t.pos())

    t.end_fill()

    # 右手心
    t.penup()
    t.seth(0)
    t.goto(-37 * proportion, 10 * proportion)
    t.pendown()

    t.fillcolor('red')
    t.begin_fill()

    # t.circle(10)
    t.seth(10)
    # t.circle(-2,20)
    t.circle(-5*proportion,160)
    t.left(0)
    t.circle(-30*proportion,26)
    print("xin",t.heading())
    print(t.pos())
    # t.circle(-1,60)
    t.seth(120)
    # t.circle(-10,10)
    # t.circle(15,160)
    # arc(20*proportion,120,-3)
    t.penup()
    t.seth(0)
    t.goto(-37 * proportion, 10 * proportion)
    t.pendown()

    t.seth(100)
    # t.circle(-2,20)
    t.circle(5 * proportion, 160)
    # t.left(0)
    t.circle(30 * proportion, 25)
    print("xin", t.heading())
    # t.circle(-1,60)
    t.seth(0)
    t.fd(-0.26*proportion)
    t.seth(90)
    t.fd(-0.23*proportion)
    print(t.pos())

    t.end_fill()

    # 左手
    t.penup()
    t.goto(-265*proportion,-43*proportion)
    t.seth(0)
    t.pendown()
    # t.circle(10)

    print(t.pos())
    t.fillcolor('black')
    t.begin_fill()

    # t.circle(10)
    t.seth(-80)
    arc(40*proportion,10,-1)
    # t.fd(40*proportion)

    t.seth(-160)
    t.circle(10*proportion,80)
    # print(t.heading())
    t.seth(-120)
    t.fd(12*proportion)
    t.circle(-10*proportion,120)
    t.circle(-15*proportion,50)
    arc(56*proportion,22,-2)
    print(t.pos())
    t.seth(0)
    t.fd(-0.81*proportion)
    t.seth(90)
    t.fd(0.46*proportion)
    print(t.pos())

    t.end_fill()

    # 左脚
    t.penup()
    t.seth(0)
    t.goto(-220*proportion,-190*proportion)
    t.pendown()
    # t.circle(10)

    t.fillcolor('black')
    t.begin_fill()

    print(t.pos())
    # t.circle(10)
    t.seth(-10)
    arc(40*proportion,20,1)
    t.circle(3,90)
    t.seth(90)
    # t.fd(5*proportion)
    arc(20*proportion,20,2)
    t.seth(90)
    t.circle(5,70)
    # arc(50*proportion,40,2)
    t.fd(40*proportion)
    t.seth(-45)
    # t.fd(5*proportion)
    t.seth(-90)
    # t.fd(50*proportion)
    # arc(50*proportion,10,-2)
    t.fd(41.16*proportion)
    t.seth(0)
    t.fd(1.76*proportion)
    # print(t.pos())
    # t.seth(0)
    # t.fd(0.86*proportion)
    # t.seth(90)
    # t.fd(0.25*proportion)
    print(t.pos())
    t.end_fill()

    # 右脚
    t.penup()
    t.seth(0)
    t.goto(-140*proportion,-195*proportion)
    t.pendown()
    print(t.pos())
    t.fillcolor('black')
    t.begin_fill()
    # t.circle(10)
    t.seth(5)
    t.fd(27*proportion)
    t.circle(10,80)
    t.fd(33*proportion)
    t.seth(-150)
    t.fd(46*proportion)
    t.seth(-90)
    t.fd(21.32*proportion)
    t.seth(0)
    t.fd(0.97*proportion)
    print(t.pos())
    t.end_fill()

    t.penup()
    t.seth(0)
    t.goto(0,0)
    t.pendown()





def face(proportion):

    # 鼻子
    t.penup()
    # t.goto(-146*proportion,-18*proportion)
    t.goto(-145 * proportion, -18 * proportion)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    # t.circle(10)
    print(t.pos())
    t.fd(3*proportion)
    t.circle(5*proportion,180)
    t.fd(7*proportion)
    t.circle(5*proportion,180)
    t.fd(4*proportion)
    print(t.pos())
    t.end_fill()

    # 嘴
    t.penup()
    t.seth(0)
    # t.goto(-160*proportion,-23*proportion)
    t.goto(-160 * proportion, -23 * proportion)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()

    print(t.pos())
    # t.circle(10)
    t.seth(-25)
    t.circle(40*proportion,40)
    # t.circle(40*proportion,-40)
    # t.circle(30*proportion,-40)
    # arc(-20*proportion,60,-4)
    t.seth(-130)
    t.circle(-17*proportion,107)
    t.seth(0)
    t.fd(0.02*proportion)
    t.seth(90)
    t.fd(0.72*proportion)
    print(t.pos())
    t.end_fill()

    # 左眼外
    t.penup()
    t.seth(0)
    t.goto(-215*proportion,-37*proportion)
    t.pendown()
    t.seth(-45)

    t.fillcolor('black')
    t.begin_fill()
    ellipse(1)
    t.end_fill()

    # 左眼

    t.penup()
    # t.seth(0)
    # t.fd(30*proportion)
    # t.seth(90)
    # t.fd(30*proportion)
    t.goto(-180*proportion,-17*proportion)
    t.pendown()
    t.seth(0)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(13 * proportion)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.goto(-180*proportion,-15*proportion)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.seth(-90)

    t.penup()
    t.seth(90)
    t.fd(7*proportion)
    t.pendown()
    t.seth(0)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(4*proportion)
    t.end_fill()
    t.penup()
    t.seth(90)
    t.fd(8 * proportion)
    t.pendown()
    t.seth(0)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(2*proportion)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.goto(-215*proportion,-37*proportion)
    t.pendown()
    # t.circle(10)
    # t.seth(-45)
    # t.circle(-20*proportion,70)
    # t.circle(-100*proportion,20)

    # t.circle(10)
    t.seth(-45)
    print("zuo",t.pos())


    # 右眼外
    t.penup()
    t.seth(0)
    t.goto(-85 * proportion, -37 * proportion)
    t.pendown()
    t.seth(35)
    t.fillcolor('black')
    t.begin_fill()
    ellipse(0.7)
    t.end_fill()

    # 右眼

    t.penup()
    t.seth(0)
    t.goto(-110 * proportion, -15 * proportion)
    t.pendown()

    t.fillcolor('white')
    t.begin_fill()
    t.circle(13 * proportion)
    t.end_fill()

    t.penup()
    t.seth(90)
    t.fd(2*proportion)
    t.seth(0)
    t.pendown()

    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.seth(-90)
    t.penup()
    t.fd(2)
    t.pendown()
    t.seth(0)

    t.penup()
    t.seth(90)

    t.fd(9 * proportion)
    t.pendown()
    t.seth(0)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(4 * proportion)
    t.end_fill()

    t.penup()
    t.seth(90)
    t.fd(8 * proportion)
    t.pendown()
    t.seth(0)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(2 * proportion)
    t.end_fill()



    t.penup()
    t.seth(0)
    t.goto(0,0)
    t.pendown()


def zi(proportion):

    t.penup()
    t.seth(0)
    t.goto(-185*proportion,-126*proportion)
    t.pendown()

    # B
    t.seth(90)
    t.fd(9*proportion)
    t.seth(0)
    t.circle(-2*proportion,180)
    t.seth(0)
    # t.fd(3*proportion)
    # t.seth(-90)
    t.circle(-3*proportion,180)

    # E
    t.seth(0)
    t.penup()
    t.fd(10*proportion)
    t.pendown()

    t.fd(-4*proportion)
    t.seth(90)
    t.fd(4*proportion)
    t.seth(0)
    t.fd(3*proportion)
    t.fd(-3*proportion)
    t.seth(90)
    t.fd(5*proportion)
    t.seth(0)
    t.fd(4*proportion)

    # I
    t.penup()
    t.fd(2*proportion)
    t.pendown()
    t.seth(-90)
    t.fd(10*proportion)

    # J
    t.penup()
    t.seth(0)
    t.fd(2*proportion)
    t.seth(90)
    t.fd(2 * proportion)
    t.seth(0)
    t.pendown()

    t.seth(-90)
    t.fd(1*proportion)
    t.seth(0)

    t.fd(2*proportion)
    t.seth(90)
    t.fd(10*proportion)

    # I
    t.penup()
    t.seth(0)
    t.fd(2*proportion)
    t.seth(-90)
    t.fd(1*proportion)
    t.pendown()

    t.seth(-90)
    t.fd(10*proportion)

    # N
    t.penup()
    t.seth(0)
    t.fd(2*proportion)
    t.seth(90)
    t.fd(1*proportion)
    t.pendown()

    t.seth(90)
    t.fd(9*proportion)
    t.seth(-60)
    t.fd(10*proportion)
    t.seth(90)
    t.fd(10*proportion)

    # G
    t.penup()
    t.seth(0)
    t.fd(8*proportion)
    t.seth(-90)
    t.fd(1*proportion)
    t.pendown()

    t.seth(180)
    t.fd(3*proportion)
    t.left(45)
    t.fd(4*proportion)
    t.left(45)
    t.fd(4*proportion)
    t.left(45)
    t.fd(3*proportion)
    t.left(45)
    t.fd(5*proportion)
    t.seth(90)
    t.fd(3*proportion)
    t.seth(180)
    t.fd(2*proportion)

    # 2
    t.penup()
    t.seth(0)
    t.fd(11*proportion)
    t.seth(90)
    t.fd(4*proportion)
    t.pendown()

    print("2",t.pos())

    numTwo(proportion)

    # 0
    t.penup()
    t.seth(0)
    t.fd(5*proportion)
    t.pendown()

    # print(t.pos())
    # t.fd(2*proportion)
    # t.left(45)
    # t.fd(4*proportion)
    # t.left(45)
    # t.fd(3*proportion)
    # t.left(45)
    # t.fd(4*proportion)
    # t.seth(180)
    # t.fd(2*proportion)
    # t.left(45)
    # t.fd(4*proportion)
    # # t.left(*proportion)
    # t.left(45)
    # t.fd(4*proportion)
    # t.seth(0)
    # t.fd(2*proportion)
    # print(t.pos())

    t.circle(4)

    # 2
    t.penup()
    t.seth(0)
    t.fd(6*proportion)
    t.seth(90)
    t.fd(7*proportion)
    # t.goto(-110*proportion,-119.61*proportion)
    t.pendown()

    numTwo(proportion)

    # 2

    t.penup()
    t.seth(0)
    t.fd(3 * proportion)
    t.seth(90)
    t.fd(7 * proportion)
    # t.goto(-102 * proportion, -119.61 * proportion)
    t.pendown()

    numTwo(proportion)

    # 五环
    t.penup()
    t.seth(0)
    # t.goto(-160*proportion,-160*proportion)
    t.fd(-50*proportion)
    t.seth(90)
    t.fd(-25*proportion)
    t.seth(0)
    t.pendown()
    t.pencolor("blue")
    t.circle(10*proportion)

    t.penup()
    t.seth(0)
    t.fd(20*proportion)
    t.pendown()
    t.pencolor("black")
    t.circle(10*proportion)

    t.penup()
    t.seth(0)
    t.fd(20 * proportion)
    t.pendown()
    t.pencolor("red")
    t.circle(10 * proportion)

    t.penup()
    t.seth(0)
    t.fd(-30 * proportion)
    t.seth(90)
    t.fd(-10*proportion)
    t.seth(0)
    t.pendown()
    t.pencolor("yellow")
    t.circle(10 * proportion)

    t.penup()
    t.seth(0)
    t.fd(20 * proportion)
    t.pendown()
    t.pencolor("green")
    t.circle(10 * proportion)

    t.penup()
    t.seth(0)
    t.goto(0,0)
    t.pendown()

    t.pencolor('black')




def faceCircle(proportion):

    t.penup()

    t.pendown()

    # ellipse(1,0.1,120)
    # t.seth(90)
    # t.fd(-5)
    # t.seth(0)
    # ellipse(1,0.2,120)
    # for i in range(30):
    #     ellipse(2,i/100,120)

    t.penup()
    t.seth(0)
    t.goto(-255*proportion,-23*proportion)
    t.pendown()
    t.seth(-90)
    t.fillcolor('blue')
    t.begin_fill()
    ellipse(3, 0.11, 120)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.fd(3 * proportion)
    t.pendown()
    t.seth(-90)
    t.fillcolor('yellow')
    t.begin_fill()
    ellipse(3, 0.1, 120)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.fd(3 * proportion)
    t.pendown()
    t.seth(-90)
    t.fillcolor('red')
    t.begin_fill()
    ellipse(3, 0.09, 120)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.goto(-73*proportion,-20*proportion)
    t.pendown()
    # t.circle(10)
    t.seth(90)
    # t.circle(100*proportion)
    t.fillcolor((1,192/255,203/255))  # 粉红色
    t.begin_fill()
    ellipse(3,0.08,120)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.fd(-2*proportion)
    t.pendown()
    t.seth(90)
    t.fillcolor((0,0,128/255))  # 深蓝色
    t.begin_fill()
    ellipse(3,0.07,120)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.fd(-2 * proportion)
    t.pendown()
    t.seth(90)
    t.fillcolor('white')  #
    t.begin_fill()
    ellipse(3, 0.06, 120)
    t.end_fill()

    t.penup()
    t.seth(0)
    t.goto(0,0)
    t.pendown()



# 绘制冰墩墩的主函数
# penSize画笔宽度
# penSpeed 画笔速度
# proportion 冰墩墩比例大小，默认值为1
def main(penSize=1,penSpeed=3,proportion=1):


    t.pensize(penSize)  # 设置画笔的宽度
    t.speed(penSpeed)  # 设置画笔的速度
    t.hideturtle()  # 隐藏海龟图形
    firstEdge(proportion)
    neiEr(proportion)
    faceCircle(proportion)
    face(proportion)
    zi(proportion)
    t.done()

if __name__ == '__main__':
    main(1,10)

