#!/usr/bin/env python3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse, Rectangle
from PIL import Image
import io
import os

FIGURES_DIR = '/Users/alex/Desktop/DMS_Framework/figures'

def save_fig(name, fig=None, dpi=150):
    if fig is None:
        fig = plt.gcf()
    path = os.path.join(FIGURES_DIR, name)
    fig.savefig(path, dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'Saved: {path}')
    return path

def plot_modular_spectrum():
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))
    ax1 = axes[0, 0]
    np.random.seed(42)
    n_levels = 200
    eigenvalues = np.sort(np.random.exponential(1.0, n_levels))
    eigenvalues = eigenvalues**2
    ax1.hist(eigenvalues, bins=50, color='#2166AC', alpha=0.8, edgecolor='white', linewidth=0.5)
    ax1.axvline(x=eigenvalues[-1], color='red', linestyle='--', linewidth=2, label=r'$\lambda_{max}$')
    ax1.axvline(x=eigenvalues[0], color='green', linestyle='--', linewidth=2, label=r'$\lambda_{min}$')
    ax1.set_xlabel(r'$\lambda_n^2$ (eigenvalues of $D^2$)', fontsize=12)
    ax1.set_ylabel('Count', fontsize=12)
    ax1.set_title(r'Modular Operator Spectrum: $\Delta_X = \exp(D^2)$', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    ax2 = axes[0, 1]
    hist_counts, hist_edges = np.histogram(eigenvalues, bins=100)
    rho = hist_counts.astype(float) / np.diff(hist_edges)
    centers = (hist_edges[:-1] + hist_edges[1:]) / 2
    ax2.plot(centers, rho, color='#E6550D', linewidth=2)
    ax2.fill_between(centers, rho, alpha=0.3, color='#E6550D')
    ax2.set_xlabel(r'$\lambda^2$', fontsize=12)
    ax2.set_ylabel(r'$\rho(\lambda^2)$', fontsize=12)
    ax2.set_title('Density of States', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax3 = axes[1, 0]
    sorted_ev = np.sort(eigenvalues)
    cumulative = np.arange(1, len(sorted_ev)+1) / len(sorted_ev)
    ax3.semilogy(sorted_ev, cumulative, color='#7522A1', linewidth=2)
    ax3.axhline(y=0.5, color='gray', linestyle=':', alpha=0.5)
    ax3.set_xlabel(r'$\lambda_n^2$', fontsize=12)
    ax3.set_ylabel('Cumulative fraction', fontsize=12)
    ax3.set_title('Cumulative Eigenvalue Distribution', fontsize=14, fontweight='bold')
    ax3.grid(True, alpha=0.3)
    ax4 = axes[1, 1]
    ax4.set_xlim(-0.5, 4.5)
    ax4.set_ylim(-0.5, 10.5)
    ax4.set_ylabel(r'Energy $E_n = \lambda_n^2$', fontsize=12)
    ax4.set_xlabel('Level n', fontsize=12)
    ax4.set_title(r'Energy Levels $E_n = \lambda_n^2$', fontsize=14, fontweight='bold')
    ax4.set_xticks(range(0, 10))
    ax4.axhline(y=0, color='black', linewidth=1)
    for i in range(10):
        y_val = (i + 1) * 0.8 + np.random.uniform(-0.2, 0.2)
        ax4.plot(i, y_val, 'o', color='#2166AC', markersize=8)
        ax4.plot([0, i], [y_val, y_val], 'k--', alpha=0.3, linewidth=0.5)
    ax4.text(10.5, 8, r'$\Delta_X |\psi_n\rangle = \exp(\lambda_n^2) |\psi_n\rangle$', fontsize=9)
    ax4.text(10.5, 7, r'$K_X = \log(\Delta_X) = D^2$', fontsize=9)
    ax4.text(10.5, 6, r'$\sigma_t(a) = e^{itK_X} a e^{-itK_X}$', fontsize=9)
    ax4.spines['top'].set_visible(False)
    ax4.spines['right'].set_visible(False)
    ax4.spines['bottom'].set_visible(False)
    ax4.set_yticks([])
    fig.suptitle('DMS Modular Operator Spectrum', fontsize=16, fontweight='bold', y=0.98)
    save_fig('modular-spectrum.png', fig)

def plot_virasoro_algebra():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-4, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text(0, 3.5, 'Virasoro Algebra from Modular Flow', fontsize=18, fontweight='bold', ha='center')
    central_box = FancyBboxPatch((-3, 2.5), 6, 0.8, boxstyle="round,pad=0.1", edgecolor='#2166AC', facecolor='#D6E4F0', linewidth=2)
    ax.add_patch(central_box)
    ax.text(0, 2.9, r'$[L_m, L_n] = (m-n)L_{m+n} + \frac{c}{12}m(m^2-1)\delta_{m+n,0}$', fontsize=14, ha='center', va='center')
    m_vals = [-3, -2, -1, 0, 1, 2, 3]
    n_vals = [-3, -2, -1, 0, 1, 2, 3]
    for i, m in enumerate(m_vals):
        for j, n in enumerate(n_vals):
            x_pos = m * 0.8 - 2.4
            y_pos = n * 0.8 - 1.6
            if m == 0 and n == 0:
                color = '#E6550D'
                ec = '#E6550D'
                lw = 2
            elif abs(m - n) <= 1:
                color = '#D6E4F0'
                ec = '#2166AC'
                lw = 1.5
            else:
                color = 'white'
                ec = '#2166AC'
                lw = 1
            box = FancyBboxPatch((x_pos - 0.3, y_pos - 0.3), 0.6, 0.6, boxstyle="round,pad=0.02", edgecolor=ec, facecolor=color, linewidth=lw)
            ax.add_patch(box)
            ax.text(x_pos, y_pos, r'$L_{{{}}}$'.format(m), fontsize=9, ha='center', va='center')
    arrow1 = FancyArrowPatch((0.8, 0.3), (1.8, 0.8), arrowstyle='->', mutation_scale=20, linewidth=2, color='#7522A1')
    ax.add_patch(arrow1)
    ax.text(1.3, 0.6, r'$[L_1, L_{-1}]$', fontsize=10, color='#7522A1')
    arrow2 = FancyArrowPatch((-1.6, 0.3), (-0.6, 0.8), arrowstyle='->', mutation_scale=20, linewidth=2, color='#7522A1')
    ax.add_patch(arrow2)
    ax.text(-1.1, 0.6, r'$[L_{-1}, L_1]$', fontsize=10, color='#7522A1')
    ax.text(4.5, 2.5, r'$c = 12\tau_2$', fontsize=12, bbox=dict(boxstyle='round', facecolor='#FFF3CD', edgecolor='#E6A800', linewidth=1.5))
    ax.text(0, -2.5, r'$L_m = \frac{1}{2\pi}\int_0^{2\pi} d\sigma\, e^{im\sigma}\, T_{modular}(\sigma)$', fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=1.5))
    ax.text(0, -3.3, r'$T_{modular}(\sigma) = \frac{1}{\alpha\prime} \,: \partial_\sigma X^\mu \partial_\sigma X_\mu :$', fontsize=11, ha='center', style='italic', bbox=dict(boxstyle='round', facecolor='#F3E5F5', edgecolor='#7522A1', linewidth=1))
    ax.text(-4.5, 2.5, r'$T(z)T(w) \sim \frac{c}{2(z-w)^4} + \frac{2T(w)}{(z-w)^2} + \frac{\partial_w T(w)}{z-w}$', fontsize=9, ha='right', bbox=dict(boxstyle='round', facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=1))
    save_fig('virasoro-algebra.png', fig)

def plot_black_hole_shadow():
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    p = 2
    lambda_min_sq = 0.5
    R_shadow_sw = 3 * np.sqrt(3)
    R_shadow_kerr = 3 * np.sqrt(3) * 0.85
    delta_R_p = R_shadow_sw * p**(-np.log2(lambda_min_sq))
    ax1 = axes[0]
    ax1.set_xlim(-5, 5)
    ax1.set_ylim(-5, 5)
    ax1.set_aspect('equal')
    ax1.axis('off')
    ax1.set_title('Schwarzschild Shadow\n$R_{shadow} = 3\sqrt{3}\,GM/c^2$', fontsize=13, fontweight='bold')
    circle1 = Circle((0, 0), R_shadow_sw * 0.7, fill=False, edgecolor='gray', linewidth=1, linestyle='--')
    ax1.add_patch(circle1)
    ax1.text(0, -R_shadow_sw * 0.7 - 0.5, 'Photon sphere\n$r_{ps} = 3GM/c^2', ha='center', fontsize=9)
    circle2 = Circle((0, 0), R_shadow_sw, fill=True, facecolor='#1a1a2e', edgecolor='white', linewidth=2)
    ax1.add_patch(circle2)
    circle3 = Circle((0, 0), R_shadow_sw + 0.3, fill=False, edgecolor='#E6550D', linewidth=3, linestyle=':')
    ax1.add_patch(circle3)
    ax1.text(R_shadow_sw + 1.2, 0, r'$\delta_R^{(p)}$', fontsize=11, color='#E6550D')
    ax1.plot(4.5, 4.5, 'o', color='yellow', markersize=12)
    ax1.plot([0, 4.5], [0, 4.5], 'y--', linewidth=1, alpha=0.5)
    ax1.text(4.7, 4.7, 'Observer', fontsize=10, color='yellow')
    ax2 = axes[1]
    ax2.set_xlim(-5, 5)
    ax2.set_ylim(-5, 5)
    ax2.set_aspect('equal')
    ax2.axis('off')
    ax2.set_title('Kerr Shadow (rotating)\n$R_{shadow}^{(Kerr)} = 3\sqrt{3}\,GM/c^2\,(1-a/2M)$', fontsize=13, fontweight='bold')
    ellipse = Ellipse((0, 0), R_shadow_kerr * 2.2, R_shadow_kerr * 1.6, fill=True, facecolor='#1a1a2e', edgecolor='white', linewidth=2)
    ax2.add_patch(ellipse)
    ax2.arrow(0, -4.5, 0, 9, head_width=0.3, head_length=0.3, fc='cyan', ec='cyan', alpha=0.5)
    ax2.text(0.5, 4.5, 'J (rotation)', fontsize=10, color='cyan')
    ax2.plot([-R_shadow_kerr * 1.1, R_shadow_kerr * 1.1], [0, 0], 'r--', linewidth=1.5)
    ax2.plot([0, 0], [-R_shadow_kerr * 0.8, R_shadow_kerr * 0.8], 'g--', linewidth=1.5)
    ax2.text(R_shadow_kerr * 1.3, 0, 'R_major', fontsize=9, color='red')
    ax2.text(0.3, R_shadow_kerr * 1.0, 'R_minor', fontsize=9, color='green')
    ax2.text(R_shadow_kerr * 1.5, 2, r'$\delta_R^{(p,Kerr)}$', fontsize=10, color='#E6550D', bbox=dict(boxstyle='round', facecolor='#FFF3CD'))
    ax3 = axes[2]
    theta = np.linspace(0, 2*np.pi, 200)
    I_0 = 1.0 / (1 + 2 * theta / (2*np.pi))
    delta_p = p**(-np.log2(lambda_min_sq))
    theta_p = 2 * np.pi / np.log(p)
    I_p = I_0 * (1 + delta_p * np.cos(2 * np.pi * theta / theta_p))
    ax3.plot(theta, I_0, 'b--', linewidth=1.5, label='Classical $I_0(\theta)$')
    ax3.plot(theta, I_p, 'r-', linewidth=2, label='DMS: $I(\theta)$')
    ax3.fill_between(theta, I_0, I_p, alpha=0.2, color='red')
    ax3.set_xlabel(r'$\theta$ (angle)', fontsize=11)
    ax3.set_ylabel('Intensity', fontsize=11)
    ax3.set_title('p-adic Intensity Oscillations', fontsize=13, fontweight='bold')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.axhline(y=0, color='black', linewidth=0.5)
    fig.suptitle('Black Hole Shadows with p-adic Corrections', fontsize=16, fontweight='bold')
    save_fig('black-hole-shadow.png', fig)

def plot_padic_ultrametric_tree():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.text(0, 5.5, 'p-adic Ultrametric Tree Structure', fontsize=18, fontweight='bold', ha='center')
    def draw_branch(x, y, length, angle, depth, max_depth):
        if depth > max_depth:
            return []
        nodes = []
        x_end = x + length * np.cos(angle)
        y_end = y + length * np.sin(angle)
        if depth == 0:
            color = '#2166AC'
            lw = 3
        else:
            color = '#2166AC'
            lw = 2 - depth * 0.3
        ax.plot([x, x_end], [y, y_end], color=color, linewidth=lw)
        if depth == max_depth:
            circle = Circle((x_end, y_end), 0.2, fill=True, facecolor='#E6550D', edgecolor='white', linewidth=1.5)
            ax.add_patch(circle)
            nodes.append((x_end, y_end))
        else:
            circle = Circle((x_end, y_end), 0.15, fill=True, facecolor='white', edgecolor=color, linewidth=1.5)
            ax.add_patch(circle)
            nodes.append((x_end, y_end))
        next_length = length * 0.6
        for i in range(3):
            new_angle = angle + (i - 1) * np.pi / 4
            sub_nodes = draw_branch(x_end, y_end, next_length, new_angle, depth + 1, max_depth)
            nodes.extend(sub_nodes)
        return nodes
    draw_branch(0, 0, 2.5, np.pi/2, 0, 4)
    ball1 = Circle((0, 0), 2.5, fill=False, edgecolor='#7522A1', linewidth=2, linestyle='--', alpha=0.7)
    ax.add_patch(ball1)
    ax.text(-3.8, 0, r'$B_{p^{-0}}$', fontsize=10, color='#7522A1')
    ball2 = Circle((0, 0), 1.5, fill=False, edgecolor='#E6550D', linewidth=2, linestyle='--', alpha=0.7)
    ax.add_patch(ball2)
    ax.text(1.5, 1.5, r'$B_{p^{-1}}$', fontsize=10, color='#E6550D')
    ball3 = Circle((0, 0), 0.8, fill=True, facecolor='#D6E4F0', edgecolor='#2166AC', linewidth=2, alpha=0.5)
    ax.add_patch(ball3)
    ax.text(0.5, -1.2, r'$B_{p^{-2}}$', fontsize=10, color='#2166AC')
    ax.text(0, -4.5, r'Ultrametric inequality: $d_p(x,z) \leq \max(d_p(x,y), d_p(y,z))$', fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=2))
    ax.text(0, -5.3, 'Every triangle is isosceles with two equal sides', fontsize=11, ha='center', style='italic')
    ax.text(-5.5, 3, 'Any two balls:\neither disjoint\nor one contained\nin the other', fontsize=9, ha='center', bbox=dict(boxstyle='round', facecolor='#FFF3CD', edgecolor='#E6A800', linewidth=1.5))
    ax.text(5.5, 3, r'$B_{p^{-k}}(x) = \bigcup_{j=0}^{p-1} B_{p^{-(k+1)}}(x + j \cdot p^k)$', fontsize=9, ha='right', bbox=dict(boxstyle='round', facecolor='#F3E5F5', edgecolor='#7522A1', linewidth=1))
    save_fig('padic-ultrametric-tree.png', fig)

