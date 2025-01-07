temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

temperatures_hot = list(filter(lambda x: x > 28, temperatures))
print(sorted(set(temperatures_hot)))
low_temperature = max(temperatures_hot)
max_temperature = min(temperatures_hot)
avg_temperature = (sum(temperatures_hot) / len(temperatures_hot))

print(
    f'Высокая температура: {low_temperature}\nНизкая температура: {max_temperature}\nСредняя температура:'
    f' {avg_temperature:.0f}'
)
