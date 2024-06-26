"""Template View for a NQRduck module."""

from nqrduck.module.module_view import ModuleView

# This is the widget that is loaded into the module view.
# It is generated from the .ui file in the same directory using the pyuic6 command.
from .widget import Ui_Form

from PyQt6.QtWidgets import QWidget

# If the module is called "duck" the class would be called "DuckView"


class ModuleView(ModuleView):
    """Template class for a NQRduck module view."""

    def __init__(self, module):
        """Initialize the view. This is usually quite similar for all modules."""
        super().__init__(module)

        widget = QWidget()
        self._ui_form = Ui_Form()
        self._ui_form.setupUi(self)
        self.widget = widget
