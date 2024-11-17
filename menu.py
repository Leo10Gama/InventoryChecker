from enum import Enum
from typing import Dict


class ColourText(Enum):
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    END = '\033[0m'
    BOLD = '\033[1m'


def print_colour(colour: ColourText, message: str):
    """Print a statement with a given colour."""
    print(f"{colour.value}{message}{ColourText.END.value}")


def option_picker(prompt: str, options: Dict[str, str]):
    """Given a prompt and set of options, allow user to pick an option."""
    
    message = prompt + "\n\n"
    for letter, choice in options.items():
        message += f"({letter}) {choice}\n"
    return input(message).strip().lower()
