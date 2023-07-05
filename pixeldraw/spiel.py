import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))


# Baue drei Rechtecke
rects = [
    pygame.Rect(100, 100, 10, 30),
    pygame.Rect(200, 200, 50, 50),
    pygame.Rect(300, 300, 50, 50),
    pygame.Rect(10, 100, 50, 50),
    pygame.Rect(20, 200, 50, 50),
    pygame.Rect(30, 300, 50, 50),
]

colors = [
    (255,255,0),
    (255,0,0),
    (0,255,0),
    (255,50,30),
    (1,40,90),
    (5,88,44),
    (255,255,0),
    (255,255,0),
    ]

richtung = [
    (1,1),
    (-1,0),
    (0,-1),
    (1,1),
    (-1,0),
    (0,-1),
    ]

pointer_rect = pygame.Rect(pygame.mouse.get_pos(), (20, 20))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_pos = pygame.mouse.get_pos()
        pointer_rect = pygame.Rect(mouse_pos, (10, 10))
        

    # Check for collision with each rectangle
    for rect in rects:
        
        if rect.collidepoint(mouse_pos):
            print("Collision detected!")
            rects.remove(rect)
                
    # Draw the rectangles
    screen.fill((255, 255, 255))
    for i,rect in enumerate(rects):
        rect.x += richtung[i][0]
        rect.y += richtung[i][1]
        pygame.draw.rect(screen, (colors[i][0],colors[i][1] ,colors[i][2]), rect)
        if rect.x > 800:
            rects.remove(rect)
    
    pygame.draw.rect(screen,(0,0,0), pointer_rect)
    
    
    clock.tick(60)
    # Update the display
    pygame.display.update()

pygame.quit()

        

    
    
    
    
    
    
    
    
    
    
    
