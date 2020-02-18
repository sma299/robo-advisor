# robo-advisor

## Prerequisites


### Environment Setup
Create and activate a new Anaconda virtual environment:
sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:
sh
pip install -r requirements.txt
From within the virtual environment, demonstrate your ability to run the Python script from the command-line:
sh
python app/robo_advisor.py
If you see the example output, you're ready to move on to project development. This would be a great time to make any desired modifications to your project's "README.md" file (like adding instructions for how to setup and run the app like you've just done), and then make your first commit, with a message like "Setup the repo".
## Basic Requirements
### Repository Requirements
Your project repository should contain an "app" directory with a "robo_advisor.py" file inside (i.e. "app/robo_advisor.py").
Your project repository should contain a "README.md" file. The README file should provide instructions to help someone else install, setup, and run your program. This includes instructions for installing package dependencies, for example using Pip. It also includes instructions for setting an environment variable named ALPHAVANTAGE_API_KEY (see "Security Requirements" section below).
Your project repository should contain a file called ".gitignore" which prevents the ".env" file and its secret credentials from being tracked in version control. The ".gitignore" file generated during the GitHub repo creation process should already do this, otherwise you can create your own ".gitignore" file and place inside the following contents:
# .gitignore

# ignore secret environment variable values in the ".env" file:
.env
Finally, your project repository should contain a "data" directory with another ".gitignore" file inside, with the following contents in it to ignore CSV files which will be written inside the data directory:
# data/.gitignore

# h/t: https://stackoverflow.com/a/5581995/670433

# ignore all files in this directory:
*

# except this gitignore file:
!.gitignore
### Security Requirements
Your program will need an API Key to issue requests to the [AlphaVantage API](https://www.alphavantage.co). But the program's source code should absolutely not include the secret API Key value. Instead, you should set an environment variable called ALPHAVANTAGE_API_KEY, and your program should read the API Key from this environment variable at run-time.
You are encouraged to use a "dotenv" approach to setting project-specific environment variables by using a file called ".env" in conjunction with [the dotenv package](/notes/python/packages/dotenv.md). Example ".env" contents:
ALPHAVANTAGE_API_KEY="abc123"
The ".env" file should absolutely not be tracked in version control or included in your GitHub repository. Use a [local ".gitignore" file](https://help.github.com/articles/ignoring-files/#create-a-local-gitignore) for this purpose (see "Repository Requirements" section above).
### Functionality Requirements
Your project should satisfy the functionality requirements detailed in the sections below.
#### Information Input Requirements
The system should prompt the user to input one stock or cryptocurrency symbol (e.g. "MSFT", "AAPL", etc.). It may optionally allow the user to specify multiple symbols, either one-by-one or all at the same time (e.g. "MSFT, AAPL, GOOG, AMZN"). It may also optionally prompt the user to specify additional inputs such as risk tolerance and/or other trading preferences, as desired and applicable.
#### Validation Requirements
Before requesting data from the Internet, the system should first perform preliminary validations on user inputs. For example, it should ensure stock symbols are a reasonable amount of characters in length and not numeric in nature.
If preliminary validations are not satisfied, the system should display a friendly error message like "Oh, expecting a properly-formed stock symbol like 'MSFT'. Please try again." and stop execution.
Otherwise, if preliminary validations are satisfied, the system should proceed to issue a GET request to the [AlphaVantage API](https://www.alphavantage.co/documentation/) to…