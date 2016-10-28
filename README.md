python-mot-epg
==============

Plugin to the `python-mot` library to handle DAB EPG binary encoding as per ETSI TS 102 371.

# Dependencies

* `python-mot`

# Utilities

# Examples

Creating an MOT object and adding parameters

```python
from mot import MotObject

# create PI file MOT object
object = MotObject("e1_c586_c234_20160902_PI.xml", data, EpgContentType.PROGRAMME_INFORMATION)

# add additional parameter - scope start, end, ID 
object.add_parameter(ScopeId(0xe1, 0xc586, 0xc234))
object.add_parameter(ScopeStart(datetime(2016, 9, 02, 00, 00, 00)))
object.add_parameter(ScopeEnd(datetime(2016, 9, 03, 01, 00, 00)))
```
