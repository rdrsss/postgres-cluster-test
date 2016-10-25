#!/bin/bash

# Setup test database
psql 'create database test_database;'
# Run setup script
psql -f setup.sql
