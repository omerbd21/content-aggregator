# Omer's content Aggregator

This is my first "big" project and it contains the following microservices:

## Microservices
1. content-aggregator, written in BeautifulSoup and Flask
2. mongo-inserter, which will insert to my MongoDB
3. mongo-fethcer, which will to the opposite
4. celery-manager, written in Django
5. ui, written in React

## What is it about?
The purpose of this project is (as its name tells you) aggregate content from
your favourite websites. The default options will include One and ynet.


## How did I set the project up?
1. A Minishift (mini openshift) centos server with the following containers:<br>
  a. content-aggregator, a flask component built with BeautifulSoup<br>
  b. mongo-inserter, a flask component to update MongoDB<br>
  c. mongo-fetcher, a flask component to fetch info from MongoDB<br>
  d. a RabbitMQ cluster for the Celery app<br>
  e. The celery-manager, a django app built with celery<br>
2. A MongoDB centos server
3. A GitLab centos server to configure webhooks and manage this repo.

---NOTICE: The React component is not yet finished and therefore it is not in here yet. It will be updated when possible.---
