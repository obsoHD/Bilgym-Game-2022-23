import pygame
import random
import time

# Initialize pygame
pygame.init()

# Initialize mixer
pygame.mixer.init()

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

# Load custom font
font = pygame.font.Font("Repositary/OpenSans-Regular.ttf", 25)

# Load sound effects
correct_sound = pygame.mixer.Sound("Repositary/correct-sound.wav")
incorrect_sound = pygame.mixer.Sound("Repositary/incorrect-sound.wav")

# Load and play background music
pygame.mixer.music.load("Repositary/background-music.mp3")
pygame.mixer.music.play(-1)  # -1 for looping the music

playing = True

while playing:
    # Reset the game variables
    score = 0
    lives = 3
    running = True

    # Your main game loop starts here
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen with a custom background color
        background_color = (200, 200, 255)
        screen.fill(background_color)

        # Get the current question and shuffle the options
        current_question = questions[score]
        random.shuffle(current_question["options"])

        # Draw the question with a custom text color
        text_color = (0, 0, 128)
        question_text = font.render(current_question["question"], 1, text_color)
        screen.blit(question_text, (50, 50))

        # Draw the options available - see before
        for i, option in enumerate(current_question["options"]):
            option_text = font.render(f"{chr(ord('A') + i)}) {option}", 1, text_color)
            screen.blit(option_text, (50, 150 + 50 * i))

        # Draw the score and lives
        score_text = font.render("Score: " + str(score), 1, text_color)
        screen.blit(score_text, (500, 50))
        lives_text = font.render("Lives: " + str(lives), 1, text_color)
        screen.blit(lives_text, (500, 100))

        # Update the display
        pygame.display.update()

        # Get player's answer
        player_answer = None
        while player_answer is None:
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

        if not running:
            break

        # Check if the player's answer is correct or incorrect
        if current_question["options"][ord(player_answer) - ord('A')] == current_question["answer"]:
            feedback_text = font.render("Correct! You strike a blow to the teacher's ego!", 1, text_color)
            screen.blit(feedback_text, (50, 350))
            pygame.display.update()
            time.sleep(1)
            correct_sound.play()
            score += 1  # increment the score if the answer is correct
            if score == len(questions):
                running = False
        else:
            feedback_text = font.render("Incorrect. The teacher scoffs at your ignorance.", 1, text_color)
            screen.blit(feedback_text, (50, 350))
            pygame.display.update()
            time.sleep(1)
            incorrect_sound.play()
            lives -= 1  # decrement the lives
            if lives <= 0:
                running = False

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
                        playing = False
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.upper() == 'Y':
                            break
                        elif event.unicode.upper() == 'N':
                            playing = False
                            break
                else:
                    continue
                break

pygame.quit()