# Chordal CMCF

Experimental augmentation of CMCF which attempts to preserve cortical thickness during flow.

`src/` contains supplemental scripts and prototype implementation of the upcoming ShapeMI paper.

- `decimate.py` invokes VTK quadric decimation as described.
- `register.py` invokes Deformetrica with extended varifold attachment to find chords.
- `flow.py` implements chordal CMCF on the registration output.

All parameter defaults are those values described in the paper. `__main__.py` invokes each step on two input files which
should be updated to point to the moving (white-matter surface) and fixed (pial surface) meshes respectively.

# Installation

This includes Deformetrica as a git subtree with modifications to include the mean-curvature-aware extended varifold
attachment. Installing this project via `uv` workspaces will automatically configure the correct installation.

## Build dependencies

This package relies on `scikit-sparse` and `pykeops`, so you will need to install the relevant dependencies. `pykeops`
*should* behave nicely on most systems. `scikit-sparse` will require installing a version of `libsuitesparse>=7.4.0`.

## Package installation

- Install uv
- Clone the project `git clone https://github.com/allemangd/chordal-cmcf`
- Install the project `cd chordal-cmcf; uv sync`
- Obtain surface meshes: "inner" white-matter surface "outer" pial surface.
- Update the paths in `src/__main__.py` to point to your surfaces.
- `python src/__main__.py`