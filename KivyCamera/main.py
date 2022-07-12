from kivymd.app import MDApp
from kivy.lang import Builder

from kivy.core.window import Window

Window.size = (600, 570)

screen_helper = """
Screen:
    Camera:
        id: cam
        resolution: (800, 800)
    MDFloatingActionButton:
        id: shutter
        icon: "camera"
        md_bg_color: "#f7f2fa"
        pos_hint: {'center_x': 0.5, 'center_y': 0.1}
        on_release: app.capture()
"""

class CameraApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = 'LightBlue'
        self.screen = Builder.load_string(screen_helper)
        return self.screen

    def capture(self):
        print("Capturing...")
        cam = self.screen.ids['cam']
        cam.export_to_png('./capture.png')

CameraApp().run()