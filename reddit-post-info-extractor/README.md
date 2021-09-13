# Reddit-post-info-extractor
These scripts generate a file with a list of multiple reddit posts' Author, Title, Link and Upvote count that can be easily imported into excel and other spreadsheets
# Usage
## Preparation:
* Install the latest version of python 3
* Enable PowerShell script execution (Run "set-executionpolicy remotesigned" as an administrator)
* Make a text file with the links to all the Reddit posts you want to include, 1 post per line with no separator character
## Use
* Launch a command prompt in the folder you have the scripts at
* Type "split.py file.txt" where file.txt is the name of the text file containing the links
* Type "download.py apidownl.txt"
* Type "powershell"
* Type ".\downloader.ps1"
* Type ".\run.bat"
* Open the "finaldata.txt" file in a text editor, copy its content and paste it in excel or another program, selectiong the text import wizzard to split collumns by semicolons.
