export ORIGIN=base_love_ville_explicit_2401_final_2
export TARGET=base_love_ville_explicit_2401_final_3

# Navigate to the backend server directory
cd reverie/backend_server || {
    echo "Directory not found: generative_agents/reverie/backend_server"
    exit 1
}

# Run the Python script
echo "Starting the Reverie backend server with ORIGIN: $ORIGIN and TARGET: $TARGET"
python reverie.py --origin $ORIGIN --target $TARGET