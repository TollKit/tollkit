from flask_app import app

from flask_app.controllers import admins_controller, tollkits_controller

# .gitignore agregado

if __name__== "__main__":
    app.run(debug=True)

