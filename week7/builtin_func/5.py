def all_true(tup):
    return all(tup)

n = int(input("Enter the number of elements: "))
values = []

for i in range(n):
    value = input("Enter True or False: ").strip().lower() == 'true'
    values.append(value)

tup = tuple(values)
print(all_true(tup))

