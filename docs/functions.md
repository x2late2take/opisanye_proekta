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
![Диаграмма хода игры](https://www.plantuml.com/plantuml/png/fLHTJi9047xVKsnuvmg6EtW0iYahDfH2skN161C5VuoIyE23lXZIw04gfk57X2lCtCYPR43gsZI4X7HPlk-R-JhxBRNOgCZqse48z8cHfYCZltbgPCEFj6VyJYZYbXzsLQJQigkybchgOtCMQCcm2fk15iepdKZ265RmXKEOqZg15FkGyLw8BLF22tpY9QJoN4ZPYxMdOYqhy4hiErRWi0upfk2W8bKiTv6SuWtMN0Scr65aTLDOKiCvBAZztAeTLgv6WW-GuHMo6g-v9oomRvKx6Bnle9nwJ9NvFJDQPxO6qNa4i81l2z4wWum0-a0AIzejwIk17xyca_zLaB22dic6Va1xEtNUuwqrKeSrat5KPkBfh_8G6tmS6JtvC9Wt8T68YvQv61S9SswU8RLUy9vm9qrvtCq3hF1c-xQivgOmnG77c9gcctGuJ2VDv94dOr6UTSfqJYW3-6ZhE4nn8KJHFPBLwb7kGfGmtV2xFp6p8En5x3tokdy59snxrIY9Iicyd72Ky9qGbF3TmnOr7JRud_S7)

## Начать новую игру
[Посмотреть код диаграммы](lab3/NewGame)
![Начать новую игру](https://www.plantuml.com/plantuml/png/lLHTJi9047xlAVeeLu07kGaniOGcYCRM-2f5yKTY7zHeJFmnNc0jh29LkCBCZVncjwKGm0TDD76pEplVp-nCgGRXncwujzLqpCOfqorzqP2xD2H5ATPtKdBYk8P3dm_ul8AiPnhZPa1AiabdTmWc-E_Jk4OJR5AE9Vc9598_IVCfwGnW0_H18nhM45CPWhGWBasU1cCkpeUGxj288r8Lnzbl-4tFNODRaLLWi9oA4e7nYI5GwoNN3v1sHQhak6wP7esh3XyNHXBZUI0aOuvoupsGIJKAWjeK0hnV1zSrjpdYtXG8ZR3XjGeLgoFczGz52r_6U9D7RI5gjbYzI2y2SnWOEYCj9K0jca5NfkalyYxIpvdAOJ3l2tQBvl2th1Cu5csURuj0lDQcNrzHMo9lOhgKWgvj7X7k4NlbU4MXTr0I0zrY_hAx8DpU-Psa7HexwDpvJ-69HB767CaOKIAT-Bi1hnbuWDzB__CHVA0tu8fFbDkKofHW-Yza9ct_ZkpiWpaZmse-BiTPxi1eLv4bFnhV)

## Управлять змейкой
[Посмотреть код диаграммы](lab3/ControlTheSnake)
![Управлять змейкой](https://www.plantuml.com/plantuml/png/nLJDJkf05DxtAMPvUGLONDwaQNBBfKb5GclSGZ4ObQGB5n8N6kCBZCL21HbUuPmtyflJK5bCua8JDyFqpFb-vfiPkaaQZDApazYJYTUc1UseuXbLf6cBSKtQVd7kyvJsF4Qvm48fRNd7yqRXC0nIrQP7ChJbAL_MYrJww2nGV2Nja-7Cfxsqp45giA8vG-lMiYJ3E4ez1PO74Ia1mbB3X1_jKbSgwga_T4VlgBtH1agO6bfH2JsG580lhHBFUSBvtvPA--4049Xg0Qx4U2cIuE2hJybrGrfP8PVK3WDVy1ZHREnc7FHMu8clxOuQwYE8xZHTprJ8dgkZ16N7OiJE79uiy5RQqT4S5JwDHByaur0B1_-Y7cPXd8JmQh7P8OnxCbAO-JOv86zgJ9AU3hq3L8vB1V-3QE0yWaBoNCiLqiXzZfBF4zHU76VmbQp3wJTiM7PKv9RpzBVDo6N7c7E6MYRtjVmvKnYL66lUwNa_YctZeiv17CWRDV2r8ctnzKlnt9gYrmMn_TVu0000)

## Съесть фрукт:
[Посмотреть код диаграммы](lab3/EatingFood)
![Съесть яблоко](https://www.plantuml.com/plantuml/png/fLDRIiD05FtFAl9fjz1ys9qCWYaDr2ecuc-JOaKjvaD4yKCHDp1zZ8sjZbkuTqUUkR4nq1P4MmYPkUUUSnydhJZPEqvE3hgUl7XDkgSFAdX81MbQuZadxKwSAnoctEUh0AWRCi0PxbTHpccC14iBqih554qKij-1VCEb2Jplj1DrGty76Y1oC4qBpi0xGOBURVXHZEYCTCFp_IOzWMt90puNiK8eyRSEeSXofkXJ82FeM4Gqo0pEUO3yg0skMquvur6L28sa4_P-L4H76Z6kLBwej6gr5uxlc_6kkfKsTRrniqul0izyYPnPHLsVLL2XNb2YSJElDUp6L1RYtjPhmc_JCd2qql2Kx2ys8qnXRpzgR-bp8lEPYoKqfp9GnIdknfnlQVg1h5Grh1cdZCN9uT7V94lVb0xbmV-5msuCFmewMxdXaLwH1yRL2b9Qkkt1YDTY3vdfMMb3nroIuIdszhpD5OXs2oZtiNq1)