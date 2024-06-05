import unittest
import pygame
from game.game import SnakeGame, Snake, Point, Apple, handle_keydown, handle_input, gameLoop, inputScreen, BLACK, BLOCK_SIZE, RED, DEFAULT_WIDTH, DEFAULT_HEIGHT, DEFAULT_SPEED, WHITE
from unittest.mock import patch, MagicMock

class TestSnakeGame(unittest.TestCase):

    def setUp(self):
        self.game = SnakeGame(800, 600, 15)
        self.game.snake = Snake([Point(100, 100)], 'UP')

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

    def test_handle_input(self):
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        focused_input = 'width'
        width, height, speed = "800", "600", "15"
        result = handle_input(event, focused_input, width, height, speed)
        self.assertEqual(result, (False, "800", "600", "15", focused_input))

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE)
        focused_input = 'width'
        width, height, speed = "800", "600", "15"
        result = handle_input(event, focused_input, width, height, speed)
        self.assertEqual(result, (True, "80", "600", "15", focused_input))

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE)
        focused_input = 'height'
        width, height, speed = "800", "600", "15"
        result = handle_input(event, focused_input, width, height, speed)
        self.assertEqual(result, (True, "800", "60", "15", focused_input))

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_BACKSPACE)
        focused_input = 'speed'
        width, height, speed = "800", "600", "15"
        result = handle_input(event, focused_input, width, height, speed)
        self.assertEqual(result, (True, "800", "600", "1", focused_input))

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_1, unicode='1')
        focused_input = 'width'
        width, height, speed = "800", "600", "15"
        result = handle_input(event, focused_input, width, height, speed)
        self.assertEqual(result, (True, "8001", "600", "15", focused_input))

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_1, unicode='1')
        focused_input = 'height'
        width, height, speed = "800", "600", "15"
        result = handle_input(event, focused_input, width, height, speed)
        self.assertEqual(result, (True, "800", "6001", "15", focused_input))

        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_1, unicode='1')
        focused_input = 'speed'
        width, height, speed = "800", "600", "15"
        result = handle_input(event, focused_input, width, height, speed)
        self.assertEqual(result, (True, "800", "600", "151", focused_input))

# тест гейм лупа
    @patch('pygame.font.Font.render')
    @patch('pygame.font.Font')
    @patch('pygame.event.get')
    @patch('pygame.display.set_mode')
    @patch('pygame.display.update')
    @patch('pygame.quit')
    @patch('game.game.inputScreen')
    @patch('game.game.SnakeGame')
    def test_game_loop_game_over(self, mock_SnakeGame, mock_inputScreen, mock_quit, mock_update, mock_set_mode, mock_event_get, mock_font, mock_font_render):
        mock_inputScreen.return_value = (800, 600, 15)

        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_f)],
            [pygame.event.Event(pygame.QUIT)],
        ]

        game_instance = MagicMock(spec=SnakeGame)
        game_instance.gameOver = True
        game_instance.isGameOverRendered = False
        mock_font_instance = MagicMock()
        mock_font.return_value = mock_font_instance
        game_instance.font = mock_font_instance
        mock_SnakeGame.return_value = game_instance

        gameLoop()

        mock_set_mode.assert_called_with((800, 600))
        self.assertTrue(mock_quit.called)
        self.assertTrue(game_instance.isGameOverRendered)
        mock_font_instance.render.assert_called_once_with("Game Over! Press R to Restart or F to Change Settings", True, RED)

    @patch('pygame.display.set_mode')
    @patch('pygame.font.SysFont')
    @patch('pygame.event.get')
    @patch('pygame.display.update')
    @patch('pygame.quit')
    @patch('game.game.inputScreen')
    @patch('game.game.SnakeGame')
    def test_game_loop_quit(self, mock_SnakeGame, mock_inputScreen, mock_quit, mock_update, mock_event_get, mock_SysFont, mock_set_mode):
        mock_inputScreen.return_value = (800, 600, 15)
        
        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.QUIT)],
        ]
        
        game_instance = MagicMock(spec=SnakeGame)
        game_instance.gameOver = False
        mock_SnakeGame.return_value = game_instance
        
        gameLoop()
        mock_set_mode.assert_called_with((800, 600))
        self.assertTrue(mock_quit.called)
    
    @patch('pygame.event.get')
    @patch('pygame.display.set_mode')
    @patch('pygame.display.update')
    @patch('pygame.quit')
    @patch('game.game.inputScreen')
    @patch('game.game.handle_keydown')
    @patch('game.game.SnakeGame')
    def test_game_loop_restart(self, mock_SnakeGame, mock_handle_keydown, mock_inputScreen, mock_quit, mock_update, mock_set_mode, mock_event_get):
        mock_inputScreen.return_value = (800, 600, 15)
        
        mock_handle_keydown.return_value = True
        
        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_f)],  
            [pygame.event.Event(pygame.QUIT)],  
        ]
        
        game_instance = MagicMock(spec=SnakeGame)
        game_instance.gameOver = False
        mock_SnakeGame.return_value = game_instance
        
        gameLoop()
        
        mock_set_mode.assert_called_with((800, 600))
        self.assertTrue(mock_quit.called)
        self.assertTrue(mock_handle_keydown.called)

