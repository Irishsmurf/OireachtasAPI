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

<a name="documentation-for-api-endpoints"></a>
## 📂 Core API Reference

All requests call the live API endpoint: `https://api.oireachtas.ie/v1`.

| Service Class | Method API | Description / Use Case | Official Specs |
| :--- | :--- | :--- | :--- |
| **`ConstituenciesApi`** | `constituencies()` | Retrieve electoral districts | [Docs](ConstituenciesApi.md) |
| **`DebatesApi`** | `debates()` | Access official debates transcripts | [Docs](DebatesApi.md) |
| **`DivisionsApi`** | `divisions()` | Inspect parliamentary votes and counts | [Docs](DivisionsApi.md) |
| **`HousesApi`** | `houses()` | Query house info (Dáil or Seanad) | [Docs](HousesApi.md) |
| **`LegislationApi`** | `legislation()` | Query active & historic bills and acts | [Docs](LegislationApi.md) |
| **`MembersApi`** | `members()` | Look up details of TDs and Senators | [Docs](MembersApi.md) |
| **`PartiesApi`** | `parties()` | List political parties | [Docs](PartiesApi.md) |
| **`QuestionsApi`** | `questions()` | Query parliamentary questions (PQs) | [Docs](QuestionsApi.md) |

---

<a name="documentation-for-models"></a>
## 📂 Data Models Reference

See the sidebar/navigation tabs for details of all data models returned by the API.

---

## 📬 Contact & Support

* **Official API Portal:** [beta.oireachtas.ie/en/open-data](https://beta.oireachtas.ie/en/open-data)
* **Email:** [open.data@oireachtas.ie](mailto:open.data@oireachtas.ie)
* **License:** [Oireachtas (Open Data) PSI Licence](https://beta.oireachtas.ie/en/open-data/license/)
