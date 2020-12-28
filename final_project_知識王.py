import pygame
import random
import pygame.freetype
import time
import datetime

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
start_font_11 = start_font.render("進入遊戲", True, (0,255,255),(0,255,0))      # 滑鼠游標放上去和沒放上去的兩種顏色
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

info_start1 = sub_font.render("遊戲開始", True, (0,0,255),(0,255,0))
info_start11 = sub_font.render("遊戲開始", True, (0,255,255),(0,255,0))
info_start2 = sub_font.render("離開遊戲", True, (0,0,255),(0,255,0))
info_start21 = sub_font.render("離開遊戲", True, (0,255,255),(0,255,0))

bg = pygame.image.load(path + 'brain.png')     # 整個遊戲的背景
bg.convert()

bg1 = pygame.image.load(path + '運動.jpg')          # 每個主題都會有不同背景
bg2 = pygame.image.load(path + '英文.jpg')
bg3 = pygame.image.load(path + '地理.jpg')
bg4 = pygame.image.load(path + '影視.jpg')
bg5 = pygame.image.load(path + '國學.jpg')
bg6 = pygame.image.load(path + '隨機.png')

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

font1 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)   # 把字體叫出來
def word_wrap(surf, text, font1, color=(255, 255, 255)):                # 題目如何呈現在畫面上
    font1.origin = True
    words = text
    width, height = (600,500)
    line_spacing = font1.get_sized_height() + 2
    x, y = 200, 100
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

def word_wrap1(surf, text, font1, color=(255, 255, 255)):   # 遊戲說明如何呈現在畫面上(字型大小和上面word_wrap不一樣，所以分開列)
    font1.origin = True
    words = text
    width, height = (600,500)
    line_spacing = font1.get_sized_height() + 2
    x, y = 200, 150
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
    global introduction
    start_run = True
    introduction = False
    
    while start_run:
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()    # buttons定義為滑鼠按下去的變數名稱
        x1, y1 = pygame.mouse.get_pos()         # 滑鼠游標目前的座標
        start_ck.blit(bg, (0,0))
        if x1 >= 200 and x1 <= 600 and y1 >= 100 and y1 <=250:      # 滑鼠移動到哪個選項(座標位置)，哪個選項就要發光
            start_ck.blit(start_font_11, (200, 100))
            start_ck.blit(start_font_2, (200, 250))
            start_ck.blit(start_font_3, (200, 400))
            if buttons[0]:              # 在開始遊戲選項點選滑鼠左鍵
                start_run = False       # 遊戲起始畫面結束，跳到選擇哪個遊戲的介面
                introduction = False    # 沒有要遊戲說明，因此跳過這個環節

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
                break
        else:
            start_ck.blit(start_font_1, (200, 100))         # 什麼都不做，則起始畫面每個選項顏色不變
            start_ck.blit(start_font_2, (200, 250))
            start_ck.blit(start_font_3, (200, 400))

        ck.blit(start_ck,(0,0))
        pygame.display.update()     # 刷新畫面

        for event in pygame.event.get():        # 如果直接點選畫面右上角的關閉按紐，則pygame直接結束
            if event.type == pygame.QUIT:       # 和點選"退出遊戲"有一樣的效果
                print("遊戲退出...")
                pygame.quit()
                exit()
start_function()            # 把start_function()叫出來，開始第一個畫面

