# probable-guacamole

# Dependencies 
- [Python 3.7x](https://www.python.org/downloads/)
- [Pipenv] (https://github.com/pypa/pipenv)
- [Github Access Token Basic Auth](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)

## Usage
--
"enter streaming key term when prompted" 
* To control page streaming append the string `~page_size=50` to end of query 
* To control streaming input `Y/N` for continuous streaming mode for results


## Install
```bash
brew install python
brew install
```
## Run
```
# Environment 
cp sample.env .env
# fill in .env with github token see instructions above
pipenv run python main.py 
```

## Tests
```
pipenv install
pipenv run pytest # woops didn't get to this 
```

## Resources
- https://developer.github.com/v3/search/#search-repositories
- https://developer.github.com/v3/guides/traversing-with-pagination/
- https://medium.com/pythonhive/python-decorator-to-measure-the-execution-time-of-methods-fa04cb6bb36d

### PROMPT
The assignment description is below, a few things to remember:
- [ ] Take around 3 hours, when that time is almost up, you should take a few more minutes to wrap up what you were working on, zip up the code, and send it over.
- [ ]Focus on accomplishing each step in full before moving onto the next.
- [ ]You can email me with any additional questions.

API Assignment

In this assignment you will be building a tool to explore the GitHub API: https://developer.github.com/v3/. You should NOT use a library that implements the GitHub API directly, you will be calling the web endpoints yourself. That said, you may use any programming languages, libraries, and tools that you prefer.


- [x]The interface to the tool should be simple (so you focus your time on the core API related work), for example a cmdline loop or very basic UI should do fine. The tool will query the GitHub API with arguments the user passes in and display the results to the user (i.e. dump json on cmdline).


Do not try to do everything at once - you should tackle one piece at a time. There is a lot here, it is not expected that you do everything. We value function above all else - it is better you get two things fully working than five things 80% working.


Here’s the tasks to complete in a rough order:

- [x] Implement the search API to find repositories.

- [x]GitHub has rate limiting, implement something that understands the rate limits and allows the client to control the rate it sends requests.

- [x] Add pagination support - use the page arguments and be able to control how much data is returned to client and allow the client to specify how much data they want.

- [x] Make the tool be push based, meaning the client makes a query and the tool keeps querying the API and pushing new results as they come in. You can treat pages like new results for testing.

- [ ] Implement fault tracking. Imagine the API will change in the future and your calls will break - we want to know when this happens and for how long we get errors. You can test this by sending bad requests.

