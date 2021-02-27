import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

cbfeed = [
    {
        'id': '0',
        'type': 'blog-post',
        'title': 'My Introduction to VR Development',
        'description': 'My Introduction to VR Development in Unity',
        'author': 'Clayton Brimm',
        'date': '08.29.2020',
        'body': 'https://www.claybrimm.com/blog/intro-to-vr.html',
    },
    {
        'id': '1',
        'type': 'blog-post',
        'title': "The jobs you won't see on my resume",
        'description': "Interesting jobs I have had before becoming a developer",
        'author': 'Clayton Brimm',
        'date': '09.18.2020',
        'body': 'https://www.claybrimm.com/blog/jobs-you-wont-see.html',
    },
    {
        'id': '2',
        'type': 'image-post',
        'title': 'Unity VR',
        'description': 'A VR bowling game made with UnityVR.',
        'author': 'Clayton Brimm',
        'date': '01.01.2020',
        'body': 'https://i.imgur.com/4w0tFFN.gifv',
    }, 
    {
        'id':'3',
        'type': 'image-post',
        'title': 'Unity Pathfinding',
        'description': 'Pathfinding program created with Unity.',
        'author': 'Clayton Brimm',
        'date': '01.01.2020',
        'body': 'https://i.imgur.com/pl906jf.gifv',
    },
    {
        'id':'4',
        'type': 'image-post',
        'title': 'Unity Pathfinding',
        'description': 'Program that creates completely random mazes with starts and finishes, Made in Unity.',
        'author': 'Clayton Brimm',
        'date': '01.01.2020',
        'body': 'https://i.imgur.com/Om4nZ1l.gifv',
    }, 
]

@app.route('/', methods=['GET'])
def get_data():
    return '''<h1>key-value-API</h1><p>A lightweight NO-SQL database for web development projects</p>'''

@app.route('/api/v1/cb/feed/all', methods=['GET'])
def cbfeed_all():
    return jsonify(cbfeed)
    
app.run()