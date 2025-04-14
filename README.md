# SAMPart3D: Segment Any Part in 3D Objects

## Overview

SAMPart3D is a project designed to segment any part in 3D objects. It is inspired by several repositories, including PointTransformerV3, Pointcept, FeatUp, dinov2, segment-anything, and PartSLIP2. Many thanks to the authors for sharing their codes.

## 🔧 Setup

Please refer to [INSTALL.md](INSTALL.md) for installation instructions.

## 🚀 Running SAMPart3D

### 1. Train

Change the rendering `data_root`, `mesh_root`, and `backbone_weight_path` in `configs/sampart3d/sampart3d-trainmlp-render16views.py`.

Run the training script:

```bash
sh scripts/train.sh -g ${NUM_GPU} -d ${DATASET_NAME} -c ${CONFIG_NAME} -n ${EXP_NAME} -o ${OBJECT_UID}
```

### 2. Test

Run the evaluation script:

```bash
sh scripts/eval.sh -g ${NUM_GPU} -d ${DATASET_NAME} -n ${EXP_NAME} -w ${WEIGHT_NAME}
```

### 3. Highlight 3D Segments

Set `render_dir`, `mesh_path`, `results_dir`, and `save_dir` in `tools/highlight_parts.py` and run:

```bash
python tools/highlight_parts.py
```

## 📚 Dataset: PartObjaverse-Tiny

Please refer to [PartObjaverse-Tiny.md](PartObjaverse-Tiny.md) for dataset details.

## Acknowledgement

If you find SAMPart3D useful in your project, please cite our work:

```bibtex
@article{yang2024sampart3d,
  title={SAMPart3D: Segment Any Part in 3D Objects},
  author={Yang, Yunhan and Huang, Yukun and Guo, Yuan-Chen and Lu, Liangjun and Wu, Xiaoyang and Lam, Edmund Y and Cao, Yan-Pei and Liu, Xihui},
  journal={arXiv preprint arXiv:2411.07184},
  year={2024}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/V-Sekai-fire/cog-sam-part-3d/blob/main/LICENSE) file for details.
