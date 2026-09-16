import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

@pytest.fixture
def user_data():
    return {
        'email' : 'user@example.com',
        'username' : 'testUser',
        'password' : 'password123'
    }

@pytest.fixture
def registration_page(page):
    return RegistrationPage(page)

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)