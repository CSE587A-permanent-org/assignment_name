import logging
import numpy as np
import unittest
from ..utils.configure_logging import configure_logging
from .assignment import square

configure_logging(logging.WARN)


class TestDiceEM(unittest.TestCase):
    
    def test_square(self):
        
        # Test with an empty list
        with self.assertRaises(ValueError):
            square('two')
        
        self.assertEqual(square(2), 4)
