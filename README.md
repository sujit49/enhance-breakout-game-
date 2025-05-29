# Enhanced Breakout Game

This is a classic Breakout-style game implemented in Python using the `turtle` module. The player controls a paddle to bounce a ball and break bricks. The game features increasing difficulty with levels, scoring, lives, and power-ups.

## Features

- **Classic Breakout Gameplay:** Control a paddle to hit a ball and destroy bricks.
- **Scoring System:** Earn points for each brick broken.
- **Lives System:** Start with a set number of lives. Losing the ball costs a life.
- **Levels:** As you clear all bricks, the game progresses to the next level.
    - The number of brick rows increases with each level.
    - The ball speed increases with each level.
- **Power-ups:**
    - Randomly drop when a brick is broken.
    - Collecting a power-up grants an extra life.
- **Dynamic Brick Layout:** Bricks are recreated for each new level.
- **Clear UI:** Displays score, lives, and current level.

## How to Play

### Prerequisites

- Python 3.x installed on your system.
- The `turtle` module (which is part of the Python standard library, so no separate installation is usually needed).

### Running the Game

1.  Save the Python code as a `.py` file (e.g., `breakout_game.py`).
2.  Open a terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the game using the command:
    ```bash
    python breakout_game.py
    ```
    (Replace `breakout_game.py` with the actual name of your file if different).

## Controls

-   **Left Arrow Key:** Move the paddle to the left.
-   **Right Arrow Key:** Move the paddle to the right.

## Game Mechanics

-   **Paddle:** Use the arrow keys to move the paddle horizontally at the bottom of the screen.
-   **Ball:** The ball will bounce off the walls and the paddle.
-   **Bricks:** When the ball hits a brick, the brick disappears, and you score points.
-   **Losing a Life:** If the ball goes past your paddle and hits the bottom of the screen, you lose a life. The ball will reset.
-   **Game Over:** The game ends when you run out of lives.
-   **Winning a Level:** Clear all the bricks on the screen to advance to the next level. The ball will reset, new bricks will appear, and the ball's speed will increase.
-   **Power-ups:** Occasionally, a destroyed brick will drop a power-up (represented by a gold circle). If the paddle catches it, you gain an extra life.

## Code Overview (`main.py`)

The game is structured as follows:

-   **Screen Setup:** Initializes the game window, title, background color, and dimensions.
-   **Game Variables:** Tracks score, lives, level, brick rows, and ball speed increment.
-   **Paddle Setup:** Creates the player-controlled paddle.
-   **Ball Setup:** Creates the ball with its initial speed and direction.
-   **Brick Setup (`create_bricks` function):** Dynamically creates and arranges the bricks for each level.
-   **Score Display:** Manages the on-screen display of score, lives, and level.
-   **Paddle Movement Functions (`paddle_left`, `paddle_right`):** Handle paddle controls.
-   **Keyboard Bindings:** Links arrow keys to paddle movement.
-   **Power-up Setup (`create_power_up` function):** Creates power-up objects.
-   **Reset Ball Function (`reset_ball`):** Resets the ball's position and direction after losing a life or starting a new level.
-   **Update Score Function (`update_score`):** Refreshes the score display.
-   **Main Game Loop:**
    -   Updates the screen.
    -   Moves the ball.
    -   Handles ball collisions with walls, paddle, and bricks.
    -   Manages power-up movement and collection.
    -   Checks for game over conditions.
    -   Checks if all bricks are cleared to advance to the next level.

## Future Enhancements (Suggestions)

-   Different types of power-ups (e.g., multi-ball, larger paddle, slower ball).
-   Different types of bricks (e.g., bricks that require multiple hits).
-   Sound effects for collisions and events.
-   High score saving/loading.
-   Pause functionality.

