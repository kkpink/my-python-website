from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.jinja_env.globals.update(enumerate=enumerate)




@app.route('/')
def home():
    return render_template('index.html',filename='uploads.png')


@app.route('/beginners')
def beginners():
    return render_template('beginners.html',filename='uploads.png')

@app.route('/buildingblocks')
def buildingblocks():
    return render_template('buildingblocks.html')

@app.route('/operators')

def operators():
    return render_template('operators.html')

@app.route('/basicfunc')
def basicfunc():
    return render_template('basicfunc.html')

@app.route('/ifconditions')
def ifconditions():
    return render_template('ifconditions.html')

@app.route('/iteration')
def iteration():
    return render_template('iteration.html')

@app.route('/datatypes')
def datatypes():
    return render_template('datatypes.html')

@app.route('/decomfunc')
def decomfunc():
    return render_template('decomfunc.html')

@app.route('/functions')
def functions():
    return render_template('functions.html')



@app.route('/handling')
def handling():
    return render_template('handling.html')



@app.route('/modules')
def modules():
    return render_template('modules.html')

@app.route('/oop')
def oop():
    return render_template('oop.html')

@app.route('/textfiles')
def textfiles():
    return render_template('textfiles.html')

@app.route('/basicfunct')
def basicfunct():
    return render_template('basicfunct.html')




@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = [
        {
            'question': 'What does an interpreter do?',
            'options': ['Translates and runs code line by line', 'Compiles all code at once', 'Saves source as .exe'],
            'answer': 'Translates and runs code line by line'
        },
        {
            'question': 'Which keyword defines a function in Python?',
            'options': ['def', 'fun', 'function'],
            'answer': 'def'
        },
        {
            'question': 'Which keyword defines a class in Python?',
            'options': ['def', 'break', 'class'],
            'answer': 'class'
        },
        {
            'question': 'What does the __init__ method do?',
            'options': ['initializing a function', 'initializing a class', 'initializing a object'],
            'answer': 'initializing a object'
        },
        {
            'question': 'How do you defin a tuple?',
            'options': ['with ()', 'with []', 'with {}'],
            'answer': 'with ()'
        },
        {
            'question': 'Which data type is mutable',
            'options': ['lists', 'tuples', 'strings'],
            'answer': 'lists'
        },
        {
            'question': 'Which is a float',
            'options': ['34', '3.14', 'Hello World'],
            'answer': 'def'
        },
        {
            'question': 'What is a attribute error?',
            'options': ['when you divide by 0', 'when you accses a feature of an object that dosnt exist', 'when you preform an option of two incompatable types'],
            'answer': 'def'
        }

    ]

    score = 0
    feedback = None

    if request.method == 'POST':
        for i, q in enumerate(questions):
            user_answer = request.form.get(f'q{i}')
            if user_answer == q['answer']:
                score += 1
        feedback = f"You scored {score} out of {len(questions)}"

    return render_template('quiz.html', questions=questions, feedback=feedback)




if __name__ == '__main__':
    app.run(debug=True)