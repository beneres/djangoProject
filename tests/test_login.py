import unittest
from tests import test_views  # import the test_views module containing the tests


# define a test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_views('test_successful_login'))
    suite.addTest(test_views('test_unsuccessful_login'))
    suite.addTest(test_views('test_logout'))
    return suite


if __name__ == '__main__':
    # run using the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite())

# run python test_login.py on terminal to perform a testing