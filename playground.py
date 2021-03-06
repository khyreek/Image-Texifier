from typing import Annotated, Any, Generator, List, Literal, Tuple, Union
import cv2 as cv # type: ignore
import numpy as np
from infofuncs import *

ELEPHANT: np.ndarray = cv.imread('random.jpg')
TOLLFACE: np.ndarray = cv.imread('220px-Trollface_non-free.png')

# print(
#     ''.join(tuple(texify(ELEPHANT, text_width_min=800, spec_height=22, spec_width=8)))
# )
print(
    ''.join(tuple(texify(TOLLFACE, text_width_min=800, spec_height=22, spec_width=8)))
)
