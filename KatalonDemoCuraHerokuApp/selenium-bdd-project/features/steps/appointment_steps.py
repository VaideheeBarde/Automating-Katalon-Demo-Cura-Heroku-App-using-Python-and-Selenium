from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("the user from row {row_index} is logged in")
def step_user_logged_in(context, row_index):
    context.execute_steps(f'''
    Given the user is on login page
    When the user enters credentials from row {row_index}
    And clicks the login button
    ''')

@when('the user selects facility from row {row_index}')
def step_select_facility(context, row_index):
    row = context.data.iloc[int(row_index)]
    facility = row["Facility"]
    dropdown = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "combo_facility"))
    )
    dropdown.send_keys(facility)

@when('clicks Apply for hospital readmission for condition from row {row_index}')
def step_hospital_readmission(context, row_index):
    row = context.data.iloc[int(row_index)]
    condition = row["Apply For Hospital Readmission"]
    if condition == 'Yes':
        context.driver.find_element(By.ID, "chk_hospotal_readmission").click()

@when('chooses healthcare program from row {row_index}')
def step_choose_program(context, row_index):
    row = context.data.iloc[int(row_index)]
    program = row["Healthcare Program"]
    if program.lower == "medicare":
        context.driver.find_element(By.ID, "radio_program_medicare").click()
    elif program.lower == "medicaid":
        context.driver.find_element(By.ID, "radio_program_medicaid").click()
    else:
        context.driver.find_element(By.ID, "radio_program_none").click()

@when('selects the visit date from row {row_index}')
def step_set_visit_date(context, row_index):
    row = context.data.iloc[int(row_index)]
    date = row["Visit Date"]
    date_picker = context.driver.find_element(By.ID, "txt_visit_date")
    date_picker.clear()
    date_picker.send_keys(date)

@when('adds a comment from row {row_index}')
def step_add_comment(context, row_index):
    row = context.data.iloc[int(row_index)]
    comment = row["Comment"]
    context.driver.find_element(By.ID, "txt_comment").send_keys(comment)

@when('clicks the Book Appointment button')
def step_book_appointment(context):
    context.driver.find_element(By.ID, "btn-book-appointment").click()

@then("the user should see the appointment confirmation for row {row_index}")
def step_verify_appointment_confirmation(context, row_index):
    confirmation_message = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Appointment Confirmation']"))
    )
    assert confirmation_message, "Appointment confirmation page not displayed!"