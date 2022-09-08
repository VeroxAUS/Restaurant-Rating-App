# About The Program

Restaurant Rating is a program designed to provide a simple GUI for users to rate restaurants. The program is written in Python 3.10.7 and uses the Tkinter library for the GUI. The program is designed to be cross-platform and should work on Windows, Mac, and Linux.

## Installation

1. Make sure we extracted the program into a clean working directory
2. Open a terminal and navigate to the working directory
3. Run the following command: `python3 rating.py`

## Usage

Once ran the program provides a GUI where the user can provide the name of a restaurant, along with three separate ratings for three categories:
food, wine, atmosphere. The user can then submit the ratings and the program will calculate the average rating for the restaurant using a local file called ratings.txt that the program automatically updates. The user can then submit another restaurant and rating, or they can quit the program.

## Roadmap

- I'm not entirely sold on the for loops I used to place all the elements in the GUI, it helps with modularity and readability I hope, but having the pylint disable statements is a bit of a bummer. I'm not sure if there's a better way to do this, but I'm open to suggestions.
- I'd like to add onscreen keyboard functionality for the user to be able to enter the restaurant name and ratings without having to use a physical keyboard, so that the program can be used on a tablet or other touchscreen devices.
- I'd like to add a feature that allows the user to view the average rating for any given category in any given restaurant.
- The resizing of the GUI is a bit wonky, ideally the text and entry boxes would resize properly when the window is resized, but I was unable to get that working properly.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[Distributed under the GNU GPLv3 License.](https://choosealicense.com/licenses/gpl-3.0)
