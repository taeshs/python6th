class CustomException(Exception):
    def __init__(self, message):
        self.message = message


try:
    raise CustomException("This is a Custom Exception")
except CustomException as e:
    print(f"Error : {e.message}")