import pygame, sys

SCALE = 20
WIDTH, HEIGHT = 28, 28

def get_line_points(a, b):

    x0, y0 = a
    x1, y1 = b
    
    # transform line for each quadrant

    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            g = line_generator(x1, y1, x0, y0)
        else:
            g = line_generator(x0, y0, x1, y1)

        for x, y in g: yield x, y

    else:
        if y0 > y1:
            g = line_generator(y1, x1, y0, x0)
        else:
            g = line_generator(y0, x0, y1, x1)

        for x, y in g: yield y, x

def line_generator(x0, y0, x1, y1):
  
    # sort of copied from wikipedia

    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy
    D = (2 * dy) - dx
    y = y0

    for x in range(x0, x1+1):

        yield x, y
        
        #extra bits make line thicker
        
        yield x, y+yi
        #yield x, y-yi

        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2*dy

def main():

    pygame.init()

    surface = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))


    while True:

        surface.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        mx, my = pygame.mouse.get_pos()

        for x, y in get_line_points((WIDTH // 2, HEIGHT // 2), (mx // SCALE, my // SCALE)):
            #print(x, y)
            pygame.draw.rect(surface, (255,255,255), (x*SCALE, y*SCALE, SCALE, SCALE))

        pygame.display.update()



if __name__ == "__main__":
    main()
