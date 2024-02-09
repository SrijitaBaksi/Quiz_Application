import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random

# List of quiz questions
questions = [
    "The first search engine on the internet is",
    "The first computer virus was known as",
    "Which one is the first web browser invented in 1990",
    "Firewall in a computer is used for",
    "Computer Hard Disk was first introduced in 1956 by",
    "‘Linux’ is an example of",
    "Which company first developed the Java programming language",
    "Number of bits used by the IPv6 address",
    "Which of the following programming languages is used to create programs like applets?",
    "Which programming language is exclusively used for artificial intelligence",
    "What is the speed of the computer measured in?",
    " __ is used to communicate from one city to another",
    "How much is a byte equal to?",
    "In computer world, Trojan refers",
    "Which of the following is the most powerful type of computer?",
    "What is the full form of lP?",
    "What is the full form of PDF?",
    "What does the letter “S” stand for in the Web terminology “HTTPS”?",
    "Who is the founder of Bluetooth?",
    "USB Port stands for:"
]

# List of answer choices for each question
answer_choices = [
    ["Archie", "Google", "Bing", "Yahoo"],
    ["Rabbit", "Elk cloner", "SCA virus", "Creeper program"],
    ["Internet Explorer", "Mosaic", "Mozilla", "Nexus"],
    ["Security", "Data Transmission", "Authentication", "Monitoring"],
    ["Dell", "IBM", "Seagate", "Microsoft"],
    ["Unix", "Windows", "Mac", "Android"],
    ["Sun Microsystems", "Microsoft", "Apple", "IBM"],
    ["32", "64", "128", "256"],
    ["Java", "Python", "C++", "JavaScript"],
    ["Python", "Lisp", "Prolog", "Java"],
    [ "Nanoseconds","Kilo seconds","Gigahertz","Megabytes"],
    ["WAN","MAN","LAN","All of the above"],
    ["16 bits","32 bits","64 bits","8 bits"],
    ["Virus","Malware","Worm","Spyware"],
    ["Super-Micro","Super Conductor","Super Computer","Megaframe"],
    ["Interface program","Interface protocol","Internet program","Internet protocol"],
    ["Printed Document Format","Public Document Format","Portable Document Format","Published Document Format"],
    ["Safe","Secure","Short","Shorter"],
    ["Ericsson","IBM","Apple","Dell"],
    ["United Serial Bus Port"," Universal Serial Bus Port","Universal Sequential Bus Port"," Universal Serial BIOS Port"]
]

# List of correct answers (index corresponding to the correct answer in answer_choices)
answers = [1, 1, 1, 0, 2, 0, 0, 1, 0, 1 ,2 ,0 ,3 ,1 ,2 ,3 ,2 ,1 ,0 ,1 ]

timer_seconds = 50
timer_label = None

indexes = []
score = 0
ques = 0
correct_label = None
incorrect_label = None
flag = False

# Function to update the timer label
def update_timer():  
    global timer_seconds, timer_label,flag
    if flag == False:
        if timer_seconds > 0:
            timer_label.config(text=f"Time Left: {timer_seconds} seconds")
            timer_seconds -= 1
            root.after(1000, update_timer)
        else:
            timer_seconds = 0
            show_result() 

# Function to initialize and start the timer
def start_timer():
    global timer_label
    timer_label = Label(root, text=f"Time Left: {timer_seconds} seconds", font=("Comic sans MS", 14, "bold"), bg="#242c43", fg="white")
    timer_label.place(x=10, y=10)
    update_timer()

# Function to generate random question indexes
def gen():
    global indexes
    while len(indexes) < 5:
        x = random.randint(0, 19)
        if x not in indexes:
            indexes.append(x)

# Function to handle the selection of an answer
def selected(value):
    global user_answer
    user_answer = value

# Function to display correct answer feedback
def correct():
    global f1, correct_label
    correct_label = Label(f1, text="Correct answer, Marks obtained = 5", bg="green", fg="white",
                          font=("Comic sans MS", 18, "bold"))
    correct_label.pack()

