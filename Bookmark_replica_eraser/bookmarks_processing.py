import json
import os


def main(filename):
    content = ""
    target_path = os.path.join(os.getcwd(), filename)
    with open(target_path, "r") as file:
        content = json.load(file)

    with open("pretty.json", "w") as pretty:
        json.dump(content, pretty, indent=4, sort_keys=True)

    with open("pretty.json", "r") as pretty:
        content = json.load(pretty)

    lists_of_bookmarks = [
        dict_with_key
        for dict_with_key in content["children"]
        if "children" in dict_with_key
    ]
    result = []
    for l in lists_of_bookmarks:
        try:
            bookmarks = sorted(l["children"], key=lambda b: b["uri"])
            for i in range(len(bookmarks)):
                if (
                    not bookmarks[i - 1]["uri"] == bookmarks[i]["uri"]
                    or len(bookmarks) == 1
                ):
                    result.append(bookmarks[i])

        except KeyError:
            print(f"Invalid list of bookmarks")

    print(result)


if __name__ == "__main__":
    filename = "bookmarks-2025-07-27.json"
    main(filename)
