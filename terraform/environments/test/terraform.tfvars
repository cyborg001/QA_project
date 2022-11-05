# Azure subscription vars
subscription_id = "" # your subscription id
client_id = "" # the service principal app name
client_secret = "" # the service principal secret value
tenant_id = "" # the tenant id

# con el sigt command: az ad sp create-for-rbac --role="Contributor" --scopes="/subscriptions/00000000-b55e-45ea-8cc8-0000000000"
# ojo para poder crear otro resource group con esas credenciales el del service principel scope debe ser hasta suscriptions


# Resource Group/Location
location = "eastus"
resource_group = "rg"
application_type = "apptype" # whatever you want like app5carlos. etc.

# Network
virtual_network_name = ""
address_space = ["10.5.0.0/16"]
address_prefix_test = "10.5.1.0/24"
address_prefixes = ["10.5.1.0/24"]

# Ssh key
username = "el-que-quieras"
key = "ssh-rsa ...." # la public key
image_id = "/subscriptions/0000000-0000-0000-0000-000000000000/resourceGroups/NetworkWatcherRG/providers/Microsoft.Compute/images/my-image"