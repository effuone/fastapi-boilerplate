#!/bin/bash

# Usage function to display help
usage() {
  echo "Usage: $0 -p <db_password>"
  exit 1
}

# Parse command-line arguments for the password
while getopts ":p:" opt; do
  case $opt in
    p)
      DB_PASSWORD=$OPTARG
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      usage
      ;;
  esac
done

# Check if password is set
if [ -z "$DB_PASSWORD" ]; then
  usage
fi

# Export the password to use with psql
export PGPASSWORD=$DB_PASSWORD

# Define database connection parameters
DB_HOST="localhost"
DB_PORT="5432"
DB_USER="app"
DB_NAME="app"
CREATE_SCRIPT="alembic/sql/CreateAll.sql"
LOAD_SCRIPT="alembic/sql/LoadAll.sql"

# Run the CreateAll.sql script
echo "Running CreateAll.sql..."
psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -f $CREATE_SCRIPT
if [ $? -ne 0 ]; then
  echo "Error running CreateAll.sql"
  exit 1
fi

# Run the LoadAll.sql script
echo "Running LoadAll.sql..."
psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -f $LOAD_SCRIPT
if [ $? -ne 0 ]; then
  echo "Error running LoadAll.sql"
  exit 1
fi

echo "Database seeded successfully."
