## Jupyter/IPython Notebook hooks

Add hooks to Jupyter/IPython Notebook so that nbconvert converts the Notebook to a .py and HTML file after saving. This allows investigating the .py file for code changes while also having the full results in Notebook and HTML format.


Add the code below to the Notebook config located somewhere like:
* ~/.ipython//ipython_notebook_config.py (IPython)
* ~/.jupyter/jupyter_notebook_config.py (Jupyter)

[Source](http://svds.com/post/jupyter-notebook-best-practices-data-science), [original](https://github.com/ipython/ipython/issues/8009).

Note: nbconvert has to be installed.

```python
c = get_config()
### If you want to auto-save .html and .py versions of your notebook:
# modified from: https://github.com/ipython/ipython/issues/8009
import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    check_call(['ipython', 'nbconvert', '--to', 'script', fname], cwd=d)
    check_call(['ipython', 'nbconvert', '--to', 'html', fname], cwd=d)

c.FileContentsManager.post_save_hook = post_save
```

## Bash aliases

Grep only in .py and .ipynb files, ignoring IPython Notebook checkpoints.
```bash
alias ipygrep='grep --include=\*.py --include=\*.ipynb --exclude-dir=\.ipynb_checkpoints'
```
