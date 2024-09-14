import models
from config import app

# routes
@app.route("/")
def index():

	return "Hello, it's work!"

if __name__ == "__main__":
	app.run(debug=True)
