'''
import pygame
import random

def game():
    
    pygame.init()
    
    #Монитор
    monitor = pygame.display.set_mode((400,500))
    pygame.display.set_caption("Snake")
    pygame.display.set_icon(pygame.image.load("assets/snake.png"))

    #color
    black = (0,0,0)
    red = (255,0,0)
    white = (255,255,255)
    green = (0, 255, 0)
    yellow = (238,255,27)

    #black line to divided monitor
    head_line_start = (0,100)
    head_line_end = (400,100)

    #Food: apple and banana
    apple = (random.randint(1, monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
    apple_spawn = True
    
    banana = (random.randint(1, monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
    banana_spawn = True

    kiwi = (random.randint(1, monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
    kiwi_spawn = True

    score = 0
    speed = 1
    level = ['easy','normal','hard','very hard', 'impossible', 'impossible x2', 'death']
    score_font = pygame.font.SysFont('lunchtime Double So',32)


    #direction of snake
    change = 'left'
    direction = 'left'

    #start
    player = [220, 200]
    snake = [[220, 200], [230, 200], [240, 200]]

    #FPS
    clock = pygame.time.Clock()
    
    # for timer kiwi-fruit
    pygame.time.set_timer(pygame.USEREVENT, 8000)
    kiwi_timer = True

    check = True

    while check:
        for action in pygame.event.get():
        #Exit
            if action.type == pygame.QUIT:
                check = False
                #pygame.quit()
            elif action.type == pygame.USEREVENT:
                kiwi_timer = not kiwi_timer
    
            
            #Keyboard
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_UP:
                    change = 'up'
                if action.key == pygame.K_DOWN:
                    change = 'down'
                if action.key == pygame.K_LEFT:
                    change = 'left'
                if action.key == pygame.K_RIGHT:
                    change = 'right'
            
        #Direction of snake 
        if direction != 'up' and change == 'down':
            direction = 'down'
        if direction != 'down' and change == 'up':
            direction = 'up'
        if direction != 'left' and change == 'right':
            direction = 'right'
        if direction != 'right' and change == 'left':
            direction = 'left'
        
        #Speed of snake (0 - x, 1 - y cordinates)
        if direction == 'up':
            player[1] -= 10
        if direction == 'down':
            player[1] += 10 
        if direction == 'left':
            player[0] -= 10 
        if direction == 'right':
            player[0] += 10  
        
        
        #Apple spawn (random) if apple generated in otherside, so this apple delete
        while apple_spawn:
            apple = (random.randint(1,monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
            if apple not in snake:
                apple_spawn = False

        while banana_spawn:
            banana = (random.randint(1,monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
            if banana not in snake:
                banana_spawn = False

        while kiwi_spawn:
                kiwi = (random.randint(1,monitor.get_width() / 10 - 1) * 10, random.randint(10, monitor.get_height() / 10 - 1) * 10)
                if kiwi not in snake:
                    kiwi_spawn = False

                
        snake.insert(0, list(player))
        
        #Обновления монитора, без этой команды змея будет увеличиваться если не будет направления, а при изменения направления размер змеи возвращается на исходный размер
        monitor.fill((142,236,123))

        if kiwi_timer:
            #Прорисовка kiwi
            pygame.draw.rect(monitor, (51,154,31), pygame.Rect(kiwi[0], kiwi[1], 10, 10))
    
        #Eat apple or banana and change score (Когда кординаты пикселей совпадают, то это засчитывается за съедение яблока) 
        if (player[0] == apple[0] and player[1] == apple[1]) or (player[0] == banana[0] and player[1] == banana[1]) or (player[0] == kiwi[0] and player[1] == kiwi[1]):
            speed = score // 4 + 1
            if player[0] == apple[0] and player[1] == apple[1]:
                score += 1
                apple_spawn = True 
            elif player[0] == banana[0] and player[1] == banana[1]:
                score += 2
                banana_spawn = True
            elif player[0] == kiwi[0] and player[1] == kiwi[1]:
                score += 1
                kiwi_spawn = True
        else:
            snake.pop()
        
        
        #line
        pygame.draw.line(monitor, black, head_line_start, head_line_end, 1)
        
        #Границы
        if ((player[0] < -5 or player[0] > monitor.get_width() - 5) or (player[1] < 100 or player[1] > monitor.get_height() - 5)):
            break
        
        #We can`t eat our body`
        if player in snake[1:]:
            break
         
        #Прорисовка объектов, к примеру это змея
        for pos in snake:
            pygame.draw.rect(monitor, black, pygame.Rect(pos[0], pos[1], 10, 10))
        
        #Прорисовка яблока
        pygame.draw.rect(monitor, red, pygame.Rect(apple[0], apple[1], 10, 10))
        #Прорисовка банана
        pygame.draw.rect(monitor, yellow, pygame.Rect(banana[0], banana[1], 10, 10))

        
        #Show score and level (level up if score +4) Мы заполняем правый верний угол информацией о текущей игре
        monitor.blit(score_font.render(f'Score: {score}' , True, black) , (20,38))
        #Текущий уровень игры
        if speed <= 7:
            monitor.blit(score_font.render(f'Speed: {level [speed - 1]}', True, black), (20,58))
        else:
            monitor.blit(score_font.render(f'Speed: death', True, black), (20,58))
        
        pygame.display.update()
        #Чтобы не нагружать систему, мы увеличиваем частоту обновления кадров с увелечения скорости
        clock.tick(10 + speed * 2)
    
    #restart or quit(После проигрыша игра не закрывается, а предлагает повторить попытку, либо просто выйти)
    while check:
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                check = False
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_r:
                    game()
                if action.key == pygame.K_q:
                    check = False
        monitor.fill(white)
        
        monitor.blit(score_font.render('Press R for restart or Q for quit' , True, black), (35,200))

        pygame.display.update()
game()
pygame.quit()
'''