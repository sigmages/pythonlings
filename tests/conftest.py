import pytest

import os
import i18n


@pytest.fixture
def fixtures_dir():
    return os.path.join(os.path.dirname(__file__), "fixtures")


def pytest_configure():
    # setup i18n before tests
    i18n.config.set("locale", os.getenv("PYTHONLINGS_LANGUAGE", "en"))
    i18n.load_path.append("pythonlings/i18n")
