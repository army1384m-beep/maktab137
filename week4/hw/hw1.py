def time_restriction(start_hour=8, end_hour=17):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_hour = datetime.now().hour
            if start_hour <= current_hour < end_hour:
                return func(*args, **kwargs)
            else:
                return f"Error: Running outside allowed hours ({start_hour}:00 - {end_hour}:00)"
        return wrapper
    return decorator


@time_restriction(9, 18)  
def my_function():
    return "Function executed."