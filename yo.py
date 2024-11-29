from datetime import datetime
import json
import os

@app.post("/rca_feedback")
def save_feedback(
    llm_responses: list,
    is_positive: bool,
    text_feedback: str = None,
    user_id: str = None
):
    # Create feedback entry
    feedback_entry = {
        "user_id": user_id,
        "is_positive": is_positive,
        "timestamp": datetime.now().isoformat(),
        "llm_responses": llm_responses  # Now storing list of responses
    }
    
    # Add text feedback if provided
    if text_feedback:
        feedback_entry["text_feedback"] = text_feedback

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
