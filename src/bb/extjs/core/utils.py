from time import time

class ramcache(object):
    """ decorator to cache a function into ram
        arguments should be hashable
    """
    
    def __init__(self, expire):
        """ expire in miliseconds
        """
        self.expire = expire
        self.cache = dict()
    
    def __call__(self, func):
        def wrapper(*args, **kw):
            key = hash((args, tuple(kw),))
            cache = self.cache.setdefault(key, dict(last=0,
                                                    result=None))
            if cache['last'] + self.expire < time():
                cache['last'] = time()
                r = func(*args, **kw)
                cache['result'] = r
                return r
            else:
                return cache['result']
        return wrapper