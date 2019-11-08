#Run Entire Code
from Base import BaseClass
import pytest
from Business_logic import BL_file
from Base.BaseClass import driver
from Page_Repository import PL_file

@pytest.mark.order1
def test_callAll():
    BaseClass.Requirements()
    BL_file.fun1()
    BL_file.fun2()
    BL_file.fun3()
    BL_file.fun4()
    BL_file.fun5()
    BL_file.fun6()
    assert PL_file.Hide_verify()== 'false'

@pytest.mark.order2
def test_call1():
    BL_file.fun7()

    BaseClass.driver.back()
    BaseClass.driver.back()
    assert PL_file.show_verify() == 'false'

@pytest.mark.order3
def test_two():
    BL_file.fun8()
    BL_file.fun9()
    BL_file.fun10()
    BL_file.fun11()
    BL_file.fun12()
    assert PL_file.verify_title() == 'true'
    #f6e16fb8-85df-4a4f-baa9-823050e09bc3


