# Azure Table SaS Generation Example

Generate an Azure Account SaS using the Azure Python SDK for accessing Azure Table data.

## Usage

Requires Python 3.

```bash
# Clone the repository
$ git clone git@github.com:jrtknauer/azure_table_example.git
$ cd azure_table_example

# (Optional) Create and activate virtualenv
$ virtualenv .venv

# Install dependencies
$ pip install -r requirements.txt

# Populate the requisite strings in table.py
STORAGE_ACCOUNT_NAME = "..."
STORAGE_ACCOUNT_KEY = "..."
STORAGE_TABLE_NAME = "..."
STORAGE_TABLE_URL = "..."

# Run table.py
$ python table.py
```