# Secrets and Inventory
We are stashing vaulted secrets in the `tenants` and `devices` directories and importing them into the playbook at runtime by providing the vault-key at runtime. 

We have provided some sample inventory and tenant/device secrets in this repo. While these credentials are encypted, in a "real" production system, one would not want to have those vault secrets stored in a CVS system like github, even though they are encryted. Again, they are here for demonstration purposes only.

## Tenants File
This is a .yml file with the same name as your CDO Tenant. Your CDO tenant name can be found in CDO under Settings --> General Settings under `Tenant Name`

### Tenant keys
The tenants file has 2 keys: 
`cdo_region` - the region where your CDO tenant resides. At this time, the regions are:
- www.defenseorchestrator.com
- www.defenseorchestrator.eu
- apj.cdo.cisco.com

`api_key` - The CDO API generate in CDO under Settings --> User Management. This key can either be vault encrypted (recommended) or in clear text.

### How to encrypt strings in ansible
To encrypt your credentials, use the CLI vault tool from ansible. In the below example, `abc1234567890asdfgh` is your CDO API key and `~/.vault_key` is your vault key. Note that you could also use `--ask-vault-password` to be prompted for the password instead. See `ansible-vault encrypt_string --help` for more details.
```
ansible-vault encrypt_string 'abc1234567890asdfgh' --name 'api_key' --vault-password-file ~/.vault_key
```

### Tenants File Example
Copy the output to a file with the same name as your CDO Tenant (CDO tenant name can be found in CDO under Settings --> General Settings under `Tenant Name`)

Sample File:
`tenants/CDO_My_Tenant.yml`
```
---
cdo_region: www.defenseorchestrator.com
api_key: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          39313534656666353037303936353736343631313938313339633439303265306361623936366561
          3334353663666364393463646662366263363733373938360a653666326432663235636437613363
          62326130353233623130623636323435396334376664313333376166366531336666376631616365
          3534333033613863610a356433316638646636393734653465626536383935303739396139346435
          64323165353137326130633039383863646139323863326134633633613535326434616439633362
