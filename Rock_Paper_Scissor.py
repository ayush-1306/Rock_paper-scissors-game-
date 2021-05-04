from tkinter import *
import random
import pyttsx3
engine = pyttsx3.init() 
game_window = Tk()
game_window.title("Rock Paper Scissors Game(Made By Ayush Sharma)")

player_score = 0
computer_score = 0
options = [('Rock',0), ('Paper',1), ('Scissor',2)]
def player_choice(player_input):
    global player_score, computer_score
    computer_input = get_computer_choice()
    player_choice_label.config(text = 'You Selected : ' + player_input[0])
    engine.say("You Selected" + player_input[0])
    engine.setProperty('rate', 150)
    engine.runAndWait()
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    engine.say("Computer Selected" + computer_input[0])
    engine.setProperty('rate', 150)
    engine.runAndWait()
    if(player_input == computer_input):
        winner_label.config(text = "Tie")
        engine.say("Tie")
        engine.setProperty('rate', 150)
        engine.runAndWait()
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner_label.config(text="You Won!!!")
        engine.say("You win")
        engine.setProperty('rate', 150)
        engine.runAndWait()
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        engine.say("Computer win")
        engine.setProperty('rate', 150)
        engine.runAndWait()
        computer_score_label.config(text='Your Score : ' + str(computer_score))
#Function to Randomly Select Computer Choice
def get_computer_choice():
    return random.choice(options)

#Displaying Game Title
game_title = Label(text = 'Rock Paper Scissors', font = ('gothic',35),bg = 'coral',width = 20)
game_title.pack()
#Label to dispay, who wins each time
winner_label = Label(text = "Let's Start the Game...", fg = 'green', font = (15), pady = 10)
winner_label.pack()
#Displaying player options
player_options = Label(game_window, text = "Your Options : ", width = 12,anchor = 'w',font = (20), fg = 'black')
player_options.place(x = 5,y = 100)
rock_btn = Button(game_window, text = 'Rock', width = 12, bd = 0, bg = 'pink',font = (20), command = lambda: player_choice(options[0]))
rock_btn.place(x = 150,y = 100)
paper_btn = Button(game_window, text = 'Paper', width = 12, bd = 0, bg = 'silver',font = (20), command = lambda: player_choice(options[1]))
paper_btn.place(x = 300,y = 100)
scissors_btn = Button(game_window, text = 'Scissors', width = 12, bd = 0, bg = 'light blue',font = (20), command = lambda: player_choice(options[2]))
scissors_btn.place(x = 450,y = 100)


#Displaying Score and players choice
score_label = Label(game_window, text = 'Score : ', font = (20), fg = 'Black')
score_label.place(x = 5,y =150)
player_choice_label = Label(game_window, text = 'You Selected : ', font = (15))
player_choice_label.place(x = 100,y =150)
player_score_label = Label(game_window, text = 'Your Score : ', font = (15))
player_score_label.place(x = 100,y =180)
computer_choice_label = Label(game_window, text = 'Computer Selected : ', font = (15), fg = 'black')
computer_choice_label.place(x = 320,y =150)
computer_score_label = Label(game_window, text = 'Computer Score : ', font = (15), fg = 'black')
computer_score_label.place(x = 320,y =180)
game_window.geometry('650x250+150+50')
game_window.resizable(False,False)
game_window.iconbitmap(r'C:\Users\Ayush\Downloads\game-console.ico')
game_window.mainloop()