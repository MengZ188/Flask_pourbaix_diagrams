##flask app for pourbaix diagrams generation##

##first to do a very basic tutorial##

from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

if __name__== "__main__":
    app.run()
    
    
