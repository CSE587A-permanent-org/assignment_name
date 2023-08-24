import logging
from utils.configure_logging import configure_logging

logger = logging.getLogger(__name__)


def square(x: [int, float]) -> [int, float]:
    """Square the numeric input

    :param x: A numeric value
    :type x: int, float]
    :raises ValueError: if `x` is not numeric
    :return: The squared value of the input
    :rtype: [int, float]
    """
    # check input type
    if not isinstance(x, (int, float)):
        raise ValueError('`x` must be numeric')
    
    # optional logging
    logger.debug('value of x: %s', x)
    
    return x**2
