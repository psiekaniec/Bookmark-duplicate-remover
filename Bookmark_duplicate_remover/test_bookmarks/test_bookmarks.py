import pytest
from bookmarks import main

def test_get_folders_of_bookmarks():
    ...
def test_get_unique_bookmarks():
    ...
def test_read_content():
    ...
def test_save_pretty_json():
    ...
def test_raises_error():
    with pytest.raises(ValueError):
        main('error_path.json')