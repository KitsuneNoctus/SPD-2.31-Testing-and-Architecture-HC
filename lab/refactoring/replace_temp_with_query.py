# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.
class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students

    def get_passing_students(self):
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.gpa > min_gpa:
                passed_students.append(s)
        return passed_students

    def print_graduation(self,passed_students):
        print('*** Student who graduated *** ')
        for s in passed_students:
            print(s.name)
        print('****************************')

    def send_emails(self,passed_students):
        for s in passed_students:
            s.send_congrat_email()

    def contact_top_employers(self,passed_students):
        passed_students.sort(key=lambda s: s.gpa)
        index = int(0.9 * len(passed_students))
        top_10_percent = passed_students[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

    def process_graduation(self):
        # Find the students in the school who have successfully graduated.
        passed_students = self.get_passing_students()

        # print student's name who graduated.
        self.print_graduation(passed_students)

        # Send congrat emails to them.
        self.send_emails(passed_students)

        # Find the top 10% of them and send their contact to the top employers
        self.contact_top_employers(passed_students)


students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'), 
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()