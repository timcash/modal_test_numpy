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

app = modal.App(name="channel-numpy-test", image=loader_image)

@app.function(
    image=loader_image,
)
def test_cron(x: int) -> int:
    xr.open_dataset("/Users/tim/temp.grib2")
    return x

@app.local_entrypoint()
def main():
    # print(test_cron.local(1))
    print(test_cron.remote(1))
    total = 0
    print(total)
