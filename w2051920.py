# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20231270
# Date: 27/11/2023

# Part 1 - Main version
from graphics import *  # import the graphics.py module

progress_count = 0
module_trailer_count = 0
module_retriever_count = 0
excluded_count = 0
total_inputs = 0
p = "PASS credits"
d = "DEFER credits"
f = "FAIL credits"
Total_credits = p + d + f  # total of pass,defer and fail credits is equal to 120
progress_data = []
module_trailer_data = []
module_retriever_data = []
exclude_data = []

print("Are you a staff member or a student ?")
while True:
    choice = input("Enter '1' for staff member or '2' for student: ")
    try:
        choice = int(choice)
    except ValueError:
        print('Integer required')
        continue

    if choice not in range(1, 3):
        print('Invalid input. Please enter again.')
        continue
    else:
        break

if choice == 1:  # if the user is a staff member
    while True:
        while True:
            p = input("Enter student's total PASS credits: ")
            try:
                p = int(p)
            except ValueError:
                print('Integer required')
                continue

            if p not in range(0, 121, 20):
                print(p, "is out of range. Please enter again.")
                continue
            else:
                break

        while True:
            d = input("Enter student's total DEFER credits: ")
            try:
                d = int(d)
            except ValueError:
                print('Integer required')
                continue

            if d not in range(0, 121, 20):
                print(d, "is out of range. Please enter again.")
                continue
            else:
                break

        while True:
            f = input("Enter student's total FAIL credits: ")
            try:
                f = int(f)
            except ValueError:
                print('Integer required')
                continue

            if f not in range(0, 121, 20):
                print(f, "is out of range. Please enter again.")
                continue
            else:
                break

        if (p + d + f) != 120:  # check whether the total of credits is 120
            print('Total incorrect')
            continue

        elif p == 120:
            progress_data.append([p, d, f])
            print("Progress")
            progress_count += 1
            total_inputs += 1

        elif p == 100:
            module_trailer_data.append([p, d, f])
            print("Progress(module trailer)")
            module_trailer_count += 1
            total_inputs += 1

        elif f in range(80, 121, 20):
            exclude_data.append([p, d, f])
            print("Exclude")
            excluded_count += 1
            total_inputs += 1

        else:
            print("Module retriever")
            module_retriever_data.append([p, d, f])
            module_retriever_count += 1
            total_inputs += 1

        print("Would you like to enter another set of data ?")  # if the user want to continue
        while True:
            next_step = input("Enter 'y' for Yes or 'q' to quit and view results: ")
            if next_step.lower() == 'y' or next_step.lower() == 'q':  # convert uppercase character to lowercase
                break
            else:
                print("Invalid input. Please enter 'y' for Yes or 'q' to quit.")

        if next_step.lower() == 'y':
            # Handle the case for 'y'
            print("You chose to continue.")
            continue
        else:
            # Handle the case for 'q'
            print("You chose to quit.")
            print("See the histogram for the results...")
            break

    # create the Histogram
    # OPEN THE WINDOW
    win = GraphWin("Histogram", 550, 600)  # open a window object called "win" with size and title
    win.setBackground("Mint Cream")  # Set the background colour of the window

    my_heading = Text(Point(185, 40), 'Histogram Results')  # Define some text.
    my_heading.draw(win)  # Render text to our window.
    my_heading.setTextColor("black")
    my_heading.setSize(22)
    my_heading.setStyle("bold")
    my_heading.setFace("helvetica")

    max_height = win.getHeight() - 100  # Adjust the maximum height of a bar based on window size
    # define the first bar
    height1 = min(int(progress_count * 10), max_height)  # Adjusting heights of the bars if they exceed the max_height
    rectangle1 = Rectangle(Point(40, win.getHeight() - 80), Point(140, win.getHeight() - 80 - height1))
    rectangle1.setFill("light blue")
    rectangle1.draw(win)  # Render the Rectangle to the window

    # define the second bar
    height2 = min(int(module_trailer_count * 10), max_height)
    rectangle2 = Rectangle(Point(150, win.getHeight() - 80), Point(250, win.getHeight() - 80 - height2))
    rectangle2.setFill("light green")
    rectangle2.draw(win)  # Render the Rectangle to the window

    # define the third bar
    height3 = min(int(module_retriever_count * 10), max_height)
    rectangle3 = Rectangle(Point(260, win.getHeight() - 80), Point(360, win.getHeight() - 80 - height3))
    rectangle3.setFill("pink")
    rectangle3.draw(win)  # Render the Rectangle to the window

    # define the fourth bar
    height4 = min((excluded_count * 10), max_height)
    rectangle4 = Rectangle(Point(370, win.getHeight() - 80), Point(470, win.getHeight() - 80 - height4))
    rectangle4.setFill("orange")
    rectangle4.draw(win)  # Render the Rectangle to the window

    text1 = Text(Point(90, win.getHeight() - (90 + height1)), str(progress_count))
    text1.setTextColor("grey")
    text1.setStyle("bold")
    text1.draw(win)

    text2 = Text(Point(200, win.getHeight() - (90 + height2)), str(module_trailer_count))
    text2.setTextColor("grey")
    text2.setStyle("bold")
    text2.draw(win)

    text3 = Text(Point(310, win.getHeight() - (90 + height3)), str(module_retriever_count))
    text3.setTextColor("grey")
    text3.setStyle("bold")
    text3.draw(win)

    text4 = Text(Point(420, win.getHeight() - (90 + height4)), str(excluded_count))
    text4.setTextColor("grey")
    text4.setStyle("bold")
    text4.draw(win)

    bar_name1 = Text(Point(90, win.getHeight() - 70), "Progress")
    bar_name1.setTextColor("grey")
    bar_name1.setSize(13)
    bar_name1.setStyle("bold")
    bar_name1.draw(win)

    bar_name2 = Text(Point(200, win.getHeight() - 70), "Trailer")
    bar_name2.setTextColor("grey")
    bar_name2.setSize(13)
    bar_name2.setStyle("bold")
    bar_name2.draw(win)

    bar_name3 = Text(Point(310, win.getHeight() - 70), "Retriever")
    bar_name3.setTextColor("grey")
    bar_name3.setSize(13)
    bar_name3.setStyle("bold")
    bar_name3.draw(win)

    bar_name4 = Text(Point(420, win.getHeight() - 70), "Excluded")
    bar_name4.setTextColor("grey")
    bar_name4.setSize(13)
    bar_name4.setStyle("bold")
    bar_name4.draw(win)

    my_footer = Text(Point(145, 560), str(total_inputs) + " outcomes in total.")
    my_footer.draw(win)
    my_footer.setTextColor("grey")
    my_footer.setSize(15)
    my_footer.setStyle("bold")
    my_footer.setFace("helvetica")

    a_Line = Line(Point(20, win.getHeight() - 80), Point(490, win.getHeight() - 80))  # the x-axis of the graph
    a_Line.draw(win)

    win.getMouse()  # Wait for mouse click to close the window
    win.close()

    # Part 2 - List(extension)
    print('\nList of input progression data:')  # Name of the list
    for data in progress_data:
        print(f"Progress - {data[0]}, {data[1]}, {data[2]}")
    for data in module_trailer_data:
        print(f"Progress(module trailer) - {data[0]}, {data[1]}, {data[2]}")
    for data in module_retriever_data:
        print(f"Module retriever - {data[0]}, {data[1]}, {data[2]}")
    for data in exclude_data:
        print(f"Exclude - {data[0]}, {data[1]}, {data[2]}")

    # Part 3 - Text file(extension)
    # Writing data to a text file
    print('\ndata from text file: ')
    file_name = "progression_data.txt"  # Name of the text file
    with open(file_name, "w") as file:
        for data in progress_data:
            file.write(f"Progress - {data[0]}, {data[1]}, {data[2]}\n")
        for data in module_trailer_data:
            file.write(f"Progress(module trailer) - {data[0]}, {data[1]}, {data[2]}\n")
        for data in module_retriever_data:
            file.write(f"Module retriever - {data[0]}, {data[1]}, {data[2]}\n")
        for data in exclude_data:
            file.write(f"Exclude - {data[0]}, {data[1]}, {data[2]}\n")
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
else:  # if the user is a student
    while True:
        while True:
            p = input("Enter your total PASS credits: ")
            try:
                p = int(p)
            except ValueError:
                print('Integer required')
                continue

            if p not in range(0, 121, 20):
                print(p, "is out of range. Please enter again.")
                continue
            else:
                break

        while True:
            d = input("Enter your total DEFER credits: ")
            try:
                d = int(d)
            except ValueError:
                print('Integer required')
                continue

            if d not in range(0, 121, 20):
                print(d, "is out of range. Please enter again.")
                continue
            else:
                break

        while True:
            f = input("Enter your total FAIL credits: ")
            try:
                f = int(f)
            except ValueError:
                print('Integer required')
                continue

            if f not in range(0, 121, 20):
                print(f, "is out of range. Please enter again.")
                continue
            else:
                break

        if (p + d + f) != 120:  # check whether the total of credits is 120
            print('Total incorrect')
            continue

        elif p == 120:
            print("Progress")

        elif p == 100:
            print("Progress(module trailer)")

        elif f in range(80, 121, 20):
            print("Exclude")

        else:
            print("Module retriever")
        break
# End of the program.
