import pygame
pygame.init()
pygame.mixer.init()
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

# 音效部分
# background_music = pygame.mixer.music()  # 背景音樂

# correct_sound = pygame.mixer.sound()  # 答對音效
# correct_sound.set_volume(0.2)
# wrong_sound = pygame.mixer.sound()  # 錯誤音效
# wrong_sound.mixer.sound(0.2)
bird_sound = pygame.mixer.Sound("C:/Users/USER/Downloads/音效.ogg")
bird_sound.set_volume(0.2)

# 題庫部分
ques1_list = list()  # 題目list
ans1_list = list()  # 答案雙層list 總共5項 前4個是選項 最後一個是數字代表正確答案是哪個選項

ques2_list = list()  # 題目list
ans2_list = list()  # 答案雙層list

ques1_list = list()  # 題目list
ans1_list = list()  # 答案雙層list

ques3_list = list()  # 題目list
ans3_list = list()  # 答案雙層list

ques4_list = list()  # 題目list
ans4_list = list()  # 答案雙層list

ques5_list = list()  # 題目list
ans5_list = list()  # 答案雙層list

ques6_list = list()  # 題目list
ans6_list = list()  # 答案雙層list
#  以下为选择开始界面鼠标检测结构。
n1 = True
while n1:
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    start_ck.blit(bg, (0,0))
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
    start_ck2.blit(bg, (0,0))
    if x1 >= 200 and x1 <= 350 and y1 >= 100 and y1 <= 150:
        start_ck2.blit(sub11,(250,100))
        start_ck2.blit(sub2,(400,100))
        start_ck2.blit(sub3,(250,200))
        start_ck2.blit(sub4,(400,200))
        start_ck2.blit(sub5,(250,300))
        start_ck2.blit(sub6,(400,300))
        if buttons[2]:
            n2 = False
            back = False
            # ques_list = ques1_list  激活主題1題庫
            # ans_list = ans1_list  激活主題1解答
    elif x1 >= 350 and x1 <= 500 and y1 >= 100 and y1 <= 150:
        start_ck2.blit(sub1,(250,100)) 
        start_ck2.blit(sub21,(400,100))
        start_ck2.blit(sub3,(250,200))
        start_ck2.blit(sub4,(400,200))
        start_ck2.blit(sub5,(250,300))
        start_ck2.blit(sub6,(400,300))
        if buttons[2]:
            n2 = False
            back = False
            # ques_list = ques2_list  激活主題2題庫
            # ans_list = ans2_list  激活主題2解答
    elif x1 >= 200 and x1 <= 350 and y1 >= 200 and y1 <= 250:
        start_ck2.blit(sub1,(250,100)) 
        start_ck2.blit(sub2,(400,100))
        start_ck2.blit(sub31,(250,200))
        start_ck2.blit(sub4,(400,200))
        start_ck2.blit(sub5,(250,300))
        start_ck2.blit(sub6,(400,300))
        if buttons[2]:
            n2 = False
            back = False
            # ques_list = ques3_list  激活主題3題庫
            # ans_list = ans3_list  激活主題3解答
    elif x1 >= 350 and x1 <= 500 and y1 >= 200 and y1 <= 250:
        start_ck2.blit(sub1,(250,100)) 
        start_ck2.blit(sub2,(400,100))
        start_ck2.blit(sub3,(250,200))
        start_ck2.blit(sub41,(400,200))
        start_ck2.blit(sub5,(250,300))
        start_ck2.blit(sub6,(400,300))
        if buttons[2]:
            n2 = False
            back = False
            # ques_list = ques4_list  激活主題4題庫
            # ans_list = ans4_list  激活主題4解答
    elif x1 >= 200 and x1 <= 350 and y1 >= 300 and y1 <= 350:
        start_ck2.blit(sub1,(250,100)) 
        start_ck2.blit(sub2,(400,100))
        start_ck2.blit(sub3,(250,200))
        start_ck2.blit(sub4,(400,200))
        start_ck2.blit(sub51,(250,300))
        start_ck2.blit(sub6,(400,300))
        if buttons[2]:
            n2 = False
            back = False
            # ques_list = ques5_list  激活主題5題庫
            # ans_list = ans5_list  激活主題5解答
    elif x1 >= 350 and x1 <= 500 and y1 >= 300 and y1 <= 350:
        start_ck2.blit(sub1,(250,100)) 
        start_ck2.blit(sub2,(400,100))
        start_ck2.blit(sub3,(250,200))
        start_ck2.blit(sub4,(400,200))
        start_ck2.blit(sub5,(250,300))
        start_ck2.blit(sub61,(400,300))
        if buttons[2]:
            n2 = False
            back = False
            # ques_list = ques6_list  激活主題6題庫
            # ans_list = ans6_list  激活主題6解答
    else:
        start_ck2.blit(sub1,(250,100)) 
        start_ck2.blit(sub2,(400,100))
        start_ck2.blit(sub3,(250,200))
        start_ck2.blit(sub4,(400,200))
        start_ck2.blit(sub5,(250,300))
        start_ck2.blit(sub6,(400,300))
        
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
        start_ck.blit(bg, (0,0))
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


