from pages.login_page import LoginPage

def login_helper(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)