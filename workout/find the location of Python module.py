Write a Python program to find the location of Python module sources.

Ans::

import sys
print("\nList of directories in sys module:")
print(sys.path)
print("\nList of directories in os module:")
import os
print(os.path)

O/P:

List of directories in sys module:
['/srv/conda/envs/notebook/lib/python36.zip', '/srv/conda/envs/notebook/lib/python3.6', '/srv/conda/envs/notebook/lib/python3.6/lib-dynload', '', '/srv/conda/envs/notebook/lib/python3.6/site-packages', '/srv/conda/envs/notebook/lib/python3.6/site-packages/IPython/extensions', '/home/jovyan/.ipython']

List of directories in os module:
<module 'posixpath' from '/srv/conda/envs/notebook/lib/python3.6/posixpath.py'>
