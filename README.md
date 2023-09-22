# Greenbone Stack with Filesystem Volumes

## Overview
The Greenbone Stack in this setup utilizes filesystem volumes, also known as bind mounts, to persistently store and manage data. Unlike anonymous volumes, which are automatically created in a predefined Docker path, filesystem volumes allow the user to specify the exact path on the host's file system where data should be stored. This grants the user more control over the storage location and access to the data.

## Advantages of Filesystem Volumes

1. **Control**: Users have full control over the data's storage location, making it easier to manage security and backup processes.
2. **Easy Data Access**: Data in filesystem volumes can be accessed directly via the host's file system path, simplifying browsing and management.
3. **Portability**: Moving data between systems or creating backups is more straightforward since the data is stored in a user-defined path, rather than a Docker-managed one.

## Implementation in the Greenbone Stack
In this specific Greenbone setup, certain services have been configured to utilize filesystem volumes for data storage. This is defined within the `docker-compose.yaml` file. Directories under the `volumes` folder house the data for the various services of the stack. It's crucial to correctly set the permissions for these directories as they contain the containers' persistent data.
