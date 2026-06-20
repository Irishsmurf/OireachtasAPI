# Houses of the Oireachtas Open Data API - Python SDK

[![Build Status](https://github.com/Irishsmurf/OireachtasAPI/actions/workflows/ci.yml/badge.svg)](https://github.com/Irishsmurf/OireachtasAPI/actions/workflows/ci.yml)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](#)
[![Python Version](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue.svg)](#)

A modern, lightweight Python client SDK for retrieving and querying open parliament data from the national parliament of Ireland (Houses of the Oireachtas).

This client SDK makes metadata queries easy, allowing you to discover and locate specific official documents, bills, members, votes (divisions), and debates. Output formats point directly to XML/PDF datasets hosted at [data.oireachtas.ie](https://data.oireachtas.ie).

---

## 🚀 Key Features

* **Modern Python 3 Support:** Fully compatible with Python 3.8+ (legacy Python 2 support has been dropped).
* **Fully Tested:** Upgraded to use `pytest` with a complete suite of unit (mocked) and integration (live API) tests.
* **Open Access:** Works out of the box with the public Oireachtas API endpoints (no authentication tokens required).
* **Automated CI/CD:** GitHub Actions verify compatibility on every push and automatically build & publish new GitHub Releases when tags are created.

---

## 🛠 Installation

### Installing directly from GitHub

To install the latest release directly from GitHub:
```bash
pip install git+https://github.com/Irishsmurf/OireachtasAPI.git
```

### Local Development Setup

To clone the repository and install it in editable mode with development dependencies:
```bash
# Clone the repository
git clone https://github.com/Irishsmurf/OireachtasAPI.git
cd OireachtasAPI

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install requirements
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt -r test-requirements.txt
pip install -e .
```

---

## 💡 Quick Start Example

This code demonstrates how to retrieve the 5 most recent active Constituencies:

```python
import oireachtas_api
from pprint import pprint

# 1. Initialize the client
client = oireachtas_api.ConstituenciesApi()

try:
    # 2. Query constituencies (limiting to 5 results)
    response = client.constituencies(limit=5)
    
    # 3. Print the API response
    print("--- Oireachtas Constituencies ---")
    pprint(response)
except oireachtas_api.rest.ApiException as e:
    print(f"Failed to query constituencies: {e}")
```

---

## 📂 Core API Reference

All requests call the live API endpoint: `https://api.oireachtas.ie/v1`.

| Service Class | Method API | Description / Use Case | Official Specs |
| :--- | :--- | :--- | :--- |
| **`ConstituenciesApi`** | `constituencies()` | Retrieve electoral districts | [Docs](docs/ConstituenciesApi.md) |
| **`DebatesApi`** | `debates()` | Access official debates transcripts | [Docs](docs/DebatesApi.md) |
| **`DivisionsApi`** | `divisions()` | Inspect parliamentary votes and counts | [Docs](docs/DivisionsApi.md) |
| **`HousesApi`** | `houses()` | Query house info (Dáil or Seanad) | [Docs](docs/HousesApi.md) |
| **`LegislationApi`** | `legislation()` | Query active & historic bills and acts | [Docs](docs/LegislationApi.md) |
| **`MembersApi`** | `members()` | Look up details of TDs and Senators | [Docs](docs/MembersApi.md) |
| **`PartiesApi`** | `parties()` | List political parties | [Docs](docs/PartiesApi.md) |
| **`QuestionsApi`** | `questions()` | Query parliamentary questions (PQs) | [Docs](docs/QuestionsApi.md) |

---

## 🧪 Testing Guide

We use `pytest` for unit and integration tests.

### 1. Isolated Unit Tests (Mocked Network)
To run local test stubs using mock API responses (extremely fast, offline-safe):
```bash
pytest -m "not integration"
```

### 2. Live Integration Tests
To verify compatibility against the real, live Oireachtas API endpoints:
```bash
pytest -m "integration"
```

### 3. Run the Whole Test Suite
To run all tests:
```bash
pytest
```

---

## 🏷 Release Automation

This project tracks official releases automatically:
1. Ensure your version code is up to date in [setup.py](setup.py).
2. Commit your changes and tag the master branch:
   ```bash
   git tag v2.0.0
   git push origin v2.0.0
   ```
3. The **Release Workflow** will automatically build the package wheels and publish a drafted GitHub Release with build assets attached.

---

## 📬 Contact & Support

* **Official API Portal:** [beta.oireachtas.ie/en/open-data](https://beta.oireachtas.ie/en/open-data)
* **Email:** open.data@oireachtas.ie
