from serpent.game_agent import GameAgent


class SerpentTombOfTyrantsGameAgent(GameAgent):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.frame_handlers["PLAY"] = self.handle_play

        self.frame_handler_setups["PLAY"] = self.setup_play

        self.analytics_client = None

    def setup_play(self):
        self.game.window_controller.resize_window(self.game.window_id, 1280, 720)

    def handle_play(self, game_frame):
        print("handle_play")
