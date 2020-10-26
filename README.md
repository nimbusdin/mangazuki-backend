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

The entire backend can run on a dockerized container I have prepared.

If you need to install Docker, you can install it following the instructions [here](https://docs.docker.com/engine/install/)

Run the following command to download the image

```docker pull nimbus22/mangazuki-backend```

Once the image has been downloaded, you can run the image with the following command

```docker run nimbus22/mangazuki-backend```

## REST API Calls

The API should run on the following IP address:

```http://172.17.0.2:5000/```

The following endpoints are available:
api/series
api/news
latest/news

### GET - The latest releases

We can get the latest releases by visiting the `series` endpoint `http://172.17.0.2:5000/api/series`.

We can also index into each individual release `http://172.17.0.2:5000/api/series/1'

We can search through these releases using the following filters:

```http://172.17.0.2:5000/api/series?q={"filters":[{"name":"title","op":"like","val":"%president%"}]}```




