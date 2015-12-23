[![Build Status](https://travis-ci.org/CodeJuan/python_convert_json2lua.svg?branch=master)](https://travis-ci.org/CodeJuan/python_convert_json2lua)



# usage
```sh
python go.py 'path of json' > aa.lua
```

# result

```lua
local msg = {}
local glossary = {}
local GlossDiv = {}
local GlossList = {}
local GlossEntry = {}
local GlossDef = {}
GlossDef.GlossSeeAlso = {"GML","XML"}
GlossDef.para = "A meta-markup language, used to create markup languages such as DocBook."
GlossEntry.GlossDef = GlossDef
GlossEntry.GlossSee = "markup"
GlossEntry.Acronym = "SGML"
GlossEntry.GlossTerm = "Standard Generalized Markup Language"
GlossEntry.Abbrev = "ISO 8879:1986"
GlossEntry.SortAs = "SGML"
GlossEntry.ID = "SGML"
GlossList.GlossEntry = GlossEntry
GlossDiv.GlossList = GlossList
GlossDiv.title = "S"
glossary.GlossDiv = GlossDiv
glossary.title = "example glossary"
msg.glossary = glossary

```
