

import trimesh
from pathlib import Path

input_file = Path("642599278f1bfd41942ae558_medium.glb")
output_file = input_file.with_suffix(".stl")

scene = trimesh.load(input_file, force="scene")

# 合并场景中的几何体，保留节点变换
mesh = scene.to_geometry()

mesh.export(output_file)

print("转换成功:", output_file)
print("顶点数:", len(mesh.vertices))
print("面数:", len(mesh.faces))
