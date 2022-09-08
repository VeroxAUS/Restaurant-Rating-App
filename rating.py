# First we have to import the modules we need
# It's not the cleanest import statement, but it works
# but it's the easiest way to import all the modules we need without having to use a wildcard import

from tkinter import END, W, Button, Entry, Label, Tk, messagebox, simpledialog

# Decided to use a class here, although not strictly necessary,
# it makes the code a bit easier to read and it was something I've been playing around with recently
# The class contains two methods, the reset method and the submit method

class RatingForm:
    ''' This is just a class that contains the code for the GUI,
    as well as some methods that are called when the user interacts with the GUI,
    the methods are:
    reset - Resets the form so that the user can enter new ratings
    submit - Submit all the ratings to the ratings.txt file granted they are all valid'''

    def __init__(self, master):
        ''' This is the constructor for the class, 
        it creates the GUI and sets the focus to the restaurant name entry box'''
        
        self.master = master
        master.title("Restaurant Rating Form")

        # We have to ensure the GUI can be resized by the user,
        # making sure that all elements are resized correctly when the window is resized,
        # including text size.

        # First we make sure that the window is set to a minimum size
        # This is so that the user can't resize the window to a size where the elements are too small to read
        # We also set the window to a maximum size,
        # so that the user can't resize the window to a size where the elements are too large to fit on the screen

        self.window_width = 500
        self.window_height = 300
        # Set the minimum window size
        master.minsize(self.window_width, self.window_height)
        # Set the maximum window size to 2x the minimum window size
        master.maxsize(self.window_width * 2, self.window_height * 2)

        # Make sure that the text in the GUI is resized correctly when the window is resized
        master.option_add("*Font", "TkDefaultFont 12")
        master.option_add("*Label.Font", "TkMenuFont 14")
        master.option_add("*Button.Font", "TkSmallCaptionFont 10")
        master.option_add("*Entry.Font", "TkTextFont 12")

        # Make sure that the entry boxes are resized correctly when the window is resized
        master.option_add("*Entry.width", 25)
        master.option_add("*Entry.height", 10)

        # Set the size of the buttons
        master.option_add("*Button.width", 10)
        master.option_add("*Button.height", 5)

        # Create all the labels, entry boxes and buttons using a for loop
        # This makes the code a bit easier to read and reduces the amount of code we have to write

        # This causes the code to be upset because it thinks we are using the member variables before they are defined,
        # but we are not, we are just defining them at runtime using these loops,
        # so we just need to tell the code to ignore this error

        # This might be a bad idea, but I wanted modularity in the code,
        # and I wasn't sure how to do it any other way

        # pylint: disable=maybe-no-member

        # For every label, we need to create a member variable for it
        for item in ["Restaurant Name", "Food", "Wine", "Atmosphere"]:
            # Create the member variable for the label
            setattr(self, item.lower().replace(" ", "_") + "_label", Label(master, text=item))

        # For every entry box, we need to create a member variable for it
        for item in ["Restaurant Name", "Food", "Wine", "Atmosphere"]:
            setattr(self, item.lower().replace(" ", "_") + "_entry", Entry(master))

        # For every button, we need to create a member variable for it

        for item in ["Submit", "Reset", "Lookup"]:
            # If the item is "Lookup", we need to make sure we don't use self.lookup, and just regular lookup
            if item == "Lookup":
                setattr(self, item.lower() + "_button", Button(master, text=item, command=lookup))
            else:
                setattr(self, item.lower() + "_button", Button(master, text=item, command=getattr(self, item.lower())))

        # Create the feedback label and set the text to an empty string
        self.feedback_label = Label(master, text="")
        self.feedback_label.config(fg="red")

        # Place the elements in the grid and get the row and column numbers
        row, column = self.place_elements()

        # Place the feedback label in the grid
        self.feedback_label.grid(row=row, column=column, columnspan=3)

        # Set the focus to the restaurant name entry box
        self.restaurant_name_entry.focus()

        # Then we make sure that the window can be resized in both the x and y directions using for loops
        # I'm very happy about this solution, as it means that if I add more rows or columns to the grid in the future,
        # the code will still work, hopefully

        # Get the number of rows in the grid
        rows = master.grid_size()[1]
        # Get the number of columns in the grid
        columns = master.grid_size()[0]

        # Loop through the rows and columns in the grid
        for row in range(rows):
            # Make sure that the row can be resized
            master.rowconfigure(row, weight=1)
        for column in range(columns):
            # Make sure that the column can be resized
            master.columnconfigure(column, weight=1)

    def place_elements(self):
        ''' Places the elements in the grid using for loops so that the code is hopefully modular'''

        # disabling the error that says we are using the member variables before they are defined
        # pylint: disable=maybe-no-member

        # Create the column and row numbers so that we can keep track of where we are in the grid
        column = 0
        row = 0

        # Create a list of the labels, entry boxes and buttons
        label = [self.restaurant_name_label, self.food_label, self.wine_label, self.atmosphere_label]
        entry = [self.restaurant_name_entry, self.food_entry, self.wine_entry, self.atmosphere_entry]
        button = [self.submit_button, self.reset_button, self.lookup_button]

        # Iterate through the list of labels, entry boxes and buttons and add them to the GUI
        # First we add the labels to the GUI
        for item in label:
            item.grid(row=row, column=column, sticky=W)
            row += 1
        row = 0
        column = 1
        # Add the entry boxes to the GUI
        for item in entry:
            item.grid(row=row, column=column)
            row += 1
        row = 0
        column = 2
        # Add the buttons to the GUI
        for item in button:
            item.grid(row=row, column=column)
            row += 1
        row = 4
        column = 0

        return row, column

    def reset(self):
        ''' Resets the form so that the user can enter new ratings'''

        # disabling the error that says we are using the member variables before they are defined
        # pylint: disable=maybe-no-member

        # Clear the text in the entry boxes
        self.restaurant_name_entry.delete(0, END)
        self.food_entry.delete(0, END)
        self.wine_entry.delete(0, END)
        self.atmosphere_entry.delete(0, END)
        self.feedback_label.config(text="")
        # Set the focus to the restaurant name entry box
        self.restaurant_name_entry.focus()

    def submit(self):
        ''' Submit all the ratings to the ratings.txt file granted they are all valid'''

        # disabling the error that says we are using the member variables before they are defined
        # pylint: disable=maybe-no-member

        # Get the restaurant name
        restaurant_name = self.restaurant_name_entry.get()
        # Get the food rating
        food_rating = self.food_entry.get()
        # Get the wine rating
        wine_rating = self.wine_entry.get()
        # Get the atmosphere rating
        atmosphere_rating = self.atmosphere_entry.get()

        # Check that the ratings are valid
        if not is_valid_rating(food_rating) or not is_valid_rating(wine_rating) or not is_valid_rating(atmosphere_rating):
            # If the ratings are not valid, display an error message
            self.feedback_label.config(text="Please enter a valid rating (1-5 or NA)")
            return

        # Open the ratings.txt file
        with open("ratings.txt", "a") as ratings_file:
            # Write the restaurant name, food rating, wine rating
            # and atmosphere rating to the file on new lines
            ratings_file.write(restaurant_name + ",food:" + food_rating + "\n")
            ratings_file.write(restaurant_name + ",wine:" + wine_rating + "\n")
            ratings_file.write(restaurant_name + ",atmosphere:" + atmosphere_rating + "\n")

        # Get the average rating for the restaurant
        average_rating = get_average_rating(restaurant_name)

        # Display a thank you message to the user,
        # and display the average rating for the restaurant reviewed
        # we have to make sure that the message box is on top of the main window
        messagebox.showinfo("Thank you", "Thank you for rating {0}. The average rating for {0} is {1}".format(restaurant_name, average_rating), parent=root)

        # Reset the form
        self.reset()

