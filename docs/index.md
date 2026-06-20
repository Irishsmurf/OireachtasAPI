# Oireachtas API Python SDK

Welcome to the official documentation for the **Houses of the Oireachtas Open Data API - Python SDK**.

This library is a modern, lightweight Python client SDK for querying open parliament data from the national parliament of Ireland (Houses of the Oireachtas).

---

## 🚀 Key Features

* **Modern Python 3 Support:** Fully compatible with Python 3.8+ (legacy Python 2 support has been dropped).
* **Fully Tested:** Upgraded to use `pytest` with a complete suite of unit (mocked) and integration (live API) tests.
* **Open Access:** Works out of the box with the public Oireachtas API endpoints (no authentication tokens required).
* **High Performance:** Optimized request headers and error handling mechanisms.

---

## 🛠 Installation

### Installing via PyPI

You can install the package directly from [PyPI](https://pypi.org/project/oireachtas-api/):

```bash
pip install oireachtas-api
```

### Installing from GitHub

To install the latest development version directly from GitHub:

```bash
pip install git+https://github.com/Irishsmurf/OireachtasAPI.git
```

---

## 💡 Quick Start Example

This code demonstrates how to retrieve the 5 most recent active Constituencies:

```python
import oireachtas_api
from pprint import pprint

# 1. Initialize the simplified client
client = oireachtas_api.Client()

try:
    # 2. Query constituencies (returns standard Python list/dict)
    response = client.constituencies(limit=5)
    
    # 3. Print the API response
    print("--- Oireachtas Constituencies ---")
    pprint(response)
except oireachtas_api.ApiException as e:
    print(f"Failed to query constituencies: {e}")
```

---

<a name="documentation-for-api-endpoints"></a>
## 📂 Core API Reference

All requests call the live API endpoint: `https://api.oireachtas.ie/v1`.

### Simplified Unified Client

The `Client` class consolidates all endpoints into a single wrapper. Method calls return standard Python dictionaries and lists, eliminating the need to interact with verbose auto-generated model objects:

```python
import oireachtas_api

client = oireachtas_api.Client()

# Retrieve constituencies
constituencies = client.constituencies(limit=5)

# Access member information
members = client.members(limit=10)
```

| Method API | Description / Use Case | Official Specs |
| :--- | :--- | :--- |
| **`constituencies()`** | Retrieve electoral districts | [Docs](ConstituenciesApi.md) |
| **`debates()`** | Access official debates transcripts | [Docs](DebatesApi.md) |
| **`divisions()`** | Inspect parliamentary votes and counts | [Docs](DivisionsApi.md) |
| **`houses()`** | Query house info (Dáil or Seanad) | [Docs](HousesApi.md) |
| **`legislation()`** | Query active & historic bills and acts | [Docs](LegislationApi.md) |
| **`members()`** | Look up details of TDs and Senators | [Docs](MembersApi.md) |
| **`parties()`** | List political parties | [Docs](PartiesApi.md) |
| **`questions()`** | Query parliamentary questions (PQs) | [Docs](QuestionsApi.md) |

*Note: The legacy individual service API classes (`ConstituenciesApi`, `MembersApi`, etc.) and data models are still exported for backward compatibility.*

---

<a name="documentation-for-models"></a>
## 📂 Data Models Reference

See the sidebar/navigation tabs for details of all data models returned by the API.

---

## 📬 Contact & Support

* **Official API Portal:** [beta.oireachtas.ie/en/open-data](https://beta.oireachtas.ie/en/open-data)
* **Email:** [open.data@oireachtas.ie](mailto:open.data@oireachtas.ie)
* **License:** [Oireachtas (Open Data) PSI Licence](https://beta.oireachtas.ie/en/open-data/license/)
