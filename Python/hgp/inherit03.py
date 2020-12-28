class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("### create Exception ###")
    def __str__(self):
        return "ERROR!!!!"

raise CustomException