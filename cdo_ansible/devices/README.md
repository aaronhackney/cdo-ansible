# Secrets and Inventory
We are stashing vaulted secrets in the `tenants` and `devices` directories and importing them into the playbook at runtime by providing the vault-key at runtime. 

We have provided some sample inventory and tenant/device secrets in this repo. While these credentials are encypted, in a "real" production system, one would not want to have those vault secrets stored in a CVS system like github, even though they are encryted. Again, they are here for demonstration purposes only.

## Devices File
This file is only required for ASA and IOS devices. FTD devices do not need a device file. For ASA and IOS files, this is a .yml file with the same name as your CDO Tenant. Your CDO tenant name can be found in CDO under Settings --> General Settings under `Tenant Name`

### Devices keys
The tenants file has 2 keys: 
`username` - The administrative username used to log into your ASA or IOS device. 
`password` - The administrative password used to log into your ASA or IOS device. 

The username and password can be vault-encrypted (recommended) or in clear text.

### How to encrypt strings in ansible
To encrypt your credentials, use the CLI vault tool from ansible. In the below example, `abc1234567890asdfgh` is your CDO API key and `~/.vault_key` is your vault key. Note that you could also use `--ask-vault-password` to be prompted for the password instead. See `ansible-vault encrypt_string --help` for more details.
```
ansible-vault encrypt_string 'abc1234567890asdfgh' --name 'username' --vault-password-file ~/.vault_key
ansible-vault encrypt_string 'abc1234567890asdfgh' --name 'password' --vault-password-file ~/.vault_key
```

### Devices File Example
Copy the output to a .yml file with the same name as the host that you have defines in the inventory file (CLI ansible) or the inventory in Ansible AWX/Tower.

Sample File:
`devices/SanAntonio.yml`
```
---
password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          38663662376536346565636466356266373430313931623034373864623035336639653262333739
          ...
          3838
          
username: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66643161376230393662333963666531313238373738623437393238653133376463323764323730
          ...
          6433