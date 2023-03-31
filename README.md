# CDO and Ansible

## Purpose
The purpose of this compilation is to  illustrate ways that Ansible can be used to manage a number of devices and tenants in Cisco Defense Orchestrator.

## Requirements
See requirements.txt for the required python packages needed to run these playbooks.
 
## Project Contents
This is an assortment of roles, scripts, sample inventory, and playbooks for interacting with Cisco Defense Orchestrator (CDO). These examples use the Ansible playbook model where we define CDO tenants' and managed devices' settings using inventory files. I am not using host_vars and group_var directory as I want to be able to use this same playbook in both ansible-playbook cli as well as with ansible tower. 

## Secrets and Inventory
We are stashing vaulted secrets in the `tenants` and `devices` directories and importing them into the playbook at runtime by providing the vault-key at runtime. 

I have provided some sample inventory and tenant/device secrets in this repo. While these credentials are encypted, in a "real" production system, one would not want to have those vault secrets stored in a CVS system like github, even though they are encryted. Again, they are here for demonstration purposes only.

## Using the Ansible CLI
Once you have ansible-vault encrypted your API key and ASA/IOS passwords and put them in the appropriate files in `tenants` and `devices` and created your inventory file `inventory`, all that is left is to run the playbook. Here is an example of how one might call the file.
```
ansible-playbook -i inventory cdo_onboard.yml --vault-password-file ~/.vault_key
```

## Using Ansible Tower/AWX
You will need to import the inventory file into Tower/AWX (Tower from this point forward). You will need to the group (which represents your tenant) to be associated with the hosts (devices) that belong to that tenant. You will specify your vault key in Tower as part of your project.

See the README files in each of the various locations in the project for details.
