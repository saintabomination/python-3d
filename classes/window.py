import pyglet.window

class Window(pyglet.window.Window):
  def __init__(self, *arguments, **keywords):
    super(Window, self).__init__(*arguments, **keywords)

  def on_draw(self):
    self.clear()
