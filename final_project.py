import pygame
pygame.init()
ck = pygame.display.set_mode((800,600))   #  游戏窗口
pygame.display.set_caption("選擇遊戲")    #  给窗口取个名 我小时候喜欢双截龙和拳皇
clock = pygame.time.Clock()                         #  游戏刷新速度（我个人这么理解）
start_ck = pygame.Surface(ck.get_size())    #   充当开始界面的画布
start_ck2 = pygame.Surface(ck.get_size())  #  充当第一关的画布界面暂时占位（可以理解为游戏开始了）
start_ck = start_ck.convert()
start_ck2 = start_ck2.convert()
start_ck.fill((255,255,255))  # 白色画布1（开始界面用的）
start_ck2.fill((255,255,255))
# 加载各个素材图片 并且赋予变量名
i1 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 100)
text1 = i1.render("急速列車", True, (0,0,255),(0,255,0))
# i1 = pygame.transform.scale(i1, (200, 100))
i11 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 100)
text11 = i11.render("急速列車", True, (0,255,255),(0,255,0))

i2 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 100)
text2 = i2.render("結束遊戲", True, (0,0,255),(0,255,0))
# i1 = pygame.transform.scale(i1, (200, 100))
i21 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 100)
text21 = i21.render("結束遊戲", True, (0,255,255),(0,255,0))

i3 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 100)
text3 = i3.render("猜猜我是誰", True, (0,0,255),(0,255,0))
# i1 = pygame.transform.scale(i1, (200, 100))
i31 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 100)
text31 = i31.render("猜猜我是誰", True, (0,255,255),(0,255,0))

player1 = pygame.font.Font(None, 50)
player1 = player1.render("player1", True, (0,0,255),(0,255,0))
player11 = pygame.font.Font(None, 50)
player11 = player11.render("player1", True, (0,255,255),(0,255,0))

player2 = pygame.font.Font(None, 50)
player2 = player2.render("player2", True, (0,0,255),(0,255,0))
player21 = pygame.font.Font(None, 50)
player21 = player21.render("player2", True, (0,255,255),(0,255,0))




sub1 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub1 = sub1.render("主題1", True, (0,0,255),(0,255,0))
sub11 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub11 = sub11.render("主題1", True, (0,255,255),(0,255,0))

sub2 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub2 = sub2.render("主題2", True, (0,0,255),(0,255,0))
sub21 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub21 = sub21.render("主題2", True, (0,255,255),(0,255,0))

sub3 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub3 = sub3.render("主題3", True, (0,0,255),(0,255,0))
sub31 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub31 = sub31.render("主題3", True, (0,255,255),(0,255,0))

sub4 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub4 = sub4.render("主題4", True, (0,0,255),(0,255,0))
sub41 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub41 = sub41.render("主題4", True, (0,255,255),(0,255,0))

sub5 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub5 = sub5.render("主題5", True, (0,0,255),(0,255,0))
sub51 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub51 = sub51.render("主題5", True, (0,255,255),(0,255,0))

sub6 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub6 = sub6.render("主題6", True, (0,0,255),(0,255,0))
sub61 = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
sub61 = sub61.render("主題6", True, (0,255,255),(0,255,0))



bg = pygame.image.load('C:/python/galaxy-dark-matter.jpg')
bg.convert()


#  以下为选择开始界面鼠标检测结构。
n1 = True
while n1:
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= 200 and x1 <= 600 and y1 >= 100 and y1 <=250:
        start_ck.blit(text11, (200, 100))
        start_ck.blit(text2, (200, 250))
        start_ck.blit(text3, (200, 400))
        if buttons[0]:
            n1 = False

    elif x1 >= 200 and x1 <= 600 and y1 >= 250 and y1 <=400:
        start_ck.blit(text21, (200, 250))
        start_ck.blit(text1, (200, 100))
        start_ck.blit(text3, (200, 400))
        if buttons[0]:
            pygame.quit()
            exit()

    elif x1 >= 200 and x1 <= 700 and y1 >= 400 and y1 <=550:
        start_ck.blit(text31, (200, 400))
        start_ck.blit(text1, (200, 100))
        start_ck.blit(text2, (200, 250))
    else:
        start_ck.blit(text1, (200, 100))
        start_ck.blit(text2, (200, 250))
        start_ck.blit(text3, (200, 400))


    ck.blit(start_ck,(0,0))
    pygame.display.update()


    # 下面是监听退出动作

    # 监听事件
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有的模块
            pygame.quit()

            # exit() 直接终止当前正在执行的程序
            exit()


