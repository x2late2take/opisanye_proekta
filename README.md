## Проект по предмету

Это программа змейка по предмету [Основы разработки ПО](https://cs.petrsu.ru/~kulakov/courses/develop/2023/task-git.php)

## Ссылки на модели
[Функциональные модели](docs/functions.md)
[Описание структурных моделей](docs/struct.md)
[Описание поведенческих моделей](docs/behavior.md)

## Функциональные возможности

1. Пользователь может управлять змейкой с помощью клавиш клавиатуры (например, стрелки).
2. Приложение отображает игровое поле, змейку, еду (обычно маркированную как фрукт) и счёт игрока.
3. Ещё пользователь может начать новую игру или завершить текущую.
4. Приложение отображает, что если змейка съедает еду, то она становится длиннее, а счёт игрока увеличивается, если змейка врезается в стену или саму себя, то игра оканчивается.
5. Приложение имеет возможность сохранять наивысший счёт игрока/составлять таблицу наилучших результатов.

## Функциональные алгоритмы

1. Появление фруктов на поле в зависимости от текущей длинны и скорости змейки, а так же от выбранного режима игры (скорость низкая/змейка маленькая = фруктиков мало, скорость увеличивается = фруктиков становится больше)
2. Функция обновления движения змейки(обработка столкновений) обработка ввода с мышки/клавиатуры/кнопок для управления движением змейки. управление движением(вверх, вниз, вправо, влево), текущее расположение(координаты змейки) и её перемещение в определенном направлении, проверка на столкновение с игровым краем или с самой собой, использование различных стратегий движения, проверка на то что бы еда не появлялась в месте где змейка уже существует.
3. Различные усложнения/упрощения игры в виде бонусов или сложностей, препятствий для усложнение игры и для дополнительных очков счёта.
4. Определение победы/поражения и счётчик очков. реагирование на выход из игры.
5. Установка начального направления змейки.
6. Создание игрового поля с заданными размерами и размещение змеи на нём.