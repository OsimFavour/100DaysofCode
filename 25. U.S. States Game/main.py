import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=735, height=495)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data_file = pandas.read_csv("50_states.csv")
states = data_file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

	answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
	guessed_states.append(answer_state)
	if answer_state == "Exit":
		missing_states = [state for state in states if state not in guessed_states]
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("states_to_learn.csv")
		break
	if answer_state in states:
		t = turtle.Turtle()
		t.hideturtle()
		t.penup()
		state_data = data_file[data_file.state == answer_state]
		t.goto(x=int(state_data.x), y=int(state_data.y))
		t.write(answer_state)