def plot_dms_architecture():
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.axis('off')
    central = FancyBboxPatch((-1.5, 1), 3, 2, boxstyle="round,pad=0.15", edgecolor='black', facecolor='#1a1a2e', linewidth=3)
    ax.add_patch(central)
    ax.text(0, 2, r'$\Delta_X = \exp(D^2)$', fontsize=14, color='white', ha='center', fontweight='bold')
    ax.text(0, 1.4, 'Modular Operator', fontsize=10, color='white', ha='center')
    von_neumann = FancyBboxPatch((-2.5, -0.5), 5, 1.3, boxstyle="round,pad=0.1", edgecolor='#2166AC', facecolor='#D6E4F0', linewidth=2)
    ax.add_patch(von_neumann)
    ax.text(0, 0.3, r'$M_X = \{T \in B(H) \mid [T, \Delta_X] = 0\}$', fontsize=11, ha='center')
    ax.text(0, -0.2, 'Type III$_1$ (QG) $\to$ Type I (classical)', fontsize=9, ha='center')
    arrow = FancyArrowPatch((0, 1), (0, 0.5), arrowstyle='->', mutation_scale=25, linewidth=2.5, color='black')
    ax.add_patch(arrow)
    branches = [('Quantum\nMechanics', -6, 4, '#2166AC'), ('QFT', -6, 0, '#E6550D'), ('General\nRelativity', -6, -4, '#2E7D32'), ('Cosmology', 6, 4, '#7522A1'), ('Information\nTheory', 6, 0, '#E6550D'), ('p-adic\nQuantum\nGravity', 6, -4, '#1565C0')]
    for name, x, y, color in branches:
        box = FancyBboxPatch((x - 1, y - 0.6), 2, 1.8, boxstyle="round,pad=0.1", edgecolor=color, facecolor=color, alpha=0.2, linewidth=2)
        ax.add_patch(box)
        ax.text(x, y + 0.3, name, fontsize=10, color=color, ha='center', fontweight='bold')
    connections = [((0, 1), (-5, 4), '#2166AC'), ((0, 1), (-5, 0), '#E6550D'), ((0, 1), (-5, -4), '#2E7D32'), ((0, 1), (5, 4), '#7522A1'), ((0, 1), (5, 0), '#E6550D'), ((0, 1), (5, -4), '#1565C0')]
    for (x1, y1), (x2, y2), color in connections:
        arrow = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle='->', mutation_scale=15, linewidth=1.5, color=color, alpha=0.6)
        ax.add_patch(arrow)
    bottom_nodes = [(r'$K_X = D^2$', -4, -6.5, 'Modular Hamiltonian'), (r'$\sigma_t = e^{itK_X}$', 0, -6.5, 'Modular Flow'), (r'$S_{ent} = -Tr(\Delta_X \log \Delta_X)$', 4, -6.5, 'Entanglement Entropy')]
    for text, x, y, label in bottom_nodes:
        box = FancyBboxPatch((x - 1.2, y - 0.4), 2.4, 0.8, boxstyle="round,pad=0.05", edgecolor='black', facecolor='white', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y + 0.1, text, fontsize=8, ha='center')
        ax.text(x, y - 0.3, label, fontsize=7, ha='center', style='italic', color='gray')
    arrow2 = FancyArrowPatch((0, -0.5), (0, -5.8), arrowstyle='->', mutation_scale=20, linewidth=2, color='black')
    ax.add_patch(arrow2)
    ax.text(0, 7, 'DMS Framework Architecture', fontsize=18, fontweight='bold', ha='center')
    save_fig('dms-architecture.png', fig)

