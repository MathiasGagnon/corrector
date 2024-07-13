import openai
from dotenv import load_dotenv
import os

class Corrector:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def correct(self, question, answer, correction):
        """
        Corrects the answer according to the correction.

        Args:
        - question: The question asked.
        - answer: Answer that was given.
        - correction: Correct answer

        Returns:
        - The grade and comments regarding the answer.
        """
        messages = [
            {
                "role": "system",
                "content": (
                    "You are an AI tutor. Your task is to grade the user's answer "
                    "based on the provided correction grid. Compare the user's answer "
                    "with the correct answer and provide a detailed grading with comments. "
                    "You will give points according to the possible points in the section. Give part of the points if they understand the concept of the query"
                    "Respond with a list of the sections and the grade. "
                    "It does not need to be exactly the same, but it needs to compile and do what the question asks. "
                    "Give comments by citing the correct answer, and be kind, as the students are human sciences students."
                    "Please respond in French."
                )
            },
            {
                "role": "user",
                "content": (
                    f"Question:\n{question}\n\n"
                    f"Correct answer:\n{correction}\n\n"
                    f"User's answer:\n{answer}"
                )
            }
        ]

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            n=1
        )

        return response.choices[0].message.content

# Example usage:
# corrector = Corrector()
# question = "Quelle est la capitale de la France ?"
# answer = "Berlin"
# correction = "La capitale de la France est Paris."
# print(corrector.correct(question, answer, correction))
