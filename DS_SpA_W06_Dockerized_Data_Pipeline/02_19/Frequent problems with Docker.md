![:lady_beetle:](https://a.slack-edge.com/production-standard-emoji-assets/13.0/google-medium/1f41e.png) **Frequent problems with Docker**

- how to delete old containers/images?
- how to rebuild properly?
- where to put credentials? environment variables
- two issues in one
- how to find out what is going on?

**Two output channels in a Unix program:**

- STDOUT : print, normal output
- STDERR : logging, used by docker-compose
- ![:exclamation:](https://a.slack-edge.com/production-standard-emoji-assets/13.0/google-medium/2757.png)docker-compose containers are not interactive, you don't get to see print() output from a running container

**Connect to Docker-postgres from local (psql):**

- hostname: localhost or 0.0.0.0
- port: first number (5555)
- dbname, username + password: as defined in `.yml`
- example: `psql -h 0.0.0.0 -p 5555 -U dummy -d tweets`example from Jupyter:

 pg = create_engine('[postgres://dummy:1234](postgres://dummy:1234)@0.0.0.0:5555/tweets', echo=True)Connect to Docker-postgres from within a service (SQLAlchemy in etl.py):- hostname: name of the service
\- port: default, second number (5432)
\- dbname, username + password: as defined in .ymlexample:
 pg = create_engine('[postgres://dummy:1234](postgres://dummy:1234)@postgresdb:5432/tweets', echo=True)docker-compose exec mongodb mongo