from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@when("the user clicks the logout button")
def step_user_clicks_logout(context):
    context.driver.find_element(By.ID, "menu-toggle").click()
    context.driver.find_element(By.LINK_TEXT, "Logout").click()

@then("the user should be redirected to the login page")
def step_verify_logout(context):
    WebDriverWait(context.driver, 10).until(
        EC.url_to_be("https://katalon-demo-cura.herokuapp.com/")
    )
    assert context.driver.current_url == "https://katalon-demo-cura.herokuapp.com/", "Logout failed!"