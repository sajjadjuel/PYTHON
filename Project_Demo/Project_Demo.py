import os
courses=[]

#HOME PAGE

def menu():
    os.system('cls')
    print('\n\t\t\tcourse management application'.upper())
    menu= '''\n\t [1] Add course \n\t [2] Update Course \n\t [3] Delete Course \n\t [4] Show Individual Courses 
         [5] Show All Courses \n\t [6] Search Courses \n\t [7] Store courses data \n\t [8] Exit'''
    print(menu.title())
    action_input=''
    while action_input=='':
        action_input = input('\n Which action you want to take? ')
        if action_input:
            if action_input.lower()=='quit':
                break
            elif action_input>='1' and action_input <='8':
                action=int(action_input)
                if action==1:
                    add_course()
                    input('\nPress Enter to go main menu')
                    menu_call()
                elif action==2:
                    update_course()
                    input('\nPress Enter to go main menu')
                    menu_call()
                elif action==3:
                    delete_course()
                    input('\nPress Enter to go main menu')
                    menu_call()
                elif action==4:
                    os.system('cls')
                    individual_code= input('\nEnter the course code you want to see the details : ').upper()
                    show_individual(individual_code)
                    input('\nPress Enter to go main menu')
                    menu_call()
                elif action==5:
                    show_courses()
                    input('\nPress Enter to go main menu')
                    menu_call()
                elif action==6:
                    search_courses()
                    input('\nPress Enter to go main menu')
                    menu_call()
                elif action==7:
                    store_data()
                    input('\nPress Enter to go main menu')
                    menu_call()
                elif action==8:
                    #sys.exit(0)
                    break
                else: 
                    #print('You have entered an invalid choice. Try again ..')
                    os.system('cls')
                    #input('You have entered an invalid choice. Try again ..')
                    menu_call()

            else:
                print('You have choosen an invalid opton. Try again.....')
                input()
                return menu_call()
        else:
            menu_call()
    

    

def menu_call():
    return menu()

#CHECK INTEGER
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))       
    except ValueError:
       print("\tNot an integer! Try again.")
       continue
    else:
       return userInput 
       break 
#PREREQUISITE ADD
def add_prerequisite_course(code):
    course_name = ''
    course_credit = ''
    course_prerequisites = ''
    print('\n\t\t\tAdd Prerequisite'.upper())
    while (course_name==''):
         course_name =          input('\nEnter Course Name          :').title()
    while (course_credit==''):
         course_credit =        inputNumber('Enter Course credit        :')
    while (course_prerequisites==''):
         course_prerequisites = input('Enter Course prerequisites :').upper()
         course_prerequisites_checked= check_prerequisite(course_prerequisites)

    course_dictionary={'Course Code':code, 
                       'Name': course_name, 
                       'Credit': course_credit, 
                       'prerequisite':course_prerequisites_checked}
    courses.append(course_dictionary)
    print(f'\n\nYour course "{course_name}[{code}]" added successfully')
    return code

#PREREQUISITE CHECK
def check_prerequisite(prerequisite):
    null="NULL"
    null2="N/A"
    checked_prerequisite=''
    if prerequisite!=null:
        for course in courses:
            if course.get('Course Code')==prerequisite:
                 checked_prerequisite=prerequisite
        if checked_prerequisite:
            return checked_prerequisite
        else:
                print ('You have enter an invalid prerequisite code.\nDo you want to add this course? :')
                prerequisite_action=input('\n\t 1. Yes \n\t 2. No \n\t Enter choice : ')
                if prerequisite_action=='1':
                    return add_prerequisite_course(prerequisite)
                    
                else:
                    return menu_call()
    else:
        return 'N/A'

            
#ADD COURSE
def add_course():
    os.system('cls')
    course_name = ''
    course_code = ''
    course_credit = ''
    course_prerequisites = ''
    print('\n\t\t\tAdd course'.upper())
    while (course_name==''):
         course_name =          input('\nEnter Course Name          :').title()
    while (course_code==''):
         course_code =          input('Enter Course Code          :').upper()
    while (course_credit==''):
         course_credit =        inputNumber('Enter Course credit        :')
    while (course_prerequisites==''):
         course_prerequisites = input('Enter Course prerequisites :').upper()
         course_prerequisites_checked= check_prerequisite(course_prerequisites)

    course_dictionary={'Course Code':course_code, 
                       'Name': course_name, 
                       'Credit': course_credit, 
                       'prerequisite':course_prerequisites_checked}
    courses.append(course_dictionary)
    print(f'\n\nYour course "{course_name}[{course_code}]" added successfully')
    
