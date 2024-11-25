from manim import *

class SineWave(Scene):
    def construct(self):
        # create the axes
        axes = Axes(x_range=[-1, 10], y_range=[-1, 10])
        self.add(axes)

        # Create the graph
        graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        self.play(ApplyPointwiseFunction(lambda x: x*2, graph))