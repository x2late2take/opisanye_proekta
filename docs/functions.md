# Функциональные модели

## Функциональные возможности

### Управление змейкой

* _Пользователь_: Нажимает клавишу со стрелкой вверх на клавиатуре.

* _Приложение_: Перемещает змейку вверх.

* _Пользователь_: Нажимает клавишу со стрелкой вправо на клавиатуре.

* _Приложение_: Перемещает змейку вправо.

### Отображение игрового поля

* _Пользователь_: Открывает Приложение и начинает игру.

* _Приложение_: Отображает игровое поле с начальной позицией змейки и едой (фруктом).

### Съедание еды и увеличение счёта

* _Пользователь_: Направляет змейку на еду с помощью клавиш клавиатуры.

* _Приложение_: Змейка съедает еду, становится длиннее, счёт игрока увеличивается.

### Окончание игры при столкновении

* _Пользователь_: Направляет змейку так, что она врезается в стену.

* _Приложение_: Отображает сообщение об окончании игры и текущий счёт игрока.

### Начало новой игры

* _Пользователь_: Нажимает кнопку “Новая игра”.

* _Приложение_: Сбрасывает игровое поле и счёт, начинает новую игру.

### Сохранение наивысшего счёта

* _Пользователь_: Завершает игру с новым наивысшим счётом.

* _Приложение_: Сохраняет новый наивысший счёт и обновляет таблицу лучших результатов.

### Таблица лучших результатов

* _Пользователь_: Открывает таблицу лучших результатов.

* _Приложение_: Отображает таблицу с наивысшими счётами игроков.


## Общая диаграмма хода игры
[Посмотреть код диаграммы](lab3/UseCaseDiagram)
![Диаграмма хода игры](https://www.plantuml.com/plantuml/png/dLJDRjf04BxlKwouHshuoSyjKf-XjrmGSLka52Hmxc2KXlv8gAUUsghg2pYqXWLgymepRzHlThsEeG9BEGoUySptVJixWw-6ONiGthsxLRV1wr27VJteldaRwflk8EY4tNvFgNOdx0yq_Q2CDloPbdZEAUQ84ecLkXi6dVOmq3NwHZ4joD1VF1EEDArf0tTEXgTahdjFiU1vmYF-LDFjeNxrydIFPiiZgOJ2p54jmPhGYjOyoI7r4kGxHyY0ZkPE6s92OI2OqGB857wI8njxo8mUhTp2dzlGRxn0dx14qrPQBz3D4lghFnN5ciVy4S4VJmAtE6lhC2P2VMgr34U8PneK6p9ucQBEgvwL67wXE94QVY3ZEnQk1_x2KGuuFo19SnuXM0hA2UQ0Ynr0B1guqUdEdHGDNLPS8Oyfioy_-Bl7H11h_AnXAOuUsuJnrCKgl3Y-Kd9PMzc3wnxo-JRE_D3YcgSfhzHFTpmUouOSdpBEQVRlyhI-mvNnlMqszSjfvmVg5S0f4aOYS4pXhVuZQnnRN6qNuj5EzxtqI1kU03z5VA_Tw7WY_pmfX47P4pUhXl9ywfPIXxu0-kH4AYhozOfyeug_IW3TA_nwDJ0wjwaGEhUbOCuzKp3ddZyLN2YOSoyLpBbOID7FWtefqL2YcmSjTHNqRl0f_GS0)

## Начать новую игру
[Посмотреть код диаграммы](lab3/NewGame)
![Начать новую игру](https://www.plantuml.com/plantuml/png/XL9HJi905FplAJPymHNWGwvYGWbD48rW_1MQQ1IqYVhX3tg55gnTYYnNc7SZvrasIWmnJNVxcfbvExElFHmTduykJlh1zqVGn1iSrZ93mNs1L2R8jJRO8CK7B3wvvp8nAFdBOOjIObF32vPofNYPrLf1r3Lrp5dULBz8Lps9vS70AbJYeuOPzS81WSz86u4nJOfiOEMQY1HhhWNPh2Jnf6bBSNZbiHmoDjGpvSf2liDe7xvBE8Cjr4nIaPuKY5n9NhIWcnmhMh5a6qcGiQzZdHxaR5daN1Fw6ik4pInMoYRNKIzJvcKlweUcxbCnI54IQubcZdGU3Nzy7tQawMk-SijT7SaOJhjoJOZPIyOh8Ql2njhhx8BWIsbFqsvtAayreeqUpCWzQpq3JLU2VY9YNkM-tDyXaJ5A7_s2ZyDx5MGuwFX4vZeyrMq_oXGhJKKz5B-CXFtXFr2z1BllYBH19-foa4_FWZQ_ETLV)

## Управлять змейкой
[Посмотреть код диаграммы](lab3/ControlTheSnake)
![Управлять змейкой](https://www.plantuml.com/plantuml/png/XLDDJi906Dtt5BEKAy12hc9Y2KqGZQrnY-32A0aR4zmeyGQrK1smZ5TuSoFVSqnJ2KIIqlRxUJzle9jc9vVPrTaW-dc8sbZ0uTDFyS5xWToFKUhTO8iSxx2eU2_zsFWRF_OZTR61DLXnR6Ry15-ivYXOBxbaMIHOnPSr1ntMdUYwdmnYSuGdB3LhEBuXaKKXbkEMIL9s7v6t8cEI7f-VHIurcjuGMWJMtq7JMJyUrlFyjF62Do8vpL1a4B-h2sLJ5mqKjCGTHv923cLG2B1i4AAMG0z_HPGo5PWNA1MASBKV-1j4Va8acN0Cp69hv05BiGV5lAhzUgquVlEOry9p9Uy25vOIPVoj7_c98jqJJnsGq1cJqvH4wa3l2RfYESJJnEdKgwzaaI3vjBoaEG040_u1wyPgM8m7QQnZLAwjK1cU9hq3XWf5oCnosQ6igUAHHH4hGSk63KKELIpneQIdsG6_SoKfoOmx78dIaiR_zErsGftV-X4tEcbsVX5rMUUVwHi0)

## Съесть фрукт:
[Посмотреть код диаграммы](lab3/EatingFood)
![Съесть яблоко](https://www.plantuml.com/plantuml/png/pL8xJiD04Ett55EIajOko5MGS4Ia410slR6H8X4acaXKL700GsnX7BndU7CZdiSO4iW1A7OrchVliwCPnydnPN9rDdDMk00F-425TpGe12MyNck66ciKg3GJlT5KSpHi5g6RJkG0pqD7-FQMv9AdFHf9SXhDYQzGZ9n8W2Uy4jcWrWLFfdSTOM6odOEcyBrjo-jGu0asy279PhJgk0RYxJjbBPflwxAsf9I-_vDXVmgKlR3ckyAzbITCa5a9h0rkDGl_kLeqYoF--x4RnRwVyo6PrO_-yhS-GIP8sNdHV9YeISzFfXFtPT0E1i7M7XYPj2KsEpiHkfuR9-SNRioQY_S9)