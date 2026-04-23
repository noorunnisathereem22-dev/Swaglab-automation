from utils.config import *

login_test_data = [
    (VALID_USER, VALID_PASSWORD, True),
    (INVALID_USER, VALID_PASSWORD, False),
    (VALID_USER, INVALID_PASSWORD, False),
]