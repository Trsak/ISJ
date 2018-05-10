#!/usr/bin/env python3
class TooManyCallsError(Exception):
    """
    Custom error message
    """
    pass


class Log:
    """
    Class used for logging
    """

    def __init__(self, file):
        """
        Opens log file for reading.
        :param file: log file path
        """
        self.file = open(file, "w")

    def __enter__(self):
        """
        Called using with statement, writes "Begin" to log file.
        :return: self Log object
        """
        self.file.write("Begin\n")
        return self

    def logging(self, message):
        """
        Writes message to log file.
        :param message: message to log
        """
        self.file.write("%s\n" % message)

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the runtime context related to this object.
        Writes "End" to log file and closes it.
        :param exc_type: exit type
        :param exc_val: exit value
        :param exc_tb: exit traceback
        """
        self.file.write("End\n")
        self.file.close()


def limit_calls(max_calls=2, error_message_tail='called too often'):
    """
    Limits calls of function, raises error when limit is exceeded
    :param max_calls: maximum of allowed function calls
    :param error_message_tail: error message
    :return: decorator for called function
    """

    def decorator(called_function):
        """
        Decorator used to count calls for functions
        :param called_function: called function
        :return: call function to count number of calls
        """

        def call(*args, **kwargs):
            """
            Counts how many times was function called.
            If max_calls is exceeded, raises TooManyCallsError.
            :param args: called function arguments
            :param kwargs: called function keyword arguments
            :return:
            """
            if call.count >= max_calls:
                specific_error_message = "function \"%s\" - %s" % (called_function.__name__, error_message_tail)
                raise TooManyCallsError(specific_error_message)

            call.count += 1
            return called_function(*args, **kwargs)

        call.count = 0
        return call

    return decorator


def ordered_merge(*args, selector=None):
    """
    Takes iterable elements and returns elements selected by selector.
    :param args: iterable elements
    :param selector
    :return: selected elements
    """
    if selector is None:
        selector = []

    objects = []
    result = []

    for argument in args:
        objects.append(list(argument))

    for select in selector:
        result.append(objects[select][0])
        objects[select].pop(0)

    return result
