from cog import BasePredictor, BaseModel
import subprocess
import tempfile

class ModelInput(BaseModel):
    mesh_path: str
    blender_path: str = "blender-4.0.0-linux-x64/blender"
    types: str = "glb"

class ModelOutput(BaseModel):
    output_dir: str

class Predictor(BasePredictor):
    def setup(self):
        pass

    def predict(self, input: ModelInput) -> ModelOutput:
        """
        Render 16 views and output them to a temporary folder.

        The 16 view images will be saved in a temporary directory,
        which is returned to Cog as the output.
        """
        out_dir = tempfile.mkdtemp(prefix="cog_output_")
        
        command = [
            input.blender_path,
            "-b",
            "-P", "thirdparty/SAMPart3D/tools/blender_render_16views.py",
            input.mesh_path,
            input.types,
            out_dir,
        ]
        
        subprocess.run(command, check=True)
        return ModelOutput(output_dir=out_dir)