# It's not necessary to make these following functions methods of the RatingForm class
# so I've just made them normal functions, I could be wrong on that though
# I'm not sure if it's better to have them as methods or not

def lookup():
    ''' Lookup the average rating for a restaurant'''

    # Pop up a dialog box asking the user to enter the name of the restaurant they want to lookup
    # Make sure that the dialog box is on top of the main window no matter where the main window is
    restaurant_name = simpledialog.askstring("Lookup", "Enter the name of the restaurant you want to lookup", parent=root)

    # Check to see if it's a valid restaurant name
    if not is_valid_restaurant_name(restaurant_name):
        # If it's not a valid restaurant name, display an error message
        messagebox.showerror("Error", "Please enter a valid restaurant name", parent=root)
        return
    # Get the average rating for the restaurant
    average_rating = get_average_rating(restaurant_name)

    # Display the average rating for the restaurant and make sure that the dialog box is on top of the main window
    messagebox.showinfo("Average Rating", "The average rating for {0} is {1}".format(restaurant_name, average_rating), parent=root)

def is_valid_restaurant_name(restaurant_name):
    ''' Check to see if the restaurant name is valid'''

    # Check to see if the restaurant name is empty
    if restaurant_name == "":
        return False
    # Check to see if the restaurant name is in the ratings.txt file
    with open("ratings.txt", "r") as ratings_file:
        for line in ratings_file:
            # If the restaurant name is in the ratings.txt file, return True
            if line.startswith(restaurant_name):
                return True
    return False

def is_valid_rating(rating):
    ''' Checks that the rating is a number between 1 and 5 or NA '''

    # Check to see if the rating is NA
    if rating == "NA":
        return True
    try:
        # Check to see if the rating is a number between 1 and 5
        # First we convert the rating to an integer
        rating = int(rating)
        # Then we check to see if it's between 1 and 5
        return 1 <= rating <= 5
    except ValueError:
        return False

def get_average_rating(restaurant_name):
    ''' Gets the average rating for the restaurant by reading the ratings from ratings.txt '''

    # Open the ratings.txt file
    with open("ratings.txt", "r") as ratings_file:
        # Read all the lines in the file
        lines = ratings_file.readlines()
        # Create a list to store the ratings
        ratings = []
        # Loop through the lines
        for line in lines:
            # Split the line into the restaurant name and the rating
            restaurant, rating = line.split(",")
            # Check if the restaurant name matches the restaurant name we are looking for
            if restaurant == restaurant_name:
                # Split the rating into the category and the rating
                _, rating = rating.split(":")
                # Check that the rating is a valid rating
                if is_valid_rating(rating):
                    # Add the rating to the list of ratings
                    ratings.append(int(rating))
    # Make sure we're not dividing by 0
    if len(ratings) == 0:
        return 0
    # Calculate the average rating
    average_rating = sum(ratings) / len(ratings)
    # Return the average rating
    return round(average_rating, 1)

# Create the root window
root = Tk()
# Create the RatingForm object
my_gui = RatingForm(root)
# Run the mainloop
root.mainloop()
