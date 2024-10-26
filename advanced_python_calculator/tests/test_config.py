# tests/test_config.py

import pytest
import os
from app.config import load_config

def test_load_config_valid():
    config = load_config('tests/test_config.json')
    assert config['setting1'] == 'value1'

def test_load_config_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_config('non_existent_file.json')

# Create a test configuration file
@pytest.fixture(scope='module', autouse=True)
def create_test_config():
    with open('tests/test_config.json', 'w') as f:
        f.write('{"setting1": "value1"}')
    yield
    os.remove('tests/test_config.json')
