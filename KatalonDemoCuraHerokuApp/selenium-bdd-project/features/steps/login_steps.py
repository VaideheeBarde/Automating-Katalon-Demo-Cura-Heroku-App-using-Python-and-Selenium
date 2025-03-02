from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage

@given("the user is on login page")
def step_user_on_login_page(context):
    context.driver.get("https://katalon-demo-cura.herokuapp.com/")
    context.driver.find_element(By.ID, "btn-make-appointment").click()

@when("the user enters credentials from row {row_index}")
def step_user_enters_credentials(context, row_index):
    row = context.data.iloc[int(row_index)]
    login_page = LoginPage(context.driver)
    login_page.enter_username(row["username"])
    login_page.enter_password(row["password"])

@when("clicks the login button")
def step_user_clicks_login(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()

@then("the user should see the result from row {row_index}")
def step_verify_login(context, row_index):
    row = context.data.iloc[int(row_index)]
    expected_result = row["expected_result"]
    if expected_result == "Success":
        WebDriverWait(context.driver, 10).until(EC.url_contains("#appointment"))
        assert "#appointment" in context.driver.current_url, "Login failed"
    else:
        assert "Login failed!" in context.driver.page_source, "Error message not displayed!"