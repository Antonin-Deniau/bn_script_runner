# BN script runner

This plugin allow a student instance of binaryninja to use the API to a certain extend.
It allow a binaryninja instance to listen to localhost:5335, waiting for scripts, then executing it, and sending back the result to the handler (The bnrunner script).
All script executed with bnrunner will have a global variable named *bv*, the BinaryView instance of the opened binary in binaryninja.

## Getting Started

- To use it you must load a binary with binaryninja.
- To start the script runner your must go to *Tools->[script_runner] start server*
- You can now execute scripts with it.

The scripts must look like this:

```python
#!/usr/bin/env bnrunner
from binaryninja import HighlightStandardColor

block = bv.get_basic_blocks_at(0x8670)[0]
block.highlight = HighlightStandardColor.BlueHighlightColor
print(bv)
```

Or on Windows:

```python
import bnrunner
from binaryninja import HighlightStandardColor

def main(): 
    block = bv.get_basic_blocks_at(0x8670)[0]
    block.highlight = HighlightStandardColor.BlueHighlightColor
    print(bv)

bnrunner.run_from_path() if __name__ == '__main__' else main()
```

You can also launch script with the bnrunner executable in both platform `bnrunner script.py`


### Installing

- Copy the script_runner directory in your binaryninja plugin folder.
- Install the [bnrunner](https://github.com/Antonin-Deniau/bnrunner) python package `pip install bnrunner`.
- Now all the python scripts that you will execute with bnrunner will be sent to the binaryninja instance.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
