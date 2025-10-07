from datetime import datetime

def restrict_hours(start=9, end=17):
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_hour = datetime.now().hour
            
            if start <= current_hour < end:
                return func(*args, **kwargs)
            else:
                return f"Error: Function can only run between {start}:00 and {end}:00"
        
        return wrapper
    return decorator


@restrict_hours(start=9, end=17)
def do_work():
    print("Working...")
    return "Work completed successfully"

print(do_work())