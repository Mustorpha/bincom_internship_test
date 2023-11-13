#!/usr/bin/python3
#_*_ encoding: utf-8 _*_

# The given dataset
DRESS_COLOR_USAGE = {
    "monday":
        ["green", "yellow", "green", "brown", "blue", "pink", "blue", "yellow", "orange", "cream", "orange", "red", "white", "blue", "white", "blue", "blue", "blue", "green"],
    "tuesday":
        ["arsh", "brown", "green", "brown", "blue", "blue", "blew", "pink", "pink", "orange", "orange", "red", "white", "blue", "white", "white", "blue", "blue", "blue"],
    'wednesday':
        ["green", "yellow", "green", "brown", "blue", "pink", "red", "yellow", "orange", "red", "orange", "red", "blue", "blue", "white", "blue", "blue", "white", "white"],
    "thursday":
        ["blue", "blue", "green", "white", "blue", "brown", "pink", "yellow", "orange", "cream", "orange", "red", "white", "blue", "white", "blue", "blue", "blue", "green"],
    "friday":
        ["green", "white", "green", "brown", "blue", "blue", "black", "white", "orange", "red", "red", "red", "white", "blue", "white", "blue", "blue", "blue", "white"]
}

def get_frequency(color: str) -> int:
    """ Calculates the frequency of a color from the dataset """

    total = 0
    for colors in DRESS_COLOR_USAGE.values():
        total += colors.count(color)
    return total

# dictionary containing each color in the dataset with their frequency
color_frequency = {
    'arsh': get_frequency('arsh'),
    'blue': get_frequency('blue'),
    'brown': get_frequency('brown'),
    'cream': get_frequency('cream'),
    'green': get_frequency('green'),
    'orange': get_frequency('orange'),
    'pink': get_frequency('pink'),
    'red': get_frequency('red'),
    'white': get_frequency('white')
}

############ QUESTION 1 ############
def get_mean_color() -> str:
    """ Returns the mean color from the dataset """

    total = sum(color_frequency.values())
    avg = float((f"{total/9:.2f}"))

    for colors in color_frequency:
        if color_frequency[color] >= int(avg):
            return color
    return None

############ QUESTION 2 ############
def get_max_worn():
    """ Returns the maximum worn shirt color from the dataset """

    max_color = max(color_frequency, key=lambda x: color_frequency[x])
    return max_color


############ QUESTION 3 ############
def get_median_color() -> str:
    """ Returns the median color from the dataset """

    total = sum(color_frequency.values())
    median = float((f"{total/2:.2f}"))

    for colors in color_frequency:
        if color_frequency[color] >= int(median):
            return color
    return None

############ QUESTION 4 ############
def get_color_variance() -> float:
    """ Calculates the variance of the color """

    total = sum(color_frequency.values())
    mean = float((f"{total/9:.2f}"))

    mean_deviation_squared = [(count - mean)**2 for count in color_frequency.values()]
    total = sum(mean_deviation_squared)
    variance = total/9
    return variance

############ QUESTION 5 ############
def random_probability(color):
    return color_frequency[color]/sum(color_frequency.values())

############ QUESTION 6 ############
def create_table(connection):
    import psycopg2 #import the module only when the function is called

    try:
        connection = psycopg2.connect(
            host="your_host",
            database="your_database",
            user="your_user",
            password="your_password"
        )

        cursor = connection.cursor()
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS sample_data (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
        '''
        connection.commit()
        insert_query = '''
            INSERT INTO sample_data (name, age)
            VALUES (%s, %s)
        '''
        cursor.execute(create_table_query)

        for color in color_frequency:
            cursor.execute(insert_query, (color, color_frequency[color]))
            connection.commit()
        cursor.close()
        connection.cloe()
    except Exception as err:
        print("An unexpected error occured")
        print(err)

############ QUESTION 7 ############
def recursive_search(num_list, num_unknown, index=0):
    if index < len(lst):
        if num_list[index] == num_unknown:
            return index
        else:
            return recursive_search(num_list, num_unknown, index + 1)
    else:
        return None


############ QUESTION 8 ############
def binary_to_decimal():
    import random
    binary_digit = ''.join(random.choice('01') for _ in range(4))
    decimal_number = int(binary_digit, 2)
    return decimal_number

############ QUESTION 9 ############
def sum_50_fibonacci(n):
    fib = [0, 1]

    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    total = sum(fib)
    return total