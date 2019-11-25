import unittest
import pytest
import logger
from login import UIloginSuite


class TestSuite(unittest.TestCase):
    logger.logger.info("Test Case Execution Starts")

    @classmethod
    @pytest.mark.functional
    def setUpClass(self):
        logger.logger.info("Test Cases setup")
        self.login_obj = UIloginSuite()

    @pytest.mark.functional
    def testLogin(self):
        logger.logger.info("Executing Login test cases")
        self.login_obj.init_browser()

    @classmethod
    def tearDownClass(self):
        logger.logger.info("Suite teardown")


if __name__ == '__main__':
    test_suite_obj = TestSuite()

    # Test Cases
    test_obj = unittest.TestSuite()
    test_obj.addTest(TestSuite('testLogin'))

    runner = unittest.TextTestRunner()
    runner.run(test_obj)
