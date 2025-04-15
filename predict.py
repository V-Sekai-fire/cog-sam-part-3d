from cog import BasePredictor, BaseModel, Path, Input
import subprocess
import tempfile
import os

BLENDER_PATH = "thirdparty/blender/blender"
BLENDER_DOWNLOAD_CMD = (
    "mkdir -p thirdparty/blender && "
    "cd thirdparty/blender && "
    "wget -qO- https://download.blender.org/release/Blender4.2/blender-4.2.8-linux-x64.tar.xz | "
    "tar -xJ --strip-components=1"
)

class ModelOutput(BaseModel):
    output_dir: Path

class Predictor(BasePredictor):
    def setup(self):
        if not os.path.exists(BLENDER_PATH):
            subprocess.run(BLENDER_DOWNLOAD_CMD, shell=True, check=True)
    
    def predict(self, mesh_path: Path = Input(description="The 3d object to segment."), types: str = "glb") -> ModelOutput:
        """
        Render 16 views and output them to a temporary folder.

        The 16 view images will be saved in a temporary directory,
        which is returned to Cog as the output.
        """
        out_dir = Path(tempfile.mkdtemp())

        with tempfile.NamedTemporaryFile(mode="w", delete=False) as arg_file:
            arg_file.write(f"-b\n-P\nblender_render_16views.py\n{mesh_path}\n{types}\n{out_dir}\n")
            arg_file_path = arg_file.name

        command = [
            BLENDER_PATH,
            f"@{arg_file_path}",
        ]

        subprocess.run(command, check=True)
        return ModelOutput(output_dir=out_dir)
