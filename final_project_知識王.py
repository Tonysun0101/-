import pygame
import random
import pygame.freetype
import time

path = "C://Users//Admin//Desktop//PBC_Final_Project//-//圖片聲音字型//"     # 把字體、圖片、音樂放置的資料夾路徑放在這裡

pygame.init()                               # 畫面初始化
pygame.mixer.init()                         # 聲音初始化
ck = pygame.display.set_mode((800,600))     # 遊戲視窗大小

pygame.display.set_caption("選擇遊戲")      # 遊戲視窗的名稱

clock = pygame.time.Clock()                 # 時鐘套件
start_ck = pygame.Surface(ck.get_size())    # get_size()取得視窗尺寸，並建立一個畫布
start_ck2 = pygame.Surface(ck.get_size())   # 充當第一關的畫布介面暫時佔位(可以理解為遊戲開始了)
start_ck = start_ck.convert()               # convert()建立副本，加快畫布在視窗顯示速度
start_ck2 = start_ck2.convert()
start_ck.fill((255,255,255))                # 白色畫布1(開始介面用的)
start_ck2.fill((255,255,255))               # 白色畫布2(第一關遊戲介面用的)

# 載入所需的素材字型圖片顏色等等，並幫他們命名
start_font = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 100)         # 設定開始介面的統一字型，給他一個名稱
start_font_1 = start_font.render("進入遊戲", True, (0, 0, 255), (0, 255, 0))    # 給三個選項各兩種顏色
start_font_11 = start_font.render("進入遊戲", True, (0,255,255),(0,255,0))      # (滑鼠游標放上去和沒放上去的兩種顏色)
start_font_2 = start_font.render("結束遊戲", True, (0,0,255),(0,255,0))
start_font_21 = start_font.render("結束遊戲", True, (0,255,255),(0,255,0))
start_font_3 = start_font.render("遊戲說明", True, (0,0,255),(0,255,0))
start_font_31 = start_font.render("遊戲說明", True, (0,255,255),(0,255,0))

player_font = pygame.font.Font(None, 50)                                    # 玩家按Shift搶答後顏色的改變
player1 = player_font.render("player1", True, (0,0,255),(0,255,0))          # 一樣分成兩種顏色
player11 = player_font.render("player1", True, (0,255,255),(0,255,0))       # 先幫這兩種顏色取變數名稱
player2 = player_font.render("player2", True, (0,0,255),(0,255,0))          # 1、2代表還沒按
player21 = player_font.render("player2", True, (0,255,255),(0,255,0))       # 11、21代表已經按了

sub_font = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 50)        # 遊戲選單游標在上面與否的顏色
sub1 = sub_font.render("運動", True, (0,0,255),(0,255,0))
sub11 = sub_font.render("運動", True, (0,255,255),(0,255,0))
sub2 = sub_font.render("英文", True, (0,0,255),(0,255,0))
sub21 = sub_font.render("英文", True, (0,255,255),(0,255,0))
sub3 = sub_font.render("地理", True, (0,0,255),(0,255,0))
sub31 = sub_font.render("地理", True, (0,255,255),(0,255,0))
sub4 = sub_font.render("影視", True, (0,0,255),(0,255,0))
sub41 = sub_font.render("影視", True, (0,255,255),(0,255,0))
sub5 = sub_font.render("國學", True, (0,0,255),(0,255,0))
sub51 = sub_font.render("國學", True, (0,255,255),(0,255,0))
sub6 = sub_font.render("隨機", True, (0,0,255),(0,255,0))
sub61 = sub_font.render("隨機", True, (0,255,255),(0,255,0))

introduction_font = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 20)
ok_1 = sub_font.render("OK", True, (0,0,255),(0,255,0))
ok_2 = sub_font.render("OK", True, (0,255,255),(0,255,0))


bg = pygame.image.load(path + '貓貓.jpg')     # 整個遊戲的背景
bg.convert()

# 音效部分
pygame.mixer.music.load(path + "超級比一比.wav")  # 背景音樂

correct_sound = pygame.mixer.Sound(path + "答對音效.ogg")  # 答對音效
correct_sound.set_volume(0.2)
wrong_sound = pygame.mixer.Sound(path + "答錯音效.ogg")  # 錯誤音效
wrong_sound.set_volume(0.2)


