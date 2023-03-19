class InfoMessage:  
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type, duration, distance, speed, calories) -> None:        
        self.training_type = training_type
        self.duration = '%.3b' % duration
        self.distance = '%.3b' % distance
        self.speed = '%.3b' % speed
        self.calories = '%.3b' % calories

    def get_message(self):
        return f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; Потрачено ккал: {self.calories}.'
    
class Training:
    """Базовый класс тренировки."""

    LEN_STEP = 0.65     
    M_IN_KM = 1000      

    def __init__(self, action: int, duration: float, weight: float) -> None:     
        self.action = action   
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:   
        """Получить дистанцию в км."""                                          
        return self.action * self.LEN_STEP / self.M_IN_KM                                       
    
    def get_mean_speed(self) -> float:  
        """Получить среднюю скорость движения."""                               
        return self.get_distance() / self.duration                    

    def get_spent_calories(self) -> float:  
        """Получить количество затраченных калорий."""                          
        pass                                                            

    def show_training_info(self) -> InfoMessage:    
        """Вернуть информационное сообщение о выполненной тренировке."""        
        return InfoMessage.get_message(self)                                        

class Running(Training):
    """Тренировка: бег."""

    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def __init__(self, action: int, duration: float, weight: float) -> None:
        super().__init__(action, duration, weight)    

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""                          
        
        return (self.coeff_calorie_1 * self.get_mean_speed() - self.coeff_calorie_2) * self.weight / self.M_IN_KM * (self.duration * 60)
    
class SportsWalking(Training):  
    """Тренировка: спортивная ходьба."""                                        
    coeff_calorie_3 = 0.035
    coeff_calorie_4 = 0.029  

    def __init__(self, action: int, duration: float, weight: float, height) -> None:
        super().__init__(action, duration, weight) 
        self.height = height  

    def get_spent_calories(self):
        """Получить количество затраченных калорий."""    
        return (self.coeff_calorie_3 * self.weight + (self.get_mean_speed() ** 2 // self.height) * self.coeff_calorie_4 * self.weight) * (self.duration * 60)

class Swimming(Training):
    """Тренировка: плавание."""

    LEN_STEP = 1.38     #Один гребок при плавании

    def __init__(self, action: int, duration: float, weight: float, length_pool, count_pool) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool   #Длина бассейна
        self.count_pool = count_pool    
    
    def get_spent_calories(self): 
        """Получить количество затраченных калорий."""                      
        return (self.get_mean_speed() + 1.1) * 2 * self.weight  #проверить! берёт из Swimming или из Training (по идее должен братье сли судить по дереву наследования)

    def get_mean_speed(self) -> float:  
        """Получить среднюю скорость движения при плавании."""               
        return self.length_pool * self.count_pool / self.M_IN_KM / self.duration

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    package_2={'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    return package_2[workout_type](*data)
    
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
