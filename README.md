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

http://172.17.0.2:5000/

The following endpoints are available:
api/series
api/news
latest/news

### GET - The latest releases

We can get the latest releases by visiting the `series` endpoint http://172.17.0.2:5000/api/series

We can also index into each individual release http://172.17.0.2:5000/api/series/1

We can search through these releases using the following filters:

```http://172.17.0.2:5000/api/series?q={"filters":[{"name":"title","op":"like","val":"%president%"}]}```

To get the releases from a specific date onwards:

```http://172.17.0.2:5000/api/series?q={"filters":[{"name":"updated","op":"ge","val":"2020-10-18"}]}```

### GET - The latest trending releases

We can get the latest trending releases by adding a filter to the series endpoint to see if the trending flag is True

```http://172.17.0.2:5000/api/series?q={"filters":[{"name":"trending","op":"eq","val":"True"}]}```

If you want multiple filters such as trending series from a certain date onwards:

```http://172.17.0.2:5000/api/series?q={"filters":[{"name":"trending","op":"eq","val":"True"},{"name":"updated","op":"ge","val":"2020-10-18"}]}```

### GET, POST, PUT, DELETE - Data for a series

### GET, POST, PUT, DELETE - Series

We can put in series data using POST, PUT, and DELETE API calls on the same endpoint as above. For PUT and DELETE, we need the specific ID for the series we are trying to update.

We can first delete a series

```DELETE http://172.17.0.2:5000/api/series/1```

Now that the series with id 1 is deleted, we can add a series with the same ID

```
POST http://172.17.0.2:5000/api/series
{
    "author": "Mangazuki",
    "content": "Manga",
    "id": 1,
    "link": "http://172.17.0.2:5000",
    "summary": "summary",
    "title": "Manga Title",
    "trending": "True",
    "updated": "2020-10-26"
}
```

If we POST without an ID, it uses the next available ID number.
If we want to PUT update the current series

```
PUT http://172.17.0.2:5000/api/series/1
{
    "summary": "New manga summary",
    "title": "New manga title"
}
```

### GET - The latest news

Currently WIP.

Fetch the latest news from the endpoint here

```http://172.17.0.2:5000/latest/news```

### GET, POST, PUT, DELETE - News pages

The same applies to the news page as the series page for the endpoint api/news. Only the format of the data that the news API holds is different:

```
POST http://172.17.0.2:5000/api/news
{
    "author": "mangazuki",
    "body": "news body",
    "date": "2020-10-20",
    "heading": "news post",
    "id": 1,
    "subheading": "this is a news post"
}

Again, the id field is not necessary.