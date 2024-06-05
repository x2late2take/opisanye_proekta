### Ошибка №1

- **Описание:** Невозможно задать атрибуты встроенного/расширенного типа `pygame.time.Clock`.
- **Тест:** test_game_loop_quit
- **Входные данные:** Pygame события, включая событие `pygame.QUIT`.
- **Ожидаемый результат:** Тест успешно завершает выполнение, вызывая `pygame.quit`.
- **Фактический результат:** Ошибка `TypeError`, связанная с невозможностью патчить встроенные типы.
- **Возможная причина:** Pygame объекты являются встроенными типами, которые нельзя патчить с помощью `unittest.mock`.
- **Статус:** Исправлена. Удалены патчи для встроенных типов Pygame и использованы фиктивные объекты.

### Ошибка №2

- **Описание:** Mock объект не имеет атрибута `font`.
- **Тест:** test_game_loop_game_over
- **Входные данные:** Pygame события, включая событие `pygame.QUIT`.
- **Ожидаемый результат:** Тест успешно завершает выполнение, проверяя наличие `font`.
- **Фактический результат:** Ошибка `AttributeError`.
- **Возможная причина:** Mock объект не имеет всех атрибутов, ожидаемых в игровом объекте.
- **Статус:** Исправлена. Добавлены необходимые атрибуты к фиктивному игровому объекту.

### Ошибка №3

- **Описание:** Mock объект не имеет атрибута `isGameOverRendered`.
- **Тест:** test_game_loop_game_over
- **Входные данные:** Pygame события, включая событие `pygame.QUIT`.
- **Ожидаемый результат:** Тест успешно завершает выполнение, проверяя наличие `isGameOverRendered`.
- **Фактический результат:** Ошибка `AttributeError`.
- **Возможная причина:** Mock объект не имеет всех атрибутов, ожидаемых в игровом объекте.
- **Статус:** Исправлена. Добавлены необходимые атрибуты к фиктивному игровому объекту.

### Ошибка №4

- **Описание:** Невозможно задать атрибуты встроенного/расширенного типа `pygame.font.Font`.
- **Тест:** test_draw_score
- **Входные данные:** Объект `pygame.font.Font` и методы `render` и `blit`.
- **Ожидаемый результат:** Тест успешно завершается, проверяя вызовы методов `render` и `blit`.
- **Фактический результат:** Ошибка `TypeError`, связанная с невозможностью патчить встроенные типы.
- **Возможная причина:** Pygame объекты являются встроенными типами, которые нельзя патчить с помощью `unittest.mock`.
- **Статус:** Исправлена. Использованы фиктивные объекты вместо патчей для встроенных типов.

### Ошибка №5

- **Описание:** Mock объект вызван дважды вместо одного раза.
- **Тест:** test_game_loop_game_over
- **Входные данные:** Pygame события, включая событие `pygame.QUIT`.
- **Ожидаемый результат:** Тест успешно завершает выполнение, проверяя вызов метода `render`.
- **Фактический результат:** Ошибка `AssertionError`, ожидается вызов один раз, но вызвано дважды.
- **Возможная причина:** Некорректная настройка теста или игрового цикла.
- **Статус:** Исправлена. Обновлен тест и игровой цикл для правильной проверки вызовов.

### Ошибка №6

- **Описание:** Невозможно задать атрибуты встроенного/расширенного типа `pygame.surface.Surface`.
- **Тест:** test_draw_score
- **Входные данные:** Объект `pygame.surface.Surface` и методы `render` и `blit`.
- **Ожидаемый результат:** Тест успешно завершается, проверяя вызовы методов `render` и `blit`.
- **Фактический результат:** Ошибка `TypeError`, связанная с невозможностью патчить встроенные типы.
- **Возможная причина:** Pygame объекты являются встроенными типами, которые нельзя патчить с помощью `unittest.mock`.
- **Статус:** Исправлена. Использованы фиктивные объекты вместо патчей для встроенных типов.

### Ошибка №7

- **Описание:** Тест выявил несоответствие ожидаемого результата фактическому для метода `__repr__` в классе `Point`.
- **Тест:** test_grow
- **Входные данные:** Создание объекта `Point` и вызов метода `__repr__`.
- **Ожидаемый результат:** Строковое представление объекта в формате `Point(x, y)`.
- **Фактический результат:** Строка не соответствует ожидаемому формату.
- **Возможная причина:** Ошибка в реализации метода `__repr__`.
- **Статус:** Исправлена. Обновлен метод `__repr__` для правильного формирования строкового представления.

### Ошибка №8

- **Описание:** Тест выявил отсутствие патча для метода `render` объекта `pygame.font.Font`.
- **Тест:** test_draw_score
- **Входные данные:** Вызов метода `drawScore` с фиктивными объектами.
- **Ожидаемый результат:** Успешное выполнение метода `drawScore`.
- **Фактический результат:** Ошибка `AttributeError`, метод `render` не найден.
- **Возможная причина:** Некорректная настройка фиктивных объектов.
- **Статус:** Исправлена. Добавлен патч для метода `render`.

### Ошибка №9

- **Описание:** Тест выявил отсутствие вызова метода `render` в методе `drawScore`.
- **Тест:** test_draw_score
- **Входные данные:** Вызов метода `drawScore` с фиктивными объектами.
- **Ожидаемый результат:** Успешное выполнение метода `drawScore` с вызовом `render`.
- **Фактический результат:** Ошибка `AssertionError`, метод `render` не был вызван.
- **Возможная причина:** Некорректная настройка теста или фиктивных объектов.
- **Статус:** Исправлена. Обновлен тест и метод `drawScore` для правильной проверки вызовов.