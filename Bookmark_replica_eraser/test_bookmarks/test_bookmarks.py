import pytest
from bookmarks_processing import get_folders_of_bookmarks, get_unique_bookmarks, main, read_content, save_pretty_json

def test_get_folders_of_bookmarks():
    ...
def test_get_get_unique_bookmarks():
    ...
def test_read_content():
    ...
def test_save_pretty_json():
    ...
def test_raises_error():
    with pytest.raises(ValueError):
        main('error_path.json')