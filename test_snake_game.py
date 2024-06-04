import unittest
import pygame
from game.game import SnakeGame, Snake, Point, Apple, handle_keydown

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        self.game = SnakeGame(800, 600, 15)

    def test_default_initialization(self):
        self.game.startGame()
        self.assertEqual(self.game.snake.segments[0].x, 400)
        self.assertEqual(self.game.snake.segments[0].y, 300)
        self.assertEqual(self.game.score, 0)
        self.assertFalse(self.game.gameOver)

    def test_custom_initialization(self):
        custom_game = SnakeGame(1000, 800, 20)
        custom_game.startGame()
        self.assertEqual(custom_game.snake.segments[0].x, 500)
        self.assertEqual(custom_game.snake.segments[0].y, 400)
        self.assertEqual(custom_game.score, 0)
        self.assertFalse(custom_game.gameOver)

    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            SnakeGame(-100, -100, 10)

    def test_move_forward(self):
        self.game.startGame()
        initial_position = self.game.snake.segments[0]
        self.game.snake.move(20, 800, 600)
        new_position = self.game.snake.segments[0]
        self.assertNotEqual(initial_position, new_position)

    def test_change_direction_and_move(self):
        self.game.startGame()
        self.game.snake.next_direction = 'DOWN'
        self.game.snake.move(20, 800, 600)
        self.assertEqual(self.game.snake.direction, 'DOWN')
        self.game.snake.next_direction = 'LEFT'
        self.game.snake.move(20, 800, 600)
        self.assertEqual(self.game.snake.direction, 'LEFT')

    def test_invalid_direction(self):
        self.game.startGame()
        with self.assertRaises(ValueError):
            self.game.snake.next_direction = 'INVALID'
            self.game.snake.move(20, 800, 600)

    def test_move_out_of_bounds(self):
        self.game.startGame()
        self.game.snake.segments[0] = Point(0, 0)
        self.game.snake.direction = 'LEFT'
        self.game.update()
        self.assertTrue(self.game.gameOver)

    def test_no_collision(self):
        self.game.startGame()
        self.assertFalse(self.game.checkCollision())

    def test_wall_collision(self):
        self.game.startGame()
        self.game.snake.segments[0] = Point(0, 0)
        self.game.snake.move(20, 800, 600)
        self.assertTrue(self.game.checkCollision())

    def test_self_collision(self):
        self.game.startGame()
        self.game.snake.segments = [
            Point(100, 100), Point(120, 100), Point(120, 80), Point(100, 80), Point(100, 100)
        ]
        self.game.snake.move(20, 800, 600)
        self.assertTrue(self.game.checkCollision())

    def test_invalid_position(self):
        self.game.startGame()
        self.game.snake.segments[0] = Point(-100, -100)
        self.assertTrue(self.game.checkCollision())

    def test_apple_collision(self):
        self.game.startGame()
        self.game.snake.segments[0] = Point(100, 100)
        self.game.apple = Apple(Point(100, 80))
        self.game.update()
        self.assertEqual(self.game.score, 1)

    def test_apple_generation(self):
        self.game.startGame()
        initial_apple_position = self.game.apple.position
        while self.game.apple.position == initial_apple_position:
            self.game.apple = self.game.generateApple()
        self.assertNotEqual(self.game.apple.position, initial_apple_position)

    def test_snake_grow(self):
        self.game.startGame()
        initial_length = len(self.game.snake.segments)
        self.game.snake.grow(20)
        self.assertEqual(len(self.game.snake.segments), initial_length + 1)

    def test_change_direction(self):
        self.game.startGame()
        self.game.snake.next_direction = 'LEFT'
        self.game.update()
        self.assertEqual(self.game.snake.direction, 'LEFT')
        self.game.snake.next_direction = 'UP'
        self.game.update()
        self.assertEqual(self.game.snake.direction, 'UP')
    
    def test_score_increment(self):
        self.game.startGame()
        self.assertEqual(self.game.score, 0)
        self.game.snake.segments[0] = Point(100, 100)
        self.game.apple = Apple(Point(100, 80))
        self.game.update()
        self.assertEqual(self.game.score, 1)

    def test_game_restart(self):
        self.game.startGame()
        self.game.snake.segments[0] = Point(0, 0)
        self.game.snake.direction = 'LEFT'
        self.game.update()
        self.assertTrue(self.game.gameOver)
        self.game.startGame()
        self.assertFalse(self.game.gameOver)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(len(self.game.snake.segments), 1)

    def test_apple_not_on_snake(self):
        self.game.startGame()
        self.game.apple = self.game.generateApple()
        for segment in self.game.snake.segments:
            self.assertNotEqual(self.game.apple.position, segment)

    def test_snake_growth_after_apple_collision(self):
        self.game.startGame()
        initial_length = len(self.game.snake.segments)
        self.game.snake.segments[0] = Point(100, 100)
        self.game.apple = Apple(Point(100, 80))
        self.game.update()
        self.assertEqual(len(self.game.snake.segments), initial_length + 1)

    def test_snake_not_reverse(self):
        self.game.startGame()
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT))
        self.game.update()
        self.assertNotEqual(self.game.snake.direction, 'LEFT')

    def test_key_press(self):
        self.game.startGame()
        initial_direction = self.game.snake.direction
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.game.snake.next_direction = 'RIGHT'
        self.game.update()
        self.assertNotEqual(self.game.snake.direction, initial_direction)    

    def test_handle_keydown(self):
        self.game.startGame()

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_LEFT)
        result = handle_keydown(event, self.game)
        self.assertFalse(result)
        self.assertEqual(self.game.snake.next_direction, 'LEFT')

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RIGHT)
        result = handle_keydown(event, self.game)
        self.assertFalse(result)
        self.assertEqual(self.game.snake.next_direction, 'RIGHT')

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP)
        result = handle_keydown(event, self.game)
        self.assertFalse(result)
        self.assertEqual(self.game.snake.next_direction, 'UP')

        self.game.snake.direction = "LEFT"
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_DOWN)
        result = handle_keydown(event, self.game)
        self.assertFalse(result)
        self.assertEqual(self.game.snake.next_direction, 'DOWN')

        self.game.gameOver = True
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_r)
        result = handle_keydown(event, self.game)
        self.assertFalse(result)
        self.assertFalse(self.game.gameOver)

        self.game.gameOver = True
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_f)
        result = handle_keydown(event, self.game)
        self.assertTrue(result)

        self.game.gameOver = False
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_f)
        result = handle_keydown(event, self.game)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()