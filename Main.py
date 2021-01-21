from variables import *

def bullet_handle(red, yellow, red_bullets, yellow_bullets):
    for bullets in red_bullets:
        bullets.x += BULLET_VEL
        if yellow.colliderect(bullets):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullets)

        elif bullets.x > WIDTH:
            red_bullets.remove(bullets)


    for bullets in yellow_bullets:
        bullets.x -= BULLET_VEL
        if red.colliderect(bullets):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullets)

        elif bullets.x  < 0:
            yellow_bullets.remove(bullets)


def yellowship_handler(key_pressed, yellow):

    if key_pressed[pygame.K_LEFT] and yellow.x != WIDTH/2:
        yellow.x -= VEL
    if key_pressed[pygame.K_RIGHT] and yellow.x + SPACESHIP_WIDTH - VEL != WIDTH:
        yellow.x += VEL
    if key_pressed[pygame.K_UP] and yellow.y != 0:
        yellow.y -= VEL
    if key_pressed[pygame.K_DOWN] and yellow.y + SPACESHIP_HEIGHT != HEIGHT:
        yellow.y += VEL


def redship_handler(key_pressed, red):
    
    if key_pressed[pygame.K_a] and red.x != 0:
        red.x -= VEL
    if key_pressed[pygame.K_d] and red.x + SPACESHIP_WIDTH - VEL != WIDTH/2:
        red.x += VEL
    if key_pressed[pygame.K_w] and red.y != 0:
        red.y -= VEL
    if key_pressed[pygame.K_s] and red.y + SPACESHIP_HEIGHT != HEIGHT:
        red.y += VEL


def display_draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(SPACE, (0, 0))

    red_score = SCORE_FONT.render("HEALTH: " + str(red_health), 1, WHITE)
    yellow_score = SCORE_FONT.render("HEALTH: " + str(yellow_health), 1, WHITE)

    WIN.blit(yellow_score, (WIDTH - red_score.get_width() -10, 10))
    WIN.blit(red_score, (10, 10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.draw.rect(WIN, BLACK, BORDER)


    for bullets in red_bullets:
        pygame.draw.rect(WIN, RED, bullets)

    for bullets in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullets)


    pygame.display.update()


def winner_draw(text):
    winner = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(winner, (WIDTH/2 - winner.get_width()/2, HEIGHT/2 - winner.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    run = 1
    red = pygame.Rect(300, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    while run:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0
                pygame.quit()

            if event.type == pygame.KEYDOWN and len(red_bullets) < MAX_BULLETS:

                if event.key == pygame.K_LCTRL:
                    bullets = pygame.Rect(red.x + SPACESHIP_WIDTH, red.y + SPACESHIP_HEIGHT//2, 10, 5)
                    red_bullets.append(bullets)
                    BULLET_FIRE.play()

                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullets = pygame.Rect(yellow.x, yellow.y + SPACESHIP_HEIGHT//2, 10, 5)
                    yellow_bullets.append(bullets)
                    BULLET_FIRE.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT.play()

        WINNER_TEXT = ""
        if red_health <= 0:
            WINNER_TEXT = "Yellow Wins!"
        if yellow_health <= 0:
            WINNER_TEXT = "Red Wins!"


        if WINNER_TEXT != "":
            winner_draw(WINNER_TEXT)
            break

        key_pressed = pygame.key.get_pressed()
        yellowship_handler(key_pressed, yellow)
        redship_handler(key_pressed, red)


        bullet_handle(red, yellow, red_bullets, yellow_bullets)
        display_draw(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)

        
    main()

main()