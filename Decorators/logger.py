
from datetime import datetime
import os


def get_path(log_path):
    data = datetime.now()
    def log(func):
        def wrapper(*args, **kwargs):
            args_str = ', '.join(args)
            kwargs_str = str(kwargs)
            _path = os.path.abspath(log_path)
            with open('log.txt', 'w', encoding= "utf-8") as f:
                f.write(str(data) + "\t")
                f.write(str(func.__name__)+"\t")
                f.write(args_str + kwargs_str + _path)
            return func(*args, **kwargs)
        return wrapper
    return log


@get_path ("log.txt")
def example(*a, **b):
    pass

if __name__ == "__main__":
    example("значение 1 ","значение 2 ", ключ="значение")
