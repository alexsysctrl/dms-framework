# Mission: Neuroscience Visualization — Agent 73

## Context
Agent 72 just completed the neuroscience paper (explorations/72-neuroscience/neuroscience.md) with 75 equations (E1936-E2010), 20 patterns (P771-P790), and 38 theorems (72.1-72.38). The paper contains 7 ASCII diagrams that need to be converted to proper visualizations.

## Goal
Create publication-quality visualizations for the neuroscience expansion. This includes:
1. Converting ASCII diagrams to proper PNG/SVG figures
2. Generating Manim animations for neural dynamics
3. Creating Matplotlib plots for eigenvalue distributions
4. Producing TikZ diagrams for commutative diagrams and spectral triples

## What to Produce

### 1. PNG Figures (figures/neuroscience/)
Create at least 8 PNG figures:

**Figure 1: eigenvalue-spectrum.png**
- Show the Delta_X eigenvalue spectrum with EEG band labels
- Delta (0.5-4Hz), Theta (4-8Hz), Alpha (8-13Hz), Beta (13-30Hz), Gamma (30-100Hz)
- Use matplotlib with SciencePlots style
- Reference: neuroscience.md Section 2, Diagram 1

**Figure 2: action-potential.png**
- Hodgkin-Huxley action potential waveform
- Label resting potential, threshold, peak, recovery
- Overlay ion channel conductances (g_Na, g_K, g_L)
- Reference: neuroscience.md Section 3, Diagram 3

**Figure 3: modular-flow.png**
- Phase evolution of eigenmodes under sigma_t = exp(i*t*K_X)
- Show phase alignment at t = T (synchronization)
- Reference: neuroscience.md Section 2, Diagram 2

**Figure 4: synaptic-plasticity.png**
- LTP eigenvalue increase vs LTD eigenvalue decrease
- Show STDP timing window (pre-post vs post-pre)
- Reference: neuroscience.md Section 4, Diagram 4

**Figure 5: brain-network.png**
- Small-world network visualization
- Show high clustering, short path length
- Reference: neuroscience.md Section 5, Diagram 5

**Figure 6: consciousness-transition.png**
- Type III -> Type II -> Type I transition
- Show coherence threshold at lambda_critical
- Reference: neuroscience.md Section 7, Diagram 6

**Figure 7: sensory-processing.png**
- Visual cortex frequency tuning + auditory spectral decomposition
- Show eigenvalue gap detection
- Reference: neuroscience.md Section 6, Diagram 7

**Figure 8: neural-oscillation-spectra.png**
- Power spectral density of neural oscillations
- Show EEG frequency bands with labeled regions
- Reference: neuroscience.md Equation E1943

### 2. Manim Animations (animations/neuroscience/)
Create at least 3 MP4 animations:

**Animation 1: eigenvalue-evolution.mp4**
- Show eigenvalues lambda_n evolving under modular flow
- Phase alignment leading to synchronization
- Duration: ~10 seconds

**Animation 2: action-potential-propagation.mp4**
- Show action potential propagating along axon
- Ion channels opening/closing
- Duration: ~15 seconds

**Animation 3: neural-oscillation.mp4**
- Show EEG frequency bands (delta, theta, alpha, beta, gamma)
- Modular flow sigma_t = exp(i*t*K_X)
- Duration: ~10 seconds

### 3. TikZ Diagrams (tikz/neuroscience/)
Create at least 3 TikZ diagrams:

**TikZ 1: spectral-triple-neural.tex**
- Commutative diagram for neural spectral triple (A_neural, H_neural, D_neural)
- Show Delta_X = exp(D^2) acting on H_neural
- Reference: neuroscience.md Theorem 72.1

**TikZ 2: ion-channel-eigenvalue.tex**
- Diagram showing ion channel conductances mapped to eigenvalues
- g_Na, g_K, g_L -> lambda_Na, lambda_K, lambda_L
- Reference: neuroscience.md Theorem 72.6

**TikZ 3: consciousness-transition.tex**
- Type III -> Type II -> Type I transition diagram
- Show lambda_critical threshold
- Reference: neuroscience.md Theorem 72.34

## Output Structure
```
explorations/73-neuroscience-visuals/
├── mission.md (this file)
├── neuroscience-visuals.md (main output document)
├── agent-handoff.md
├── session-log.md
├── figures/
│   └── neuroscience/
│       ├── eigenvalue-spectrum.png
│       ├── action-potential.png
│       ├── modular-flow.png
│       ├── synaptic-plasticity.png
│       ├── brain-network.png
│       ├── consciousness-transition.png
│       ├── sensory-processing.png
│       └── neural-oscillation-spectra.png
├── animations/
│   └── neuroscience/
│       ├── eigenvalue-evolution.mp4
│       ├── action-potential-propagation.mp4
│       └── neural-oscillation.mp4
└── tikz/
    └── neuroscience/
        ├── spectral-triple-neural.tex
        ├── ion-channel-eigenvalue.tex
        └── consciousness-transition.tex
```

## Main Document Contents
Write to: explorations/73-neuroscience-visuals/neuroscience-visuals.md

Include:
1. Introduction — purpose of visualization expansion
2. Figure descriptions — what each figure shows, which equation/theorem it illustrates
3. Animation descriptions — what each animation shows, timing, key frames
4. TikZ descriptions — what each diagram shows, LaTeX code snippets
5. Reference mapping — explicit mapping from each visualization to neuroscience.md sections
6. Quality notes — rendering details, resolution, color schemes

## Quality Requirements
- All PNG figures: at least 300 DPI, 800x600 minimum
- All MP4 animations: 720p minimum, clear labels
- All TikZ diagrams: compilable LaTeX, proper math typography
- All visualizations must reference specific equations/theorems from neuroscience.md
- Color scheme: consistent across all figures (use matplotlib default or SciencePlots)
- All figures must be self-contained (no external dependencies)

## Statistics to Achieve
- At least 8 PNG figures
- At least 3 MP4 animations
- At least 3 TikZ diagrams
- Explicit reference to all 7 ASCII diagrams from neuroscience.md
- Reference to all 9 sections of neuroscience.md

## Tools Available
- Python with matplotlib, numpy, scipy
- Manim Community Edition (pip install manim)
- LaTeX/TikZ (pdflatex available)
- All tools are Python-based and can be run from command line

## Important Notes
- The neuroscience paper is at: explorations/72-neuroscience/neuroscience.md
- Read it first to understand the ASCII diagrams and equations
- Create output directories before writing files
- Write PNG figures using matplotlib with SciencePlots style
- Write Manim animations as Python files, then render with manim command
- Write TikZ diagrams as .tex files that compile to PDF/SVG
- After writing, also update:
  - explorations/73-neuroscience-visuals/agent-handoff.md
  - explorations/73-neuroscience-visuals/session-log.md
  - explorations/72-neuroscience/agent-handoff.md (add next steps for Agent 74)

IMPORTANT: Make this a substantial, detailed document. Aim for 5000+ words. Include full LaTeX code for TikZ diagrams. Include full Python code for Manim animations. Include detailed descriptions for each figure.
