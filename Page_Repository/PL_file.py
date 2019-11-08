from Base import BaseClass
from Locators import Locator_call as call
#Read JSON file on Each method
#sys.path['C:\\Users\\ajeetpal\\PycharmProjects\\Appium Project\\Base\\Base.py']

def Animation_click():
  val1= BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","xpath_Animation"))
  return val1

def Hide_show_click():
  val2= BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String2"))
  return val2

def Zero_click():
  val3= BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String3"))
  return val3

def One_click():
  val4= BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String4"))
  return val4

def Two_click():
  val5= BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String5"))

  return val5

def Three_click():
  val6= BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String6"))
  return val6

def Hide_verify():
    try:
     BaseClass.driver.find_element_by_xpath(call.Call_fun("'Locators.json","String4"))
     return 'true'
    except Exception:
        return 'false'


def Show_button_click():
  val7= BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String7"))
  return val7

def show_verify():
    try:
     BaseClass.driver.find_element_by_xpath(call.Call_fun("'Locators.json","String4"))
     return 'true'
    except Exception:
        return 'false'

def App_click():
   val8=BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String8"))

   return val8

def Action_Bar_click():
   val9=BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String9"))
   return val9


def Display_Options_click():
   val10=BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String10"))
   return val10


def Display_Show_Title_click():
   val11=BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String11"))
   return val11

def Display_Show_Title_click1():
   val11=BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String11"))
   return val11

def verify_title():
    if(BaseClass.driver.find_element_by_xpath(call.Call_fun("Locators.json","String12"))).is_displayed():
        return 'true'
    else:
        return 'false'






