"""
Manim Animation 1: Eigenvalue Evolution Under Modular Flow
Duration: ~10 seconds
References: Diagram 2, Section 2.2, Theorems 72.3, 72.5, Equations E1936-E1940

Shows eigenvalues lambda_n evolving under modular flow sigma_t = exp(i*t*K_X),
with phase alignment leading to synchronization at t = T = 2*pi/omega_max.
"""

from manim import *
import numpy as np


class EigenvalueEvolution(Scene):
    """Eigenvalues evolving under modular flow with phase alignment and synchronization."""

    def construct(self):
        # Title
        title = Text("Eigenvalue Evolution Under Modular Flow", font_size=32)
        title.to_top().shift(UP * 0.3)
        subtitle = Text(
            r"$\sigma_t = \exp(i \cdot t \cdot K_X)$ — Phase Alignment & Synchronization",
            font_size=20,
        )
        subtitle.next_to(title, DOWN)

        # Phase evolution plot area
        axes = Axes(
            x_range=[0, 6.5, np.pi / 2],
            y_range=[0, 2 * np.pi, np.pi],
            x_length=10,
            y_length=5,
            axis_config={"color": GREY},
            x_axis_config={"numbers_to_include": [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]},
            y_axis_config={"numbers_to_include": [0, np.pi, 2 * np.pi]},
        )
        axes_labels = axes.get_axis_labels(
            Text("Time t", font_size=18),
            Text("Phase (mod 2$\pi$)", font_size=18),
        )

        # Eigenmode parameters
        n_modes = 6
        omegas = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
        t_max = 2 * np.pi / omegas[-1]  # Period T = 2*pi / omega_max
        colors = [BLUE, GREEN, RED, PURPLE, GOLD, TEAL]
        mode_labels = [r"$\omega_1$", r"$\omega_2$", r"$\omega_3$", r"$\omega_4$", r"$\omega_5$", r"$\omega_6$"]

        # Create phase curves
        phase_curves = []
        for i in range(n_modes):
            phase_func = lambda t, w=omegas[i]: (w * t) % (2 * np.pi)
            curve = axes.plot(phase_func, x_range=[0, t_max], color=colors[i], stroke_width=3)
            phase_curves.append(curve)

        # Synchronization marker
        sync_line = DashedLine(
            axes.c2p(t_max, 0),
            axes.c2p(t_max, 2 * np.pi),
            color=RED,
            dash_length=0.1,
        )
        sync_label = Text(f"Synchronization at t = T = {t_max:.2f}", color=RED, font_size=16)
        sync_label.next_to(sync_line, RIGHT, buff=0.2)

        # Eigenvalue display panel
        eigenvalue_panel = VGroup()
        for i in range(n_modes):
            eq = MathTex(
                rf"\lambda_{i+1} = \exp(\mu_{i+1})",
                color=colors[i],
                font_size=20,
            )
            eq.set_x(5).set_y(2.5 - i * 0.6)
            eigenvalue_panel.add(eq)

        # Phase alignment visualization (bottom)
        phase_circle = Circle(radius=1.5, color=WHITE, stroke_width=2)
        phase_circle.shift(DOWN * 3)
        phase_arrows = VGroup()
        for i in range(n_modes):
            angle = omegas[i] * 0
            arrow = Arrow(
                phase_circle.get_center(),
                phase_circle.get_center() + np.array([
                    1.5 * np.cos(angle),
                    1.5 * np.sin(angle),
                    0,
                ]),
                color=colors[i],
                buff=0,
                stroke_width=3,
            )
            phase_arrows.add(arrow)

        phase_label = Text("Phase Alignment at t = 0", font_size=16)
        phase_label.next_to(phase_circle, DOWN, buff=0.2)

        # Coherence display
        coherence_text = Text("Coherence C(t) = |Tr($\\sigma_t$) / N|", font_size=20, color=MAROON)
        coherence_text.to_edge(DOWN).shift(UP * 0.5)

        # Build scene
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)

        self.play(Write(axes), Write(axes_labels))
        self.wait(0.5)

        # Animate phase curves appearing
        for i, curve in enumerate(phase_curves):
            self.play(Create(curve), run_time=0.3)
        self.wait(0.5)

        # Animate eigenvalue panel
        self.play(FadeIn(eigenvalue_panel), run_time=1)
        self.wait(0.5)

        # Show synchronization point
        self.play(Create(sync_line), Write(sync_label))
        self.wait(0.5)

        # Animate phase evolution with animation
        t_animate = np.linspace(0, t_max, 200)
        for phase_curve, w in zip(phase_curves, omegas):
            # Get existing points and update
            old_points = phase_curve.points
            new_curve = axes.plot(
                lambda t: (w * t) % (2 * np.pi),
                x_range=[0, t_max],
                color=phase_curve.get_color(),
                stroke_width=3,
            )
            self.play(
                Transform(phase_curve, new_curve),
                run_time=0.5,
            )

        # Show phase circle
        self.play(Create(phase_circle), Write(phase_label))
        for i, arrow in enumerate(phase_arrows):
            self.play(Create(arrow), run_time=0.1)
        self.wait(0.5)

        # Show coherence
        self.play(Write(coherence_text))
        self.wait(1)

        # Final state: all phases aligned
        final_circle = Circle(radius=1.5, color=WHITE, stroke_width=2)
        final_circle.shift(DOWN * 3)
        final_arrows = VGroup()
        for i in range(n_modes):
            # All arrows point to same direction at synchronization
            arrow = Arrow(
                final_circle.get_center(),
                final_circle.get_center() + np.array([1.5, 0, 0]),
                color=colors[i],
                buff=0,
                stroke_width=3,
            )
            final_arrows.add(arrow)

        final_label = Text("Phase Alignment at t = T (Synchronization)", font_size=16, color=GREEN)
        final_label.next_to(final_circle, DOWN, buff=0.2)

        self.play(
            Transform(phase_circle, final_circle),
            Transform(phase_arrows, final_arrows),
            Transform(phase_label, final_label),
            run_time=1.5,
        )
        self.wait(1)

        # Summary text
        summary = Text(
            "Theorem 72.3: Period T = 2*pi/omega_max. Theorem 72.5: Coherence C > 0.8",
            font_size=14,
        )
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(1)
