import unittest
import pygame
from game import SnakeGame, Snake, Point, Apple

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
        self.game.apple = Apple(Point(100, 100))
        self.game.update()
        self.assertEqual(self.game.score, 1)
        self.assertEqual(len(self.game.snake.segments), 2)

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

    def test_game_object_draw(self):
        surface = pygame.Surface((800, 600))
        apple = Apple(Point(100, 100))
        apple.draw(surface, 20)
        self.assertTrue(pygame.Surface.get_at(surface, (100, 100)) != (0, 0, 0, 255))

    def test_change_direction(self):
        self.game.startGame()
        self.game.snake.next_direction = 'LEFT'
        self.game.update()
        self.assertEqual(self.game.snake.direction, 'LEFT')
        self.game.snake.next_direction = 'UP'
        self.game.update()
        self.assertEqual(self.game.snake.direction, 'UP')


if __name__ == "__main__":
    unittest.main()