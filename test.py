import logging

def using_log(func):
    def wrapper():
        logging.warning('%s is running' % func.__name__)
        return func()


    return wrapper

def fool():
    print('i am a fool')

bar=using_log(fool)
bar()