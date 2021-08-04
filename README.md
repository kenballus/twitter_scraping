##Instructions:

Open up Command Prompt and run these commands:
    - `git clone --recurse-submodules https://github.com/kenballus/twitter_scraping`
    - `cd twitter_scraping\Scweep`
    - `pip uninstall Scweep` (This may say it can't find Scweep, but that's not a problem)
    - `pip install -e .`
    - `cd ..`
    - `python3 scrape.py example_file_name.csv` (You can make the file name whatever you want)

That will generate a file called `example_file_name.csv` containing your data.

By default, it just scrapes an example search. The code is well-commented and it should be clear how to make it search for whatever you want by editing `scrape.py`.

