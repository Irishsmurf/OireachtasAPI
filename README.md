# oireachtas-api

[![CI](https://github.com/Irishsmurf/OireachtasAPI/actions/workflows/ci.yml/badge.svg)](https://github.com/Irishsmurf/OireachtasAPI/actions/workflows/ci.yml)

Houses of the Oireachtas Open Data APIs Python SDK.

The Houses of the Oireachtas provides these APIs to allow parliamentary datasets to be retrieved and reused as widely as possible. They are intended to be used in conjunction with [data.oireachtas.ie](https://data.oireachtas.ie), from where datasets can be accessed directly. By using the APIs, users can make metadata queries to identify the specific data they require. New data are available through the API as soon as they are published.

For more information, please visit [beta.oireachtas.ie/en/open-data](https://beta.oireachtas.ie/en/open-data).

- **API version:** 1.0
- **Package version:** 2.0.0

---

## Requirements

- Python 3.8+

## Installation & Usage

### Installing from GitHub

You can install this package directly from GitHub:

```sh
pip install git+https://github.com/Irishsmurf/OireachtasAPI.git
```

### Local Development Installation

Clone the repository and install it in editable mode:

```sh
git clone https://github.com/Irishsmurf/OireachtasAPI.git
cd OireachtasAPI
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt -r test-requirements.txt
pip install -e .
```

---

## Running Tests

We use `pytest` for running our test suite.

### Run Unit Tests (Mocked API calls)

To run tests without making actual network requests to the live Oireachtas API:

```sh
pytest -m "not integration"
```

### Run Integration Tests (Real API calls)

To run the integration tests targeting the live Oireachtas API endpoints:

```sh
pytest -m "integration"
```

### Run All Tests

To run the entire test suite:

```sh
pytest
```

---

## Getting Started

Follow the installation instructions and run the following example script:

```python
import oireachtas_api
from pprint import pprint

# Create an instance of the API class
api_instance = oireachtas_api.ConstituenciesApi()

try:
    # Fetch list of Constituencies (limit to 5 results)
    api_response = api_instance.constituencies(limit=5)
    pprint(api_response)
except oireachtas_api.rest.ApiException as e:
    print("Exception when calling ConstituenciesApi->constituencies: %s\n" % e)
```

---

## Documentation for API Endpoints

All URIs are relative to *https://api.oireachtas.ie/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConstituenciesApi* | [**constituencies**](docs/ConstituenciesApi.md#constituencies) | **GET** /constituencies | Constituencies List
*DebatesApi* | [**debates**](docs/DebatesApi.md#debates) | **GET** /debates | Debates List
*DivisionsApi* | [**divisions**](docs/DivisionsApi.md#divisions) | **GET** /divisions | Divisions
*FiltersApi* | [**members**](docs/FiltersApi.md#members) | **GET** /members | Members
*HousesApi* | [**houses**](docs/HousesApi.md#houses) | **GET** /houses | Houses
*LegislationApi* | [**legislation**](docs/LegislationApi.md#legislation) | **GET** /legislation | Legislation API
*MembersApi* | [**members**](docs/MembersApi.md#members) | **GET** /members | Members
*PartiesApi* | [**parties**](docs/PartiesApi.md#parties) | **GET** /parties | Parties List
*QuestionsApi* | [**questions**](docs/QuestionsApi.md#questions) | **GET** /questions | Questions Filtered by Type Only

---

## Releases and Version Tracking

This repository utilizes GitHub Actions to automate release tracking.

1. Updates are committed to the `master` / `main` branch.
2. When ready for a release, draft a tag matching `v*` (e.g. `v2.0.0`):
   ```sh
   git tag v2.0.0
   git push origin v2.0.0
   ```
3. The **Release Workflow** automatically:
   - Builds Python `wheel` and source distribution packages.
   - Generates release changelog notes.
   - Publishes a new GitHub Release with the build artifacts attached.

## Author

open.data@oireachtas.ie
