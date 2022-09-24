



keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

every = {}
for key in keys:
    for value in values:
        every[key] = value
        values.remove(value)
        break

print("Resultant dictionary :" + str(every))








