"""
Manim Animation 2: Action Potential Propagation Along Axon
Duration: ~15 seconds
References: Diagram 3, Section 3, Theorems 72.6-72.12, Equations E1946-E1960

Shows action potential propagating along axon with ion channels opening/closing.
Ion channel conductances mapped to eigenvalues: g_Na = lambda_Na/Z_Na, g_K = lambda_K/Z_K.
"""

from manim import *
import numpy as np


class ActionPotentialPropagation(Scene):
    """Action potential propagating along axon with ion channel dynamics."""

    def construct(self):
        # Title
        title = Text("Action Potential Propagation", font_size=32)
        title.to_top().shift(UP * 0.3)
        subtitle = Text(
            r"Hodgkin-Huxley: $V_m(t)$ with Ion Channel Eigenvalues",
            font_size=20,
        )
        subtitle.next_to(title, DOWN)

        # Axon representation
        axon_length = 10
        axon = Rectangle(
            width=axon_length,
            height=0.3,
            fill_color=GREY_B,
            fill_opacity=0.5,
            stroke_color=GREY,
            stroke_width=2,
        )
        axon.shift(LEFT * 0.5)

        axon_label = Text("Axon (myelinated)", font_size=16)
        axon_label.next_to(axon, DOWN, buff=0.2)

        # Membrane potential waveform display
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[-80, 40, 20],
            x_length=10,
            y_length=4,
            axis_config={"color": GREY},
        )
        axes_labels = axes.get_axis_labels(
            Text("Distance (mm)", font_size=16),
            Text("V_m (mV)", font_size=16),
        )
        axes.shift(UP * 1.5)

        # Action potential shape
        def ap_shape(x):
            """Simulate AP at position x along axon."""
            t = x / 2  # time delay proportional to distance
            if x < 1:
                return -70
            elif x < 2:
                return -70 + 100 * (1 - np.exp(-(x - 1) / 0.3)) ** 3
            elif x < 4:
                return 30 - 60 * (1 - np.exp(-(x - 2) / 1.5))
            elif x < 6:
                return -80 + 10 * (1 - np.exp(-(x - 4) / 2))
            else:
                return -70 + 5 * np.exp(-(x - 6) / 3)

        ap_curve = axes.plot(ap_shape, color=BLUE, stroke_width=3)

        # Resting potential line
        resting_line = DashedLine(
            axes.c2p(0, -70),
            axes.c2p(10, -70),
            color=GRAY,
            dash_length=0.1,
        )
        resting_label = Text("-70 mV (Resting)", font_size=12, color=GRAY)
        resting_label.next_to(resting_line, LEFT, buff=0.1)

        # Threshold line
        threshold_line = DashedLine(
            axes.c2p(0, -55),
            axes.c2p(10, -55),
            color=RED,
            dash_length=0.1,
        )
        threshold_label = Text("-55 mV (Threshold)", font_size=12, color=RED)
        threshold_label.next_to(threshold_line, LEFT, buff=0.1)

        # Ion channel eigenvalue bars (right side)
        channel_panel = VGroup()
        channel_names = [r"$\lambda_{Na}$", r"$\lambda_{K}$", r"$\lambda_{L}$"]
        channel_colors = [BLUE, GREEN, GOLD]
        channel_descs = ["Sodium", "Potassium", "Leak"]

        for i, (name, color, desc) in enumerate(zip(channel_names, channel_colors, channel_descs)):
            bar_bg = Rectangle(width=2, height=0.4, fill_color=color, fill_opacity=0.2, stroke_color=color)
            bar_bg.shift(RIGHT * 3.5 + UP * (2 - i * 0.8))
            bar_text = Text(f"{desc}: g = {name}/Z", font_size=14)
            bar_text.next_to(bar_bg, RIGHT, buff=0.1)
            channel_panel.add(bar_bg, bar_text)

        # Animated ion channel opening indicator
        na_indicator = Circle(radius=0.2, color=BLUE)
        na_indicator.next_to(channel_panel[0], LEFT, buff=0.1)
        na_open = Text("CLOSED", font_size=12, color=BLUE)
        na_open.next_to(na_indicator, LEFT, buff=0.1)

        k_indicator = Circle(radius=0.2, color=GREEN)
        k_indicator.next_to(channel_panel[1], LEFT, buff=0.1)
        k_open = Text("CLOSED", font_size=12, color=GREEN)
        k_open.next_to(k_indicator, LEFT, buff=0.1)

        l_indicator = Circle(radius=0.2, color=GOLD)
        l_indicator.next_to(channel_panel[2], LEFT, buff=0.1)
        l_open = Text("OPEN", font_size=12, color=GOLD)
        l_open.next_to(l_indicator, LEFT, buff=0.1)

        channel_indicators = VGroup(na_indicator, na_open, k_indicator, k_open, l_indicator, l_open)

        # Propagation marker (moving dot along axon)
        prop_dot = Dot(color=RED, radius=0.15)
        prop_dot.move_to(axon.get_left())

        # Equations panel
        equations = VGroup(
            MathTex(r"C_m \frac{dV_m}{dt} = -g_{Na}(V_m - E_{Na}) - g_K(V_m - E_K) - g_L(V_m - E_L)", font_size=16),
            MathTex(r"g_{Na} = \frac{\lambda_{Na}}{Z_{Na}}, \quad g_K = \frac{\lambda_K}{Z_K}, \quad g_L = \frac{\lambda_L}{Z_L}", font_size=16),
        )
        equations.arrange(DOWN, buff=0.2)
        equations.to_edge(UP).shift(DOWN * 0.3)

        # Build scene
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)

        self.play(Write(equations[0]))
        self.wait(0.5)
        self.play(Write(equations[1]))
        self.wait(0.5)

        self.play(Create(axon), Write(axon_label))
        self.wait(0.5)

        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        self.play(Create(resting_line), Write(resting_label))
        self.play(Create(threshold_line), Write(threshold_label))
        self.wait(0.5)

        self.play(Create(channel_panel), FadeIn(channel_indicators))
        self.wait(0.5)

        # Animate propagation
        for i in range(50):
            x_pos = i * axon_length / 50
            prop_dot.move_to(axon.get_left() + RIGHT * x_pos)

            # Ion channel states based on position
            if x_pos < 1.5:
                self.play(
                    na_indicator.set_fill(BLUE, 0),
                    Transform(na_open, Text("CLOSED", font_size=12, color=BLUE)),
                    run_time=0.1,
                )
            elif x_pos < 2.5:
                self.play(
                    na_indicator.set_fill(BLUE, 1),
                    Transform(na_open, Text("OPEN", font_size=12, color=BLUE)),
                    k_indicator.set_fill(GREEN, 0),
                    Transform(k_open, Text("CLOSED", font_size=12, color=GREEN)),
                    run_time=0.15,
                )
            elif x_pos < 4:
                self.play(
                    na_indicator.set_fill(BLUE, 0),
                    Transform(na_open, Text("CLOSED", font_size=12, color=BLUE)),
                    k_indicator.set_fill(GREEN, 1),
                    Transform(k_open, Text("OPEN", font_size=12, color=GREEN)),
                    run_time=0.15,
                )
            else:
                self.play(
                    k_indicator.set_fill(GREEN, 0),
                    Transform(k_open, Text("CLOSED", font_size=12, color=GREEN)),
                    run_time=0.1,
                )

            self.play(MoveAlongPath(prop_dot, axon), run_time=0.05, rate_func=linear)

        # Show final AP waveform
        self.play(Create(ap_curve))
        self.wait(0.5)

        # Theorem summary
        theorems = Text(
            "Theorem 72.6: g_ion = lambda_ion/Z_ion | Theorem 72.9: V_th = E_Na(1-exp(-lambda_Na/lambda_max))\n"
            "Theorem 72.10: v_prop = sqrt(g_Na/C_m) * (lambda_Na/lambda_K) | Theorem 72.8: V_m is eigenmode of Delta_X",
            font_size=12,
        )
        theorems.to_edge(DOWN)
        self.play(Write(theorems))
        self.wait(1)
