import os

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.notebook_dir = os.getenv('JUPYTER_NOTEBOOK_DIR', '/home/jupyter/data')
c.NotebookApp.password = os.getenv('JUPYTER_PASSWORD', 'sha1:9348540f8294:d9efbf1b40ac0f3977ea4121aa085437641a9983')
c.NotebookApp.open_browser = False
c.NotebookApp.enable_mathjax = True
