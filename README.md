# robo-advisor project

A solution for the ["Robo Advisor" project](https://github.com/prof-rossetti/intro-to-python/blob/master/projects/robo-advisor/README.md)

Issues requests to the [AlphaVantage Stock Market API](alphavantage.co/) in order to provide automated stock or cryptocurrency trading recommendations.

## Prerequisites

+ Anaconda 3.7
+ Python 3.7
+ Pip

## Installation
Clone or download [this repository](https://github.com/sma299/robo-advisor) onto your computer. Then navigate there from the command line:

```sh
cd robo-advisor
```
Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env". From inside the virtual environment, install package dependencies:

```sh
pip install requests python-dotenv matplotlib
```

## Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://alphavantage.co/support/#api-key) (e.g. "abc123").


## Usage
 
Run the recommendation script:

```py
python app/robo_advisor.py
```

## Tests

Install pytest package (first time only):
``` sh
pip install pytest
```

Run tests:
```sh
pytest --disable-pytest-warnings
```

## [License](/LICENSE.md)
