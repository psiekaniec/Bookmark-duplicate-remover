# Bookmark duplicate remover

This script is for removing duplicate entries in Firefox bookmark backup file. It assumes that input file is formatted like JSON. Script requires the user to specify the name of the input and output files. These files must be in the working directory of the script. In addition, the bookmarks backup should only include bookmarks in the Bookmark Bar folder in the (Mozilla Firefox) browser. Output file contains unique bookmarks pretty JSON formatted. This file can be easily loaded in the Firefox browser.

## Installation

Download repo and move it to your target directory. Grab your backup JSON file from Firefox and paste to the directory. Run script as

```bash
   python bookmarks.py
```

Enter the name of the input file, next the output file. If everything is ok with the data content, you should see a count of unique bookmarks in console and the output file should contain pretty formatted JSON. In case of any error, you will see a message in the console and the output file will not contain the correct data to restore the bookmarks in the browser.
