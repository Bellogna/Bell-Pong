import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 64)
game_started = False
winner = ""
message_font = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)

left_paddle = pygame.Rect(20, 255, 15, 90)
right_paddle = pygame.Rect(765, 255, 15, 90)
ball = pygame.Rect(393, 293, 15, 15)
ball_speed_x = 5
ball_speed_y = 5
left_score = 0
right_score = 0
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not game_started:
            left_score = 0
            right_score = 0
            winner = ""
            ball.center = (400, 300)
            game_started = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= 7
    if keys[pygame.K_s] and left_paddle.bottom < 600:
        left_paddle.y += 7
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= 7
    if keys[pygame.K_DOWN] and right_paddle.bottom < 600:
        right_paddle.y += 7
    if left_score >= 5:
        winner = "Left Player Wins!"
        game_started = False
    if right_score >= 5:
        winner = "Right Player Wins!"
        game_started = False
    if game_started:
        ball.x += ball_speed_x
        ball.y += ball_speed_y
    if ball.top <=0 or ball.bottom >= 600:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
            ball_speed_x = -ball_speed_x
    if ball.left <= 0:
        right_score += 1
        ball.center = (400, 300)
        ball_speed_x = -ball_speed_x
    if ball.right >= 800:
        left_score += 1
        ball.center = (400, 300)
        ball_speed_x = -ball_speed_x

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (200, 20))
    screen.blit(right_text, (600, 20))
    if not game_started and winner == "":
        start_text = message_font.render("Press ENTER to start", True, WHITE)
        screen.blit(start_text, (265, 280))
    if winner != "":
        win_text = font.render(winner, True, WHITE)
        screen.blit(win_text, win_text.get_rect(center=(425, 260)))
        again_text = message_font.render("Press ENTER to play again", True, WHITE)
        screen.blit(again_text, (265, 320))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
