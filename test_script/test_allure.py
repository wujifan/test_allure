import pytest
import allure
from base.init__driver import ini_data


class Test_allure:
    @pytest.mark.parametrize('test_name, name, exp_value', ini_data('test_data', ['name', 'exp_value']))
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('这里是测试步骤')
    def test_001(self, test_name, name, exp_value):
        allure.attach('这里是测试用例:%s'% test_name, '描述')
        assert name == exp_value





