import modal
import xarray as xr

loader_image = (
    modal.Image.debian_slim(python_version="3.11")
    .micromamba(python_version="3.11")
    .micromamba_install(
        [
            "cfgrib",
            "pygrib",
            "xarray",
        ],
        channels=["conda-forge"],
    )
    .pip_install([])
)

app = modal.App(name="numpy-test", image=loader_image)

@app.function(
    image=loader_image,
)
def test_xarray():
    xr.open_dataset("./temp.grib2")

@app.local_entrypoint()
def main():
    test_xarray.remote(1)
