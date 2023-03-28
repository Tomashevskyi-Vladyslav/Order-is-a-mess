import pygame as pp
pp.init()
pp.mixer.init()
screen = pp.display.set_mode((400, 400))
#rect = ppe.Rect(0, 0, 120, 120)
run  = True
while run:
#    pp.draw.rect(screen, (0, 0, 144), rect, 0)
#    pp.display.update()
    for event in pp.event.get():
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                rect.move_ip(-40, 0)
#            elif event.key == pygame.K_RIGHT:
#                rect.move_ip(40, 0)
#            elif event.key == pygame.K_UP:
#                rect.move_ip(0, -40)
#            elif event.key == pygame.K_DOWN:
#                rect.move_ip(0, 40)
        if event.type == pp.QUIT:
            pp.quit()
            run = False
