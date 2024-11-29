from typing import List
from pydantic import BaseModel
from datetime import datetime
import json
import os

# Define the model for feedback data
class FeedbackInput(BaseModel):
    llm_responses: List[str]
    is_positive: bool
    text_feedback: str = None
    user_id: str = None

@app.post("/rca_feedback")
def save_feedback(feedback: FeedbackInput):
    # Create feedback entry
    feedback_entry = {
        "user_id": feedback.user_id,
        "is_positive": feedback.is_positive,
        "timestamp": datetime.now().isoformat(),
        "llm_responses": feedback.llm_responses
    }

    # Add text feedback if provided
    if feedback.text_feedback:
        feedback_entry["text_feedback"] = feedback.text_feedback

    # Load existing feedback or create a new list
    filename = "feedback.json"
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
