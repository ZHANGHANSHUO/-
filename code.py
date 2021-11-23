import copy
import random
import pygame


snake_list = [[10, 10]]



x = random.randint(10, 490)
y = random.randint(10, 490)
food_point = [x, y]


move_up = False
move_down = False
move_left = False
move_right = True



pygame.init()

screen = pygame.display.set_mode((500, 500))

title = pygame.display.set_caption('식탐 뱀 게임')
 
clock = pygame.time.Clock()
while True:
    
    clock.tick(20)
    
    screen.fill([255, 255, 255])

   
    
    for event in pygame.event.get():
       
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_DOWN:
                move_up = False
                move_down = True
                move_left = False
                move_right = False
            if event.key == pygame.K_UP:
                move_up = True
                move_down = False
                move_left = False
                move_right = False
            if event.key == pygame.K_LEFT:
                move_up = False
                move_down = False
                move_left = True
                move_right = False
            if event.key == pygame.K_RIGHT:
                move_up = False
                move_down = False
                move_left = False
                move_right = True

    
    snake_len = len(snake_list) - 1
    while snake_len > 0:
        snake_list[snake_len] = copy.deepcopy(snake_list[snake_len - 1])
        snake_len -= 1
    
    if move_up:
        snake_list[snake_len][1] -= 10
        if snake_list[snake_len][1] < 0:
            snake_list[snake_len][1] = 500

    if move_down:
        snake_list[snake_len][1] += 10
        if snake_list[snake_len][1] > 500:
            snake_list[snake_len][1] = 0

    if move_left:
        snake_list[snake_len][0] -= 10
        if snake_list[snake_len][0] < 0:
            snake_list[snake_len][0] = 500

    if move_right:
        snake_list[snake_len][0] += 10
        if snake_list[snake_len][0] > 500:
            snake_list[snake_len][0] = 0
    
    food_rect = pygame.draw.circle(screen, [255, 0, 0], food_point, 15)
    
    snake_rect = []
    for snake_pos in snake_list:
        snake_rect.append(pygame.draw.circle(screen, [255, 0, 0], snake_pos, 5))
       
        if food_rect.collidepoint(snake_pos):
            snake_list.append(food_point)
            
            food_point = [random.randint(10, 490), random.randint(10, 490)]
            break
    
    snake_head_rect = snake_rect[0]
    count = len(snake_rect)
    while count > 1:
        
        if snake_head_rect.colliderect(snake_rect[count - 1]):
            print('탐식뱀은 자기만 먹고 게임을 끝냅니다.')
            pygame.quit()
        count -= 1
   
    pygame.display.update()
