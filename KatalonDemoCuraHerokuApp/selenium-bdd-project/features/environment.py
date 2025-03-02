import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Load test data from Excel
def before_all(context):
    context.data = pd.read_excel("C:\\Users\\vaide\\OneDrive\\Documents\\VaideheeBarde\\Selenium\\KatalonDemoCuraHerokuApp\\selenium-bdd-project\\tests\\test_data.xlsx")

def before_scenario(context, scenario):
    """Setup WebDriver before each scenario."""
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.maximize_window()

def after_scenario(context, scenario):
    """Quit WebDriver after each scenario."""
    context.driver.quit()
