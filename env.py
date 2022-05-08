class Env:

    def __init__(self):
        r = 10
        self.x_range = (0, 10 * r)
        self.y_range = (0, 10 * r)
        self.obs_boundary = self.obs_boundary()
        self.obs_circle = self.obs_circle()
        self.obs_rectangle = self.obs_rectangle()

    @staticmethod
    def obs_boundary():
        r = 10
        obs_boundary = [
            [0, 0, 0.1*r, 10*r],
            [0, 10*r, 10*r, 0.1*r],
            [0.1*r, 0, 10*r, 0.1*r],
            [10*r, 0.1*r, 0.1*r, 10*r]
        ]
        return obs_boundary

    @staticmethod
    def obs_rectangle():
        r = 10
        obs_rectangle = [
            [0.25*r, 4.25*r, 1.5*r, 1.5*r],
            [3.75*r, 4.25*r, 2.5*r, 1.5*r],
            [7.25*r, 2*r, 1.5*r, 2*r]
        ]
        return obs_rectangle

    @staticmethod
    def obs_circle():
        r = 10
        obs_cir = [
            [2*r, 2*r, 1*r],
            [2*r, 8*r, 1*r]
        ]

        return obs_cir