ck.blit(start_ck2,(0,0))
pygame.display.update()
pygame.display.set_caption("選擇題目")
#  以下可以写第一关的代码了
n2 = True
while n2:
    clock.tick(30)
    ck.blit(start_ck2, (0, 0))
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= 200 and x1 <= 350 and y1 >= 100 and y1 <= 150:
        start_ck2.blit(sub11,(200,100))
        start_ck2.blit(sub2,(350,100))
        start_ck2.blit(sub3,(200,200))
        start_ck2.blit(sub4,(350,200))
        start_ck2.blit(sub5,(200,300))
        start_ck2.blit(sub6,(350,300))
        if buttons[2]:
            n2 = False
            back = False
            # 激活主題1題庫
    elif x1 >= 350 and x1 <= 500 and y1 >= 100 and y1 <= 150:
        start_ck2.blit(sub1,(200,100)) 
        start_ck2.blit(sub21,(350,100))
        start_ck2.blit(sub3,(200,200))
        start_ck2.blit(sub4,(350,200))
        start_ck2.blit(sub5,(200,300))
        start_ck2.blit(sub6,(350,300))
        if buttons[2]:
            n2 = False
            back = False
            # 激活主題2題庫
    elif x1 >= 200 and x1 <= 350 and y1 >= 200 and y1 <= 250:
        start_ck2.blit(sub1,(200,100)) 
        start_ck2.blit(sub2,(350,100))
        start_ck2.blit(sub31,(200,200))
        start_ck2.blit(sub4,(350,200))
        start_ck2.blit(sub5,(200,300))
        start_ck2.blit(sub6,(350,300))
        if buttons[2]:
            n2 = False
            back = False
            # 激活主題3題庫
    elif x1 >= 350 and x1 <= 500 and y1 >= 200 and y1 <= 250:
        start_ck2.blit(sub1,(200,100)) 
        start_ck2.blit(sub2,(350,100))
        start_ck2.blit(sub3,(200,200))
        start_ck2.blit(sub41,(350,200))
        start_ck2.blit(sub5,(200,300))
        start_ck2.blit(sub6,(350,300))
        if buttons[2]:
            n2 = False
            back = False
            # 激活主題4題庫
    elif x1 >= 200 and x1 <= 350 and y1 >= 300 and y1 <= 350:
        start_ck2.blit(sub1,(200,100)) 
        start_ck2.blit(sub2,(350,100))
        start_ck2.blit(sub3,(200,200))
        start_ck2.blit(sub4,(350,200))
        start_ck2.blit(sub51,(200,300))
        start_ck2.blit(sub6,(350,300))
        if buttons[2]:
            n2 = False
            back = False
            # 激活主題5題庫
    elif x1 >= 350 and x1 <= 500 and y1 >= 300 and y1 <= 350:
        start_ck2.blit(sub1,(200,100)) 
        start_ck2.blit(sub2,(350,100))
        start_ck2.blit(sub3,(200,200))
        start_ck2.blit(sub4,(350,200))
        start_ck2.blit(sub5,(200,300))
        start_ck2.blit(sub61,(350,300))
        if buttons[2]:
            n2 = False
            back = False
            # 激活主題6題庫
    else:
        start_ck2.blit(sub1,(200,100)) 
        start_ck2.blit(sub2,(350,100))
        start_ck2.blit(sub3,(200,200))
        start_ck2.blit(sub4,(350,200))
        start_ck2.blit(sub5,(200,300))
        start_ck2.blit(sub6,(350,300))
        
    pygame.display.update()
    for event in pygame.event.get():

        # 判断事件类型是否是退出事件
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  # 可以回到目錄
                n2 = False
                back = True
        elif event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有的模块
            pygame.quit()

            # exit() 直接终止当前正在执行的程序
            exit()



if back is True:
    pygame.display.set_caption("選擇遊戲")
    n1 = True
    while n1:
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()
        x1, y1 = pygame.mouse.get_pos()
        if x1 >= 200 and x1 <= 600 and y1 >= 100 and y1 <=250:
            start_ck.blit(text11, (200, 100))
            start_ck.blit(text2, (200, 250))
            start_ck.blit(text3, (200, 400))
            if buttons[0]:
                n1 = False

        elif x1 >= 200 and x1 <= 600 and y1 >= 250 and y1 <=400:
            start_ck.blit(text21, (200, 250))
            start_ck.blit(text1, (200, 100))
            start_ck.blit(text3, (200, 400))
            if buttons[0]:
                pygame.quit()
                exit()

        elif x1 >= 200 and x1 <= 700 and y1 >= 400 and y1 <=550:
            start_ck.blit(text31, (200, 400))
            start_ck.blit(text1, (200, 100))
            start_ck.blit(text2, (200, 250))
        else:
            start_ck.blit(text1, (200, 100))
            start_ck.blit(text2, (200, 250))
            start_ck.blit(text3, (200, 400))


        ck.blit(start_ck,(0,0))
        pygame.display.update()


        # 下面是监听退出动作

        # 监听事件
        for event in pygame.event.get():

            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                print("游戏退出...")

                # quit 卸载所有的模块
                pygame.quit()

                # exit() 直接终止当前正在执行的程序
                exit()


    ck.blit(start_ck2,(0,0))
    pygame.display.update()


pygame.display.set_caption("急速列車")
def main(): 
    screen = pygame.display.set_mode((800, 600)) 
    font = pygame.font.Font(None, 32) 
    clock = pygame.time.Clock() 
    input_box = pygame.Rect(300, 100, 200, 32) 
    color_inactive = pygame.Color('lightskyblue3') 
    color_active = pygame.Color('dodgerblue2') 
    color = color_inactive 
    active = False 
    text = '' 
    done = False 
    count = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                done = True 
            if event.type == pygame.MOUSEBUTTONDOWN: 
                # If the user clicked on the input_box rect. 
                if input_box.collidepoint(event.pos): 
                    # Toggle the active variable. 
                    active = not active 
                else: 
                    active = False
                # Change the current color of the input box. 
                color = color_active if active else color_inactive 
            if event.type == pygame.KEYDOWN: 
                if active: 
                    if event.key == pygame.K_RETURN: 
                        print(text)
                        text = ''
                        count += 1
                    elif event.key == pygame.K_BACKSPACE: 
                        text = text[:-1]
                    else: 
                        text += event.unicode
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True


        screen.fill((255, 255, 255)) 
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long. 
        width = max(200, txt_surface.get_width()+10) 
        input_box.w = width
        # Blit the text.
        if count % 2 == 0:
            screen.blit(player11, (150, 150))
            screen.blit(player2, (550, 150))
        else:
            screen.blit(player1, (150, 150))
            screen.blit(player21, (550, 150))
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5)) 
        # Blit the input_box rect. 
        pygame.draw.rect(screen, color, input_box, 2) 

        pygame.display.flip() 
        clock.tick(30) 


if __name__ == '__main__': 
    pygame.init() 
    main() 
    pygame.quit()