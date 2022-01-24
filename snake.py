import pygame, random
from pygame.math import Vector2
pygame.font.init()
pygame.init()



#variables
score = 0
body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)]
direction = Vector2(-1, 0)
###
cell_size = 20
cell_number = 15
###
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number))
pygame.display.set_caption("Shitty Snake Game :)")
myfont = pygame.font.SysFont('Comic Sans MS', 20)
update = pygame.USEREVENT
pygame.time.set_timer(update, 75)
###


#snake variables

def main():
    global direction
    run = True
    define_fruit()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == update:
                render()
                draw_fruit()
                draw_snake()
                draw_text()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction.y != 1:
                    direction = Vector2(0,-1)
                if event.key == pygame.K_DOWN and direction.y != -1:
                    direction = Vector2(0,1)
                if event.key == pygame.K_LEFT and direction.x != 1:
                    direction = Vector2(-1,0)
                if event.key == pygame.K_RIGHT and direction.x != -1:
                    direction = Vector2(1,0)
        screen.fill("black")
        draw_fruit()
        draw_snake()
        draw_text()
        pygame.display.update()

def define_fruit():
    global fruit_pos_x, fruit_pos_y, fruit_color
    fruit_pos_x = random.randint(1, cell_number - 1)
    fruit_pos_y = random.randint(1, cell_number - 1)
    fruit_color = "red"
    for position in body:
        if position.x == fruit_pos_x and position.y == fruit_pos_y:
            fruit_pos_x = random.randint(1, cell_number - 1)
            fruit_pos_y = random.randint(1, cell_number - 1)

def draw_fruit():
    fruit = pygame.Rect(fruit_pos_x * cell_size,fruit_pos_y * cell_size,cell_size,cell_size)
    pygame.draw.rect(screen, fruit_color, fruit)

def draw_snake():
    global x_pos, y_pos
    for block in body:
        x_pos = int(block.x * cell_size)
        y_pos = int(block.y * cell_size)
        snake_block = pygame.Rect(x_pos, y_pos, cell_size,cell_size)
        pygame.draw.rect(screen, (255,255,255), snake_block)

def draw_text():
    textsurface = myfont.render('Score %d' % score, False, (255, 255, 255))
    screen.blit(textsurface, (10, 10))

def render():
    global body, direction, score
    # snakeblocks
    if not (body[0].x == fruit_pos_x and body[0].y == fruit_pos_y):
        clear = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
        pygame.draw.rect(screen, (0, 0, 0), clear)
        body_copy = body[:-1]
        new_pos = body_copy[0] + direction
        body_copy.insert(0, new_pos)
        body = body_copy[:]
        if new_pos.x >= cell_number:
            new_pos.x = new_pos.x - cell_number
        elif new_pos.x < 0:
            new_pos.x = cell_number
        elif new_pos.y >= cell_number:
            new_pos.y = new_pos.y - cell_number
        elif new_pos.y < 0:
            new_pos.y = cell_number
        for position in body[1:]:
            if position == body[0]:
                pygame.quit()
    else:
        body.append(body[0] + direction)
        score +=1
        define_fruit()

main()
