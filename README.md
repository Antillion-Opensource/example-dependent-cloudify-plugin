# Dependent Dummy Plugin

This plugin depends on the dummy plugin for some of it's functionality.

This is exhibited in 3 ways:

1. The plugin is declared (in the `setup.py`) as depending on the dummy plugin
2. The types file has a type that derives from the dummy type file
3. The plugin code that will be executed uses the dummy code

A potential 4th way is available, but to reduce initial complexity is not
included:

4. The types file directly includes the dummy type file

Because Cloudify validates the blueprint after collating all type files,
as long as the blueprint that includes this plugin _also_ includes the
dummy plugin then the dependency will not fail.
