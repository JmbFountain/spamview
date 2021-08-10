# Documentation on used stuff:
https://selenium-python.readthedocs.io/getting-started.html#selenium-remote-webdriver
https://flask.palletsprojects.com/en/1.1.x/api/#flask.Response.set_cookie
https://docs.docker.com/compose/compose-file/compose-file-v3/#args

# Architecture
## Infrastructure
The project is split into a frontend nginx server hosting the UI, a worker node that does the major analysis,
and a selenium node for taking screenshots of the results of extracted links.

## Frontend
### Framework
to be decided

## Application / Worker
### Framework
Flask is used as the main framework for this node, implementing a simple HTTP API for the front-end to call. This also
enables a future use of an SMTP Frontend to directly send suspicious E-Mails to.
