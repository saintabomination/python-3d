import pyglet
import constants

window = pyglet.window.Window(
  constants.WINDOW_WIDTH,
  constants.WINDOW_HEIGHT,
  fullscreen=constants.WINDOW_FULLSCREEN,
  caption=constants.WINDOW_TITLE
)

@window.event
def on_draw():
  window.clear()

pyglet.app.run()
