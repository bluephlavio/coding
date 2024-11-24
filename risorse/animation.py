import threading
from IPython.display import display
import ipywidgets as widgets

class Animation:
    _thread = None
    _running_event = threading.Event()

    def __init__(self, canvas, update):
        self.canvas = canvas
        self.update = update
        self._create_styles()
        self._create_ui()

    def run(self):
        while Animation._running_event.is_set():
            self.update()

    def start(self):
        if not Animation._running_event.is_set():
            Animation._running_event.set()
            Animation._thread = threading.Thread(target=self.run)
            Animation._thread.start()

    def stop(self):
        Animation._running_event.clear()
        if Animation._thread is not None:
            Animation._thread.join()

    def display(self):
        container = widgets.VBox([self.styles, self.ui])
        display(container)

    def _create_ui(self):
        self.play_pause_button = widgets.ToggleButton(
            value=True,
            button_style='',
            tooltip='Play/Pause',
            icon='pause',
            _dom_classes=['play-pause-button']
        )

        self.play_pause_button.observe(self._toggle_play_pause, 'value')
        self.controls = widgets.HBox(
            [self.play_pause_button],
            _dom_classes=['controls']
        )

        self.ui = widgets.VBox([self.canvas, self.controls])
    
    def _toggle_play_pause(self, change):
        if change['new']:
            self.play_pause_button.icon = 'pause'
            self.start()
        else:
            self.play_pause_button.icon = 'play'
            self.stop()

    def _create_styles(self):
        css = """
            canvas {
                display: block;
                margin: 0 auto !important;
                padding: 0;
                background: white;  /* Ensure the canvas has a background color */
            }

            canvas:focus {
                outline: none;
                border: none;
            }

            .cell-output-ipywidget-background {
                width: auto !important;
                padding: 0 !important;
                background: transparent !important;
            }
     
            i.fa {
                margin: 0 !important;
            }

            .play-pause-button {
                width: 50px;
                height: 50px;
                border-radius: 100%;
                padding: 0;
            }
 
            .play-pause-button:focus {
                outline: none !important;
                box-shadow: none !important;
            }

            .controls {
                margin: 10px 0;
                width: 100%;
                display: flex;
                justify-content: center;
            }
        """

        self.styles = widgets.HTML(f"<style>{css}</style>")
