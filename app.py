from flask import Flask

import recommender

app = Flask(__name__)

@app.route('/api/v0/recommendations/<int:id>', methods=['GET'])
def get_recommendations(id):
    """
    Controller for recommendations route.
    
    Arguments:
        id {int} -- Product ID
    """
    print(f"Product ID: {id}")
    return recommender.get_recommendations(id)

if __name__=='__main__':
    app.run()