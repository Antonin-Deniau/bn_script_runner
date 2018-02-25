#!/usr/bin/env runner
from binaryninja import HighlightStandardColor

block = bv.get_basic_blocks_at(0x8670)[0]
block.highlight = HighlightStandardColor.BlueHighlightColor
print(bv)