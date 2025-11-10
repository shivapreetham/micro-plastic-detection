from typing import Optional
import segmentation_models_pytorch as smp


def build_unet(
    encoder_name: str = "resnet34",
    encoder_weights: Optional[str] = "imagenet",
    classes: int = 1,
    activation: Optional[str] = None,
):
    return smp.Unet(
        encoder_name=encoder_name,
        encoder_weights=encoder_weights,
        in_channels=3,
        classes=classes,
        activation=activation,
    )

