import os

from easytorch.utils.registry import scan_modules

from .registry import SCALER_REGISTRY
from .dataset import TimeSeriesForecastingDataset

__all__ = ["SCALER_REGISTRY", "TimeSeriesForecastingDataset"]

# scan_modules("E:/MS/2021/BasicTS/basicts/data/", __file__, ["__init__.py", "registry.py"])
# scan_modules("E:/MS/2021/BasicTS/basicts/data", __file__, [ "registry.py"])
# print(os.getcwd())
scan_modules(os.getcwd(), __file__, ["__init__.py", "registry.py"])
