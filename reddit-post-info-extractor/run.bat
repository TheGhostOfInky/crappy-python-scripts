copy parse.py JSON
cd JSON
for /r %%f in (*.json) do parse.py %%f
copy finaldata.txt ..\