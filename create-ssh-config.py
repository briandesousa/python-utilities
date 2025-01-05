#!/usr/bin/env python3
"""
This script generates SSH configuration files that can be included in a top level SSH config file.

Usage:
    Modify hosts and default values in main() function as required.
    Run the script to create SSH config files in specified folder.
    Add an include statement to your top-level SSH config file (i.e. ~/.ssh/config):
    ```
    Include ~/.ssh/config.d/*
    ```
"""

ssh_config_template = '''\
Host {host}
    HostName {hostname}
    Port {port}
    User {username}
'''

def get_ssh_config(host, hostname, port, username):
    return ssh_config_template.format(host=host, hostname=hostname, port=port, username=username)

def write_files(hosts, ssh_config_dir, ssh_port, ssh_username):
    for host, hostname in hosts.items():
        with open(ssh_config_dir + host, "w", encoding="utf-8") as file:
            file.write(get_ssh_config(host, hostname, ssh_port, ssh_username))

def main():
    hosts = {
        "host1": "127.0.0.1",
        "host2": "127.0.0.1",
        "host3": "127.0.0.1"
    }
    write_files(hosts, "./config.d/", "22", "username")

if __name__ == "__main__":
    main()