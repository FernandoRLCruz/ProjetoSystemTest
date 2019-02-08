from selenium import webdriver


def before_feature(context, feature):
    context.driver = webdriver.Chrome(context.config.userdata['driverPathLinux'])
    context.driver.implicitly_wait(15)
    context.driver.delete_all_cookies()
    context.driver.maximize_window()

def after_feature(context, feature):
    context.driver.quit()