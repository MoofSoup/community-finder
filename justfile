baml:
    # Refresh the BAML client files
    uv run baml-cli generate
    
setup:
    # Setting up project with UV package manager
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Copy .env.sample into .env without overwriting
    cp --no-clobber .env.sample .env
    # Creating a virtual environment
    uv venv

dev: baml
    # Run web server, watching for changes 
    uv run uvicorn baml_neo4j_fastapi.app:app --reload

ping:
    # Ping the dev server to check API
    curl -X GET -H "Content-Type: application/json" http://localhost:8000/