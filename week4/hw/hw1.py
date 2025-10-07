from datetime import datetime

def time_restriction(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.now()
        hour = current_time.hour
        
        if 8 <= hour < 17:
            return func(*args, **kwargs)
        else:
            return "Error: Running outside allowed hours"
    
    return wrapper



@time_restriction
def my_function():
    return "Function executed."

print(my_function())