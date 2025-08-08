from behave import *
from selenium import webdriver

driver = webdriver.Chrome()


@given('a user is on homescreen')
def openHomeScreen(context):
    driver.get("https://automationexercise.com")

@when('user sign up as new user')
def createUser():
    log('log')