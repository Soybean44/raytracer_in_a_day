from pathlib import Path

import moderngl_window as mglw
import numpy as np


class Window(mglw.WindowConfig):
    gl_version = (3, 3)
    resource_dir = (Path(__file__) / "..").absolute()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prog = self.load_program("main.glsl")
        vertices = np.array(
            [[0, 1, 0, 1, 0, 0], [-1, -1, 0, 0, 1, 0], [1, -1, 0, 0, 0, 1]],
            dtype="f4",
        )

        vbo = self.ctx.buffer(vertices.tobytes())
        self.vao = self.ctx.simple_vertex_array(self.prog, vbo, "in_pos", "in_color")

    def render(self, _time: float, _frametime):
        self.ctx.clear(0.0, 0.0, 0.0, 1.0)
        self.vao.render()


if __name__ == "__main__":
    Window.run()
