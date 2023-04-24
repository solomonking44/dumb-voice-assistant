from flask import Flask, render_template, request
from flask_restful import Api, Resource
import pyttsx3


app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return render_template('index.html')
    

class Profile(Resource):    
    
    # if request.method == 'POST':
    with app.test_request_context():
    
        data = request.form('text')
        print(data)

            
        try:
            engine = pyttsx3.init()
            engine.say(text)
            engine.runAndWait()  
        except ImportError:
            engine = None
            print(data)
            print("Engine failed to initialise")
        
    
    
api.add_resource(Profile, '/profile')
    

if __name__ == '__main__':
    app.run()