#UPDATE COURSE INFORMATION
def update_course():
    os.system('cls')
    print('\n\t\t\tUpdate Course'.upper())
    show_courses()
    updated_course={}
    
    update_code= input('\nEnter the course code you want to update : ').upper()
    for course in courses:
        if course.get('Course Code')==update_code:
            updated_course_name = ''
            updated_course_code = ''
            updated_course_credit = ''
            updated_course_prerequisites = ''
            update_menu='''\n\t 1. Name \n\t 2. Course Code \n\t 3. Credit information \n\t 4. prerequisites \n\t 5. None'''
            print(update_menu)
            update_action=int(input('\nWhich information you want to update? : '))
            
            
            if update_action==1:
                while (updated_course_name==''):
                    updated_course_name =          input('\nEnter Course Name       :').title()
                    updated_course_code = course['Course Code']
                    updated_course_credit = course['Credit']
                    updated_course_prerequisites = course['prerequisite']
                updated_course={'Course Code':updated_course_code, 
                                'Name': updated_course_name, 
                                'Credit': updated_course_credit, 
                                'prerequisite':updated_course_prerequisites}
                course.update(updated_course)

            elif update_action==2:
                while (updated_course_code==''):
                     updated_course_code =          input('Enter Course Code          :').upper()
                     updated_course_name = course['Name']
                     updated_course_credit = course['Credit']
                     updated_course_prerequisites = course['prerequisite']
                updated_course={'Course Code':updated_course_code, 
                                'Name': updated_course_name, 
                                'Credit': updated_course_credit, 
                                'prerequisite':updated_course_prerequisites}
                course.update(updated_course)

            elif update_action==3:
                while (updated_course_credit==''):
                    updated_course_credit =        input('Enter Course credit        :')
                    updated_course_name = course['Name']
                    updated_course_code = course['Course Code']
                    updated_course_prerequisites = course['prerequisite']
                updated_course={'Course Code':updated_course_code, 
                                'Name': updated_course_name, 
                                'Credit': updated_course_credit, 
                                'prerequisite':updated_course_prerequisites}
                course.update(updated_course)

            elif update_action==4:
                while (updated_course_prerequisites==''):
                    updated_course_prerequisites = input('Enter Course prerequisites :').upper()
                    course_prerequisites_check= check_prerequisite(updated_course_prerequisites)
                    updated_course_name = course['Name']
                    updated_course_code = course['Course Code']
                    updated_course_credit = course['Credit']
                updated_course={'Course Code':updated_course_code, 
                                'Name': updated_course_name, 
                                'Credit': updated_course_credit, 
                                'prerequisite':course_prerequisites_check}
                course.update(updated_course)

            elif update_action==5:
                menu_call()
                
    if updated_course:
        print(f'\n\nYour course "{update_code}" updated successfully')
        input('\nPress Enter to go main menu')
        menu_call()
    else:
        print('\n\tInvalid Course code!\n')
        input('\nPress Enter to go main menu')
        menu()

#DELETE COURSE 
def delete_course():
    os.system('cls')
    print('\n\t\t\tDelete Course'.upper())
    show_courses()
    delete_code= input('\nEnter the course code you want to delete : ').upper()
    deleted_courses=0
    for course in courses:
        if course.get('Course Code')==delete_code:
            courses.remove(course)
            deleted_courses = 1           
    if deleted_courses==1:
            print(f'\n\nYour course "{delete_code}" deleted successfully')
    else:
        print('\n\tInvalid Course code!\n')     
#Display Indivual
def show_individual(individual_code):
    os.system('cls')
    print('\n\t\t\tFind individual course\n'.upper())
    individual_courses=0
    for course in courses:
        if course.get('Course Code')==individual_code:
           
            individual_courses=course
    
    if individual_courses:
        print("\tCourse Code\t\tCourse Name\t\tCredit\t\tPrerequisite")
        print("\t___________\t\t___________\t\t______\t\t____________")
        print()
        print(f"\t{individual_courses['Course Code']}\t\t\t{individual_courses['Name']}\t\t\t {individual_courses['Credit']}\t\t{individual_courses['prerequisite']}")
    else:
         print(f'\n\nYour course "{individual_code}" not found or you have entered an invalid course code')
         

#DISPLAY ALL COURSES
def show_courses():
    if (courses):
        print("\tCourse Code\t\tCourse Name\t\tCredit\t\tPrerequisite")
        print("\t___________\t\t___________\t\t______\t\t____________")
        print()
        for course in courses:
            print(f"\t{course['Course Code']}\t\t\t{course['Name']}\t\t\t {course['Credit']}\t\t{course['prerequisite']}")
                
    else:
        print('\n\tThere is no courses added yet!\n')
        input('\nPress Enter to go main menu')
        menu()

#SEARCH A COURSES 
def search_courses():
    os.system('cls')
    print('\n\t\t\tSearch course\n'.upper())
    found_course=[]
    search_code= input('Enter the course code you want to search : ').upper()
    
    for course in courses:
        if course.get('Course Code')==search_code:
            print(f'\n\nYour course "{search_code}" found successfully\n')
            found_course=course
    
    if found_course:
        print("\tCourse Code\t\tCourse Name\t\tCredit\t\tPrerequisite")
        print("\t___________\t\t___________\t\t______\t\t____________")
        print()
        print(f"\t{found_course['Course Code']}\t\t\t{found_course['Name']}\t\t\t {found_course['Credit']}\t\t{found_course['prerequisite']}")
    else:
         print(f'\n\nYour course "{search_code}" not found. \nDo you want to add this course?')
         prerequisite_action=input('\n\t 1. Yes \n\t 2. No \n\t Enter choice : ')
         if prerequisite_action=='1':
            return add_prerequisite_course(search_code)         
         else:
            return menu_call()


#STORE FUNCTIONALITY
def store_data():
    os.system('cls')
    print('\n\t\t\tStore all data\n'.upper())
    show_courses()
    print('\nDo you want to store courses data?')
    store_action=int(input('\n\t 1. Yes \n\t 2. No \n\tEnter choice :'))
    if store_action==1:
        file_name=input('Enter your preffered file name : ')
        filename=f'{file_name}.txt'
        with open(filename,'w') as file:
            for course in courses:
                file.write(f'{course}\n')
            print(f"\nFile stored successfully as '{filename} in your local disk")

    else:
       return menu_call()
            
print('\n\n\n\n\n\t\t\tProject Title: Develop a course management application using Python. ')        
print('\n\t\t\t\t\t Name: Md Sajjadul Islam Juel ')        
print('\n\t\t\t\t\t    ID: 20-42576-1 ')        
print('\n\t\t\t\t\t       Section: B ')    
input()
menu()
