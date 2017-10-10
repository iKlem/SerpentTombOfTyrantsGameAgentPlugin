import time

from serpent.game_agent import GameAgent
# from serpent.input_controller import MouseButton, KeyboardKey
from serpent.sprite_locator import SpriteLocator


class SerpentTombOfTyrantsGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

        self.analytics_client = None

        self.sprite_locator = SpriteLocator()

        self.need_reset = True
        self.game_paused = False

    def setup_play(self):
        self.game.window_controller.resize_window(
            self.game.window_id,
            1280,
            720
        )

    def handle_play(self, game_frame):
        if self.check_on_menu(game_frame):
            print("The game is on the menu.")
            if self.need_reset:
                print("RESET NEEDED!!!")
                self.do_reset(game_frame)
                time.sleep(2)
                self.input_controller.click()
            else:
                print("Resuming game...")
                self.start_or_resume(game_frame)
        else:
            print("The game is live.")
            self.handle_play_random(game_frame)

    def check_on_menu(self, game_frame):
        print(self.sprite_locator.locate(
            sprite=self.game.sprites["SPRITE_TOMB_OF_TYRANTS_LOGO"],
            game_frame=game_frame
        ))
        return self.sprite_locator.locate(
            sprite=self.game.sprites["SPRITE_TOMB_OF_TYRANTS_LOGO"],
            game_frame=game_frame
        ) is not None

    # This method is used for random grid/build play.
    def handle_play_random(self, game_frame):
        print("GRID PLAY")

        print("BUILD PLAY")

    def start_or_resume(self, game_frame):
        self.input_controller.click_string(
            query_string="RULE",
            game_frame=game_frame,
            ocr_preset=self.game.ocr_presets["MENU"]
        )

    def do_reset(self, game_frame):
        self.input_controller.click_string(
            query_string="USURP",
            game_frame=game_frame,
            ocr_preset=self.game.ocr_presets["MENU"]
        )

        self.input_controller.click_screen_region(
            screen_region="RESTART_YES"
        )

        self.need_reset = False
