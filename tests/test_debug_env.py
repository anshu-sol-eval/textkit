import os


def test_debug_environment():
    # Temporary: helps debug the CI-only failure in #4.
    print(os.environ)
    assert True
