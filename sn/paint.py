"""
import pygame

# functions
def erase():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 50
    rect_height = 50
    pygame.draw.rect(screen, white, (rect_pos, (rect_width, rect_height)))

def cirlce():
    circle_pos = pygame.mouse.get_pos()
    circle_radius = 30
    pygame.draw.circle(screen, color, circle_pos, circle_radius)

def rectangle():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 30
    rect_height = 50
    pygame.draw.rect(screen, color, (rect_pos, (rect_width, rect_height)))

def square():
    sq_pos = pygame.mouse.get_pos()
    sq_lenght = 60
    pygame.draw.rect(screen, color, (sq_pos, (sq_lenght, sq_lenght)))

def equilateral_triangle():
    x, y = pygame.mouse.get_pos()
    pygame.draw.polygon(screen, color, [(x-50, y+50), (x, y), (x+50, y+50)])

def right_triangle():
    x, y = pygame.mouse.get_pos()
    pygame.draw.polygon(screen, color, [(x,y), (x+50, y), (x, y-50)])

def rhombus():
    x, y = pygame.mouse.get_pos()
    pygame.draw.polygon(screen, color, [(x-30, y+20), (x, y), (x+30, y+20), (x, y+40)])


# Функция считывает передвижение кисти, без нее линия будет обрывчитывой, а с ней прямая и аккуратная
def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)
    
pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paint")
pygame.display.set_icon(pygame.image.load('assets/icon.png'))


#Colors
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
pink = (255,0,255)

#Начальные значания или константы
color = red
last_pos = (0,0)
mouse_down = False
screen.fill(white)
pygame.display.update()
radius = 5


blue_image = pygame.image.load('assets/blue.png').convert_alpha()
red_image = pygame.image.load('assets/red.png').convert_alpha()
green_image = pygame.image.load('assets/green.png').convert_alpha()
pink_image = pygame.image.load('assets/pink.png').convert_alpha()
eraser_image = pygame.image.load('assets/eraser.png').convert_alpha()

class Button():
    def __init__(self, x,y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.cliecked = False

    def draw(self):
        action = False

        # get mouse position
        pos = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.cliecked == False:
                self.cliecked = True
                action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

blue_button = Button(10, 10, blue_image)
red_button = Button(50, 10, red_image)
green_button = Button(10, 50, green_image)
pink_button = Button(50, 50, pink_image)
eraser_button = Button(10, 90, eraser_image)

#FPS
clock = pygame.time.Clock()
check = True

while check:

    action = pygame.event.wait()
    
    if blue_button.draw():
        color = blue
        radius = 5
    if red_button.draw():
        color = red
        radius = 5
    if green_button.draw():
        color = green
        radius = 5
    if pink_button.draw():
        color = pink
        radius = 5
    if eraser_button.draw():
        color = white
        radius = 20


    if action.type == pygame.QUIT:
        check = False
        pygame.quit()
    
    pygame.display.update()
    
    if action.type == pygame.KEYDOWN:
        if action.key == pygame.K_e:
            erase()
        
        #Rectange (t - от слова төртбұрыш)
        if action.key == pygame.K_r:
            rectangle()
        #Circle
        if action.key == pygame.K_c:
            cirlce()
        # Square
        if action.key == pygame.K_s:
            square()
        if action.key == pygame.K_t:
            equilateral_triangle()
        if action.key == pygame.K_x:
            right_triangle()
        if action.key == pygame.K_b:
            rhombus()

    #Mouse (brush) При нажатии мыши значение mouse_down меняется на True, что означает мышь активирована
    if action.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(screen, color, action.pos, 5)
        mouse_down = True
    
    #При отпускании мыши значение mouse_down меняется на False, что означает мышь диактивирована
    if action.type == pygame.MOUSEBUTTONUP:
        mouse_down = False
    
    
    if action.type == pygame.MOUSEMOTION:
        if mouse_down:
            pygame.draw.circle(screen, color, action.pos, radius)
            roundline(screen, color, action.pos, last_pos, radius)
        last_pos = action.pos
    
    
    clock.tick(60)
"""