# Function to display incorrect answer feedback
def incorrect():
    global f1, incorrect_label
    incorrect_label = Label(f1, text="Wrong answer, Marks obtained = 0", bg="red", fg="white",
                            font=("Comic sans MS", 18, "bold"))
    incorrect_label.pack()

# Function to display poor result feedback
def poor():
    global poor_label
    poor_label = Label(f1, text="Poor result. Try Again!😔", bg="red", fg="white",font=("Comic sans MS", 18, "bold"))
    poor_label.pack(pady=20)

# Function to display average result feedback
def average():
    global average_label
    average_label = Label(f1, text="Average result! Better luck next time 🤔", bg="yellow", fg="black",font=("Comic sans MS", 18, "bold"))
    average_label.pack(pady=20)

# Function to display good result feedback
def good():
    global good_label
    good_label = Label(f1, text="Well done!😎👍", bg="#90EE90", fg="black",font=("Comic sans MS", 18, "bold"))
    good_label.pack(pady=20)

# Function to display excellent result feedback
def excellent():
    global excellent_label
    excellent_label = Label(f1, text="Excellent job!👏😊🎉", bg="green", fg="white",font=("Comic sans MS", 18, "bold"))
    excellent_label.pack(pady=20)

# Function to handle the submission of an answer
def submit():
    global user_answer, correct_label, incorrect_label, score, ques
    
    # Check if the quiz is already completed
    if ques == 5:
        return
        
    if ques < len(indexes):
        if user_answer is not None:
            if user_answer == answers[indexes[ques]]:
                correct()
                score += 5
            else:
                incorrect()
            # Disable the submit button
            submit_btn.config(state=DISABLED)
            # Move to the next question after a delay
            f1.after(1000, next_question)

# Function to move to the next question
def next_question():
    global ques, correct_label, incorrect_label

    if correct_label:
        correct_label.destroy()
    if incorrect_label:
        incorrect_label.destroy()

    if ques < 4:
        ques += 1
        show_question()
        # Re-enable the submit button for the next question
        submit_btn.config(state=NORMAL)
    else:
        show_result()

# Function to display the current question and answer choices
def show_question():
    global lblQuestion, r1, r2, r3, r4, user_answer, ques, radioVar, f1
    p = ques + 1
    lblQuestion.config(text=f"{p} :  {questions[indexes[ques]]}")
    r1['text'] = answer_choices[indexes[ques]][0]
    r2['text'] = answer_choices[indexes[ques]][1]
    r3['text'] = answer_choices[indexes[ques]][2]
    r4['text'] = answer_choices[indexes[ques]][3]
    radioVar.set(-1)
    user_answer = None

# Function to display the final result
def show_result():
    global lblQuestion, r1, r2, r3, r4, user_answer, ques, correct_label, incorrect_label, submit_btn,timer_seconds,flag
    lblQuestion.config(text="Quiz Completed")
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    submit_btn.destroy()

    result_label = Label(f1, text=f"Your Score: {score}", font=("Comic sans MS", 18, "bold"))
    result_label.pack()
    
    if score==0:
        poor()
    elif score==5 or score==10:
        average()
    elif score==15 or score==20:
        good()
    else:
        excellent()
    
    # last_time = timer_seconds
    flag = True
    timer_label = Label(root, text=f"Time Left: {timer_seconds} seconds", font=("Comic sans MS", 14, "bold"), bg="#242c43", fg="white")
    timer_label.place(x=10, y=10)
    
    # Write the name and score
    player_name = nameValue.get()
    with open("score.txt", "a") as file:
        file.write(f"Player Name: {player_name}, Score: {score}\n")

# Function to disable the start button if the name is not entered
def not_start():
    global nameValue
    if nameValue.get()=="":
        startbtn.config(state=Tk.DISABLED)
           
