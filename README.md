# Polypinion API

This is the api that front end and backend will use to interact. This api stores CSVs locally, which will be updated at different cadences from the database (not yet deployed).
When a request is made the locally stored CSVs aggregate and output a JSON. 

Currently, this has CSVs for RANK and Articles. RANK is where on the feed the article cluster will show. ARTICLE is the content (headlines, gist, articles, date)

- Note: as of 01/20/2024 cloud development has not started for the backend.

![Alt text](https://github.com/ethanjones-git/api_polypinion/blob/master/backend_arch.png?raw=true)

## Installation

dependencies should be in the requirements.txt file.



