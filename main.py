from Board import window
from kivy.config import Config
#from kivy.core.window import Window
import Data_Conversion.tela

def setup():
    #Set the Height and Width of the Board, tela grande 820, 800: tela média 656, 640 e piquena 410, 400.
    
    width_of_board = 656
    height_of_board = 640

    # Set the Hight and Width of the App
    Config.set('graphics', 'width', str(width_of_board))
    Config.set('graphics', 'height', str(height_of_board))

    #Tornar o aplicativo não redimensionável
    Config.set('graphics', 'resizable', '0')
    Config.write()

    #Faça a barra superior do Windows desaparecer
#    Window.borderless = True

    #Disable the Multi-Touch
    Config.set('input', 'mouse', 'mouse,disable_multitouch')

    #Runs the
    window().run()


if __name__ == "__main__":
    setup()
