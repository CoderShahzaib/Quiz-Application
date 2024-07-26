import tkinter as tk
from tkinter import ttk, messagebox

# Sample questions
questions = [
    {"question": "What is the capital of France?", "type": "mcq", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "2 + 2 = ?", "type": "mcq", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"question": "Fill in the blank: The chemical symbol for water is __.", "type": "fill", "answer": "H2O"}
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x600")

        # Initialize quiz variables
        self.question_index = 0
        self.score = 0

        # Create a notebook (tabbed interface) for questions
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Create frames for different parts of the quiz
        self.frames = []

        for i, question in enumerate(questions):
            question_frame = ttk.Frame(self.notebook)
            self.notebook.add(question_frame, text=f"Question {i+1}")
            self.frames.append(question_frame)

            self.display_question(question_frame, question)

    def display_question(self, frame, question):
        """Display a question in a given frame."""
        question_label = ttk.Label(frame, text=question["question"], font=("Arial", 18), wraplength=600)
        question_label.pack(pady=20)

        self.answer_var = tk.StringVar()

        if question["type"] == "mcq":
            for option in question["options"]:
                radio_button = ttk.Radiobutton(frame, text=option, variable=self.answer_var, value=option)
                radio_button.pack(anchor='w', padx=20, pady=5)
        elif question["type"] == "fill":
            fill_entry = ttk.Entry(frame, textvariable=self.answer_var, font=("Arial", 14))
            fill_entry.pack(pady=10)

        submit_button = ttk.Button(frame, text="Submit Answer", command=lambda: self.check_answer(frame, question))
        submit_button.pack(pady=20)

    def check_answer(self, frame, question):
        """Check the user's answer and provide feedback."""
        user_answer = self.answer_var.get().strip()

        if user_answer.lower() == question["answer"].lower():  # Case insensitive comparison
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct.")
        else:
            messagebox.showinfo("Incorrect!", f"The correct answer is: {question['answer']}")

        # Move to the next question
        self.question_index += 1

        if self.question_index < len(questions):
            # Select the next tab
            self.notebook.select(self.frames[self.question_index])

        else:
            # Show final results after all questions
            self.show_results()

    def show_results(self):
        """Display the final score and message."""
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(questions)}")

        # Reset quiz variables for potential restart
        self.question_index = 0
        self.score = 0

# Main program to start the quiz game
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
