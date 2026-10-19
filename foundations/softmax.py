import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        if z.ndim == 1:
            axis = 0
        else:
            axis = 1
        
        max  = np.max(z, axis, keepdims=True)
        exp = np.exp(z - max)

        sum = np.sum(exp, axis, keepdims=True)
        
        return np.round(exp / sum, 4)
