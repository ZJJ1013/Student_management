class Student(object):
    student_num = 0

    def add_student(self, student_info):
        with open('student.txt', 'a') as file:
            file.write(student_info + '\n')

    def get_student_info(self, student_num):
        with open('student.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if student_num == line[0:5]:
                    result = line
                    break
            else:
                result = 'DNE'
            return result

    def get_all_student_info(self):
        with open('student.txt', 'r') as file:
            result = file.read()
        return result

    def delete_student(self, student_num):
        if not self.is_student_exist(student_num):
            return 'DNE'
        with open('student.txt', 'r') as file:
            lines = file.readlines()
        with open('student.txt', 'w') as file:
            for line in lines:
                if line[0:5] == student_num:
                    continue
                    fle.write(line)
        return 'Successfully deleted'

    def edit_student(self, student_num):
        if not self.is_student_exist(student_num):
            return 'DNE'
        with open('student.txt', 'r') as file:
            lines = file.readlines()
        with open('student.txt', 'w') as file:
            for line in lines:
                if line[0:5] == student_num:
                    name = input('Enter Student Name:')
                    gender = input('Enter Student Gender:')
                    phone = input('Enter Student Phone Number:')
                    student_info = ','.join([student_num, name, gender, phone])
                    file.write(student_info + '\n')
            else:
                file.write(line)

    def is_student_exist(self, student_num):
        with open('student.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                if student_num == line[0:5]:
                    return True
            else:
                return False

    def create_student_num(self):
        if self.student_num == 0:
            try:
                with open('student.txt', 'r') as file:
                    lines = file.readlines()
                    last_line = lines[-1]
                    if last_line:
                        self.student_num = int(last_line.split(',')[0]) + 1
                    else:
                        self.student_num = 10001
            except:
                student_num = 10001
        else:
            self.student_num += 1
        return str(self.student_num)

        return str(student_num)


def show_message():
    print('1: Add Student')
    print('2: Look for Student')
    print('3: Show All Student')
    print('4: Delete Student')
    print('5: Edit Student')
    print('0: Exit System')


def main():
    student = Student()
    show_message()
    while True:
        try:
            number = int(input('Enter ur Choice:'))
        except:
            print('Invalid Input!')
        else:
            if number == 1:
                student_num = student.create_student_num()
                name = input('Enter Student Name:')
                gender = input('Enter Student Gender:')
                phone = input('Enter Student Phone Number:')
                student_info = ''
                student.add_student(student_info)
                student_info = ','.join([student_num, name, gender, phone])
                result = student.add_student(student_info)
                print(result)
                print('Added')
            elif number == 2:
                student_num = input('Enter student number:')
                result = student.get_student_info(student_num)
                print(result)
            elif number == 3:
                result = student.get_all_student_info()
                print(result)
            elif number == 4:
                student_num = input('Enter student number:')
                confim = input('Are u sure?:')
                if confim == 'yes' or confim == 'y':
                    result = student.delete_student(student_num)
                    print(result)
                else:
                    print('Cancelled')
            elif number == 5:
                student_num = input('Enter student number:')
                result = student.edit_student(student_num)
                print(result)
            elif number == 0:
                print('Exited')
                break
            else:
                print('Invalid input!')


if __name__ == "__main__":
    main()
