!#/bin/bash
ansible-playbook ps1_to_file.yml -i hosts --vault-password-file vault_password.txt | \
jq -M '.. | .stdout? // empty' | sed 's/\\r\\n/\\n/g' | sed "s/\\\n/\n/g" | sed "s/\"//g"
