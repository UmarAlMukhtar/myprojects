print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

questions_answers = {
    "What does CPU stand for? " : "central processing unit", 
    "What does GPU stand for? " : "graphics processing unit",
    "What does RAM stand for? " : "random access memory",
    "What does PSU stand for? " : "power supply",
    }
for question, answer in questions_answers.items():
    guess = input(question)
    if guess.lower() == answer:
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
