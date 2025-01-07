export ORIGIN=base_love_ville_0601
export TARGET=base_love_ville_0601_step_2

# Navigate to the backend server directory
cd reverie/backend_server || {
    echo "Directory not found: generative_agents/reverie/backend_server"
    exit 1
}

# Run the Python script
echo "Starting the Reverie backend server with ORIGIN: $ORIGIN and TARGET: $TARGET"
python reverie.py --origin $ORIGIN --target $TARGET