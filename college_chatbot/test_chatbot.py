import unittest
from main import get_bot_response
from data import college_data

class TestChatbot(unittest.TestCase):

    def test_admissions(self):
        user_input = "Tell me about admissions"
        expected_response = f"Admissions deadline is {college_data['admissions']['deadline']}. Requirements: {college_data['admissions']['requirements']}. The application fee is {college_data['admissions']['application_fee']}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_programs(self):
        user_input = "what programs do you have"
        expected_response = f"We offer the following programs: {', '.join(college_data['academics']['programs'])}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_contact(self):
        user_input = "how can I contact you"
        expected_response = f"You can contact us at {college_data['general']['contact']} or visit our website at {college_data['general']['website']}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_tuition(self):
        user_input = "what is the tuition"
        expected_response = f"In-state tuition is {college_data['tuition']['in_state']}. Out-of-state tuition is {college_data['tuition']['out_of_state']}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_financial_aid(self):
        user_input = "do you offer financial aid"
        expected_response = f"Financial aid is {college_data['tuition']['financial_aid']}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_housing(self):
        user_input = "tell me about housing"
        expected_response = f"On-campus housing is {college_data['campus_life']['housing']}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_clubs(self):
        user_input = "what clubs are there"
        expected_response = f"We have many clubs, including: {', '.join(college_data['campus_life']['clubs'])}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_sports(self):
        user_input = "do you have sports"
        expected_response = f"Our college has the following sports teams: {', '.join(college_data['campus_life']['sports'])}."
        self.assertEqual(get_bot_response(user_input), expected_response)

    def test_unknown_input(self):
        user_input = "what is the meaning of life"
        expected_response = "I'm sorry, I don't understand that. Please ask about admissions, programs, contact, tuition, financial aid, housing, clubs, or sports."
        self.assertEqual(get_bot_response(user_input), expected_response)

if __name__ == '__main__':
    unittest.main()
