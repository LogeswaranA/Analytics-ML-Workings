#What it does
#The yield keyword is used instead of return. When yield is called, the function pauses, saving its state, and yields a value. The next time the generator is called, it resumes from where it left off.

def fibonacci_series(limit):
    a,b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for number in fibonacci_series(5):
    print(number)
