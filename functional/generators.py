# Genetors: Objeto de creación de secuencias
# Un ejemplo: range()

print(sum(range(1,11)))
print(sum([1,2,3,4,5,6,7,8,9,10]))

def my_range(first=0,last=10,step=1):
    number = first
    while number < last:
        yield number
        # numbers.append(number)
        number += step

print(my_range(1,101))

for n in my_range(1,11):
    print(n)