# racing prediction

An experiment with horse and dog racing data.

### Components:
1. Web Scraper (Python + Beautiful Soup).
   * Scrapes race results from the TAB NZ website.
   * Saves results in SQL Server database via C# Web API.
   * Run with `pipenv run python3 date_range-scraper.py'
2. C# Web API for [create, read] access over the race data.
