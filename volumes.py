#!/usr/bin/env python3
import json
import os
import argparse
import sys

# Standardpfad der permissions.json Datei
default_permissions_file = "permissions.json"

def save_permissions(permissions_file):
    permissions = {}
    
    for name in os.listdir(script_path):
        full_path = os.path.join(script_path, name)
        if os.path.isdir(full_path):
            stat_info = os.stat(full_path)
            permissions[name] = {
                "uid": stat_info.st_uid,
                "gid": stat_info.st_gid,
                "mode": stat_info.st_mode
            }

    with open(permissions_file, 'w') as f:
        json.dump(permissions, f)

    print(f"Permissions saved in {permissions_file}")

def restore_permissions(permissions_file):
    if not os.path.exists(permissions_file):
        print(f"{permissions_file} not found!")
        return

    with open(permissions_file, 'r') as f:
        permissions = json.load(f)

    for name, attrs in permissions.items():
        full_path = os.path.join(script_path, name)
        os.makedirs(full_path, exist_ok=True)
        os.chown(full_path, attrs["uid"], attrs["gid"])
        os.chmod(full_path, attrs["mode"])

    print(f"Permissions restored from {permissions_file}")

def main():
    script_path = os.path.dirname(os.path.realpath(__file__))
    default_permissions_file=os.path.join("permissions.json")
    parser = argparse.ArgumentParser(description='Save or restore file permissions.')
    parser.add_argument('action', choices=['save', 'restore'], help='Action to save or restore permissions')
    parser.add_argument('-f', '--file', default=default_permissions_file, help='Path to the permissions file')

    args = parser.parse_args()


    if args.action == 'save':
        save_permissions(args.file)
    elif args.action == 'restore':
        restore_permissions(args.file)

if __name__ == "__main__":
    main()

