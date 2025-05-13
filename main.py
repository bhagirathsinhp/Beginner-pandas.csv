import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250430.csv')

def count_fur_total(color):
    fur_data = data['Primary Fur Color']
    fur = data[fur_data == f"{color}"]
    total_count = fur['Primary Fur Color'].count()
    return total_count

gray_fur = count_fur_total("Gray")
black_fur = count_fur_total("Black")
cinnamon_fur = count_fur_total("Cinnamon")

#Creating a DataFrame:
data_dict = {
    "Fur Color" : ["Gray", "Black", "Cinnamon"],
    "Count" : [f"{gray_fur}", f'{black_fur}', f'{cinnamon_fur}'],
}
print(data_dict)

data_csv = pandas.DataFrame(data_dict)
print(data_csv)
data_csv.to_csv("new_data.csv")
