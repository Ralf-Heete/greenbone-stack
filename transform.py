#!/bin/env python
import os
import yaml

BASE_PATH = "/docker/greenbone/volumes"  # Basispfad für anonyme Volumes

def transform_and_create_dirs(compose_data):
    for service, service_data in compose_data['services'].items():
        if 'volumes' in service_data:
            for index, volume in enumerate(service_data['volumes']):
                # Split bei ':' und nur den Host-Pfad nehmen
                host_path, container_path = volume.split(':', 1)

                # Wenn der Pfad nicht mit einem '/' beginnt, handelt es sich wahrscheinlich um ein anonymes Volume
                if not host_path.startswith('/'):
                    new_host_path = os.path.join(BASE_PATH, host_path)
                    os.makedirs(new_host_path, exist_ok=True)
                    print(f"Verzeichnis {new_host_path} erstellt.")
                    # Ersetzen des alten Pfads durch den neuen im YAML
                    service_data['volumes'][index] = new_host_path + ":" + container_path

    return compose_data

if __name__ == '__main__':
    with open('docker-compose.yaml', 'r') as original_file:
        compose_data = yaml.safe_load(original_file)

    new_compose_data = transform_and_create_dirs(compose_data)

    with open('new_docker-compose.yaml', 'w') as new_file:
        yaml.safe_dump(new_compose_data, new_file)

    print("Neue docker-compose Datei als 'new_docker-compose.yaml' erstellt.")

