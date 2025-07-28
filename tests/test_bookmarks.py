import pytest
from bookmarks import get_folders_of_bookmarks


def test_correct_get_folders_of_bookmarks():
    test_case = {
        "children": [
            {
                "guid": "menu________",
                "id": 2,
                "index": 0,
                "root": "bookmarksMenuFolder",
                "title": "menu",
                "type": "text/x-moz-place-container",
                "typeCode": 2,
            },
            {
                "children": [
                    {
                        "guid": "ChxCSQm0N06WZUajllLuUQ==",
                        "iconUri": "http://192.168.1.1/img/favicon.ico",
                        "id": 153,
                        "index": 133,
                        "type": "text/x-moz-place",
                        "typeCode": 1,
                        "uri": "http://192.168.1.1/",
                    },
                    {
                        "guid": "1o2jU+kfykG+I4f3fGE8hA==",
                        "id": 1193,
                        "index": 1168,
                        "type": "text/x-moz-place",
                        "typeCode": 1,
                        "uri": "https://www.foo.com/",
                    },
                ],
                "guid": "toolbar_____",
                "id": 3,
                "index": 1,
                "root": "toolbarFolder",
                "title": "toolbar",
                "type": "text/x-moz-place-container",
                "typeCode": 2,
            },
            {
                "guid": "unfiled_____",
                "id": 5,
                "index": 3,
                "root": "unfiledBookmarksFolder",
                "title": "unfiled",
                "type": "text/x-moz-place-container",
                "typeCode": 2,
            },
            {
                "guid": "mobile______",
                "id": 6,
                "index": 4,
                "root": "mobileFolder",
                "title": "mobile",
                "type": "text/x-moz-place-container",
                "typeCode": 2,
            },
        ],
        "guid": "root________",
        "id": 1,
        "index": 0,
        "root": "placesRoot",
        "title": "",
        "type": "text/x-moz-place-container",
        "typeCode": 2,
    }

    test_case_result = [
        [
            {
                "guid": "ChxCSQm0N06WZUajllLuUQ==",
                "iconUri": "http://192.168.1.1/img/favicon.ico",
                "id": 153,
                "index": 133,
                "type": "text/x-moz-place",
                "typeCode": 1,
                "uri": "http://192.168.1.1/",
            },
            {
                "guid": "1o2jU+kfykG+I4f3fGE8hA==",
                "id": 1193,
                "index": 1168,
                "type": "text/x-moz-place",
                "typeCode": 1,
                "uri": "https://www.foo.com/",
            },
        ]
    ]

    assert get_folders_of_bookmarks(test_case) == test_case_result


def test_error_get_folders_of_bookmarks():
    test_case = {
        "child": [
            {
                "guid": "menu________",
                "id": 2,
                "index": 0,
                "root": "bookmarksMenuFolder",
                "title": "menu",
                "type": "text/x-moz-place-container",
                "typeCode": 2,
            },
            {
                "children": [
                    {
                "guid": "1o2jU+kfykG+I4f3fGE8hA==",
                "id": 1193,
                "index": 1168,
                "type": "text/x-moz-place",
                "typeCode": 1,
                "uri": "https://www.foo.com/",
                    }
                ],
                "guid": "toolbar_____",
                "id": 3,
                "index": 1,
                "root": "toolbarFolder",
                "title": "toolbar",
                "type": "text/x-moz-place-container",
                "typeCode": 2,
            },
        ]
    }

    with pytest.raises(KeyError):
        assert get_folders_of_bookmarks(test_case)


def test_get_unique_bookmarks():
    test_case = [
        [
            {
                "guid": "ChxCSQm0N06WZUajllLuUQ==",
                "iconUri": "http://192.168.1.1/img/favicon.ico",
                "id": 153,
                "index": 133,
                "type": "text/x-moz-place",
                "typeCode": 1,
                "uri": "http://192.168.1.1/",
            },
            {
                "guid": "1o2jU+kfykG+I4f3fGE8hA==",
                "id": 1193,
                "index": 1168,
                "type": "text/x-moz-place",
                "typeCode": 1,
                "uri": "https://www.foo.com/",
            },
        ]
    ]

    test_case_result = [
            {
                "guid": "ChxCSQm0N06WZUajllLuUQ==",
                "iconUri": "http://192.168.1.1/img/favicon.ico",
                "id": 153,
                "index": 133,
                "type": "text/x-moz-place",
                "typeCode": 1,
                "uri": "http://192.168.1.1/",
            },
            {
                "guid": "1o2jU+kfykG+I4f3fGE8hA==",
                "id": 1193,
                "index": 1168,
                "type": "text/x-moz-place",
                "typeCode": 1,
                "uri": "https://www.foo.com/",
            },
        ]