"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   1) Encapsulation - data and behavior are kept close together
   2) Abstraction - hiding away complexity allows for ease of use.
    You don't need to understand how a method works internally to use it
   3) Polymorphism - can use the same method on different things in different
    ways

2. What is a class?
    A "type" of thing, like a blueprint that can specify certain attributes
    and methods and allows for variations that share the same features

3. What is an instance attribute?
    An attribute that is unique from instance to instance

4. What is a method?
    A function that is tied to a class

5. What is an instance in object orientation?
    A particular instance of a particular class

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
    All instances of a particular class will share the same class attribute
    while instance attributes differ between instances. If I created a
    Hackbright student class I would assign as a class attribute female for gender
    but assign name as an instance attribute.

"""
# Parts 2 through 5:
# Create your classes and class methods

#creating student class with instance attributes first and last name and address
class Student(object):
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

#creating Question class that has a ask_and_evaluate method which returns
#a boolean indicating whether the user's answer to a question was correct
class Question(object):
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        answer = raw_input(self.question)
        if answer == self.correct_answer:
            return True
        else:
            return False

class Exam(object):
    """
    This class has an instance attribute called questions initially
    set to an empty list. The add_Question method allows you to append a Question
    instance to the list. The administer method asks all the questions and returns
    a score
    """
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_Question(self, question, correct_answer):
        self.questions.append(Question(question, correct_answer))

    def administer(self):
        score = 0
        for q in self.questions:
            if q.ask_and_evaluate() == True:
                score += 1
        return score

#Part 4: Creat an actual exam

def take_test(exam, student):
    """exam.administer() returns a score which is assigned as a student's instance
    attribute"""
    student.score = exam.administer()

def example():
    """Creating and administering an astronomy test to student Stephanie

    Creates an exam instance called astronomy_test, adds questions to the test
    using the add_Question method, creates an instance of the class
    Student called stephanie, administers the test to stephanie and the score
    is stored as an instance attribute
    """
    astronomy_test = Exam('astronomy_test')
    astronomy_test.add_Question('How many moons does Mars have?', '2')
    astronomy_test.add_Question("Which planet is closest to the sun?", "Mercury")
    astronomy_test.add_Question("Biggest planet in our solar system?", "Jupiter")
    astronomy_test.add_Question("What galaxy are we in?", "Milky Way")

    stephanie = Student('Stephanie', 'Song', '1275 University Ave. Berkeley, CA')
    take_test(astronomy_test, stephanie)


example()

#Part 5 - Inheritance
#creating a Quiz class that inherits from Exam class. uses super on administer
#and returns a boolean if the score is better than half of the questions
#?-the point of using super here to differentiate btwn administer on Quiz and
#administer on Exam?
class Quiz(Exam):
    def administer(self):
        x = super(Quiz, self).administer()
        if x > len(self.questions) / 2:
            return True
        else:
            return False
