import pygame
import math
import random

# 初期化
pygame.init()

# 画面作成
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerpos = [100, 100]
acc = [0, 0]
arrows = []
badtimer = 100
badtimer1 = 0
badguys = [[640, 100]]
healthvalue = 194
pygame.mixer.init()


# イメージ呼び出し
player = pygame.image.load("resources/images/dude.png")  # プレイヤー
grass = pygame.image.load("resources/images/grass.png")  # 背景
castle = pygame.image.load("resources/images/castle.png")  # 城
arrow = pygame.image.load("resources/images/bullet.png")  # 矢
badguyimg = pygame.image.load("resources/images/badguy.png")  # 敵
healthbar = pygame.image.load("resources/images/healthbar.png")  # hp bar
health = pygame.image.load("resources/images/health.png")  # hp
gameover = pygame.image.load("resources/images/gameover.png")  # gameover
youwin = pygame.image.load("resources/images/youwin.png")  # youwin




hit = pygame.mixer.Sound("resources/audio/explode.wav")
enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load("resources/audio/moonlight.wav")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


# ずっと表示
running = 1
exitcode = 0
while running:
    badtimer -= 1
    # 画面を綺麗にする
    screen.fill((0, 0, 0))  # (R, G, B)

    # 全ての要素を再び描く
    for x in range(width//grass.get_width() + 1):
        for y in range(height//grass.get_height() + 1):
            screen.blit(grass, (x * 100, y * 100))

    screen.blit(castle, (0, 30))  # 城1
    screen.blit(castle, (0, 135))  # 城2
    screen.blit(castle, (0, 240))  # 城3
    screen.blit(castle, (0, 345))  # 城4

    # プレイヤーをマウスで回転
    position = pygame.mouse.get_pos()
    angle = math.atan2(
        position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width //
                  2, playerpos[1] - playerrot.get_rect().height // 2)
    screen.blit(playerrot, playerpos1)

    # 矢の設定
    for bullet in arrows:  # 角度、プレイヤーのxとy位置
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index += 1

    for projectile in arrows:
        arrow1 = pygame.transform.rotate(arrow, 360-projectile[0] * 57.29)
        screen.blit(arrow1, (projectile[1], projectile[2]))

    # 敵の設定
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5

        index = 0
        for badguy in badguys:
            if badguy[0] < -64:
                badguys.pop(index)
            else:
                badguy[0] -= 7

            # 城を攻撃
            badrect = pygame.Rect(badguyimg.get_rect())
            badrect.top = badguy[1]
            badrect.left = badguy[0]
            if badrect.left < 64:
                hit.play()
                healthvalue -= random.randint(5, 20)
                badguys.pop(index)

            # 攻撃された敵
            index1 = 0
            for bullet in arrows:
                bullrect = pygame.Rect(arrow.get_rect())
                bullrect.left = bullet[1]
                bullrect.top = bullet[2]
                if badrect.colliderect(bullrect):
                    enemy.play()
                    acc[0] += 1
                    badguys.pop(index)
                    arrows.pop(index1)
                index1 += 1

            index += 1
        for badguy in badguys:
            screen.blit(badguyimg, badguy)

        # time
        font = pygame.font.Font(None, 24)
        survivedtext = font.render(str(int((90000 - pygame.time.get_ticks()) / 60000)) + ":" + str(
            int((90000 - pygame.time.get_ticks()) / 1000 % 60)).zfill(2), True, (0, 0, 0))
        textRect = survivedtext.get_rect()
        textRect.topright = [635, 5]
        screen.blit(survivedtext, textRect)

        # health
        screen.blit(healthbar, (5, 5))
        for health1 in range(healthvalue):
            screen.blit(health, (health1 + 8, 8))

    # 画面を再び描く
    pygame.display.flip()

    # ゲームを終了する
    for event in pygame.event.get():
        # 閉じるボタンを押したら
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # キーボード
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

        # 矢を発射
        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            acc[1] = acc[1] + 1
            arrows.append([math.atan2(position[1] - (playerpos[1] + 32), position[0] -
                                      (playerpos[0] + 26)), playerpos1[0] + 32, playerpos[1] + 32])

    # 移動範囲
    if keys[0]:
        playerpos[1] = playerpos[1] - 5
    elif keys[2]:
        playerpos[1] = playerpos[1] + 5
    elif keys[1]:
        playerpos[0] = playerpos[0] - 5
    elif keys[3]:
        playerpos[0] = playerpos[0] + 5

    # 勝ち負けチェック
    if pygame.time.get_ticks() >= 90000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0

if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(gameover, (0, 0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery + 24
    screen.blit(youwin, (0, 0))
    screen.blit(text, textRect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        pygame.display.flip()

# キーボードでイメージを動かす
# マウスでイメージを開店させる
# 矢を発射
# 敵が来る
# 弓と敵が衝突
# 残り時間とHPの表示
# 条件による結果
# ミュージック、音
