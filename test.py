import json
from subprocess import Popen, PIPE

def get_stdout(data_json, stdout):
    if type(data_json) is list:
        for data in data_json:
            if type(data) is list:
                get_stdout(data_json, stdout)
            elif type(data) is dict:
                for key, value in data.items():
                    if key == 'stdout' and len(value):
                        stdout.append(value)
                    elif type(value) is dict or type(value) is list:
                        get_stdout(value, stdout)
                    else:
                        continue
    if type(data_json) is dict:
        for key, value in data_json.items():
            if key == 'stdout' and len(value):
                stdout.append(value)
            elif type(value) is dict or type(value) is list:
                get_stdout(value, stdout)
            else:
                continue

# .replace('\r\n', "\n")
cmd = "ansible-playbook ps1_to_file.yml -i hosts --vault-password-file vault_password.txt"
cmd = cmd.split()
p = Popen(cmd, stdout=PIPE, stderr=PIPE)
stdout, stderr = p.communicate()
data_stdout = stdout.decode()
data_stderr = stderr.decode()
data_json = json.loads(data_stdout)
stdout = []
get_stdout(data_json, stdout)
print(stdout[0])
