import offshoot

from serpent.game_agent import GameAgent
from serpent.input_controller import MouseButton, KeyboardKey
from serpent.sprite_locator import SpriteLocator
# from serpent.machine_learning.context_classification.context_classifiers.cnn_inception_v3_context_classifier import CNNInceptionV3ContextClassifier

plugin_path = offshoot.config["file_paths"]["plugins"]

class SerpentTombOfTyrantsGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

        self.analytics_client = None

        self.sprite_locator = SpriteLocator()

        self.need_reset = False

    def setup_play(self):
        # TODO: get sprites for each screen to make the "screen dectection"

        self.game.window_controller.resize_window(self.game.window_id, 1280, 720)

    def handle_play(self, game_frame):
        logo_sprite = self.game.sprites["SPRITE_TOMB_OF_TYRANTS_LOGO"]

        isOnMenu = self.sprite_locator.locate(sprite=logo_sprite, game_frame=game_frame);

        print(isOnMenu)
