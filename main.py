from manim import GREEN, RED, GOLD, GRAY, BLUE_E, BLUE
from manimlib.imports import *

class LinearTransformation3D(ThreeDScene):
    CONFIG = {
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
    }



    def construct(self):
        A = np.array([
            [round(math.cos(60 / 180 * math.pi), 2), -round(math.sin(60 / 180 * math.pi), 2), 0],
            [round(math.sin(60 / 180 * math.pi), 2), round(math.cos(60 / 180 * math.pi), 2), 0],
            [0, 0, 1]
        ])

        B = np.array([
            [1, 0, 0],
            [0, round(math.cos(30 / 180 * math.pi), 2), -round(math.sin(30 / 180 * math.pi), 2)],
            [0, round(math.sin(30 / 180 * math.pi), 2), round(math.cos(30 / 180 * math.pi), 2)]
        ])


        axes = ThreeDAxes()
        axes.set_color(GRAY)
        axes.add(axes.get_axis_labels())

        self.set_camera_orientation(phi=55 * DEGREES, theta=-45 * DEGREES)

        # basis vectors i,j,k
        basis_vector_helper = TextMobject("$i$", "$,$", "$j$", "$,$", "$k$")
        basis_vector_helper[0].set_color(GREEN)
        basis_vector_helper[2].set_color(RED)
        basis_vector_helper[4].set_color(GOLD)

        basis_vector_helper.to_corner(UP + RIGHT)

        self.add_fixed_in_frame_mobjects(basis_vector_helper)

        # self.add_fixed_in_frame_mobjects(self.create_matrix(M))
        self.add_fixed_in_frame_mobjects(matrix_to_mobject(matrix=B).set_color(GREEN).scale(0.7).to_corner(UP + LEFT))
        self.add_fixed_in_frame_mobjects(matrix_to_mobject(matrix=A).set_color(BLUE_E).scale(0.7).to_corner(DOWN + LEFT))

        # axes & camera
        self.add(axes)

        self.begin_ambient_camera_rotation(rate=0.2)

        cube = Cube(side_length=2, fill_color=BLUE, stroke_width=2, fill_opacity=0.1)
        cube.set_stroke(BLUE_E)

        i_vec = Vector(np.array([1, 0, 0]), color=GREEN)
        j_vec = Vector(np.array([0, 1, 0]), color=RED)
        k_vec = Vector(np.array([0, 0, 1]), color=GOLD)

        i_vec_new = Vector(A @ B @ np.array([1, 0, 0]), color=GREEN)
        j_vec_new = Vector(A @ B @ np.array([0, 1, 0]), color=RED)
        k_vec_new = Vector(A @ B @ np.array([0, 0, 1]), color=GOLD)

        self.play(
            ShowCreation(cube),
            GrowArrow(i_vec),
            GrowArrow(j_vec),
            GrowArrow(k_vec),
            Write(basis_vector_helper)
        )

        self.wait()

        matrix_anim = ApplyMatrix(A @ B, cube)

        self.play(
            matrix_anim,
            Transform(i_vec, i_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(j_vec, j_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time()),
            Transform(k_vec, k_vec_new, rate_func=matrix_anim.get_rate_func(),
                      run_time=matrix_anim.get_run_time())
        )

        self.wait()

        self.wait(7)
