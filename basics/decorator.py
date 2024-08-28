import time

# def time_decorator(func):
#     def wrapper(*args,**kwargs):
#         start_time = time.time()
#         result = func(*args,**kwargs)
#         end_time = time.time()
#         print(f"Execution time for the function is { end_time - start_time} seconds")
#         return result
#     return wrapper

# @time_decorator
# def calculate_sum(n):
#     return (sum(range(n)))


# print(calculate_sum(5))

def time_decorator(func):
    def wrappper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f"Execution time for the function is {end_time - start_time} seconds")
        return result
    return wrappper

@time_decorator
def calculate_avg(n):
    return (n**2)

print(calculate_avg(5))
