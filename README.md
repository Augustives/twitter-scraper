# Twitter Scraper

- To run the scraper with the users listed on settings:
```
make scrape
```

- To run the sraper into a specific user:
```
make scrape username=xxxxxxx
```

- Make sure to create a .env file at the root of the project before running it, with the following variables that you can get at you twitter account:
```
ACCESS_TOKEN=
ACCESS_TOKEN_SECRET=
API_KEY=
API_KEY_SECRET=
BEARER_TOKEN=
```