# 題庫部分
ques1_list = list() # 題目list
ans1_list = list()  # 答案雙層list 總共5項 前4個是選項 最後一個是數字代表正確答案是哪個選項
ques2_list = list() # 題目list
ans2_list = list()  # 答案雙層list
ques3_list = list() # 題目list
ans3_list = list()  # 答案雙層list
ques4_list = list() # 題目list
ans4_list = list()  # 答案雙層list
ques5_list = list() # 題目list
ans5_list = list()  # 答案雙層list
ques6_list = list() # 題目list
ans6_list = list()  # 答案雙層list

sub_question1 = open(path + "運動題目.txt", 'r', encoding = 'utf-8')        # 把題庫們打開
sub_answer1 = open(path + "運動答案.txt", 'r', encoding = 'utf-8')
sub_question2 = open(path + "英文主題題目.txt", 'r', encoding = 'utf-8')
sub_answer2 = open(path + "英文主題答案.txt", 'r', encoding = 'utf-8')
sub_question3 = open(path + "地理題目.txt", 'r', encoding = 'utf-8')
sub_answer3 = open(path + "地理答案.txt", 'r', encoding = 'utf-8')
sub_question4 = open(path + "影視題目.txt", 'r', encoding = 'utf-8')
sub_answer4 = open(path + "影視答案.txt", 'r', encoding = 'utf-8')
sub_question5 = open(path + "國學題目.txt", 'r', encoding = 'utf-8')
sub_answer5 = open(path + "國學答案.txt", 'r', encoding = 'utf-8')
sub_question6 = open(path + "隨機題目.txt", 'r', encoding = 'utf-8')
sub_answer6 = open(path + "隨機答案.txt", 'r', encoding = 'utf-8')

for a_ques1 in sub_question1:           # 把題庫們裝進清單裡面
    a_ques1 = a_ques1.strip("\n")
    ques1_list.append(a_ques1)
for a_ans1 in sub_answer1:              # 答案部分則是用雙層清單，正確的選項是第五個
    a_ans1 = a_ans1.strip("\n")
    a_ans_list1 = a_ans1.split(";")
    ans1_list.append(a_ans_list1)

for a_ques2 in sub_question2:
    a_ques2 = a_ques2.strip("\n")
    ques2_list.append(a_ques2)
for a_ans2 in sub_answer2:
    a_ans2 = a_ans2.strip("\n")
    a_ans_list2 = a_ans2.split(";")
    ans2_list.append(a_ans_list2)

for a_ques3 in sub_question3:
    a_ques3 = a_ques3.strip("\n")
    ques3_list.append(a_ques3)
for a_ans3 in sub_answer3:
    a_ans3 = a_ans3.strip("\n")
    a_ans_list3 = a_ans3.split(";")
    ans3_list.append(a_ans_list3)
    
for a_ques4 in sub_question4:
    a_ques4 = a_ques4.strip("\n")
    ques4_list.append(a_ques4)
for a_ans4 in sub_answer4:
    a_ans4 = a_ans4.strip("\n")
    a_ans_list4 = a_ans4.split(";")
    ans4_list.append(a_ans_list4)
    
for a_ques5 in sub_question5:
    a_ques5 = a_ques5.strip("\n")
    ques5_list.append(a_ques5)
for a_ans5 in sub_answer5:
    a_ans5 = a_ans5.strip("\n")
    a_ans_list5 = a_ans5.split(";")
    ans5_list.append(a_ans_list5)
    
for a_ques6 in sub_question6:
    a_ques6 = a_ques6.strip("\n")
    ques6_list.append(a_ques6)
for a_ans6 in sub_answer6:
    a_ans6 = a_ans6.strip("\n")
    a_ans_list6 = a_ans6.split(";")
    ans6_list.append(a_ans_list6)

font1 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
introduction_font = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 20)

