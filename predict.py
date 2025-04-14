from cog import BasePredictor, BaseModel, Path, Input
import subprocess
import tempfile

class ModelOutput(BaseModel):
    output_dir: Path

class Predictor(BasePredictor):
    def setup(self):
        pass
    
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

        blender_path = "thirdparty/blender/blender"
        command = [
            blender_path,
            f"@{arg_file_path}",
        ]

        subprocess.run(command, check=True)
        return ModelOutput(output_dir=out_dir)
