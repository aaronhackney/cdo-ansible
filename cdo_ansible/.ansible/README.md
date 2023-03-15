# Ansible Inventory
This is a sample of the inventory scheme used in the example playbooks. This is just one imagining of how one might organize their inventory. Of couse, this could all just be jammed into a single inventory file, but I wanted to deomstrate how this might be implemented in a more scalable way.

The password files named `vault` have been ansible-vault encrypted with sample data to provide an example of how one might store the inventory credentials in a more secure manner than a clear text file or environment variables. Of course in a "real" production system, one would not want to have those vault files stored in a CVS system like github, even though they are encryted. Again, they are here for demonstration purposes only.

The inventory file `inventory` contains groups. These groups align to CDO tenants with a list of hosts (devices) for each tenant. A host may only live in one tenant in CDO.

In the `group_vars` for each tenant, we will find the CDO API key for that tenant that we will use for the CDO API. In the `host_vars`, we have the individual device usernames/passwords (ansible vault encrypted), along with other host level settings like IP addresses and license entitlements.


