from app import create_app
from app.config import Config, DevelopmentConfig

app = create_app()
#app.config.from_object(Config)
app.config.from_object(DevelopmentConfig)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
