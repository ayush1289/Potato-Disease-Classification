#!/bin/bash

# Start the first command in a new terminal window
gnome-terminal -e  --tab --title="Uvicorn" --command="bash -c 'uvicorn main:app --reload'"

# sleep 5

# Start the second command in a new terminal window
gnome-terminal -e  --tab --title="NPM" --command="bash -c 'cd app && npm start run'"
