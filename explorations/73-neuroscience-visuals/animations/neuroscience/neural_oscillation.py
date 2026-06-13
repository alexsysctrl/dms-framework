"""
Manim Animation 3: Neural Oscillation EEG Frequency Bands
Duration: ~10 seconds
References: Diagram 1, Section 2.1-2.3, Theorems 72.2, 72.4, Equations E1936-E1945

Shows EEG frequency bands (Delta, Theta, Alpha, Beta, Gamma) with modular flow
sigma_t = exp(i*t*K_X) and power spectral density S(f).
"""

from manim import *
import numpy as np


class NeuralOscillationBands(Scene):
    """EEG frequency bands showing modular flow sigma_t = exp(i*t*K_X)."""

    def construct(self):
        # Title
        title = Text("Neural Oscillation EEG Frequency Bands", font_size=32)
        title.to_top().shift(UP * 0.3)
        subtitle = Text(
            r"Modular Flow: $\sigma_t = \exp(i \cdot t \cdot K_X)$",
            font_size=20,
        )
        subtitle.next_to(title, DOWN)

        # EEG Band definitions
        bands = [
            {"name": "Delta", "range": "0.5-4 Hz", "color": BLUE, "lambda_ratio": "[0.001, 0.008]", "eq": "E1936"},
            {"name": "Theta", "range": "4-8 Hz", "color": GREEN, "lambda_ratio": "[0.008, 0.016]", "eq": "E1936"},
            {"name": "Alpha", "range": "8-13 Hz", "color": RED, "lambda_ratio": "[0.016, 0.026]", "eq": "E1936"},
            {"name": "Beta", "range": "13-30 Hz", "color": PURPLE, "lambda_ratio": "[0.026, 0.060]", "eq": "E1936"},
            {"name": "Gamma", "range": "30-100 Hz", "color": GOLD, "lambda_ratio": "[0.060, 0.200]", "eq": "E1936"},
        ]

        # Band info panel
        band_panel = VGroup()
        for i, band in enumerate(bands):
            band_line = MathTex(
                rf"{band['name']}: f = \frac{{\lambda}}{{2\pi\hbar}} \in [{band['range']}]",
                color=band["color"],
                font_size=18,
            )
            band_line.shift(RIGHT * 3.5 + UP * (2.5 - i * 0.7))
            band_panel.add(band_line)

        # Power spectral density plot
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 1, 0.2],
            x_length=10,
            y_length=4,
            axis_config={"color": GREY},
            x_axis_config={"numbers_to_include": [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},
        )
        axes_labels = axes.get_axis_labels(
            Text("Frequency (Hz)", font_size=16),
            Text("Power S(f)", font_size=16),
        )
        axes.shift(LEFT * 0.5)

        # Power spectral density with EEG peaks
        def psd(f):
            delta_peak = 15 / (1 + ((f - 1.5) / 1.0) ** 2)
            theta_peak = 12 / (1 + ((f - 6) / 2.0) ** 2)
            alpha_peak = 20 / (1 + ((f - 10) / 2.5) ** 2)
            beta_peak = 10 / (1 + ((f - 20) / 5.0) ** 2)
            gamma_peak = 8 / (1 + ((f - 50) / 20.0) ** 2)
            noise = 5 / (f + 0.5)
            return (delta_peak + theta_peak + alpha_peak + beta_peak + gamma_peak + noise) / 30

        psd_curve = axes.plot(psd, color=STEEL_BLUE, stroke_width=4)

        # Band region fills
        band_fills = VGroup()
        band_regions = [
            (0.5, 4, BLUE, 0.15),
            (4, 8, GREEN, 0.15),
            (8, 13, RED, 0.15),
            (13, 30, PURPLE, 0.15),
            (30, 100, GOLD, 0.15),
        ]

        for f_lo, f_hi, color, alpha in band_regions:
            fill_curve = axes.plot(
                lambda f, lo=f_lo, hi=f_hi: psd(f) if f_lo <= f <= f_hi else 0,
                color=color,
                stroke_width=0,
            )
            band_fills.add(fill_curve)

        # Frequency band labels on plot
        band_label_positions = [
            (2.25, "Delta"),
            (6, "Theta"),
            (10.5, "Alpha"),
            (21.5, "Beta"),
            (65, "Gamma"),
        ]

        band_labels_on_plot = VGroup()
        for f_pos, label in band_label_positions:
            bl = Text(label, font_size=14, font_weight=BOLD)
            bl.move_to(axes.c2p(f_pos, psd(f_pos) + 0.15))
            band_labels_on_plot.add(bl)

        # Modular flow phase visualization (top right)
        phase_display = VGroup()
        n_phases = 5
        phase_angles = [0, 0, 0, 0, 0]  # all aligned at t=0
        phase_circles = VGroup()
        phase_arrows = VGroup()

        for i in range(n_phases):
            circle = Circle(radius=0.4, color=bands[i]["color"], stroke_width=2)
            circle.shift(RIGHT * 3.5 + UP * (3 - i * 0.8))
            phase_circles.add(circle)

            arrow = Arrow(
                circle.get_center(),
                circle.get_center() + np.array([0.4, 0, 0]),
                color=bands[i]["color"],
                buff=0,
                stroke_width=2,
            )
            phase_arrows.add(arrow)

        phase_display.add(phase_circles, phase_arrows)

        phase_label = Text("t = 0: Random Phases", font_size=14)
        phase_label.next_to(phase_display, UP, buff=0.1)

        # Eigenvalue to frequency mapping
        mapping_eq = MathTex(
            r"f_n = \frac{\lambda_n}{2\pi\hbar}",
            font_size=22,
            color=YELLOW,
        )
        mapping_eq.to_edge(DOWN).shift(UP * 0.5)

        # Build scene
        self.play(Write(title), Write(subtitle))
        self.wait(0.5)

        # Show band definitions
        for i, band_line in enumerate(band_panel):
            self.play(FadeIn(band_line), run_time=0.2)
        self.wait(0.5)

        # Show PSD plot
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)

        # Animate PSD curve
        self.play(Create(psd_curve))
        self.wait(0.5)

        # Show band regions
        for fill in band_fills:
            self.play(FadeIn(fill), run_time=0.3)
        self.wait(0.5)

        # Show band labels
        for bl in band_labels_on_plot:
            self.play(FadeIn(bl), run_time=0.2)
        self.wait(0.5)

        # Show modular flow phase evolution
        self.play(FadeIn(phase_display), Write(phase_label))
        self.wait(0.5)

        # Animate phase rotation (modular flow)
        omega_values = [0.5, 1.0, 1.5, 2.0, 2.5]
        for step in range(20):
            t = step * 0.15
            new_arrows = VGroup()
            for i in range(n_phases):
                angle = omega_values[i] * t
                arrow = Arrow(
                    phase_circles[i].get_center(),
                    phase_circles[i].get_center() + np.array([
                        0.4 * np.cos(angle),
                        0.4 * np.sin(angle),
                        0,
                    ]),
                    color=bands[i]["color"],
                    buff=0,
                    stroke_width=2,
                )
                new_arrows.add(arrow)

            self.play(
                Transform(phase_arrows, new_arrows),
                run_time=0.15,
            )

            # Update label
            if step == 19:
                self.play(
                    Transform(phase_label, Text("t = T: Synchronized!", font_size=14, color=GREEN)),
                    run_time=0.3,
                )

        # Show eigenvalue-frequency mapping
        self.play(Write(mapping_eq))
        self.wait(1)

        # Theorem summary
        theorems = Text(
            "Theorem 72.2: f_n = lambda_n/(2*pi*hbar) | Theorem 72.4: EEG Band Correspondence\n"
            "Theorem 72.5: Coherence C > 0.8 | Eq. E1943: S(f) = |sum c_n * exp(i*2*pi*f_n*t)|^2",
            font_size=12,
        )
        theorems.to_edge(DOWN)
        self.play(Write(theorems))
        self.wait(1)
