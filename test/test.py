import yaml
server_config="config/servers.yml"
with open(server_config) as f:
        data=yaml.safe_load(f)
print(data["httpd"])   