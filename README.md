# pyTSon
pyTSon is a plugin for the TeamSpeak 3 client, it offers a python3 interface for the plugin sdk.
pyTSon has a minimum C/C++ part, so that the main plugin runs in embedded python.

Current used python version is Python 3.4.3.

Batteries included
==================
The python standard library is included, either built in the plugin or bundled in include/Lib (which is in sys.path by default).
pyTSon has PythonQt included, so that scripts can have UIs written in python, see pyTSon's own configdialog or the scripting console for examples.

Dependencies
============
pyTSon has multiple layers of dependencies listed below.

Generating Code
---------------
* Python3
* [pycparser](https://github.com/eliben/pycparser/)
* jinja2

Generating Documentation
------------------------
* Python3
* epydoc (which is only available for Python2, so we'll switch to another doctool in the future)

Building
--------
* Qt 5.5.1 (which is the version, the TeamSpeak 3 client is currently using)
* Python 3.4.3
* [PythonQt](https://github.com/pathmann/PythonQt)

Running
-------
* None!

How to build
============
* Adjust the python include and lib path in pyTSon.pro
* Download/Clone PythonQt from [here](https://github.com/pathmann/PythonQt) to includes/
```
qmake
(n)make
```
Done

How to develop a python plugin
==============================
Create a *.py file in \<TeamSpeak 3 client install\>/plugins/pyTSon/scripts with a subclass of ts3plugin.
Needed class attributes are requestAutoload, name, version, apiVersion, author, description, offersConfigure, commandKeyword, infoTitle, menuItems, hotkeys.
Otherwise pyTSon refuses to load the plugin. See ts3plugin.py or the documentation for a description of each attribute.

On load, pyTSon will create an instance of your class (call the constructor), after that callbacks are called (if available) as methods of the created instance, eg if you were poked, onClientPokeEvent(self, schid, fromClientID, pokerName, pokerUniqueIdentity, message, ffIgnored) will be called.
On unload, pyTSon will call stop and delete the instance of your class.

TeamSpeak 3's library functions are available with the ts3 module (eg err, myid = ts3.getClientID(schid)).
Constants are available in the ts3defines module (see ts3defines.py in include/ directory).

Platform Notes
==============
Linux
-----
You might need to bypass your TeamSpeak 3's runscript with `LD_PRELOAD=./plugins/libpyTSon.so`