def word_wrap(surf, text, font1, color=(255, 255, 255)):
    font1.origin = True
    words = text
    width, height = (600,500)
    line_spacing = font1.get_sized_height() + 2
    x, y = 200, 50
    space = font1.get_rect(' ')
    for word in words:
        bounds = font1.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 200, y + line_spacing
        if x + bounds.width + bounds.x >= width:
            raise ValueError("word too wide for the surface")
        if y + bounds.height - bounds.y >= height:
            raise ValueError("text to long for the surface")
        font1.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return x, y


# 選擇我要開始?結束?還是遊戲說明
def start_function():
    start_run = True
    introduction = False
    while start_run:
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()    # buttons定義為滑鼠按下去的變數名稱
        x1, y1 = pygame.mouse.get_pos()         # 滑鼠游標目前的座標
        start_ck.blit(bg, (0,0))
        if x1 >= 200 and x1 <= 600 and y1 >= 100 and y1 <=250:      # 滑鼠移動到哪個選項，哪個選項就要發光
            start_ck.blit(start_font_11, (200, 100))
            start_ck.blit(start_font_2, (200, 250))
            start_ck.blit(start_font_3, (200, 400))
            if buttons[0]:              # 在開始遊戲選項點選滑鼠左鍵
                start_run = False       # 遊戲起始畫面結束，跳到選擇哪個遊戲介面

        elif x1 >= 200 and x1 <= 600 and y1 >= 250 and y1 <=400:
            start_ck.blit(start_font_21, (200, 250))
            start_ck.blit(start_font_1, (200, 100))
            start_ck.blit(start_font_3, (200, 400))
            if buttons[0]:          # 在退出遊戲選項點選滑鼠左鍵
                pygame.quit()       # 我要退出遊戲，整個pygame關閉
                exit()

        elif x1 >= 200 and x1 <= 600 and y1 >= 400 and y1 <=550:    # 遊戲說明畫面
            start_ck.blit(start_font_31, (200, 400))
            start_ck.blit(start_font_1, (200, 100))
            start_ck.blit(start_font_2, (200, 250))
            if buttons[0]:              # 在開始遊戲選項點選滑鼠左鍵
                start_run = False       # 遊戲起始畫面結束
                introduction = True     # 等等要進行遊戲介紹
                print("嗨嗨")
                break
        else:
            start_ck.blit(start_font_1, (200, 100))         # 什麼都不做，則起始畫面每個選項顏色不變
            start_ck.blit(start_font_2, (200, 250))
            start_ck.blit(start_font_3, (200, 400))

        ck.blit(start_ck,(0,0))
        pygame.display.update()

        for event in pygame.event.get():        # 如果直接點選畫面右上角的關閉按紐，則pygame直接結束
            if event.type == pygame.QUIT:       # 和點選"退出遊戲"有一樣的效果
                print("遊戲退出...")
                pygame.quit()
                exit()
start_function()


###
font1 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 20)
def intro_function():
    intro_run = True
    while intro_run:
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()    # buttons定義為滑鼠按下去的變數名稱
        x1, y1 = pygame.mouse.get_pos()         # 滑鼠游標目前的座標
        start_ck.blit(bg, (0,0))
        
        if x1 >= 200 and x1 <= 600 and y1 >= 100 and y1 <=250:      # 滑鼠移動到哪個選項，哪個選項就要發光
            start_ck.blit(start_font_11, (200, 100))
            start_ck.blit(start_font_2, (200, 250))
            if buttons[0]:              # 在開始遊戲選項點選滑鼠左鍵
                intro_run = False       # 遊戲起始畫面結束，跳到選擇哪個遊戲介面

        elif x1 >= 200 and x1 <= 600 and y1 >= 250 and y1 <=400:
            start_ck.blit(start_font_21, (200, 250))
            start_ck.blit(start_font_1, (200, 100))
            if buttons[0]:          # 在退出遊戲選項點選滑鼠左鍵
                pygame.quit()       # 我要退出遊戲，整個pygame關閉
                exit()
        
        else:
            start_ck.blit(start_font_1, (200, 100))         # 什麼都不做，則起始畫面每個選項顏色不變
            start_ck.blit(start_font_2, (200, 250))
        # print("嗨嗨")
        word_wrap(start_ck,"我跟你說啦哈哈哈治療上硬度置１並長輩幹你娘",font1)
        
        ck.blit(start_ck,(0,0))
        pygame.display.update()

        for event in pygame.event.get():        # 如果直接點選畫面右上角的關閉按紐，則pygame直接結束
            if event.type == pygame.QUIT:       # 和點選"退出遊戲"有一樣的效果
                print("遊戲退出...")
                pygame.quit()
                exit()
