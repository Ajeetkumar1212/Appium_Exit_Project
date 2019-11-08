from appium import webdriver
import selenium
#Device Information
##Here the Android  device Connected by Extrnal Cable
driver=None
def Requirements():
    Desired_Capabilities={
    "deviceName": "Redmi 6A",
    "platformName": "android",
    "platformVersion": "8.1.0",
    "appPackage": "com.touchboarder.android.api.demos",
    "appActivity": "com.example.android.apis.ApiDemos",
#"path":"C:\\Users\\ajeetpal\\PycharmProjects\\Appium Project\\API.apk"

}
    ##Appium Address
    global driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",Desired_Capabilities)
    driver.implicitly_wait(30)

