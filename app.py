from flask import Flask, render_template, request, redirect
import datetime
import pytz # timezone 
import requests
import os
import random
import simplegui



app = Flask(__name__)

COMPUTER_SCORE = 0
HUMAN_SCORE = 0
human_choice = ""
computer_choice = ""


@app.route('/', methods=['GET'])
def home_page():
	return render_template('index.html')

@app.route('/<name>')
def profile(name):
	new_name = name + " is awesome!"
	return render_template('index.html', name=new_name)


@app.route('/add_numbers', methods=['GET','POST'])
def add_numbers_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))
	  if request.method == 'GET':
	  	return render_template('add_numbers.html')
	  elif request.method == 'POST':
  	      print(request.form['text'].split())
  	      list_of_numbers = request.form['text'].split()
  	      try:
  	      	max_number = max(list_of_numbers)
  	      	return render_template('add_numbers.html', result=max_number)
  	      except ValueError:
  	      	return "Easy now! Let's keep it simple! Numbers only please."


@app.route('/shopping_list', methods=['GET','POST'])
def shopping_list_post():
	  # --> ['5', '6', '8']
	  # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('shopping_list.html')
    elif request.method == 'POST':
          print(request.form['text'].split())
          
          shop_list = []
          try:
            for item in request.form['text'].split():
              shop_list.append(item)
	    
            sorted_list = sorted(shop_list)
              
            return render_template('shopping_list.html', result="\n".join([str(item) for item in sorted_list]))
          except ValueError:
            return "Easy now! Let's keep it simple! Just words with a space between them"
          
  	      
@app.route('/time', methods=['GET','POST'])
def time_post():
    # --> ['5', '6', '8']
    # print(type(request.form['text']))

    if request.method == 'GET':
      return render_template('time.html')
    elif request.method == 'POST':
          #print(request.form['text'].split())
          
          #for item in request.form['text'].split():
            #answer = (datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime('Time = ' + '%H:%M:%S' + ' GMT ' + ' Year = ' + '%d-%m-%Y'))
            #answer = datetime.datetime.now().strftime('Time == ' + '%H:%M:%S' + ' Year == ' + '%d-%m-%Y')
            #answer = datetime.datetime.now().strftime('%Y-%m-%d \n %H:%M:%S')
		
	    play_rps()
              
              
            #return render_template('time.html', result=answer)

         

@app.route('/python_apps')
def python_apps_page():
	# testing stuff
	return render_template('python_apps.html')


@app.route('/blog', methods=['GET'])
def blog_page():
  return render_template('blog.html')

def choice_to_number(choice):
    """Convert choice to number."""
    # If choice is 'rock', give me 0
    # If choice is 'paper', give me 1
    # If choice is 'scissors', give me 2
    return {'rock' : 0, 'paper' : 1, 'scissors' : 2}[choice]


def number_to_choice(number):
    """Convert number to choice."""
    # If number is 0, give me 'rock'
    # If number is 1, give me 'paper'
    # If number is 2, give me 'scissors'
    return {0 : 'rock', 1 : 'paper', 2 : 'scissors'}[number]

def random_computer_choice():
    """Choose randomly for computer."""
    
    # lookup random.choice()
    return random.choice(['rock', 'paper', 'scissors'])

def choice_result(human_choice, computer_choice):
    """Return the result of who wins."""
    
    # DO NOT REMOVE THESE GLOBAL VARIABLE LINES.
    global COMPUTER_SCORE
    global HUMAN_SCORE
    
    # based on the given human_choice and computer_choice
    # determine who won and increment their score by 1.
    # if tie, then don't increment anyone's score.
    
    # example code
    # if human_choice == 'rock' and computer_choice == 'paper':
    #    COMPUTER_SCORE = COMPUTER_SCORE + 1
    human_number = choice_to_number(human_choice)
    computer_number = choice_to_number(computer_choice)
    
    if (human_number - computer_number) % 3 == 1:
        COMPUTER_SCORE += 1
    elif human_number == computer_number:
        print('Tie')
    else:
        HUMAN_SCORE += 1
	
# Handler for mouse click on rock button.
# This code is for the GUI part of the game.
def rock():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'rock'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)

def paper():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'paper'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
    
# Handler for mouse click on paper button.
def scissors():
    global human_choice, computer_choice
    global HUMAN_SCORE, COMPUTER_SCORE
    
    human_choice = 'scissors'
    computer_choice = random_computer_choice()
    choice_result(computer_choice, human_choice)
	
# Handler to draw on canvas
def draw(canvas):
    
    try:
        # Draw choices
        canvas.draw_text("You: " + human_choice, [10,40], 48, "Green")
        canvas.draw_text("Comp: " + computer_choice, [10,80], 48, "Red")
        
        # Draw scores
        canvas.draw_text("Human Score: " + str(HUMAN_SCORE), [10,150], 30, "Green")
        canvas.draw_text("Comp Score: " + str(COMPUTER_SCORE), [10,190], 30, "Red")
        
    except TypeError:
        pass
    

# Create a frame and assign callbacks to event handlers
def play_rps():
    frame = simplegui.create_frame("Home", 300, 200)
    frame.add_button("Rock", rock)
    frame.add_button("Paper", paper)
    frame.add_button("Scissors", scissors)
    frame.set_draw_handler(draw)

    # Start the frame animation
    frame.start()


if __name__ == '__main__':
	app.run(debug=True)
