class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses and course in lecturer.courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def mid_grade(self, grades):
        self.grades = list[grades]
        count = 0
        for grade in self.grades:
            sum1 += grade
            count += 1
        if count == 0:
            return 'Оценок нет'
        else:
            sum1 = sum1/count
        return sum1

    def stud_eq(self, other):
        if student.mid_grade > other.sum_:
            print(f"{self.name} учится лучше, чем {other.sum_}")  
        else:
            print(f"{self.name} учится хуже, чем {other.sum_}")

    def __lt__(self, other):
        if mid_grade(self) >= mid_grade(other):
            return
        return mid_grade(self) < mid_grade(other)

    def __gt__(self, other):
        if mid_grade(self) <= mid_grade(other):
            return
        return mid_grade(self) > mid_grade(other)

    def __eq__(self, other):
        if mid_grade(self) != mid_grade(other):
            return
        return mid_grade(self) == mid_grade(other)

    def students_rate(students_list, course_name):
        some_list = []
        summ = 0
        count = 0
        for student_hw in students_list:
            for key, value in student_hw.grades_student.items():
                if key == course_name:
                    some_list.append(value)
        for i in some_list:
            for n in i:
                summ +=n
                count += 1
        avg_rating_all = summ / count


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {self.sum_}\nКурсы в процессе изучения: {self.courses_in_progress} Завершенные курсы: {self.finished_courses}"
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses = []
        self.grades = {}
    
    def mid_grade(self):
        count = 0
        for grade in self.grades:
            self.sum_ += grade
            count += 1
        if count == 0:
            pass
        else:
            self.sum_=self.sum_/count
        return self.sum_

    def __lt__(self, other):
        if mid_grade(self) >= mid_grade(other):
            return
        return mid_grade(self) < mid_grade(other)

    def __gt__(self, other):
        if mid_grade(self) <= mid_grade(other):
            return
        return mid_grade(self) > mid_grade(other)

    def __eq__(self, other):
        if mid_grade(self) != mid_grade(other):
            return
        return mid_grade(self) == mid_grade(other)

    def stud_eq(self, other):
        if self.sum_ > other.sum_:
            print(f"{self.name} имеет рейтинг выше, чем {other.sum_}")  
        else:
            print(f"{self.name} имеет рейтинг ниже, чем {other.sum_}")
        
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредний балл: {self.sum_}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

student1 = Student("Иван","Крутов","Мужской")
student2 = Student("Мария", "Шалимова","Женский")
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student2.courses_in_progress += ['Python']

any_reviewer = Reviewer("Роман", "Журавлев")
any_reviewer.courses_attached = ['Python']

any_reviewer.rate_hw(student1, 'Python', 10)
any_reviewer.rate_hw(student1, 'Python', 8)
any_reviewer.rate_hw(student1, 'Git', 6)
any_reviewer.rate_hw(student1, 'Git', 10)

any_reviewer.rate_hw(student2, 'Python', 9)
any_reviewer.rate_hw(student2, 'Python', 7)
any_reviewer.rate_hw(student2, 'Git', 10)
any_reviewer.rate_hw(student2, 'Git', 8)

print(student1.__eq__(student2))
