import pygame as pg
import datetime
import time

def countdown_timer(timer):
    pg.init()                                   # 建立一個視窗
    screen = pg.display.set_mode((500, 500))    # 設定視窗大小
    font = pg.font.Font(None, 50)               # 調整字體以及字型大小
    gray = pg.Color('gray19')
    blue = pg.Color('dodgerblue')               # 套入灰色和藍色套件
    screen.fill(gray)                           # 用灰色填滿視窗
    
    time_left = datetime.timedelta(seconds=timer).seconds
    done = False
    while True :
        for event in pg.event.get():            # 判斷使用者有沒有用滑鼠把視窗關掉
            if event.type == pg.QUIT:           # 如果關掉了，則停止計時
                done = True
                break
            elif event.type == pg.KEYDOWN:      # 如果觸發了鍵盤事件
                if event.key == pg.K_r:         # 如果按"r"，則時間重置
                    print("時間重置!!")
                    timer = 10
        if done:
            break
        
        txt = font.render(str(round(time_left, 2)), True, blue)     # 設定文字格式
        screen.blit(txt, (225, 10))                                 # 文字出現的位置(我把他置頂置中，文字長度50)
        pg.display.flip()                                           # 更新上述設定到螢幕上面
        
        time_left -= 1
        time.sleep(1)
        
        if time_left == 0:
            break
        print(time_left)

countdown_timer(10)  # 叫出來