# Поведенческие модели

## Диаграмма обновления состояния игры "Змейка"

[Посмотреть код диаграммы](lab5/gameprocess)
![Сост](https://www.plantuml.com/plantuml/png/fLDBpjf03Dxd55dslqAoA3SPLMeGaIYjcbJTaanLa43ALOQ1G7WGhc3Vg9-TgA4eg_wB13nZVm_RcMJvf-_vZo_pGFy44JLqfuP_uzVH5UyJEOcuCWZslEHD74HikU2I779RydGXP_3NyKgAUAl7Ushra1wynDi3hKOiI02z8JYZi04QKkMcHbxFDOx6lq1lwIBCSV1pbiwJy4Ed2WAKfwK3dYiToG6lXChgurkOPiWxa7iBmZ2YXsIm1RpgeTf0dDTIeBHS6aqHvfFQSo2i4LSnwjCfiCJMKSzHSG6V-6juJGvi-InP37nW1CYkxrG3JTlHjb3zRrjGciopHCdWf8SQKi0C2Y_s1w-ARDGAvcYuGEvUA-vSAkJYSphjkg3zhkLIPzaf6_3P_dNxmjbgFdZ5zzDGnitZpaltGB3gITIuWlBorRIM54yRqU3H8VITau0tT1w81sEZWhtQn1gBN2u4n1kr00gsOversmizhtlD_VBRJcAMV_tsFwI8RsoxkUouUZyttleT36iIQNjqdKqdWgtiiim73xeN1menGQry-C4V)

## Диаграмма определение победы/поражения, счётчик очков и состояния выхода из игры

[Посмотреть код диаграммы](lab5/hodigri)
![[ходигры]](https://www.plantuml.com/plantuml/png/pLJ1RjD04BtxAtAaDyx9WVx92ebKZHGA8a5S4nkHeWQY_icoiPkjdJg_CFD7l7sR9J4o73YWIethcPrvy-RDhBFBsVprX_d7jzECBzbGl3o9ro_uRwN1SoSsMBenCBQwqBjHDjH2bvgBHMmhJcgn1gzMLo59rtHlfQLJ3hh0qm6jWasadUnXF2BH0qssFAaGbshrekbdb2-a3fNxIS2nqdlDaUeZgnQlTJWdf7avoZvTJwRZmOlOJGYnHFI0GCIhYy5aXjDIx4Ks60pbWEG6fLQHlLG6WGxECiBd9eQ0vuuyBC0gs9iHyYTNm0AiFD2FZ5eQgk7rbjNcr-ERKprK1CYFOqiUdQnxHPIg8w89VmSgI2Kf35mkElLUIj8q-Wq7hUorw9_Dzq1wF9r18EBaYLGgHb5BP40-P282jUAy34N1_c0CYDqouqdp3WtYtxoPN2LnVWDk8tLaGwREnFkqmfaBOeFvwgWM6oAeBhgBziUKxjQSxKnAMPvjgCUFOqwpWQ5tydZ6zUyzEWvfn-jbKNeDLw2GKwsYhqr6Eqfu6pcdorWSAPA3IuF_rP7XEoXYf_JhQNLQRWEbUeZUfCzi_kxzlz27ZQNYv55gy_owI62T9JEov_LVmW3zOFq_vl31KqhLmnbFVgTErp2Lm1qpSGJWs-WQzIn-t5P2N28tVD1_0W00)

## Диаграмма обработки столкновения змейки с самой собой и границами

[Посмотреть код диаграммы](lab5/obrabotka)
![Столкновения](https://www.plantuml.com/plantuml/png/nLJ1IiD04BtlL-nD4Fe3FKZ_GsGHzAOUjDvjm7Ye4Bo98Fv2g5cRjcdw2s_-oBVPQApTYC60XoJCp9lt9c-M7LsDZo_7r-TdQa_Z6QdS8SLAxh562QjbWb8c4l6TC9KpnTUhtCXK7UuVwS7WG3DVjw4qdzLWjiBxWFGpFWk3ZGiaXgNGn44pUP18kO4UloBrDbBzZiTBpb70Oe4bKeEC7JdU28m8JTIFLT-_gOKilmxbFS6AmTeNd3kIi62ggT8gZlaja7Cs1-vVIcxTpzU8ehBiPRjTjxMpe7SdLNtzQOTDww4c1JrerUfvgYK39nWtvtBOuXFi3YEtrzdeRtlwmux_qTVG89sj39pOfm-Evce9y7gzcKp9K29p-Rbf6i85tyMBIerEBqvuoxq3)

## Диаграмма последовательности обновления состояния игр

### Пунктирные стрелки в диаграмме последовательностей PlantUML представляют асинхронные сообщения или возврат управления

#### В контексте вашей диаграммы, пунктирные стрелки между "Еда" и "Змейка" и между "Препятствия" и "Змейка" указывают на асинхронные события, которые происходят в ответ на действия змейки, но не блокируют её дальнейшее движение

#### "Еда --> Змейка: Съесть_еду" означает, что когда змейка сталкивается с едой, происходит событие "Съесть_еду", но змейка продолжает своё движение без ожидания завершения этого события

#### "Препятствия --> Змейка: Столкновение_с_препятствием" означает, что при столкновении змейки с препятствием происходит событие "Столкновение_с_препятствием", но это событие не останавливает игровой цикл; оно будет обработано позже

#### Эти стрелки помогают понять, что некоторые действия или проверки могут происходить параллельно с основным потоком выполнения, что важно для асинхронных систем, где множество событий может происходить одновременно

[Посмотреть код диаграммы](lab5/sostojania)
![Последовательность обновления состояния игры](https://www.plantuml.com/plantuml/png/bPHTJi904CVVznIzW1VmmN2JfW4UI108Lfy5uqSC2IyQVL5Yl411rXO1kSBCZVoFTcLATgEGaBBpyPl_p4wfdQH9FpqzRfkaddRx4KteavOyeXpF6MKy92jdqqDOgzxg9PqqeaTwutFAgiO7MY5sGH-xZdkQxvecIBUquJ4FUO0QCofuR4oeUdHmz5lqCA8dUAx5owEO2Z7pXUXldILfSwlE_P1ihGw45_1pcZj6xfoQerEgB3JaerYQg_moJ9q3JRUxtPuJZQxnNSHyHGNgBas4JsWgdhvUWOTAH2rXNGDYLNU25c8boqEv4sdqxWZ-53U4IIdRuWbVBAs9NXpMuX2AD0h7zuYs8a0GbkTs-1QuWPggNu9teFjAslWWA5H8pK0DhsXV3RAX6ZYl_hoBFNlXIrcVCi9FLs_HCqrBH26J1i3bybXTlDhyu2OAJH9fAf6KbqGgr59RZ46oWMrs6iRyZ-kYOhYodp7m3KdFcMaq_U-gjikEQKlWGdM4Asbgq8b_nYy0)

## Документация к обновления состояния игры "Змейка"

### Эта схема состоит из двух основных состояний: "Игра" и "Играет", которые представляют основной игровой процесс

* _Описание схемы состояний_:

1. "Игра" - начальное состояние, отображающее процесс инициализации игры и переход к режиму игры.
2. "Играет" - основное состояние, описывающее игровой процесс, включая движение змейки, проверку столкновений, обновление яблока, рост змейки, генерацию препятствий и завершение хода.

* _Описание взаимодействия состояний_:
Игра начинается с инициализации, переходя в режим "Играет" после старта игры.
В режиме "Играет" происходит последовательный процесс: движение змейки, проверка столкновений (самой с собой и границами), обновление яблока, рост змейки, генерация нового яблока, генерация препятствия, завершение хода и начало нового хода.
Если происходит столкновение, игра переходит к состоянию "КонецИгры", где отображается результат игры.
После завершения игры можно сбросить игру и вернуться к начальному состоянию "Начало".

* _Пример использования_:
Состояние "Обработка столкновений" позволяет игре корректно определить ситуацию, когда змейка сталкивается с препятствием или самой собой, что приводит к завершению игры в состоянии "КонецИгры". Диаграмма последовательности "Обновление состояния игры" показывает процесс от инициализации до завершения игры, подчеркивая важность ввода пользователя, обновления состояния и проверки условий для завершения игры.

## Диаграмма состояний "Определение победы/поражения, счётчик очков и состояния выхода из игры"

### Эта диаграмма состояний представляет логику определения исхода игры, учета очков и возможности выхода из игры

* _Инициализация игры_:
  Игра начинается с начального состояния "Игра", где система проверяет все необходимые условия для продолжения игрового процесса.

* _Проверка состояния_:
  В состоянии "Проверка состояния" игра оценивает текущее положение игрока и игровые условия, чтобы определить, продолжается ли игра, достигнута ли победа или наступило поражение.

* _Обновление положения и счета_:
  Если игра продолжается, система переходит к "Обновлению положения", где может произойти изменение счета, например, если была съедена еда. После обновления счета система возвращается к "Проверке состояния".

* _Конец игры_:
  В случае достижения условий победы или поражения, игра переходит в состояние "Конец игры", где игровой процесс завершается.

* _Выход из игры_:
  В любой момент игры можно выйти из игры, нажав кнопку выхода, что приведет к немедленному завершению игровой сессии.

Эта диаграмма помогает разработчикам и аналитикам понять, как игра реагирует на различные события и какие переходы между состояниями возможны в процессе игры. Она также служит в качестве визуального справочника для улучшения и отладки игрового процесса. Если вам нужны дополнительные изменения или уточнения, пожалуйста, сообщите мне.

## Схема состояния "Обработка столкновений змейки с самой собой и границами"

### Эта схема состояния представляет процесс обработки столкновений змейки с самой собой и границами в игре "Змейка"

* _Начальное состояние (Столкновение не обнаружено)_:
В этом состоянии игра находится до момента обнаружения столкновения змейки с бомбой.

* _Конечное состояние (Обнаружение столкновения)_:
Игра обнаруживает столкновение змейки с самой собой или границами поля в текущем расположении.

## Диаграмма последовательности "Обновление состояния игры"

### Эта диаграмма последовательности иллюстрирует процесс обновления состояния игры в игре "Змейка"

* _Инициализация игры_:
Игра начинается с инициализации, включая установку начального состояния, загрузку игровых объектов и отображение начального экрана.

* _Получение ввода пользователя_:
Игра ожидает ввода пользователя, включая управление змейкой (нажатие клавиш для движения).

* _Обновление состояния игры_:
После получения ввода пользователя, игра обновляет состояние в соответствии с действиями пользователя и текущим состоянием игрового процесса.

* _Отображение изменений на экране_:
После обновления состояния игры, происходит отображение всех изменений на экране, включая новое положение змейки, еды и т. д.

* _Проверка условий завершения игры_:
Игра проверяет условия, при которых игра может завершиться (например, столкновение змейки с препятствием(самой собой или границами поля) или съедание определенного количества яблок).

* _Завершение игры_:
Если условия завершения игры выполнены, игра завершается, и пользователю предоставляется информация о результате игры (победа/поражение, счёт, время и рекордное время).
