# Overview

In this project we will show how to organize a package namespace and 
deploy it.

The app-project have the following architecture (cmd : `tree /f`)

```md
app-project
│   main.py
│   REAMDME.md
│   setup.py
└───app
    │   utils.py
    │   __init__.py
    ├───data
    │       data.json
    ├───model
    │       model.py
    │       utils.py
    │       __init__.py
    │       __main__.py
    └───stream
            __init__.py
            __main__.py
```
---
## 1. Creating a package
When creating a package, two files show a particular importance:
- `__init__.py`: help managing the namespace
- `__main__.py`: run automatically as a script when a call to a package
is made

  
### a. Organize package namespace
The package namespace can be managed through the `__init__.py`. When 
an import statement is made, python execute automatically every 
`__init__.py` of every package. So it is a good place to define import rules.


### relative import
It is more robust to use relative imports through the package when refactoring is
needed. Indeed, fully qualified path need to be rename when a module or package name
is changed.

```py
# model.py
from .utils import utility_function
from ..utils import time_a_function
```
### controlling the namespace
A good way to control the namespace is to import all required symbols within the `__init__.py` of each package.
When doing so, symbols are referenced under the package name which greatly simplify
the calling. Instead of importing `package.subpackage.utils.my_function` now,
`package.my_function` become enough. It creates a simpler interface for the user.

To do so, use `ìmport *` together with `__all__`.  The `__all__` variable dictates 
which symbols are retrieved from `ìmport *`. If no `__all__` is defined then all symbols
from the module are retrieved.

```py
# model.__init__.py
from .model import * 
from .utils import *

__all__ = (
        model.__all__ + 
        utils.__all__
)
```

### b. Running a package submodule as a main script
Because of relative import running `model.py` will raise an import error. To do so, 
we shall run the command `python -m app.model.model.py` which specifies the 
python interpreter to run the module as a main script. 

If a `__main__.py` is defined in model it is also possible to run the command 
`python -m app.model`.


## 2. Deploying a package

### create distribution file
### install distribution file
