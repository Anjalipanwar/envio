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
    def testLogin01(self):
        logger.logger.info("Executing Login test cases")
        self.login_obj.init_browser()

    @pytest.mark.functional
    def testLogin02(self):
        logger.logger.info("Executing Login test case 02")
        self.login_obj.login()

    @pytest.mark.functional
    def testLogin03(self):
        logger.logger.info("Executing Login test case 02")
        self.login_obj.settings()

    @pytest.mark.functional
    def testLogin04(self):
        logger.logger.info("Executing Login test case 02")
        self.login_obj.logout()

    @pytest.mark.functional
    def testLogin05(self):
        logger.logger.info("Executing Login test case 02")
        self.login_obj.shut_driver()

    @classmethod
    def tearDownClass(self):
        logger.logger.info("Suite teardown")


if __name__ == '__main__':
    test_suite_obj = TestSuite()

    # Test Cases
    test_obj = unittest.TestSuite()
    test_obj.addTest(TestSuite('testLogin01'))
    test_obj.addTest(TestSuite('testLogin02'))
    test_obj.addTest(TestSuite('testLogin03'))
    test_obj.addTest(TestSuite('testLogin04'))
    test_obj.addTest(TestSuite('testLogin05'))

    runner = unittest.TextTestRunner()
    runner.run(test_obj)