intro_function()



def choice_function():
    choice_run = True
    global ques_list
    global ans_list
    
    while choice_run:
        clock.tick(30)
        ck.blit(start_ck2, (0, 0))
        buttons = pygame.mouse.get_pressed()    # buttons定義為滑鼠按下去的變數名稱
        x1, y1 = pygame.mouse.get_pos()         # 滑鼠游標目前的座標
        start_ck2.blit(bg, (0,0))
        if x1 >= 250 and x1 <= 350 and y1 >= 100 and y1 <= 150:     # 我要玩第一個主題，把滑鼠放在第一個選項上面
            start_ck2.blit(sub11,(250,100))
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                # back = False
                ques_list = ques1_list  # 激活主題1題庫
                ans_list = ans1_list    # 激活主題1解答
        elif x1 >= 400 and x1 <= 500 and y1 >= 100 and y1 <= 150:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub21,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                # back = False
                ques_list = ques2_list  # 激活主題2題庫
                ans_list = ans2_list    # 激活主題2解答
        elif x1 >= 250 and x1 <= 350 and y1 >= 200 and y1 <= 250:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub31,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                # back = False
                ques_list = ques3_list  # 激活主題3題庫
                ans_list = ans3_list    # 激活主題3解答
        elif x1 >= 400 and x1 <= 500 and y1 >= 200 and y1 <= 250:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub41,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                # back = False
                ques_list = ques4_list  # 激活主題4題庫
                ans_list = ans4_list    # 激活主題4解答
        elif x1 >= 250 and x1 <= 350 and y1 >= 300 and y1 <= 350:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub51,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                # back = False
                ques_list = ques5_list  # 激活主題5題庫
                ans_list = ans5_list   # 激活主題5解答
        elif x1 >= 400 and x1 <= 500 and y1 >= 300 and y1 <= 350:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub61,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                # back = False
                ques_list = ques6_list  # 激活主題6題庫
                ans_list = ans6_list  # 激活主題6解答
        else:
            start_ck2.blit(sub1,(250,100))      # 什麼都不做，則選擇畫面每個選項顏色不變
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            
        pygame.display.update()
        for event in pygame.event.get():                # 判斷事件
            if event.type == pygame.KEYDOWN:            # 鍵盤事件
                if event.key == pygame.K_BACKSPACE:     # 可以回到目錄
                    choice_run = False
                    # start_function()                    # 回到起始畫面
                    # back = True
            elif event.type == pygame.QUIT:
                print("遊戲退出...")
                pygame.quit()
                exit()

ck.blit(start_ck2,(0,0))
pygame.display.update()
pygame.display.set_caption("選擇題目")
choice_function()

select = random.sample(range(0,len(ques_list)-1), 10)
# print(select)

# if back is True:
    # pygame.display.set_caption("選擇遊戲")
    # n1 = True
    # while n1:
        # clock.tick(30)
        # print(111)
        # buttons = pygame.mouse.get_pressed()
        # x1, y1 = pygame.mouse.get_pos()
        # start_ck.blit(bg, (0,0))
        # if x1 >= 200 and x1 <= 600 and y1 >= 100 and y1 <=250:
            # start_ck.blit(start_font_11, (200, 100))
            # start_ck.blit(start_font_2, (200, 250))
            # start_ck.blit(start_font_3, (200, 400))
            # if buttons[0]:
                # print(22)
                # back = False
                # n1 = False

        # elif x1 >= 200 and x1 <= 600 and y1 >= 250 and y1 <=400:
            # start_ck.blit(start_font_21, (200, 250))
            # start_ck.blit(start_font_1, (200, 100))
            # start_ck.blit(start_font_3, (200, 400))
            # if buttons[0]:
                # pygame.quit()
                # exit()

        # elif x1 >= 200 and x1 <= 700 and y1 >= 400 and y1 <=550:
            # start_ck.blit(start_font_31, (200, 400))
            # start_ck.blit(start_font_1, (200, 100))
            # start_ck.blit(start_font_2, (200, 250))
        # else:
            # start_ck.blit(start_font_1, (200, 100))
            # start_ck.blit(start_font_2, (200, 250))
            # start_ck.blit(start_font_3, (200, 400))


        # ck.blit(start_ck,(0,0))
        # pygame.display.update()


        # 下面是监听退出动作

        # 监听事件
        # for event in pygame.event.get():

            # 判断事件类型是否是退出事件
            # if event.type == pygame.QUIT:
                # print("遊戲退出...")

                # quit 卸载所有的模块
                # pygame.quit()

                # exit() 直接终止当前正在执行的程序
                # exit()


    # ck.blit(start_ck2,(0,0))
    # pygame.display.update()


