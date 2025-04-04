import os
from dotenv import load_dotenv
from app import create_app

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

app = create_app()
app.config.from_object(os.getenv('APP_SETTINGS', 'app.config.ProductionConfig').strip('"').strip("'"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
