import json
import os


def main(filename):
    content = ""
    target_path = os.path.join(os.getcwd(), filename)
    content = read_content(target_path)

    save_pretty_json("pretty.json", content)
    content = read_content("pretty.json")

    folders = get_folders_of_bookmarks(content)
    result = get_unique_bookmarks(folders)

    print(f"Found: {len(result)} unique bookmark(s)")

    save_pretty_json("pretty.json", result)


def get_unique_bookmarks(folders_of_bookmarks):
    result = []
    for f in folders_of_bookmarks:
        try:
            bookmarks = sorted(f, key=lambda bookmark: bookmark["uri"])
            for i in range(len(bookmarks)):
                if (
                    not bookmarks[i - 1]["uri"] == bookmarks[i]["uri"]
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


def save_pretty_json(path, content):
    with open("pretty.json", "w") as pretty:
        json.dump(content, pretty, indent=4, sort_keys=True)


def read_content(path):
    with open(path, "r") as pretty:
        content = json.load(pretty)

    return content


if __name__ == "__main__":
    filename = "bookmarks-2025-07-27.json"
    main(filename)