font1 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 15)
def intro_function():       # 遊戲說明畫面
    intro_run = True
    if not introduction:    # 如果剛剛有點選遊戲說明，才需要這個環節
        intro_run = False
    while intro_run:
        clock.tick(30)
        buttons = pygame.mouse.get_pressed()    # buttons定義為滑鼠按下去的變數名稱
        x1, y1 = pygame.mouse.get_pos()         # 滑鼠游標目前的座標
        start_ck.blit(bg, (0,0))

        if x1 >= 100 and x1 <= 300 and y1 >= 50 and y1 <= 100:      # 滑鼠移動到哪個選項，哪個選項就要發光
            start_ck.blit(info_start11, (100, 50))
            start_ck.blit(info_start2, (500, 50))
            if buttons[0]:              # 在開始遊戲選項點選滑鼠左鍵
                intro_run = False       # 遊戲起始畫面結束，跳到選擇哪個遊戲的介面

        elif x1 >= 500 and x1 <= 700 and y1 >= 50 and y1 <= 100:
            start_ck.blit(info_start21, (500, 50))
            start_ck.blit(info_start1, (100, 50))
            if buttons[0]:          # 在退出遊戲選項點選滑鼠左鍵
                pygame.quit()       # 我要退出遊戲，整個pygame關閉
                exit()
        
        else:
            start_ck.blit(info_start1, (100, 50))         # 什麼都不做，則起始畫面每個選項顏色不變
            start_ck.blit(info_start2, (500, 50))
        word_wrap1(start_ck,"按'遊戲開始'後， 點選滑鼠'右鍵'來選擇要玩哪個主題， 遊戲開始後兩個玩家進行搶答， 一號玩家按左邊的Shift按鍵搶答， 二號玩家按右邊的Shift按鍵搶答， 第一個按下Shift按鍵的玩家便可獲得這次回答機會， 按下鍵盤上的A、B、C、D按鍵來回答， 答錯的話就換另一個玩家回答， 不需按Shift按鍵， 一樣按下鍵盤上的A、B、C、D按鍵來回答。\
                           每次回答時間都只有三秒， 超過時間就換對方回答， 答對一個選項加兩分， 答錯一個選項扣一分， 按下'Enter'按鍵來換下一題， 總共會進行十個題目， 遊戲結束後分數高者獲勝。",font1)
        
        ck.blit(start_ck,(0,0))     # 把word_wrap1()叫出來，並把說明文字丟進去，最後會呈現在遊戲說明畫面上
        pygame.display.update()     # 刷新畫面
        pygame.display.set_caption("遊戲介紹")

        for event in pygame.event.get():        # 如果直接點選畫面右上角的關閉按紐，則pygame直接結束
            if event.type == pygame.QUIT:       # 和點選"退出遊戲"有一樣的效果
                print("遊戲退出...")
                pygame.quit()
                exit()
intro_function()            # 把介紹畫面叫出來，當然，如果introduction == False，就會跳過這個步驟

def choice_function():      # 選擇要玩哪個主題
    choice_run = True
    global ques_list
    global ans_list
    global bg
    
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
                ques_list = ques1_list  # 激活主題1題庫
                ans_list = ans1_list    # 激活主題1解答
                bg = bg1                # 套用第一個主題的背景
        elif x1 >= 400 and x1 <= 500 and y1 >= 100 and y1 <= 150:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub21,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                ques_list = ques2_list  # 激活主題2題庫
                ans_list = ans2_list    # 激活主題2解答
                bg = bg2                # 套用第二個主題的背景
        elif x1 >= 250 and x1 <= 350 and y1 >= 200 and y1 <= 250:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub31,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                ques_list = ques3_list  # 激活主題3題庫
                ans_list = ans3_list    # 激活主題3解答
                bg = bg3                # 套用第三個主題的背景
        elif x1 >= 400 and x1 <= 500 and y1 >= 200 and y1 <= 250:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub41,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                ques_list = ques4_list  # 激活主題4題庫
                ans_list = ans4_list    # 激活主題4解答
                bg = bg4                # 套用第四個主題的背景
        elif x1 >= 250 and x1 <= 350 and y1 >= 300 and y1 <= 350:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub51,(250,300))
            start_ck2.blit(sub6,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                ques_list = ques5_list  # 激活主題5題庫
                ans_list = ans5_list    # 激活主題5解答
                bg = bg5                # 套用第五個主題的背景
        elif x1 >= 400 and x1 <= 500 and y1 >= 300 and y1 <= 350:
            start_ck2.blit(sub1,(250,100)) 
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub61,(400,300))
            if buttons[2]:              # 並且還滑鼠點選了他
                choice_run = False      # 選擇頁面結束，跳到遊戲介面
                ques_list = ques6_list  # 激活主題6題庫
                ans_list = ans6_list    # 激活主題6解答
                bg = bg6                # 套用第六個主題的背景
        else:
            start_ck2.blit(sub1,(250,100))      # 什麼都不做，則選擇畫面每個選項顏色不變
            start_ck2.blit(sub2,(400,100))
            start_ck2.blit(sub3,(250,200))
            start_ck2.blit(sub4,(400,200))
            start_ck2.blit(sub5,(250,300))
            start_ck2.blit(sub6,(400,300))
        
        ck.blit(start_ck2,(0,0))
        pygame.display.set_caption("選擇題目")
        pygame.display.update()
        for event in pygame.event.get():        # 判斷事件
            if event.type == pygame.QUIT:       # 如果直接點選畫面右上角的關閉按紐，則pygame直接結束
                print("遊戲退出...")
                pygame.quit()
                exit()
