from mmse15project.views.Login import Login
from tests.views.FrameTests import FrameTests


class LoginTests:
    def __init__(self):
        self.root = FrameTests(Login)

LoginTests().root.mainloop()
