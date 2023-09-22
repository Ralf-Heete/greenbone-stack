import os
import json

dir_path = "/docker/greenbone/volumes"
permissions_file = "permissions.json"

def save_permissions():
    permissions = {}
    
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        if os.path.isdir(full_path):
            stat_info = os.stat(full_path)
            permissions[name] = {
                "uid": stat_info.st_uid,
                "gid": stat_info.st_gid,
                "mode": stat_info.st_mode
            }

    with open(permissions_file, 'w') as f:
        json.dump(permissions, f)

    print(f"Berechtigungen gespeichert in {permissions_file}")

def restore_permissions():
    if not os.path.exists(permissions_file):
        print(f"{permissions_file} nicht gefunden!")
        return

    with open(permissions_file, 'r') as f:
        permissions = json.load(f)

    for name, attrs in permissions.items():
        full_path = os.path.join(dir_path, name)
        # Verzeichnis erstellen, falls es nicht existiert (exist_ok=True verhindert Fehler bei bereits existierenden Verzeichnissen)
        os.makedirs(full_path, exist_ok=True)
        
        os.chown(full_path, attrs["uid"], attrs["gid"])
        os.chmod(full_path, attrs["mode"])

    print(f"Berechtigungen wiederhergestellt aus {permissions_file}")

if __name__ == "__main__":
    choice = input("Möchten Sie die Berechtigungen speichern oder wiederherstellen? (speichern/wiederherstellen): ")
    if choice == "speichern":
        save_permissions()
    elif choice == "wiederherstellen":
        restore_permissions()
    else:
        print("Ungültige Auswahl!")

