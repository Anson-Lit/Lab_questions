

class Student:
    """
    param name_: Name of student
    param type: str
    param student_number_:
    param type: str
    param grades: Grades of student
    param type: list
    param courses: The courses the students are taking
    param type: list
    """
    def __init__(self, name_, student_number_, grades, courses):
        self.name = name_
        self.student_number = student_number_
        self._grades = grades
        self._courses = courses

    #Gets the value of name
    @property
    def name(self):
        return self._name
    #Sets the value of name
    @name.setter
    def name(self, value):
            self._name = value

    #Gets the value of student number
    @property
    def student_number(self):
        return self._student_number
    #Sets the value of name
    @student_number.setter
    def student_number(self, value):
            self._student_number = value


class Course():
    """
    param name: Name of the course
    param type: Str
    param name: Name of the instructor
    param type: Str
    """
    def __init__(self, name, instructor):
        """
        initialization of attributes
        """
        self.name = name
        self.instructor = instructor
        
    def run():
        pass

    #Gets the value of name
    @property
    def name(self):
        return self._name
    #Sets the value of name
    @name.setter
    def name(self, value):
        self._name = value
    
    #Gets the value of instructor
    @property
    def instructor(self):
        return self._instructor
    #Sets the value of instructor
    @instructor.setter
    def instructor(self, value):
        self._instructor = value


if __name__ == "__main__":
    student = Student("A","B",[],[])
    my_courses = Course("A","bob")
    print(my_courses.instructor)