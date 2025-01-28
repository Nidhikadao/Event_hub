# Create a virtual environment if it doesn't exist
python3.9 -m venv venv
# Activate the virtual environment
source venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Collect static files
python manage.py collectstatic --noinput
echo "BUILD END"
