import inspect

class A1TypeError(TypeError):
    def __init__(self, entity : any, arguments_name : list, expected_arguments_type : str, received_arguments : list):
        error_message = f"The type of argument(s) {arguments_name} of {'class instantiation' if inspect.isclass(entity) else type(entity).__name__} '{entity.__name__}' needs to be type '{expected_arguments_type}'.\n"
        for i in range(len(arguments_name)):
            error_message += (
                f"Current received type of '{arguments_name[i]}': {type(received_arguments[i])}.\n"
            )
        super().__init__(error_message)

class A1ValueError(ValueError):
    def __init__(self, entity : any, arguments_name : list, expected_arguments_value : str, received_arguments : list):
        error_message = f"The value of argument(s) {arguments_name} of {'class instantiation' if inspect.isclass(entity) else type(entity).__name__} '{entity.__name__}' {expected_arguments_value}.\n"
        for i in range(len(arguments_name)):
            error_message += (
                f"Current received value of '{arguments_name[i]}': {received_arguments[i]}"
            )
        super().__init__(error_message)
