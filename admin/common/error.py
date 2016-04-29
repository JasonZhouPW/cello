CODE_OK = 200
CODE_FAIL = 400
CODE_NOT_FOUND = 404
CODE_INVALID_OPERATION = 405
CODE_INVALID_PARAM = 406
CODE_ALREADY_EXIST = 409

status_response_ok = {
    "status": "OK",
    "code": CODE_OK,
    "error": "",
    "data": "",
}

status_response_fail = {
    "status": "FAIL",
    "code": CODE_FAIL,
    "data": "",
}

errors = {
    'UserAlreadyExistsError': {
        'message': "A user with that username already exists.",
        'status': CODE_ALREADY_EXIST,
        'extra': "NA",
    },
    'ResourceDoesNotExist': {
        'message': "A resource with that ID no longer exists.",
        'status': CODE_NOT_FOUND,
        'extra': "NA",
    },
    'InvalidParams': {
        'message': "Not valid param is given",
        'status': CODE_INVALID_PARAM,
        'extra': "NA",
    },
    'InvalidOperations': {
        'message': "Invalid operation method is given",
        'status': CODE_INVALID_OPERATION,
        'extra': "NA",
    },
}