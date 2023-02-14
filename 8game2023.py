import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
size = (1280, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Science Quiz: Battle Against the Teachers")

# Initialize variables for the player's score and lives
score = 0
lives = 3

# Create a list of questions and corresponding answers
questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris",
        "options": ["Paris", "London", "Rome", "Berlin"]
    },
    {
        "question": "What is the largest planet in the solar system?",
        "answer": "Jupiter",
        "options": ["Jupiter", "Saturn", "Uranus", "Neptune"]
    },
    {
        "question": "What is the smallest country in the world?",
        "answer": "Vatican City",
        "options": ["Vatican City", "Monaco", "San Marino", "Andorra"]
    }
]

# Create a font object - for writing in the pygame later
font = pygame.font.Font(None, 25)

# Create a variable to control the game loop
running = True

# Use a while loop to iterate through each question
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the current question and shuffle the options
    current_question = questions[score]
    random.shuffle(current_question["options"])

    # Draw the question
    question_text = font.render(current_question["question"], 1, (0, 0, 0))
    screen.blit(question_text, (50, 50))

    # Draw the options available -see before
    for i, option in enumerate(current_question["options"]):
        option_text = font.render(f"{chr(ord('A')+i)}) {option}", 1, (0, 0, 0))
        screen.blit(option_text, (50, 150+50*i))

    # Draw the score and lives
    score_text = font.render("Score: " + str(score), 1, (0, 0, 0))
    screen.blit(score_text, (500, 50))
    lives_text = font.render("Lives: " + str(lives), 1, (0, 0, 0))
    screen.blit(lives_text, (500, 100))

    # Update the display
    pygame.display.update()

    # Get player's answer
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.unicode.upper() in 'ABCD':
                    player_answer = event.unicode.upper()
                    break
        else:
            continue
        break
    # Check if the player's answer is correct or incorrect
    if player_answer:
        if current_question["options"][ord(player_answer) - ord('A')] == current_question["answer"]:
            print("Correct! You strike a blow to the teacher's ego!")
            score += 1  # increment the score if the answer is correct
            if score == len(questions):
                running = False
            else:
                print("Score:", score)
                print("Lives:", lives)
        else:
            print("Incorrect. The teacher scoffs at your ignorance.")
            lives -= 1  # decrement the lives if the answer is incorrect
            if lives == 0:
                running = False
                print("Sorry, you lose. The teacher mock your defeat.")

    if not running:
        end_text = "Congratulations! You win!" if score == len(
            questions) else "Sorry, you lose. The teacher mocks your defeat."
        end_text = font.render(end_text, 1, (0, 0, 0))
        screen.blit(end_text, (50, 400))
        pygame.display.update()

        play_again_text = font.render("Do you want to play again? (Y/N)", 1, (0, 0, 0))
        screen.blit(play_again_text, (50, 450))
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.unicode.upper() == 'Y':
                        score = 0
                        lives = 3
                        running = True
                        break
                    elif event.unicode.upper() == 'N':
                        pygame.quit()
                        quit()
            else:
                continue
            break