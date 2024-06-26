"""Template class for a NQRduck module controller."""

from nqrduck.module.module_controller import ModuleController

# If the module is called "duck" the class would be called "DuckController"


class ModuleController(ModuleController):
    """Template class for a NQRduck module controller."""

    def __init__(self, module):
        """Initialize the controller."""
        super().__init__(module)

    def on_loading(self):
        """This method is called when the module is loaded."""
        pass
