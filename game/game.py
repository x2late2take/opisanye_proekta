import pygame
import random

# Инициализация Pygame
pygame.init()

# Дефолтные параметры
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600
BLOCK_SIZE = 20
DEFAULT_SPEED = 15

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Настройки окна
window = pygame.display.set_mode((DEFAULT_WIDTH, DEFAULT_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Классы и функции игры
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GameObject:
    def __init__(self, position: Point):
        self.position = position

    def draw(self, surface, block_size):
        pygame.draw.rect(surface, GREEN, [self.position.x, self.position.y, block_size, block_size])

class Snake:
    def __init__(self, start_segments: list, start_direction: str):
        self.segments = start_segments
        self.direction = start_direction
        self.next_direction = start_direction  # Новая переменная для хранения следующего направления

    def move(self, block_size, game_width, game_height):
        if self.next_direction not in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            raise ValueError(f"Invalid direction: {self.next_direction}")

        self.direction = self.next_direction  # Обновляем текущее направление только здесь
        head = self.segments[0]
        new_head = None
        if self.direction == 'UP':
            new_head = Point(head.x, head.y - block_size)
        elif self.direction == 'DOWN':
            new_head = Point(head.x, head.y + block_size)
        elif self.direction == 'LEFT':
            new_head = Point(head.x - block_size, head.y)
        elif self.direction == 'RIGHT':
            new_head = Point(head.x + block_size, head.y)

        self.segments.insert(0, new_head)
        self.segments.pop()

    def grow(self, block_size):
        tail = self.segments[-1]
        if self.direction == 'UP':
            new_segment = Point(tail.x, tail.y + block_size)
        elif self.direction == 'DOWN':
            new_segment = Point(tail.x, tail.y - block_size)
        elif self.direction == 'LEFT':
            new_segment = Point(tail.x + block_size, tail.y)
        elif self.direction == 'RIGHT':
            new_segment = Point(tail.x - block_size, tail.y)
        
        self.segments.append(new_segment)

    def draw(self, surface, block_size):
        for segment in self.segments:
            pygame.draw.rect(surface, WHITE, [segment.x, segment.y, block_size, block_size])

class Apple(GameObject):
    def __init__(self, position: Point):
        super().__init__(position)

class SnakeGame:
    def __init__(self, game_width, game_height, speed):
        self.gameWidth = game_width
        self.gameHeight = game_height
        self.speed = speed
        self.snake = Snake([Point(game_width // 2, game_height // 2)], 'UP')
        self.apple = self.generateApple()
        self.score = 0
        self.gameOver = False
        self.font = pygame.font.SysFont(None, 35)

    def startGame(self):
        self.snake = Snake([Point(self.gameWidth // 2, self.gameHeight // 2)], 'UP')
        self.apple = self.generateApple()
        self.score = 0
        self.gameOver = False

    def generateApple(self):
        return Apple(Point(random.randint(0, self.gameWidth // BLOCK_SIZE - 1) * BLOCK_SIZE,
                           random.randint(0, self.gameHeight // BLOCK_SIZE - 1) * BLOCK_SIZE))

    def checkCollision(self):
        head = self.snake.segments[0]
        # Проверка столкновения с границами поля
        if head.x < 0 or head.x >= self.gameWidth or head.y < 0 or head.y >= self.gameHeight:
            return True
        # Проверка столкновения с хвостом
        for segment in self.snake.segments[1:]:
            if head.x == segment.x and head.y == segment.y:
                return True
        return False

    def update(self):
        if not self.gameOver:
            self.snake.move(BLOCK_SIZE, self.gameWidth, self.gameHeight)
            if self.checkCollision():
                self.gameOver = True

            # Проверка столкновения с яблоком
            head = self.snake.segments[0]
            if head.x == self.apple.position.x and head.y == self.apple.position.y:
                self.score += 1
                self.snake.grow(BLOCK_SIZE)
                self.apple = self.generateApple()

    def drawScore(self, surface):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        surface.blit(score_text, [10, 10])

    def drawObjects(self, surface, block_size):
        self.snake.draw(surface, block_size)
        self.apple.draw(surface, block_size)

def handle_input(event, focused_input, width, height, speed):
    if event.key == pygame.K_RETURN:
        return False, width, height, speed, focused_input
    elif event.key == pygame.K_BACKSPACE:
        if focused_input == 'width':
            width = width[:-1]
        elif focused_input == 'height':
            height = height[:-1]
        elif focused_input == 'speed':
            speed = speed[:-1]
    else:
        if focused_input == 'width' and event.unicode.isdigit():
            width += event.unicode
        elif focused_input == 'height' and event.unicode.isdigit():
            height += event.unicode
        elif focused_input == 'speed' and event.unicode.isdigit():
            speed += event.unicode
    return True, width, height, speed, focused_input

def inputScreen():
    width = str(DEFAULT_WIDTH)
    height = str(DEFAULT_HEIGHT)
    speed = str(DEFAULT_SPEED)
    focused_input = 'width'

    input_active = True
    font = pygame.font.SysFont(None, 35)

    width_rect = pygame.Rect(200, 150, 400, 40)
    height_rect = pygame.Rect(200, 250, 400, 40)
    speed_rect = pygame.Rect(200, 350, 400, 40)

    while input_active:
        window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                input_active, width, height, speed, focused_input = handle_input(event, focused_input, width, height, speed)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if width_rect.collidepoint(event.pos):
                    focused_input = 'width'
                elif height_rect.collidepoint(event.pos):
                    focused_input = 'height'
                elif speed_rect.collidepoint(event.pos):
                    focused_input = 'speed'

        width_rect = pygame.draw.rect(window, WHITE, (200, 150, 400, 40))
        height_rect = pygame.draw.rect(window, WHITE, (200, 250, 400, 40))
        speed_rect = pygame.draw.rect(window, WHITE, (200, 350, 400, 40))

        width_text = font.render(f'Width(800 - 1500): {width}', True, BLACK)
        height_text = font.render(f'Height(600 - 1300): {height}', True, BLACK)
        speed_text = font.render(f'Speed(5 - 50): {speed}', True, BLACK)

        window.blit(width_text, (210, 160))
        window.blit(height_text, (210, 260))
        window.blit(speed_text, (210, 360))

        pygame.display.flip()
        clock.tick(15)

    width = max(800, min(1500, int(width)))
    height = max(600, min(1300, int(height)))
    speed = max(5, min(50, int(speed)))

    return width, height, speed

def handle_keydown(event, game):
    if event.key == pygame.K_LEFT and game.snake.direction != 'RIGHT':
        game.snake.next_direction = 'LEFT'
    elif event.key == pygame.K_RIGHT and game.snake.direction != 'LEFT':
        game.snake.next_direction = 'RIGHT'
    elif event.key == pygame.K_UP and game.snake.direction != 'DOWN':
        game.snake.next_direction = 'UP'
    elif event.key == pygame.K_DOWN and game.snake.direction != 'UP':
        game.snake.next_direction = 'DOWN'
    elif event.key == pygame.K_r and game.gameOver:
        game.startGame()
    elif event.key == pygame.K_f and game.gameOver:
        return True
    return False

def gameLoop():
    width, height, speed = inputScreen()
    global window
    window = pygame.display.set_mode((width, height))
    game = SnakeGame(width, height, speed)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if handle_keydown(event, game):
                    width, height, speed = inputScreen()
                    window = pygame.display.set_mode((width, height))
                    game = SnakeGame(width, height, speed)

        game.update()

        window.fill(BLACK)
        game.drawObjects(window, BLOCK_SIZE)
        game.drawScore(window)

        if game.gameOver:
            gameOverText = game.font.render("Game Over! Press R to Restart or F to Change Settings", True, RED)
            window.blit(gameOverText, [width // 2 - gameOverText.get_width() // 2, height // 2])

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()

if __name__ == "__main__":
    gameLoop()

