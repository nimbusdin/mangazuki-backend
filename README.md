Mangazuki Backend REST API
==========================

This is the REST API designed for Mangazuki.

The REST API was developed using Python Flask and Flask-Restless

## Backend Scraping

You can run the feed scraper by running the following command:

```python3 db.py```

The scraper requires `xmltodict` as a library so you can install that with the following command:

```pip3 install --user --upgrade xmltodict```

The resulting file should be `mangazuki.db` which is an SQLITE database.

## Running the Backend
