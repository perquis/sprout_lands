from abc import ABC


class Rigidbody(ABC):
    """
    A class for controlling the movement
    of the game object in Pygame.
    """

    def __init__(self) -> None:
        self.sprint = False

    def toggle_sprint(self):
        if self.sprint:
            self.sprint = False
        else:
            self.sprint = True

        return self.sprint
