from ._version import version_info, __version__

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'jupyter-rs-vtk',
        'require': 'jupyter-rs-vtk/extension'
    }]
