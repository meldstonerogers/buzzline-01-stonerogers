"""
basic_generator_stonerogers.py

Generate some streaming buzz messages. 
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import sys
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Define the path to the parent directory of the utils folder
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add the parent directory to the system path
sys.path.append(parent_dir)

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define some lists for generating buzz messages
ADJECTIVES: list = ["odd", "lame", "awesome", "silly", "funny"]
ACTIONS: list = ["found", "saw", "tried", "shared", "loved"]
TOPICS: list = ["a movie", "a meme", "an app", "a trick", "a story"]

#####################################
# Define a function to generate buzz messages
#####################################


def generate_messages():
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}."


#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:

    logger.info("START custom producer script...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    # Assign the return value to a variable called interval_secs
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        # Use the time module to pause execution for a specified number of seconds
        # The time.sleep() function takes a single argument: the number of seconds to pause
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END custom producer script.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()
