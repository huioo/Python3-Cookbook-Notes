def out_put(result, logger=None):
    if logger is not None:
        logger.debug('Got %r', result)
      
      
def add(x, y):
    return x+y
    
    
if __name__ == '__main__':
    import logging
    from multiprocessing import Pool
    from functools import partial
    
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(asctime)s %(thread)d %(threadName)s %(process)d] '
                               '[%(name)s %(levelname)s %(module)s:%(lineno)d] [%(funcName)s]: %(message)s')
    logger = logging.getLogger('test')
    # logger.level = logging.DEBUG
    p = Pool()
    p1 = Pool()

    for i in range(5):
        p.apply_async(add, (i, 1), callback=partial(out_put, logger=logger))
        p1.apply_async(add, (i+5, 1), callback=partial(out_put, logger=logger))

    p.close()
    p1.close()
    p.join()
    p1.join()


