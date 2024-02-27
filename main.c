#include <iostream>
#include <conio.h>
#include <vector>
#include <cstdlib>
#include <ctime>

using namespace std;

// Структура для представления координат клетки на игровом поле
struct Point {
    int x, y;
    Point(int x=0, int y=0): x(x), y(y) {}
};

int main() {
    const int width = 20; // Ширина игрового поля
    const int height = 20; // Высота игрового поля
    bool game_over = false; // Флаг окончания игры

    vector<Point> snake; // Вектор для хранения координат змейки
    Point food; // Позиция еды

    // Инициализация змейки с начальной длиной 3 клетки
    snake.push_back(Point(width/2, height/2));
    snake.push_back(Point(width/2, height/2 + 1));
    snake.push_back(Point(width/2, height/2 + 2));

    // Генерация случайной позиции для еды
    srand(time(NULL));
    food.x = rand() % width;
    food.y = rand() % height;

    // Основной игровой цикл
    while (!game_over) {
        system("cls"); // Очистить экран

        // Вывод игрового поля
        for (int y = 0; y < height; ++y) {
            for (int x = 0; x < width; ++x) {
                // Выводим границы поля
                if (y == 0 || y == height-1 || x == 0 || x == width-1)
                    cout << "#";
                else if (x == food.x && y == food.y)
                    cout << "@"; // Выводим еду
                else {
                    bool is_snake = false;
                    for (const Point &p : snake) {
                        if (p.x == x && p.y == y) {
                            cout << "O"; // Выводим змейку
                            is_snake = true;
                            break;
                        }
                    }
                    if (!is_snake)
                        cout << " ";
                }
            }
            cout << endl;
        }

        // Движение змейки (пока только вправо)
        Point new_head = snake.back();
        new_head.x++;
        snake.push_back(new_head);
        snake.erase(snake.begin()); // Удаляем хвост змейки

        // Проверка столкновения с стеной или самим собой
        if (new_head.x == 0 || new_head.x == width-1 || new_head.y == 0 || new_head.y == height-1)
            game_over = true;
        for (size_t i = 0; i < snake.size()-1; ++i) {
            if (new_head.x == snake[i].x && new_head.y == snake[i].y)
                game_over = true;
        }

        // Проверка поедания еды
        if (new_head.x == food.x && new_head.y == food.y) {
            snake.push_back(new_head); // Растем
            food.x = rand() % width; // Сгенерировать новую позицию для еды
            food.y = rand() % height;
        }

        // Задержка для плавности анимации
        _sleep(100); // На Windows используем _sleep, на Linux - usleep

        // Если клавиша нажата (кроссплатформенная функция)
        if (_kbhit()) {
            char key = _getch();
            if (key == 'q')
                game_over = true; // Выход из игры
        }
    }

    cout << "Game Over!" << endl;
    
    return 0;
}
