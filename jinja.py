from flask import Flask, render_template
import random

app = Flask(__name__)

inStream = open('occupations.csv','r')
occupation = inStream.readlines()
inStream.close()

occupations = {}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def store(string):
    for data in occupation:
        stripped = data.rstrip() #stripped data of /n
        temp = stripped.split(',')
        if is_number(temp[1]):
            occupations[temp[0]] = float(temp[1])

store(occupations) #create dictionary
occupations.pop('Total', None)
occupations.pop('Job Class', None)

def randomize():
    return random.choice(occupations.keys())



@app.route("/") 
def a():
    return "<a href = '/occupations'> Occupation Randomizer </a>"


@app.route("/occupations")
def occupy():
    return render_template('table.html', collection = occupations, job = randomize())

if __name__ == "__main__":
    app.debug = True;
    app.run()
