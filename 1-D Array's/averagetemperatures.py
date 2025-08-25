temperatures = [10, 13, 16, 18, 19, 21, 29]
temperature_total = 0
for x in range(len(temperatures)):
    temperature_total = temperatures[x] + temperature_total
print(temperature_total/7)