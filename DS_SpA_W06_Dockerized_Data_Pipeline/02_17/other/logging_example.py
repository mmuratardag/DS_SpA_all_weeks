import logging # The first thing import statements do is to look for a python file in the current directory with the name that provide, in this case logging.py

logging.basicConfig(level=logging.ERROR, filename='debug.log') # There are different levels of logs and we can decide which events to log
# Different levels are DEBUG, INFO, WARNING, ERROR, CRITICAL (ordered list)

# logging is important for error handling / for debugging / to understand where our code failed and what it did
# we want to be able to separate different levels of logs so that we can filter information. If the application crashes we do not necessarily want to scan through 
# all the INFO logs, but we want to receive information about the ERROR logs or CRITICAL logs


def factorial(n=10):
    """Calculates factorials with log messages."""
    i = 1
    factorial = 1
    while i < n:
        logging.info('starting iteration {}'.format(i))
        factorial *= i
        logging.debug('new factorial: {}'.format(factorial))
        i += 1
    logging.warning('Final result: {}'.format(factorial))
        

if __name__ == '__main__':
    logging.warning('this is a warning message')
    logging.info('this is a info message')
    factorial(10)
    logging.critical('Factorial calculation ended')