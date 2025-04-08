# from https://easings.net/#easeInSine

import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()


def easeInSine(x: int) -> float:
    """
    Ease in with sine wave.

    Parameters
    ----------
    x : int
        Represents the absolute progress of the animation in the bounds of [0, 1].

    Returns
    -------
    float
        Resulting calculation.
    """
    return 1 - math.cos((x * math.pi) / 2)


if __name__ == "__main__":
    X = np.linspace(start=0, stop=1, num=1000)
    y = [easeInSine(x) for x in X]

    plt.plot(X, y)
    plt.show()
