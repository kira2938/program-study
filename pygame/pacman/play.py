import pygame, random


# 1- reset
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height), 0, 32)
keys = [False, False, False, False]
pacmanpos = [350, 280]
circleCounter = 0
circles = []
for i in range(10):
    circles.append(pygame.Rect(random.randint(0, width - 10),random.randint(0, height - 10), 10, 10))

# 2- イメージを呼び出し
pacman1 = pygame.image.load("resources/images/pacman1.png")
pacman1Rect = pacman1.get_rect()
circle_s = pygame.image.load("resources/images/small_circle.png")
circleRect = circle_s.get_rect()

# 3- サウンド
# 4- ループして画面表示
while True:

    # 5- 画面を掃除
    screen.fill((0, 0, 0))
# 6- 全ての要素を再び呼び出し
    pygame.draw.rect(screen, (255, 255, 0), pacman1Rect)

    for circle in circles[:]:
        if pacman1Rect.colliderect(circle):
            circles.remove(circle)

    for i in range(len(circles)):
        pygame.draw.rect(screen, (255, 255, 255), circles[i])
    # 6-1 丸を呼び出し
    # for x in range(width // circle_s.get_width() + 1):
    #     for y in range(height // circle_s.get_height() + 1):
    #         screen.blit(circle_s, (x * 50, y * 50))
    # for x in range(15):
    #     for y in range(15):
    #         screen.blit(circle_s, (x * 50, y * 50))
    # screen.blit(circle_s, (150, 200))

    # 6-2 丸を食べる
    # index1 = 0
    # for eat in circle:
    #     pacmanrect = pygame.Rect(pacman1.get_rect())
    #     circlerect = pygame.Rect(circle_s.get_rect())
    #     circlerect.left = eat[1]
    #     circlerect.top = eat[2]
    #     if pacman1.colliderect(circlerect):
    #         acc[0] += 1
    #         circle_s.pop(index)
    #         circle.pop(index1)
    #     index1 += 1

# 7- 画面をまた表示
    pygame.display.flip()
# 8- ゲーム終了準備
    for event in pygame.event.get():
        # close button
        if event.type == pygame.QUIT:
            # close
            pygame.quit()
            exit(0)
        # keyborde event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_LEFT:
                keys[1] = True
            elif event.key == pygame.K_DOWN:
                keys[2] = True
            elif event.key == pygame.K_RIGHT:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_LEFT:
                keys[1] = False
            elif event.key == pygame.K_DOWN:
                keys[2] = False
            elif event.key == pygame.K_RIGHT:
                keys[3] = False

    if keys[0]:
        pacmanpos[1] -= 0.5
    elif keys[2]:
        pacmanpos[1] += 0.5
    if keys[1]:
        pacmanpos[0] -= 0.5
    elif keys[3]:
        pacmanpos[0] += 0.5

    pygame.display.update()
# パックマン
#    自動
#     手動
# えさ
#    全面に置く
#        全部なくなったらクリア

# モンスター
#    数
#        1
#     自動
#        パックマンを狙う

# ルール
#    全てのユニットは 壁を通過できない
#     全てのユニットは 直線だけ動く
#     モンスターはずっと動く
#     モンスターは交差点があるところで方向が
#     パックマンはモンスターに触れるとゲームオーバー


# アイテム
#    あり
#        敵が弱くなって食われる
#     なし
#        通常
