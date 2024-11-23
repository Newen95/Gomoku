def send_message(message):
    return f"{message}"

def send_debug(debug_info):
    return f"DEBUG {debug_info}"

def send_error(error_message):
    return f"ERROR {error_message}"

def send_unknown(unknown_message):
    return f"UNKNOWN {unknown_message}"

def send_ok(ok_message):
    return f"OK {ok_message}"