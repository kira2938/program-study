import pygame

# 初期化
pygame.init()

# 画面作成
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# イメージ呼び出し
player = pygame.image.load("resources/images/dude.png")
# 背景画像呼び出し
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

keys = [False, False, False, False]
playerpos = [100, 100]

# ずっと表示
while True:
    # 画面を綺麗にする
    screen.fill((0, 0, 0))  # (R, G, B)

    # 全ての要素を再び描く
    for x in range(width//grass.get_width() + 1):
        for y in range(height//grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    screen.blit(player, playerpos)

    # 画面を再び描く
    pygame.display.flip()

    # ゲームを終了する
    for event in pygame.event.get():
        # 閉じるボタンを押したら
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            elif event.key == pygame.K_a:
                keys[1] = True
            elif event.key == pygame.K_s:
                keys[2] = True
            elif event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False

    if keys[0]:
        playerpos[1] = playerpos[1] - 5
    elif keys[2]:
        playerpos[1] = playerpos[1] + 5
    elif keys[1]:
        playerpos[0] = playerpos[0] - 5
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5

# キーボードでイメージを動かす
# マウスでイメージを開店させる
# 弓を発射
# 敵が来る
# 弓と敵が衝突
# 残り時間とHPの表示
# 条件による結果
# ミュージック、音
