import logging
from pathlib import Path

from decimate import decimate
from flow import flow_3d

logging.basicConfig(level=logging.INFO)

data_root = Path("data/")
aux_outputs = data_root.joinpath("outputs")
aux_outputs.mkdir(exist_ok=True)

model = data_root.joinpath('achilles.vtk')
print(f"pipeline input:\n  {model}")

model = decimate(model, target_reduction=0.9)
print(f"decimation outputs:\n  {model}")

model = flow_3d(model)
print(f"chordal flow outputs:\n  {model}")