choice_function()


font2 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 15)
def timer_wrap(surf, text, font2, color=(255, 255, 255)):   # 計時器字型格式
    font2.origin = True
    words = text
    width, height = (600,500)
    line_spacing = font2.get_sized_height() + 2
    x, y = 250, 50
    space = font2.get_rect(' ')
    for word in words:
        bounds = font2.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 250, y + line_spacing
        if x + bounds.width + bounds.x >= width:
            raise ValueError("word too wide for the surface")
        if y + bounds.height - bounds.y >= height:
            raise ValueError("text to long for the surface")
        font2.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return x, y


pygame.display.set_caption("知識王")   # 遊戲頁面名稱
font0 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
font2 = pygame.freetype.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
select = random.sample(range(0,len(ques_list)-1), 10)

def main():     # 主要遊戲開始了!
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 32) 
    clock = pygame.time.Clock()
    
    init_score1 = 0     # 一開始分數都是零分
    init_score2 = 0
    init_number = 0     # 隨機清單裡面的第一個數字
    correct = 0         # 一開始還沒有人答對
    ans_turn = 0        # 一開始還沒有任何人回答
    
    correct_ans = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 50)     # 答對該選項後，該選項要亮起來
    correct_ans = correct_ans.render("correct", True, (0,0,255),(0,255,0))
    wrong_ans = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 50)       # 答錯該選項後，該選項要亮起來
    wrong_ans = wrong_ans.render("wrong", True, (0,0,255),(0,255,0))
    
    shift_avail = True      # 一開始可以按Shift來搶答
    done = False            # 迴圈還沒結束
    
    word_color_a = (255,255,255)    # 設定所有選項的預設顏色
    word_color_b = (255,255,255)
    word_color_c = (255,255,255)
    word_color_d = (255,255,255)
    result = ""
    pygame.mixer.music.play(-1)
    
    time_run = True     # 計時器還在倒數
    change = False      # 還沒換人回答(時間到了或者是有人回答了，就得換人回答)
    times_up = False    # 時間還沒到
    first = True        # 這是這個題目第一次被回答
    
    while not done:     # 開始跑一個無限回圈
        ques_ans_number = select[init_number]               # 在隨機清單裡面選第一個數字
        current_question = ques_list[ques_ans_number]       # 這個數字就是我們這回題目的編號，把這個隨機題目叫出來
        answer_option = ans_list[ques_ans_number]           # 答案也是一樣的道理
        correct_answer = ans_list[ques_ans_number][4]       # 正確答案會是答案清單裡面的第五項，把它放進變數裡面
        
        blit_timer = False      # 計時器沒有運作
        
        if shift_avail == False and time_run == True and first == True:     # 按下Shift了，開始計時，而這是這個題目第一次被計時
            d_now = time.time()         # 記下當下時間
            differ = d_now - d_shift    # 把當下時間減去按下shift瞬間的時間，得出自從搶答後已經過了多少秒數
            # print(3 - differ)           # 用3-differ就是我要的計時器
            blit_timer = True           # 計時器運作了!

        if ans_turn == 1 and differ > 5 and time_run == True:       # 如果秒數大於三，代表這個玩家回答太久了
            ans_turn = 2                # 換成二號回答
            first = False               # 這不是第一次計時了
            d_shift = time.time()       # 計下換人回答當下的時間
            times_up = True             # 計下有人沒在時間內回答
        elif ans_turn == 2 and differ > 5 and time_run == True:     # 如果秒數大於三，代表這個玩家回答太久了
            ans_turn = 1                # 換成一號回答
            first = False               # 這不是第一次計時了
            d_shift = time.time()       # 計下換人回答當下的時間
            times_up = True             # 計下有人沒在時間內回答
        
        if times_up == True or change == True:      # 有人沒在時間內回答，或是有人回答了，都要換人，並重新計時
            d_now = time.time()                     # 記下當下時間
            differ = d_now - d_shift                # 和換人當下的秒數相減，就可以得出新的計時器
            # print(3 - differ)
            blit_timer = True                       # 計時器正在運作
        
        for event in pygame.event.get():    # 判斷玩家做了哪些動作
            
            if event.type == pygame.QUIT:   # 直接關掉視窗，迴圈結束
                done = True
            

            if event.type == pygame.KEYDOWN:    # 鍵盤事件
                if shift_avail == True:         # 如果可以搶答
                    if event.key == pygame.K_LSHIFT:    # 如果一號玩家按下Shift搶答了
                        ans_turn = 1                    # 這輪是一號玩家的局
                        shift_avail = False             # 這個題目不能搶答了，必須輪流在時間內回答
                        pygame.mixer.music.pause()      # 緊張的音樂停止
                        
                        d_shift = time.time()           # 記下搶答瞬間當下的時間
                        time_run = True                 # 時間正在跑
                        
                    if event.key == pygame.K_RSHIFT:    # 如果二號玩家按下Shift搶答了
                        ans_turn = 2                    # 這輪是二號玩家的局
                        shift_avail = False             # 這個題目不能搶答了，必須輪流在時間內回答
                        pygame.mixer.music.pause()      # 緊張的音樂停止
                        
                        d_shift = time.time()           # 記下搶答瞬間當下的時間
                        time_run = True                 # 時間正在跑

                if event.key == pygame.K_a and shift_avail == False:    # 如果玩家按了shift，並且選擇了a當答案
                    change = True                   # 等等要換人回答
                    d_shift = time.time()           # 記下選答案瞬間的時間
                    answer = answer_option[0]       # 按a代表選了第0個選項
                    word_color_a = (255,0,0)        # 選項a要亮起來(這裡先記下他們的顏色就好，後面才會blit)
                    word_color_b = (255,255,255)
                    word_color_c = (255,255,255)
                    word_color_d = (255,255,255)
                    
                    if answer == correct_answer:    # 如果回答正確
                        time_run = False            # 計時器停止運作
                        times_up = False            # 沒有人超時回答
                        change = False              # 因為回答正確，所以不用進行換人，而是進入下一輪搶答環節
                        if ans_turn == 1:           # 如果是一號回答正確，一號加分!
                            init_score1 += 2        # 加兩分
                        elif ans_turn == 2:         # 如果是二號回答正確，二號加分!
                            init_score2 += 2        # 加兩分
                        ans_turn = 0                # 回到沒有人回答的情況，因為等等要搶答
                        correct = 1                 # 記下"有人回答正確"這件事情
                        correct_sound.play()        # 播放回答正確的音樂
                    else:
                        if ans_turn == 1:           # 一號回答錯了，扣一分
                            init_score1 -= 1
                            ans_turn = 2            # 一號答錯了，失去此輪回答機會，換二號回答
                        elif ans_turn == 2:         # 二號回答錯了，扣一分
                            init_score2 -= 1
                            ans_turn = 1            # 二號答錯了，失去此輪回答機會，換一號回答
                        correct = 2                 # 用correct = 2，記下"有人回答錯誤"這件事情
                        wrong_sound.play()          # 撥放回答錯誤的音效
                
                elif event.key == pygame.K_b and shift_avail == False:  # 如果玩家按了shift，並且選擇了b當答案
                    change = True
                    d_shift = time.time()
                    answer = answer_option[1]
                    word_color_a = (255,255,255)
                    word_color_b = (255,0,0)
                    word_color_c = (255,255,255)
                    word_color_d = (255,255,255)
                    if answer == correct_answer:
                        time_run = False
                        times_up = False
                        change = False
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
                
                elif event.key == pygame.K_c and shift_avail == False:  # 如果玩家按了shift，並且選擇了c當答案
                    change = True
                    d_shift = time.time()
                    answer = answer_option[2]
                    word_color_a = (255,255,255)
                    word_color_b = (255,255,255)
                    word_color_c = (255,0,0)
                    word_color_d = (255,255,255)
                    if answer == correct_answer:
                        time_run = False
                        times_up = False
                        change = False
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
                
                elif event.key == pygame.K_d and shift_avail == False:  # 如果玩家按了shift，並且選擇了d當答案
                    change = True
                    d_shift = time.time()
                    answer = answer_option[3]
                    word_color_a = (255,255,255)
                    word_color_b = (255,255,255)
                    word_color_c = (255,255,255)
                    word_color_d = (255,0,0)
                    if answer == correct_answer:
                        time_run = False
                        times_up = False
                        change = False
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
                
                elif event.key == pygame.K_RETURN:  # 如果有人按下enter鍵盤
                    change = False                  # 沒有換人的動作
                    time_run = False                # 計時器停止運作
                    times_up = False                # 沒有人超時回答
                    first = True                    # 下一題第一次被啟動
                    pygame.mixer.music.unpause()    # 音樂不要停，接著播
                    word_color_a = (255,255,255)    # 沒有選項是亮著的
                    word_color_b = (255,255,255)
                    word_color_c = (255,255,255)
                    word_color_d = (255,255,255)
                    ans_turn = 0                    # 一開始沒有人回答
                    correct = 0                     # 一開始沒有人回答正確
                    shift_avail = True              # 開放搶答
                    
                    if init_number == len(select) - 1:      # 代表已經玩了十個題目了
                        pygame.mixer.music.pause()          # 緊張的音樂停止
                        shift_avail = False
                        if init_score1 > init_score2:       # 顯示哪個玩家贏了
                            result = "P1 win"
                        elif init_score1 == init_score2:
                            result = "Tie"
                        elif init_score1 < init_score2:
                            result = "P2 win"
                    if init_number < len(select) - 1:       # 如果還沒玩十題
                        if type(init_number) != int:        # 一開始先不秀題目，按了enter後開始
                            init_number = 0
                        else:
                            init_number += 1                # 跳下一個隨機題目跟解答
                    
                else:
                    if event.type == pygame.KEYDOWN:        # 按esc鍵盤可以退出遊戲
                        if event.key == pygame.K_ESCAPE:
                            done = True
        
        screen.blit(bg, (0,0))  # 背景
        score1 = pygame.font.Font(None, 50)                             # 一號玩家分數字型
        score1 = score1.render(str(init_score1), (0,0,255),(0,255,0))   # 一號玩家分數顏色
        score2 = pygame.font.Font(None, 50)                             # 二號玩家分數字型
        score2 = score2.render(str(init_score2), (0,0,255),(0,255,0))   # 二號玩家分數顏色
        
        word_wrap(screen, ques_list[select[init_number]], font0)        # 題目顯示
        if blit_timer == True:                                          # 計時器顯示，前提是blit_timer == True
            timer_wrap(screen, str(round(5 - differ, 3)), font2)
        
        option_a = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)                            # 答案們的字型以及顏色
        option_a = option_a.render(str("(A)" + " " + answer_option[0]), (255,255,255),word_color_a)     # 除了ABCD，還要套入題庫中的答案
        option_b = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
        option_b = option_b.render(str("(B)" + " " + answer_option[1]), (255,255,255),word_color_b)
        option_c = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
        option_c = option_c.render(str("(C)" + " " + answer_option[2]), (255,255,255),word_color_c)
        option_d = pygame.font.Font(path + "NotoSansMonoCJKtc-Bold.otf", 32)
        option_d = option_d.render(str("(D)" + " " + answer_option[3]), (255,255,255),word_color_d)

        if correct == 1:                            # 如果這輪有人回答正確
            screen.blit(correct_ans, (450, 0))    # blit correct_ans(也就是correct)
        elif correct == 2:                          # 如果這輪有人回答錯誤
            screen.blit(wrong_ans, (450,0))       # blit wrong_ans(也就是wrong)
            
        if type(ques_ans_number) == int:        # 讓所有選項blit出來
            screen.blit(option_a, (50,400))
            screen.blit(option_b, (400,400))
            screen.blit(option_c, (50,500))
            screen.blit(option_d, (400,500))
        screen.blit(score1, (80,60))            # 讓分數列表blit出來
        screen.blit(score2, (700,60))
        if ans_turn == 0:                       # 如果這輪還沒有人回答，則玩家名稱不亮
            screen.blit(player1, (30, 20))
            screen.blit(player2, (650, 20))
        elif ans_turn == 1:
            screen.blit(player11, (30, 20))     # 如果這輪一號回答，則一號玩家名稱亮起
            screen.blit(player2, (650, 20))
        elif ans_turn == 2:
            screen.blit(player1, (30, 20))      # 如果這輪二號回答，則二號玩家名稱亮起
            screen.blit(player21, (650, 20))

        if init_number == len(select) - 1:                                      # 玩十個題目了
            final_result = pygame.font.Font(None, 100)                          # 遊戲最終結果的字型顏色
            final_result = final_result.render(result, (0,0,255),(0,255,0))
            screen.blit(final_result, (325,300))
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__': 
    pygame.init() 
    main() 
    pygame.quit()