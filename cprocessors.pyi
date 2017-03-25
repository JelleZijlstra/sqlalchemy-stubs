# Stubs for sqlalchemy.cprocessors (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

def int_to_boolean(*args, **kwargs): ...
def str_to_date(*args, **kwargs): ...
def str_to_datetime(*args, **kwargs): ...
def str_to_time(*args, **kwargs): ...
def to_float(*args, **kwargs): ...
def to_str(*args, **kwargs): ...

class DecimalResultProcessor(object):
    def __init__(self, *args, **kwargs): ...
    def process(self, *args, **kwargs): ...

class UnicodeResultProcessor(object):
    def __init__(self, *args, **kwargs): ...
    def conditional_process(self, *args, **kwargs): ...
    def process(self, *args, **kwargs): ...
