import pyglet
import constants
from classes.window import Window

window = Window(
  constants.WINDOW_WIDTH,
  constants.WINDOW_HEIGHT,
  fullscreen=constants.WINDOW_FULLSCREEN,
  caption=constants.WINDOW_TITLE
)
pyglet.app.run()
