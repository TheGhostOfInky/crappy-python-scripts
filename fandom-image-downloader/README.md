# Fandom-image-downloader
A pair of python scripts that creates a PowerShell script that will download all the images in bullet lists in original uncompressed state from a fandom webpage.<br>
This script is designed for Windows, a Linux version is available at [Fandom-Image-Downloader-Linux](https://github.com/TheGhostOfInky/Fandom-Image-Downloader-Linux)
# Usage
## Preparation:
* Install the latest version of python 3
* Enable PowerShell script execution (Run "set-executionpolicy remotesigned" as an administrator)
* Download the webpage you want to extract the files from and place it inside the folder you unzipped the scripts to
## Use
* Launch a command prompt in the folder you have the scripts at
* Type "split.py file.html" where file.html is the name of the downloaded webpage
* Type "download.py links.txt"
* Type "powershell"
* Type ".\downloader.ps1"
* Your images will now download 
