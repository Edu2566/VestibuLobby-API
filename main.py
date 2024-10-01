from flask import Flask
from routes.college_api.college_api import college_api_blueprint
from routes.course_api.course_api import course_api_blueprint
from routes.information_api.information_api import information_api_blueprint
from routes.location_api.location_api import location_api_blueprint
from routes.exams_api.exams_api import exams_api_blueprint
from routes.template_api.template_api import template_api_blueprint

app = Flask(__name__)

app.register_blueprint(college_api_blueprint)
app.register_blueprint(course_api_blueprint)
app.register_blueprint(information_api_blueprint)
app.register_blueprint(location_api_blueprint)
app.register_blueprint(exams_api_blueprint)
app.register_blueprint(template_api_blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
