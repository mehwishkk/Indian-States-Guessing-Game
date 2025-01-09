import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("India States Game")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("states_data.csv")
all_states = data.state.to_list()
print(all_states)


guessed_states = []
while len(guessed_states) < 28:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States correct",
                                       prompt="What's the state's name ?").title()

        print(answer_state)
        if answer_state in all_states:
                #print('got it')
                guessed_states.append(answer_state)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                state_data = data[data.state == answer_state]
                #rint(state_data)
                t.goto(int(state_data.x), int(state_data.y))
                t.write(answer_state)
        if answer_state == "Exit":
                missing_states = []
                for state in all_states:
                        if state not in guessed_states:
                                missing_states.append(state)
                new_data = pd.DataFrame(missing_states)
                new_data.to_csv("states_to_learn.csv")
                break
screen.exitonclick()
