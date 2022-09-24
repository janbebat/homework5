


numbers = [12, 75, 150, 180, 145, 525, 50]

result_number = []


for no in numbers:


    if no > 500:
        break

    if no > 150:
        continue

    if no % 5 == 0:
        result_number.append(no)

print(result_number)

