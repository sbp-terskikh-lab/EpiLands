from basicpy import BaSiC
from ._ezsave import ezsave
from ._ezload import ezload


def save_illumination_correction_model(correction_model: BaSiC, file: str) -> None:
    ezsave(
        {"model": correction_model, "dummy": []},
        file,
    )


def load_illumination_correction_model(file: str) -> BaSiC:
    return ezload(file)["model"]
