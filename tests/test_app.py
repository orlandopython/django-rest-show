import sys

def test_python_version():
    assert sys.version_info.major == 3 and sys.version_info.minor >= 6
