# 1
class StringTool:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input().strip()

    def printString(self):
        print(self.s.upper())


# 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# 4
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        from math import sqrt
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# 5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough funds")
        elif amount <= 0:
            print("Withdraw must be positive")
        else:
            self.balance -= amount


# 6
def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def filter_primes_with_filter(nums):
    return list(filter(lambda x: is_prime(x), nums))


# 7
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 8
def f_to_c(f):
    return (5 / 9) * (f - 32)

# 9
def solve(numheads, numlegs):
    r = (numlegs - 2 * numheads) // 2
    c = numheads - r
    return {"rabbits": r, "chickens": c}

# 10
def filter_prime(nums):
    return [n for n in nums if is_prime(n)]

# 11
def all_permutations(s):
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

# 12
def reverse_words(sentence):
    parts = sentence.split()
    return ' '.join(parts[::-1])

# 13
def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

# 14
def spy_game(nums):
    pattern = [0, 0, 7]
    j = 0
    for n in nums:
        if n == pattern[j]:
            j += 1
            if j == len(pattern):
                return True
    return False

# 15
def sphere_volume(r):
    from math import pi
    return (4/3) * pi * (r**3)

# 16
def unique_list(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

# 17
def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

# 18
def histogram(numbers):
    for n in numbers:
        print('*' * n)

# 19
def play_guess():
    import random
    name = input("Hello! What is your name?\n")
    secret = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    tries = 0
    while True:
        guess = int(input("Take a guess: "))
        tries += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {tries} tries!")
            break


# 20+
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"},
]

# 20
def is_good_movie(movie):
    return movie["imdb"] > 5.5

# 21
def high_score_movies(mvs):
    result = []
    for m in mvs:
        if is_good_movie(m):
            result.append(m)
    return result

# 22
def movies_by_category(mvs, category):
    return [m for m in mvs if m["category"] == category]

# 23
def average_imdb(mvs):
    total = 0
    for m in mvs:
        total += m["imdb"]
    return total / len(mvs)

# 24
def average_imdb_by_category(mvs, category):
    sub = movies_by_category(mvs, category)
    return average_imdb(sub)

