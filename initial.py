# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     new_data = [i.strip('\n') for i in data]
#     print(new_data)

import csv

with open("weather_data.csv") as weather_data:
    data = csv.reader(weather_data)

    temperature = []

    # for r in data:
    #     temperature.append(r[1])
    # temperature = [int(r) for r in temperature[1:]]
    # print(temperature)

    for row in data:
        if row[1] != 'temp':
            temperature.append(int(row[1]))

    print(temperature)


import pandas

data = pandas.read_csv('weather_data.csv')
print(data)
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.temp)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print((monday.temp[0] * 9/5 ) + 32)

#Create a Dataframe:
data_dict = {
    'students': ['Amy', "James", 'Angela'],
    'score' : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv('new_data.csv')