# py-wtf
A static analyzer of Python which forces you to write comments, and write them in a well-mannered way.

**wtf** is short for **what the function** or **why that function**.  

Since most of the time, when you read some code snippet of your own without comments, you might have the question, "what the function was used for? Why did I write that function? What the hell was I thinking about at that time?" And my product is to help you with this problem.

---

## Requirements
Python >= 3.5

---

## Installation
Install `py-wtf`:

```bash
sudo pip3 install py-wtf
```

---

## Developing
Install `py-wtf` for development:

```bash
sudo python3 setup.py develop
```

---

## Usage
Before you actually use it, there are two modes in this tool that you need to know:
- normal mode
- strict mode

In `normal mode`, both comments (#-style) and docstrings will be considered as "comments". It won't complain missing of comments if you'd at least written a `#` mark for your functions.

However, in `strict mode`, it only considers docstrings as "comments". So, if you only have comments (#-style) in your script, it will report warnings.

> The default mode is `normal mode`.
---

Use it as a command in Terminal:
```bash
# you can process multiple files at the same time
wtf NAME_OF_FILE0.py NAME_OF_FILE1.py NAME_OF_FILEn.py

# you can process a folder of files (currently only one folder is supported)
wtf NAME_OF_FOLDER

# you can switch to strict mode by passing -s argument
wtf NAME_OF_FILE.py -s
```
or  

use it as a normal Python library:
```python
import pywtf
```

> It only complains the missing of class's docstrings, class member functions' comments and top-level functions' comments. It **DOESN'T** care about docstrings or comments for **source files**.
