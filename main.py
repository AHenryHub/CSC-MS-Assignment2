from flask import Flask, jsonify, request
import random
app = Flask(__name__)

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    
    #create a json array of jokes
    jokes = ["I invented a new joke: plagiarism!","Did you hear about the claustrophobic astronaut? He just needed a little space.","Where are average things manufactured? The satisfactory.","What sits at the bottom of the sea and twitches? A nervous wreck.","What does a nosy pepper do? Get jalapeno business!","How does Moses make tea? He brews.","What did the 0 say to the 8? Nice belt!","Why did the yogurt go to the art exhibit? Because it was cultured.","What do you get from a pampered cow? Spoiled milk.","A bacterium got his car fixed. It was micro-serviced!"]
    #@AHenryHub
    js = {}
    #request user for an integer value to get the number of jokes to send
    number = int(request.args.get('num',default=1))
    for i in range(number):
        name = 'joke'+str(i+1)
        jonk = random.choice(jokes)
        js[name] = jonk 
    #
    return jsonify(js)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
