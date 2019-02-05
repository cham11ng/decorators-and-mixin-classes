from functools import wraps


def log(logger, prefix):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                logger.debug('{0} - Payload: {1} {2}'.format(
                    prefix, args or '', kwargs or '')
                )
                res = function(*args, **kwargs)
                logger.debug('{0} - Result: {1}'.format(prefix, res))

                return res
            except ValueError as ex:
                logger.error('{0} - {1}: {2}'.format(prefix, type(ex).__name__, ex.args))

                raise ex  # Call custom exception
            except Exception as ex:
                logger.error('{0} - {1}: {2}'.format(prefix, type(ex).__name__, ex.args))

                raise ex  # Call custom exception
        return wrapper
    return decorator
