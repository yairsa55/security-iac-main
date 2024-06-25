from waitress import serve
#test
#blablabla
from app import app

serve(app, listen='*:5000')
