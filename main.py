#importing the Flask module and creating a Flask web server from the Flask module.
from flask import Flask,render_template

#__name__ means this current file. In this case, it will be main.py. This current file will represent my web application.
#We are creating an instance of the Flask class and calling it app. Here we are creating a new web application.
app = Flask(__name__)

#It represents the default page
@app.route('/')
def home():
    #return "Hello, World !"
    #We imported render_template() method from the flask framework. render_template() looks for a template (HTML file) in the templates folder. Then it will render the template for which you ask. Learn more about render_templates() function.
    return render_template("index.html")

@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/about")
def about():
    return render_template("about.html")

#When you run your Python script, Python assigns the name “__main__” to the script when executed.
#This will run the application. Having debug=True allows possible Python errors to appear on the web page. This will help us trace the errors.
if __name__ == "__main__":
    app.run(debug=True)

#The Flask Framework looks for HTML files in a folder called templates. You need to create a templates folder and put all your HTML files in there.