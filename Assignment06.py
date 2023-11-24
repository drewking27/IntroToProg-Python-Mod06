# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Your Name Here>,<Date>,<Activity>
# ------------------------------------------------------------------------------------------ #
import json

# -- Data -- #
    # Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
    # Define the Data Constants
    # FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

    # Define the Data Variables and constants
# student_first_name: str = ''  # Holds the first name of a student entered by the user.
# student_last_name: str = ''  # Holds the last name of a student entered by the user.
# course_name: str = ''  # Holds the name of a course entered by the user.
# student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
# csv_data: str = ''  # Holds combined string data separated by a comma.
# json_data: str = ''  # Holds combined string data in a json format.
# file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


class FileProcessor:
    """
        A collection of processing layer functions that work with Json files

        ChangeLog: (Who, When, What)
        Aking,11/22/2024,Created Class
        """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads the data from the existing json file

                    ChangeLog: (Who, When, What)
                    AKing,11/22/2023,Created function

                    :return: student data
                    """
        try:
            file = open(file_name, "r")

            # CSV Answer
            # for row in file.readlines():
            #     # Transform the data from the file
            #     student_data = row.split(',')
            #     student_data = {"FirstName": student_data[0],
            #                     "LastName": student_data[1],
            #                     "CourseName": student_data[2].strip()}
            #     # Load it into our collection (list of lists)
            #     students.append(student_data)

            # JSON Answer
            student_data = json.load(file)

            file.close()
        except Exception as e:
            print("Error: There was a problem with reading the file.")
            print("Please check that the file exists and that it is in a json format.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes the data to the  json file

                            ChangeLog: (Who, When, What)
                            AKing,11/22/2023,Created function

                            :return: none
                            """
        try:
            file = open(file_name, "w")
            # CSV answer
            # for student in students:
            #     csv_data = f'{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n'
            #     file.write(csv_data)

            # # JSON answer
            json.dump(student_data, file)

            file.close()
            print("The following data was saved to file!")
            for student in student_data:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            if file.closed == False:
                file.close()
            print("Error: There was a problem with writing to the file.")
            print("Please check that the file is not open by another program.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

class IO:
    """
        A collection of presentation layer functions that manage user input and output

        ChangeLog: (Who, When, What)
        Aking,11/22/2024,Created Class
        Aking,11/22/2024,Added menu output and input functions
        Aking,11/22/2024,Added a function to display the data
        Aking,11/22/2024,Added a function to display custom error messages
        """

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

            ChangeLog: (Who, When, What)
            AKing,11/22/2023,Created function

            :return: None
            """

        print(menu)

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

            :return: string with the users choice
            """

        global menu_choice
        menu_choice = input("Enter your menu choice number: ")
        print()  # Adding extra space to make it look nicer.
        return menu_choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

            ChangeLog: (Who, When, What)
            AKing,11/22/2023,Created function

            :return: str
            """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays the students that have been registered

            ChangeLog: (Who, When, What)
            AKing,11/22/2023,Created function


            :return: student data
            """

        print("-" * 50)
        for student in student_data:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        return student_data

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays custom error messages to the user

            ChangeLog: (Who, When, What)
            AKing,11/22/2024,Created function

            :return: None
            """

        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data = students)

# -- Presentation (Input/Output) -- #
    # Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)
    IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(student_data=students, file_name = FILE_NAME)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
