# compile-report-pack
Single-action Looker Action Hub using Python + FastAPI. Includes SendGrid for emails.

# SDK credentials must be configured as environment variables
NOTE: This project assumes that you have set SDK credentials as environment variables.

# To use
Requites Python 3.7+. To run locally:

1. `python3 -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `cp start.example start`
5. Update environment variables in start script
4. `./start`

# Adding a new action

Any new, conforming action added to the actions folder will automatically be added to the Action Hub.

See the original Fast Hub project for more examples: [https://github.com/ContrastingSounds/fast-hub](Fast Hub project on GitHub)
