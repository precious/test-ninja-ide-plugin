from ninja_ide.core import plugin


class HelloWorld(plugin.Plugin):
    def initialize(self):
        print "The plugin is loading..."
        print "plugin information: %s" % self.metadata
        print "service locator: %s" % self.locator

    def finish(self):
        print "The plugin is shutting down because the user has closed NINJA-IDE"


    def get_preferences_widget(self):
        pass