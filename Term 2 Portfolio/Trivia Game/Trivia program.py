#Parker Dean
#1-2-19
#Trivia Challenge

#Triviva game that reads a plain text file
import sys

def open_file(file_name,mode):
    #Open a file
    try:
        the_file = open(file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    #Return next line form the trivia file, formatted.
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    #Return the next block of data form the trivia file
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answer = next_line(the_file)
        answers.append(answer) 
    correct = next_line(the_file)
    if correct:
        correct = correct[0]     
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation


def welcome(title):
    #Welcome the player and get his/her name.
    print("\t\tWelcome to the Trivia Challenge!\n")
    print("\t\t"+ title + "\n")


def main():
    the_file = open_file("test_file.txt","r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i+1,":" , answers[i])
        user_answer = input("Enter the number of the correct answer: ")
        if user_answer == correct:
            print("That was correct, you get +1 point")
            score += 1
        else:
            print("That was incorrect, you get nothing")
        print(explanation)
        print("Score:", score, "\n")
        category, question, answers, correct, explanation = next_block(the_file)
    print("That is the last question, your final score is", score)
    input("Hit enter to exit")
        
main()
