# Azure Table Account SaS Generation Example
# MSFT Azure Create Account SaS Documentation:
# https://learn.microsoft.com/en-us/rest/api/storageservices/create-account-sas
# Constructing SaS URIs by hand is error prone, and the signature needs to
# be generating by encryption anyway. Use the Python (or any other of the 
# programmatic Azure SDKs) instead.
#
# Python SDK Documentation for generate_account_sas:
# https://azuresdkdocs.blob.core.windows.net/$web/python/azure-data-tables/12.4.1/azure.data.tables.html?highlight=generate_#azure.data.tables.generate_account_sas

import datetime

from azure.core.credentials import AzureNamedKeyCredential, AzureSasCredential
import azure.data.tables as aztables


# Azure requirements.
# The STORAGE_ACCOUNT_KEY must belong to the storage account specified by
# STORAGE_ACCOUNT_NAME. Note that all Azure storage accounts must have unique
# names on creation, so unlike other Azure service credentials the
# subscription/tenant/client ID is not required here.
STORAGE_ACCOUNT_NAME = ""
STORAGE_ACCOUNT_KEY = ""

assert STORAGE_ACCOUNT_NAME and STORAGE_ACCOUNT_KEY

# Azure table name and endpoint. These are not used as part of SaS generation
# but rather to validate the SaS URI. The table should exist in the storage
# account being used to generate the SaS URI.
STORAGE_TABLE_NAME = ""
STORAGE_TABLE_URL = ""

assert STORAGE_TABLE_NAME and STORAGE_TABLE_URL

# generate_account_sas expirt expects either a formatted timestamp, or a
# Python datetime object. A default expiry date has been provided - change
# as needed.
SAS_EXPIRY = datetime.datetime(year=2023, month=1, day=1)

assert SAS_EXPIRY

# Generate the Account SaS with minimal permissions - in this case the
# generated URI will enable users to perform READ operations on objects within
# the storage account (e.g. Azure Tables) up to the expiry date.
# NOTE: Account SaS URIs are revoked upon rotation of the storage account key
# used to generate them. See https://learn.microsoft.com/en-us/rest/api/storageservices/create-service-sas#revoke-a-sas
# for more information on how to revoke a SaS.
account_sas = aztables.generate_account_sas(
    credential=AzureNamedKeyCredential(name=STORAGE_ACCOUNT_NAME, key=STORAGE_ACCOUNT_KEY),
    resource_types=aztables.ResourceTypes(object=True),
    permission="r",
    expiry=SAS_EXPIRY
)

# Verify the SaS URI by connecting to the table with the generated URI, query
# for entries, and print them to the stdout.
table_service_client = aztables.TableServiceClient(
    endpoint=STORAGE_TABLE_URL,
    credential=AzureSasCredential(account_sas)
)

table_client = table_service_client.get_table_client(table_name=STORAGE_TABLE_NAME)
entries = table_client.query_entities("")

for entry in entries:
    print(entry)
