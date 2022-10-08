

numbers = [5, 20, 30, 35, 50]

insval = int(input('Enter the insertion value: '))

if (insval <= numbers[0]):
    numbers.insert(0, insval)

for i in range(len(numbers) - 1):

    if (numbers[i] < insval <= numbers[i + 1]):
        numbers.insert((i + 1), insval)

if (insval > numbers[len(numbers) - 1]):
    numbers.insert((len(numbers)), insval)


print(numbers)
