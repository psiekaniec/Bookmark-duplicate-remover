import json
import os


def main(filename):
    content = ""
    target_path = os.path.join(os.getcwd(), filename)
    content = read_content(target_path)

    save_pretty_json("pretty2.json", content)
    content = read_content("pretty2.json")

    folders = get_folders_of_bookmarks(content)
    result = get_unique_bookmarks(folders)

    print(f"Found: {len(result)} unique bookmark(s)")

    save_pretty_json("pretty_final.json", result)


def get_unique_bookmarks(folders_of_bookmarks, key="uri"):
    result = []
    for f in folders_of_bookmarks:
        try:
            bookmarks = sorted(f, key=lambda bookmark: bookmark[key])
            for i in range(len(bookmarks)):
                if (
                    not bookmarks[i - 1][key] == bookmarks[i][key]
                    or len(bookmarks) == 1
                ):
                    result.append(bookmarks[i])

        except KeyError:
            print(f"Invalid list of bookmarks")

    return result


def get_folders_of_bookmarks(content):
    return [
        folder["children"] for folder in content["children"] if "children" in folder
    ]


def save_pretty_json(path, content, final=False):
    if final:
        content = (
            """
        { "children": 
            [
                {
                    "dateAdded": 1753605265591000,
                    "guid": "menu________",
                    "id": 2,
                    "index": 0,
                    "lastModified": 1753647823370000,
                    "root": "bookmarksMenuFolder",
                    "title": "menu",
                    "type": "text/x-moz-place-container",
                    "typeCode": 2
                },
                {
                "children": """
            + content
            + """
                ,
                        "dateAdded": 1753605265591000,
                        "guid": "toolbar_____",
                        "id": 3,
                        "index": 1,
                        "lastModified": 1753648620860000,
                        "root": "toolbarFolder",
                        "title": "toolbar",
                        "type": "text/x-moz-place-container",
                        "typeCode": 2
                    },
                    {
                        "dateAdded": 1753605265591000,
                        "guid": "unfiled_____",
                        "id": 5,
                        "index": 3,
                        "lastModified": 1753647823370000,
                        "root": "unfiledBookmarksFolder",
                        "title": "unfiled",
                        "type": "text/x-moz-place-container",
                        "typeCode": 2
                    },
                    {
                        "dateAdded": 1753605265603000,
                        "guid": "mobile______",
                        "id": 6,
                        "index": 4,
                        "lastModified": 1753647823370000,
                        "root": "mobileFolder",
                        "title": "mobile",
                        "type": "text/x-moz-place-container",
                        "typeCode": 2
                    }
            ],
            "dateAdded": 1753605265591000,
            "guid": "root________",
            "id": 1,
            "index": 0,
            "lastModified": 1753648620860000,
            "root": "placesRoot",
            "title": "",
            "type": "text/x-moz-place-container",
            "typeCode": 2
        }"""
        )

    with open(path, "w") as pretty:
        json.dump(content, pretty, indent=4, sort_keys=True)


def read_content(path):
    with open(path, "r") as pretty:
        content = json.load(pretty)

    return content


if __name__ == "__main__":
    filename = "bookmarks-2025-07-27.json"
    main(filename)