# тест импут скрина
    @patch('pygame.font.SysFont')
    @patch('pygame.draw.rect')
    @patch('pygame.display.flip')
    @patch('pygame.event.get')
    @patch('pygame.display.set_mode')
    @patch('pygame.quit')
    def test_input_screen_quit(self, mock_quit, mock_set_mode, mock_event_get, mock_flip, mock_rect, mock_SysFont):
        mock_set_mode.return_value = MagicMock()
        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.QUIT)],
        ]

        with self.assertRaises(SystemExit):
            inputScreen()

        mock_quit.assert_called_once()

    @patch('pygame.font.SysFont')
    @patch('pygame.draw.rect')
    @patch('pygame.display.flip')
    @patch('pygame.event.get')
    @patch('pygame.display.set_mode')
    @patch('pygame.quit')
    @patch('game.game.handle_input')
    def test_input_screen_keydown(self, mock_handle_input, mock_quit, mock_set_mode, mock_event_get, mock_flip, mock_rect, mock_SysFont):
        mock_set_mode.return_value = MagicMock()
        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)],
            [pygame.event.Event(pygame.QUIT)]
        ]
        mock_handle_input.return_value = (False, '800', '600', '15', 'width')

        width, height, speed = inputScreen()

        self.assertEqual(width, 800)
        self.assertEqual(height, 600)
        self.assertEqual(speed, 15)

    @patch('pygame.font.SysFont')
    @patch('pygame.draw.rect')
    @patch('pygame.display.flip')
    @patch('pygame.event.get')
    @patch('pygame.display.set_mode')
    @patch('pygame.quit')
    @patch('game.game.handle_input')
    def test_input_screen_mouse_click(self, mock_handle_input, mock_quit, mock_set_mode, mock_event_get, mock_flip, mock_rect, mock_SysFont):
        mock_set_mode.return_value = MagicMock()
        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(210, 160))],
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)],
            [pygame.event.Event(pygame.QUIT)]
        ]
        mock_handle_input.return_value = (False, '800', '600', '15', 'width')

        width, height, speed = inputScreen()

        self.assertEqual(width, 800)
        self.assertEqual(height, 600)
        self.assertEqual(speed, 15)

        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(210, 260))],
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)],
            [pygame.event.Event(pygame.QUIT)]
        ]
        mock_handle_input.return_value = (False, '800', '600', '15', 'height')

        width, height, speed = inputScreen()

        self.assertEqual(width, 800)
        self.assertEqual(height, 600)
        self.assertEqual(speed, 15)
        
        mock_event_get.side_effect = [
            [pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=(210, 360))],
            [pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)],
            [pygame.event.Event(pygame.QUIT)]
        ]
        mock_handle_input.return_value = (False, '800', '600', '15', 'speed')

        width, height, speed = inputScreen()

        self.assertEqual(width, 800)
        self.assertEqual(height, 600)
        self.assertEqual(speed, 15)

    def test_grow(self):
        self.game.startGame()
        self.game.snake = Snake([Point(100, 100)], 'UP')
        initial_length = len(self.game.snake.segments)

        self.game.snake.grow(20)
        self.assertEqual(len(self.game.snake.segments), initial_length + 1)
        self.assertEqual(self.game.snake.segments[-1], Point(100, 120))

        self.game.snake.direction = 'LEFT'
        self.game.snake.grow(20)
        self.assertEqual(len(self.game.snake.segments), initial_length + 2)
        self.assertEqual(self.game.snake.segments[-1], Point(120, 120))

        self.game.snake.direction = 'DOWN'
        self.game.snake.grow(20)
        self.assertEqual(len(self.game.snake.segments), initial_length + 3)
        self.assertEqual(self.game.snake.segments[-1], Point(120, 100))

        self.game.snake.direction = 'RIGHT'
        self.game.snake.grow(20)
        self.assertEqual(len(self.game.snake.segments), initial_length + 4)
        self.assertEqual(self.game.snake.segments[-1], Point(100, 100))

    def test_draw(self):
        with patch('pygame.draw.rect') as mock_draw_rect:
            surface = MagicMock()
            self.game.snake.draw(surface, 20)
            self.assertEqual(mock_draw_rect.call_count, len(self.game.snake.segments))
            for segment in self.game.snake.segments:
                mock_draw_rect.assert_any_call(surface, WHITE, [segment.x, segment.y, 20, 20])

    def test_draw_objects(self):
        self.game.apple = Apple(Point(0, 100))
        with patch('pygame.draw.rect') as mock_draw_rect:
            surface = MagicMock()
            self.game.drawObjects(surface, BLOCK_SIZE)
            self.assertEqual(mock_draw_rect.call_count, len(self.game.snake.segments) + 1)
            for segment in self.game.snake.segments:
                mock_draw_rect.assert_any_call(surface, WHITE, [segment.x, segment.y, BLOCK_SIZE, BLOCK_SIZE])
            mock_draw_rect.assert_any_call(surface, pygame.Color('green'), [self.game.apple.position.x, self.game.apple.position.y, BLOCK_SIZE, BLOCK_SIZE])

if __name__ == "__main__":
    unittest.main()