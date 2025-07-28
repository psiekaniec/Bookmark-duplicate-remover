import json, os, re, sys


def main():
    pattern = r".+\.json"
    while True:
        try:
            input_filename, output_filename = "", ""
            if matched := re.search(
                pattern, input("Input filename: ").rstrip(), re.IGNORECASE
            ):
                input_filename = matched.string
            if matched := re.search(
                pattern, input("Output filename: ").rstrip(), re.IGNORECASE
            ):
                output_filename = matched.string
            if not input_filename:
                raise TypeError("Fix input file name")
            if not output_filename:
                raise TypeError("Fix output file name")
            break
        except TypeError as te:
            print(te.args[0])
            continue

    try:
        input_path = os.path.join(os.getcwd(), input_filename)
        output_path = os.path.join(os.getcwd(), output_filename)
        if not os.path.isfile(input_path):
            raise ValueError(f"{input_path} is not a file")

        content = read_content(input_path)

        save_pretty_json(output_filename, content)
        content = read_content(output_path)

        folders = get_folders_of_bookmarks(content)
        unique = get_unique_bookmarks(folders)

        print(f"Found: {len(unique)} unique bookmark(s)")

        save_pretty_json(output_path, unique, True)

    except ValueError as ve:
        sys.exit(ve.args[0])


def get_folders_of_bookmarks(content):
    return [
        folder["children"] for folder in content["children"] if "children" in folder
    ]


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


def read_content(path):
    content = ""
    with open(path, "r") as pretty:
        content = json.load(pretty)

    return content


def save_pretty_json(path, content, final=False):
    if final:
        content = {
            "guid": "root________",
            "id": 1,
            "index": 0,
            "root": "placesRoot",
            "title": "",
            "type": "text/x-moz-place-container",
            "typeCode": 2,
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
                    "children": content,
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
        }

    with open(path, "w") as pretty:
        json.dump(content, pretty, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
