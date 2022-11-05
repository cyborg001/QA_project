
provider "azurerm" {
  tenant_id       = "${var.tenant_id}"
  subscription_id = "${var.subscription_id}"
  client_id       = "${var.client_id}"
  client_secret   = "${var.client_secret}"
  features {}
}
terraform {
  backend "azurerm" {
    # use_microsoft_graph  = "false"
    storage_account_name = "tfstate1978"
    container_name       = "tfstate"
    key                  = "key1"
    access_key           = "d2fSuuNZ5xXA4sRZw/dXX3LVSwikzYTDXKuX/Uyl2EBFt2SMfIKgUG1C9Z3W7iTyVqxhgrv6u8DY+ASthM3lTg=="
    
  }
}
module "resource_group" {
  source               = "../../modules/resource_group"
  resource_group       = "${var.resource_group}"
  location             = "${var.location}"
}
module "network" {
  source               = "../../modules/network"
  address_space        = "${var.address_space}"
  location             = "${var.location}"
  virtual_network_name = "${var.virtual_network_name}"
  application_type     = "${var.application_type}"
  resource_type        = "NET"
  resource_group       = "${module.resource_group.resource_group_name}"
  address_prefix_test  = "${var.address_prefix_test}"
  address_prefixes     = "${var.address_prefixes}"
}

module "nsg-test" {
  source           = "../../modules/networksecuritygroup"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "NSG"
  resource_group   = "${module.resource_group.resource_group_name}"
  subnet_id        = "${module.network.subnet_id_test}"
  address_prefix_test = "${var.address_prefix_test}"
}
module "appservice" {
  source           = "../../modules/appservice"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "AppService"
  resource_group   = "${module.resource_group.resource_group_name}"
}
module "publicip" {
  source           = "../../modules/publicip"
  location         = "${var.location}"
  application_type = "${var.application_type}"
  resource_type    = "publicip"
  resource_group   = "${module.resource_group.resource_group_name}"
}

module "vm" {
  source                = "../../modules/vm"
  location              = "${var.location}"
  resource_group        = "${module.resource_group.resource_group_name}"
  application_type      = "${var.application_type}"
  resource_type         = "VirtualMachine"
  subnet_id             = "${module.network.subnet_id_test}"
  public_ip_address_id  = "${module.publicip.public_ip_address_id}"
  username              = "${var.username}"
  key                   = "${var.key}"
  image_id              = "${var.image_id}"            
}