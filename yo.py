import json
from datetime import datetime
import os


def save_feedback(user_id: str, is_positive: bool, text_feedback: str = None, filename: str = "feedback.json"):
    """
    Save user feedback to a JSON file.

    Args:
        user_id (str): Identifier for the user
        is_positive (bool): True for thumbs up, False for thumbs down
        text_feedback (str, optional): User's text feedback for negative responses
        filename (str): Name of the JSON file to store feedback
    """
    # Create feedback entry
    feedback_entry = {
        "user_id": user_id,
        "is_positive": is_positive,
        "timestamp": datetime.now().isoformat()
    }

    # Add text feedback if provided
    if text_feedback:
        feedback_entry["text_feedback"] = text_feedback

    # Load existing feedback or create new list
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            try:
                feedback_data = json.load(f)
            except json.JSONDecodeError:
                feedback_data = []
    else:
        feedback_data = []

    # Add new feedback
    feedback_data.append(feedback_entry)

    # Save updated feedback
    with open(filename, 'w') as f:
        json.dump(feedback_data, f, indent=2)

    return feedback_entry


# Example usage:
if __name__ == "__main__":
    # Example thumbs up without text
    save_feedback(
        user_id="user123",
        is_positive=True
    )

    # Example thumbs down with feedback
    save_feedback(
        user_id="user456",
        is_positive=False,
        text_feedback="The response was not clear enough"
    )




