from flask import Flask, render_template, Markup
from utils import occupation
import csv


myApp = Flask(__name__)

@myApp.route('/')

def root():
    return render_template('base.html')

@myApp.route('/occupations')
def occupations():
    return render_template('occupations.html',table = makeTable(), jobs = Markup("<h1>List of jobs</h1>"), randomJob = Markup("<p> Random Job: " + occupation.pick() + "</p>"))

'''def pick():
    #read file
    file = csv.reader(open('occupations.csv','rU'))
    occupations = []
    next(file)
    for row in file:
        if row[0] == "Total":
            break
        percentage = int(float(row[1]) * 10)
        for i in range(0,percentage):
            occupations.append(row[0])
    #pick occupation
    num = random.randint(0,len(occupations) - 1)
    return occupations[num]'''

def makeTable():
    file = csv.reader(open('data/occupations.csv','rU'))
    output = '<table border="1">'
    for row in file:
        output += '<tr><td>' + row[0] + '</td> <td>' + row[1] +' </td>'
    output += '</table>'
    return Markup(output)


if __name__ == '__main__':
    myApp.debug = True
    myApp.run()