def plot_band_structure():
    fig, ax = plt.subplots(figsize=(12, 8))
    k = np.linspace(0, 2*np.pi, 200)
    n_bands = 8
    bands = []
    for n in range(n_bands):
        E_n = (n + 0.5) * 0.8 + 0.3 * np.cos(k * (n + 1))
        bands.append(E_n)
    E_fermi = 3.5
    for i in range(0, n_bands, 2):
        ax.fill_between(k, bands[i], bands[i+1] if i+1 < n_bands else bands[i] + 1.5, alpha=0.3, color='#2166AC')
    for i in range(1, n_bands, 2):
        ax.plot(k, bands[i], 'b-', linewidth=2)
    ax.axhline(y=E_fermi, color='red', linestyle='--', linewidth=2, label='Fermi level')
    ax.axhline(y=E_fermi + 0.5, color='green', linestyle=':', linewidth=1.5, label=r'Band gap $\Delta E$')
    ax.annotate('', xy=(1.5, E_fermi + 0.5), xytext=(1.5, E_fermi), arrowprops=dict(arrowstyle='<->', color='green', lw=2))
    ax.text(1.8, (E_fermi + E_fermi + 0.5) / 2, r'$\Delta E$', fontsize=12, color='green')
    ax.set_xlabel(r'$k$ (momentum)', fontsize=12)
    ax.set_ylabel(r'$E_n = \lambda_n^2$', fontsize=12)
    ax.set_title(r'Electronic Band Structure from DMS Eigenvalues\n$E_n = \lambda_n^2$, Band gap $\Delta E \sim \lambda_{min}^2$', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 9)
    ax.text(0.2, 2, 'Valence\nband', fontsize=10, color='white', fontweight='bold', bbox=dict(boxstyle='round', facecolor='#2166AC', alpha=0.8))
    ax.text(0.2, 6, 'Conduction\nband', fontsize=10, color='white', fontweight='bold', bbox=dict(boxstyle='round', facecolor='#E6550D', alpha=0.8))
    ax.text(5.5, 7, r'$\Delta E^{(p)} = \Delta E \cdot p^{-v_p(\lambda_{min}^2)}$', fontsize=10, bbox=dict(boxstyle='round', facecolor='#F3E5F5', edgecolor='#7522A1', linewidth=1.5))
    save_fig('band-structure.png', fig)

