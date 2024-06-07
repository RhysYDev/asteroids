# asteroids

##Tutorial information


Line 1 imports the Pygame module to get access to all its amazing features.

Line 3 creates the AsteroidAnnihilator class.

Line 4 is the constructor of the AsteroidAnnihilator class. The actual Pygame initialization happens in _init_pygame().

Line 6 creates a display surface. Images in Pygame are represented by surfaces.

useful info:

Surfaces can be drawn on one another, allowing you to create complex scenes from simple pictures.

There’s one special surface in each Pygame project. That surface represents the screen and is the one that will eventually be displayed to players. All other surfaces have to be drawn on this one at some point. Otherwise, they won’t be shown.

To create the display surface, your program uses pygame.display.set_mode(). The only argument you pass to this method is the size of the screen, represented by a tuple of two values: width and height. In this case, Pygame will create a screen with a width of 800 pixels and a height of 600 pixels.

Line 8 is the game loop. It contains the same three steps for each frame:

Line 10 contains input handling.

Line 11 contains game logic.

Line 12 contains drawing.

Line 14 defines a method called _init_pygame(). This is where a one-time initialization of Pygame happens. The method does two things:

Line 15 calls pygame.init(). This single line of code is responsible for setting up the features of Pygame.

Line 16 sets the caption of your Pygame program using pygame.display.set_caption(). In this case, the caption will be the name of your game: Asteroid Annihilator.

Lines 18 and 21 define _handle_input() and _process_game_logic().

Line 24 defines _draw(). this is called every frame to draw the content of the screen, and it does that in two steps:

Line 25 fills the screen with a color using screen.fill(). The method takes a tuple with three values, representing three base colors: red, green, and blue. Each color value ranges between 0 and 255, representing its intensity. In this example, a tuple of (0, 0, 255) means that the color will consist only of blue, with no traces of red or green.

Line 26 updates the content of the screen using pygame.display.flip(). This will be called every frame to update the display. Because of this, you need to fill your screen with color every frame, as the method will clear the contents generated during the previous frame.