pygame.display.set_caption("知識王")
def main(): 
    screen = pygame.display.set_mode((800, 600)) 
    font = pygame.font.Font(None, 32) 
    clock = pygame.time.Clock() 
    # input_box = pygame.Rect(310, 50, 200, 32) 
    # color_inactive = pygame.Color('lightskyblue3') 
    # color_active = pygame.Color('red2') 
    # color = color_inactive 
    # active = False 
    # text = '' 
    done = False 
    init_score1 = 0
    init_score2 = 0
    correct_ans = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
    correct_ans = correct_ans.render("correct", True, (0,0,255),(0,255,0))
    wrong_ans = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 50)
    wrong_ans = wrong_ans.render("wrong", True, (0,0,255),(0,255,0))
    correct = 0
    ans_turn = 0
    shift_avail = True
    ques_ans_number = 0  # 第一題 list中的第一項
    while not done:
        # question = ques_list[ques_ans_number]
        # answer_option = ans_list[ques_ans_number]
        # correct_answer = ans_list[ques_ans_number][4]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True 

            if event.type == pygame.KEYDOWN:
                if shift_avail == True:
                    if event.key == pygame.K_LSHIFT:
                        ans_turn = 1  
                        print(ans_turn)
                        shift_avail = False
                        # background_music.stop()
                    if event.key == pygame.K_RSHIFT:
                        ans_turn = 2  
                        print(ans_turn)
                        shift_avail = False
                        # background_music.stop()

                if event.key == pygame.K_a:
                    # answer = answer_option[0]
                    # if answer == correct_answer:
                        if ans_turn == 1:
                            init_score1 += 2
                        elif ans_turn == 2:
                            init_score2 += 2
                        shift_avail = True
                        ans_turn = 0
                        correct = 1
                        # correct_sound.play()
                    # else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1
                        correct = 2
                        # wrong_sound.play()
                elif event.key == pygame.K_b:
                    # answer = answer_option[1]
                    # if answer == correct_answer:
                        if ans_turn == 1:
                            init_score1 += 2
                        elif ans_turn == 2:
                            init_score2 += 2
                        shift_avail = True
                        ans_turn = 0
                        correct = 1
                        # correct_sound.play()
                    # else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1
                        correct = 2
                        # wrong_sound.play()
                elif event.key == pygame.K_c:
                    # answer = answer_option[2]
                    # if answer == correct_answer:
                        if ans_turn == 1:
                            init_score1 += 2
                        elif ans_turn == 2:
                            init_score2 += 2
                        shift_avail = True
                        ans_turn = 0
                        correct = 1
                        # correct_sound.play()
                    # else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1
                        correct = 2
                        # wrong_sound.play()
                elif event.key == pygame.K_d:
                    # answer = answer_option[3]
                    # if answer == correct_answer:
                        if ans_turn == 1:
                            init_score1 += 2
                        elif ans_turn == 2:
                            init_score2 += 2
                        shift_avail = True
                        ans_turn = 0
                        correct = 1
                        # correct_sound.play()
                    # else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1
                        correct = 2
                        # wrong_sound.play()
                elif event.key == pygame.K_RETURN:
                    ans_turn = 0
                    # background_music.play()
                    if ques_ans_number != int:  # 一開始先不秀題目 按了enter後開始
                        ques_ans_number = 0
                    else:
                        ques_ans_number += 1# 跳下一個題目跟解答
                    correct = 0
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True

                            
        score1 = pygame.font.Font(None, 50)
        score1 = score1.render(str(init_score1), (0,0,255),(0,255,0))
        score2 = pygame.font.Font(None, 50)
        score2 = score2.render(str(init_score2), (0,0,255),(0,255,0))
        # question = pygame.font.Font("C:/python/NotoSansMonoCJKtc-Bold.otf", 32)
        # question = question.render(question, (0,0,0),(255,255,255))
        screen.fill((255, 255, 255))

        screen.blit(bg, (0,0))
        if correct == 1:
            screen.blit(correct_ans, (350, 20))
        elif correct == 2:
            screen.blit(wrong_ans, (350,20))
            
        # if ques_ans_number == int:
            # screen.blit(question, (100,100))
        screen.blit(score1, (80,60))
        screen.blit(score2, (700,60))
        if ans_turn == 0:
            screen.blit(player1, (30, 20))
            screen.blit(player2, (650, 20))
        elif ans_turn == 1:
            screen.blit(player11, (30, 20))
            screen.blit(player2, (650, 20))
        elif ans_turn == 2:
            screen.blit(player1, (30, 20))
            screen.blit(player21, (650, 20))            
        # screen.blit(txt_surface, (input_box.x+5, input_box.y+5)) 
        # Blit the input_box rect. 
        # pygame.draw.rect(screen, color, input_box, 2) 

        pygame.display.flip() 
        clock.tick(30) 


if __name__ == '__main__': 
    pygame.init() 
    main() 
    pygame.quit()