def plot_gravitational_wave_spectrum():
    fig, ax = plt.subplots(figsize=(12, 8))
    f = np.logspace(-11, -6, 500)
    f_peak = 1e-9
    sigma = 0.5e-9
    G_f = 1e-21 * (f / f_peak)**2 / ((f / f_peak)**2 + (sigma / f_peak)**2)
    G_bg = 1e-22 * (f / 1e-9)**(-2/3)
    G_total = G_f + G_bg
    ax.loglog(f, G_total, 'b-', linewidth=2.5, label='DMS: $G(f)$')
    ax.loglog(f, G_f, 'r--', linewidth=2, label='Peak: $f_{peak} = \lambda_{max}/(2\pi)$')
    ax.loglog(f, G_bg, 'g:', linewidth=2, label='Background')
    ax.plot(f_peak, G_f[f.argmax()], 'ro', markersize=12)
    ax.annotate(f'$f_{{peak}} = 10^{{-9}}$ Hz', xy=(f_peak, G_f[f.argmax()]), xytext=(f_peak * 3, G_f[f.argmax()] * 2), arrowprops=dict(arrowstyle='->', color='red', lw=2), fontsize=11, color='red')
    ax.axvline(x=f_peak, color='red', linestyle='--', alpha=0.5, linewidth=1.5)
    ax.plot(1e-9, 1e-21, 'o', color='orange', markersize=15, label='Sgr A*', zorder=5)
    ax.plot(1e-10, 5e-22, 's', color='purple', markersize=12, label='M87*', zorder=5)
    ax.set_xlabel('Frequency f (Hz)', fontsize=12)
    ax.set_ylabel(r'$G(f)$ (strain$^2$/Hz)', fontsize=12)
    ax.set_title(r'Gravitational Wave Spectrum from DMS\n$G(f)$ peak at $f_{peak} = \lambda_{max}/(2\pi)$', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10, loc='upper left')
    ax.grid(True, alpha=0.3, which='both')
    ax.text(0.02, 0.95, r'$\delta G^{(p)} = G(f) \cdot p^{-v_p(\lambda_{min}^2)}$', transform=ax.transAxes, fontsize=10, bbox=dict(boxstyle='round', facecolor='#FFF3CD', edgecolor='#E6A800', linewidth=1.5), ha='left')
    save_fig('gravitational-wave-spectrum.png', fig)

