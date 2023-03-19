class InfoMessage:  #готов
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories) -> None:        
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self):
        return f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.'

class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65     #Один шаг в метрах
    M_IN_KM = 1000      #Метров в километре

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:     
        self.action = action   
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:    #готов
        """Получить дистанцию в км."""                                          
        return self.action * self.LEN_STEP / self.M_IN_KM                                       
    
    def get_mean_speed(self) -> float:  #готов
        """Получить среднюю скорость движения."""                               
        return self.get_distance() / self.duration                    

    def get_spent_calories(self) -> float:  #готов
        """Получить количество затраченных калорий."""                          
        pass                                                            

    def show_training_info(self) -> InfoMessage:    #не готов
        """Вернуть информационное сообщение о выполненной тренировке."""        
        return InfoMessage.get_message()                                              

class Running(Training):    #готов
    """Тренировка: бег."""
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""                          
        
        return (self.coeff_calorie_1 * self.get_mean_speed() - self.coeff_calorie_2) * self.weight / self.M_IN_KM * self.duration

class SportsWalking(Training):  #готов
    """Тренировка: спортивная ходьба."""                                        
    coeff_calorie_3 = 0.035
    coeff_calorie_4 = 0.029  
                                        
    def __init__(self, height):
        self.height = height 

    def get_spent_calories(self):
        """Получить количество затраченных калорий."""    
        return (self.coeff_calorie_3 * self.weight + (self.get_mean_speed() ** 2 // self.height) * self.coeff_calorie_4 * self.weight) * self.duration

class Swimming(Training):   #готов
    """Тренировка: плавание."""

    LEN_STEP = 1.38     #Один гребок при плавании

    def __init__(self, length_pool, count_pool) -> None:
        self.length_pool = length_pool   #Длина бассейна
        self.count_pool = count_pool     #Сколько раз переплыл бассейн
    
    def get_spent_calories(self): 
        """Получить количество затраченных калорий."""                      
        return (self.get_mean_speed() + 1.1) * 2 * self.weight  #проверить! берёт из Swimming или из Training (по идее должен братье сли судить по дереву наследования)

    def get_mean_speed(self) -> float:  
        """Получить среднюю скорость движения при плавании."""               
        return self.length_pool * self.count_pool / self.M_IN_KM


def read_package(workout_type: str, data: list) -> Training: #готов
    """Прочитать данные полученные от датчиков."""

    if workout_type == 'SWM':
        return Swimming(data)
    
    elif workout_type == 'RUN':
        return Running(data)    
    
    return SportsWalking(data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
