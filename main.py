import snake as s
import pygame

# RGB tuples for colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Display properties:
# width, height and size of a grid element
width = 600
height = 400
grid_size = 10


def render_screen(display, snake, fruit):
    for i in range(snake.length):
        pygame.draw.rect(display, WHITE, (snake.past_position[i][0], snake.past_position[i][1], grid_size, grid_size))
    pygame.draw.rect(display, WHITE, (snake.x, snake.y, grid_size, grid_size))

    pygame.draw.rect(display, RED, (fruit.x, fruit.y, grid_size, grid_size))


def main():
    snake = s.Snake(width / 2, height / 2, 0, 0, width, height)
    fruit = s.Fruit(width, height)

    pygame.init()
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('pySnake')
    font = pygame.font.Font(pygame.font.get_default_font(), 16)

    clock = pygame.time.Clock()

    fruit.generate()
    text_surface = font.render("0", True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.center = (50, 30)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake.set_velocity(0, 1)
                elif event.key == pygame.K_UP:
                    snake.set_velocity(0, -1)
                elif event.key == pygame.K_LEFT:
                    snake.set_velocity(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    snake.set_velocity(1, 0)

        if snake.eaten_itself():
            snake.die()

        if fruit.eaten(snake):
            fruit.generate()
            snake.increment_length()

        snake.update_position()

        display.fill(BLACK)
        display.blit(text_surface, text_rect)
        text_surface = font.render(str(snake.length - 1), True, WHITE)
        render_screen(display, snake, fruit)

        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
