from Scweet.scweet import scrap # They can't spell scrape!
from datetime import date
import sys

def main():
    if len(sys.argv) != 2:
        print("USAGE: python3 scrape.py <output_filename>")
        sys.exit(1)

    filename = "output.csv"

    # A matching tweet must contain at least one of these words
    # keywords = ["women", "woman", "girl", "girls", "female", "females", "feminine", "femininity"]
    keywords = []

    # A matching tweet must be from one of these users
    from_accounts = ["@narendramodi", "@PMOIndia", "@ChouhanShivraj", "@amitshah", "@rajnathsingh",
                     "@piyushgoyal", "@sambitswaraj", "@JPnadda", "@GautamGambhir", "@Swamy39",
                     "@BJP4India", "@myogiadityanath"]

    # A matching tweet must be directed at at least one of these users
    to_accounts = []

    # A matching tweet must contain at least one of these hashtags (you don't need to write the # symbol)
    hashtags = ["Tokyo2020", "Olympics"]

    # A matching tweet must be from between these dates (YYYY-MM-DD)
    start_date = "2021-08-04"
    max_date = "2021-08-05"

    # Name for output file. Remember to change this each time you run the script.

    ############################ You probably won't need to change anything below this line.

    # Order by date, not by popularity. This also excludes comments that would otherwise be included for no reason.
    display_type = "latest"

    # This is probably the most annoying part of scweet. Instead of making a single search and scrolling a lot,
    # scweet makes many searches and scrolls a little on each one. It breaks these searches up by date range.
    # For example, if our date range gives us 365 days, and interval == 5, then scweet will make 365/5=73 
    # consecutive searches; one for each 5 day chunk. If our date range is not an even multiple of interval,
    # then the remainder of the days will not be searched. That's terrible logic! The obvious workarounds are
    # setting interval to 1 (slow) and setting interval to the number of days in the date range,
    # (uses a lot of RAM) which is what I do below.
    # Unfortunately, scweet's default is (inexplicably) just interval=5.
    interval = (date(*(int(n) for n in max_date.split("-"))) - date(*(int(n) for n in start_date.split("-")))).days

    # These are workarounds because scweet doesn't allow you to specify more than one from_account, to_account, or hashtag
    if from_accounts:
        from_accounts = "%20OR%20from%3A".join(from_accounts)
    if to_accounts:
        to_accounts = "%20OR%20to%3A".join(to_accounts)
    if hashtags:
        hashtags = "%20OR%20%23".join(hashtags)

    # This grabs the data from Twitter, makes a folder called "outputs," and saves a csv of all the data into that folder
    data = scrap(start_date=start_date,
                 max_date=max_date,
                 from_account=from_accounts or None,
                 to_account=to_accounts or None,
                 words=keywords or None,
                 hashtag=hashtags or None,
                 interval=interval,
                 display_type=display_type,
                 filename=filename)

if __name__ == "__main__":
    main()