import pytest
from playwright.sync_api import sync_playwright
from config.devices import DEVICES


def pytest_addoption(parser):
    parser.addoption(
        "--test-device",
        action="store",
        default="iphone",
        help="Device to run tests on: android or iphone"
    )


@pytest.fixture()
def device_config(request):
    device_name = request.config.getoption("--test-device").lower()
    if device_name not in DEVICES:
        raise ValueError(
            f"Unsupported device: {device_name}. Supported devices are: {list(DEVICES.keys())}")

    device_config = DEVICES[device_name]
    with sync_playwright() as p:
        browser_type = getattr(p, device_config["browser"])
        browser = browser_type.launch(headless=False)
        device = p.devices[device_config["device"]]
        context = browser.new_context(**device)
        page = context.new_page()
        yield page
        context.close()
        browser.close()
