# Example file showing a circle moving on screen
import pygame
from body import Body
from vector2 import Vector2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
paused = False
deltat = 0
#center of screen
center = Vector2(screen.get_width() / 2, screen.get_height() / 2)

# initialization of array to hold bodies
bodies = []
# initialization of bodies
plan_one = Body(center + 100, 10, 50, vel=Vector2(-1.5, 1.5))
plan_two = Body(center - 100, 10, 100, vel=Vector2(0.5, 3))
star1 = Body(center, 18, 1000, color="yellow")
bodies.append(plan_one)
bodies.append(plan_two)
bodies.append(star1)

while running:
    # ends game loop if pygame window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fills display with black to get rid of last frame
    screen.fill("black")

    # gets keys pressed
    keys = pygame.key.get_pressed()

    # pauses game if 'p' key is pressed
    if keys[pygame.K_p]:
        paused = True
    else:
        paused = False

    # moves all bodies by 10 units when w, a, s, or d is pressed
    for self in bodies:
        # set displacement per frame
        disp = 5
        if keys[pygame.K_w]:
            self.pos -= Vector2(0, disp)
        if keys[pygame.K_s]:
            self.pos += Vector2(0, disp)
        if keys[pygame.K_a]:
            self.pos -= Vector2(disp, 0)
        if keys[pygame.K_d]:
            self.pos += Vector2(disp, 0)
    
    # calculates each body's position if the game is not paused
    for self in bodies:
        if not paused:
            self.calculate(bodies)
        #draws each body
        pygame.draw.circle(screen, self.color, (self.pos.x, self.pos.y), self.radius)

    # updates display
    pygame.display.flip()

    # limits FPS to 60
    deltat = clock.tick(60) / 1000

pygame.quit()