from waitress import serve
#test
from app import app

serve(app, listen='*:5000')
