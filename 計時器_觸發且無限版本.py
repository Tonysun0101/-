import pygame as pg

def main():
    pg.init()                                   # 建立一個視窗
    screen = pg.display.set_mode((500, 500))    # 設定視窗大小
    font = pg.font.Font(None, 50)               # 調整字體以及字型大小
    gray = pg.Color('gray19')
    blue = pg.Color('dodgerblue')               # 套入灰色和藍色套件

    clock = pg.time.Clock()                     # 套入時鐘套件
    timer = 10                                  # 總共倒數多少
    dt = 0                                      # 從timer-dt開始倒數

    done = False
    while not done:
        for event in pg.event.get():            # 判斷使用者有沒有用滑鼠把視窗關掉
            if event.type == pg.QUIT:           # 如果關掉了，則停止計時
                done = True
            elif event.type == pg.KEYDOWN:      # 如果觸發了鍵盤事件
                if event.key == pg.K_r:         # 如果按r，則時間重置
                    print("時間重置!!")
                    timer = 10
        
        timer -= dt
        if timer <= 0:
            timer = 10                          # 時間重置

        screen.fill(gray)                                       # 用灰色填滿視窗
        txt = font.render(str(round(timer, 2)), True, blue)     # 設定文字格式
        screen.blit(txt, (225, 10))                             # 文字出現的位置(我把他置頂置中，文字長度50)
        pg.display.flip()                                       # 更新上述設定到螢幕上面
        dt = clock.tick(10) / 1000                              # 跳轉幀數


main()  # 叫出來