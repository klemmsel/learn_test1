import numpy as np
import pandas as pd
from numpy import log
import os


def SELpercentile(SEL, percentile=5):    
    """ SELpercentile for x% highest."""
    fff = np.percentile(SEL, 100-percentile)

    return fff
    