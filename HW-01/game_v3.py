def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    
def game_core_v3(number: int = 1) -> int:
    """ Код начинает угадывать с 50, то есть с середины заданного отрезка.
        Затем, когда становится понятно, больше или меньше загаданное число, 
        одним из концов отрезка становится число из последней попытки, а вторым 
        соответственно  больший или меньшийконец отрезка. Следующая поптыка 
        угадать - середина нового отрезка.

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: number of attempts
    """
    count = 1
    predict = 50
    beggining = 1
    ending = 100

    while number != predict:
        count += 1
        if number > predict:
            beggining = predict + 1
            predict = (ending+beggining) // 2 
        elif number < predict:
            ending = predict - 1
            predict = (ending+beggining) // 2

    return count

    
import numpy as np

# RUN
print('Run benchmarking for game_core_v3: ', end='')
if __name__ == '__main__':
    score_game(game_core_v3)