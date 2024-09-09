import xarray as xr
import os

def read_generic_grib2(
    file_path: os.PathLike, type_of_level: str, stepType: str
) -> xr.Dataset:
    return xr.open_dataset(
        file_path,
        engine="cfgrib",
        filter_by_keys={"typeOfLevel": type_of_level, "stepType": stepType},
    )



