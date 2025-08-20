from data import college_data

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "admission" in user_input:
        return f"Admissions deadline is {college_data['admissions']['deadline']}. Requirements: {college_data['admissions']['requirements']}. The application fee is {college_data['admissions']['application_fee']}."
    elif "program" in user_input:
        return f"We offer the following programs: {', '.join(college_data['academics']['programs'])}."
    elif "contact" in user_input:
        return f"You can contact us at {college_data['general']['contact']} or visit our website at {college_data['general']['website']}."
    elif "tuition" in user_input or "fee" in user_input:
        return f"In-state tuition is {college_data['tuition']['in_state']}. Out-of-state tuition is {college_data['tuition']['out_of_state']}."
    elif "financial aid" in user_input:
        return f"Financial aid is {college_data['tuition']['financial_aid']}."
    elif "housing" in user_input or "dorms" in user_input:
        return f"On-campus housing is {college_data['campus_life']['housing']}."
    elif "clubs" in user_input:
        return f"We have many clubs, including: {', '.join(college_data['campus_life']['clubs'])}."
    elif "sports" in user_input:
        return f"Our college has the following sports teams: {', '.join(college_data['campus_life']['sports'])}."
    else:
        return "I'm sorry, I don't understand that. Please ask about admissions, programs, contact, tuition, financial aid, housing, clubs, or sports."

if __name__ == "__main__":
    print("Welcome to the College Chatbot!")
    print("You can ask about admissions, programs, contact, tuition, financial aid, housing, clubs, or sports.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        response = get_bot_response(user_input)
        print(response)
