import pygame


# 1- reset
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
pacmanpos = [350, 280]


# 2- イメージを呼び出し
pacman1 = pygame.image.load("resources/images/pacman.png")
pacman2 = pygame.image.load("resources/images/pacman_c.png")


# 3- サウンド
# 4- ループして画面表示
while True:

    # 5- 画面を掃除
    screen.fill((0, 0, 0))
# 6- 全ての要素を再び呼び出し
    screen.blit(pacman, pacmanpos)
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
        pacmanpos[1] -= 0.3
    elif keys[2]:
        pacmanpos[1] += 0.3
    if keys[1]:
        pacmanpos[0] -= 0.3
    elif keys[3]:
        pacmanpos[0] += 0.3

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
