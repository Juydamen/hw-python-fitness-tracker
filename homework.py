class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 LEN_STEP: float,
                 ) -> None:     
        self.action = action   
        self.duration = duration
        self.weight = weight
        self.LEN_STEP = LEN_STEP
        self.M_IN_KM = 1000


    def get_distance(self) -> float:
        """Получить дистанцию в км."""                          #готов
        return self.action * self.LEN_STEP / self.M_IN_KM                                       
    
    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""               #готов
        return Training.get_distance() / self.duration                    

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""          #готов
        pass                                                            

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""        #корекция
        return InfoMessage                                              


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""          #готов
        coeff_calorie_1 = 18
        coeff_calorie_2 = 20
        return (coeff_calorie_1 * Training.get_mean_speed - coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""                    #готов
    def __init__(self, height):
        self.height = height 
    def get_spent_calories(self):
        """Получить количество затраченных калорий."""          
        coeff_calorie_3 = 0.035
        coeff_calorie_4 = 0.029
        return (coeff_calorie_3 * self.weight + (Training.get_mean_speed() ** 2 // self.height) * coeff_calorie_4 * self.weight) * self.duration

class Swimming(Training):
    """Тренировка: плавание."""
    def get_spent_calories(self, length_pool, count_pool):
        """Получить количество затраченных калорий."""  
    


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    pass


def main(training: Training) -> None:
    """Главная функция."""
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

#expected = 'Тип тренировки: Swimming; Длительность: 1.000 ч.; Дистанция: 75.000 км; Ср. скорость: 1.000 км/ч; Потрачено ккал: 80.000.'