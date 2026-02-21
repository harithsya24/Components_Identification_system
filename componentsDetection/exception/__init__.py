import sys
import traceback

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return f"{str(error)}"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in python script "
        f"[{file_name}] at line [{line_number}] "
        f"with error message [{str(error)}]"
    )
    
class AppException(Exception):
    def __init__(self, error_message, error_detail):
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message