def plot_neural_network_dms():
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 9)
    ax.axis('off')
    ax.text(3.5, 8.5, 'Neural Network Architecture from DMS Modular Operator', fontsize=16, fontweight='bold', ha='center')
    layers = [('Input:\n$\lambda_n^2$', 0.5, 6, '#2166AC'), ('Hidden 1:\n$\sigma_t$', 2, 6, '#E6550D'), ('Hidden 2:\n$\Delta_X$', 3.5, 6, '#2E7D32'), ('Hidden 3:\n$K_X=D^2$', 5, 6, '#7522A1'), ('Output:\n$M_X$', 6.5, 6, '#1565C0')]
    node_positions = []
    for i, (name, x, y, color) in enumerate(layers):
        circle = Circle((x, y), 0.5, fill=True, facecolor=color, edgecolor='white', linewidth=2)
        ax.add_patch(circle)
        ax.text(x, y, name, fontsize=8, color='white', ha='center', va='center')
        node_positions.append((x, y))
    for i in range(len(node_positions) - 1):
        x1, y1 = node_positions[i]
        x2, y2 = node_positions[i + 1]
        for j in range(3):
            offset = (j - 1) * 0.15
            ax.plot([x1 + offset, x2 - offset], [y1, y2], color='#555555', linewidth=2 - j * 0.5, alpha=0.6 - j * 0.15)
    ax.text(3.5, 3.8, r'$\sigma_t(a) = e^{itK_X} a e^{-itK_X}$', fontsize=12, ha='center', bbox=dict(boxstyle='round', facecolor='#E3F2FD', edgecolor='#1565C0', linewidth=2))
    ax.text(3.5, 2.8, r'$x_i^{(l+1)} = \sum_j W_{ij}^{(l)} \cdot \sigma(\lambda_j^2 \cdot x_i^{(l)})$', fontsize=10, ha='center', style='italic', bbox=dict(boxstyle='round', facecolor='#F3E5F5', edgecolor='#7522A1', linewidth=1.5))
    ax.text(3.5, 1.8, r'$W_{ij} = \frac{\lambda_i^2 \lambda_j^2}{\lambda_i^2 + \lambda_j^2}$', fontsize=10, ha='center', bbox=dict(boxstyle='round', facecolor='#FFF3CD', edgecolor='#E6A800', linewidth=1.5))
    ax.text(3.5, 0.8, r'$\sigma(\lambda^2) = \frac{1}{1 + e^{-\lambda^2}}$', fontsize=10, ha='center', style='italic', bbox=dict(boxstyle='round', facecolor='#E8F5E9', edgecolor='#2E7D32', linewidth=1.5))
    features = [('Quantum\nStates', 1, 0.3), ('QFT\nAction', 3, 0.3), ('GR\nCurvature', 5, 0.3)]
    for name, x, y in features:
        box = FancyBboxPatch((x - 0.6, y - 0.3), 1.2, 0.6, boxstyle="round,pad=0.05", edgecolor='gray', facecolor='white', linewidth=1.5)
        ax.add_patch(box)
        ax.text(x, y, name, fontsize=8, ha='center', va='center')
        ax.plot([6.5, x + 0.6], [6, y + 0.3], 'k--', linewidth=1, alpha=0.4)
    save_fig('neural-network-dms.png', fig)

