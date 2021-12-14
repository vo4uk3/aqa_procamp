from providers.service.drivers import Driver


def test_open_page():
    driver = Driver('chrome')
    print(type(driver))
    