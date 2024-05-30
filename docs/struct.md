# Структурные модели


## Описание внутренней структуры приложения

[Посмотреть код диаграммы](lab4/InsideStructure)
![Внутренняя структура](https://www.plantuml.com/plantuml/png/fLHBRjim4Dth5DnLRkqB246Hea0_AnV88aj3bXXBjImQ8Xttqm9DlEaYG6xGCxY5dJXsh5vXUAEEF5H9gqq_I005dC-Rnvb7pw5KOQ4ceynxmE0BVDUVO0aB_3RuRM45ImPhDERwJ9z12T-yA0kbPAz4cYlstcFurs5l0eQcCTvQun7b-HHlcr3B--YPCi_34U_sN_F8rXeBcQfKv05XJHsRw3SIMYOZBiAfBoV5IHZnDkjd8XhsPFgEEsnFnkEC_vc8Skx1qUtZHAE_qb3QlPYEyd1eQIGVZ7YkPC2oLAg3NR779XQd1O-8HAg260Zkx-Jl_HRSPXJSHzSN78bJxjjx6O47A5DlciOgSHq9JmU9Ge_jRr28QHF-lxtZcx3zLqJ7FuaTvmjBNe-g0WTKmxZ2IlM0nA-p8b7mPh7kAIy2rXSYCyuJaMFjPw8MrjxC_zTPq9XtaDep6SUXicQKy6ZuL6Ge3ifmdAgaVZxob_T3jpF09CpZZB_CnnFbfzN_FGa7FES5yj2JRxdjDpcbxufpL8scLiWDq2zKtYbUjMFqEMoXr9zfl-XB1hTul8A5dhchPexkbKThvk13f-Di0CyUAKJtRdhh6JK3HdZxX1xUuQEoZiyjQlObhAgxrfkot6yERXnqmAfSH9ImqHTmhMUmrESCpGLigzwlTuEuWRMUxSDkCUUAabTeu45V61oKJ5_2LzYWkKO3FND67B3q3daULwlz1m00)

## Описание используемых структур/объектов данных

[Посмотреть код диаграммы](lab4/UsedStructures)
![Используеммые структуры и объекты](https://www.plantuml.com/plantuml/png/bLJBJjjC6DtxAKPi_hyII5rRRKKtRNSWeQgBgWiJ35WrTXIxbwggHEoIjYGYRz1dI4D277BX5UPxevwZ6J5n8Y4L4PZvBkUSR-PCThCyQEKVpcBlFwL_wpivrsCzmcU6pq9NUgpqBJO3QKjRB_LGwGg_Sg4GAb1TwJzIIi6KruY3B5FxQPJawgkdyBEZFlkAswVgiGrySO5ldcrvtcp6uNrBCysYF4eJ7r2cD0a_cVN_ZrpJtY6qD_wzxo09thkcB3mv2vCyyrKSPVaJLkVFqFhsdIquYbfXmy1cUGkPhTVxMsjeBuCpXtY2pPleA3zrWxh4gp0wEStNCnb1V8DbP9irP9k2W0VastCo1LoxWgoHji9rs5Dm7RX4NSdUnx3bgyCqZP4u3k8ijCdZD8705_ZBAMaBAM25fVmqbf2-qdCiR_H8IgMNCC0bjhUe6Y1HUMOCjREZtEbubBiHD5Uu6RTc15SRcDQ6tDo1RYOzFQ7VJ0fod0PhH7Sflg9jwMXuzGRLHQrQkePrsnwjhkvjLGSf-JH0E0Hz7s20gVGrGg2JhfuhvB6H3dBcfSm9XaY17HyJo2cPlGebFxZmZ55zrBcdvnWuxGIQE_XSRKofCFrWHGOvJG_ex7a3sUA2igZfb-zoBYN1jld4bmH5fAkdlDubzB8Ab5sCqAFaIwjleQ2A3fYoJq_TDJv4rwP-bYjsaGjW5MS0VgdaWXEOjbNyYXFE-0zZsXllIDSC2d287zRrZrVR1xLXXXI7B2bxuEfRhpwWss59kSqfg95KVVab9Q-bqXF4KNFDIhsmjsEK8o9NjfApEXkvxzSHjXKb6Zjxks5on6zaxoy0)

# Внутренняя структура приложения
## Игра "Змейка" состоит из нескольких основных компонентов:

* _SnakeGame_: Этот класс представляет основное состояние игры, включая размер игрового поля, объекты змейки, еды(фрукта), препятствий(тела змейки и границ поля), текущий счет, рекордный счет, флаг окончания игры и шрифт.
* _Snake_: Этот класс представляет змейку на игровом поле. Он содержит список сегментов, образующих тело змейки, а также текущее направление движения.
* _Point_: Представляет точку на игровом поле с координатами x и y.
* _Apple_: Представляет еду(в нашем случае фрукт) на игровом поле. Оно имеет позицию, представленную объектом Point.

## Используемые структуры/объекты данных:

* _Point_: Точка на игровом поле с координатами x и y.
* _Apple_: Еда(в нашем случае фрукт) на игровом поле с позицией, представленной объектом Point.
* _Obstacle_: Точки на поле представленные объектом Point, при попадании на пиксели которых игра заканчивается(змейка врезается в саму себя или в границы поля).
* _Snake_: Змейка на игровом поле с сегментами, образующими ее тело, и текущим направлением движения.
* _SnakeGame_: Состояние игры, включающее размер игрового поля, объекты змейки, еды(фрукта), препятствий(тела змейки и границ поля), текущий счет, рекордный счет, флаг окончания игры и шрифт.