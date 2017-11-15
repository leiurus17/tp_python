from network_error_exception import NetworkError

try:
    raise NetworkError("Bad Hostname")
except NetworkError, e:
    print e.args