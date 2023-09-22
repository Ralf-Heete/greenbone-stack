import os

def create_directory(path, uid, gid):
    try:
        os.makedirs(path, exist_ok=True) # Erstellt das Verzeichnis, wenn es nicht existiert
        os.chown(path, uid, gid)         # Ändert den Eigentümer des Verzeichnisses
        print(f"Verzeichnis {path} erfolgreich erstellt und Eigentümer geändert.")
    except Exception as e:
        print(f"Fehler beim Erstellen oder Ändern des Verzeichnisses {path}: {e}")

def main():
    dirs_to_create = [
        ('cert_data_vol', 0, 0),
        ('data_objects_vol', 0, 0),
        ('gpg_data_vol', 1001, 1001),
        ('gvmd_data_vol', 1001, 1001),
        ('gvmd_socket_vol', 1001, 1001),
        ('notus_data_vol', 1001, 1001),
        ('ospd_openvas_socket_vol', 1001, 1001),
        ('psql_data_vol', 104, 106),
        ('psql_socket_vol', 104, 106),
        ('redis_socket_vol', 100, 101),
        ('scap_data_vol', 0, 0),
        ('syslog_socket_vol', 0, 0),
        ('syslog_vol', 0, 0),
        ('vt_data_vol', 0, 0)
    ]

    for (path, uid, gid) in dirs_to_create:
        create_directory(path, uid, gid)

if __name__ == '__main__':
    main()

