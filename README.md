# cuda-jupyter

Jupyter notebook images with CUDA9.0 and cuDNN7.

**NOTE**
This image is intended to use in development or personal use.
Only single user use is supported for now.

## Execute

```bash
docker run -p=8888:8888 saint1991/cuda-jupyter
```

The jupyter notebook is started on port 8888 as default.

## Persist data

To persist you should attach external persistent volume and 
set the environment variable `JUPYTER_NOTEBOOK_DIR` to point a directory on the attached volume.

```bash
docker run -p=8888:8888 -v=$ATTACHED_DIR:/home/jupyter/data -e=JUPYTER_NOTEBOOK_DIR=/home/jupyter/data saint1991/cuda-jupyter
```

## Password

As default `jupyter` is used for a login password but you can configure it
via the environment variable `JUPYTER_PASSWORD`.

See [here](http://jupyter-notebook.readthedocs.io/en/stable/public_server.html#preparing-a-hashed-password) for more details.

## Install packages on notebook

This image runs a container as the user `jupyter` but **NOT** `root` for security reasons.
So you should install packages as follows on a notebook:

```jupyter
!pip3 install --user $some_package
```

The directory of user sites seems not to be included in the PATH as default.
Following script somehow corrects it.

```jupyter
import site
site.addsitedir(site.USER_SITE)
```

## License

This image is Open Source and available under the MIT License.
