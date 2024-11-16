from typing import Dict


def option_picker(prompt: str, options: Dict[str, str]):
    """Given a prompt and set of options, allow user to pick an option."""
    
    message = prompt + "\n\n"
    for letter, choice in options.items():
        message += f"({letter}) {choice}\n"
    return input(message).strip().lower()