# print(ques_list)
pygame.display.set_caption("知識王")



# def timer_wrap(surf, text, font1, color=(255, 255, 255)):
    # font1.origin = True
    # words = text
    # width, height = (600,500)
    # line_spacing = font1.get_sized_height() + 2
    # x, y = 400, 350
    # space = font1.get_rect(' ')
    # for word in words:
        # bounds = font1.get_rect(word)
        # if x + bounds.width + bounds.x >= width:
            # x, y = 200, y + line_spacing
        # if x + bounds.width + bounds.x >= width:
            # raise ValueError("word too wide for the surface")
        # if y + bounds.height - bounds.y >= height:
            # raise ValueError("text to long for the surface")
        # font1.render_to(surf, (x, y), None, color)
        # x += bounds.width + space.width
    # return x, y

# clock = pg.time.Clock()
# timer = 10
# dt = 0

font1 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)

def main(): 
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 32) 
    clock = pygame.time.Clock() 
    # blue = pygame.Color('dodgerblue')
    # font = pygame.font.Font(None, 50)
    # timer = 10
    # txt = font.render(str(round(timer, 2)), True, blue)
    # screen.blit(txt, (225, 10))
    # pygame.display.flip()
 
    done = False 
    init_score1 = 0
    init_score2 = 0
    correct_ans = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 50)
    correct_ans = correct_ans.render("correct", True, (0,0,255),(0,255,0))
    wrong_ans = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 50)
    wrong_ans = wrong_ans.render("wrong", True, (0,0,255),(0,255,0))
    correct = 0
    ans_turn = 0
    shift_avail = True
    init_number = 0
    word_color_a = (255,255,255)
    word_color_b = (255,255,255)
    word_color_c = (255,255,255)
    word_color_d = (255,255,255)
    result = ""
    pygame.mixer.music.play(-1)
    while not done:
        ques_ans_number = select[init_number]  # 第一題 list中的第一項
        current_question = ques_list[ques_ans_number]
        answer_option = ans_list[ques_ans_number]
        correct_answer = ans_list[ques_ans_number][4]
        
        # print(current_question)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True 

            if event.type == pygame.KEYDOWN:
                # print("keydown")
                if shift_avail == True:
                    if event.key == pygame.K_LSHIFT:
                        ans_turn = 1  
                        shift_avail = False
                        pygame.mixer.music.pause()
                        # print("leftt")
                    if event.key == pygame.K_RSHIFT:
                        ans_turn = 2  
                        shift_avail = False
                        pygame.mixer.music.pause()

                if event.key == pygame.K_a:
                    answer = answer_option[0]   # 按a代表選了第0個選項
                    word_color_a = (255,0,0)
                    word_color_b = (255,255,255)
                    word_color_c = (255,255,255)
                    word_color_d = (255,255,255)
                    if answer == correct_answer:
                        if ans_turn == 1:       # 輪到一號回答，且回答正確，一號加分!
                            init_score1 += 2
                        elif ans_turn == 2:     # 輪到二號回答，且回答正確，二號加分!
                            init_score2 += 2
                        ans_turn = 0
                        correct = 1
                        correct_sound.play()
                    else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2        # 一號答錯了，失去此輪回答機會，換二號回答
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1        # 二號答錯了，失去此輪回答機會，換一號回答
                        correct = 2
                        wrong_sound.play()
                elif event.key == pygame.K_b:
                    answer = answer_option[1]
                    word_color_a = (255,255,255)
                    word_color_b = (255,0,0)
                    word_color_c = (255,255,255)
                    word_color_d = (255,255,255)
                    if answer == correct_answer:
                        if ans_turn == 1:
                            init_score1 += 2
                        elif ans_turn == 2:
                            init_score2 += 2
                        ans_turn = 0
                        correct = 1
                        correct_sound.play()
                    else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1
                        correct = 2
                        wrong_sound.play()
                elif event.key == pygame.K_c:
                    answer = answer_option[2]
                    word_color_a = (255,255,255)
                    word_color_b = (255,255,255)
                    word_color_c = (255,0,0)
                    word_color_d = (255,255,255)
                    if answer == correct_answer:
                        if ans_turn == 1:
                            init_score1 += 2
                        elif ans_turn == 2:
                            init_score2 += 2
                        ans_turn = 0
                        correct = 1
                        correct_sound.play()
                    else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1
                        correct = 2
                        wrong_sound.play()
                elif event.key == pygame.K_d:
                    answer = answer_option[3]
                    word_color_a = (255,255,255)
                    word_color_b = (255,255,255)
                    word_color_c = (255,255,255)
                    word_color_d = (255,0,0)
                    if answer == correct_answer:
                        if ans_turn == 1:
                            init_score1 += 2
                        elif ans_turn == 2:
                            init_score2 += 2
                        ans_turn = 0
                        correct = 1
                        correct_sound.play()
                    else:
                        if ans_turn == 1:
                            init_score1 -= 1
                            ans_turn = 2
                        elif ans_turn == 2:
                            init_score2 -= 1
                            ans_turn = 1
                        correct = 2
                        wrong_sound.play()
                elif event.key == pygame.K_RETURN:
                    pygame.mixer.music.unpause()
                    word_color_a = (255,255,255)
                    word_color_b = (255,255,255)
                    word_color_c = (255,255,255)
                    word_color_d = (255,255,255)
                    ans_turn = 0
                    shift_avail = True
                    
                    if init_number == len(select) - 1:
                        if init_score1 > init_score2:
                            result = "P1 win"
                        elif init_score1 == init_score2:
                            result = "Tie"
                        elif init_score1 < init_score2:
                            result = "P2 win"
                    if init_number < len(select) - 1:
                        if type(init_number) != int:  # 一開始先不秀題目 按了enter後開始
                            init_number = 0
                        else:
                            init_number += 1# 跳下一個題目跟解答
                    else:
                        pass
                    correct = 0
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True
        screen.blit(bg, (0,0))
        # print(question)
        # print(type(question))
        score1 = pygame.font.Font(None, 50)
        score1 = score1.render(str(init_score1), (0,0,255),(0,255,0))
        score2 = pygame.font.Font(None, 50)
        score2 = score2.render(str(init_score2), (0,0,255),(0,255,0))
        word_wrap(screen, ques_list[select[init_number]], font1)
        
        # global timer
        # timer = "10"
        # timer_wrap(screen, timer, font1)
        
        # print(answer_option)
        option_a = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
        option_a = option_a.render(str("(A)" + " " + answer_option[0]), (255,255,255),word_color_a)
        option_b = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
        option_b = option_b.render(str("(B)" + " " + answer_option[1]), (255,255,255),word_color_b)
        option_c = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
        option_c = option_c.render(str("(C)" + " " + answer_option[2]), (255,255,255),word_color_c)
        option_d = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
        option_d = option_d.render(str("(D)" + " " + answer_option[3]), (255,255,255),word_color_d)



        if correct == 1:
            screen.blit(correct_ans, (350, 300))
        elif correct == 2:
            screen.blit(wrong_ans, (350,300))
            
        if type(ques_ans_number) == int:
            screen.blit(option_a, (100,400))
            screen.blit(option_b, (400,400))
            screen.blit(option_c, (100,500))
            screen.blit(option_d, (400,500))
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

        if init_number == len(select) - 1:
            final_result = pygame.font.Font(None, 100)
            final_result = final_result.render(result, (0,0,255),(0,255,0))
            screen.blit(final_result, (325,300))
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__': 
    pygame.init() 
    main() 
    pygame.quit()