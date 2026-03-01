# Fizz Buzz Game
pre = 0
for i in range(1, 101):
    new_no = i+pre

    if new_no % 3 == 0 and new_no % 5 == 0:
        print("Fizz Buzz")
    elif new_no % 3 == 0:
        print("Fizz")
    elif new_no % 5 == 0:
        print("Buzz")
    else:
        print(new_no)

    pre = i

# Movies Budget analyzer

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

budget=0
for i in movies:
    budget=budget+i[1]

average=budget/len(movies)
print(f'Average Budget is: {average}')

num=0
print("\n Movies with higher budget:")
for i in movies:
    if i[1]>average:
        diff=i[1]-average
        print(f'{i[0]} is higher then average by: {diff} ')
        num+=1
print(f'Total movies higher than average : {num}')