def plot_information_theory():
    fig, ax = plt.subplots(figsize=(12, 9))
    ax.set_xlim(-6, 6)
    ax.set_ylim(-5, 5)
    ax.axis('off')
    ax.text(0, 4.5, 'Information Theory from DMS Modular Trace', fontsize=16, fontweight='bold', ha='center')
    central_box = FancyBboxPatch((-3, 2.5), 6, 1.2, boxstyle="round,pad=0.1", edgecolor='black', facecolor='#1a1a2e', linewidth=2)
    ax.add_patch(central_box)
    ax.text(0, 3.3, r'$S_{ent} = -Tr(\Delta_X \log(\Delta_X)) = -\sum_n e^{\lambda_n^2} \lambda_n^2$', fontsize=12, color='white', ha='center')
    ax.text(0, 2.7, 'Entanglement entropy from modular trace', fontsize=10, color='white', ha='center', style='italic')
    shannon_box = FancyBboxPatch((-4, 0.5), 3, 1.5, boxstyle="round,pad=0.1", edgecolor='#2166AC', facecolor='#D6E4F0', linewidth=2)
    ax.add_patch(shannon_box)
    ax.text(-2.5, 1.5, r'$S_{Shannon} = -\sum p_i \log p_i$', fontsize=11, ha='center')
    ax.text(-2.5, 0.8, 'Shannon entropy', fontsize=10, ha='center', style='italic')
    padic_box = FancyBboxPatch((1, 0.5), 3, 1.5, boxstyle="round,pad=0.1", edgecolor='#7522A1', facecolor='#F3E5F5', linewidth=2)
    ax.add_patch(padic_box)
    ax.text(2.5, 1.5, r'$S_p = \log(p) \cdot \chi(M_X) = \log(p)$', fontsize=11, ha='center')
    ax.text(2.5, 0.8, 'p-adic entropy', fontsize=10, ha='center', style='italic')
    vneumann_box = FancyBboxPatch((-4, -2), 3, 1.5, boxstyle="round,pad=0.1", edgecolor='#E6550D', facecolor='#FFF3CD', linewidth=2)
    ax.add_patch(vneumann_box)
    ax.text(-2.5, -1, r'$S_{vN} = -Tr(\rho_X \log \rho_X)$', fontsize=11, ha='center')
    ax.text(-2.5, -1.7, 'von Neumann entropy', fontsize=10, ha='center', style='italic')
    mutual_box = FancyBboxPatch((1, -2), 3, 1.5, boxstyle="round,pad=0.1", edgecolor='#2E7D32', facecolor='#E8F5E9', linewidth=2)
    ax.add_patch(mutual_box)
    ax.text(2.5, -1, r'$I(A:B) = S_A + S_B - S_{AB}$', fontsize=11, ha='center')
    ax.text(2.5, -1.7, 'Mutual information', fontsize=10, ha='center', style='italic')
    ax.annotate('', xy=(0, 2.5), xytext=(-2.5, 2), arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.annotate('', xy=(0, 2.5), xytext=(2.5, 2), arrowprops=dict(arrowstyle='->', color='black', lw=2))
    ax.annotate('', xy=(-2.5, 0.5), xytext=(-2.5, -0.5), arrowprops=dict(arrowstyle='->', color='#2166AC', lw=2))
    ax.annotate('', xy=(2.5, 0.5), xytext=(2.5, -0.5), arrowprops=dict(arrowstyle='->', color='#7522A1', lw=2))
    type_box = FancyBboxPatch((-3, -4), 6, 1, boxstyle="round,pad=0.1", edgecolor='black', facecolor='white', linewidth=2)
    ax.add_patch(type_box)
    ax.text(0, -3.5, r'Type III $\longrightarrow$ Type I: $S_{III} = \infty \to S_I = \log(N)$', fontsize=11, ha='center')
    ax.text(0, -4, 'Information recovery via Type transition', fontsize=9, ha='center', style='italic')
    ax.text(0, -4.7, r'Page curve: $S_{ent}(t) = \min(S_{BH}(t), S_{rad}(t))$', fontsize=10, ha='center', style='italic')
    save_fig('information-theory.png', fig)

def make_gif(frames_list, filename):
    imgs = []
    for f in frames_list:
        buf = io.BytesIO()
        f.savefig(buf, format='png', dpi=100)
        buf.seek(0)
        imgs.append(Image.open(buf))
    path = os.path.join(FIGURES_DIR, filename)
    imgs[0].save(path, save_all=True, append_images=imgs[1:], duration=100, loop=0)
    plt.close()
    print(f'Saved: {path}')

def create_modular_flow_animation():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_aspect('equal')
    frames = []
    t_values = np.linspace(0, 4*np.pi, 30)
    for i, t in enumerate(t_values):
        ax.clear()
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        n_elements = 8
        for j in range(n_elements):
            angle = 2 * np.pi * j / n_elements
            r = 0.8
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            new_angle = angle + t
            new_x = r * np.cos(new_angle)
            new_y = r * np.sin(new_angle)
            phase = np.cos(t + 2 * np.pi * j / n_elements)
            color = plt.cm.viridis((phase + 1) / 2)
            circle = Circle((new_x, new_y), 0.15, fill=True, facecolor=color, edgecolor='black', linewidth=1.5)
            ax.add_patch(circle)
            if j < n_elements - 1:
                next_angle = 2 * np.pi * (j + 1) / n_elements + t
                ax.plot([new_x, r * np.cos(next_angle)], [new_y, r * np.sin(next_angle)], 'k-', linewidth=1, alpha=0.3)
        central = Circle((0, 0), 0.3, fill=True, facecolor='#1a1a2e', edgecolor='white', linewidth=2)
        ax.add_patch(central)
        ax.text(0, 1.6, r'$\sigma_t(a) = e^{itK_X} a e^{-itK_X}$', fontsize=14, ha='center', fontweight='bold')
        ax.text(0, -1.6, f't = {t:.2f}', fontsize=12, ha='center')
        arrow = FancyArrowPatch((0, 0), (1.5 * np.cos(t), 1.5 * np.sin(t)), arrowstyle='->', mutation_scale=20, linewidth=2, color='red', alpha=0.7)
        ax.add_patch(arrow)
        ax.axis('off')
        frames.append(fig)
    make_gif(frames, 'modular-flow-animation.gif')

def create_type_transition_animation():
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    frames = []
    n_frames = 30
    for i in range(n_frames):
        for ax in axes:
            ax.clear()
            ax.set_xlim(-2, 2)
            ax.set_ylim(-2, 2)
            ax.set_aspect('equal')
            ax.axis('off')
        progress = i / n_frames
        ax1 = axes[0]
        ax1.set_title('Type III$_1$', fontsize=14, fontweight='bold')
        n_points = 50
        for j in range(n_points):
            x = (j / n_points - 0.5) * 3
            y = np.sin(x * 5 + progress * 2 * np.pi) * 0.3
            alpha = 0.5 + 0.5 * np.abs(np.sin(x * 3 + progress * np.pi))
            circle = Circle((x, y), 0.05, fill=True, facecolor='#2166AC', alpha=alpha)
            ax1.add_patch(circle)
        x_line = np.linspace(-1.5, 1.5, 100)
        y_line = 0.5 * np.sin(x_line * 4 + progress * 2 * np.pi)
        ax1.plot(x_line, y_line, 'r-', linewidth=2, alpha=0.7)
        ax1.text(0, -1.5, r'S = $\infty$', fontsize=11, ha='center')
        ax1.text(0, 1.5, 'Continuous spectrum', fontsize=10, ha='center')
        ax2 = axes[1]
        ax2.set_title('Type I', fontsize=14, fontweight='bold')
        n_levels = int(2 + progress * 8)
        for j in range(n_levels):
            y_level = (j - n_levels / 2) * 0.3
            alpha = min(1.0, progress * 2)
            rect = Rectangle((-0.4, y_level - 0.05), 0.8, 0.1, facecolor='#E6550D', alpha=alpha, edgecolor='white')
            ax2.add_patch(rect)
        arrow = FancyArrowPatch((-0.3, 0), (0.3, 0), arrowstyle='->', mutation_scale=30, linewidth=3, color='black', alpha=progress)
        ax2.add_patch(arrow)
        ax2.text(0, -1.5, r'S = $\log(N)$', fontsize=11, ha='center')
        ax2.text(0, 1.5, 'Discrete spectrum', fontsize=10, ha='center')
        fig.suptitle(f'Type III $\to$ Type I Transition: $\Delta_X$ continuous $\to$ discrete\nPage curve: $S_{{ent}}(t) = \min(S_{{BH}}(t), S_{{rad}}(t))', fontsize=14, fontweight='bold')
        frames.append(fig)
    make_gif(frames, 'type-transition-animation.gif')

def create_padic_convergence_animation():
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    frames = []
    n_frames = 30
    for i in range(n_frames):
        ax.clear()
        ax.set_xlim(-3, 3)
        ax.set_ylim(-3, 3)
        ax.set_aspect('equal')
        progress = i / n_frames
        p = 2
        n_branches = p ** int(progress * 4)
        angle_step = 2 * np.pi / max(n_branches, 1)
        for j in range(int(n_branches)):
            angle = j * angle_step
            r = 1.5 * (1 - progress * 0.3)
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            dist = p ** (-j / max(n_branches, 1))
            size = 0.1 + 0.15 * dist
            alpha = 0.3 + 0.7 * progress
            color_idx = int(dist * 255)
            circle = Circle((x, y), size, fill=True, facecolor=(color_idx / 255, 100 / 255, (255 - color_idx) / 255), edgecolor='white', linewidth=1)
            ax.add_patch(circle)
            ax.plot([0, x], [0, y], 'k-', linewidth=0.5, alpha=alpha * 0.5)
        central = Circle((0, 0), 0.2 + 0.1 * progress, fill=True, facecolor='#1a1a2e', edgecolor='white', linewidth=2)
        ax.add_patch(central)
        ax.text(0, 2.5, 'p-adic $\to$ Classical Convergence', fontsize=14, fontweight='bold', ha='center')
        ax.text(0, 2, r'$||\sigma_t^{{(p)}} - \sigma_t|| = O(p^{{-1}})$', fontsize=11, ha='center')
        ax.text(0, -2.5, f'p = {p}, convergence: {progress:.0%}', fontsize=11, ha='center')
        ax.text(0, -2, r'$\Delta_X^{{(p)}} \to \Delta_X$', fontsize=10, ha='center', style='italic')
        ax.axis('off')
        frames.append(fig)
    make_gif(frames, 'padic-convergence-animation.gif')

if __name__ == '__main__':
    print('=' * 60)
    print('DMS Visual Outputs Generator')
    print('=' * 60)
    print('\n[1/13] Generating modular spectrum...')
    plot_modular_spectrum()
    print('[2/13] Generating Virasoro algebra diagram...')
    plot_virasoro_algebra()
    print('[3/13] Generating black hole shadow diagram...')
    plot_black_hole_shadow()
    print('[4/13] Generating p-adic ultrametric tree...')
    plot_padic_ultrametric_tree()
    print('[5/13] Generating DMS architecture diagram...')
    plot_dms_architecture()
    print('[6/13] Generating band structure diagram...')
    plot_band_structure()
    print('[7/13] Generating gravitational wave spectrum...')
    plot_gravitational_wave_spectrum()
    print('[8/13] Generating neural network from DMS...')
    plot_neural_network_dms()
    print('[9/13] Generating information theory diagram...')
    plot_information_theory()
    print('[10/13] Generating modular flow animation...')
    create_modular_flow_animation()
    print('[11/13] Generating Type III to Type I transition animation...')
    create_type_transition_animation()
    print('[12/13] Generating p-adic convergence animation...')
    create_padic_convergence_animation()
    print('\n' + '=' * 60)
    print('All visual outputs generated successfully!')
    print('=' * 60)
