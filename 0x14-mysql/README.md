# MySQL Project

## Overview

This project involves setting up a MySQL database with primary-replica replication and a backup strategy.

## Learning Objectives

- Understand the role and purpose of a database and its replicas.
- Implement a database backup strategy and ensure its effectiveness.

## Requirements

- Use Ubuntu 16.04 LTS.
- Scripts must pass Shellcheck without errors.
- All files should end with a new line.

## Tasks

1. **Install MySQL**: Install MySQL 5.7.x on both web-01 and web-02 servers.
2. **User Configuration**: Create a user `holberton_user` with specific permissions for the checker.
3. **Database Setup**: Set up a database `tyrell_corp` with a table `nexus6` and add an entry.
4. **Replication User**: Create a user `replica_user` for the replica server with appropriate permissions.
5. **Primary-Replica Infrastructure**: Configure MySQL primary on web-01 and replica on web-02.
6. **MySQL Backup**: Write a script to generate a MySQL dump and compress it into a tar.gz archive.

## Servers

- 267497-web-01 | IP: 18.206.198.24
- 267497-web-02 | IP: 54.236.43.182
- 267497-lb-01 | IP: 54.84.62.123

## Plagiarism Notice

Plagiarism is strictly prohibited. All work must be original.

## Author

**Aed10**
