cd environment/frontend_server || {
    echo "Directory not found: generative_agents/environment/frontend_server"
    exit 1
}

# Start the Django development server
echo "Starting the server..."
python manage.py runserver
