# food-pantry
A community fridge and pantry with food for the taking
Built with Django, PostgreSQL, and Docker.

### Development Setup

Clone the project and run the docker container:
```
git clone [url]
cd food-pantry
chmod +x entrypoint.sh     # if you get an access denied error
docker-compose up
```
The Django server runs from the `web` service while PostgreSQL runs from `db`.

## Running the tests

Explain how to run the automated tests for this system

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [PostgreSQL](https://www.postgresql.org/) - Database

## Authors

* **Jennifer Long** - [j-alicia-long](https://github.com/j-alicia-long)
* **Ishaan Dey** - [ishaandey](https://github.com/ishaandey)
* **Camille Digamo** - [CamilleDigamo](https://github.com/CamilleDigamo)

## Acknowledgments

* HackCville Deploy staff (Chris, Jedidiah, Harrison)
