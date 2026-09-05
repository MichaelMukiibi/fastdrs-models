# fastDRS Models

Model artifacts for the [fastDRS](https://github.com/MichaelMukiibi/diabetic-retinopathy-screening) diabetic retinopathy screening toolkit.

This repository contains metadata and release artifacts for trained fastDRS models.

## Available artifacts

Each registered model may have:

- PyTorch `.pth` weights
- LiteRT `.tflite` model

The model binaries are distributed as GitHub Release assets rather than committed directly to Git.

## Model architectures

Currently supported:

- ResNet18
- ResNet50
- DenseNet121
- ConvNeXt Tiny
- Swin Transformer Tiny
- MobileNetV2

## Downloading models

Models are normally downloaded automatically through `fastdrs`:

```python
from fastdrs import Predictor

predictor = Predictor.from_pretrained("mobilenet_v2")
```

For LiteRT:

```python
from fastdrs.inference import LiteRTPredictor

predictor = LiteRTPredictor.from_pretrained("mobilenet_v2")

```

Downloaded models are cached locally by `fastdrs`