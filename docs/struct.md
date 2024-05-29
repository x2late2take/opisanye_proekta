# Структурные модели


## Описание внутренней структуры приложения

[Код диаграммы](lab4/InsideStructure)
![Внутренняя структура](https://www.plantuml.com/plantuml/png/fLJBhfim4Dtp5LuwQlW1T7Lrsqfzh58fYomZOoRWnjZ8Ov8-sd-lmUEQq4TxbImYV6REd9avXYVqmlcnruNK0f5ziCfuzhLWuLUoJnKBHpfypeSNCO_7-9P2c-9xGMNUYXvszKUGkTPWKNbbJHMvL2SdybN2XZ8Q9wuSHtSI4hQirbQUZwY-m4BjvJ1e-BjGpBb3OrUZ5_9VCfHsbzBUY7EMGMXxC1uhfXNwXxdO8yKQvK164VGkAaGwdsqz_fQyPJ5uoquDzlO2FFT51hV1fkDLDRvR0XsejlCpakYjizSr_RcpXpkHvv-43Z-55-2xB4ueJkGgrY18JAvNqNo2B3cKbf8SIqkjRL-dsAlmd72Kri6wYTq5N1KeLXDuiYRqzCQc2v4dul-xmsZFJ4d8E3J2vwFiG9vVMwqL1liEodTf2FpbtiNkYDW9qsXuRuRHSpNztrZVWW4NTEAhibckRQs9V6dgVbfDSdOPY6ys_j7q-BKfoqUs-10K-P4zV2jBQcEDff7N0V8_twHGdh0dCCtOwny0)

## Описание используемых структур/объектов данных

[Код диаграммы](lab4/UsedStructures)
![Используеммые структуры и объекты](https://www.plantuml.com/plantuml/png/bL0zJyCm4DtzAwnExH29sG9K682jbIh4W1YSv9fOE7QKk_8Xn7_dZ6siUiFJ-Tw7xhqjabxeD5aXEgiHvTuRH_9BI7wD_50oVA_aHLfybiLtbjpCiuK_oUpHaF5EiLMaEdYFytfJHBiMINV_rnsSVYqYX642HwYaDKYNl-nhbZw_949l5kYYBTB2oEfnlwhSxlLK70V-F9cUnXAq00zWXf5g18E9Ybxnx3YlDucWGq4gzHG9OIu4dyh8EN8vPr5QFxMPSClp6OYTNw0-REHh3pMGi-pUO55iwYq3HsqH4dZqZYFUUKUXfvXADeqiPOcOf5hce-kz45jm_McoFm00)

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