# Function to start the quiz
def start_quiz():
    global lblQuestion, r1, r2, r3, r4, submit_btn, radioVar, f1, img4, img3
    f1 = Frame(
        root,
        bg="#e2db21",
        height=900,
        width=900,
        relief=SUNKEN,
        borderwidth=10
    )
    f1.pack(pady=20)

    lblQuestion = Label(
        f1,
        bg="grey",
        text=f"1 : {questions[indexes[ques]]}",
        font=("consolas", 19),
        justify="center",
        wraplength=400,
        padx=60,
        pady=10
    )  
    lblQuestion.pack(pady=30)

    radioVar = IntVar()
    radioVar.set(-1)

    r1 = Radiobutton(
        f1,
        bg="#e2db21",
        text=answer_choices[indexes[ques]][0],
        font=("Times", 18),
        value=0,
        variable=radioVar,
        command=lambda: selected(0),
    )
    r1.pack(anchor=W, padx=(20, 0), pady=20)

    r2 = Radiobutton(
        f1,
        bg="#e2db21",
        text=answer_choices[indexes[ques]][1],
        font=("Times", 18),
        value=1,
        variable=radioVar,
        command=lambda: selected(1),
    )
    r2.pack(anchor=W, padx=(20, 0), pady=20)

    r3 = Radiobutton(
        f1,
        bg="#e2db21",
        text=answer_choices[indexes[ques]][2],
        font=("Times", 18),
        value=2,
        variable=radioVar,
        command=lambda: selected(2),
    )
    r3.pack(anchor=W, padx=(20, 0), pady=20)

    r4 = Radiobutton(
        f1,
        bg="#e2db21",
        text=answer_choices[indexes[ques]][3],
        font=("Times", 18),
        value=3,
        variable=radioVar,
        command=lambda: selected(3),
    )
    r4.pack(anchor=W, padx=(20, 0), pady=20)

    img3 = Image.open("submit.jpg")
    newimg = img3.resize((160, 35))
    img4 = ImageTk.PhotoImage(newimg)
    submit_btn = Button(f1, image=img4, relief=FLAT, border=0, pady=30, command=submit)
    submit_btn.pack(pady=(0, 10))

    start_timer()

# Function to handle the start button press
def startIsPressed():
    # Destroy the previous widgets and start the quiz
    not_start()
    imageLabel.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    L1.destroy()
    L2.destroy()
    nameEntry.destroy()
    startbtn.destroy()
    gen()
    start_quiz()

# Main GUI setup
root = tkinter.Tk()
root.title("The Quizard")
root.geometry("1300x680")
root.config(background="#242c43")
root.resizable(False, False)

img1 = PhotoImage(file="img1.png")
imageLabel = Label(root, image=img1, relief="sunken", bd=0)
imageLabel.pack()

L1 = Label(root, text="Welcome to our Online Quiz. Let's Go!!!", font=("Comic sans MS", 24, "bold"), bg="#242c43",
           fg="#e2db21")
L1.pack()

L2 = Label(root, text="Enter Your Name : ", font=("Comic sans MS", 18, "bold"), fg="white", bg="#242c43")
L2.pack(pady=25)

nameValue = StringVar()

nameEntry = Entry(root, font=("Comic sans MS", 18, "bold"), textvariable=nameValue, bd=2, relief="solid", width=20)

nameEntry.pack()

img2 = Image.open("img2.jpg")
resize_image = img2.resize((160, 35))
img = ImageTk.PhotoImage(resize_image)
startbtn = Button(image=img, relief=FLAT, border=0, command=startIsPressed)
startbtn.pack(pady=(40, 20))

lblInstruction = Label(root,
                       text="Read the rules carefully. Click start once you are ready!",
                       background="#242c43", fg="white", font=("Consolas", 18, "bold"), justify="center")
lblInstruction.pack(pady=(0, 20))

lblRules = Label(root,
                 text='''1. This quiz contains 5 questions, each question carries 5 marks.\n2. You will get 50 seconds for the entire quiz.\n3. Once you submit it will automatically show the next question.\n4. The quiz will autosubmit once the time is up.\n5. Your score will be displayed in the end. ''',
                 width=1300,
                 font=("Times", 18, "bold"),
                 background="#e2db21",
                 fg="black",
                 pady=20)
lblRules.pack()

root.mainloop()
