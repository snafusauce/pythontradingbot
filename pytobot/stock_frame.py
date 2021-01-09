import numpy as np
import pandas as pd

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

from pandas.core.groupby import DataFrameGroupBy
from pandas.core.window import RollingGroupby

class StockFrame():
    def __init__(self) -> None:
        super().__init__()