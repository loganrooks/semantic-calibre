import PyQt6.QtCore
import PyQt6.QtGui
import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['QAbstractButton', 'QAbstractGraphicsShapeItem', 'QAbstractItemDelegate', 'QAbstractItemView', 'QAbstractScrollArea', 'QAbstractSlider', 'QAbstractSpinBox', 'QApplication', 'QBoxLayout', 'QButtonGroup', 'QCalendarWidget', 'QCheckBox', 'QColorDialog', 'QColumnView', 'QComboBox', 'QCommandLinkButton', 'QCommonStyle', 'QCompleter', 'QDataWidgetMapper', 'QDateEdit', 'QDateTimeEdit', 'QDial', 'QDialog', 'QDialogButtonBox', 'QDockWidget', 'QDoubleSpinBox', 'QErrorMessage', 'QFileDialog', 'QFileIconProvider', 'QFocusFrame', 'QFontComboBox', 'QFontDialog', 'QFormLayout', 'QFrame', 'QGesture', 'QGestureEvent', 'QGestureRecognizer', 'QGraphicsAnchor', 'QGraphicsAnchorLayout', 'QGraphicsBlurEffect', 'QGraphicsColorizeEffect', 'QGraphicsDropShadowEffect', 'QGraphicsEffect', 'QGraphicsEllipseItem', 'QGraphicsGridLayout', 'QGraphicsItem', 'QGraphicsItemGroup', 'QGraphicsLayout', 'QGraphicsLayoutItem', 'QGraphicsLineItem', 'QGraphicsLinearLayout', 'QGraphicsObject', 'QGraphicsOpacityEffect', 'QGraphicsPathItem', 'QGraphicsPixmapItem', 'QGraphicsPolygonItem', 'QGraphicsProxyWidget', 'QGraphicsRectItem', 'QGraphicsRotation', 'QGraphicsScale', 'QGraphicsScene', 'QGraphicsSceneContextMenuEvent', 'QGraphicsSceneDragDropEvent', 'QGraphicsSceneEvent', 'QGraphicsSceneHelpEvent', 'QGraphicsSceneHoverEvent', 'QGraphicsSceneMouseEvent', 'QGraphicsSceneMoveEvent', 'QGraphicsSceneResizeEvent', 'QGraphicsSceneWheelEvent', 'QGraphicsSimpleTextItem', 'QGraphicsTextItem', 'QGraphicsTransform', 'QGraphicsView', 'QGraphicsWidget', 'QGridLayout', 'QGroupBox', 'QHBoxLayout', 'QHeaderView', 'QInputDialog', 'QItemDelegate', 'QItemEditorCreatorBase', 'QItemEditorFactory', 'QKeySequenceEdit', 'QLCDNumber', 'QLabel', 'QLayout', 'QLayoutItem', 'QLineEdit', 'QListView', 'QListWidget', 'QListWidgetItem', 'QMainWindow', 'QMdiArea', 'QMdiSubWindow', 'QMenu', 'QMenuBar', 'QMessageBox', 'QPanGesture', 'QPinchGesture', 'QPlainTextDocumentLayout', 'QPlainTextEdit', 'QProgressBar', 'QProgressDialog', 'QProxyStyle', 'QPushButton', 'QRadioButton', 'QRubberBand', 'QScrollArea', 'QScrollBar', 'QScroller', 'QScrollerProperties', 'QSizeGrip', 'QSizePolicy', 'QSlider', 'QSpacerItem', 'QSpinBox', 'QSplashScreen', 'QSplitter', 'QSplitterHandle', 'QStackedLayout', 'QStackedWidget', 'QStatusBar', 'QStyle', 'QStyleFactory', 'QStyleHintReturn', 'QStyleHintReturnMask', 'QStyleHintReturnVariant', 'QStyleOption', 'QStyleOptionButton', 'QStyleOptionComboBox', 'QStyleOptionComplex', 'QStyleOptionDockWidget', 'QStyleOptionFocusRect', 'QStyleOptionFrame', 'QStyleOptionGraphicsItem', 'QStyleOptionGroupBox', 'QStyleOptionHeader', 'QStyleOptionHeaderV2', 'QStyleOptionMenuItem', 'QStyleOptionProgressBar', 'QStyleOptionRubberBand', 'QStyleOptionSizeGrip', 'QStyleOptionSlider', 'QStyleOptionSpinBox', 'QStyleOptionTab', 'QStyleOptionTabBarBase', 'QStyleOptionTabWidgetFrame', 'QStyleOptionTitleBar', 'QStyleOptionToolBar', 'QStyleOptionToolBox', 'QStyleOptionToolButton', 'QStyleOptionViewItem', 'QStylePainter', 'QStyledItemDelegate', 'QSwipeGesture', 'QSystemTrayIcon', 'QTabBar', 'QTabWidget', 'QTableView', 'QTableWidget', 'QTableWidgetItem', 'QTableWidgetSelectionRange', 'QTapAndHoldGesture', 'QTapGesture', 'QTextBrowser', 'QTextEdit', 'QTimeEdit', 'QToolBar', 'QToolBox', 'QToolButton', 'QToolTip', 'QTreeView', 'QTreeWidget', 'QTreeWidgetItem', 'QTreeWidgetItemIterator', 'QUndoView', 'QVBoxLayout', 'QWIDGETSIZE_MAX', 'QWhatsThis', 'QWidget', 'QWidgetAction', 'QWidgetItem', 'QWizard', 'QWizardPage', 'qDrawBorderPixmap', 'qDrawPlainRect', 'qDrawPlainRoundedRect', 'qDrawShadeLine', 'qDrawShadePanel', 'qDrawShadeRect', 'qDrawWinButton', 'qDrawWinPanel']
class QAbstractButton(QWidget):
    @staticmethod
    def animateClick(*args, **kwargs):
        ...
    @staticmethod
    def autoExclusive(*args, **kwargs):
        ...
    @staticmethod
    def autoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def autoRepeatDelay(*args, **kwargs):
        ...
    @staticmethod
    def autoRepeatInterval(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def checkStateSet(*args, **kwargs):
        ...
    @staticmethod
    def click(*args, **kwargs):
        ...
    @staticmethod
    def clicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def group(*args, **kwargs):
        ...
    @staticmethod
    def hitButton(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def iconSize(*args, **kwargs):
        ...
    @staticmethod
    def isCheckable(*args, **kwargs):
        ...
    @staticmethod
    def isChecked(*args, **kwargs):
        ...
    @staticmethod
    def isDown(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def nextCheckState(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def pressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def released(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setAutoExclusive(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRepeatDelay(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRepeatInterval(*args, **kwargs):
        ...
    @staticmethod
    def setCheckable(*args, **kwargs):
        ...
    @staticmethod
    def setChecked(*args, **kwargs):
        ...
    @staticmethod
    def setDown(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setIconSize(*args, **kwargs):
        ...
    @staticmethod
    def setShortcut(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def shortcut(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def toggle(*args, **kwargs):
        ...
    @staticmethod
    def toggled(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QAbstractGraphicsShapeItem(QGraphicsItem):
    @staticmethod
    def brush(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def pen(*args, **kwargs):
        ...
    @staticmethod
    def setBrush(*args, **kwargs):
        ...
    @staticmethod
    def setPen(*args, **kwargs):
        ...
class QAbstractItemDelegate(PyQt6.QtCore.QObject):
    class EndEditHint(enum.Enum):
        EditNextItem: typing.ClassVar[QAbstractItemDelegate.EndEditHint]  # value = <EndEditHint.EditNextItem: 1>
        EditPreviousItem: typing.ClassVar[QAbstractItemDelegate.EndEditHint]  # value = <EndEditHint.EditPreviousItem: 2>
        NoHint: typing.ClassVar[QAbstractItemDelegate.EndEditHint]  # value = <EndEditHint.NoHint: 0>
        RevertModelCache: typing.ClassVar[QAbstractItemDelegate.EndEditHint]  # value = <EndEditHint.RevertModelCache: 4>
        SubmitModelCache: typing.ClassVar[QAbstractItemDelegate.EndEditHint]  # value = <EndEditHint.SubmitModelCache: 3>
    @staticmethod
    def closeEditor(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def commitData(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def createEditor(*args, **kwargs):
        ...
    @staticmethod
    def destroyEditor(*args, **kwargs):
        ...
    @staticmethod
    def editorEvent(*args, **kwargs):
        ...
    @staticmethod
    def helpEvent(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def setEditorData(*args, **kwargs):
        ...
    @staticmethod
    def setModelData(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sizeHintChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def updateEditorGeometry(*args, **kwargs):
        ...
class QAbstractItemView(QAbstractScrollArea):
    class CursorAction(enum.Enum):
        MoveDown: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MoveDown: 1>
        MoveEnd: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MoveEnd: 5>
        MoveHome: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MoveHome: 4>
        MoveLeft: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MoveLeft: 2>
        MoveNext: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MoveNext: 8>
        MovePageDown: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MovePageDown: 7>
        MovePageUp: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MovePageUp: 6>
        MovePrevious: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MovePrevious: 9>
        MoveRight: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MoveRight: 3>
        MoveUp: typing.ClassVar[QAbstractItemView.CursorAction]  # value = <CursorAction.MoveUp: 0>
    class DragDropMode(enum.Enum):
        DragDrop: typing.ClassVar[QAbstractItemView.DragDropMode]  # value = <DragDropMode.DragDrop: 3>
        DragOnly: typing.ClassVar[QAbstractItemView.DragDropMode]  # value = <DragDropMode.DragOnly: 1>
        DropOnly: typing.ClassVar[QAbstractItemView.DragDropMode]  # value = <DragDropMode.DropOnly: 2>
        InternalMove: typing.ClassVar[QAbstractItemView.DragDropMode]  # value = <DragDropMode.InternalMove: 4>
        NoDragDrop: typing.ClassVar[QAbstractItemView.DragDropMode]  # value = <DragDropMode.NoDragDrop: 0>
    class DropIndicatorPosition(enum.Enum):
        AboveItem: typing.ClassVar[QAbstractItemView.DropIndicatorPosition]  # value = <DropIndicatorPosition.AboveItem: 1>
        BelowItem: typing.ClassVar[QAbstractItemView.DropIndicatorPosition]  # value = <DropIndicatorPosition.BelowItem: 2>
        OnItem: typing.ClassVar[QAbstractItemView.DropIndicatorPosition]  # value = <DropIndicatorPosition.OnItem: 0>
        OnViewport: typing.ClassVar[QAbstractItemView.DropIndicatorPosition]  # value = <DropIndicatorPosition.OnViewport: 3>
    class EditTrigger(enum.Flag):
        AnyKeyPressed: typing.ClassVar[QAbstractItemView.EditTrigger]  # value = <EditTrigger.AnyKeyPressed: 16>
        CurrentChanged: typing.ClassVar[QAbstractItemView.EditTrigger]  # value = <EditTrigger.CurrentChanged: 1>
        DoubleClicked: typing.ClassVar[QAbstractItemView.EditTrigger]  # value = <EditTrigger.DoubleClicked: 2>
        EditKeyPressed: typing.ClassVar[QAbstractItemView.EditTrigger]  # value = <EditTrigger.EditKeyPressed: 8>
        SelectedClicked: typing.ClassVar[QAbstractItemView.EditTrigger]  # value = <EditTrigger.SelectedClicked: 4>
    class ScrollHint(enum.Enum):
        EnsureVisible: typing.ClassVar[QAbstractItemView.ScrollHint]  # value = <ScrollHint.EnsureVisible: 0>
        PositionAtBottom: typing.ClassVar[QAbstractItemView.ScrollHint]  # value = <ScrollHint.PositionAtBottom: 2>
        PositionAtCenter: typing.ClassVar[QAbstractItemView.ScrollHint]  # value = <ScrollHint.PositionAtCenter: 3>
        PositionAtTop: typing.ClassVar[QAbstractItemView.ScrollHint]  # value = <ScrollHint.PositionAtTop: 1>
    class ScrollMode(enum.Enum):
        ScrollPerItem: typing.ClassVar[QAbstractItemView.ScrollMode]  # value = <ScrollMode.ScrollPerItem: 0>
        ScrollPerPixel: typing.ClassVar[QAbstractItemView.ScrollMode]  # value = <ScrollMode.ScrollPerPixel: 1>
    class SelectionBehavior(enum.Enum):
        SelectColumns: typing.ClassVar[QAbstractItemView.SelectionBehavior]  # value = <SelectionBehavior.SelectColumns: 2>
        SelectItems: typing.ClassVar[QAbstractItemView.SelectionBehavior]  # value = <SelectionBehavior.SelectItems: 0>
        SelectRows: typing.ClassVar[QAbstractItemView.SelectionBehavior]  # value = <SelectionBehavior.SelectRows: 1>
    class SelectionMode(enum.Enum):
        ContiguousSelection: typing.ClassVar[QAbstractItemView.SelectionMode]  # value = <SelectionMode.ContiguousSelection: 4>
        ExtendedSelection: typing.ClassVar[QAbstractItemView.SelectionMode]  # value = <SelectionMode.ExtendedSelection: 3>
        MultiSelection: typing.ClassVar[QAbstractItemView.SelectionMode]  # value = <SelectionMode.MultiSelection: 2>
        NoSelection: typing.ClassVar[QAbstractItemView.SelectionMode]  # value = <SelectionMode.NoSelection: 0>
        SingleSelection: typing.ClassVar[QAbstractItemView.SelectionMode]  # value = <SelectionMode.SingleSelection: 1>
    class State(enum.Enum):
        AnimatingState: typing.ClassVar[QAbstractItemView.State]  # value = <State.AnimatingState: 6>
        CollapsingState: typing.ClassVar[QAbstractItemView.State]  # value = <State.CollapsingState: 5>
        DragSelectingState: typing.ClassVar[QAbstractItemView.State]  # value = <State.DragSelectingState: 2>
        DraggingState: typing.ClassVar[QAbstractItemView.State]  # value = <State.DraggingState: 1>
        EditingState: typing.ClassVar[QAbstractItemView.State]  # value = <State.EditingState: 3>
        ExpandingState: typing.ClassVar[QAbstractItemView.State]  # value = <State.ExpandingState: 4>
        NoState: typing.ClassVar[QAbstractItemView.State]  # value = <State.NoState: 0>
    @staticmethod
    def activated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def alternatingRowColors(*args, **kwargs):
        ...
    @staticmethod
    def autoScrollMargin(*args, **kwargs):
        ...
    @staticmethod
    def clearSelection(*args, **kwargs):
        ...
    @staticmethod
    def clicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def closeEditor(*args, **kwargs):
        ...
    @staticmethod
    def closePersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def commitData(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        ...
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def dataChanged(*args, **kwargs):
        ...
    @staticmethod
    def defaultDropAction(*args, **kwargs):
        ...
    @staticmethod
    def dirtyRegionOffset(*args, **kwargs):
        ...
    @staticmethod
    def doubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def dragDropMode(*args, **kwargs):
        ...
    @staticmethod
    def dragDropOverwriteMode(*args, **kwargs):
        ...
    @staticmethod
    def dragEnabled(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropIndicatorPosition(*args, **kwargs):
        ...
    @staticmethod
    def edit(*args, **kwargs):
        ...
    @staticmethod
    def editTriggers(*args, **kwargs):
        ...
    @staticmethod
    def editorDestroyed(*args, **kwargs):
        ...
    @staticmethod
    def entered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def executeDelayedItemsLayout(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def hasAutoScroll(*args, **kwargs):
        ...
    @staticmethod
    def horizontalOffset(*args, **kwargs):
        ...
    @staticmethod
    def horizontalScrollMode(*args, **kwargs):
        ...
    @staticmethod
    def horizontalScrollbarAction(*args, **kwargs):
        ...
    @staticmethod
    def horizontalScrollbarValueChanged(*args, **kwargs):
        ...
    @staticmethod
    def iconSize(*args, **kwargs):
        ...
    @staticmethod
    def iconSizeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def indexAt(*args, **kwargs):
        ...
    @staticmethod
    def indexWidget(*args, **kwargs):
        ...
    @staticmethod
    def initViewItemOption(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def isIndexHidden(*args, **kwargs):
        ...
    @staticmethod
    def isPersistentEditorOpen(*args, **kwargs):
        ...
    @staticmethod
    def itemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def itemDelegateForColumn(*args, **kwargs):
        ...
    @staticmethod
    def itemDelegateForIndex(*args, **kwargs):
        ...
    @staticmethod
    def itemDelegateForRow(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyboardSearch(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def openPersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def pressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def resetHorizontalScrollMode(*args, **kwargs):
        ...
    @staticmethod
    def resetVerticalScrollMode(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def rootIndex(*args, **kwargs):
        ...
    @staticmethod
    def rowsAboutToBeRemoved(*args, **kwargs):
        ...
    @staticmethod
    def rowsInserted(*args, **kwargs):
        ...
    @staticmethod
    def scheduleDelayedItemsLayout(*args, **kwargs):
        ...
    @staticmethod
    def scrollDirtyRegion(*args, **kwargs):
        ...
    @staticmethod
    def scrollTo(*args, **kwargs):
        ...
    @staticmethod
    def scrollToBottom(*args, **kwargs):
        ...
    @staticmethod
    def scrollToTop(*args, **kwargs):
        ...
    @staticmethod
    def selectAll(*args, **kwargs):
        ...
    @staticmethod
    def selectedIndexes(*args, **kwargs):
        ...
    @staticmethod
    def selectionBehavior(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        ...
    @staticmethod
    def selectionCommand(*args, **kwargs):
        ...
    @staticmethod
    def selectionMode(*args, **kwargs):
        ...
    @staticmethod
    def selectionModel(*args, **kwargs):
        ...
    @staticmethod
    def setAlternatingRowColors(*args, **kwargs):
        ...
    @staticmethod
    def setAutoScroll(*args, **kwargs):
        ...
    @staticmethod
    def setAutoScrollMargin(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultDropAction(*args, **kwargs):
        ...
    @staticmethod
    def setDirtyRegion(*args, **kwargs):
        ...
    @staticmethod
    def setDragDropMode(*args, **kwargs):
        ...
    @staticmethod
    def setDragDropOverwriteMode(*args, **kwargs):
        ...
    @staticmethod
    def setDragEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setDropIndicatorShown(*args, **kwargs):
        ...
    @staticmethod
    def setEditTriggers(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalScrollMode(*args, **kwargs):
        ...
    @staticmethod
    def setIconSize(*args, **kwargs):
        ...
    @staticmethod
    def setIndexWidget(*args, **kwargs):
        ...
    @staticmethod
    def setItemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def setItemDelegateForColumn(*args, **kwargs):
        ...
    @staticmethod
    def setItemDelegateForRow(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setRootIndex(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionBehavior(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionMode(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionModel(*args, **kwargs):
        ...
    @staticmethod
    def setState(*args, **kwargs):
        ...
    @staticmethod
    def setTabKeyNavigation(*args, **kwargs):
        ...
    @staticmethod
    def setTextElideMode(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalScrollMode(*args, **kwargs):
        ...
    @staticmethod
    def showDropIndicator(*args, **kwargs):
        ...
    @staticmethod
    def sizeHintForColumn(*args, **kwargs):
        ...
    @staticmethod
    def sizeHintForIndex(*args, **kwargs):
        ...
    @staticmethod
    def sizeHintForRow(*args, **kwargs):
        ...
    @staticmethod
    def startDrag(*args, **kwargs):
        ...
    @staticmethod
    def state(*args, **kwargs):
        ...
    @staticmethod
    def tabKeyNavigation(*args, **kwargs):
        ...
    @staticmethod
    def textElideMode(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def updateEditorData(*args, **kwargs):
        ...
    @staticmethod
    def updateEditorGeometries(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometries(*args, **kwargs):
        ...
    @staticmethod
    def verticalOffset(*args, **kwargs):
        ...
    @staticmethod
    def verticalScrollMode(*args, **kwargs):
        ...
    @staticmethod
    def verticalScrollbarAction(*args, **kwargs):
        ...
    @staticmethod
    def verticalScrollbarValueChanged(*args, **kwargs):
        ...
    @staticmethod
    def viewportEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def viewportEvent(*args, **kwargs):
        ...
    @staticmethod
    def viewportSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def visualRect(*args, **kwargs):
        ...
    @staticmethod
    def visualRegionForSelection(*args, **kwargs):
        ...
class QAbstractScrollArea(QFrame):
    class SizeAdjustPolicy(enum.Enum):
        AdjustIgnored: typing.ClassVar[QAbstractScrollArea.SizeAdjustPolicy]  # value = <SizeAdjustPolicy.AdjustIgnored: 0>
        AdjustToContents: typing.ClassVar[QAbstractScrollArea.SizeAdjustPolicy]  # value = <SizeAdjustPolicy.AdjustToContents: 2>
        AdjustToContentsOnFirstShow: typing.ClassVar[QAbstractScrollArea.SizeAdjustPolicy]  # value = <SizeAdjustPolicy.AdjustToContentsOnFirstShow: 1>
    @staticmethod
    def addScrollBarWidget(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def cornerWidget(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def horizontalScrollBar(*args, **kwargs):
        ...
    @staticmethod
    def horizontalScrollBarPolicy(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def maximumViewportSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def scrollBarWidgets(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def setCornerWidget(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalScrollBar(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalScrollBarPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setSizeAdjustPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalScrollBar(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalScrollBarPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setViewport(*args, **kwargs):
        ...
    @staticmethod
    def setViewportMargins(*args, **kwargs):
        ...
    @staticmethod
    def setupViewport(*args, **kwargs):
        ...
    @staticmethod
    def sizeAdjustPolicy(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def verticalScrollBar(*args, **kwargs):
        ...
    @staticmethod
    def verticalScrollBarPolicy(*args, **kwargs):
        ...
    @staticmethod
    def viewport(*args, **kwargs):
        ...
    @staticmethod
    def viewportEvent(*args, **kwargs):
        ...
    @staticmethod
    def viewportMargins(*args, **kwargs):
        ...
    @staticmethod
    def viewportSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
class QAbstractSlider(QWidget):
    class SliderAction(enum.Enum):
        SliderMove: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderMove: 7>
        SliderNoAction: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderNoAction: 0>
        SliderPageStepAdd: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderPageStepAdd: 3>
        SliderPageStepSub: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderPageStepSub: 4>
        SliderSingleStepAdd: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderSingleStepAdd: 1>
        SliderSingleStepSub: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderSingleStepSub: 2>
        SliderToMaximum: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderToMaximum: 6>
        SliderToMinimum: typing.ClassVar[QAbstractSlider.SliderAction]  # value = <SliderAction.SliderToMinimum: 5>
    class SliderChange(enum.Enum):
        SliderOrientationChange: typing.ClassVar[QAbstractSlider.SliderChange]  # value = <SliderChange.SliderOrientationChange: 1>
        SliderRangeChange: typing.ClassVar[QAbstractSlider.SliderChange]  # value = <SliderChange.SliderRangeChange: 0>
        SliderStepsChange: typing.ClassVar[QAbstractSlider.SliderChange]  # value = <SliderChange.SliderStepsChange: 2>
        SliderValueChange: typing.ClassVar[QAbstractSlider.SliderChange]  # value = <SliderChange.SliderValueChange: 3>
    @staticmethod
    def actionTriggered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def hasTracking(*args, **kwargs):
        ...
    @staticmethod
    def invertedAppearance(*args, **kwargs):
        ...
    @staticmethod
    def invertedControls(*args, **kwargs):
        ...
    @staticmethod
    def isSliderDown(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def maximum(*args, **kwargs):
        ...
    @staticmethod
    def minimum(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def pageStep(*args, **kwargs):
        ...
    @staticmethod
    def rangeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def repeatAction(*args, **kwargs):
        ...
    @staticmethod
    def setInvertedAppearance(*args, **kwargs):
        ...
    @staticmethod
    def setInvertedControls(*args, **kwargs):
        ...
    @staticmethod
    def setMaximum(*args, **kwargs):
        ...
    @staticmethod
    def setMinimum(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setPageStep(*args, **kwargs):
        ...
    @staticmethod
    def setRange(*args, **kwargs):
        ...
    @staticmethod
    def setRepeatAction(*args, **kwargs):
        ...
    @staticmethod
    def setSingleStep(*args, **kwargs):
        ...
    @staticmethod
    def setSliderDown(*args, **kwargs):
        ...
    @staticmethod
    def setSliderPosition(*args, **kwargs):
        ...
    @staticmethod
    def setTracking(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def singleStep(*args, **kwargs):
        ...
    @staticmethod
    def sliderChange(*args, **kwargs):
        ...
    @staticmethod
    def sliderMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sliderPosition(*args, **kwargs):
        ...
    @staticmethod
    def sliderPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sliderReleased(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def triggerAction(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def valueChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
class QAbstractSpinBox(QWidget):
    class ButtonSymbols(enum.Enum):
        NoButtons: typing.ClassVar[QAbstractSpinBox.ButtonSymbols]  # value = <ButtonSymbols.NoButtons: 2>
        PlusMinus: typing.ClassVar[QAbstractSpinBox.ButtonSymbols]  # value = <ButtonSymbols.PlusMinus: 1>
        UpDownArrows: typing.ClassVar[QAbstractSpinBox.ButtonSymbols]  # value = <ButtonSymbols.UpDownArrows: 0>
    class CorrectionMode(enum.Enum):
        CorrectToNearestValue: typing.ClassVar[QAbstractSpinBox.CorrectionMode]  # value = <CorrectionMode.CorrectToNearestValue: 1>
        CorrectToPreviousValue: typing.ClassVar[QAbstractSpinBox.CorrectionMode]  # value = <CorrectionMode.CorrectToPreviousValue: 0>
    class StepEnabledFlag(enum.Flag):
        StepDownEnabled: typing.ClassVar[QAbstractSpinBox.StepEnabledFlag]  # value = <StepEnabledFlag.StepDownEnabled: 2>
        StepUpEnabled: typing.ClassVar[QAbstractSpinBox.StepEnabledFlag]  # value = <StepEnabledFlag.StepUpEnabled: 1>
    class StepType(enum.Enum):
        AdaptiveDecimalStepType: typing.ClassVar[QAbstractSpinBox.StepType]  # value = <StepType.AdaptiveDecimalStepType: 1>
        DefaultStepType: typing.ClassVar[QAbstractSpinBox.StepType]  # value = <StepType.DefaultStepType: 0>
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def buttonSymbols(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def correctionMode(*args, **kwargs):
        ...
    @staticmethod
    def editingFinished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def fixup(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def hasAcceptableInput(*args, **kwargs):
        ...
    @staticmethod
    def hasFrame(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def interpretText(*args, **kwargs):
        ...
    @staticmethod
    def isAccelerated(*args, **kwargs):
        ...
    @staticmethod
    def isGroupSeparatorShown(*args, **kwargs):
        ...
    @staticmethod
    def isReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyboardTracking(*args, **kwargs):
        ...
    @staticmethod
    def lineEdit(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def selectAll(*args, **kwargs):
        ...
    @staticmethod
    def setAccelerated(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setButtonSymbols(*args, **kwargs):
        ...
    @staticmethod
    def setCorrectionMode(*args, **kwargs):
        ...
    @staticmethod
    def setFrame(*args, **kwargs):
        ...
    @staticmethod
    def setGroupSeparatorShown(*args, **kwargs):
        ...
    @staticmethod
    def setKeyboardTracking(*args, **kwargs):
        ...
    @staticmethod
    def setLineEdit(*args, **kwargs):
        ...
    @staticmethod
    def setReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def setSpecialValueText(*args, **kwargs):
        ...
    @staticmethod
    def setWrapping(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def specialValueText(*args, **kwargs):
        ...
    @staticmethod
    def stepBy(*args, **kwargs):
        ...
    @staticmethod
    def stepDown(*args, **kwargs):
        ...
    @staticmethod
    def stepEnabled(*args, **kwargs):
        ...
    @staticmethod
    def stepUp(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def wrapping(*args, **kwargs):
        ...
class QApplication(PyQt6.QtGui.QGuiApplication):
    @staticmethod
    def aboutQt(*args, **kwargs):
        ...
    @staticmethod
    def activeModalWidget(*args, **kwargs):
        ...
    @staticmethod
    def activePopupWidget(*args, **kwargs):
        ...
    @staticmethod
    def activeWindow(*args, **kwargs):
        ...
    @staticmethod
    def alert(*args, **kwargs):
        ...
    @staticmethod
    def allWidgets(*args, **kwargs):
        ...
    @staticmethod
    def autoSipEnabled(*args, **kwargs):
        ...
    @staticmethod
    def beep(*args, **kwargs):
        ...
    @staticmethod
    def closeAllWindows(*args, **kwargs):
        ...
    @staticmethod
    def cursorFlashTime(*args, **kwargs):
        ...
    @staticmethod
    def doubleClickInterval(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def focusChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def focusWidget(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def isEffectEnabled(*args, **kwargs):
        ...
    @staticmethod
    def keyboardInputInterval(*args, **kwargs):
        ...
    @staticmethod
    def notify(*args, **kwargs):
        ...
    @staticmethod
    def palette(*args, **kwargs):
        ...
    @staticmethod
    def setActiveWindow(*args, **kwargs):
        ...
    @staticmethod
    def setAutoSipEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setCursorFlashTime(*args, **kwargs):
        ...
    @staticmethod
    def setDoubleClickInterval(*args, **kwargs):
        ...
    @staticmethod
    def setEffectEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setKeyboardInputInterval(*args, **kwargs):
        ...
    @staticmethod
    def setPalette(*args, **kwargs):
        ...
    @staticmethod
    def setStartDragDistance(*args, **kwargs):
        ...
    @staticmethod
    def setStartDragTime(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def setStyleSheet(*args, **kwargs):
        ...
    @staticmethod
    def setWheelScrollLines(*args, **kwargs):
        ...
    @staticmethod
    def startDragDistance(*args, **kwargs):
        ...
    @staticmethod
    def startDragTime(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def styleSheet(*args, **kwargs):
        ...
    @staticmethod
    def topLevelAt(*args, **kwargs):
        ...
    @staticmethod
    def topLevelWidgets(*args, **kwargs):
        ...
    @staticmethod
    def wheelScrollLines(*args, **kwargs):
        ...
    @staticmethod
    def widgetAt(*args, **kwargs):
        ...
class QBoxLayout(QLayout):
    class Direction(enum.Enum):
        BottomToTop: typing.ClassVar[QBoxLayout.Direction]  # value = <Direction.BottomToTop: 3>
        LeftToRight: typing.ClassVar[QBoxLayout.Direction]  # value = <Direction.LeftToRight: 0>
        RightToLeft: typing.ClassVar[QBoxLayout.Direction]  # value = <Direction.RightToLeft: 1>
        TopToBottom: typing.ClassVar[QBoxLayout.Direction]  # value = <Direction.TopToBottom: 2>
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addLayout(*args, **kwargs):
        ...
    @staticmethod
    def addSpacerItem(*args, **kwargs):
        ...
    @staticmethod
    def addSpacing(*args, **kwargs):
        ...
    @staticmethod
    def addStretch(*args, **kwargs):
        ...
    @staticmethod
    def addStrut(*args, **kwargs):
        ...
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def direction(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def insertItem(*args, **kwargs):
        ...
    @staticmethod
    def insertLayout(*args, **kwargs):
        ...
    @staticmethod
    def insertSpacerItem(*args, **kwargs):
        ...
    @staticmethod
    def insertSpacing(*args, **kwargs):
        ...
    @staticmethod
    def insertStretch(*args, **kwargs):
        ...
    @staticmethod
    def insertWidget(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def setDirection(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setStretch(*args, **kwargs):
        ...
    @staticmethod
    def setStretchFactor(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def spacing(*args, **kwargs):
        ...
    @staticmethod
    def stretch(*args, **kwargs):
        ...
    @staticmethod
    def takeAt(*args, **kwargs):
        ...
class QButtonGroup(PyQt6.QtCore.QObject):
    @staticmethod
    def addButton(*args, **kwargs):
        ...
    @staticmethod
    def button(*args, **kwargs):
        ...
    @staticmethod
    def buttonClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def buttonPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def buttonReleased(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def buttonToggled(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def checkedButton(*args, **kwargs):
        ...
    @staticmethod
    def checkedId(*args, **kwargs):
        ...
    @staticmethod
    def exclusive(*args, **kwargs):
        ...
    @staticmethod
    def id(*args, **kwargs):
        ...
    @staticmethod
    def idClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def idPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def idReleased(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def idToggled(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def removeButton(*args, **kwargs):
        ...
    @staticmethod
    def setExclusive(*args, **kwargs):
        ...
    @staticmethod
    def setId(*args, **kwargs):
        ...
class QCalendarWidget(QWidget):
    class HorizontalHeaderFormat(enum.Enum):
        LongDayNames: typing.ClassVar[QCalendarWidget.HorizontalHeaderFormat]  # value = <HorizontalHeaderFormat.LongDayNames: 3>
        NoHorizontalHeader: typing.ClassVar[QCalendarWidget.HorizontalHeaderFormat]  # value = <HorizontalHeaderFormat.NoHorizontalHeader: 0>
        ShortDayNames: typing.ClassVar[QCalendarWidget.HorizontalHeaderFormat]  # value = <HorizontalHeaderFormat.ShortDayNames: 2>
        SingleLetterDayNames: typing.ClassVar[QCalendarWidget.HorizontalHeaderFormat]  # value = <HorizontalHeaderFormat.SingleLetterDayNames: 1>
    class SelectionMode(enum.Enum):
        NoSelection: typing.ClassVar[QCalendarWidget.SelectionMode]  # value = <SelectionMode.NoSelection: 0>
        SingleSelection: typing.ClassVar[QCalendarWidget.SelectionMode]  # value = <SelectionMode.SingleSelection: 1>
    class VerticalHeaderFormat(enum.Enum):
        ISOWeekNumbers: typing.ClassVar[QCalendarWidget.VerticalHeaderFormat]  # value = <VerticalHeaderFormat.ISOWeekNumbers: 1>
        NoVerticalHeader: typing.ClassVar[QCalendarWidget.VerticalHeaderFormat]  # value = <VerticalHeaderFormat.NoVerticalHeader: 0>
    @staticmethod
    def activated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def calendar(*args, **kwargs):
        ...
    @staticmethod
    def clearMaximumDate(*args, **kwargs):
        ...
    @staticmethod
    def clearMinimumDate(*args, **kwargs):
        ...
    @staticmethod
    def clicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentPageChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def dateEditAcceptDelay(*args, **kwargs):
        ...
    @staticmethod
    def dateTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def firstDayOfWeek(*args, **kwargs):
        ...
    @staticmethod
    def headerTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def horizontalHeaderFormat(*args, **kwargs):
        ...
    @staticmethod
    def isDateEditEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isGridVisible(*args, **kwargs):
        ...
    @staticmethod
    def isNavigationBarVisible(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def maximumDate(*args, **kwargs):
        ...
    @staticmethod
    def minimumDate(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def monthShown(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintCell(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def selectedDate(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def selectionMode(*args, **kwargs):
        ...
    @staticmethod
    def setCalendar(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentPage(*args, **kwargs):
        ...
    @staticmethod
    def setDateEditAcceptDelay(*args, **kwargs):
        ...
    @staticmethod
    def setDateEditEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setDateRange(*args, **kwargs):
        ...
    @staticmethod
    def setDateTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def setFirstDayOfWeek(*args, **kwargs):
        ...
    @staticmethod
    def setGridVisible(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalHeaderFormat(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumDate(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumDate(*args, **kwargs):
        ...
    @staticmethod
    def setNavigationBarVisible(*args, **kwargs):
        ...
    @staticmethod
    def setSelectedDate(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionMode(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalHeaderFormat(*args, **kwargs):
        ...
    @staticmethod
    def setWeekdayTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def showNextMonth(*args, **kwargs):
        ...
    @staticmethod
    def showNextYear(*args, **kwargs):
        ...
    @staticmethod
    def showPreviousMonth(*args, **kwargs):
        ...
    @staticmethod
    def showPreviousYear(*args, **kwargs):
        ...
    @staticmethod
    def showSelectedDate(*args, **kwargs):
        ...
    @staticmethod
    def showToday(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def updateCell(*args, **kwargs):
        ...
    @staticmethod
    def updateCells(*args, **kwargs):
        ...
    @staticmethod
    def verticalHeaderFormat(*args, **kwargs):
        ...
    @staticmethod
    def weekdayTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def yearShown(*args, **kwargs):
        ...
class QCheckBox(QAbstractButton):
    @staticmethod
    def checkState(*args, **kwargs):
        ...
    @staticmethod
    def checkStateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def checkStateSet(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def hitButton(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def isTristate(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def nextCheckState(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setCheckState(*args, **kwargs):
        ...
    @staticmethod
    def setTristate(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def stateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QColorDialog(QDialog):
    class ColorDialogOption(enum.Flag):
        DontUseNativeDialog: typing.ClassVar[QColorDialog.ColorDialogOption]  # value = <ColorDialogOption.DontUseNativeDialog: 4>
        NoButtons: typing.ClassVar[QColorDialog.ColorDialogOption]  # value = <ColorDialogOption.NoButtons: 2>
        NoEyeDropperButton: typing.ClassVar[QColorDialog.ColorDialogOption]  # value = <ColorDialogOption.NoEyeDropperButton: 8>
        ShowAlphaChannel: typing.ClassVar[QColorDialog.ColorDialogOption]  # value = <ColorDialogOption.ShowAlphaChannel: 1>
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def colorSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentColor(*args, **kwargs):
        ...
    @staticmethod
    def currentColorChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def customColor(*args, **kwargs):
        ...
    @staticmethod
    def customCount(*args, **kwargs):
        ...
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def getColor(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def selectedColor(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentColor(*args, **kwargs):
        ...
    @staticmethod
    def setCustomColor(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setStandardColor(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def standardColor(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
class QColumnView(QAbstractItemView):
    @staticmethod
    def columnWidths(*args, **kwargs):
        ...
    @staticmethod
    def createColumn(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        ...
    @staticmethod
    def horizontalOffset(*args, **kwargs):
        ...
    @staticmethod
    def indexAt(*args, **kwargs):
        ...
    @staticmethod
    def initializeColumn(*args, **kwargs):
        ...
    @staticmethod
    def isIndexHidden(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def previewWidget(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeGripsVisible(*args, **kwargs):
        ...
    @staticmethod
    def rowsInserted(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def scrollTo(*args, **kwargs):
        ...
    @staticmethod
    def selectAll(*args, **kwargs):
        ...
    @staticmethod
    def setColumnWidths(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setPreviewWidget(*args, **kwargs):
        ...
    @staticmethod
    def setResizeGripsVisible(*args, **kwargs):
        ...
    @staticmethod
    def setRootIndex(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionModel(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def updatePreviewWidget(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def verticalOffset(*args, **kwargs):
        ...
    @staticmethod
    def visualRect(*args, **kwargs):
        ...
    @staticmethod
    def visualRegionForSelection(*args, **kwargs):
        ...
class QComboBox(QWidget):
    class InsertPolicy(enum.Enum):
        InsertAfterCurrent: typing.ClassVar[QComboBox.InsertPolicy]  # value = <InsertPolicy.InsertAfterCurrent: 4>
        InsertAlphabetically: typing.ClassVar[QComboBox.InsertPolicy]  # value = <InsertPolicy.InsertAlphabetically: 6>
        InsertAtBottom: typing.ClassVar[QComboBox.InsertPolicy]  # value = <InsertPolicy.InsertAtBottom: 3>
        InsertAtCurrent: typing.ClassVar[QComboBox.InsertPolicy]  # value = <InsertPolicy.InsertAtCurrent: 2>
        InsertAtTop: typing.ClassVar[QComboBox.InsertPolicy]  # value = <InsertPolicy.InsertAtTop: 1>
        InsertBeforeCurrent: typing.ClassVar[QComboBox.InsertPolicy]  # value = <InsertPolicy.InsertBeforeCurrent: 5>
        NoInsert: typing.ClassVar[QComboBox.InsertPolicy]  # value = <InsertPolicy.NoInsert: 0>
    class SizeAdjustPolicy(enum.Enum):
        AdjustToContents: typing.ClassVar[QComboBox.SizeAdjustPolicy]  # value = <SizeAdjustPolicy.AdjustToContents: 0>
        AdjustToContentsOnFirstShow: typing.ClassVar[QComboBox.SizeAdjustPolicy]  # value = <SizeAdjustPolicy.AdjustToContentsOnFirstShow: 1>
        AdjustToMinimumContentsLengthWithIcon: typing.ClassVar[QComboBox.SizeAdjustPolicy]  # value = <SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon: 2>
    @staticmethod
    def activated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addItems(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearEditText(*args, **kwargs):
        ...
    @staticmethod
    def completer(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentData(*args, **kwargs):
        ...
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def currentIndexChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentText(*args, **kwargs):
        ...
    @staticmethod
    def currentTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def duplicatesEnabled(*args, **kwargs):
        ...
    @staticmethod
    def editTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def findData(*args, **kwargs):
        ...
    @staticmethod
    def findText(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def hasFrame(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def hidePopup(*args, **kwargs):
        ...
    @staticmethod
    def highlighted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def iconSize(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def insertItem(*args, **kwargs):
        ...
    @staticmethod
    def insertItems(*args, **kwargs):
        ...
    @staticmethod
    def insertPolicy(*args, **kwargs):
        ...
    @staticmethod
    def insertSeparator(*args, **kwargs):
        ...
    @staticmethod
    def isEditable(*args, **kwargs):
        ...
    @staticmethod
    def itemData(*args, **kwargs):
        ...
    @staticmethod
    def itemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def itemIcon(*args, **kwargs):
        ...
    @staticmethod
    def itemText(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def lineEdit(*args, **kwargs):
        ...
    @staticmethod
    def maxCount(*args, **kwargs):
        ...
    @staticmethod
    def maxVisibleItems(*args, **kwargs):
        ...
    @staticmethod
    def minimumContentsLength(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def modelColumn(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def placeholderText(*args, **kwargs):
        ...
    @staticmethod
    def removeItem(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def rootModelIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCompleter(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentText(*args, **kwargs):
        ...
    @staticmethod
    def setDuplicatesEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setEditText(*args, **kwargs):
        ...
    @staticmethod
    def setEditable(*args, **kwargs):
        ...
    @staticmethod
    def setFrame(*args, **kwargs):
        ...
    @staticmethod
    def setIconSize(*args, **kwargs):
        ...
    @staticmethod
    def setInsertPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setItemData(*args, **kwargs):
        ...
    @staticmethod
    def setItemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def setItemIcon(*args, **kwargs):
        ...
    @staticmethod
    def setItemText(*args, **kwargs):
        ...
    @staticmethod
    def setLineEdit(*args, **kwargs):
        ...
    @staticmethod
    def setMaxCount(*args, **kwargs):
        ...
    @staticmethod
    def setMaxVisibleItems(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumContentsLength(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setModelColumn(*args, **kwargs):
        ...
    @staticmethod
    def setPlaceholderText(*args, **kwargs):
        ...
    @staticmethod
    def setRootModelIndex(*args, **kwargs):
        ...
    @staticmethod
    def setSizeAdjustPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setValidator(*args, **kwargs):
        ...
    @staticmethod
    def setView(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def showPopup(*args, **kwargs):
        ...
    @staticmethod
    def sizeAdjustPolicy(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def textActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textHighlighted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def validator(*args, **kwargs):
        ...
    @staticmethod
    def view(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QCommandLinkButton(QPushButton):
    @staticmethod
    def description(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setDescription(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
class QCommonStyle(QStyle):
    @staticmethod
    def drawComplexControl(*args, **kwargs):
        ...
    @staticmethod
    def drawControl(*args, **kwargs):
        ...
    @staticmethod
    def drawPrimitive(*args, **kwargs):
        ...
    @staticmethod
    def generatedIconPixmap(*args, **kwargs):
        ...
    @staticmethod
    def hitTestComplexControl(*args, **kwargs):
        ...
    @staticmethod
    def layoutSpacing(*args, **kwargs):
        ...
    @staticmethod
    def pixelMetric(*args, **kwargs):
        ...
    @staticmethod
    def polish(*args, **kwargs):
        ...
    @staticmethod
    def sizeFromContents(*args, **kwargs):
        ...
    @staticmethod
    def standardIcon(*args, **kwargs):
        ...
    @staticmethod
    def standardPixmap(*args, **kwargs):
        ...
    @staticmethod
    def styleHint(*args, **kwargs):
        ...
    @staticmethod
    def subControlRect(*args, **kwargs):
        ...
    @staticmethod
    def subElementRect(*args, **kwargs):
        ...
    @staticmethod
    def unpolish(*args, **kwargs):
        ...
class QCompleter(PyQt6.QtCore.QObject):
    class CompletionMode(enum.Enum):
        InlineCompletion: typing.ClassVar[QCompleter.CompletionMode]  # value = <CompletionMode.InlineCompletion: 2>
        PopupCompletion: typing.ClassVar[QCompleter.CompletionMode]  # value = <CompletionMode.PopupCompletion: 0>
        UnfilteredPopupCompletion: typing.ClassVar[QCompleter.CompletionMode]  # value = <CompletionMode.UnfilteredPopupCompletion: 1>
    class ModelSorting(enum.Enum):
        CaseInsensitivelySortedModel: typing.ClassVar[QCompleter.ModelSorting]  # value = <ModelSorting.CaseInsensitivelySortedModel: 2>
        CaseSensitivelySortedModel: typing.ClassVar[QCompleter.ModelSorting]  # value = <ModelSorting.CaseSensitivelySortedModel: 1>
        UnsortedModel: typing.ClassVar[QCompleter.ModelSorting]  # value = <ModelSorting.UnsortedModel: 0>
    @staticmethod
    def activated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def caseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def complete(*args, **kwargs):
        ...
    @staticmethod
    def completionColumn(*args, **kwargs):
        ...
    @staticmethod
    def completionCount(*args, **kwargs):
        ...
    @staticmethod
    def completionMode(*args, **kwargs):
        ...
    @staticmethod
    def completionModel(*args, **kwargs):
        ...
    @staticmethod
    def completionPrefix(*args, **kwargs):
        ...
    @staticmethod
    def completionRole(*args, **kwargs):
        ...
    @staticmethod
    def currentCompletion(*args, **kwargs):
        ...
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def currentRow(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def filterMode(*args, **kwargs):
        ...
    @staticmethod
    def highlighted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def maxVisibleItems(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def modelSorting(*args, **kwargs):
        ...
    @staticmethod
    def pathFromIndex(*args, **kwargs):
        ...
    @staticmethod
    def popup(*args, **kwargs):
        ...
    @staticmethod
    def setCaseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def setCompletionColumn(*args, **kwargs):
        ...
    @staticmethod
    def setCompletionMode(*args, **kwargs):
        ...
    @staticmethod
    def setCompletionPrefix(*args, **kwargs):
        ...
    @staticmethod
    def setCompletionRole(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentRow(*args, **kwargs):
        ...
    @staticmethod
    def setFilterMode(*args, **kwargs):
        ...
    @staticmethod
    def setMaxVisibleItems(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setModelSorting(*args, **kwargs):
        ...
    @staticmethod
    def setPopup(*args, **kwargs):
        ...
    @staticmethod
    def setWidget(*args, **kwargs):
        ...
    @staticmethod
    def setWrapAround(*args, **kwargs):
        ...
    @staticmethod
    def splitPath(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
    @staticmethod
    def wrapAround(*args, **kwargs):
        ...
class QDataWidgetMapper(PyQt6.QtCore.QObject):
    class SubmitPolicy(enum.Enum):
        AutoSubmit: typing.ClassVar[QDataWidgetMapper.SubmitPolicy]  # value = <SubmitPolicy.AutoSubmit: 0>
        ManualSubmit: typing.ClassVar[QDataWidgetMapper.SubmitPolicy]  # value = <SubmitPolicy.ManualSubmit: 1>
    @staticmethod
    def addMapping(*args, **kwargs):
        ...
    @staticmethod
    def clearMapping(*args, **kwargs):
        ...
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def currentIndexChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def mappedPropertyName(*args, **kwargs):
        ...
    @staticmethod
    def mappedSection(*args, **kwargs):
        ...
    @staticmethod
    def mappedWidgetAt(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def removeMapping(*args, **kwargs):
        ...
    @staticmethod
    def revert(*args, **kwargs):
        ...
    @staticmethod
    def rootIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentModelIndex(*args, **kwargs):
        ...
    @staticmethod
    def setItemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setRootIndex(*args, **kwargs):
        ...
    @staticmethod
    def setSubmitPolicy(*args, **kwargs):
        ...
    @staticmethod
    def submit(*args, **kwargs):
        ...
    @staticmethod
    def submitPolicy(*args, **kwargs):
        ...
    @staticmethod
    def toFirst(*args, **kwargs):
        ...
    @staticmethod
    def toLast(*args, **kwargs):
        ...
    @staticmethod
    def toNext(*args, **kwargs):
        ...
    @staticmethod
    def toPrevious(*args, **kwargs):
        ...
class QDateEdit(QDateTimeEdit):
    pass
class QDateTimeEdit(QAbstractSpinBox):
    class Section(enum.Flag):
        AmPmSection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.AmPmSection: 1>
        DaySection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.DaySection: 256>
        HourSection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.HourSection: 16>
        MSecSection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.MSecSection: 2>
        MinuteSection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.MinuteSection: 8>
        MonthSection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.MonthSection: 512>
        SecondSection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.SecondSection: 4>
        YearSection: typing.ClassVar[QDateTimeEdit.Section]  # value = <Section.YearSection: 1024>
    @staticmethod
    def calendar(*args, **kwargs):
        ...
    @staticmethod
    def calendarPopup(*args, **kwargs):
        ...
    @staticmethod
    def calendarWidget(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearMaximumDate(*args, **kwargs):
        ...
    @staticmethod
    def clearMaximumDateTime(*args, **kwargs):
        ...
    @staticmethod
    def clearMaximumTime(*args, **kwargs):
        ...
    @staticmethod
    def clearMinimumDate(*args, **kwargs):
        ...
    @staticmethod
    def clearMinimumDateTime(*args, **kwargs):
        ...
    @staticmethod
    def clearMinimumTime(*args, **kwargs):
        ...
    @staticmethod
    def currentSection(*args, **kwargs):
        ...
    @staticmethod
    def currentSectionIndex(*args, **kwargs):
        ...
    @staticmethod
    def date(*args, **kwargs):
        ...
    @staticmethod
    def dateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def dateTime(*args, **kwargs):
        ...
    @staticmethod
    def dateTimeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def dateTimeFromText(*args, **kwargs):
        ...
    @staticmethod
    def displayFormat(*args, **kwargs):
        ...
    @staticmethod
    def displayedSections(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def fixup(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def maximumDate(*args, **kwargs):
        ...
    @staticmethod
    def maximumDateTime(*args, **kwargs):
        ...
    @staticmethod
    def maximumTime(*args, **kwargs):
        ...
    @staticmethod
    def minimumDate(*args, **kwargs):
        ...
    @staticmethod
    def minimumDateTime(*args, **kwargs):
        ...
    @staticmethod
    def minimumTime(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def sectionAt(*args, **kwargs):
        ...
    @staticmethod
    def sectionCount(*args, **kwargs):
        ...
    @staticmethod
    def sectionText(*args, **kwargs):
        ...
    @staticmethod
    def setCalendar(*args, **kwargs):
        ...
    @staticmethod
    def setCalendarPopup(*args, **kwargs):
        ...
    @staticmethod
    def setCalendarWidget(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentSection(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentSectionIndex(*args, **kwargs):
        ...
    @staticmethod
    def setDate(*args, **kwargs):
        ...
    @staticmethod
    def setDateRange(*args, **kwargs):
        ...
    @staticmethod
    def setDateTime(*args, **kwargs):
        ...
    @staticmethod
    def setDateTimeRange(*args, **kwargs):
        ...
    @staticmethod
    def setDisplayFormat(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumDate(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumDateTime(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumTime(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumDate(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumDateTime(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumTime(*args, **kwargs):
        ...
    @staticmethod
    def setSelectedSection(*args, **kwargs):
        ...
    @staticmethod
    def setTime(*args, **kwargs):
        ...
    @staticmethod
    def setTimeRange(*args, **kwargs):
        ...
    @staticmethod
    def setTimeSpec(*args, **kwargs):
        ...
    @staticmethod
    def setTimeZone(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def stepBy(*args, **kwargs):
        ...
    @staticmethod
    def stepEnabled(*args, **kwargs):
        ...
    @staticmethod
    def textFromDateTime(*args, **kwargs):
        ...
    @staticmethod
    def time(*args, **kwargs):
        ...
    @staticmethod
    def timeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def timeSpec(*args, **kwargs):
        ...
    @staticmethod
    def timeZone(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
class QDial(QAbstractSlider):
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def notchSize(*args, **kwargs):
        ...
    @staticmethod
    def notchTarget(*args, **kwargs):
        ...
    @staticmethod
    def notchesVisible(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setNotchTarget(*args, **kwargs):
        ...
    @staticmethod
    def setNotchesVisible(*args, **kwargs):
        ...
    @staticmethod
    def setWrapping(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sliderChange(*args, **kwargs):
        ...
    @staticmethod
    def wrapping(*args, **kwargs):
        ...
class QDialog(QWidget):
    class DialogCode(enum.IntEnum):
        Accepted: typing.ClassVar[QDialog.DialogCode]  # value = <DialogCode.Accepted: 1>
        Rejected: typing.ClassVar[QDialog.DialogCode]  # value = <DialogCode.Rejected: 0>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def accepted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def finished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def isSizeGripEnabled(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def reject(*args, **kwargs):
        ...
    @staticmethod
    def rejected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def result(*args, **kwargs):
        ...
    @staticmethod
    def setModal(*args, **kwargs):
        ...
    @staticmethod
    def setResult(*args, **kwargs):
        ...
    @staticmethod
    def setSizeGripEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
class QDialogButtonBox(QWidget):
    class ButtonLayout(enum.Enum):
        AndroidLayout: typing.ClassVar[QDialogButtonBox.ButtonLayout]  # value = <ButtonLayout.AndroidLayout: 4>
        GnomeLayout: typing.ClassVar[QDialogButtonBox.ButtonLayout]  # value = <ButtonLayout.GnomeLayout: 3>
        KdeLayout: typing.ClassVar[QDialogButtonBox.ButtonLayout]  # value = <ButtonLayout.KdeLayout: 2>
        MacLayout: typing.ClassVar[QDialogButtonBox.ButtonLayout]  # value = <ButtonLayout.MacLayout: 1>
        WinLayout: typing.ClassVar[QDialogButtonBox.ButtonLayout]  # value = <ButtonLayout.WinLayout: 0>
    class ButtonRole(enum.Enum):
        AcceptRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.AcceptRole: 0>
        ActionRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.ActionRole: 3>
        ApplyRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.ApplyRole: 8>
        DestructiveRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.DestructiveRole: 2>
        HelpRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.HelpRole: 4>
        InvalidRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.InvalidRole: -1>
        NoRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.NoRole: 6>
        RejectRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.RejectRole: 1>
        ResetRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.ResetRole: 7>
        YesRole: typing.ClassVar[QDialogButtonBox.ButtonRole]  # value = <ButtonRole.YesRole: 5>
    class StandardButton(enum.Flag):
        Abort: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Abort: 262144>
        Apply: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Apply: 33554432>
        Cancel: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Cancel: 4194304>
        Close: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Close: 2097152>
        Discard: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Discard: 8388608>
        Help: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Help: 16777216>
        Ignore: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Ignore: 1048576>
        No: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.No: 65536>
        NoToAll: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.NoToAll: 131072>
        Ok: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Ok: 1024>
        Open: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Open: 8192>
        Reset: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Reset: 67108864>
        RestoreDefaults: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.RestoreDefaults: 134217728>
        Retry: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Retry: 524288>
        Save: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Save: 2048>
        SaveAll: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.SaveAll: 4096>
        Yes: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.Yes: 16384>
        YesToAll: typing.ClassVar[QDialogButtonBox.StandardButton]  # value = <StandardButton.YesToAll: 32768>
    @staticmethod
    def accepted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def addButton(*args, **kwargs):
        ...
    @staticmethod
    def button(*args, **kwargs):
        ...
    @staticmethod
    def buttonRole(*args, **kwargs):
        ...
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def centerButtons(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def helpRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def rejected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def removeButton(*args, **kwargs):
        ...
    @staticmethod
    def setCenterButtons(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setStandardButtons(*args, **kwargs):
        ...
    @staticmethod
    def standardButton(*args, **kwargs):
        ...
    @staticmethod
    def standardButtons(*args, **kwargs):
        ...
class QDockWidget(QWidget):
    class DockWidgetFeature(enum.Flag):
        DockWidgetClosable: typing.ClassVar[QDockWidget.DockWidgetFeature]  # value = <DockWidgetFeature.DockWidgetClosable: 1>
        DockWidgetFloatable: typing.ClassVar[QDockWidget.DockWidgetFeature]  # value = <DockWidgetFeature.DockWidgetFloatable: 4>
        DockWidgetMovable: typing.ClassVar[QDockWidget.DockWidgetFeature]  # value = <DockWidgetFeature.DockWidgetMovable: 2>
        DockWidgetVerticalTitleBar: typing.ClassVar[QDockWidget.DockWidgetFeature]  # value = <DockWidgetFeature.DockWidgetVerticalTitleBar: 8>
    @staticmethod
    def allowedAreas(*args, **kwargs):
        ...
    @staticmethod
    def allowedAreasChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def dockLocationChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def features(*args, **kwargs):
        ...
    @staticmethod
    def featuresChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def isAreaAllowed(*args, **kwargs):
        ...
    @staticmethod
    def isFloating(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setAllowedAreas(*args, **kwargs):
        ...
    @staticmethod
    def setFeatures(*args, **kwargs):
        ...
    @staticmethod
    def setFloating(*args, **kwargs):
        ...
    @staticmethod
    def setTitleBarWidget(*args, **kwargs):
        ...
    @staticmethod
    def setWidget(*args, **kwargs):
        ...
    @staticmethod
    def titleBarWidget(*args, **kwargs):
        ...
    @staticmethod
    def toggleViewAction(*args, **kwargs):
        ...
    @staticmethod
    def topLevelChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def visibilityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def widget(*args, **kwargs):
        ...
class QDoubleSpinBox(QAbstractSpinBox):
    @staticmethod
    def cleanText(*args, **kwargs):
        ...
    @staticmethod
    def decimals(*args, **kwargs):
        ...
    @staticmethod
    def fixup(*args, **kwargs):
        ...
    @staticmethod
    def maximum(*args, **kwargs):
        ...
    @staticmethod
    def minimum(*args, **kwargs):
        ...
    @staticmethod
    def prefix(*args, **kwargs):
        ...
    @staticmethod
    def setDecimals(*args, **kwargs):
        ...
    @staticmethod
    def setMaximum(*args, **kwargs):
        ...
    @staticmethod
    def setMinimum(*args, **kwargs):
        ...
    @staticmethod
    def setPrefix(*args, **kwargs):
        ...
    @staticmethod
    def setRange(*args, **kwargs):
        ...
    @staticmethod
    def setSingleStep(*args, **kwargs):
        ...
    @staticmethod
    def setStepType(*args, **kwargs):
        ...
    @staticmethod
    def setSuffix(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def singleStep(*args, **kwargs):
        ...
    @staticmethod
    def stepType(*args, **kwargs):
        ...
    @staticmethod
    def suffix(*args, **kwargs):
        ...
    @staticmethod
    def textChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textFromValue(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def valueChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def valueFromText(*args, **kwargs):
        ...
class QErrorMessage(QDialog):
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def qtHandler(*args, **kwargs):
        ...
    @staticmethod
    def showMessage(*args, **kwargs):
        ...
class QFileDialog(QDialog):
    class AcceptMode(enum.Enum):
        AcceptOpen: typing.ClassVar[QFileDialog.AcceptMode]  # value = <AcceptMode.AcceptOpen: 0>
        AcceptSave: typing.ClassVar[QFileDialog.AcceptMode]  # value = <AcceptMode.AcceptSave: 1>
    class DialogLabel(enum.Enum):
        Accept: typing.ClassVar[QFileDialog.DialogLabel]  # value = <DialogLabel.Accept: 3>
        FileName: typing.ClassVar[QFileDialog.DialogLabel]  # value = <DialogLabel.FileName: 1>
        FileType: typing.ClassVar[QFileDialog.DialogLabel]  # value = <DialogLabel.FileType: 2>
        LookIn: typing.ClassVar[QFileDialog.DialogLabel]  # value = <DialogLabel.LookIn: 0>
        Reject: typing.ClassVar[QFileDialog.DialogLabel]  # value = <DialogLabel.Reject: 4>
    class FileMode(enum.Enum):
        AnyFile: typing.ClassVar[QFileDialog.FileMode]  # value = <FileMode.AnyFile: 0>
        Directory: typing.ClassVar[QFileDialog.FileMode]  # value = <FileMode.Directory: 2>
        ExistingFile: typing.ClassVar[QFileDialog.FileMode]  # value = <FileMode.ExistingFile: 1>
        ExistingFiles: typing.ClassVar[QFileDialog.FileMode]  # value = <FileMode.ExistingFiles: 3>
    class Option(enum.Flag):
        DontConfirmOverwrite: typing.ClassVar[QFileDialog.Option]  # value = <Option.DontConfirmOverwrite: 4>
        DontResolveSymlinks: typing.ClassVar[QFileDialog.Option]  # value = <Option.DontResolveSymlinks: 2>
        DontUseCustomDirectoryIcons: typing.ClassVar[QFileDialog.Option]  # value = <Option.DontUseCustomDirectoryIcons: 64>
        DontUseNativeDialog: typing.ClassVar[QFileDialog.Option]  # value = <Option.DontUseNativeDialog: 8>
        HideNameFilterDetails: typing.ClassVar[QFileDialog.Option]  # value = <Option.HideNameFilterDetails: 32>
        ReadOnly: typing.ClassVar[QFileDialog.Option]  # value = <Option.ReadOnly: 16>
        ShowDirsOnly: typing.ClassVar[QFileDialog.Option]  # value = <Option.ShowDirsOnly: 1>
    class ViewMode(enum.Enum):
        Detail: typing.ClassVar[QFileDialog.ViewMode]  # value = <ViewMode.Detail: 0>
        List: typing.ClassVar[QFileDialog.ViewMode]  # value = <ViewMode.List: 1>
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def acceptMode(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentUrlChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def defaultSuffix(*args, **kwargs):
        ...
    @staticmethod
    def directory(*args, **kwargs):
        ...
    @staticmethod
    def directoryEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def directoryUrl(*args, **kwargs):
        ...
    @staticmethod
    def directoryUrlEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def fileMode(*args, **kwargs):
        ...
    @staticmethod
    def fileSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def filesSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def filter(*args, **kwargs):
        ...
    @staticmethod
    def filterSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def getExistingDirectory(*args, **kwargs):
        ...
    @staticmethod
    def getExistingDirectoryUrl(*args, **kwargs):
        ...
    @staticmethod
    def getOpenFileName(*args, **kwargs):
        ...
    @staticmethod
    def getOpenFileNames(*args, **kwargs):
        ...
    @staticmethod
    def getOpenFileUrl(*args, **kwargs):
        ...
    @staticmethod
    def getOpenFileUrls(*args, **kwargs):
        ...
    @staticmethod
    def getSaveFileName(*args, **kwargs):
        ...
    @staticmethod
    def getSaveFileUrl(*args, **kwargs):
        ...
    @staticmethod
    def history(*args, **kwargs):
        ...
    @staticmethod
    def iconProvider(*args, **kwargs):
        ...
    @staticmethod
    def itemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def labelText(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypeFilters(*args, **kwargs):
        ...
    @staticmethod
    def nameFilters(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def proxyModel(*args, **kwargs):
        ...
    @staticmethod
    def restoreState(*args, **kwargs):
        ...
    @staticmethod
    def saveFileContent(*args, **kwargs):
        ...
    @staticmethod
    def saveState(*args, **kwargs):
        ...
    @staticmethod
    def selectFile(*args, **kwargs):
        ...
    @staticmethod
    def selectMimeTypeFilter(*args, **kwargs):
        ...
    @staticmethod
    def selectNameFilter(*args, **kwargs):
        ...
    @staticmethod
    def selectUrl(*args, **kwargs):
        ...
    @staticmethod
    def selectedFiles(*args, **kwargs):
        ...
    @staticmethod
    def selectedMimeTypeFilter(*args, **kwargs):
        ...
    @staticmethod
    def selectedNameFilter(*args, **kwargs):
        ...
    @staticmethod
    def selectedUrls(*args, **kwargs):
        ...
    @staticmethod
    def setAcceptMode(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultSuffix(*args, **kwargs):
        ...
    @staticmethod
    def setDirectory(*args, **kwargs):
        ...
    @staticmethod
    def setDirectoryUrl(*args, **kwargs):
        ...
    @staticmethod
    def setFileMode(*args, **kwargs):
        ...
    @staticmethod
    def setFilter(*args, **kwargs):
        ...
    @staticmethod
    def setHistory(*args, **kwargs):
        ...
    @staticmethod
    def setIconProvider(*args, **kwargs):
        ...
    @staticmethod
    def setItemDelegate(*args, **kwargs):
        ...
    @staticmethod
    def setLabelText(*args, **kwargs):
        ...
    @staticmethod
    def setMimeTypeFilters(*args, **kwargs):
        ...
    @staticmethod
    def setNameFilter(*args, **kwargs):
        ...
    @staticmethod
    def setNameFilters(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setProxyModel(*args, **kwargs):
        ...
    @staticmethod
    def setSidebarUrls(*args, **kwargs):
        ...
    @staticmethod
    def setSupportedSchemes(*args, **kwargs):
        ...
    @staticmethod
    def setViewMode(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def sidebarUrls(*args, **kwargs):
        ...
    @staticmethod
    def supportedSchemes(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def urlSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def urlsSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def viewMode(*args, **kwargs):
        ...
class QFileIconProvider(PyQt6.QtGui.QAbstractFileIconProvider):
    @staticmethod
    def icon(*args, **kwargs):
        ...
class QFocusFrame(QWidget):
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setWidget(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
class QFontComboBox(QComboBox):
    class FontFilter(enum.Flag):
        MonospacedFonts: typing.ClassVar[QFontComboBox.FontFilter]  # value = <FontFilter.MonospacedFonts: 4>
        NonScalableFonts: typing.ClassVar[QFontComboBox.FontFilter]  # value = <FontFilter.NonScalableFonts: 2>
        ProportionalFonts: typing.ClassVar[QFontComboBox.FontFilter]  # value = <FontFilter.ProportionalFonts: 8>
        ScalableFonts: typing.ClassVar[QFontComboBox.FontFilter]  # value = <FontFilter.ScalableFonts: 1>
    @staticmethod
    def currentFont(*args, **kwargs):
        ...
    @staticmethod
    def currentFontChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def displayFont(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def fontFilters(*args, **kwargs):
        ...
    @staticmethod
    def sampleTextForFont(*args, **kwargs):
        ...
    @staticmethod
    def sampleTextForSystem(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentFont(*args, **kwargs):
        ...
    @staticmethod
    def setDisplayFont(*args, **kwargs):
        ...
    @staticmethod
    def setFontFilters(*args, **kwargs):
        ...
    @staticmethod
    def setSampleTextForFont(*args, **kwargs):
        ...
    @staticmethod
    def setSampleTextForSystem(*args, **kwargs):
        ...
    @staticmethod
    def setWritingSystem(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def writingSystem(*args, **kwargs):
        ...
class QFontDialog(QDialog):
    class FontDialogOption(enum.Flag):
        DontUseNativeDialog: typing.ClassVar[QFontDialog.FontDialogOption]  # value = <FontDialogOption.DontUseNativeDialog: 2>
        MonospacedFonts: typing.ClassVar[QFontDialog.FontDialogOption]  # value = <FontDialogOption.MonospacedFonts: 16>
        NoButtons: typing.ClassVar[QFontDialog.FontDialogOption]  # value = <FontDialogOption.NoButtons: 1>
        NonScalableFonts: typing.ClassVar[QFontDialog.FontDialogOption]  # value = <FontDialogOption.NonScalableFonts: 8>
        ProportionalFonts: typing.ClassVar[QFontDialog.FontDialogOption]  # value = <FontDialogOption.ProportionalFonts: 32>
        ScalableFonts: typing.ClassVar[QFontDialog.FontDialogOption]  # value = <FontDialogOption.ScalableFonts: 4>
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def currentFont(*args, **kwargs):
        ...
    @staticmethod
    def currentFontChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def fontSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def getFont(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def selectedFont(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentFont(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
class QFormLayout(QLayout):
    class FieldGrowthPolicy(enum.Enum):
        AllNonFixedFieldsGrow: typing.ClassVar[QFormLayout.FieldGrowthPolicy]  # value = <FieldGrowthPolicy.AllNonFixedFieldsGrow: 2>
        ExpandingFieldsGrow: typing.ClassVar[QFormLayout.FieldGrowthPolicy]  # value = <FieldGrowthPolicy.ExpandingFieldsGrow: 1>
        FieldsStayAtSizeHint: typing.ClassVar[QFormLayout.FieldGrowthPolicy]  # value = <FieldGrowthPolicy.FieldsStayAtSizeHint: 0>
    class ItemRole(enum.Enum):
        FieldRole: typing.ClassVar[QFormLayout.ItemRole]  # value = <ItemRole.FieldRole: 1>
        LabelRole: typing.ClassVar[QFormLayout.ItemRole]  # value = <ItemRole.LabelRole: 0>
        SpanningRole: typing.ClassVar[QFormLayout.ItemRole]  # value = <ItemRole.SpanningRole: 2>
    class RowWrapPolicy(enum.Enum):
        DontWrapRows: typing.ClassVar[QFormLayout.RowWrapPolicy]  # value = <RowWrapPolicy.DontWrapRows: 0>
        WrapAllRows: typing.ClassVar[QFormLayout.RowWrapPolicy]  # value = <RowWrapPolicy.WrapAllRows: 2>
        WrapLongRows: typing.ClassVar[QFormLayout.RowWrapPolicy]  # value = <RowWrapPolicy.WrapLongRows: 1>
    class TakeRowResult(PyQt6.sip.simplewrapper):
        pass
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addRow(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def fieldGrowthPolicy(*args, **kwargs):
        ...
    @staticmethod
    def formAlignment(*args, **kwargs):
        ...
    @staticmethod
    def getItemPosition(*args, **kwargs):
        ...
    @staticmethod
    def getLayoutPosition(*args, **kwargs):
        ...
    @staticmethod
    def getWidgetPosition(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def horizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def insertRow(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def isRowVisible(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def labelAlignment(*args, **kwargs):
        ...
    @staticmethod
    def labelForField(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def removeRow(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def rowWrapPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setFieldGrowthPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setFormAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setItem(*args, **kwargs):
        ...
    @staticmethod
    def setLabelAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setLayout(*args, **kwargs):
        ...
    @staticmethod
    def setRowVisible(*args, **kwargs):
        ...
    @staticmethod
    def setRowWrapPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setWidget(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def spacing(*args, **kwargs):
        ...
    @staticmethod
    def takeAt(*args, **kwargs):
        ...
    @staticmethod
    def takeRow(*args, **kwargs):
        ...
    @staticmethod
    def verticalSpacing(*args, **kwargs):
        ...
class QFrame(QWidget):
    class Shadow(enum.IntEnum):
        Plain: typing.ClassVar[QFrame.Shadow]  # value = <Shadow.Plain: 16>
        Raised: typing.ClassVar[QFrame.Shadow]  # value = <Shadow.Raised: 32>
        Sunken: typing.ClassVar[QFrame.Shadow]  # value = <Shadow.Sunken: 48>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class Shape(enum.IntEnum):
        Box: typing.ClassVar[QFrame.Shape]  # value = <Shape.Box: 1>
        HLine: typing.ClassVar[QFrame.Shape]  # value = <Shape.HLine: 4>
        NoFrame: typing.ClassVar[QFrame.Shape]  # value = <Shape.NoFrame: 0>
        Panel: typing.ClassVar[QFrame.Shape]  # value = <Shape.Panel: 2>
        StyledPanel: typing.ClassVar[QFrame.Shape]  # value = <Shape.StyledPanel: 6>
        VLine: typing.ClassVar[QFrame.Shape]  # value = <Shape.VLine: 5>
        WinPanel: typing.ClassVar[QFrame.Shape]  # value = <Shape.WinPanel: 3>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class StyleMask(enum.Enum):
        Shadow_Mask: typing.ClassVar[QFrame.StyleMask]  # value = <StyleMask.Shadow_Mask: 240>
        Shape_Mask: typing.ClassVar[QFrame.StyleMask]  # value = <StyleMask.Shape_Mask: 15>
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def drawFrame(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def frameRect(*args, **kwargs):
        ...
    @staticmethod
    def frameShadow(*args, **kwargs):
        ...
    @staticmethod
    def frameShape(*args, **kwargs):
        ...
    @staticmethod
    def frameStyle(*args, **kwargs):
        ...
    @staticmethod
    def frameWidth(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def lineWidth(*args, **kwargs):
        ...
    @staticmethod
    def midLineWidth(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setFrameRect(*args, **kwargs):
        ...
    @staticmethod
    def setFrameShadow(*args, **kwargs):
        ...
    @staticmethod
    def setFrameShape(*args, **kwargs):
        ...
    @staticmethod
    def setFrameStyle(*args, **kwargs):
        ...
    @staticmethod
    def setLineWidth(*args, **kwargs):
        ...
    @staticmethod
    def setMidLineWidth(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
class QGesture(PyQt6.QtCore.QObject):
    class GestureCancelPolicy(enum.Enum):
        CancelAllInContext: typing.ClassVar[QGesture.GestureCancelPolicy]  # value = <GestureCancelPolicy.CancelAllInContext: 1>
        CancelNone: typing.ClassVar[QGesture.GestureCancelPolicy]  # value = <GestureCancelPolicy.CancelNone: 0>
    @staticmethod
    def gestureCancelPolicy(*args, **kwargs):
        ...
    @staticmethod
    def gestureType(*args, **kwargs):
        ...
    @staticmethod
    def hasHotSpot(*args, **kwargs):
        ...
    @staticmethod
    def hotSpot(*args, **kwargs):
        ...
    @staticmethod
    def setGestureCancelPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setHotSpot(*args, **kwargs):
        ...
    @staticmethod
    def state(*args, **kwargs):
        ...
    @staticmethod
    def unsetHotSpot(*args, **kwargs):
        ...
class QGestureEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def activeGestures(*args, **kwargs):
        ...
    @staticmethod
    def canceledGestures(*args, **kwargs):
        ...
    @staticmethod
    def gesture(*args, **kwargs):
        ...
    @staticmethod
    def gestures(*args, **kwargs):
        ...
    @staticmethod
    def ignore(*args, **kwargs):
        ...
    @staticmethod
    def isAccepted(*args, **kwargs):
        ...
    @staticmethod
    def mapToGraphicsScene(*args, **kwargs):
        ...
    @staticmethod
    def setAccepted(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
class QGestureRecognizer(PyQt6.sip.wrapper):
    class ResultFlag(enum.Flag):
        CancelGesture: typing.ClassVar[QGestureRecognizer.ResultFlag]  # value = <ResultFlag.CancelGesture: 16>
        ConsumeEventHint: typing.ClassVar[QGestureRecognizer.ResultFlag]  # value = <ResultFlag.ConsumeEventHint: 256>
        FinishGesture: typing.ClassVar[QGestureRecognizer.ResultFlag]  # value = <ResultFlag.FinishGesture: 8>
        Ignore: typing.ClassVar[QGestureRecognizer.ResultFlag]  # value = <ResultFlag.Ignore: 1>
        MayBeGesture: typing.ClassVar[QGestureRecognizer.ResultFlag]  # value = <ResultFlag.MayBeGesture: 2>
        TriggerGesture: typing.ClassVar[QGestureRecognizer.ResultFlag]  # value = <ResultFlag.TriggerGesture: 4>
    @staticmethod
    def create(*args, **kwargs):
        ...
    @staticmethod
    def recognize(*args, **kwargs):
        ...
    @staticmethod
    def registerRecognizer(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def unregisterRecognizer(*args, **kwargs):
        ...
class QGraphicsAnchor(PyQt6.QtCore.QObject):
    @staticmethod
    def setSizePolicy(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def sizePolicy(*args, **kwargs):
        ...
    @staticmethod
    def spacing(*args, **kwargs):
        ...
    @staticmethod
    def unsetSpacing(*args, **kwargs):
        ...
class QGraphicsAnchorLayout(QGraphicsLayout):
    @staticmethod
    def addAnchor(*args, **kwargs):
        ...
    @staticmethod
    def addAnchors(*args, **kwargs):
        ...
    @staticmethod
    def addCornerAnchors(*args, **kwargs):
        ...
    @staticmethod
    def anchor(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def horizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def removeAt(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def verticalSpacing(*args, **kwargs):
        ...
class QGraphicsBlurEffect(QGraphicsEffect):
    class BlurHint(enum.Flag):
        AnimationHint: typing.ClassVar[QGraphicsBlurEffect.BlurHint]  # value = <BlurHint.AnimationHint: 2>
        QualityHint: typing.ClassVar[QGraphicsBlurEffect.BlurHint]  # value = <BlurHint.QualityHint: 1>
    @staticmethod
    def blurHints(*args, **kwargs):
        ...
    @staticmethod
    def blurHintsChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def blurRadius(*args, **kwargs):
        ...
    @staticmethod
    def blurRadiusChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def boundingRectFor(*args, **kwargs):
        ...
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def setBlurHints(*args, **kwargs):
        ...
    @staticmethod
    def setBlurRadius(*args, **kwargs):
        ...
class QGraphicsColorizeEffect(QGraphicsEffect):
    @staticmethod
    def color(*args, **kwargs):
        ...
    @staticmethod
    def colorChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def setColor(*args, **kwargs):
        ...
    @staticmethod
    def setStrength(*args, **kwargs):
        ...
    @staticmethod
    def strength(*args, **kwargs):
        ...
    @staticmethod
    def strengthChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QGraphicsDropShadowEffect(QGraphicsEffect):
    @staticmethod
    def blurRadius(*args, **kwargs):
        ...
    @staticmethod
    def blurRadiusChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def boundingRectFor(*args, **kwargs):
        ...
    @staticmethod
    def color(*args, **kwargs):
        ...
    @staticmethod
    def colorChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def offset(*args, **kwargs):
        ...
    @staticmethod
    def offsetChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setBlurRadius(*args, **kwargs):
        ...
    @staticmethod
    def setColor(*args, **kwargs):
        ...
    @staticmethod
    def setOffset(*args, **kwargs):
        ...
    @staticmethod
    def setXOffset(*args, **kwargs):
        ...
    @staticmethod
    def setYOffset(*args, **kwargs):
        ...
    @staticmethod
    def xOffset(*args, **kwargs):
        ...
    @staticmethod
    def yOffset(*args, **kwargs):
        ...
class QGraphicsEffect(PyQt6.QtCore.QObject):
    class ChangeFlag(enum.Flag):
        SourceAttached: typing.ClassVar[QGraphicsEffect.ChangeFlag]  # value = <ChangeFlag.SourceAttached: 1>
        SourceBoundingRectChanged: typing.ClassVar[QGraphicsEffect.ChangeFlag]  # value = <ChangeFlag.SourceBoundingRectChanged: 4>
        SourceDetached: typing.ClassVar[QGraphicsEffect.ChangeFlag]  # value = <ChangeFlag.SourceDetached: 2>
        SourceInvalidated: typing.ClassVar[QGraphicsEffect.ChangeFlag]  # value = <ChangeFlag.SourceInvalidated: 8>
    class PixmapPadMode(enum.Enum):
        NoPad: typing.ClassVar[QGraphicsEffect.PixmapPadMode]  # value = <PixmapPadMode.NoPad: 0>
        PadToEffectiveBoundingRect: typing.ClassVar[QGraphicsEffect.PixmapPadMode]  # value = <PixmapPadMode.PadToEffectiveBoundingRect: 2>
        PadToTransparentBorder: typing.ClassVar[QGraphicsEffect.PixmapPadMode]  # value = <PixmapPadMode.PadToTransparentBorder: 1>
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def boundingRectFor(*args, **kwargs):
        ...
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def drawSource(*args, **kwargs):
        ...
    @staticmethod
    def enabledChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def sourceBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def sourceChanged(*args, **kwargs):
        ...
    @staticmethod
    def sourceIsPixmap(*args, **kwargs):
        ...
    @staticmethod
    def sourcePixmap(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def updateBoundingRect(*args, **kwargs):
        ...
class QGraphicsEllipseItem(QAbstractGraphicsShapeItem):
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def setRect(*args, **kwargs):
        ...
    @staticmethod
    def setSpanAngle(*args, **kwargs):
        ...
    @staticmethod
    def setStartAngle(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def spanAngle(*args, **kwargs):
        ...
    @staticmethod
    def startAngle(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsGridLayout(QGraphicsLayout):
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def columnAlignment(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def columnMaximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def columnMinimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def columnPreferredWidth(*args, **kwargs):
        ...
    @staticmethod
    def columnSpacing(*args, **kwargs):
        ...
    @staticmethod
    def columnStretchFactor(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def horizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def removeAt(*args, **kwargs):
        ...
    @staticmethod
    def removeItem(*args, **kwargs):
        ...
    @staticmethod
    def rowAlignment(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def rowMaximumHeight(*args, **kwargs):
        ...
    @staticmethod
    def rowMinimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def rowPreferredHeight(*args, **kwargs):
        ...
    @staticmethod
    def rowSpacing(*args, **kwargs):
        ...
    @staticmethod
    def rowStretchFactor(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setColumnAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setColumnFixedWidth(*args, **kwargs):
        ...
    @staticmethod
    def setColumnMaximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def setColumnMinimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def setColumnPreferredWidth(*args, **kwargs):
        ...
    @staticmethod
    def setColumnSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setColumnStretchFactor(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setRowAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setRowFixedHeight(*args, **kwargs):
        ...
    @staticmethod
    def setRowMaximumHeight(*args, **kwargs):
        ...
    @staticmethod
    def setRowMinimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def setRowPreferredHeight(*args, **kwargs):
        ...
    @staticmethod
    def setRowSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setRowStretchFactor(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def verticalSpacing(*args, **kwargs):
        ...
class QGraphicsItem(PyQt6.sip.wrapper):
    class CacheMode(enum.Enum):
        DeviceCoordinateCache: typing.ClassVar[QGraphicsItem.CacheMode]  # value = <CacheMode.DeviceCoordinateCache: 2>
        ItemCoordinateCache: typing.ClassVar[QGraphicsItem.CacheMode]  # value = <CacheMode.ItemCoordinateCache: 1>
        NoCache: typing.ClassVar[QGraphicsItem.CacheMode]  # value = <CacheMode.NoCache: 0>
    class GraphicsItemChange(enum.Enum):
        ItemChildAddedChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemChildAddedChange: 6>
        ItemChildRemovedChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemChildRemovedChange: 7>
        ItemCursorChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemCursorChange: 17>
        ItemCursorHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemCursorHasChanged: 18>
        ItemEnabledChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemEnabledChange: 3>
        ItemEnabledHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemEnabledHasChanged: 13>
        ItemFlagsChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemFlagsChange: 21>
        ItemFlagsHaveChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemFlagsHaveChanged: 22>
        ItemOpacityChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemOpacityChange: 25>
        ItemOpacityHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemOpacityHasChanged: 26>
        ItemParentChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemParentChange: 5>
        ItemParentHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemParentHasChanged: 15>
        ItemPositionChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemPositionChange: 0>
        ItemPositionHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemPositionHasChanged: 9>
        ItemRotationChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemRotationChange: 28>
        ItemRotationHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemRotationHasChanged: 29>
        ItemScaleChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemScaleChange: 30>
        ItemScaleHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemScaleHasChanged: 31>
        ItemSceneChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemSceneChange: 11>
        ItemSceneHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemSceneHasChanged: 16>
        ItemScenePositionHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemScenePositionHasChanged: 27>
        ItemSelectedChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemSelectedChange: 4>
        ItemSelectedHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemSelectedHasChanged: 14>
        ItemToolTipChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemToolTipChange: 19>
        ItemToolTipHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemToolTipHasChanged: 20>
        ItemTransformChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemTransformChange: 8>
        ItemTransformHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemTransformHasChanged: 10>
        ItemTransformOriginPointChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemTransformOriginPointChange: 32>
        ItemTransformOriginPointHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemTransformOriginPointHasChanged: 33>
        ItemVisibleChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemVisibleChange: 2>
        ItemVisibleHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemVisibleHasChanged: 12>
        ItemZValueChange: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemZValueChange: 23>
        ItemZValueHasChanged: typing.ClassVar[QGraphicsItem.GraphicsItemChange]  # value = <GraphicsItemChange.ItemZValueHasChanged: 24>
    class GraphicsItemFlag(enum.Flag):
        ItemAcceptsInputMethod: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemAcceptsInputMethod: 4096>
        ItemClipsChildrenToShape: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemClipsChildrenToShape: 16>
        ItemClipsToShape: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemClipsToShape: 8>
        ItemContainsChildrenInShape: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemContainsChildrenInShape: 524288>
        ItemDoesntPropagateOpacityToChildren: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemDoesntPropagateOpacityToChildren: 128>
        ItemHasNoContents: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemHasNoContents: 1024>
        ItemIgnoresParentOpacity: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemIgnoresParentOpacity: 64>
        ItemIgnoresTransformations: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemIgnoresTransformations: 32>
        ItemIsFocusable: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemIsFocusable: 4>
        ItemIsMovable: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemIsMovable: 1>
        ItemIsPanel: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemIsPanel: 16384>
        ItemIsSelectable: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemIsSelectable: 2>
        ItemNegativeZStacksBehindParent: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemNegativeZStacksBehindParent: 8192>
        ItemSendsGeometryChanges: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemSendsGeometryChanges: 2048>
        ItemSendsScenePositionChanges: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemSendsScenePositionChanges: 65536>
        ItemStacksBehindParent: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemStacksBehindParent: 256>
        ItemUsesExtendedStyleOption: typing.ClassVar[QGraphicsItem.GraphicsItemFlag]  # value = <GraphicsItemFlag.ItemUsesExtendedStyleOption: 512>
    class PanelModality(enum.Enum):
        NonModal: typing.ClassVar[QGraphicsItem.PanelModality]  # value = <PanelModality.NonModal: 0>
        PanelModal: typing.ClassVar[QGraphicsItem.PanelModality]  # value = <PanelModality.PanelModal: 1>
        SceneModal: typing.ClassVar[QGraphicsItem.PanelModality]  # value = <PanelModality.SceneModal: 2>
    Type: typing.ClassVar[int] = 1
    UserType: typing.ClassVar[int] = 65536
    @staticmethod
    def acceptDrops(*args, **kwargs):
        ...
    @staticmethod
    def acceptHoverEvents(*args, **kwargs):
        ...
    @staticmethod
    def acceptTouchEvents(*args, **kwargs):
        ...
    @staticmethod
    def acceptedMouseButtons(*args, **kwargs):
        ...
    @staticmethod
    def advance(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def boundingRegion(*args, **kwargs):
        ...
    @staticmethod
    def boundingRegionGranularity(*args, **kwargs):
        ...
    @staticmethod
    def cacheMode(*args, **kwargs):
        ...
    @staticmethod
    def childItems(*args, **kwargs):
        ...
    @staticmethod
    def childrenBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def clearFocus(*args, **kwargs):
        ...
    @staticmethod
    def clipPath(*args, **kwargs):
        ...
    @staticmethod
    def collidesWithItem(*args, **kwargs):
        ...
    @staticmethod
    def collidesWithPath(*args, **kwargs):
        ...
    @staticmethod
    def collidingItems(*args, **kwargs):
        ...
    @staticmethod
    def commonAncestorItem(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def cursor(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def deviceTransform(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def effectiveOpacity(*args, **kwargs):
        ...
    @staticmethod
    def ensureVisible(*args, **kwargs):
        ...
    @staticmethod
    def filtersChildEvents(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusItem(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusProxy(*args, **kwargs):
        ...
    @staticmethod
    def grabKeyboard(*args, **kwargs):
        ...
    @staticmethod
    def grabMouse(*args, **kwargs):
        ...
    @staticmethod
    def graphicsEffect(*args, **kwargs):
        ...
    @staticmethod
    def group(*args, **kwargs):
        ...
    @staticmethod
    def hasCursor(*args, **kwargs):
        ...
    @staticmethod
    def hasFocus(*args, **kwargs):
        ...
    @staticmethod
    def hide(*args, **kwargs):
        ...
    @staticmethod
    def hoverEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodHints(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def installSceneEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def isAncestorOf(*args, **kwargs):
        ...
    @staticmethod
    def isBlockedByModalPanel(*args, **kwargs):
        ...
    @staticmethod
    def isClipped(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isObscured(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def isPanel(*args, **kwargs):
        ...
    @staticmethod
    def isSelected(*args, **kwargs):
        ...
    @staticmethod
    def isUnderMouse(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def isVisibleTo(*args, **kwargs):
        ...
    @staticmethod
    def isWidget(*args, **kwargs):
        ...
    @staticmethod
    def isWindow(*args, **kwargs):
        ...
    @staticmethod
    def itemChange(*args, **kwargs):
        ...
    @staticmethod
    def itemTransform(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def mapFromItem(*args, **kwargs):
        ...
    @staticmethod
    def mapFromParent(*args, **kwargs):
        ...
    @staticmethod
    def mapFromScene(*args, **kwargs):
        ...
    @staticmethod
    def mapRectFromItem(*args, **kwargs):
        ...
    @staticmethod
    def mapRectFromParent(*args, **kwargs):
        ...
    @staticmethod
    def mapRectFromScene(*args, **kwargs):
        ...
    @staticmethod
    def mapRectToItem(*args, **kwargs):
        ...
    @staticmethod
    def mapRectToParent(*args, **kwargs):
        ...
    @staticmethod
    def mapRectToScene(*args, **kwargs):
        ...
    @staticmethod
    def mapToItem(*args, **kwargs):
        ...
    @staticmethod
    def mapToParent(*args, **kwargs):
        ...
    @staticmethod
    def mapToScene(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveBy(*args, **kwargs):
        ...
    @staticmethod
    def opacity(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def panel(*args, **kwargs):
        ...
    @staticmethod
    def panelModality(*args, **kwargs):
        ...
    @staticmethod
    def parentItem(*args, **kwargs):
        ...
    @staticmethod
    def parentObject(*args, **kwargs):
        ...
    @staticmethod
    def parentWidget(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def prepareGeometryChange(*args, **kwargs):
        ...
    @staticmethod
    def removeSceneEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def resetTransform(*args, **kwargs):
        ...
    @staticmethod
    def rotation(*args, **kwargs):
        ...
    @staticmethod
    def scale(*args, **kwargs):
        ...
    @staticmethod
    def scene(*args, **kwargs):
        ...
    @staticmethod
    def sceneBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def sceneEvent(*args, **kwargs):
        ...
    @staticmethod
    def sceneEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def scenePos(*args, **kwargs):
        ...
    @staticmethod
    def sceneTransform(*args, **kwargs):
        ...
    @staticmethod
    def scroll(*args, **kwargs):
        ...
    @staticmethod
    def setAcceptDrops(*args, **kwargs):
        ...
    @staticmethod
    def setAcceptHoverEvents(*args, **kwargs):
        ...
    @staticmethod
    def setAcceptTouchEvents(*args, **kwargs):
        ...
    @staticmethod
    def setAcceptedMouseButtons(*args, **kwargs):
        ...
    @staticmethod
    def setActive(*args, **kwargs):
        ...
    @staticmethod
    def setBoundingRegionGranularity(*args, **kwargs):
        ...
    @staticmethod
    def setCacheMode(*args, **kwargs):
        ...
    @staticmethod
    def setCursor(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setFiltersChildEvents(*args, **kwargs):
        ...
    @staticmethod
    def setFlag(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setFocus(*args, **kwargs):
        ...
    @staticmethod
    def setFocusProxy(*args, **kwargs):
        ...
    @staticmethod
    def setGraphicsEffect(*args, **kwargs):
        ...
    @staticmethod
    def setGroup(*args, **kwargs):
        ...
    @staticmethod
    def setInputMethodHints(*args, **kwargs):
        ...
    @staticmethod
    def setOpacity(*args, **kwargs):
        ...
    @staticmethod
    def setPanelModality(*args, **kwargs):
        ...
    @staticmethod
    def setParentItem(*args, **kwargs):
        ...
    @staticmethod
    def setPos(*args, **kwargs):
        ...
    @staticmethod
    def setRotation(*args, **kwargs):
        ...
    @staticmethod
    def setScale(*args, **kwargs):
        ...
    @staticmethod
    def setSelected(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setTransform(*args, **kwargs):
        ...
    @staticmethod
    def setTransformOriginPoint(*args, **kwargs):
        ...
    @staticmethod
    def setTransformations(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def setZValue(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def show(*args, **kwargs):
        ...
    @staticmethod
    def stackBefore(*args, **kwargs):
        ...
    @staticmethod
    def toGraphicsObject(*args, **kwargs):
        ...
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
    @staticmethod
    def topLevelItem(*args, **kwargs):
        ...
    @staticmethod
    def topLevelWidget(*args, **kwargs):
        ...
    @staticmethod
    def transform(*args, **kwargs):
        ...
    @staticmethod
    def transformOriginPoint(*args, **kwargs):
        ...
    @staticmethod
    def transformations(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def ungrabKeyboard(*args, **kwargs):
        ...
    @staticmethod
    def ungrabMouse(*args, **kwargs):
        ...
    @staticmethod
    def unsetCursor(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def updateMicroFocus(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def window(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
    @staticmethod
    def zValue(*args, **kwargs):
        ...
class QGraphicsItemGroup(QGraphicsItem):
    @staticmethod
    def addToGroup(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def removeFromGroup(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsLayout(QGraphicsLayoutItem):
    @staticmethod
    def activate(*args, **kwargs):
        ...
    @staticmethod
    def addChildLayoutItem(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def getContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def isActivated(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def removeAt(*args, **kwargs):
        ...
    @staticmethod
    def setContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometry(*args, **kwargs):
        ...
    @staticmethod
    def widgetEvent(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QGraphicsLayoutItem(PyQt6.sip.wrapper):
    @staticmethod
    def contentsRect(*args, **kwargs):
        ...
    @staticmethod
    def effectiveSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def getContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def graphicsItem(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isLayout(*args, **kwargs):
        ...
    @staticmethod
    def maximumHeight(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def maximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def minimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def ownedByLayout(*args, **kwargs):
        ...
    @staticmethod
    def parentLayoutItem(*args, **kwargs):
        ...
    @staticmethod
    def preferredHeight(*args, **kwargs):
        ...
    @staticmethod
    def preferredSize(*args, **kwargs):
        ...
    @staticmethod
    def preferredWidth(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setGraphicsItem(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumHeight(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumSize(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumSize(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def setOwnedByLayout(*args, **kwargs):
        ...
    @staticmethod
    def setParentLayoutItem(*args, **kwargs):
        ...
    @staticmethod
    def setPreferredHeight(*args, **kwargs):
        ...
    @staticmethod
    def setPreferredSize(*args, **kwargs):
        ...
    @staticmethod
    def setPreferredWidth(*args, **kwargs):
        ...
    @staticmethod
    def setSizePolicy(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sizePolicy(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometry(*args, **kwargs):
        ...
class QGraphicsLineItem(QGraphicsItem):
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def line(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def pen(*args, **kwargs):
        ...
    @staticmethod
    def setLine(*args, **kwargs):
        ...
    @staticmethod
    def setPen(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsLinearLayout(QGraphicsLayout):
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addStretch(*args, **kwargs):
        ...
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def insertItem(*args, **kwargs):
        ...
    @staticmethod
    def insertStretch(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def itemSpacing(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def removeAt(*args, **kwargs):
        ...
    @staticmethod
    def removeItem(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setItemSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setStretchFactor(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def spacing(*args, **kwargs):
        ...
    @staticmethod
    def stretchFactor(*args, **kwargs):
        ...
class QGraphicsObject(PyQt6.QtCore.QObject, QGraphicsItem):
    @staticmethod
    def enabledChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def grabGesture(*args, **kwargs):
        ...
    @staticmethod
    def opacityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def parentChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rotationChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def scaleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def ungrabGesture(*args, **kwargs):
        ...
    @staticmethod
    def updateMicroFocus(*args, **kwargs):
        ...
    @staticmethod
    def visibleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def xChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def yChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def zChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QGraphicsOpacityEffect(QGraphicsEffect):
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def opacity(*args, **kwargs):
        ...
    @staticmethod
    def opacityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def opacityMask(*args, **kwargs):
        ...
    @staticmethod
    def opacityMaskChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setOpacity(*args, **kwargs):
        ...
    @staticmethod
    def setOpacityMask(*args, **kwargs):
        ...
class QGraphicsPathItem(QAbstractGraphicsShapeItem):
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
    @staticmethod
    def setPath(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsPixmapItem(QGraphicsItem):
    class ShapeMode(enum.Enum):
        BoundingRectShape: typing.ClassVar[QGraphicsPixmapItem.ShapeMode]  # value = <ShapeMode.BoundingRectShape: 1>
        HeuristicMaskShape: typing.ClassVar[QGraphicsPixmapItem.ShapeMode]  # value = <ShapeMode.HeuristicMaskShape: 2>
        MaskShape: typing.ClassVar[QGraphicsPixmapItem.ShapeMode]  # value = <ShapeMode.MaskShape: 0>
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def offset(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def setOffset(*args, **kwargs):
        ...
    @staticmethod
    def setPixmap(*args, **kwargs):
        ...
    @staticmethod
    def setShapeMode(*args, **kwargs):
        ...
    @staticmethod
    def setTransformationMode(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def shapeMode(*args, **kwargs):
        ...
    @staticmethod
    def transformationMode(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsPolygonItem(QAbstractGraphicsShapeItem):
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def fillRule(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def polygon(*args, **kwargs):
        ...
    @staticmethod
    def setFillRule(*args, **kwargs):
        ...
    @staticmethod
    def setPolygon(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsProxyWidget(QGraphicsWidget):
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def createProxyForChildWidget(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def grabMouseEvent(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def itemChange(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def newProxyWidget(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setWidget(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def subWidgetRect(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def ungrabMouseEvent(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
class QGraphicsRectItem(QAbstractGraphicsShapeItem):
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def setRect(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsRotation(QGraphicsTransform):
    @staticmethod
    def angle(*args, **kwargs):
        ...
    @staticmethod
    def angleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def applyTo(*args, **kwargs):
        ...
    @staticmethod
    def axis(*args, **kwargs):
        ...
    @staticmethod
    def axisChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def origin(*args, **kwargs):
        ...
    @staticmethod
    def originChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setAngle(*args, **kwargs):
        ...
    @staticmethod
    def setAxis(*args, **kwargs):
        ...
    @staticmethod
    def setOrigin(*args, **kwargs):
        ...
class QGraphicsScale(QGraphicsTransform):
    @staticmethod
    def applyTo(*args, **kwargs):
        ...
    @staticmethod
    def origin(*args, **kwargs):
        ...
    @staticmethod
    def originChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def scaleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setOrigin(*args, **kwargs):
        ...
    @staticmethod
    def setXScale(*args, **kwargs):
        ...
    @staticmethod
    def setYScale(*args, **kwargs):
        ...
    @staticmethod
    def setZScale(*args, **kwargs):
        ...
    @staticmethod
    def xScale(*args, **kwargs):
        ...
    @staticmethod
    def xScaleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def yScale(*args, **kwargs):
        ...
    @staticmethod
    def yScaleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def zScale(*args, **kwargs):
        ...
    @staticmethod
    def zScaleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QGraphicsScene(PyQt6.QtCore.QObject):
    class ItemIndexMethod(enum.Enum):
        BspTreeIndex: typing.ClassVar[QGraphicsScene.ItemIndexMethod]  # value = <ItemIndexMethod.BspTreeIndex: 0>
        NoIndex: typing.ClassVar[QGraphicsScene.ItemIndexMethod]  # value = <ItemIndexMethod.NoIndex: -1>
    class SceneLayer(enum.Flag):
        BackgroundLayer: typing.ClassVar[QGraphicsScene.SceneLayer]  # value = <SceneLayer.BackgroundLayer: 2>
        ForegroundLayer: typing.ClassVar[QGraphicsScene.SceneLayer]  # value = <SceneLayer.ForegroundLayer: 4>
        ItemLayer: typing.ClassVar[QGraphicsScene.SceneLayer]  # value = <SceneLayer.ItemLayer: 1>
    @staticmethod
    def activePanel(*args, **kwargs):
        ...
    @staticmethod
    def activeWindow(*args, **kwargs):
        ...
    @staticmethod
    def addEllipse(*args, **kwargs):
        ...
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addLine(*args, **kwargs):
        ...
    @staticmethod
    def addPath(*args, **kwargs):
        ...
    @staticmethod
    def addPixmap(*args, **kwargs):
        ...
    @staticmethod
    def addPolygon(*args, **kwargs):
        ...
    @staticmethod
    def addRect(*args, **kwargs):
        ...
    @staticmethod
    def addSimpleText(*args, **kwargs):
        ...
    @staticmethod
    def addText(*args, **kwargs):
        ...
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def advance(*args, **kwargs):
        ...
    @staticmethod
    def backgroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def bspTreeDepth(*args, **kwargs):
        ...
    @staticmethod
    def changed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearFocus(*args, **kwargs):
        ...
    @staticmethod
    def clearSelection(*args, **kwargs):
        ...
    @staticmethod
    def collidingItems(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def createItemGroup(*args, **kwargs):
        ...
    @staticmethod
    def destroyItemGroup(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def drawBackground(*args, **kwargs):
        ...
    @staticmethod
    def drawForeground(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusItem(*args, **kwargs):
        ...
    @staticmethod
    def focusItemChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOnTouch(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def foregroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def hasFocus(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def helpEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def itemIndexMethod(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def itemsBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def minimumRenderSize(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseGrabberItem(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def palette(*args, **kwargs):
        ...
    @staticmethod
    def removeItem(*args, **kwargs):
        ...
    @staticmethod
    def render(*args, **kwargs):
        ...
    @staticmethod
    def sceneRect(*args, **kwargs):
        ...
    @staticmethod
    def sceneRectChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def selectedItems(*args, **kwargs):
        ...
    @staticmethod
    def selectionArea(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sendEvent(*args, **kwargs):
        ...
    @staticmethod
    def setActivePanel(*args, **kwargs):
        ...
    @staticmethod
    def setActiveWindow(*args, **kwargs):
        ...
    @staticmethod
    def setBackgroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def setBspTreeDepth(*args, **kwargs):
        ...
    @staticmethod
    def setFocus(*args, **kwargs):
        ...
    @staticmethod
    def setFocusItem(*args, **kwargs):
        ...
    @staticmethod
    def setFocusOnTouch(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setForegroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def setItemIndexMethod(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumRenderSize(*args, **kwargs):
        ...
    @staticmethod
    def setPalette(*args, **kwargs):
        ...
    @staticmethod
    def setSceneRect(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionArea(*args, **kwargs):
        ...
    @staticmethod
    def setStickyFocus(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def stickyFocus(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def views(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
class QGraphicsSceneContextMenuEvent(QGraphicsSceneEvent):
    class Reason(enum.Enum):
        Keyboard: typing.ClassVar[QGraphicsSceneContextMenuEvent.Reason]  # value = <Reason.Keyboard: 1>
        Mouse: typing.ClassVar[QGraphicsSceneContextMenuEvent.Reason]  # value = <Reason.Mouse: 0>
        Other: typing.ClassVar[QGraphicsSceneContextMenuEvent.Reason]  # value = <Reason.Other: 2>
    @staticmethod
    def modifiers(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def reason(*args, **kwargs):
        ...
    @staticmethod
    def scenePos(*args, **kwargs):
        ...
    @staticmethod
    def screenPos(*args, **kwargs):
        ...
class QGraphicsSceneDragDropEvent(QGraphicsSceneEvent):
    @staticmethod
    def acceptProposedAction(*args, **kwargs):
        ...
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def dropAction(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def modifiers(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def possibleActions(*args, **kwargs):
        ...
    @staticmethod
    def proposedAction(*args, **kwargs):
        ...
    @staticmethod
    def scenePos(*args, **kwargs):
        ...
    @staticmethod
    def screenPos(*args, **kwargs):
        ...
    @staticmethod
    def setDropAction(*args, **kwargs):
        ...
    @staticmethod
    def source(*args, **kwargs):
        ...
class QGraphicsSceneEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def timestamp(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
class QGraphicsSceneHelpEvent(QGraphicsSceneEvent):
    @staticmethod
    def scenePos(*args, **kwargs):
        ...
    @staticmethod
    def screenPos(*args, **kwargs):
        ...
class QGraphicsSceneHoverEvent(QGraphicsSceneEvent):
    @staticmethod
    def lastPos(*args, **kwargs):
        ...
    @staticmethod
    def lastScenePos(*args, **kwargs):
        ...
    @staticmethod
    def lastScreenPos(*args, **kwargs):
        ...
    @staticmethod
    def modifiers(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def scenePos(*args, **kwargs):
        ...
    @staticmethod
    def screenPos(*args, **kwargs):
        ...
class QGraphicsSceneMouseEvent(QGraphicsSceneEvent):
    @staticmethod
    def button(*args, **kwargs):
        ...
    @staticmethod
    def buttonDownPos(*args, **kwargs):
        ...
    @staticmethod
    def buttonDownScenePos(*args, **kwargs):
        ...
    @staticmethod
    def buttonDownScreenPos(*args, **kwargs):
        ...
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def lastPos(*args, **kwargs):
        ...
    @staticmethod
    def lastScenePos(*args, **kwargs):
        ...
    @staticmethod
    def lastScreenPos(*args, **kwargs):
        ...
    @staticmethod
    def modifiers(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def scenePos(*args, **kwargs):
        ...
    @staticmethod
    def screenPos(*args, **kwargs):
        ...
    @staticmethod
    def source(*args, **kwargs):
        ...
class QGraphicsSceneMoveEvent(QGraphicsSceneEvent):
    @staticmethod
    def newPos(*args, **kwargs):
        ...
    @staticmethod
    def oldPos(*args, **kwargs):
        ...
class QGraphicsSceneResizeEvent(QGraphicsSceneEvent):
    @staticmethod
    def newSize(*args, **kwargs):
        ...
    @staticmethod
    def oldSize(*args, **kwargs):
        ...
class QGraphicsSceneWheelEvent(QGraphicsSceneEvent):
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def delta(*args, **kwargs):
        ...
    @staticmethod
    def isInverted(*args, **kwargs):
        ...
    @staticmethod
    def modifiers(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def phase(*args, **kwargs):
        ...
    @staticmethod
    def pixelDelta(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def scenePos(*args, **kwargs):
        ...
    @staticmethod
    def screenPos(*args, **kwargs):
        ...
class QGraphicsSimpleTextItem(QAbstractGraphicsShapeItem):
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsTextItem(QGraphicsObject):
    @staticmethod
    def adjustSize(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def defaultTextColor(*args, **kwargs):
        ...
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def hoverEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def isObscuredBy(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def linkActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def linkHovered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def opaqueArea(*args, **kwargs):
        ...
    @staticmethod
    def openExternalLinks(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def sceneEvent(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultTextColor(*args, **kwargs):
        ...
    @staticmethod
    def setDocument(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setHtml(*args, **kwargs):
        ...
    @staticmethod
    def setOpenExternalLinks(*args, **kwargs):
        ...
    @staticmethod
    def setPlainText(*args, **kwargs):
        ...
    @staticmethod
    def setTabChangesFocus(*args, **kwargs):
        ...
    @staticmethod
    def setTextCursor(*args, **kwargs):
        ...
    @staticmethod
    def setTextInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def setTextWidth(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def tabChangesFocus(*args, **kwargs):
        ...
    @staticmethod
    def textCursor(*args, **kwargs):
        ...
    @staticmethod
    def textInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def textWidth(*args, **kwargs):
        ...
    @staticmethod
    def toHtml(*args, **kwargs):
        ...
    @staticmethod
    def toPlainText(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QGraphicsTransform(PyQt6.QtCore.QObject):
    @staticmethod
    def applyTo(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
class QGraphicsView(QAbstractScrollArea):
    class CacheModeFlag(enum.Flag):
        CacheBackground: typing.ClassVar[QGraphicsView.CacheModeFlag]  # value = <CacheModeFlag.CacheBackground: 1>
    class DragMode(enum.Enum):
        NoDrag: typing.ClassVar[QGraphicsView.DragMode]  # value = <DragMode.NoDrag: 0>
        RubberBandDrag: typing.ClassVar[QGraphicsView.DragMode]  # value = <DragMode.RubberBandDrag: 2>
        ScrollHandDrag: typing.ClassVar[QGraphicsView.DragMode]  # value = <DragMode.ScrollHandDrag: 1>
    class OptimizationFlag(enum.Flag):
        DontAdjustForAntialiasing: typing.ClassVar[QGraphicsView.OptimizationFlag]  # value = <OptimizationFlag.DontAdjustForAntialiasing: 2>
        DontSavePainterState: typing.ClassVar[QGraphicsView.OptimizationFlag]  # value = <OptimizationFlag.DontSavePainterState: 1>
    class ViewportAnchor(enum.Enum):
        AnchorUnderMouse: typing.ClassVar[QGraphicsView.ViewportAnchor]  # value = <ViewportAnchor.AnchorUnderMouse: 2>
        AnchorViewCenter: typing.ClassVar[QGraphicsView.ViewportAnchor]  # value = <ViewportAnchor.AnchorViewCenter: 1>
        NoAnchor: typing.ClassVar[QGraphicsView.ViewportAnchor]  # value = <ViewportAnchor.NoAnchor: 0>
    class ViewportUpdateMode(enum.Enum):
        BoundingRectViewportUpdate: typing.ClassVar[QGraphicsView.ViewportUpdateMode]  # value = <ViewportUpdateMode.BoundingRectViewportUpdate: 4>
        FullViewportUpdate: typing.ClassVar[QGraphicsView.ViewportUpdateMode]  # value = <ViewportUpdateMode.FullViewportUpdate: 0>
        MinimalViewportUpdate: typing.ClassVar[QGraphicsView.ViewportUpdateMode]  # value = <ViewportUpdateMode.MinimalViewportUpdate: 1>
        NoViewportUpdate: typing.ClassVar[QGraphicsView.ViewportUpdateMode]  # value = <ViewportUpdateMode.NoViewportUpdate: 3>
        SmartViewportUpdate: typing.ClassVar[QGraphicsView.ViewportUpdateMode]  # value = <ViewportUpdateMode.SmartViewportUpdate: 2>
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def backgroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def cacheMode(*args, **kwargs):
        ...
    @staticmethod
    def centerOn(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMode(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def drawBackground(*args, **kwargs):
        ...
    @staticmethod
    def drawForeground(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def ensureVisible(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def fitInView(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def foregroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def invalidateScene(*args, **kwargs):
        ...
    @staticmethod
    def isInteractive(*args, **kwargs):
        ...
    @staticmethod
    def isTransformed(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def mapFromScene(*args, **kwargs):
        ...
    @staticmethod
    def mapToScene(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def optimizationFlags(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def render(*args, **kwargs):
        ...
    @staticmethod
    def renderHints(*args, **kwargs):
        ...
    @staticmethod
    def resetCachedContent(*args, **kwargs):
        ...
    @staticmethod
    def resetTransform(*args, **kwargs):
        ...
    @staticmethod
    def resizeAnchor(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def rotate(*args, **kwargs):
        ...
    @staticmethod
    def rubberBandChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rubberBandRect(*args, **kwargs):
        ...
    @staticmethod
    def rubberBandSelectionMode(*args, **kwargs):
        ...
    @staticmethod
    def scale(*args, **kwargs):
        ...
    @staticmethod
    def scene(*args, **kwargs):
        ...
    @staticmethod
    def sceneRect(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setBackgroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def setCacheMode(*args, **kwargs):
        ...
    @staticmethod
    def setDragMode(*args, **kwargs):
        ...
    @staticmethod
    def setForegroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def setInteractive(*args, **kwargs):
        ...
    @staticmethod
    def setOptimizationFlag(*args, **kwargs):
        ...
    @staticmethod
    def setOptimizationFlags(*args, **kwargs):
        ...
    @staticmethod
    def setRenderHint(*args, **kwargs):
        ...
    @staticmethod
    def setRenderHints(*args, **kwargs):
        ...
    @staticmethod
    def setResizeAnchor(*args, **kwargs):
        ...
    @staticmethod
    def setRubberBandSelectionMode(*args, **kwargs):
        ...
    @staticmethod
    def setScene(*args, **kwargs):
        ...
    @staticmethod
    def setSceneRect(*args, **kwargs):
        ...
    @staticmethod
    def setTransform(*args, **kwargs):
        ...
    @staticmethod
    def setTransformationAnchor(*args, **kwargs):
        ...
    @staticmethod
    def setViewportUpdateMode(*args, **kwargs):
        ...
    @staticmethod
    def setupViewport(*args, **kwargs):
        ...
    @staticmethod
    def shear(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def transform(*args, **kwargs):
        ...
    @staticmethod
    def transformationAnchor(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def updateScene(*args, **kwargs):
        ...
    @staticmethod
    def updateSceneRect(*args, **kwargs):
        ...
    @staticmethod
    def viewportEvent(*args, **kwargs):
        ...
    @staticmethod
    def viewportTransform(*args, **kwargs):
        ...
    @staticmethod
    def viewportUpdateMode(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
class QGraphicsWidget(QGraphicsObject, QGraphicsLayoutItem):
    @staticmethod
    def actions(*args, **kwargs):
        ...
    @staticmethod
    def addAction(*args, **kwargs):
        ...
    @staticmethod
    def addActions(*args, **kwargs):
        ...
    @staticmethod
    def adjustSize(*args, **kwargs):
        ...
    @staticmethod
    def autoFillBackground(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusPolicy(*args, **kwargs):
        ...
    @staticmethod
    def focusWidget(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def geometryChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def getContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def getWindowFrameMargins(*args, **kwargs):
        ...
    @staticmethod
    def grabKeyboardEvent(*args, **kwargs):
        ...
    @staticmethod
    def grabMouseEvent(*args, **kwargs):
        ...
    @staticmethod
    def grabShortcut(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def hoverMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def insertAction(*args, **kwargs):
        ...
    @staticmethod
    def insertActions(*args, **kwargs):
        ...
    @staticmethod
    def isActiveWindow(*args, **kwargs):
        ...
    @staticmethod
    def itemChange(*args, **kwargs):
        ...
    @staticmethod
    def layout(*args, **kwargs):
        ...
    @staticmethod
    def layoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def moveEvent(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def paintWindowFrame(*args, **kwargs):
        ...
    @staticmethod
    def palette(*args, **kwargs):
        ...
    @staticmethod
    def polishEvent(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def releaseShortcut(*args, **kwargs):
        ...
    @staticmethod
    def removeAction(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def sceneEvent(*args, **kwargs):
        ...
    @staticmethod
    def setAttribute(*args, **kwargs):
        ...
    @staticmethod
    def setAutoFillBackground(*args, **kwargs):
        ...
    @staticmethod
    def setContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def setFocusPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setLayout(*args, **kwargs):
        ...
    @staticmethod
    def setLayoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def setPalette(*args, **kwargs):
        ...
    @staticmethod
    def setShortcutAutoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def setShortcutEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def setTabOrder(*args, **kwargs):
        ...
    @staticmethod
    def setWindowFlags(*args, **kwargs):
        ...
    @staticmethod
    def setWindowFrameMargins(*args, **kwargs):
        ...
    @staticmethod
    def setWindowTitle(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def testAttribute(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def ungrabKeyboardEvent(*args, **kwargs):
        ...
    @staticmethod
    def ungrabMouseEvent(*args, **kwargs):
        ...
    @staticmethod
    def unsetLayoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def unsetWindowFrameMargins(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometry(*args, **kwargs):
        ...
    @staticmethod
    def windowFlags(*args, **kwargs):
        ...
    @staticmethod
    def windowFrameEvent(*args, **kwargs):
        ...
    @staticmethod
    def windowFrameGeometry(*args, **kwargs):
        ...
    @staticmethod
    def windowFrameRect(*args, **kwargs):
        ...
    @staticmethod
    def windowFrameSectionAt(*args, **kwargs):
        ...
    @staticmethod
    def windowTitle(*args, **kwargs):
        ...
    @staticmethod
    def windowType(*args, **kwargs):
        ...
class QGridLayout(QLayout):
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addLayout(*args, **kwargs):
        ...
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def cellRect(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def columnMinimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def columnStretch(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def getItemPosition(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def horizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def itemAtPosition(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def originCorner(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def rowMinimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def rowStretch(*args, **kwargs):
        ...
    @staticmethod
    def setColumnMinimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def setColumnStretch(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultPositioning(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setOriginCorner(*args, **kwargs):
        ...
    @staticmethod
    def setRowMinimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def setRowStretch(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalSpacing(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def spacing(*args, **kwargs):
        ...
    @staticmethod
    def takeAt(*args, **kwargs):
        ...
    @staticmethod
    def verticalSpacing(*args, **kwargs):
        ...
class QGroupBox(QWidget):
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def childEvent(*args, **kwargs):
        ...
    @staticmethod
    def clicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def isCheckable(*args, **kwargs):
        ...
    @staticmethod
    def isChecked(*args, **kwargs):
        ...
    @staticmethod
    def isFlat(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setCheckable(*args, **kwargs):
        ...
    @staticmethod
    def setChecked(*args, **kwargs):
        ...
    @staticmethod
    def setFlat(*args, **kwargs):
        ...
    @staticmethod
    def setTitle(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
    @staticmethod
    def toggled(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QHBoxLayout(QBoxLayout):
    pass
class QHeaderView(QAbstractItemView):
    class ResizeMode(enum.Enum):
        Fixed: typing.ClassVar[QHeaderView.ResizeMode]  # value = <ResizeMode.Fixed: 2>
        Interactive: typing.ClassVar[QHeaderView.ResizeMode]  # value = <ResizeMode.Interactive: 0>
        ResizeToContents: typing.ClassVar[QHeaderView.ResizeMode]  # value = <ResizeMode.ResizeToContents: 3>
        Stretch: typing.ClassVar[QHeaderView.ResizeMode]  # value = <ResizeMode.Stretch: 1>
    @staticmethod
    def cascadingSectionResizes(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        ...
    @staticmethod
    def dataChanged(*args, **kwargs):
        ...
    @staticmethod
    def defaultAlignment(*args, **kwargs):
        ...
    @staticmethod
    def defaultSectionSize(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def geometriesChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def headerDataChanged(*args, **kwargs):
        ...
    @staticmethod
    def hiddenSectionCount(*args, **kwargs):
        ...
    @staticmethod
    def hideSection(*args, **kwargs):
        ...
    @staticmethod
    def highlightSections(*args, **kwargs):
        ...
    @staticmethod
    def horizontalOffset(*args, **kwargs):
        ...
    @staticmethod
    def indexAt(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOptionForIndex(*args, **kwargs):
        ...
    @staticmethod
    def initialize(*args, **kwargs):
        ...
    @staticmethod
    def initializeSections(*args, **kwargs):
        ...
    @staticmethod
    def isFirstSectionMovable(*args, **kwargs):
        ...
    @staticmethod
    def isIndexHidden(*args, **kwargs):
        ...
    @staticmethod
    def isSectionHidden(*args, **kwargs):
        ...
    @staticmethod
    def isSortIndicatorClearable(*args, **kwargs):
        ...
    @staticmethod
    def isSortIndicatorShown(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def logicalIndex(*args, **kwargs):
        ...
    @staticmethod
    def logicalIndexAt(*args, **kwargs):
        ...
    @staticmethod
    def maximumSectionSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumSectionSize(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def moveSection(*args, **kwargs):
        ...
    @staticmethod
    def offset(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintSection(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def resetDefaultSectionSize(*args, **kwargs):
        ...
    @staticmethod
    def resizeContentsPrecision(*args, **kwargs):
        ...
    @staticmethod
    def resizeSection(*args, **kwargs):
        ...
    @staticmethod
    def resizeSections(*args, **kwargs):
        ...
    @staticmethod
    def restoreState(*args, **kwargs):
        ...
    @staticmethod
    def rowsInserted(*args, **kwargs):
        ...
    @staticmethod
    def saveState(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def scrollTo(*args, **kwargs):
        ...
    @staticmethod
    def sectionClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionCountChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionHandleDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionPosition(*args, **kwargs):
        ...
    @staticmethod
    def sectionPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionResizeMode(*args, **kwargs):
        ...
    @staticmethod
    def sectionResized(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sectionSize(*args, **kwargs):
        ...
    @staticmethod
    def sectionSizeFromContents(*args, **kwargs):
        ...
    @staticmethod
    def sectionSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sectionViewportPosition(*args, **kwargs):
        ...
    @staticmethod
    def sectionsAboutToBeRemoved(*args, **kwargs):
        ...
    @staticmethod
    def sectionsClickable(*args, **kwargs):
        ...
    @staticmethod
    def sectionsHidden(*args, **kwargs):
        ...
    @staticmethod
    def sectionsInserted(*args, **kwargs):
        ...
    @staticmethod
    def sectionsMovable(*args, **kwargs):
        ...
    @staticmethod
    def sectionsMoved(*args, **kwargs):
        ...
    @staticmethod
    def setCascadingSectionResizes(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultSectionSize(*args, **kwargs):
        ...
    @staticmethod
    def setFirstSectionMovable(*args, **kwargs):
        ...
    @staticmethod
    def setHighlightSections(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumSectionSize(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumSectionSize(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setOffset(*args, **kwargs):
        ...
    @staticmethod
    def setOffsetToLastSection(*args, **kwargs):
        ...
    @staticmethod
    def setOffsetToSectionPosition(*args, **kwargs):
        ...
    @staticmethod
    def setResizeContentsPrecision(*args, **kwargs):
        ...
    @staticmethod
    def setSectionHidden(*args, **kwargs):
        ...
    @staticmethod
    def setSectionResizeMode(*args, **kwargs):
        ...
    @staticmethod
    def setSectionsClickable(*args, **kwargs):
        ...
    @staticmethod
    def setSectionsMovable(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setSortIndicator(*args, **kwargs):
        ...
    @staticmethod
    def setSortIndicatorClearable(*args, **kwargs):
        ...
    @staticmethod
    def setSortIndicatorShown(*args, **kwargs):
        ...
    @staticmethod
    def setStretchLastSection(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def showSection(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sortIndicatorChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sortIndicatorClearableChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sortIndicatorOrder(*args, **kwargs):
        ...
    @staticmethod
    def sortIndicatorSection(*args, **kwargs):
        ...
    @staticmethod
    def stretchLastSection(*args, **kwargs):
        ...
    @staticmethod
    def stretchSectionCount(*args, **kwargs):
        ...
    @staticmethod
    def swapSections(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometries(*args, **kwargs):
        ...
    @staticmethod
    def updateSection(*args, **kwargs):
        ...
    @staticmethod
    def verticalOffset(*args, **kwargs):
        ...
    @staticmethod
    def viewportEvent(*args, **kwargs):
        ...
    @staticmethod
    def visualIndex(*args, **kwargs):
        ...
    @staticmethod
    def visualIndexAt(*args, **kwargs):
        ...
    @staticmethod
    def visualRect(*args, **kwargs):
        ...
    @staticmethod
    def visualRegionForSelection(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QInputDialog(QDialog):
    class InputDialogOption(enum.Flag):
        NoButtons: typing.ClassVar[QInputDialog.InputDialogOption]  # value = <InputDialogOption.NoButtons: 1>
        UseListViewForComboBoxItems: typing.ClassVar[QInputDialog.InputDialogOption]  # value = <InputDialogOption.UseListViewForComboBoxItems: 2>
        UsePlainTextEditForTextInput: typing.ClassVar[QInputDialog.InputDialogOption]  # value = <InputDialogOption.UsePlainTextEditForTextInput: 4>
    class InputMode(enum.Enum):
        DoubleInput: typing.ClassVar[QInputDialog.InputMode]  # value = <InputMode.DoubleInput: 2>
        IntInput: typing.ClassVar[QInputDialog.InputMode]  # value = <InputMode.IntInput: 1>
        TextInput: typing.ClassVar[QInputDialog.InputMode]  # value = <InputMode.TextInput: 0>
    @staticmethod
    def cancelButtonText(*args, **kwargs):
        ...
    @staticmethod
    def comboBoxItems(*args, **kwargs):
        ...
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def doubleDecimals(*args, **kwargs):
        ...
    @staticmethod
    def doubleMaximum(*args, **kwargs):
        ...
    @staticmethod
    def doubleMinimum(*args, **kwargs):
        ...
    @staticmethod
    def doubleStep(*args, **kwargs):
        ...
    @staticmethod
    def doubleValue(*args, **kwargs):
        ...
    @staticmethod
    def doubleValueChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def doubleValueSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def getDouble(*args, **kwargs):
        ...
    @staticmethod
    def getInt(*args, **kwargs):
        ...
    @staticmethod
    def getItem(*args, **kwargs):
        ...
    @staticmethod
    def getMultiLineText(*args, **kwargs):
        ...
    @staticmethod
    def getText(*args, **kwargs):
        ...
    @staticmethod
    def inputMode(*args, **kwargs):
        ...
    @staticmethod
    def intMaximum(*args, **kwargs):
        ...
    @staticmethod
    def intMinimum(*args, **kwargs):
        ...
    @staticmethod
    def intStep(*args, **kwargs):
        ...
    @staticmethod
    def intValue(*args, **kwargs):
        ...
    @staticmethod
    def intValueChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def intValueSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def isComboBoxEditable(*args, **kwargs):
        ...
    @staticmethod
    def labelText(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def okButtonText(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def setCancelButtonText(*args, **kwargs):
        ...
    @staticmethod
    def setComboBoxEditable(*args, **kwargs):
        ...
    @staticmethod
    def setComboBoxItems(*args, **kwargs):
        ...
    @staticmethod
    def setDoubleDecimals(*args, **kwargs):
        ...
    @staticmethod
    def setDoubleMaximum(*args, **kwargs):
        ...
    @staticmethod
    def setDoubleMinimum(*args, **kwargs):
        ...
    @staticmethod
    def setDoubleRange(*args, **kwargs):
        ...
    @staticmethod
    def setDoubleStep(*args, **kwargs):
        ...
    @staticmethod
    def setDoubleValue(*args, **kwargs):
        ...
    @staticmethod
    def setInputMode(*args, **kwargs):
        ...
    @staticmethod
    def setIntMaximum(*args, **kwargs):
        ...
    @staticmethod
    def setIntMinimum(*args, **kwargs):
        ...
    @staticmethod
    def setIntRange(*args, **kwargs):
        ...
    @staticmethod
    def setIntStep(*args, **kwargs):
        ...
    @staticmethod
    def setIntValue(*args, **kwargs):
        ...
    @staticmethod
    def setLabelText(*args, **kwargs):
        ...
    @staticmethod
    def setOkButtonText(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setTextEchoMode(*args, **kwargs):
        ...
    @staticmethod
    def setTextValue(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def textEchoMode(*args, **kwargs):
        ...
    @staticmethod
    def textValue(*args, **kwargs):
        ...
    @staticmethod
    def textValueChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textValueSelected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QItemDelegate(QAbstractItemDelegate):
    @staticmethod
    def createEditor(*args, **kwargs):
        ...
    @staticmethod
    def drawBackground(*args, **kwargs):
        ...
    @staticmethod
    def drawCheck(*args, **kwargs):
        ...
    @staticmethod
    def drawDecoration(*args, **kwargs):
        ...
    @staticmethod
    def drawDisplay(*args, **kwargs):
        ...
    @staticmethod
    def drawFocus(*args, **kwargs):
        ...
    @staticmethod
    def editorEvent(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def hasClipping(*args, **kwargs):
        ...
    @staticmethod
    def itemEditorFactory(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def setClipping(*args, **kwargs):
        ...
    @staticmethod
    def setEditorData(*args, **kwargs):
        ...
    @staticmethod
    def setItemEditorFactory(*args, **kwargs):
        ...
    @staticmethod
    def setModelData(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def updateEditorGeometry(*args, **kwargs):
        ...
class QItemEditorCreatorBase(PyQt6.sip.wrapper):
    @staticmethod
    def createWidget(*args, **kwargs):
        ...
    @staticmethod
    def valuePropertyName(*args, **kwargs):
        ...
class QItemEditorFactory(PyQt6.sip.wrapper):
    @staticmethod
    def createEditor(*args, **kwargs):
        ...
    @staticmethod
    def defaultFactory(*args, **kwargs):
        ...
    @staticmethod
    def registerEditor(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultFactory(*args, **kwargs):
        ...
    @staticmethod
    def valuePropertyName(*args, **kwargs):
        ...
class QKeySequenceEdit(QWidget):
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def editingFinished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def finishingKeyCombinations(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def isClearButtonEnabled(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def keySequence(*args, **kwargs):
        ...
    @staticmethod
    def keySequenceChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def maximumSequenceLength(*args, **kwargs):
        ...
    @staticmethod
    def setClearButtonEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setFinishingKeyCombinations(*args, **kwargs):
        ...
    @staticmethod
    def setKeySequence(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumSequenceLength(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
class QLCDNumber(QFrame):
    class Mode(enum.Enum):
        Bin: typing.ClassVar[QLCDNumber.Mode]  # value = <Mode.Bin: 3>
        Dec: typing.ClassVar[QLCDNumber.Mode]  # value = <Mode.Dec: 1>
        Hex: typing.ClassVar[QLCDNumber.Mode]  # value = <Mode.Hex: 0>
        Oct: typing.ClassVar[QLCDNumber.Mode]  # value = <Mode.Oct: 2>
    class SegmentStyle(enum.Enum):
        Filled: typing.ClassVar[QLCDNumber.SegmentStyle]  # value = <SegmentStyle.Filled: 1>
        Flat: typing.ClassVar[QLCDNumber.SegmentStyle]  # value = <SegmentStyle.Flat: 2>
        Outline: typing.ClassVar[QLCDNumber.SegmentStyle]  # value = <SegmentStyle.Outline: 0>
    @staticmethod
    def checkOverflow(*args, **kwargs):
        ...
    @staticmethod
    def digitCount(*args, **kwargs):
        ...
    @staticmethod
    def display(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def intValue(*args, **kwargs):
        ...
    @staticmethod
    def mode(*args, **kwargs):
        ...
    @staticmethod
    def overflow(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def segmentStyle(*args, **kwargs):
        ...
    @staticmethod
    def setBinMode(*args, **kwargs):
        ...
    @staticmethod
    def setDecMode(*args, **kwargs):
        ...
    @staticmethod
    def setDigitCount(*args, **kwargs):
        ...
    @staticmethod
    def setHexMode(*args, **kwargs):
        ...
    @staticmethod
    def setMode(*args, **kwargs):
        ...
    @staticmethod
    def setNumDigits(*args, **kwargs):
        ...
    @staticmethod
    def setOctMode(*args, **kwargs):
        ...
    @staticmethod
    def setSegmentStyle(*args, **kwargs):
        ...
    @staticmethod
    def setSmallDecimalPoint(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def smallDecimalPoint(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QLabel(QFrame):
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def buddy(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def hasScaledContents(*args, **kwargs):
        ...
    @staticmethod
    def hasSelectedText(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def indent(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def linkActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def linkHovered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def margin(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def movie(*args, **kwargs):
        ...
    @staticmethod
    def openExternalLinks(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def picture(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def resourceProvider(*args, **kwargs):
        ...
    @staticmethod
    def selectedText(*args, **kwargs):
        ...
    @staticmethod
    def selectionStart(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setBuddy(*args, **kwargs):
        ...
    @staticmethod
    def setIndent(*args, **kwargs):
        ...
    @staticmethod
    def setMargin(*args, **kwargs):
        ...
    @staticmethod
    def setMovie(*args, **kwargs):
        ...
    @staticmethod
    def setNum(*args, **kwargs):
        ...
    @staticmethod
    def setOpenExternalLinks(*args, **kwargs):
        ...
    @staticmethod
    def setPicture(*args, **kwargs):
        ...
    @staticmethod
    def setPixmap(*args, **kwargs):
        ...
    @staticmethod
    def setResourceProvider(*args, **kwargs):
        ...
    @staticmethod
    def setScaledContents(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def setTextInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def setWordWrap(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textFormat(*args, **kwargs):
        ...
    @staticmethod
    def textInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def wordWrap(*args, **kwargs):
        ...
class QLayout(PyQt6.QtCore.QObject, QLayoutItem):
    class SizeConstraint(enum.Enum):
        SetDefaultConstraint: typing.ClassVar[QLayout.SizeConstraint]  # value = <SizeConstraint.SetDefaultConstraint: 0>
        SetFixedSize: typing.ClassVar[QLayout.SizeConstraint]  # value = <SizeConstraint.SetFixedSize: 3>
        SetMaximumSize: typing.ClassVar[QLayout.SizeConstraint]  # value = <SizeConstraint.SetMaximumSize: 4>
        SetMinAndMaxSize: typing.ClassVar[QLayout.SizeConstraint]  # value = <SizeConstraint.SetMinAndMaxSize: 5>
        SetMinimumSize: typing.ClassVar[QLayout.SizeConstraint]  # value = <SizeConstraint.SetMinimumSize: 2>
        SetNoConstraint: typing.ClassVar[QLayout.SizeConstraint]  # value = <SizeConstraint.SetNoConstraint: 1>
    @staticmethod
    def activate(*args, **kwargs):
        ...
    @staticmethod
    def addChildLayout(*args, **kwargs):
        ...
    @staticmethod
    def addChildWidget(*args, **kwargs):
        ...
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def alignmentRect(*args, **kwargs):
        ...
    @staticmethod
    def childEvent(*args, **kwargs):
        ...
    @staticmethod
    def closestAcceptableSize(*args, **kwargs):
        ...
    @staticmethod
    def contentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def contentsRect(*args, **kwargs):
        ...
    @staticmethod
    def controlTypes(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def getContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def layout(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def menuBar(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def parentWidget(*args, **kwargs):
        ...
    @staticmethod
    def removeItem(*args, **kwargs):
        ...
    @staticmethod
    def removeWidget(*args, **kwargs):
        ...
    @staticmethod
    def replaceWidget(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setMenuBar(*args, **kwargs):
        ...
    @staticmethod
    def setSizeConstraint(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def sizeConstraint(*args, **kwargs):
        ...
    @staticmethod
    def spacing(*args, **kwargs):
        ...
    @staticmethod
    def takeAt(*args, **kwargs):
        ...
    @staticmethod
    def totalHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def totalMaximumSize(*args, **kwargs):
        ...
    @staticmethod
    def totalMinimumSize(*args, **kwargs):
        ...
    @staticmethod
    def totalSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def unsetContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def widgetEvent(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QLayoutItem(PyQt6.sip.wrapper):
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def controlTypes(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def layout(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def spacerItem(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
class QLineEdit(QWidget):
    class ActionPosition(enum.Enum):
        LeadingPosition: typing.ClassVar[QLineEdit.ActionPosition]  # value = <ActionPosition.LeadingPosition: 0>
        TrailingPosition: typing.ClassVar[QLineEdit.ActionPosition]  # value = <ActionPosition.TrailingPosition: 1>
    class EchoMode(enum.Enum):
        NoEcho: typing.ClassVar[QLineEdit.EchoMode]  # value = <EchoMode.NoEcho: 1>
        Normal: typing.ClassVar[QLineEdit.EchoMode]  # value = <EchoMode.Normal: 0>
        Password: typing.ClassVar[QLineEdit.EchoMode]  # value = <EchoMode.Password: 2>
        PasswordEchoOnEdit: typing.ClassVar[QLineEdit.EchoMode]  # value = <EchoMode.PasswordEchoOnEdit: 3>
    @staticmethod
    def addAction(*args, **kwargs):
        ...
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def backspace(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def completer(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def createStandardContextMenu(*args, **kwargs):
        ...
    @staticmethod
    def cursorBackward(*args, **kwargs):
        ...
    @staticmethod
    def cursorForward(*args, **kwargs):
        ...
    @staticmethod
    def cursorMoveStyle(*args, **kwargs):
        ...
    @staticmethod
    def cursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def cursorPositionAt(*args, **kwargs):
        ...
    @staticmethod
    def cursorPositionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cursorRect(*args, **kwargs):
        ...
    @staticmethod
    def cursorWordBackward(*args, **kwargs):
        ...
    @staticmethod
    def cursorWordForward(*args, **kwargs):
        ...
    @staticmethod
    def cut(*args, **kwargs):
        ...
    @staticmethod
    def del_(*args, **kwargs):
        ...
    @staticmethod
    def deselect(*args, **kwargs):
        ...
    @staticmethod
    def displayText(*args, **kwargs):
        ...
    @staticmethod
    def dragEnabled(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def echoMode(*args, **kwargs):
        ...
    @staticmethod
    def editingFinished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def end(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def hasAcceptableInput(*args, **kwargs):
        ...
    @staticmethod
    def hasFrame(*args, **kwargs):
        ...
    @staticmethod
    def hasSelectedText(*args, **kwargs):
        ...
    @staticmethod
    def home(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def inputMask(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def inputRejected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def isClearButtonEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isModified(*args, **kwargs):
        ...
    @staticmethod
    def isReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def isRedoAvailable(*args, **kwargs):
        ...
    @staticmethod
    def isUndoAvailable(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def maxLength(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def paste(*args, **kwargs):
        ...
    @staticmethod
    def placeholderText(*args, **kwargs):
        ...
    @staticmethod
    def redo(*args, **kwargs):
        ...
    @staticmethod
    def returnPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def selectAll(*args, **kwargs):
        ...
    @staticmethod
    def selectedText(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def selectionEnd(*args, **kwargs):
        ...
    @staticmethod
    def selectionLength(*args, **kwargs):
        ...
    @staticmethod
    def selectionStart(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setClearButtonEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setCompleter(*args, **kwargs):
        ...
    @staticmethod
    def setCursorMoveStyle(*args, **kwargs):
        ...
    @staticmethod
    def setCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def setDragEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setEchoMode(*args, **kwargs):
        ...
    @staticmethod
    def setFrame(*args, **kwargs):
        ...
    @staticmethod
    def setInputMask(*args, **kwargs):
        ...
    @staticmethod
    def setMaxLength(*args, **kwargs):
        ...
    @staticmethod
    def setModified(*args, **kwargs):
        ...
    @staticmethod
    def setPlaceholderText(*args, **kwargs):
        ...
    @staticmethod
    def setReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextMargins(*args, **kwargs):
        ...
    @staticmethod
    def setValidator(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textEdited(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textMargins(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def undo(*args, **kwargs):
        ...
    @staticmethod
    def validator(*args, **kwargs):
        ...
class QListView(QAbstractItemView):
    class Flow(enum.Enum):
        LeftToRight: typing.ClassVar[QListView.Flow]  # value = <Flow.LeftToRight: 0>
        TopToBottom: typing.ClassVar[QListView.Flow]  # value = <Flow.TopToBottom: 1>
    class LayoutMode(enum.Enum):
        Batched: typing.ClassVar[QListView.LayoutMode]  # value = <LayoutMode.Batched: 1>
        SinglePass: typing.ClassVar[QListView.LayoutMode]  # value = <LayoutMode.SinglePass: 0>
    class Movement(enum.Enum):
        Free: typing.ClassVar[QListView.Movement]  # value = <Movement.Free: 1>
        Snap: typing.ClassVar[QListView.Movement]  # value = <Movement.Snap: 2>
        Static: typing.ClassVar[QListView.Movement]  # value = <Movement.Static: 0>
    class ResizeMode(enum.Enum):
        Adjust: typing.ClassVar[QListView.ResizeMode]  # value = <ResizeMode.Adjust: 1>
        Fixed: typing.ClassVar[QListView.ResizeMode]  # value = <ResizeMode.Fixed: 0>
    class ViewMode(enum.Enum):
        IconMode: typing.ClassVar[QListView.ViewMode]  # value = <ViewMode.IconMode: 1>
        ListMode: typing.ClassVar[QListView.ViewMode]  # value = <ViewMode.ListMode: 0>
    @staticmethod
    def batchSize(*args, **kwargs):
        ...
    @staticmethod
    def clearPropertyFlags(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        ...
    @staticmethod
    def dataChanged(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def flow(*args, **kwargs):
        ...
    @staticmethod
    def gridSize(*args, **kwargs):
        ...
    @staticmethod
    def horizontalOffset(*args, **kwargs):
        ...
    @staticmethod
    def indexAt(*args, **kwargs):
        ...
    @staticmethod
    def indexesMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def initViewItemOption(*args, **kwargs):
        ...
    @staticmethod
    def isIndexHidden(*args, **kwargs):
        ...
    @staticmethod
    def isRowHidden(*args, **kwargs):
        ...
    @staticmethod
    def isSelectionRectVisible(*args, **kwargs):
        ...
    @staticmethod
    def isWrapping(*args, **kwargs):
        ...
    @staticmethod
    def itemAlignment(*args, **kwargs):
        ...
    @staticmethod
    def layoutMode(*args, **kwargs):
        ...
    @staticmethod
    def modelColumn(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def movement(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def rectForIndex(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeMode(*args, **kwargs):
        ...
    @staticmethod
    def rowsAboutToBeRemoved(*args, **kwargs):
        ...
    @staticmethod
    def rowsInserted(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def scrollTo(*args, **kwargs):
        ...
    @staticmethod
    def selectedIndexes(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        ...
    @staticmethod
    def setBatchSize(*args, **kwargs):
        ...
    @staticmethod
    def setFlow(*args, **kwargs):
        ...
    @staticmethod
    def setGridSize(*args, **kwargs):
        ...
    @staticmethod
    def setItemAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setLayoutMode(*args, **kwargs):
        ...
    @staticmethod
    def setModelColumn(*args, **kwargs):
        ...
    @staticmethod
    def setMovement(*args, **kwargs):
        ...
    @staticmethod
    def setPositionForIndex(*args, **kwargs):
        ...
    @staticmethod
    def setResizeMode(*args, **kwargs):
        ...
    @staticmethod
    def setRootIndex(*args, **kwargs):
        ...
    @staticmethod
    def setRowHidden(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionRectVisible(*args, **kwargs):
        ...
    @staticmethod
    def setSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setUniformItemSizes(*args, **kwargs):
        ...
    @staticmethod
    def setViewMode(*args, **kwargs):
        ...
    @staticmethod
    def setWordWrap(*args, **kwargs):
        ...
    @staticmethod
    def setWrapping(*args, **kwargs):
        ...
    @staticmethod
    def spacing(*args, **kwargs):
        ...
    @staticmethod
    def startDrag(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def uniformItemSizes(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometries(*args, **kwargs):
        ...
    @staticmethod
    def verticalOffset(*args, **kwargs):
        ...
    @staticmethod
    def viewMode(*args, **kwargs):
        ...
    @staticmethod
    def viewportSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def visualRect(*args, **kwargs):
        ...
    @staticmethod
    def visualRegionForSelection(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def wordWrap(*args, **kwargs):
        ...
class QListWidget(QListView):
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addItems(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def closePersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentItem(*args, **kwargs):
        ...
    @staticmethod
    def currentItemChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentRow(*args, **kwargs):
        ...
    @staticmethod
    def currentRowChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def editItem(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def findItems(*args, **kwargs):
        ...
    @staticmethod
    def indexFromItem(*args, **kwargs):
        ...
    @staticmethod
    def insertItem(*args, **kwargs):
        ...
    @staticmethod
    def insertItems(*args, **kwargs):
        ...
    @staticmethod
    def isPersistentEditorOpen(*args, **kwargs):
        ...
    @staticmethod
    def isSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def item(*args, **kwargs):
        ...
    @staticmethod
    def itemActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def itemChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemFromIndex(*args, **kwargs):
        ...
    @staticmethod
    def itemPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemSelectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemWidget(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def openPersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def removeItemWidget(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def scrollToItem(*args, **kwargs):
        ...
    @staticmethod
    def selectedItems(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentItem(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentRow(*args, **kwargs):
        ...
    @staticmethod
    def setItemWidget(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionModel(*args, **kwargs):
        ...
    @staticmethod
    def setSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def sortItems(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
    @staticmethod
    def takeItem(*args, **kwargs):
        ...
    @staticmethod
    def visualItemRect(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QListWidgetItem(PyQt6.sip.wrapper):
    class ItemType(enum.IntEnum):
        Type: typing.ClassVar[QListWidgetItem.ItemType]  # value = <ItemType.Type: 0>
        UserType: typing.ClassVar[QListWidgetItem.ItemType]  # value = <ItemType.UserType: 1000>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def background(*args, **kwargs):
        ...
    @staticmethod
    def checkState(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def foreground(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def isHidden(*args, **kwargs):
        ...
    @staticmethod
    def isSelected(*args, **kwargs):
        ...
    @staticmethod
    def listWidget(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def setBackground(*args, **kwargs):
        ...
    @staticmethod
    def setCheckState(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setForeground(*args, **kwargs):
        ...
    @staticmethod
    def setHidden(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setSelected(*args, **kwargs):
        ...
    @staticmethod
    def setSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def setStatusTip(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def statusTip(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textAlignment(*args, **kwargs):
        ...
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def whatsThis(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QMainWindow(QWidget):
    class DockOption(enum.Flag):
        AllowNestedDocks: typing.ClassVar[QMainWindow.DockOption]  # value = <DockOption.AllowNestedDocks: 2>
        AllowTabbedDocks: typing.ClassVar[QMainWindow.DockOption]  # value = <DockOption.AllowTabbedDocks: 4>
        AnimatedDocks: typing.ClassVar[QMainWindow.DockOption]  # value = <DockOption.AnimatedDocks: 1>
        ForceTabbedDocks: typing.ClassVar[QMainWindow.DockOption]  # value = <DockOption.ForceTabbedDocks: 8>
        GroupedDragging: typing.ClassVar[QMainWindow.DockOption]  # value = <DockOption.GroupedDragging: 32>
        VerticalTabs: typing.ClassVar[QMainWindow.DockOption]  # value = <DockOption.VerticalTabs: 16>
    @staticmethod
    def addDockWidget(*args, **kwargs):
        ...
    @staticmethod
    def addToolBar(*args, **kwargs):
        ...
    @staticmethod
    def addToolBarBreak(*args, **kwargs):
        ...
    @staticmethod
    def centralWidget(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def corner(*args, **kwargs):
        ...
    @staticmethod
    def createPopupMenu(*args, **kwargs):
        ...
    @staticmethod
    def dockOptions(*args, **kwargs):
        ...
    @staticmethod
    def dockWidgetArea(*args, **kwargs):
        ...
    @staticmethod
    def documentMode(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def iconSize(*args, **kwargs):
        ...
    @staticmethod
    def iconSizeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def insertToolBar(*args, **kwargs):
        ...
    @staticmethod
    def insertToolBarBreak(*args, **kwargs):
        ...
    @staticmethod
    def isAnimated(*args, **kwargs):
        ...
    @staticmethod
    def isDockNestingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isSeparator(*args, **kwargs):
        ...
    @staticmethod
    def menuBar(*args, **kwargs):
        ...
    @staticmethod
    def menuWidget(*args, **kwargs):
        ...
    @staticmethod
    def removeDockWidget(*args, **kwargs):
        ...
    @staticmethod
    def removeToolBar(*args, **kwargs):
        ...
    @staticmethod
    def removeToolBarBreak(*args, **kwargs):
        ...
    @staticmethod
    def resizeDocks(*args, **kwargs):
        ...
    @staticmethod
    def restoreDockWidget(*args, **kwargs):
        ...
    @staticmethod
    def restoreState(*args, **kwargs):
        ...
    @staticmethod
    def saveState(*args, **kwargs):
        ...
    @staticmethod
    def setAnimated(*args, **kwargs):
        ...
    @staticmethod
    def setCentralWidget(*args, **kwargs):
        ...
    @staticmethod
    def setCorner(*args, **kwargs):
        ...
    @staticmethod
    def setDockNestingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setDockOptions(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentMode(*args, **kwargs):
        ...
    @staticmethod
    def setIconSize(*args, **kwargs):
        ...
    @staticmethod
    def setMenuBar(*args, **kwargs):
        ...
    @staticmethod
    def setMenuWidget(*args, **kwargs):
        ...
    @staticmethod
    def setStatusBar(*args, **kwargs):
        ...
    @staticmethod
    def setTabPosition(*args, **kwargs):
        ...
    @staticmethod
    def setTabShape(*args, **kwargs):
        ...
    @staticmethod
    def setToolButtonStyle(*args, **kwargs):
        ...
    @staticmethod
    def setUnifiedTitleAndToolBarOnMac(*args, **kwargs):
        ...
    @staticmethod
    def splitDockWidget(*args, **kwargs):
        ...
    @staticmethod
    def statusBar(*args, **kwargs):
        ...
    @staticmethod
    def tabPosition(*args, **kwargs):
        ...
    @staticmethod
    def tabShape(*args, **kwargs):
        ...
    @staticmethod
    def tabifiedDockWidgetActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabifiedDockWidgets(*args, **kwargs):
        ...
    @staticmethod
    def tabifyDockWidget(*args, **kwargs):
        ...
    @staticmethod
    def takeCentralWidget(*args, **kwargs):
        ...
    @staticmethod
    def toolBarArea(*args, **kwargs):
        ...
    @staticmethod
    def toolBarBreak(*args, **kwargs):
        ...
    @staticmethod
    def toolButtonStyle(*args, **kwargs):
        ...
    @staticmethod
    def toolButtonStyleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def unifiedTitleAndToolBarOnMac(*args, **kwargs):
        ...
class QMdiArea(QAbstractScrollArea):
    class AreaOption(enum.Flag):
        DontMaximizeSubWindowOnActivation: typing.ClassVar[QMdiArea.AreaOption]  # value = <AreaOption.DontMaximizeSubWindowOnActivation: 1>
    class ViewMode(enum.Enum):
        SubWindowView: typing.ClassVar[QMdiArea.ViewMode]  # value = <ViewMode.SubWindowView: 0>
        TabbedView: typing.ClassVar[QMdiArea.ViewMode]  # value = <ViewMode.TabbedView: 1>
    class WindowOrder(enum.Enum):
        ActivationHistoryOrder: typing.ClassVar[QMdiArea.WindowOrder]  # value = <WindowOrder.ActivationHistoryOrder: 2>
        CreationOrder: typing.ClassVar[QMdiArea.WindowOrder]  # value = <WindowOrder.CreationOrder: 0>
        StackingOrder: typing.ClassVar[QMdiArea.WindowOrder]  # value = <WindowOrder.StackingOrder: 1>
    @staticmethod
    def activateNextSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def activatePreviousSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def activationOrder(*args, **kwargs):
        ...
    @staticmethod
    def activeSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def addSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def background(*args, **kwargs):
        ...
    @staticmethod
    def cascadeSubWindows(*args, **kwargs):
        ...
    @staticmethod
    def childEvent(*args, **kwargs):
        ...
    @staticmethod
    def closeActiveSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def closeAllSubWindows(*args, **kwargs):
        ...
    @staticmethod
    def currentSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def documentMode(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def removeSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def setActivationOrder(*args, **kwargs):
        ...
    @staticmethod
    def setActiveSubWindow(*args, **kwargs):
        ...
    @staticmethod
    def setBackground(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentMode(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setTabPosition(*args, **kwargs):
        ...
    @staticmethod
    def setTabShape(*args, **kwargs):
        ...
    @staticmethod
    def setTabsClosable(*args, **kwargs):
        ...
    @staticmethod
    def setTabsMovable(*args, **kwargs):
        ...
    @staticmethod
    def setViewMode(*args, **kwargs):
        ...
    @staticmethod
    def setupViewport(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def subWindowActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def subWindowList(*args, **kwargs):
        ...
    @staticmethod
    def tabPosition(*args, **kwargs):
        ...
    @staticmethod
    def tabShape(*args, **kwargs):
        ...
    @staticmethod
    def tabsClosable(*args, **kwargs):
        ...
    @staticmethod
    def tabsMovable(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def tileSubWindows(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def viewMode(*args, **kwargs):
        ...
    @staticmethod
    def viewportEvent(*args, **kwargs):
        ...
class QMdiSubWindow(QWidget):
    class SubWindowOption(enum.Flag):
        RubberBandMove: typing.ClassVar[QMdiSubWindow.SubWindowOption]  # value = <SubWindowOption.RubberBandMove: 8>
        RubberBandResize: typing.ClassVar[QMdiSubWindow.SubWindowOption]  # value = <SubWindowOption.RubberBandResize: 4>
    @staticmethod
    def aboutToActivate(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def childEvent(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def isShaded(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyboardPageStep(*args, **kwargs):
        ...
    @staticmethod
    def keyboardSingleStep(*args, **kwargs):
        ...
    @staticmethod
    def leaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mdiArea(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setKeyboardPageStep(*args, **kwargs):
        ...
    @staticmethod
    def setKeyboardSingleStep(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setSystemMenu(*args, **kwargs):
        ...
    @staticmethod
    def setWidget(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def showShaded(*args, **kwargs):
        ...
    @staticmethod
    def showSystemMenu(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def systemMenu(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
    @staticmethod
    def windowStateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QMenu(QWidget):
    @staticmethod
    def aboutToHide(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def aboutToShow(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def actionAt(*args, **kwargs):
        ...
    @staticmethod
    def actionEvent(*args, **kwargs):
        ...
    @staticmethod
    def actionGeometry(*args, **kwargs):
        ...
    @staticmethod
    def activeAction(*args, **kwargs):
        ...
    @staticmethod
    def addMenu(*args, **kwargs):
        ...
    @staticmethod
    def addSection(*args, **kwargs):
        ...
    @staticmethod
    def addSeparator(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def defaultAction(*args, **kwargs):
        ...
    @staticmethod
    def enterEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def hideTearOffMenu(*args, **kwargs):
        ...
    @staticmethod
    def hovered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def insertMenu(*args, **kwargs):
        ...
    @staticmethod
    def insertSection(*args, **kwargs):
        ...
    @staticmethod
    def insertSeparator(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isTearOffEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isTearOffMenuVisible(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def leaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def menuAction(*args, **kwargs):
        ...
    @staticmethod
    def menuInAction(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def popup(*args, **kwargs):
        ...
    @staticmethod
    def separatorsCollapsible(*args, **kwargs):
        ...
    @staticmethod
    def setActiveAction(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultAction(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setNoReplayFor(*args, **kwargs):
        ...
    @staticmethod
    def setSeparatorsCollapsible(*args, **kwargs):
        ...
    @staticmethod
    def setTearOffEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setTitle(*args, **kwargs):
        ...
    @staticmethod
    def setToolTipsVisible(*args, **kwargs):
        ...
    @staticmethod
    def showTearOffMenu(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
    @staticmethod
    def toolTipsVisible(*args, **kwargs):
        ...
    @staticmethod
    def triggered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
class QMenuBar(QWidget):
    @staticmethod
    def actionAt(*args, **kwargs):
        ...
    @staticmethod
    def actionEvent(*args, **kwargs):
        ...
    @staticmethod
    def actionGeometry(*args, **kwargs):
        ...
    @staticmethod
    def activeAction(*args, **kwargs):
        ...
    @staticmethod
    def addMenu(*args, **kwargs):
        ...
    @staticmethod
    def addSeparator(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def cornerWidget(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def hovered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def insertMenu(*args, **kwargs):
        ...
    @staticmethod
    def insertSeparator(*args, **kwargs):
        ...
    @staticmethod
    def isDefaultUp(*args, **kwargs):
        ...
    @staticmethod
    def isNativeMenuBar(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def leaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setActiveAction(*args, **kwargs):
        ...
    @staticmethod
    def setCornerWidget(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultUp(*args, **kwargs):
        ...
    @staticmethod
    def setNativeMenuBar(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def triggered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QMessageBox(QDialog):
    class ButtonRole(enum.Enum):
        AcceptRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.AcceptRole: 0>
        ActionRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.ActionRole: 3>
        ApplyRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.ApplyRole: 8>
        DestructiveRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.DestructiveRole: 2>
        HelpRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.HelpRole: 4>
        InvalidRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.InvalidRole: -1>
        NoRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.NoRole: 6>
        RejectRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.RejectRole: 1>
        ResetRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.ResetRole: 7>
        YesRole: typing.ClassVar[QMessageBox.ButtonRole]  # value = <ButtonRole.YesRole: 5>
    class Icon(enum.Enum):
        Critical: typing.ClassVar[QMessageBox.Icon]  # value = <Icon.Critical: 3>
        Information: typing.ClassVar[QMessageBox.Icon]  # value = <Icon.Information: 1>
        NoIcon: typing.ClassVar[QMessageBox.Icon]  # value = <Icon.NoIcon: 0>
        Question: typing.ClassVar[QMessageBox.Icon]  # value = <Icon.Question: 4>
        Warning: typing.ClassVar[QMessageBox.Icon]  # value = <Icon.Warning: 2>
    class Option(enum.Enum):
        DontUseNativeDialog: typing.ClassVar[QMessageBox.Option]  # value = <Option.DontUseNativeDialog: 1>
    class StandardButton(enum.IntFlag):
        Abort: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Abort: 262144>
        Apply: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Apply: 33554432>
        Cancel: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Cancel: 4194304>
        Close: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Close: 2097152>
        Default: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Default: 256>
        Discard: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Discard: 8388608>
        Escape: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Escape: 512>
        Help: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Help: 16777216>
        Ignore: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Ignore: 1048576>
        No: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.No: 65536>
        NoToAll: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.NoToAll: 131072>
        Ok: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Ok: 1024>
        Open: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Open: 8192>
        Reset: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Reset: 67108864>
        RestoreDefaults: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.RestoreDefaults: 134217728>
        Retry: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Retry: 524288>
        Save: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Save: 2048>
        SaveAll: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.SaveAll: 4096>
        Yes: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.Yes: 16384>
        YesToAll: typing.ClassVar[QMessageBox.StandardButton]  # value = <StandardButton.YesToAll: 32768>
        @classmethod
        def __new__(cls, value):
            ...
        def __and__(self, other):
            ...
        def __format__(self, format_spec):
            ...
        def __invert__(self):
            ...
        def __or__(self, other):
            ...
        def __rand__(self, other):
            ...
        def __ror__(self, other):
            ...
        def __rxor__(self, other):
            ...
        def __xor__(self, other):
            ...
    @staticmethod
    def about(*args, **kwargs):
        ...
    @staticmethod
    def aboutQt(*args, **kwargs):
        ...
    @staticmethod
    def addButton(*args, **kwargs):
        ...
    @staticmethod
    def button(*args, **kwargs):
        ...
    @staticmethod
    def buttonClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def buttonRole(*args, **kwargs):
        ...
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def checkBox(*args, **kwargs):
        ...
    @staticmethod
    def clickedButton(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def critical(*args, **kwargs):
        ...
    @staticmethod
    def defaultButton(*args, **kwargs):
        ...
    @staticmethod
    def detailedText(*args, **kwargs):
        ...
    @staticmethod
    def escapeButton(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def iconPixmap(*args, **kwargs):
        ...
    @staticmethod
    def information(*args, **kwargs):
        ...
    @staticmethod
    def informativeText(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def question(*args, **kwargs):
        ...
    @staticmethod
    def removeButton(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setCheckBox(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultButton(*args, **kwargs):
        ...
    @staticmethod
    def setDetailedText(*args, **kwargs):
        ...
    @staticmethod
    def setEscapeButton(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setIconPixmap(*args, **kwargs):
        ...
    @staticmethod
    def setInformativeText(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setStandardButtons(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def setTextInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def setWindowModality(*args, **kwargs):
        ...
    @staticmethod
    def setWindowTitle(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def standardButton(*args, **kwargs):
        ...
    @staticmethod
    def standardButtons(*args, **kwargs):
        ...
    @staticmethod
    def standardIcon(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textFormat(*args, **kwargs):
        ...
    @staticmethod
    def textInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def warning(*args, **kwargs):
        ...
class QPanGesture(QGesture):
    @staticmethod
    def acceleration(*args, **kwargs):
        ...
    @staticmethod
    def delta(*args, **kwargs):
        ...
    @staticmethod
    def lastOffset(*args, **kwargs):
        ...
    @staticmethod
    def offset(*args, **kwargs):
        ...
    @staticmethod
    def setAcceleration(*args, **kwargs):
        ...
    @staticmethod
    def setLastOffset(*args, **kwargs):
        ...
    @staticmethod
    def setOffset(*args, **kwargs):
        ...
class QPinchGesture(QGesture):
    class ChangeFlag(enum.Flag):
        CenterPointChanged: typing.ClassVar[QPinchGesture.ChangeFlag]  # value = <ChangeFlag.CenterPointChanged: 4>
        RotationAngleChanged: typing.ClassVar[QPinchGesture.ChangeFlag]  # value = <ChangeFlag.RotationAngleChanged: 2>
        ScaleFactorChanged: typing.ClassVar[QPinchGesture.ChangeFlag]  # value = <ChangeFlag.ScaleFactorChanged: 1>
    @staticmethod
    def centerPoint(*args, **kwargs):
        ...
    @staticmethod
    def changeFlags(*args, **kwargs):
        ...
    @staticmethod
    def lastCenterPoint(*args, **kwargs):
        ...
    @staticmethod
    def lastRotationAngle(*args, **kwargs):
        ...
    @staticmethod
    def lastScaleFactor(*args, **kwargs):
        ...
    @staticmethod
    def rotationAngle(*args, **kwargs):
        ...
    @staticmethod
    def scaleFactor(*args, **kwargs):
        ...
    @staticmethod
    def setCenterPoint(*args, **kwargs):
        ...
    @staticmethod
    def setChangeFlags(*args, **kwargs):
        ...
    @staticmethod
    def setLastCenterPoint(*args, **kwargs):
        ...
    @staticmethod
    def setLastRotationAngle(*args, **kwargs):
        ...
    @staticmethod
    def setLastScaleFactor(*args, **kwargs):
        ...
    @staticmethod
    def setRotationAngle(*args, **kwargs):
        ...
    @staticmethod
    def setScaleFactor(*args, **kwargs):
        ...
    @staticmethod
    def setStartCenterPoint(*args, **kwargs):
        ...
    @staticmethod
    def setTotalChangeFlags(*args, **kwargs):
        ...
    @staticmethod
    def setTotalRotationAngle(*args, **kwargs):
        ...
    @staticmethod
    def setTotalScaleFactor(*args, **kwargs):
        ...
    @staticmethod
    def startCenterPoint(*args, **kwargs):
        ...
    @staticmethod
    def totalChangeFlags(*args, **kwargs):
        ...
    @staticmethod
    def totalRotationAngle(*args, **kwargs):
        ...
    @staticmethod
    def totalScaleFactor(*args, **kwargs):
        ...
class QPlainTextDocumentLayout(PyQt6.QtGui.QAbstractTextDocumentLayout):
    @staticmethod
    def blockBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def cursorWidth(*args, **kwargs):
        ...
    @staticmethod
    def documentChanged(*args, **kwargs):
        ...
    @staticmethod
    def documentSize(*args, **kwargs):
        ...
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def ensureBlockLayout(*args, **kwargs):
        ...
    @staticmethod
    def frameBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def hitTest(*args, **kwargs):
        ...
    @staticmethod
    def pageCount(*args, **kwargs):
        ...
    @staticmethod
    def requestUpdate(*args, **kwargs):
        ...
    @staticmethod
    def setCursorWidth(*args, **kwargs):
        ...
class QPlainTextEdit(QAbstractScrollArea):
    class LineWrapMode(enum.Enum):
        NoWrap: typing.ClassVar[QPlainTextEdit.LineWrapMode]  # value = <LineWrapMode.NoWrap: 0>
        WidgetWidth: typing.ClassVar[QPlainTextEdit.LineWrapMode]  # value = <LineWrapMode.WidgetWidth: 1>
    @staticmethod
    def anchorAt(*args, **kwargs):
        ...
    @staticmethod
    def appendHtml(*args, **kwargs):
        ...
    @staticmethod
    def appendPlainText(*args, **kwargs):
        ...
    @staticmethod
    def backgroundVisible(*args, **kwargs):
        ...
    @staticmethod
    def blockBoundingGeometry(*args, **kwargs):
        ...
    @staticmethod
    def blockBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def blockCount(*args, **kwargs):
        ...
    @staticmethod
    def blockCountChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def canInsertFromMimeData(*args, **kwargs):
        ...
    @staticmethod
    def canPaste(*args, **kwargs):
        ...
    @staticmethod
    def centerCursor(*args, **kwargs):
        ...
    @staticmethod
    def centerOnScroll(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contentOffset(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def copyAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def createMimeDataFromSelection(*args, **kwargs):
        ...
    @staticmethod
    def createStandardContextMenu(*args, **kwargs):
        ...
    @staticmethod
    def currentCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def cursorForPosition(*args, **kwargs):
        ...
    @staticmethod
    def cursorPositionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cursorRect(*args, **kwargs):
        ...
    @staticmethod
    def cursorWidth(*args, **kwargs):
        ...
    @staticmethod
    def cut(*args, **kwargs):
        ...
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def documentTitle(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def ensureCursorVisible(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def extraSelections(*args, **kwargs):
        ...
    @staticmethod
    def find(*args, **kwargs):
        ...
    @staticmethod
    def firstVisibleBlock(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def getPaintContext(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def insertFromMimeData(*args, **kwargs):
        ...
    @staticmethod
    def insertPlainText(*args, **kwargs):
        ...
    @staticmethod
    def isReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def isUndoRedoEnabled(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def lineWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def loadResource(*args, **kwargs):
        ...
    @staticmethod
    def maximumBlockCount(*args, **kwargs):
        ...
    @staticmethod
    def mergeCurrentCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def modificationChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def overwriteMode(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def paste(*args, **kwargs):
        ...
    @staticmethod
    def placeholderText(*args, **kwargs):
        ...
    @staticmethod
    def print(*args, **kwargs):
        ...
    @staticmethod
    def redo(*args, **kwargs):
        ...
    @staticmethod
    def redoAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def selectAll(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setBackgroundVisible(*args, **kwargs):
        ...
    @staticmethod
    def setCenterOnScroll(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def setCursorWidth(*args, **kwargs):
        ...
    @staticmethod
    def setDocument(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentTitle(*args, **kwargs):
        ...
    @staticmethod
    def setExtraSelections(*args, **kwargs):
        ...
    @staticmethod
    def setLineWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumBlockCount(*args, **kwargs):
        ...
    @staticmethod
    def setOverwriteMode(*args, **kwargs):
        ...
    @staticmethod
    def setPlaceholderText(*args, **kwargs):
        ...
    @staticmethod
    def setPlainText(*args, **kwargs):
        ...
    @staticmethod
    def setReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def setTabChangesFocus(*args, **kwargs):
        ...
    @staticmethod
    def setTabStopDistance(*args, **kwargs):
        ...
    @staticmethod
    def setTextCursor(*args, **kwargs):
        ...
    @staticmethod
    def setTextInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def setUndoRedoEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setWordWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def tabChangesFocus(*args, **kwargs):
        ...
    @staticmethod
    def tabStopDistance(*args, **kwargs):
        ...
    @staticmethod
    def textChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textCursor(*args, **kwargs):
        ...
    @staticmethod
    def textInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def toPlainText(*args, **kwargs):
        ...
    @staticmethod
    def undo(*args, **kwargs):
        ...
    @staticmethod
    def undoAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def updateRequest(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def wordWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def zoomIn(*args, **kwargs):
        ...
    @staticmethod
    def zoomOut(*args, **kwargs):
        ...
class QProgressBar(QWidget):
    class Direction(enum.Enum):
        BottomToTop: typing.ClassVar[QProgressBar.Direction]  # value = <Direction.BottomToTop: 1>
        TopToBottom: typing.ClassVar[QProgressBar.Direction]  # value = <Direction.TopToBottom: 0>
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def isTextVisible(*args, **kwargs):
        ...
    @staticmethod
    def maximum(*args, **kwargs):
        ...
    @staticmethod
    def minimum(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def resetFormat(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setInvertedAppearance(*args, **kwargs):
        ...
    @staticmethod
    def setMaximum(*args, **kwargs):
        ...
    @staticmethod
    def setMinimum(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setRange(*args, **kwargs):
        ...
    @staticmethod
    def setTextDirection(*args, **kwargs):
        ...
    @staticmethod
    def setTextVisible(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def valueChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QProgressDialog(QDialog):
    @staticmethod
    def autoClose(*args, **kwargs):
        ...
    @staticmethod
    def autoReset(*args, **kwargs):
        ...
    @staticmethod
    def cancel(*args, **kwargs):
        ...
    @staticmethod
    def canceled(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def forceShow(*args, **kwargs):
        ...
    @staticmethod
    def labelText(*args, **kwargs):
        ...
    @staticmethod
    def maximum(*args, **kwargs):
        ...
    @staticmethod
    def minimum(*args, **kwargs):
        ...
    @staticmethod
    def minimumDuration(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setAutoClose(*args, **kwargs):
        ...
    @staticmethod
    def setAutoReset(*args, **kwargs):
        ...
    @staticmethod
    def setBar(*args, **kwargs):
        ...
    @staticmethod
    def setCancelButton(*args, **kwargs):
        ...
    @staticmethod
    def setCancelButtonText(*args, **kwargs):
        ...
    @staticmethod
    def setLabel(*args, **kwargs):
        ...
    @staticmethod
    def setLabelText(*args, **kwargs):
        ...
    @staticmethod
    def setMaximum(*args, **kwargs):
        ...
    @staticmethod
    def setMinimum(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumDuration(*args, **kwargs):
        ...
    @staticmethod
    def setRange(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def wasCanceled(*args, **kwargs):
        ...
class QProxyStyle(QCommonStyle):
    @staticmethod
    def baseStyle(*args, **kwargs):
        ...
    @staticmethod
    def drawComplexControl(*args, **kwargs):
        ...
    @staticmethod
    def drawControl(*args, **kwargs):
        ...
    @staticmethod
    def drawItemPixmap(*args, **kwargs):
        ...
    @staticmethod
    def drawItemText(*args, **kwargs):
        ...
    @staticmethod
    def drawPrimitive(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def generatedIconPixmap(*args, **kwargs):
        ...
    @staticmethod
    def hitTestComplexControl(*args, **kwargs):
        ...
    @staticmethod
    def itemPixmapRect(*args, **kwargs):
        ...
    @staticmethod
    def itemTextRect(*args, **kwargs):
        ...
    @staticmethod
    def layoutSpacing(*args, **kwargs):
        ...
    @staticmethod
    def pixelMetric(*args, **kwargs):
        ...
    @staticmethod
    def polish(*args, **kwargs):
        ...
    @staticmethod
    def setBaseStyle(*args, **kwargs):
        ...
    @staticmethod
    def sizeFromContents(*args, **kwargs):
        ...
    @staticmethod
    def standardIcon(*args, **kwargs):
        ...
    @staticmethod
    def standardPalette(*args, **kwargs):
        ...
    @staticmethod
    def standardPixmap(*args, **kwargs):
        ...
    @staticmethod
    def styleHint(*args, **kwargs):
        ...
    @staticmethod
    def subControlRect(*args, **kwargs):
        ...
    @staticmethod
    def subElementRect(*args, **kwargs):
        ...
    @staticmethod
    def unpolish(*args, **kwargs):
        ...
class QPushButton(QAbstractButton):
    @staticmethod
    def autoDefault(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def hitButton(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def isDefault(*args, **kwargs):
        ...
    @staticmethod
    def isFlat(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def menu(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setAutoDefault(*args, **kwargs):
        ...
    @staticmethod
    def setDefault(*args, **kwargs):
        ...
    @staticmethod
    def setFlat(*args, **kwargs):
        ...
    @staticmethod
    def setMenu(*args, **kwargs):
        ...
    @staticmethod
    def showMenu(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
class QRadioButton(QAbstractButton):
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def hitButton(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
class QRubberBand(QWidget):
    class Shape(enum.Enum):
        Line: typing.ClassVar[QRubberBand.Shape]  # value = <Shape.Line: 0>
        Rectangle: typing.ClassVar[QRubberBand.Shape]  # value = <Shape.Rectangle: 1>
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def move(*args, **kwargs):
        ...
    @staticmethod
    def moveEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
class QScrollArea(QAbstractScrollArea):
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def ensureVisible(*args, **kwargs):
        ...
    @staticmethod
    def ensureWidgetVisible(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setWidget(*args, **kwargs):
        ...
    @staticmethod
    def setWidgetResizable(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def takeWidget(*args, **kwargs):
        ...
    @staticmethod
    def viewportSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
    @staticmethod
    def widgetResizable(*args, **kwargs):
        ...
class QScrollBar(QAbstractSlider):
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sliderChange(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
class QScroller(PyQt6.QtCore.QObject):
    class Input(enum.Enum):
        InputMove: typing.ClassVar[QScroller.Input]  # value = <Input.InputMove: 2>
        InputPress: typing.ClassVar[QScroller.Input]  # value = <Input.InputPress: 1>
        InputRelease: typing.ClassVar[QScroller.Input]  # value = <Input.InputRelease: 3>
    class ScrollerGestureType(enum.Enum):
        LeftMouseButtonGesture: typing.ClassVar[QScroller.ScrollerGestureType]  # value = <ScrollerGestureType.LeftMouseButtonGesture: 1>
        MiddleMouseButtonGesture: typing.ClassVar[QScroller.ScrollerGestureType]  # value = <ScrollerGestureType.MiddleMouseButtonGesture: 3>
        RightMouseButtonGesture: typing.ClassVar[QScroller.ScrollerGestureType]  # value = <ScrollerGestureType.RightMouseButtonGesture: 2>
        TouchGesture: typing.ClassVar[QScroller.ScrollerGestureType]  # value = <ScrollerGestureType.TouchGesture: 0>
    class State(enum.Enum):
        Dragging: typing.ClassVar[QScroller.State]  # value = <State.Dragging: 2>
        Inactive: typing.ClassVar[QScroller.State]  # value = <State.Inactive: 0>
        Pressed: typing.ClassVar[QScroller.State]  # value = <State.Pressed: 1>
        Scrolling: typing.ClassVar[QScroller.State]  # value = <State.Scrolling: 3>
    @staticmethod
    def activeScrollers(*args, **kwargs):
        ...
    @staticmethod
    def ensureVisible(*args, **kwargs):
        ...
    @staticmethod
    def finalPosition(*args, **kwargs):
        ...
    @staticmethod
    def grabGesture(*args, **kwargs):
        ...
    @staticmethod
    def grabbedGesture(*args, **kwargs):
        ...
    @staticmethod
    def handleInput(*args, **kwargs):
        ...
    @staticmethod
    def hasScroller(*args, **kwargs):
        ...
    @staticmethod
    def pixelPerMeter(*args, **kwargs):
        ...
    @staticmethod
    def resendPrepareEvent(*args, **kwargs):
        ...
    @staticmethod
    def scrollTo(*args, **kwargs):
        ...
    @staticmethod
    def scroller(*args, **kwargs):
        ...
    @staticmethod
    def scrollerProperties(*args, **kwargs):
        ...
    @staticmethod
    def scrollerPropertiesChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setScrollerProperties(*args, **kwargs):
        ...
    @staticmethod
    def setSnapPositionsX(*args, **kwargs):
        ...
    @staticmethod
    def setSnapPositionsY(*args, **kwargs):
        ...
    @staticmethod
    def state(*args, **kwargs):
        ...
    @staticmethod
    def stateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def stop(*args, **kwargs):
        ...
    @staticmethod
    def target(*args, **kwargs):
        ...
    @staticmethod
    def ungrabGesture(*args, **kwargs):
        ...
    @staticmethod
    def velocity(*args, **kwargs):
        ...
class QScrollerProperties(PyQt6.sip.simplewrapper):
    class FrameRates(enum.Enum):
        Fps20: typing.ClassVar[QScrollerProperties.FrameRates]  # value = <FrameRates.Fps20: 3>
        Fps30: typing.ClassVar[QScrollerProperties.FrameRates]  # value = <FrameRates.Fps30: 2>
        Fps60: typing.ClassVar[QScrollerProperties.FrameRates]  # value = <FrameRates.Fps60: 1>
        Standard: typing.ClassVar[QScrollerProperties.FrameRates]  # value = <FrameRates.Standard: 0>
    class OvershootPolicy(enum.Enum):
        OvershootAlwaysOff: typing.ClassVar[QScrollerProperties.OvershootPolicy]  # value = <OvershootPolicy.OvershootAlwaysOff: 1>
        OvershootAlwaysOn: typing.ClassVar[QScrollerProperties.OvershootPolicy]  # value = <OvershootPolicy.OvershootAlwaysOn: 2>
        OvershootWhenScrollable: typing.ClassVar[QScrollerProperties.OvershootPolicy]  # value = <OvershootPolicy.OvershootWhenScrollable: 0>
    class ScrollMetric(enum.Enum):
        AcceleratingFlickMaximumTime: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.AcceleratingFlickMaximumTime: 9>
        AcceleratingFlickSpeedupFactor: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.AcceleratingFlickSpeedupFactor: 10>
        AxisLockThreshold: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.AxisLockThreshold: 3>
        DecelerationFactor: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.DecelerationFactor: 5>
        DragStartDistance: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.DragStartDistance: 1>
        DragVelocitySmoothingFactor: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.DragVelocitySmoothingFactor: 2>
        FrameRate: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.FrameRate: 19>
        HorizontalOvershootPolicy: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.HorizontalOvershootPolicy: 17>
        MaximumClickThroughVelocity: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.MaximumClickThroughVelocity: 8>
        MaximumVelocity: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.MaximumVelocity: 7>
        MinimumVelocity: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.MinimumVelocity: 6>
        MousePressEventDelay: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.MousePressEventDelay: 0>
        OvershootDragDistanceFactor: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.OvershootDragDistanceFactor: 14>
        OvershootDragResistanceFactor: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.OvershootDragResistanceFactor: 13>
        OvershootScrollDistanceFactor: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.OvershootScrollDistanceFactor: 15>
        OvershootScrollTime: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.OvershootScrollTime: 16>
        ScrollMetricCount: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.ScrollMetricCount: 20>
        ScrollingCurve: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.ScrollingCurve: 4>
        SnapPositionRatio: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.SnapPositionRatio: 11>
        SnapTime: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.SnapTime: 12>
        VerticalOvershootPolicy: typing.ClassVar[QScrollerProperties.ScrollMetric]  # value = <ScrollMetric.VerticalOvershootPolicy: 18>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def scrollMetric(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultScrollerProperties(*args, **kwargs):
        ...
    @staticmethod
    def setScrollMetric(*args, **kwargs):
        ...
    @staticmethod
    def unsetDefaultScrollerProperties(*args, **kwargs):
        ...
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QSizeGrip(QWidget):
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
class QSizePolicy(PyQt6.sip.simplewrapper):
    class ControlType(enum.Flag):
        ButtonBox: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.ButtonBox: 2>
        CheckBox: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.CheckBox: 4>
        ComboBox: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.ComboBox: 8>
        DefaultType: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.DefaultType: 1>
        Frame: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.Frame: 16>
        GroupBox: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.GroupBox: 32>
        Label: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.Label: 64>
        Line: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.Line: 128>
        LineEdit: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.LineEdit: 256>
        PushButton: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.PushButton: 512>
        RadioButton: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.RadioButton: 1024>
        Slider: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.Slider: 2048>
        SpinBox: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.SpinBox: 4096>
        TabWidget: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.TabWidget: 8192>
        ToolButton: typing.ClassVar[QSizePolicy.ControlType]  # value = <ControlType.ToolButton: 16384>
    class Policy(enum.Enum):
        Expanding: typing.ClassVar[QSizePolicy.Policy]  # value = <Policy.Expanding: 7>
        Fixed: typing.ClassVar[QSizePolicy.Policy]  # value = <Policy.Fixed: 0>
        Ignored: typing.ClassVar[QSizePolicy.Policy]  # value = <Policy.Ignored: 13>
        Maximum: typing.ClassVar[QSizePolicy.Policy]  # value = <Policy.Maximum: 4>
        Minimum: typing.ClassVar[QSizePolicy.Policy]  # value = <Policy.Minimum: 1>
        MinimumExpanding: typing.ClassVar[QSizePolicy.Policy]  # value = <Policy.MinimumExpanding: 3>
        Preferred: typing.ClassVar[QSizePolicy.Policy]  # value = <Policy.Preferred: 5>
    class PolicyFlag(enum.IntFlag):
        ExpandFlag: typing.ClassVar[QSizePolicy.PolicyFlag]  # value = <PolicyFlag.ExpandFlag: 2>
        GrowFlag: typing.ClassVar[QSizePolicy.PolicyFlag]  # value = <PolicyFlag.GrowFlag: 1>
        IgnoreFlag: typing.ClassVar[QSizePolicy.PolicyFlag]  # value = <PolicyFlag.IgnoreFlag: 8>
        ShrinkFlag: typing.ClassVar[QSizePolicy.PolicyFlag]  # value = <PolicyFlag.ShrinkFlag: 4>
        @classmethod
        def __new__(cls, value):
            ...
        def __and__(self, other):
            ...
        def __format__(self, format_spec):
            ...
        def __invert__(self):
            ...
        def __or__(self, other):
            ...
        def __rand__(self, other):
            ...
        def __ror__(self, other):
            ...
        def __rxor__(self, other):
            ...
        def __xor__(self, other):
            ...
    @staticmethod
    def controlType(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def hasWidthForHeight(*args, **kwargs):
        ...
    @staticmethod
    def horizontalPolicy(*args, **kwargs):
        ...
    @staticmethod
    def horizontalStretch(*args, **kwargs):
        ...
    @staticmethod
    def retainSizeWhenHidden(*args, **kwargs):
        ...
    @staticmethod
    def setControlType(*args, **kwargs):
        ...
    @staticmethod
    def setHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalStretch(*args, **kwargs):
        ...
    @staticmethod
    def setRetainSizeWhenHidden(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalStretch(*args, **kwargs):
        ...
    @staticmethod
    def setWidthForHeight(*args, **kwargs):
        ...
    @staticmethod
    def transpose(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    @staticmethod
    def verticalPolicy(*args, **kwargs):
        ...
    @staticmethod
    def verticalStretch(*args, **kwargs):
        ...
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __hash__(self):
        """
        Return hash(self).
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QSlider(QAbstractSlider):
    class TickPosition(enum.Enum):
        NoTicks: typing.ClassVar[QSlider.TickPosition]  # value = <TickPosition.NoTicks: 0>
        TicksAbove: typing.ClassVar[QSlider.TickPosition]  # value = <TickPosition.TicksAbove: 1>
        TicksBelow: typing.ClassVar[QSlider.TickPosition]  # value = <TickPosition.TicksBelow: 2>
        TicksBothSides: typing.ClassVar[QSlider.TickPosition]  # value = <TickPosition.TicksBothSides: 3>
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setTickInterval(*args, **kwargs):
        ...
    @staticmethod
    def setTickPosition(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def tickInterval(*args, **kwargs):
        ...
    @staticmethod
    def tickPosition(*args, **kwargs):
        ...
class QSpacerItem(QLayoutItem):
    @staticmethod
    def changeSize(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sizePolicy(*args, **kwargs):
        ...
    @staticmethod
    def spacerItem(*args, **kwargs):
        ...
class QSpinBox(QAbstractSpinBox):
    @staticmethod
    def cleanText(*args, **kwargs):
        ...
    @staticmethod
    def displayIntegerBase(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def fixup(*args, **kwargs):
        ...
    @staticmethod
    def maximum(*args, **kwargs):
        ...
    @staticmethod
    def minimum(*args, **kwargs):
        ...
    @staticmethod
    def prefix(*args, **kwargs):
        ...
    @staticmethod
    def setDisplayIntegerBase(*args, **kwargs):
        ...
    @staticmethod
    def setMaximum(*args, **kwargs):
        ...
    @staticmethod
    def setMinimum(*args, **kwargs):
        ...
    @staticmethod
    def setPrefix(*args, **kwargs):
        ...
    @staticmethod
    def setRange(*args, **kwargs):
        ...
    @staticmethod
    def setSingleStep(*args, **kwargs):
        ...
    @staticmethod
    def setStepType(*args, **kwargs):
        ...
    @staticmethod
    def setSuffix(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def singleStep(*args, **kwargs):
        ...
    @staticmethod
    def stepType(*args, **kwargs):
        ...
    @staticmethod
    def suffix(*args, **kwargs):
        ...
    @staticmethod
    def textChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textFromValue(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def valueChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def valueFromText(*args, **kwargs):
        ...
class QSplashScreen(QWidget):
    @staticmethod
    def clearMessage(*args, **kwargs):
        ...
    @staticmethod
    def drawContents(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def finish(*args, **kwargs):
        ...
    @staticmethod
    def message(*args, **kwargs):
        ...
    @staticmethod
    def messageChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def repaint(*args, **kwargs):
        ...
    @staticmethod
    def setPixmap(*args, **kwargs):
        ...
    @staticmethod
    def showMessage(*args, **kwargs):
        ...
class QSplitter(QFrame):
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def childEvent(*args, **kwargs):
        ...
    @staticmethod
    def childrenCollapsible(*args, **kwargs):
        ...
    @staticmethod
    def closestLegalPosition(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def createHandle(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def getRange(*args, **kwargs):
        ...
    @staticmethod
    def handle(*args, **kwargs):
        ...
    @staticmethod
    def handleWidth(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def insertWidget(*args, **kwargs):
        ...
    @staticmethod
    def isCollapsible(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def moveSplitter(*args, **kwargs):
        ...
    @staticmethod
    def opaqueResize(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def refresh(*args, **kwargs):
        ...
    @staticmethod
    def replaceWidget(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def restoreState(*args, **kwargs):
        ...
    @staticmethod
    def saveState(*args, **kwargs):
        ...
    @staticmethod
    def setChildrenCollapsible(*args, **kwargs):
        ...
    @staticmethod
    def setCollapsible(*args, **kwargs):
        ...
    @staticmethod
    def setHandleWidth(*args, **kwargs):
        ...
    @staticmethod
    def setOpaqueResize(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setRubberBand(*args, **kwargs):
        ...
    @staticmethod
    def setSizes(*args, **kwargs):
        ...
    @staticmethod
    def setStretchFactor(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sizes(*args, **kwargs):
        ...
    @staticmethod
    def splitterMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def widget(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QSplitterHandle(QWidget):
    @staticmethod
    def closestLegalPosition(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveSplitter(*args, **kwargs):
        ...
    @staticmethod
    def opaqueResize(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def splitter(*args, **kwargs):
        ...
class QStackedLayout(QLayout):
    class StackingMode(enum.Enum):
        StackAll: typing.ClassVar[QStackedLayout.StackingMode]  # value = <StackingMode.StackAll: 1>
        StackOne: typing.ClassVar[QStackedLayout.StackingMode]  # value = <StackingMode.StackOne: 0>
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def currentWidget(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def insertWidget(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentWidget(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setStackingMode(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def stackingMode(*args, **kwargs):
        ...
    @staticmethod
    def takeAt(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
    @staticmethod
    def widgetRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QStackedWidget(QFrame):
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def currentWidget(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def insertWidget(*args, **kwargs):
        ...
    @staticmethod
    def removeWidget(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentWidget(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
    @staticmethod
    def widgetRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    def __len__(self):
        """
        Return len(self).
        """
class QStatusBar(QWidget):
    @staticmethod
    def addPermanentWidget(*args, **kwargs):
        ...
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def clearMessage(*args, **kwargs):
        ...
    @staticmethod
    def currentMessage(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def hideOrShow(*args, **kwargs):
        ...
    @staticmethod
    def insertPermanentWidget(*args, **kwargs):
        ...
    @staticmethod
    def insertWidget(*args, **kwargs):
        ...
    @staticmethod
    def isSizeGripEnabled(*args, **kwargs):
        ...
    @staticmethod
    def messageChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def reformat(*args, **kwargs):
        ...
    @staticmethod
    def removeWidget(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setSizeGripEnabled(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def showMessage(*args, **kwargs):
        ...
class QStyle(PyQt6.QtCore.QObject):
    class ComplexControl(enum.IntEnum):
        CC_ComboBox: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_ComboBox: 1>
        CC_CustomBase: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_CustomBase: 4026531840>
        CC_Dial: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_Dial: 6>
        CC_GroupBox: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_GroupBox: 7>
        CC_MdiControls: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_MdiControls: 8>
        CC_ScrollBar: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_ScrollBar: 2>
        CC_Slider: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_Slider: 3>
        CC_SpinBox: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_SpinBox: 0>
        CC_TitleBar: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_TitleBar: 5>
        CC_ToolButton: typing.ClassVar[QStyle.ComplexControl]  # value = <ComplexControl.CC_ToolButton: 4>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class ContentsType(enum.IntEnum):
        CT_CheckBox: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_CheckBox: 1>
        CT_ComboBox: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_ComboBox: 4>
        CT_CustomBase: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_CustomBase: 4026531840>
        CT_DialogButtons: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_DialogButtons: 18>
        CT_GroupBox: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_GroupBox: 20>
        CT_HeaderSection: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_HeaderSection: 19>
        CT_ItemViewItem: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_ItemViewItem: 22>
        CT_LineEdit: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_LineEdit: 14>
        CT_MdiControls: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_MdiControls: 21>
        CT_Menu: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_Menu: 10>
        CT_MenuBar: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_MenuBar: 9>
        CT_MenuBarItem: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_MenuBarItem: 8>
        CT_MenuItem: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_MenuItem: 7>
        CT_ProgressBar: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_ProgressBar: 6>
        CT_PushButton: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_PushButton: 0>
        CT_RadioButton: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_RadioButton: 2>
        CT_ScrollBar: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_ScrollBar: 13>
        CT_SizeGrip: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_SizeGrip: 16>
        CT_Slider: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_Slider: 12>
        CT_SpinBox: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_SpinBox: 15>
        CT_Splitter: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_Splitter: 5>
        CT_TabBarTab: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_TabBarTab: 11>
        CT_TabWidget: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_TabWidget: 17>
        CT_ToolButton: typing.ClassVar[QStyle.ContentsType]  # value = <ContentsType.CT_ToolButton: 3>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class ControlElement(enum.IntEnum):
        CE_CheckBox: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_CheckBox: 3>
        CE_CheckBoxLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_CheckBoxLabel: 4>
        CE_ColumnViewGrip: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ColumnViewGrip: 44>
        CE_ComboBoxLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ComboBoxLabel: 39>
        CE_CustomBase: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_CustomBase: 4026531840>
        CE_DockWidgetTitle: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_DockWidgetTitle: 30>
        CE_FocusFrame: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_FocusFrame: 38>
        CE_Header: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_Header: 23>
        CE_HeaderEmptyArea: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_HeaderEmptyArea: 43>
        CE_HeaderLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_HeaderLabel: 25>
        CE_HeaderSection: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_HeaderSection: 24>
        CE_ItemViewItem: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ItemViewItem: 45>
        CE_MenuBarEmptyArea: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuBarEmptyArea: 21>
        CE_MenuBarItem: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuBarItem: 20>
        CE_MenuEmptyArea: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuEmptyArea: 19>
        CE_MenuHMargin: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuHMargin: 17>
        CE_MenuItem: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuItem: 14>
        CE_MenuScroller: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuScroller: 15>
        CE_MenuTearoff: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuTearoff: 18>
        CE_MenuVMargin: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_MenuVMargin: 16>
        CE_ProgressBar: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ProgressBar: 10>
        CE_ProgressBarContents: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ProgressBarContents: 12>
        CE_ProgressBarGroove: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ProgressBarGroove: 11>
        CE_ProgressBarLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ProgressBarLabel: 13>
        CE_PushButton: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_PushButton: 0>
        CE_PushButtonBevel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_PushButtonBevel: 1>
        CE_PushButtonLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_PushButtonLabel: 2>
        CE_RadioButton: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_RadioButton: 5>
        CE_RadioButtonLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_RadioButtonLabel: 6>
        CE_RubberBand: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_RubberBand: 29>
        CE_ScrollBarAddLine: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ScrollBarAddLine: 31>
        CE_ScrollBarAddPage: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ScrollBarAddPage: 33>
        CE_ScrollBarFirst: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ScrollBarFirst: 36>
        CE_ScrollBarLast: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ScrollBarLast: 37>
        CE_ScrollBarSlider: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ScrollBarSlider: 35>
        CE_ScrollBarSubLine: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ScrollBarSubLine: 32>
        CE_ScrollBarSubPage: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ScrollBarSubPage: 34>
        CE_ShapedFrame: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ShapedFrame: 46>
        CE_SizeGrip: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_SizeGrip: 27>
        CE_Splitter: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_Splitter: 28>
        CE_TabBarTab: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_TabBarTab: 7>
        CE_TabBarTabLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_TabBarTabLabel: 9>
        CE_TabBarTabShape: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_TabBarTabShape: 8>
        CE_ToolBar: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ToolBar: 40>
        CE_ToolBoxTab: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ToolBoxTab: 26>
        CE_ToolBoxTabLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ToolBoxTabLabel: 42>
        CE_ToolBoxTabShape: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ToolBoxTabShape: 41>
        CE_ToolButtonLabel: typing.ClassVar[QStyle.ControlElement]  # value = <ControlElement.CE_ToolButtonLabel: 22>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class PixelMetric(enum.IntEnum):
        PM_ButtonDefaultIndicator: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ButtonDefaultIndicator: 1>
        PM_ButtonIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ButtonIconSize: 72>
        PM_ButtonMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ButtonMargin: 0>
        PM_ButtonShiftHorizontal: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ButtonShiftHorizontal: 3>
        PM_ButtonShiftVertical: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ButtonShiftVertical: 4>
        PM_CheckBoxLabelSpacing: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_CheckBoxLabelSpacing: 67>
        PM_ComboBoxFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ComboBoxFrameWidth: 7>
        PM_CustomBase: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_CustomBase: 4026531840>
        PM_DefaultFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DefaultFrameWidth: 5>
        PM_DialogButtonsButtonHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DialogButtonsButtonHeight: 43>
        PM_DialogButtonsButtonWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DialogButtonsButtonWidth: 42>
        PM_DialogButtonsSeparator: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DialogButtonsSeparator: 41>
        PM_DockWidgetFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DockWidgetFrameWidth: 18>
        PM_DockWidgetHandleExtent: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DockWidgetHandleExtent: 17>
        PM_DockWidgetSeparatorExtent: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DockWidgetSeparatorExtent: 16>
        PM_DockWidgetTitleBarButtonMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DockWidgetTitleBarButtonMargin: 73>
        PM_DockWidgetTitleMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_DockWidgetTitleMargin: 70>
        PM_ExclusiveIndicatorHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ExclusiveIndicatorHeight: 40>
        PM_ExclusiveIndicatorWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ExclusiveIndicatorWidth: 39>
        PM_FocusFrameHMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_FocusFrameHMargin: 65>
        PM_FocusFrameVMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_FocusFrameVMargin: 64>
        PM_HeaderDefaultSectionSizeHorizontal: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_HeaderDefaultSectionSizeHorizontal: 89>
        PM_HeaderDefaultSectionSizeVertical: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_HeaderDefaultSectionSizeVertical: 90>
        PM_HeaderGripMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_HeaderGripMargin: 48>
        PM_HeaderMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_HeaderMargin: 46>
        PM_HeaderMarkSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_HeaderMarkSize: 47>
        PM_IconViewIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_IconViewIconSize: 61>
        PM_IndicatorHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_IndicatorHeight: 38>
        PM_IndicatorWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_IndicatorWidth: 37>
        PM_LargeIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LargeIconSize: 63>
        PM_LayoutBottomMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LayoutBottomMargin: 78>
        PM_LayoutHorizontalSpacing: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LayoutHorizontalSpacing: 79>
        PM_LayoutLeftMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LayoutLeftMargin: 75>
        PM_LayoutRightMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LayoutRightMargin: 77>
        PM_LayoutTopMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LayoutTopMargin: 76>
        PM_LayoutVerticalSpacing: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LayoutVerticalSpacing: 80>
        PM_LineEditIconMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LineEditIconMargin: 94>
        PM_LineEditIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_LineEditIconSize: 93>
        PM_ListViewIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ListViewIconSize: 60>
        PM_MaximumDragDistance: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MaximumDragDistance: 8>
        PM_MdiSubWindowFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MdiSubWindowFrameWidth: 44>
        PM_MdiSubWindowMinimizedWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MdiSubWindowMinimizedWidth: 45>
        PM_MenuBarHMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuBarHMargin: 36>
        PM_MenuBarItemSpacing: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuBarItemSpacing: 34>
        PM_MenuBarPanelWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuBarPanelWidth: 33>
        PM_MenuBarVMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuBarVMargin: 35>
        PM_MenuButtonIndicator: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuButtonIndicator: 2>
        PM_MenuDesktopFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuDesktopFrameWidth: 32>
        PM_MenuHMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuHMargin: 28>
        PM_MenuPanelWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuPanelWidth: 30>
        PM_MenuScrollerHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuScrollerHeight: 27>
        PM_MenuTearoffHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuTearoffHeight: 31>
        PM_MenuVMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MenuVMargin: 29>
        PM_MessageBoxIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_MessageBoxIconSize: 71>
        PM_ProgressBarChunkWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ProgressBarChunkWidth: 24>
        PM_RadioButtonLabelSpacing: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_RadioButtonLabelSpacing: 74>
        PM_ScrollBarExtent: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ScrollBarExtent: 9>
        PM_ScrollBarSliderMin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ScrollBarSliderMin: 10>
        PM_ScrollView_ScrollBarOverlap: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ScrollView_ScrollBarOverlap: 86>
        PM_ScrollView_ScrollBarSpacing: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ScrollView_ScrollBarSpacing: 85>
        PM_SizeGripSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SizeGripSize: 69>
        PM_SliderControlThickness: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SliderControlThickness: 12>
        PM_SliderLength: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SliderLength: 13>
        PM_SliderSpaceAvailable: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SliderSpaceAvailable: 15>
        PM_SliderThickness: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SliderThickness: 11>
        PM_SliderTickmarkOffset: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SliderTickmarkOffset: 14>
        PM_SmallIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SmallIconSize: 62>
        PM_SpinBoxFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SpinBoxFrameWidth: 6>
        PM_SpinBoxSliderHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SpinBoxSliderHeight: 58>
        PM_SplitterWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SplitterWidth: 25>
        PM_SubMenuOverlap: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_SubMenuOverlap: 87>
        PM_TabBarBaseHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarBaseHeight: 22>
        PM_TabBarBaseOverlap: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarBaseOverlap: 23>
        PM_TabBarIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarIconSize: 68>
        PM_TabBarScrollButtonWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarScrollButtonWidth: 51>
        PM_TabBarTabHSpace: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarTabHSpace: 20>
        PM_TabBarTabOverlap: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarTabOverlap: 19>
        PM_TabBarTabShiftHorizontal: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarTabShiftHorizontal: 49>
        PM_TabBarTabShiftVertical: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarTabShiftVertical: 50>
        PM_TabBarTabVSpace: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBarTabVSpace: 21>
        PM_TabBar_ScrollButtonOverlap: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabBar_ScrollButtonOverlap: 81>
        PM_TabCloseIndicatorHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabCloseIndicatorHeight: 84>
        PM_TabCloseIndicatorWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TabCloseIndicatorWidth: 83>
        PM_TextCursorWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TextCursorWidth: 82>
        PM_TitleBarButtonIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TitleBarButtonIconSize: 91>
        PM_TitleBarButtonSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TitleBarButtonSize: 92>
        PM_TitleBarHeight: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TitleBarHeight: 26>
        PM_ToolBarExtensionExtent: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolBarExtensionExtent: 57>
        PM_ToolBarFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolBarFrameWidth: 52>
        PM_ToolBarHandleExtent: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolBarHandleExtent: 53>
        PM_ToolBarIconSize: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolBarIconSize: 59>
        PM_ToolBarItemMargin: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolBarItemMargin: 55>
        PM_ToolBarItemSpacing: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolBarItemSpacing: 54>
        PM_ToolBarSeparatorExtent: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolBarSeparatorExtent: 56>
        PM_ToolTipLabelFrameWidth: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_ToolTipLabelFrameWidth: 66>
        PM_TreeViewIndentation: typing.ClassVar[QStyle.PixelMetric]  # value = <PixelMetric.PM_TreeViewIndentation: 88>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class PrimitiveElement(enum.IntEnum):
        PE_CustomBase: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_CustomBase: 251658240>
        PE_Frame: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_Frame: 0>
        PE_FrameButtonBevel: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameButtonBevel: 10>
        PE_FrameButtonTool: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameButtonTool: 11>
        PE_FrameDefaultButton: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameDefaultButton: 1>
        PE_FrameDockWidget: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameDockWidget: 2>
        PE_FrameFocusRect: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameFocusRect: 3>
        PE_FrameGroupBox: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameGroupBox: 4>
        PE_FrameLineEdit: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameLineEdit: 5>
        PE_FrameMenu: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameMenu: 6>
        PE_FrameStatusBarItem: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameStatusBarItem: 7>
        PE_FrameTabBarBase: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameTabBarBase: 12>
        PE_FrameTabWidget: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameTabWidget: 8>
        PE_FrameWindow: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_FrameWindow: 9>
        PE_IndicatorArrowDown: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorArrowDown: 19>
        PE_IndicatorArrowLeft: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorArrowLeft: 20>
        PE_IndicatorArrowRight: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorArrowRight: 21>
        PE_IndicatorArrowUp: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorArrowUp: 22>
        PE_IndicatorBranch: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorBranch: 23>
        PE_IndicatorButtonDropDown: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorButtonDropDown: 24>
        PE_IndicatorCheckBox: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorCheckBox: 26>
        PE_IndicatorColumnViewArrow: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorColumnViewArrow: 42>
        PE_IndicatorDockWidgetResizeHandle: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorDockWidgetResizeHandle: 27>
        PE_IndicatorHeaderArrow: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorHeaderArrow: 28>
        PE_IndicatorItemViewItemCheck: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorItemViewItemCheck: 25>
        PE_IndicatorItemViewItemDrop: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorItemViewItemDrop: 43>
        PE_IndicatorMenuCheckMark: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorMenuCheckMark: 29>
        PE_IndicatorProgressChunk: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorProgressChunk: 30>
        PE_IndicatorRadioButton: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorRadioButton: 31>
        PE_IndicatorSpinDown: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorSpinDown: 32>
        PE_IndicatorSpinMinus: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorSpinMinus: 33>
        PE_IndicatorSpinPlus: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorSpinPlus: 34>
        PE_IndicatorSpinUp: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorSpinUp: 35>
        PE_IndicatorTabClose: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorTabClose: 47>
        PE_IndicatorTabTear: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorTabTear: 39>
        PE_IndicatorTabTearRight: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorTabTearRight: 49>
        PE_IndicatorToolBarHandle: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorToolBarHandle: 36>
        PE_IndicatorToolBarSeparator: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_IndicatorToolBarSeparator: 37>
        PE_PanelButtonBevel: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelButtonBevel: 14>
        PE_PanelButtonCommand: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelButtonCommand: 13>
        PE_PanelButtonTool: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelButtonTool: 15>
        PE_PanelItemViewItem: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelItemViewItem: 44>
        PE_PanelItemViewRow: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelItemViewRow: 45>
        PE_PanelLineEdit: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelLineEdit: 18>
        PE_PanelMenu: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelMenu: 48>
        PE_PanelMenuBar: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelMenuBar: 16>
        PE_PanelScrollAreaCorner: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelScrollAreaCorner: 40>
        PE_PanelStatusBar: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelStatusBar: 46>
        PE_PanelTipLabel: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelTipLabel: 38>
        PE_PanelToolBar: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_PanelToolBar: 17>
        PE_Widget: typing.ClassVar[QStyle.PrimitiveElement]  # value = <PrimitiveElement.PE_Widget: 41>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class RequestSoftwareInputPanel(enum.Enum):
        RSIP_OnMouseClick: typing.ClassVar[QStyle.RequestSoftwareInputPanel]  # value = <RequestSoftwareInputPanel.RSIP_OnMouseClick: 1>
        RSIP_OnMouseClickAndAlreadyFocused: typing.ClassVar[QStyle.RequestSoftwareInputPanel]  # value = <RequestSoftwareInputPanel.RSIP_OnMouseClickAndAlreadyFocused: 0>
    class StandardPixmap(enum.IntEnum):
        SP_ArrowBack: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ArrowBack: 54>
        SP_ArrowDown: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ArrowDown: 51>
        SP_ArrowForward: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ArrowForward: 55>
        SP_ArrowLeft: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ArrowLeft: 52>
        SP_ArrowRight: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ArrowRight: 53>
        SP_ArrowUp: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ArrowUp: 50>
        SP_BrowserReload: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_BrowserReload: 59>
        SP_BrowserStop: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_BrowserStop: 60>
        SP_CommandLink: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_CommandLink: 57>
        SP_ComputerIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ComputerIcon: 15>
        SP_CustomBase: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_CustomBase: 4026531840>
        SP_DesktopIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DesktopIcon: 13>
        SP_DialogAbortButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogAbortButton: 74>
        SP_DialogApplyButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogApplyButton: 45>
        SP_DialogCancelButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogCancelButton: 40>
        SP_DialogCloseButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogCloseButton: 44>
        SP_DialogDiscardButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogDiscardButton: 47>
        SP_DialogHelpButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogHelpButton: 41>
        SP_DialogIgnoreButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogIgnoreButton: 76>
        SP_DialogNoButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogNoButton: 49>
        SP_DialogNoToAllButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogNoToAllButton: 72>
        SP_DialogOkButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogOkButton: 39>
        SP_DialogOpenButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogOpenButton: 42>
        SP_DialogResetButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogResetButton: 46>
        SP_DialogRetryButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogRetryButton: 75>
        SP_DialogSaveAllButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogSaveAllButton: 73>
        SP_DialogSaveButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogSaveButton: 43>
        SP_DialogYesButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogYesButton: 48>
        SP_DialogYesToAllButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DialogYesToAllButton: 71>
        SP_DirClosedIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DirClosedIcon: 22>
        SP_DirHomeIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DirHomeIcon: 56>
        SP_DirIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DirIcon: 38>
        SP_DirLinkIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DirLinkIcon: 23>
        SP_DirLinkOpenIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DirLinkOpenIcon: 24>
        SP_DirOpenIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DirOpenIcon: 21>
        SP_DockWidgetCloseButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DockWidgetCloseButton: 8>
        SP_DriveCDIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DriveCDIcon: 18>
        SP_DriveDVDIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DriveDVDIcon: 19>
        SP_DriveFDIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DriveFDIcon: 16>
        SP_DriveHDIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DriveHDIcon: 17>
        SP_DriveNetIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_DriveNetIcon: 20>
        SP_FileDialogBack: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogBack: 37>
        SP_FileDialogContentsView: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogContentsView: 35>
        SP_FileDialogDetailedView: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogDetailedView: 33>
        SP_FileDialogEnd: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogEnd: 30>
        SP_FileDialogInfoView: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogInfoView: 34>
        SP_FileDialogListView: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogListView: 36>
        SP_FileDialogNewFolder: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogNewFolder: 32>
        SP_FileDialogStart: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogStart: 29>
        SP_FileDialogToParent: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileDialogToParent: 31>
        SP_FileIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileIcon: 25>
        SP_FileLinkIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_FileLinkIcon: 26>
        SP_LineEditClearButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_LineEditClearButton: 70>
        SP_MediaPause: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaPause: 63>
        SP_MediaPlay: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaPlay: 61>
        SP_MediaSeekBackward: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaSeekBackward: 67>
        SP_MediaSeekForward: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaSeekForward: 66>
        SP_MediaSkipBackward: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaSkipBackward: 65>
        SP_MediaSkipForward: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaSkipForward: 64>
        SP_MediaStop: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaStop: 62>
        SP_MediaVolume: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaVolume: 68>
        SP_MediaVolumeMuted: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MediaVolumeMuted: 69>
        SP_MessageBoxCritical: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MessageBoxCritical: 11>
        SP_MessageBoxInformation: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MessageBoxInformation: 9>
        SP_MessageBoxQuestion: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MessageBoxQuestion: 12>
        SP_MessageBoxWarning: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_MessageBoxWarning: 10>
        SP_RestoreDefaultsButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_RestoreDefaultsButton: 77>
        SP_TabCloseButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TabCloseButton: 78>
        SP_TitleBarCloseButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarCloseButton: 3>
        SP_TitleBarContextHelpButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarContextHelpButton: 7>
        SP_TitleBarMaxButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarMaxButton: 2>
        SP_TitleBarMenuButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarMenuButton: 0>
        SP_TitleBarMinButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarMinButton: 1>
        SP_TitleBarNormalButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarNormalButton: 4>
        SP_TitleBarShadeButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarShadeButton: 5>
        SP_TitleBarUnshadeButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TitleBarUnshadeButton: 6>
        SP_ToolBarHorizontalExtensionButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ToolBarHorizontalExtensionButton: 27>
        SP_ToolBarVerticalExtensionButton: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_ToolBarVerticalExtensionButton: 28>
        SP_TrashIcon: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_TrashIcon: 14>
        SP_VistaShield: typing.ClassVar[QStyle.StandardPixmap]  # value = <StandardPixmap.SP_VistaShield: 58>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class StateFlag(enum.Flag):
        State_Active: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Active: 65536>
        State_AutoRaise: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_AutoRaise: 4096>
        State_Bottom: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Bottom: 1024>
        State_Children: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Children: 524288>
        State_DownArrow: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_DownArrow: 64>
        State_Editing: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Editing: 4194304>
        State_Enabled: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Enabled: 1>
        State_FocusAtBorder: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_FocusAtBorder: 2048>
        State_HasFocus: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_HasFocus: 256>
        State_Horizontal: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Horizontal: 128>
        State_Item: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Item: 1048576>
        State_KeyboardFocusChange: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_KeyboardFocusChange: 8388608>
        State_Mini: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Mini: 134217728>
        State_MouseOver: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_MouseOver: 8192>
        State_NoChange: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_NoChange: 16>
        State_Off: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Off: 8>
        State_On: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_On: 32>
        State_Open: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Open: 262144>
        State_Raised: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Raised: 2>
        State_ReadOnly: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_ReadOnly: 33554432>
        State_Selected: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Selected: 32768>
        State_Sibling: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Sibling: 2097152>
        State_Small: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Small: 67108864>
        State_Sunken: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Sunken: 4>
        State_Top: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Top: 512>
        State_UpArrow: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_UpArrow: 16384>
        State_Window: typing.ClassVar[QStyle.StateFlag]  # value = <StateFlag.State_Window: 131072>
    class StyleHint(enum.IntEnum):
        SH_BlinkCursorWhenTextSelected: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_BlinkCursorWhenTextSelected: 28>
        SH_Button_FocusPolicy: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Button_FocusPolicy: 49>
        SH_ComboBox_AllowWheelScrolling: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ComboBox_AllowWheelScrolling: 114>
        SH_ComboBox_LayoutDirection: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ComboBox_LayoutDirection: 58>
        SH_ComboBox_ListMouseTracking: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ComboBox_ListMouseTracking: 19>
        SH_ComboBox_Popup: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ComboBox_Popup: 25>
        SH_ComboBox_PopupFrameStyle: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ComboBox_PopupFrameStyle: 69>
        SH_CustomBase: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_CustomBase: 4026531840>
        SH_Dial_BackgroundRole: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Dial_BackgroundRole: 57>
        SH_DialogButtonBox_ButtonsHaveIcons: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_DialogButtonBox_ButtonsHaveIcons: 71>
        SH_DialogButtonLayout: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_DialogButtonLayout: 68>
        SH_DialogButtons_DefaultButton: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_DialogButtons_DefaultButton: 36>
        SH_DitherDisabledText: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_DitherDisabledText: 1>
        SH_DockWidget_ButtonsHaveFrame: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_DockWidget_ButtonsHaveFrame: 93>
        SH_DrawMenuBarSeparator: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_DrawMenuBarSeparator: 47>
        SH_EtchDisabledText: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_EtchDisabledText: 0>
        SH_FocusFrame_AboveWidget: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_FocusFrame_AboveWidget: 76>
        SH_FocusFrame_Mask: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_FocusFrame_Mask: 53>
        SH_FontDialog_SelectAssociatedText: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_FontDialog_SelectAssociatedText: 13>
        SH_FormLayoutFieldGrowthPolicy: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_FormLayoutFieldGrowthPolicy: 88>
        SH_FormLayoutFormAlignment: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_FormLayoutFormAlignment: 89>
        SH_FormLayoutLabelAlignment: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_FormLayoutLabelAlignment: 90>
        SH_FormLayoutWrapPolicy: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_FormLayoutWrapPolicy: 85>
        SH_GroupBox_TextLabelColor: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_GroupBox_TextLabelColor: 32>
        SH_GroupBox_TextLabelVerticalAlignment: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_GroupBox_TextLabelVerticalAlignment: 31>
        SH_Header_ArrowAlignment: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Header_ArrowAlignment: 6>
        SH_ItemView_ActivateItemOnSingleClick: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_ActivateItemOnSingleClick: 61>
        SH_ItemView_ArrowKeysNavigateIntoChildren: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_ArrowKeysNavigateIntoChildren: 79>
        SH_ItemView_ChangeHighlightOnFocus: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_ChangeHighlightOnFocus: 22>
        SH_ItemView_DrawDelegateFrame: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_DrawDelegateFrame: 91>
        SH_ItemView_EllipsisLocation: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_EllipsisLocation: 59>
        SH_ItemView_MovementWithoutUpdatingSelection: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_MovementWithoutUpdatingSelection: 74>
        SH_ItemView_PaintAlternatingRowColorsForEmptyArea: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_PaintAlternatingRowColorsForEmptyArea: 84>
        SH_ItemView_ScrollMode: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_ScrollMode: 111>
        SH_ItemView_ShowDecorationSelected: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ItemView_ShowDecorationSelected: 60>
        SH_LineEdit_PasswordCharacter: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_LineEdit_PasswordCharacter: 35>
        SH_LineEdit_PasswordMaskDelay: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_LineEdit_PasswordMaskDelay: 103>
        SH_ListViewExpand_SelectMouseType: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ListViewExpand_SelectMouseType: 40>
        SH_MainWindow_SpaceBelowMenuBar: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_MainWindow_SpaceBelowMenuBar: 12>
        SH_MenuBar_AltKeyNavigation: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_MenuBar_AltKeyNavigation: 18>
        SH_MenuBar_MouseTracking: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_MenuBar_MouseTracking: 21>
        SH_Menu_AllowActiveAndDisabled: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_AllowActiveAndDisabled: 14>
        SH_Menu_FadeOutOnHide: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_FadeOutOnHide: 82>
        SH_Menu_FillScreenWithScroll: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_FillScreenWithScroll: 45>
        SH_Menu_FlashTriggeredItem: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_FlashTriggeredItem: 81>
        SH_Menu_KeyboardSearch: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_KeyboardSearch: 66>
        SH_Menu_Mask: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_Mask: 80>
        SH_Menu_MouseTracking: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_MouseTracking: 20>
        SH_Menu_Scrollable: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_Scrollable: 30>
        SH_Menu_SelectionWrap: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SelectionWrap: 73>
        SH_Menu_SloppySubMenus: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SloppySubMenus: 33>
        SH_Menu_SpaceActivatesItem: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SpaceActivatesItem: 15>
        SH_Menu_SubMenuDontStartSloppyOnLeave: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SubMenuDontStartSloppyOnLeave: 110>
        SH_Menu_SubMenuPopupDelay: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SubMenuPopupDelay: 16>
        SH_Menu_SubMenuResetWhenReenteringParent: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SubMenuResetWhenReenteringParent: 109>
        SH_Menu_SubMenuSloppyCloseTimeout: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SubMenuSloppyCloseTimeout: 108>
        SH_Menu_SubMenuSloppySelectOtherActions: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SubMenuSloppySelectOtherActions: 107>
        SH_Menu_SubMenuUniDirection: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SubMenuUniDirection: 105>
        SH_Menu_SubMenuUniDirectionFailCount: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SubMenuUniDirectionFailCount: 106>
        SH_Menu_SupportsSections: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Menu_SupportsSections: 97>
        SH_MessageBox_CenterButtons: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_MessageBox_CenterButtons: 72>
        SH_MessageBox_TextInteractionFlags: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_MessageBox_TextInteractionFlags: 70>
        SH_MessageBox_UseBorderForButtonSpacing: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_MessageBox_UseBorderForButtonSpacing: 50>
        SH_PrintDialog_RightAlignButtons: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_PrintDialog_RightAlignButtons: 11>
        SH_ProgressDialog_CenterCancelButton: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ProgressDialog_CenterCancelButton: 9>
        SH_ProgressDialog_TextLabelAlignment: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ProgressDialog_TextLabelAlignment: 10>
        SH_RequestSoftwareInputPanel: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_RequestSoftwareInputPanel: 95>
        SH_RichText_FullWidthSelection: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_RichText_FullWidthSelection: 29>
        SH_RubberBand_Mask: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_RubberBand_Mask: 54>
        SH_ScrollBar_ContextMenu: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ScrollBar_ContextMenu: 62>
        SH_ScrollBar_LeftClickAbsolutePosition: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ScrollBar_LeftClickAbsolutePosition: 39>
        SH_ScrollBar_MiddleClickAbsolutePosition: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ScrollBar_MiddleClickAbsolutePosition: 2>
        SH_ScrollBar_RollBetweenButtons: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ScrollBar_RollBetweenButtons: 63>
        SH_ScrollBar_ScrollWhenPointerLeavesControl: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ScrollBar_ScrollWhenPointerLeavesControl: 3>
        SH_ScrollBar_Transient: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ScrollBar_Transient: 96>
        SH_ScrollView_FrameOnlyAroundContents: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ScrollView_FrameOnlyAroundContents: 17>
        SH_Slider_AbsoluteSetButtons: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Slider_AbsoluteSetButtons: 64>
        SH_Slider_PageSetButtons: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Slider_PageSetButtons: 65>
        SH_Slider_SloppyKeyEvents: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Slider_SloppyKeyEvents: 8>
        SH_Slider_SnapToValue: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Slider_SnapToValue: 7>
        SH_Slider_StopMouseOverSlider: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Slider_StopMouseOverSlider: 27>
        SH_SpinBox_AnimateButton: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinBox_AnimateButton: 42>
        SH_SpinBox_ButtonsInsideFrame: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinBox_ButtonsInsideFrame: 115>
        SH_SpinBox_ClickAutoRepeatRate: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinBox_ClickAutoRepeatRate: 44>
        SH_SpinBox_ClickAutoRepeatThreshold: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinBox_ClickAutoRepeatThreshold: 83>
        SH_SpinBox_KeyPressAutoRepeatRate: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinBox_KeyPressAutoRepeatRate: 43>
        SH_SpinBox_SelectOnStep: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinBox_SelectOnStep: 119>
        SH_SpinBox_StepModifier: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinBox_StepModifier: 116>
        SH_SpinControls_DisableOnBounds: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_SpinControls_DisableOnBounds: 56>
        SH_Splitter_OpaqueResize: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Splitter_OpaqueResize: 101>
        SH_TabBar_Alignment: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabBar_Alignment: 5>
        SH_TabBar_AllowWheelScrolling: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabBar_AllowWheelScrolling: 117>
        SH_TabBar_ChangeCurrentDelay: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabBar_ChangeCurrentDelay: 104>
        SH_TabBar_CloseButtonPosition: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabBar_CloseButtonPosition: 92>
        SH_TabBar_ElideMode: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabBar_ElideMode: 67>
        SH_TabBar_PreferNoArrows: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabBar_PreferNoArrows: 38>
        SH_TabBar_SelectMouseType: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabBar_SelectMouseType: 4>
        SH_TabWidget_DefaultTabPosition: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TabWidget_DefaultTabPosition: 86>
        SH_Table_AlwaysDrawLeftTopGridLines: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Table_AlwaysDrawLeftTopGridLines: 118>
        SH_Table_GridLineColor: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Table_GridLineColor: 34>
        SH_TextControl_FocusIndicatorTextCharFormat: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TextControl_FocusIndicatorTextCharFormat: 77>
        SH_TitleBar_AutoRaise: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TitleBar_AutoRaise: 51>
        SH_TitleBar_ModifyNotification: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TitleBar_ModifyNotification: 48>
        SH_TitleBar_NoBorder: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TitleBar_NoBorder: 26>
        SH_TitleBar_ShowToolTipsOnButtons: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_TitleBar_ShowToolTipsOnButtons: 112>
        SH_ToolBar_Movable: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolBar_Movable: 87>
        SH_ToolBox_SelectedPageTitleBold: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolBox_SelectedPageTitleBold: 37>
        SH_ToolButtonStyle: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolButtonStyle: 94>
        SH_ToolButton_PopupDelay: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolButton_PopupDelay: 52>
        SH_ToolTipLabel_Opacity: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolTipLabel_Opacity: 46>
        SH_ToolTip_FallAsleepDelay: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolTip_FallAsleepDelay: 99>
        SH_ToolTip_Mask: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolTip_Mask: 75>
        SH_ToolTip_WakeUpDelay: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_ToolTip_WakeUpDelay: 98>
        SH_UnderlineShortcut: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_UnderlineShortcut: 41>
        SH_Widget_Animate: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Widget_Animate: 100>
        SH_Widget_Animation_Duration: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Widget_Animation_Duration: 113>
        SH_Widget_ShareActivation: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Widget_ShareActivation: 23>
        SH_WindowFrame_Mask: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_WindowFrame_Mask: 55>
        SH_WizardStyle: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_WizardStyle: 78>
        SH_Workspace_FillSpaceOnMaximize: typing.ClassVar[QStyle.StyleHint]  # value = <StyleHint.SH_Workspace_FillSpaceOnMaximize: 24>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class SubControl(enum.Flag):
        SC_ScrollBarAddLine: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarAddLine: 1>
        SC_ScrollBarAddPage: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarAddPage: 4>
        SC_ScrollBarFirst: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarFirst: 16>
        SC_ScrollBarGroove: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarGroove: 128>
        SC_ScrollBarLast: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarLast: 32>
        SC_ScrollBarSlider: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarSlider: 64>
        SC_ScrollBarSubLine: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarSubLine: 2>
        SC_ScrollBarSubPage: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_ScrollBarSubPage: 8>
        SC_TitleBarLabel: typing.ClassVar[QStyle.SubControl]  # value = <SubControl.SC_TitleBarLabel: 256>
    class SubElement(enum.IntEnum):
        SE_CheckBoxClickRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_CheckBoxClickRect: 5>
        SE_CheckBoxContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_CheckBoxContents: 3>
        SE_CheckBoxFocusRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_CheckBoxFocusRect: 4>
        SE_CheckBoxIndicator: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_CheckBoxIndicator: 2>
        SE_CheckBoxLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_CheckBoxLayoutItem: 32>
        SE_ComboBoxFocusRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ComboBoxFocusRect: 10>
        SE_ComboBoxLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ComboBoxLayoutItem: 33>
        SE_CustomBase: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_CustomBase: 4026531840>
        SE_DateTimeEditLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_DateTimeEditLayoutItem: 34>
        SE_DockWidgetCloseButton: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_DockWidgetCloseButton: 28>
        SE_DockWidgetFloatButton: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_DockWidgetFloatButton: 29>
        SE_DockWidgetIcon: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_DockWidgetIcon: 31>
        SE_DockWidgetTitleBarText: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_DockWidgetTitleBarText: 30>
        SE_FrameContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_FrameContents: 27>
        SE_FrameLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_FrameLayoutItem: 42>
        SE_GroupBoxLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_GroupBoxLayoutItem: 43>
        SE_HeaderArrow: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_HeaderArrow: 17>
        SE_HeaderLabel: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_HeaderLabel: 16>
        SE_ItemViewItemCheckIndicator: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ItemViewItemCheckIndicator: 23>
        SE_ItemViewItemDecoration: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ItemViewItemDecoration: 45>
        SE_ItemViewItemFocusRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ItemViewItemFocusRect: 47>
        SE_ItemViewItemText: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ItemViewItemText: 46>
        SE_LabelLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_LabelLayoutItem: 35>
        SE_LineEditContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_LineEditContents: 26>
        SE_ProgressBarContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ProgressBarContents: 13>
        SE_ProgressBarGroove: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ProgressBarGroove: 12>
        SE_ProgressBarLabel: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ProgressBarLabel: 14>
        SE_ProgressBarLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ProgressBarLayoutItem: 36>
        SE_PushButtonBevel: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_PushButtonBevel: 56>
        SE_PushButtonContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_PushButtonContents: 0>
        SE_PushButtonFocusRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_PushButtonFocusRect: 1>
        SE_PushButtonLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_PushButtonLayoutItem: 37>
        SE_RadioButtonClickRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_RadioButtonClickRect: 9>
        SE_RadioButtonContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_RadioButtonContents: 7>
        SE_RadioButtonFocusRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_RadioButtonFocusRect: 8>
        SE_RadioButtonIndicator: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_RadioButtonIndicator: 6>
        SE_RadioButtonLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_RadioButtonLayoutItem: 38>
        SE_ShapedFrameContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ShapedFrameContents: 51>
        SE_SliderFocusRect: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_SliderFocusRect: 11>
        SE_SliderLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_SliderLayoutItem: 39>
        SE_SpinBoxLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_SpinBoxLayoutItem: 40>
        SE_TabBarScrollLeftButton: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabBarScrollLeftButton: 53>
        SE_TabBarScrollRightButton: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabBarScrollRightButton: 54>
        SE_TabBarTabLeftButton: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabBarTabLeftButton: 48>
        SE_TabBarTabRightButton: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabBarTabRightButton: 49>
        SE_TabBarTabText: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabBarTabText: 50>
        SE_TabBarTearIndicator: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabBarTearIndicator: 24>
        SE_TabBarTearIndicatorRight: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabBarTearIndicatorRight: 55>
        SE_TabWidgetLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabWidgetLayoutItem: 44>
        SE_TabWidgetLeftCorner: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabWidgetLeftCorner: 21>
        SE_TabWidgetRightCorner: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabWidgetRightCorner: 22>
        SE_TabWidgetTabBar: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabWidgetTabBar: 18>
        SE_TabWidgetTabContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabWidgetTabContents: 20>
        SE_TabWidgetTabPane: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TabWidgetTabPane: 19>
        SE_ToolBarHandle: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ToolBarHandle: 52>
        SE_ToolBoxTabContents: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ToolBoxTabContents: 15>
        SE_ToolButtonLayoutItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_ToolButtonLayoutItem: 41>
        SE_TreeViewDisclosureItem: typing.ClassVar[QStyle.SubElement]  # value = <SubElement.SE_TreeViewDisclosureItem: 25>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    @staticmethod
    def alignedRect(*args, **kwargs):
        ...
    @staticmethod
    def combinedLayoutSpacing(*args, **kwargs):
        ...
    @staticmethod
    def drawComplexControl(*args, **kwargs):
        ...
    @staticmethod
    def drawControl(*args, **kwargs):
        ...
    @staticmethod
    def drawItemPixmap(*args, **kwargs):
        ...
    @staticmethod
    def drawItemText(*args, **kwargs):
        ...
    @staticmethod
    def drawPrimitive(*args, **kwargs):
        ...
    @staticmethod
    def generatedIconPixmap(*args, **kwargs):
        ...
    @staticmethod
    def hitTestComplexControl(*args, **kwargs):
        ...
    @staticmethod
    def itemPixmapRect(*args, **kwargs):
        ...
    @staticmethod
    def itemTextRect(*args, **kwargs):
        ...
    @staticmethod
    def layoutSpacing(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def pixelMetric(*args, **kwargs):
        ...
    @staticmethod
    def polish(*args, **kwargs):
        ...
    @staticmethod
    def proxy(*args, **kwargs):
        ...
    @staticmethod
    def sizeFromContents(*args, **kwargs):
        ...
    @staticmethod
    def sliderPositionFromValue(*args, **kwargs):
        ...
    @staticmethod
    def sliderValueFromPosition(*args, **kwargs):
        ...
    @staticmethod
    def standardIcon(*args, **kwargs):
        ...
    @staticmethod
    def standardPalette(*args, **kwargs):
        ...
    @staticmethod
    def standardPixmap(*args, **kwargs):
        ...
    @staticmethod
    def styleHint(*args, **kwargs):
        ...
    @staticmethod
    def subControlRect(*args, **kwargs):
        ...
    @staticmethod
    def subElementRect(*args, **kwargs):
        ...
    @staticmethod
    def unpolish(*args, **kwargs):
        ...
    @staticmethod
    def visualAlignment(*args, **kwargs):
        ...
    @staticmethod
    def visualPos(*args, **kwargs):
        ...
    @staticmethod
    def visualRect(*args, **kwargs):
        ...
class QStyleFactory(PyQt6.sip.simplewrapper):
    @staticmethod
    def create(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
class QStyleHintReturn(PyQt6.sip.simplewrapper):
    class HintReturnType(enum.Enum):
        SH_Default: typing.ClassVar[QStyleHintReturn.HintReturnType]  # value = <HintReturnType.SH_Default: 61440>
        SH_Mask: typing.ClassVar[QStyleHintReturn.HintReturnType]  # value = <HintReturnType.SH_Mask: 61441>
        SH_Variant: typing.ClassVar[QStyleHintReturn.HintReturnType]  # value = <HintReturnType.SH_Variant: 61442>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleHintReturn.StyleOptionType]  # value = <StyleOptionType.Type: 61440>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleHintReturn.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleHintReturnMask(QStyleHintReturn):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleHintReturnMask.StyleOptionType]  # value = <StyleOptionType.Type: 61441>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleHintReturnMask.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleHintReturnVariant(QStyleHintReturn):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleHintReturnVariant.StyleOptionType]  # value = <StyleOptionType.Type: 61442>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleHintReturnVariant.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOption(PyQt6.sip.simplewrapper):
    class OptionType(enum.Enum):
        SO_Button: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_Button: 2>
        SO_ComboBox: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_ComboBox: 983044>
        SO_Complex: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_Complex: 983040>
        SO_ComplexCustomBase: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_ComplexCustomBase: 251658240>
        SO_CustomBase: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_CustomBase: 3840>
        SO_Default: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_Default: 0>
        SO_DockWidget: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_DockWidget: 9>
        SO_FocusRect: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_FocusRect: 1>
        SO_Frame: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_Frame: 5>
        SO_GraphicsItem: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_GraphicsItem: 15>
        SO_GroupBox: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_GroupBox: 983046>
        SO_Header: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_Header: 8>
        SO_MenuItem: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_MenuItem: 4>
        SO_ProgressBar: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_ProgressBar: 6>
        SO_RubberBand: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_RubberBand: 13>
        SO_SizeGrip: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_SizeGrip: 983047>
        SO_Slider: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_Slider: 983041>
        SO_SpinBox: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_SpinBox: 983042>
        SO_Tab: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_Tab: 3>
        SO_TabBarBase: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_TabBarBase: 12>
        SO_TabWidgetFrame: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_TabWidgetFrame: 11>
        SO_TitleBar: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_TitleBar: 983045>
        SO_ToolBar: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_ToolBar: 14>
        SO_ToolBox: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_ToolBox: 7>
        SO_ToolButton: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_ToolButton: 983043>
        SO_ViewItem: typing.ClassVar[QStyleOption.OptionType]  # value = <OptionType.SO_ViewItem: 10>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOption.StyleOptionType]  # value = <StyleOptionType.Type: 0>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOption.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
    @staticmethod
    def initFrom(*args, **kwargs):
        ...
class QStyleOptionButton(QStyleOption):
    class ButtonFeature(enum.Flag):
        AutoDefaultButton: typing.ClassVar[QStyleOptionButton.ButtonFeature]  # value = <ButtonFeature.AutoDefaultButton: 8>
        CommandLinkButton: typing.ClassVar[QStyleOptionButton.ButtonFeature]  # value = <ButtonFeature.CommandLinkButton: 16>
        DefaultButton: typing.ClassVar[QStyleOptionButton.ButtonFeature]  # value = <ButtonFeature.DefaultButton: 4>
        Flat: typing.ClassVar[QStyleOptionButton.ButtonFeature]  # value = <ButtonFeature.Flat: 1>
        HasMenu: typing.ClassVar[QStyleOptionButton.ButtonFeature]  # value = <ButtonFeature.HasMenu: 2>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionButton.StyleOptionType]  # value = <StyleOptionType.Type: 2>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionButton.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionComboBox(QStyleOptionComplex):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionComboBox.StyleOptionType]  # value = <StyleOptionType.Type: 983044>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionComboBox.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionComplex(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionComplex.StyleOptionType]  # value = <StyleOptionType.Type: 983040>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionComplex.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionDockWidget(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionDockWidget.StyleOptionType]  # value = <StyleOptionType.Type: 9>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionDockWidget.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionFocusRect(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionFocusRect.StyleOptionType]  # value = <StyleOptionType.Type: 1>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionFocusRect.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionFrame(QStyleOption):
    class FrameFeature(enum.Flag):
        Flat: typing.ClassVar[QStyleOptionFrame.FrameFeature]  # value = <FrameFeature.Flat: 1>
        Rounded: typing.ClassVar[QStyleOptionFrame.FrameFeature]  # value = <FrameFeature.Rounded: 2>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionFrame.StyleOptionType]  # value = <StyleOptionType.Type: 5>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionFrame.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionGraphicsItem(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionGraphicsItem.StyleOptionType]  # value = <StyleOptionType.Type: 15>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionGraphicsItem.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
    @staticmethod
    def levelOfDetailFromTransform(*args, **kwargs):
        ...
class QStyleOptionGroupBox(QStyleOptionComplex):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionGroupBox.StyleOptionType]  # value = <StyleOptionType.Type: 983046>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionGroupBox.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionHeader(QStyleOption):
    class SectionPosition(enum.Enum):
        Beginning: typing.ClassVar[QStyleOptionHeader.SectionPosition]  # value = <SectionPosition.Beginning: 0>
        End: typing.ClassVar[QStyleOptionHeader.SectionPosition]  # value = <SectionPosition.End: 2>
        Middle: typing.ClassVar[QStyleOptionHeader.SectionPosition]  # value = <SectionPosition.Middle: 1>
        OnlyOneSection: typing.ClassVar[QStyleOptionHeader.SectionPosition]  # value = <SectionPosition.OnlyOneSection: 3>
    class SelectedPosition(enum.Enum):
        NextAndPreviousAreSelected: typing.ClassVar[QStyleOptionHeader.SelectedPosition]  # value = <SelectedPosition.NextAndPreviousAreSelected: 3>
        NextIsSelected: typing.ClassVar[QStyleOptionHeader.SelectedPosition]  # value = <SelectedPosition.NextIsSelected: 1>
        NotAdjacent: typing.ClassVar[QStyleOptionHeader.SelectedPosition]  # value = <SelectedPosition.NotAdjacent: 0>
        PreviousIsSelected: typing.ClassVar[QStyleOptionHeader.SelectedPosition]  # value = <SelectedPosition.PreviousIsSelected: 2>
    class SortIndicator(enum.Enum):
        None_: typing.ClassVar[QStyleOptionHeader.SortIndicator]  # value = <SortIndicator.None_: 0>
        SortDown: typing.ClassVar[QStyleOptionHeader.SortIndicator]  # value = <SortIndicator.SortDown: 2>
        SortUp: typing.ClassVar[QStyleOptionHeader.SortIndicator]  # value = <SortIndicator.SortUp: 1>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionHeader.StyleOptionType]  # value = <StyleOptionType.Type: 8>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionHeader.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionHeaderV2(QStyleOptionHeader):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionHeaderV2.StyleOptionType]  # value = <StyleOptionType.Type: 8>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionHeaderV2.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 2>
class QStyleOptionMenuItem(QStyleOption):
    class CheckType(enum.Enum):
        Exclusive: typing.ClassVar[QStyleOptionMenuItem.CheckType]  # value = <CheckType.Exclusive: 1>
        NonExclusive: typing.ClassVar[QStyleOptionMenuItem.CheckType]  # value = <CheckType.NonExclusive: 2>
        NotCheckable: typing.ClassVar[QStyleOptionMenuItem.CheckType]  # value = <CheckType.NotCheckable: 0>
    class MenuItemType(enum.Enum):
        DefaultItem: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.DefaultItem: 1>
        EmptyArea: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.EmptyArea: 7>
        Margin: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.Margin: 6>
        Normal: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.Normal: 0>
        Scroller: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.Scroller: 4>
        Separator: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.Separator: 2>
        SubMenu: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.SubMenu: 3>
        TearOff: typing.ClassVar[QStyleOptionMenuItem.MenuItemType]  # value = <MenuItemType.TearOff: 5>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionMenuItem.StyleOptionType]  # value = <StyleOptionType.Type: 4>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionMenuItem.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionProgressBar(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionProgressBar.StyleOptionType]  # value = <StyleOptionType.Type: 6>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionProgressBar.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionRubberBand(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionRubberBand.StyleOptionType]  # value = <StyleOptionType.Type: 13>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionRubberBand.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionSizeGrip(QStyleOptionComplex):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionSizeGrip.StyleOptionType]  # value = <StyleOptionType.Type: 983047>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionSizeGrip.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionSlider(QStyleOptionComplex):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionSlider.StyleOptionType]  # value = <StyleOptionType.Type: 983041>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionSlider.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionSpinBox(QStyleOptionComplex):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionSpinBox.StyleOptionType]  # value = <StyleOptionType.Type: 983042>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionSpinBox.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionTab(QStyleOption):
    class CornerWidget(enum.Flag):
        LeftCornerWidget: typing.ClassVar[QStyleOptionTab.CornerWidget]  # value = <CornerWidget.LeftCornerWidget: 1>
        RightCornerWidget: typing.ClassVar[QStyleOptionTab.CornerWidget]  # value = <CornerWidget.RightCornerWidget: 2>
    class SelectedPosition(enum.Enum):
        NextIsSelected: typing.ClassVar[QStyleOptionTab.SelectedPosition]  # value = <SelectedPosition.NextIsSelected: 1>
        NotAdjacent: typing.ClassVar[QStyleOptionTab.SelectedPosition]  # value = <SelectedPosition.NotAdjacent: 0>
        PreviousIsSelected: typing.ClassVar[QStyleOptionTab.SelectedPosition]  # value = <SelectedPosition.PreviousIsSelected: 2>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionTab.StyleOptionType]  # value = <StyleOptionType.Type: 3>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionTab.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
    class TabFeature(enum.Flag):
        HasFrame: typing.ClassVar[QStyleOptionTab.TabFeature]  # value = <TabFeature.HasFrame: 1>
    class TabPosition(enum.Enum):
        Beginning: typing.ClassVar[QStyleOptionTab.TabPosition]  # value = <TabPosition.Beginning: 0>
        End: typing.ClassVar[QStyleOptionTab.TabPosition]  # value = <TabPosition.End: 2>
        Middle: typing.ClassVar[QStyleOptionTab.TabPosition]  # value = <TabPosition.Middle: 1>
        Moving: typing.ClassVar[QStyleOptionTab.TabPosition]  # value = <TabPosition.Moving: 4>
        OnlyOneTab: typing.ClassVar[QStyleOptionTab.TabPosition]  # value = <TabPosition.OnlyOneTab: 3>
class QStyleOptionTabBarBase(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionTabBarBase.StyleOptionType]  # value = <StyleOptionType.Type: 12>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionTabBarBase.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionTabWidgetFrame(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionTabWidgetFrame.StyleOptionType]  # value = <StyleOptionType.Type: 11>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionTabWidgetFrame.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionTitleBar(QStyleOptionComplex):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionTitleBar.StyleOptionType]  # value = <StyleOptionType.Type: 983045>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionTitleBar.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
class QStyleOptionToolBar(QStyleOption):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionToolBar.StyleOptionType]  # value = <StyleOptionType.Type: 14>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionToolBar.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
    class ToolBarFeature(enum.Flag):
        Movable: typing.ClassVar[QStyleOptionToolBar.ToolBarFeature]  # value = <ToolBarFeature.Movable: 1>
    class ToolBarPosition(enum.Enum):
        Beginning: typing.ClassVar[QStyleOptionToolBar.ToolBarPosition]  # value = <ToolBarPosition.Beginning: 0>
        End: typing.ClassVar[QStyleOptionToolBar.ToolBarPosition]  # value = <ToolBarPosition.End: 2>
        Middle: typing.ClassVar[QStyleOptionToolBar.ToolBarPosition]  # value = <ToolBarPosition.Middle: 1>
        OnlyOne: typing.ClassVar[QStyleOptionToolBar.ToolBarPosition]  # value = <ToolBarPosition.OnlyOne: 3>
class QStyleOptionToolBox(QStyleOption):
    class SelectedPosition(enum.Enum):
        NextIsSelected: typing.ClassVar[QStyleOptionToolBox.SelectedPosition]  # value = <SelectedPosition.NextIsSelected: 1>
        NotAdjacent: typing.ClassVar[QStyleOptionToolBox.SelectedPosition]  # value = <SelectedPosition.NotAdjacent: 0>
        PreviousIsSelected: typing.ClassVar[QStyleOptionToolBox.SelectedPosition]  # value = <SelectedPosition.PreviousIsSelected: 2>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionToolBox.StyleOptionType]  # value = <StyleOptionType.Type: 7>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionToolBox.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
    class TabPosition(enum.Enum):
        Beginning: typing.ClassVar[QStyleOptionToolBox.TabPosition]  # value = <TabPosition.Beginning: 0>
        End: typing.ClassVar[QStyleOptionToolBox.TabPosition]  # value = <TabPosition.End: 2>
        Middle: typing.ClassVar[QStyleOptionToolBox.TabPosition]  # value = <TabPosition.Middle: 1>
        OnlyOneTab: typing.ClassVar[QStyleOptionToolBox.TabPosition]  # value = <TabPosition.OnlyOneTab: 3>
class QStyleOptionToolButton(QStyleOptionComplex):
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionToolButton.StyleOptionType]  # value = <StyleOptionType.Type: 983043>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionToolButton.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
    class ToolButtonFeature(enum.Flag):
        Arrow: typing.ClassVar[QStyleOptionToolButton.ToolButtonFeature]  # value = <ToolButtonFeature.Arrow: 1>
        HasMenu: typing.ClassVar[QStyleOptionToolButton.ToolButtonFeature]  # value = <ToolButtonFeature.HasMenu: 16>
        Menu: typing.ClassVar[QStyleOptionToolButton.ToolButtonFeature]  # value = <ToolButtonFeature.Menu: 4>
        PopupDelay: typing.ClassVar[QStyleOptionToolButton.ToolButtonFeature]  # value = <ToolButtonFeature.PopupDelay: 8>
class QStyleOptionViewItem(QStyleOption):
    class Position(enum.Enum):
        Bottom: typing.ClassVar[QStyleOptionViewItem.Position]  # value = <Position.Bottom: 3>
        Left: typing.ClassVar[QStyleOptionViewItem.Position]  # value = <Position.Left: 0>
        Right: typing.ClassVar[QStyleOptionViewItem.Position]  # value = <Position.Right: 1>
        Top: typing.ClassVar[QStyleOptionViewItem.Position]  # value = <Position.Top: 2>
    class StyleOptionType(enum.Enum):
        Type: typing.ClassVar[QStyleOptionViewItem.StyleOptionType]  # value = <StyleOptionType.Type: 10>
    class StyleOptionVersion(enum.Enum):
        Version: typing.ClassVar[QStyleOptionViewItem.StyleOptionVersion]  # value = <StyleOptionVersion.Version: 1>
    class ViewItemFeature(enum.Flag):
        Alternate: typing.ClassVar[QStyleOptionViewItem.ViewItemFeature]  # value = <ViewItemFeature.Alternate: 2>
        HasCheckIndicator: typing.ClassVar[QStyleOptionViewItem.ViewItemFeature]  # value = <ViewItemFeature.HasCheckIndicator: 4>
        HasDecoration: typing.ClassVar[QStyleOptionViewItem.ViewItemFeature]  # value = <ViewItemFeature.HasDecoration: 16>
        HasDisplay: typing.ClassVar[QStyleOptionViewItem.ViewItemFeature]  # value = <ViewItemFeature.HasDisplay: 8>
        WrapText: typing.ClassVar[QStyleOptionViewItem.ViewItemFeature]  # value = <ViewItemFeature.WrapText: 1>
    class ViewItemPosition(enum.Enum):
        Beginning: typing.ClassVar[QStyleOptionViewItem.ViewItemPosition]  # value = <ViewItemPosition.Beginning: 1>
        End: typing.ClassVar[QStyleOptionViewItem.ViewItemPosition]  # value = <ViewItemPosition.End: 3>
        Invalid: typing.ClassVar[QStyleOptionViewItem.ViewItemPosition]  # value = <ViewItemPosition.Invalid: 0>
        Middle: typing.ClassVar[QStyleOptionViewItem.ViewItemPosition]  # value = <ViewItemPosition.Middle: 2>
        OnlyOne: typing.ClassVar[QStyleOptionViewItem.ViewItemPosition]  # value = <ViewItemPosition.OnlyOne: 4>
class QStylePainter(PyQt6.QtGui.QPainter):
    @staticmethod
    def begin(*args, **kwargs):
        ...
    @staticmethod
    def drawComplexControl(*args, **kwargs):
        ...
    @staticmethod
    def drawControl(*args, **kwargs):
        ...
    @staticmethod
    def drawItemPixmap(*args, **kwargs):
        ...
    @staticmethod
    def drawItemText(*args, **kwargs):
        ...
    @staticmethod
    def drawPrimitive(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
class QStyledItemDelegate(QAbstractItemDelegate):
    @staticmethod
    def createEditor(*args, **kwargs):
        ...
    @staticmethod
    def displayText(*args, **kwargs):
        ...
    @staticmethod
    def editorEvent(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def itemEditorFactory(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def setEditorData(*args, **kwargs):
        ...
    @staticmethod
    def setItemEditorFactory(*args, **kwargs):
        ...
    @staticmethod
    def setModelData(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def updateEditorGeometry(*args, **kwargs):
        ...
class QSwipeGesture(QGesture):
    class SwipeDirection(enum.Enum):
        Down: typing.ClassVar[QSwipeGesture.SwipeDirection]  # value = <SwipeDirection.Down: 4>
        Left: typing.ClassVar[QSwipeGesture.SwipeDirection]  # value = <SwipeDirection.Left: 1>
        NoDirection: typing.ClassVar[QSwipeGesture.SwipeDirection]  # value = <SwipeDirection.NoDirection: 0>
        Right: typing.ClassVar[QSwipeGesture.SwipeDirection]  # value = <SwipeDirection.Right: 2>
        Up: typing.ClassVar[QSwipeGesture.SwipeDirection]  # value = <SwipeDirection.Up: 3>
    @staticmethod
    def horizontalDirection(*args, **kwargs):
        ...
    @staticmethod
    def setSwipeAngle(*args, **kwargs):
        ...
    @staticmethod
    def swipeAngle(*args, **kwargs):
        ...
    @staticmethod
    def verticalDirection(*args, **kwargs):
        ...
class QSystemTrayIcon(PyQt6.QtCore.QObject):
    class ActivationReason(enum.Enum):
        Context: typing.ClassVar[QSystemTrayIcon.ActivationReason]  # value = <ActivationReason.Context: 1>
        DoubleClick: typing.ClassVar[QSystemTrayIcon.ActivationReason]  # value = <ActivationReason.DoubleClick: 2>
        MiddleClick: typing.ClassVar[QSystemTrayIcon.ActivationReason]  # value = <ActivationReason.MiddleClick: 4>
        Trigger: typing.ClassVar[QSystemTrayIcon.ActivationReason]  # value = <ActivationReason.Trigger: 3>
        Unknown: typing.ClassVar[QSystemTrayIcon.ActivationReason]  # value = <ActivationReason.Unknown: 0>
    class MessageIcon(enum.Enum):
        Critical: typing.ClassVar[QSystemTrayIcon.MessageIcon]  # value = <MessageIcon.Critical: 3>
        Information: typing.ClassVar[QSystemTrayIcon.MessageIcon]  # value = <MessageIcon.Information: 1>
        NoIcon: typing.ClassVar[QSystemTrayIcon.MessageIcon]  # value = <MessageIcon.NoIcon: 0>
        Warning: typing.ClassVar[QSystemTrayIcon.MessageIcon]  # value = <MessageIcon.Warning: 2>
    @staticmethod
    def activated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def contextMenu(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def hide(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def isSystemTrayAvailable(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def messageClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setContextMenu(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def show(*args, **kwargs):
        ...
    @staticmethod
    def showMessage(*args, **kwargs):
        ...
    @staticmethod
    def supportsMessages(*args, **kwargs):
        ...
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
class QTabBar(QWidget):
    class ButtonPosition(enum.Enum):
        LeftSide: typing.ClassVar[QTabBar.ButtonPosition]  # value = <ButtonPosition.LeftSide: 0>
        RightSide: typing.ClassVar[QTabBar.ButtonPosition]  # value = <ButtonPosition.RightSide: 1>
    class SelectionBehavior(enum.Enum):
        SelectLeftTab: typing.ClassVar[QTabBar.SelectionBehavior]  # value = <SelectionBehavior.SelectLeftTab: 0>
        SelectPreviousTab: typing.ClassVar[QTabBar.SelectionBehavior]  # value = <SelectionBehavior.SelectPreviousTab: 2>
        SelectRightTab: typing.ClassVar[QTabBar.SelectionBehavior]  # value = <SelectionBehavior.SelectRightTab: 1>
    class Shape(enum.Enum):
        RoundedEast: typing.ClassVar[QTabBar.Shape]  # value = <Shape.RoundedEast: 3>
        RoundedNorth: typing.ClassVar[QTabBar.Shape]  # value = <Shape.RoundedNorth: 0>
        RoundedSouth: typing.ClassVar[QTabBar.Shape]  # value = <Shape.RoundedSouth: 1>
        RoundedWest: typing.ClassVar[QTabBar.Shape]  # value = <Shape.RoundedWest: 2>
        TriangularEast: typing.ClassVar[QTabBar.Shape]  # value = <Shape.TriangularEast: 7>
        TriangularNorth: typing.ClassVar[QTabBar.Shape]  # value = <Shape.TriangularNorth: 4>
        TriangularSouth: typing.ClassVar[QTabBar.Shape]  # value = <Shape.TriangularSouth: 5>
        TriangularWest: typing.ClassVar[QTabBar.Shape]  # value = <Shape.TriangularWest: 6>
    @staticmethod
    def accessibleTabName(*args, **kwargs):
        ...
    @staticmethod
    def addTab(*args, **kwargs):
        ...
    @staticmethod
    def autoHide(*args, **kwargs):
        ...
    @staticmethod
    def changeCurrentOnDrag(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def documentMode(*args, **kwargs):
        ...
    @staticmethod
    def drawBase(*args, **kwargs):
        ...
    @staticmethod
    def elideMode(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def expanding(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def iconSize(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def insertTab(*args, **kwargs):
        ...
    @staticmethod
    def isMovable(*args, **kwargs):
        ...
    @staticmethod
    def isTabEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isTabVisible(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def minimumTabSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveTab(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def removeTab(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def selectionBehaviorOnRemove(*args, **kwargs):
        ...
    @staticmethod
    def setAccessibleTabName(*args, **kwargs):
        ...
    @staticmethod
    def setAutoHide(*args, **kwargs):
        ...
    @staticmethod
    def setChangeCurrentOnDrag(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentMode(*args, **kwargs):
        ...
    @staticmethod
    def setDrawBase(*args, **kwargs):
        ...
    @staticmethod
    def setElideMode(*args, **kwargs):
        ...
    @staticmethod
    def setExpanding(*args, **kwargs):
        ...
    @staticmethod
    def setIconSize(*args, **kwargs):
        ...
    @staticmethod
    def setMovable(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionBehaviorOnRemove(*args, **kwargs):
        ...
    @staticmethod
    def setShape(*args, **kwargs):
        ...
    @staticmethod
    def setTabButton(*args, **kwargs):
        ...
    @staticmethod
    def setTabData(*args, **kwargs):
        ...
    @staticmethod
    def setTabEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setTabIcon(*args, **kwargs):
        ...
    @staticmethod
    def setTabText(*args, **kwargs):
        ...
    @staticmethod
    def setTabTextColor(*args, **kwargs):
        ...
    @staticmethod
    def setTabToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setTabVisible(*args, **kwargs):
        ...
    @staticmethod
    def setTabWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def setTabsClosable(*args, **kwargs):
        ...
    @staticmethod
    def setUsesScrollButtons(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def tabAt(*args, **kwargs):
        ...
    @staticmethod
    def tabBarClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabBarDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabButton(*args, **kwargs):
        ...
    @staticmethod
    def tabCloseRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabData(*args, **kwargs):
        ...
    @staticmethod
    def tabIcon(*args, **kwargs):
        ...
    @staticmethod
    def tabInserted(*args, **kwargs):
        ...
    @staticmethod
    def tabLayoutChange(*args, **kwargs):
        ...
    @staticmethod
    def tabMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabRect(*args, **kwargs):
        ...
    @staticmethod
    def tabRemoved(*args, **kwargs):
        ...
    @staticmethod
    def tabSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def tabText(*args, **kwargs):
        ...
    @staticmethod
    def tabTextColor(*args, **kwargs):
        ...
    @staticmethod
    def tabToolTip(*args, **kwargs):
        ...
    @staticmethod
    def tabWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def tabsClosable(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def usesScrollButtons(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QTabWidget(QWidget):
    class TabPosition(enum.Enum):
        East: typing.ClassVar[QTabWidget.TabPosition]  # value = <TabPosition.East: 3>
        North: typing.ClassVar[QTabWidget.TabPosition]  # value = <TabPosition.North: 0>
        South: typing.ClassVar[QTabWidget.TabPosition]  # value = <TabPosition.South: 1>
        West: typing.ClassVar[QTabWidget.TabPosition]  # value = <TabPosition.West: 2>
    class TabShape(enum.Enum):
        Rounded: typing.ClassVar[QTabWidget.TabShape]  # value = <TabShape.Rounded: 0>
        Triangular: typing.ClassVar[QTabWidget.TabShape]  # value = <TabShape.Triangular: 1>
    @staticmethod
    def addTab(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def cornerWidget(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def currentWidget(*args, **kwargs):
        ...
    @staticmethod
    def documentMode(*args, **kwargs):
        ...
    @staticmethod
    def elideMode(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def iconSize(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def insertTab(*args, **kwargs):
        ...
    @staticmethod
    def isMovable(*args, **kwargs):
        ...
    @staticmethod
    def isTabEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isTabVisible(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def removeTab(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def setCornerWidget(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentWidget(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentMode(*args, **kwargs):
        ...
    @staticmethod
    def setElideMode(*args, **kwargs):
        ...
    @staticmethod
    def setIconSize(*args, **kwargs):
        ...
    @staticmethod
    def setMovable(*args, **kwargs):
        ...
    @staticmethod
    def setTabBar(*args, **kwargs):
        ...
    @staticmethod
    def setTabBarAutoHide(*args, **kwargs):
        ...
    @staticmethod
    def setTabEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setTabIcon(*args, **kwargs):
        ...
    @staticmethod
    def setTabPosition(*args, **kwargs):
        ...
    @staticmethod
    def setTabShape(*args, **kwargs):
        ...
    @staticmethod
    def setTabText(*args, **kwargs):
        ...
    @staticmethod
    def setTabToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setTabVisible(*args, **kwargs):
        ...
    @staticmethod
    def setTabWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def setTabsClosable(*args, **kwargs):
        ...
    @staticmethod
    def setUsesScrollButtons(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def tabBar(*args, **kwargs):
        ...
    @staticmethod
    def tabBarAutoHide(*args, **kwargs):
        ...
    @staticmethod
    def tabBarClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabBarDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabCloseRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def tabIcon(*args, **kwargs):
        ...
    @staticmethod
    def tabInserted(*args, **kwargs):
        ...
    @staticmethod
    def tabPosition(*args, **kwargs):
        ...
    @staticmethod
    def tabRemoved(*args, **kwargs):
        ...
    @staticmethod
    def tabShape(*args, **kwargs):
        ...
    @staticmethod
    def tabText(*args, **kwargs):
        ...
    @staticmethod
    def tabToolTip(*args, **kwargs):
        ...
    @staticmethod
    def tabWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def tabsClosable(*args, **kwargs):
        ...
    @staticmethod
    def usesScrollButtons(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QTableView(QAbstractItemView):
    @staticmethod
    def clearSpans(*args, **kwargs):
        ...
    @staticmethod
    def columnAt(*args, **kwargs):
        ...
    @staticmethod
    def columnCountChanged(*args, **kwargs):
        ...
    @staticmethod
    def columnMoved(*args, **kwargs):
        ...
    @staticmethod
    def columnResized(*args, **kwargs):
        ...
    @staticmethod
    def columnSpan(*args, **kwargs):
        ...
    @staticmethod
    def columnViewportPosition(*args, **kwargs):
        ...
    @staticmethod
    def columnWidth(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        ...
    @staticmethod
    def gridStyle(*args, **kwargs):
        ...
    @staticmethod
    def hideColumn(*args, **kwargs):
        ...
    @staticmethod
    def hideRow(*args, **kwargs):
        ...
    @staticmethod
    def horizontalHeader(*args, **kwargs):
        ...
    @staticmethod
    def horizontalOffset(*args, **kwargs):
        ...
    @staticmethod
    def horizontalScrollbarAction(*args, **kwargs):
        ...
    @staticmethod
    def indexAt(*args, **kwargs):
        ...
    @staticmethod
    def initViewItemOption(*args, **kwargs):
        ...
    @staticmethod
    def isColumnHidden(*args, **kwargs):
        ...
    @staticmethod
    def isCornerButtonEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isIndexHidden(*args, **kwargs):
        ...
    @staticmethod
    def isRowHidden(*args, **kwargs):
        ...
    @staticmethod
    def isSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def resizeColumnToContents(*args, **kwargs):
        ...
    @staticmethod
    def resizeColumnsToContents(*args, **kwargs):
        ...
    @staticmethod
    def resizeRowToContents(*args, **kwargs):
        ...
    @staticmethod
    def resizeRowsToContents(*args, **kwargs):
        ...
    @staticmethod
    def rowAt(*args, **kwargs):
        ...
    @staticmethod
    def rowCountChanged(*args, **kwargs):
        ...
    @staticmethod
    def rowHeight(*args, **kwargs):
        ...
    @staticmethod
    def rowMoved(*args, **kwargs):
        ...
    @staticmethod
    def rowResized(*args, **kwargs):
        ...
    @staticmethod
    def rowSpan(*args, **kwargs):
        ...
    @staticmethod
    def rowViewportPosition(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def scrollTo(*args, **kwargs):
        ...
    @staticmethod
    def selectColumn(*args, **kwargs):
        ...
    @staticmethod
    def selectRow(*args, **kwargs):
        ...
    @staticmethod
    def selectedIndexes(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        ...
    @staticmethod
    def setColumnHidden(*args, **kwargs):
        ...
    @staticmethod
    def setColumnWidth(*args, **kwargs):
        ...
    @staticmethod
    def setCornerButtonEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setGridStyle(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalHeader(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setRootIndex(*args, **kwargs):
        ...
    @staticmethod
    def setRowHeight(*args, **kwargs):
        ...
    @staticmethod
    def setRowHidden(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionModel(*args, **kwargs):
        ...
    @staticmethod
    def setShowGrid(*args, **kwargs):
        ...
    @staticmethod
    def setSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSpan(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalHeader(*args, **kwargs):
        ...
    @staticmethod
    def setWordWrap(*args, **kwargs):
        ...
    @staticmethod
    def showColumn(*args, **kwargs):
        ...
    @staticmethod
    def showGrid(*args, **kwargs):
        ...
    @staticmethod
    def showRow(*args, **kwargs):
        ...
    @staticmethod
    def sizeHintForColumn(*args, **kwargs):
        ...
    @staticmethod
    def sizeHintForRow(*args, **kwargs):
        ...
    @staticmethod
    def sortByColumn(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometries(*args, **kwargs):
        ...
    @staticmethod
    def verticalHeader(*args, **kwargs):
        ...
    @staticmethod
    def verticalOffset(*args, **kwargs):
        ...
    @staticmethod
    def verticalScrollbarAction(*args, **kwargs):
        ...
    @staticmethod
    def viewportSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def visualRect(*args, **kwargs):
        ...
    @staticmethod
    def visualRegionForSelection(*args, **kwargs):
        ...
    @staticmethod
    def wordWrap(*args, **kwargs):
        ...
class QTableWidget(QTableView):
    @staticmethod
    def cellActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cellChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cellClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cellDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cellEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cellPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cellWidget(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearContents(*args, **kwargs):
        ...
    @staticmethod
    def closePersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def column(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def currentCellChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentColumn(*args, **kwargs):
        ...
    @staticmethod
    def currentItem(*args, **kwargs):
        ...
    @staticmethod
    def currentItemChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentRow(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def editItem(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def findItems(*args, **kwargs):
        ...
    @staticmethod
    def horizontalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def indexFromItem(*args, **kwargs):
        ...
    @staticmethod
    def insertColumn(*args, **kwargs):
        ...
    @staticmethod
    def insertRow(*args, **kwargs):
        ...
    @staticmethod
    def isPersistentEditorOpen(*args, **kwargs):
        ...
    @staticmethod
    def isSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def item(*args, **kwargs):
        ...
    @staticmethod
    def itemActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def itemChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemFromIndex(*args, **kwargs):
        ...
    @staticmethod
    def itemPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemPrototype(*args, **kwargs):
        ...
    @staticmethod
    def itemSelectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def openPersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def removeCellWidget(*args, **kwargs):
        ...
    @staticmethod
    def removeColumn(*args, **kwargs):
        ...
    @staticmethod
    def removeRow(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def scrollToItem(*args, **kwargs):
        ...
    @staticmethod
    def selectedItems(*args, **kwargs):
        ...
    @staticmethod
    def selectedRanges(*args, **kwargs):
        ...
    @staticmethod
    def setCellWidget(*args, **kwargs):
        ...
    @staticmethod
    def setColumnCount(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentCell(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentItem(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def setHorizontalHeaderLabels(*args, **kwargs):
        ...
    @staticmethod
    def setItem(*args, **kwargs):
        ...
    @staticmethod
    def setItemPrototype(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setRangeSelected(*args, **kwargs):
        ...
    @staticmethod
    def setRowCount(*args, **kwargs):
        ...
    @staticmethod
    def setSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalHeaderLabels(*args, **kwargs):
        ...
    @staticmethod
    def sortItems(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
    @staticmethod
    def takeHorizontalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def takeItem(*args, **kwargs):
        ...
    @staticmethod
    def takeVerticalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def verticalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def visualColumn(*args, **kwargs):
        ...
    @staticmethod
    def visualItemRect(*args, **kwargs):
        ...
    @staticmethod
    def visualRow(*args, **kwargs):
        ...
class QTableWidgetItem(PyQt6.sip.wrapper):
    class ItemType(enum.IntEnum):
        Type: typing.ClassVar[QTableWidgetItem.ItemType]  # value = <ItemType.Type: 0>
        UserType: typing.ClassVar[QTableWidgetItem.ItemType]  # value = <ItemType.UserType: 1000>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def background(*args, **kwargs):
        ...
    @staticmethod
    def checkState(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def column(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def foreground(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def isSelected(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def setBackground(*args, **kwargs):
        ...
    @staticmethod
    def setCheckState(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setForeground(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setSelected(*args, **kwargs):
        ...
    @staticmethod
    def setSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def setStatusTip(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def statusTip(*args, **kwargs):
        ...
    @staticmethod
    def tableWidget(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textAlignment(*args, **kwargs):
        ...
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def whatsThis(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QTableWidgetSelectionRange(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def bottomRow(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def leftColumn(*args, **kwargs):
        ...
    @staticmethod
    def rightColumn(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def topRow(*args, **kwargs):
        ...
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QTapAndHoldGesture(QGesture):
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
    @staticmethod
    def setTimeout(*args, **kwargs):
        ...
    @staticmethod
    def timeout(*args, **kwargs):
        ...
class QTapGesture(QGesture):
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
class QTextBrowser(QTextEdit):
    @staticmethod
    def anchorClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def backward(*args, **kwargs):
        ...
    @staticmethod
    def backwardAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def backwardHistoryCount(*args, **kwargs):
        ...
    @staticmethod
    def clearHistory(*args, **kwargs):
        ...
    @staticmethod
    def doSetSource(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def forward(*args, **kwargs):
        ...
    @staticmethod
    def forwardAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def forwardHistoryCount(*args, **kwargs):
        ...
    @staticmethod
    def highlighted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def historyChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def historyTitle(*args, **kwargs):
        ...
    @staticmethod
    def historyUrl(*args, **kwargs):
        ...
    @staticmethod
    def home(*args, **kwargs):
        ...
    @staticmethod
    def isBackwardAvailable(*args, **kwargs):
        ...
    @staticmethod
    def isForwardAvailable(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def loadResource(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def openExternalLinks(*args, **kwargs):
        ...
    @staticmethod
    def openLinks(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def reload(*args, **kwargs):
        ...
    @staticmethod
    def searchPaths(*args, **kwargs):
        ...
    @staticmethod
    def setOpenExternalLinks(*args, **kwargs):
        ...
    @staticmethod
    def setOpenLinks(*args, **kwargs):
        ...
    @staticmethod
    def setSearchPaths(*args, **kwargs):
        ...
    @staticmethod
    def setSource(*args, **kwargs):
        ...
    @staticmethod
    def source(*args, **kwargs):
        ...
    @staticmethod
    def sourceChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sourceType(*args, **kwargs):
        ...
class QTextEdit(QAbstractScrollArea):
    class AutoFormattingFlag(enum.Flag):
        AutoBulletList: typing.ClassVar[QTextEdit.AutoFormattingFlag]  # value = <AutoFormattingFlag.AutoBulletList: 1>
    class ExtraSelection(PyQt6.sip.simplewrapper):
        pass
    class LineWrapMode(enum.Enum):
        FixedColumnWidth: typing.ClassVar[QTextEdit.LineWrapMode]  # value = <LineWrapMode.FixedColumnWidth: 3>
        FixedPixelWidth: typing.ClassVar[QTextEdit.LineWrapMode]  # value = <LineWrapMode.FixedPixelWidth: 2>
        NoWrap: typing.ClassVar[QTextEdit.LineWrapMode]  # value = <LineWrapMode.NoWrap: 0>
        WidgetWidth: typing.ClassVar[QTextEdit.LineWrapMode]  # value = <LineWrapMode.WidgetWidth: 1>
    @staticmethod
    def acceptRichText(*args, **kwargs):
        ...
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def anchorAt(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def autoFormatting(*args, **kwargs):
        ...
    @staticmethod
    def canInsertFromMimeData(*args, **kwargs):
        ...
    @staticmethod
    def canPaste(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def copyAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def createMimeDataFromSelection(*args, **kwargs):
        ...
    @staticmethod
    def createStandardContextMenu(*args, **kwargs):
        ...
    @staticmethod
    def currentCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def currentCharFormatChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentFont(*args, **kwargs):
        ...
    @staticmethod
    def cursorForPosition(*args, **kwargs):
        ...
    @staticmethod
    def cursorPositionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cursorRect(*args, **kwargs):
        ...
    @staticmethod
    def cursorWidth(*args, **kwargs):
        ...
    @staticmethod
    def cut(*args, **kwargs):
        ...
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def documentTitle(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def ensureCursorVisible(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def extraSelections(*args, **kwargs):
        ...
    @staticmethod
    def find(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def fontFamily(*args, **kwargs):
        ...
    @staticmethod
    def fontItalic(*args, **kwargs):
        ...
    @staticmethod
    def fontPointSize(*args, **kwargs):
        ...
    @staticmethod
    def fontUnderline(*args, **kwargs):
        ...
    @staticmethod
    def fontWeight(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def insertFromMimeData(*args, **kwargs):
        ...
    @staticmethod
    def insertHtml(*args, **kwargs):
        ...
    @staticmethod
    def insertPlainText(*args, **kwargs):
        ...
    @staticmethod
    def isReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def isUndoRedoEnabled(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def lineWrapColumnOrWidth(*args, **kwargs):
        ...
    @staticmethod
    def lineWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def loadResource(*args, **kwargs):
        ...
    @staticmethod
    def mergeCurrentCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def overwriteMode(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def paste(*args, **kwargs):
        ...
    @staticmethod
    def placeholderText(*args, **kwargs):
        ...
    @staticmethod
    def print(*args, **kwargs):
        ...
    @staticmethod
    def redo(*args, **kwargs):
        ...
    @staticmethod
    def redoAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def scrollToAnchor(*args, **kwargs):
        ...
    @staticmethod
    def selectAll(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setAcceptRichText(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setAutoFormatting(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentFont(*args, **kwargs):
        ...
    @staticmethod
    def setCursorWidth(*args, **kwargs):
        ...
    @staticmethod
    def setDocument(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentTitle(*args, **kwargs):
        ...
    @staticmethod
    def setExtraSelections(*args, **kwargs):
        ...
    @staticmethod
    def setFontFamily(*args, **kwargs):
        ...
    @staticmethod
    def setFontItalic(*args, **kwargs):
        ...
    @staticmethod
    def setFontPointSize(*args, **kwargs):
        ...
    @staticmethod
    def setFontUnderline(*args, **kwargs):
        ...
    @staticmethod
    def setFontWeight(*args, **kwargs):
        ...
    @staticmethod
    def setHtml(*args, **kwargs):
        ...
    @staticmethod
    def setLineWrapColumnOrWidth(*args, **kwargs):
        ...
    @staticmethod
    def setLineWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def setMarkdown(*args, **kwargs):
        ...
    @staticmethod
    def setOverwriteMode(*args, **kwargs):
        ...
    @staticmethod
    def setPlaceholderText(*args, **kwargs):
        ...
    @staticmethod
    def setPlainText(*args, **kwargs):
        ...
    @staticmethod
    def setReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def setTabChangesFocus(*args, **kwargs):
        ...
    @staticmethod
    def setTabStopDistance(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextBackgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def setTextColor(*args, **kwargs):
        ...
    @staticmethod
    def setTextCursor(*args, **kwargs):
        ...
    @staticmethod
    def setTextInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def setUndoRedoEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setWordWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def tabChangesFocus(*args, **kwargs):
        ...
    @staticmethod
    def tabStopDistance(*args, **kwargs):
        ...
    @staticmethod
    def textBackgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def textChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def textColor(*args, **kwargs):
        ...
    @staticmethod
    def textCursor(*args, **kwargs):
        ...
    @staticmethod
    def textInteractionFlags(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def toHtml(*args, **kwargs):
        ...
    @staticmethod
    def toMarkdown(*args, **kwargs):
        ...
    @staticmethod
    def toPlainText(*args, **kwargs):
        ...
    @staticmethod
    def undo(*args, **kwargs):
        ...
    @staticmethod
    def undoAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def wordWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def zoomIn(*args, **kwargs):
        ...
    @staticmethod
    def zoomOut(*args, **kwargs):
        ...
class QTimeEdit(QDateTimeEdit):
    pass
class QToolBar(QWidget):
    @staticmethod
    def actionAt(*args, **kwargs):
        ...
    @staticmethod
    def actionEvent(*args, **kwargs):
        ...
    @staticmethod
    def actionGeometry(*args, **kwargs):
        ...
    @staticmethod
    def actionTriggered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def addSeparator(*args, **kwargs):
        ...
    @staticmethod
    def addWidget(*args, **kwargs):
        ...
    @staticmethod
    def allowedAreas(*args, **kwargs):
        ...
    @staticmethod
    def allowedAreasChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def iconSize(*args, **kwargs):
        ...
    @staticmethod
    def iconSizeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def insertSeparator(*args, **kwargs):
        ...
    @staticmethod
    def insertWidget(*args, **kwargs):
        ...
    @staticmethod
    def isAreaAllowed(*args, **kwargs):
        ...
    @staticmethod
    def isFloatable(*args, **kwargs):
        ...
    @staticmethod
    def isFloating(*args, **kwargs):
        ...
    @staticmethod
    def isMovable(*args, **kwargs):
        ...
    @staticmethod
    def movableChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def orientationChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def setAllowedAreas(*args, **kwargs):
        ...
    @staticmethod
    def setFloatable(*args, **kwargs):
        ...
    @staticmethod
    def setIconSize(*args, **kwargs):
        ...
    @staticmethod
    def setMovable(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setToolButtonStyle(*args, **kwargs):
        ...
    @staticmethod
    def toggleViewAction(*args, **kwargs):
        ...
    @staticmethod
    def toolButtonStyle(*args, **kwargs):
        ...
    @staticmethod
    def toolButtonStyleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def topLevelChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def visibilityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def widgetForAction(*args, **kwargs):
        ...
class QToolBox(QFrame):
    @staticmethod
    def addItem(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentIndex(*args, **kwargs):
        ...
    @staticmethod
    def currentWidget(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def insertItem(*args, **kwargs):
        ...
    @staticmethod
    def isItemEnabled(*args, **kwargs):
        ...
    @staticmethod
    def itemIcon(*args, **kwargs):
        ...
    @staticmethod
    def itemInserted(*args, **kwargs):
        ...
    @staticmethod
    def itemRemoved(*args, **kwargs):
        ...
    @staticmethod
    def itemText(*args, **kwargs):
        ...
    @staticmethod
    def itemToolTip(*args, **kwargs):
        ...
    @staticmethod
    def removeItem(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentWidget(*args, **kwargs):
        ...
    @staticmethod
    def setItemEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setItemIcon(*args, **kwargs):
        ...
    @staticmethod
    def setItemText(*args, **kwargs):
        ...
    @staticmethod
    def setItemToolTip(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QToolButton(QAbstractButton):
    class ToolButtonPopupMode(enum.Enum):
        DelayedPopup: typing.ClassVar[QToolButton.ToolButtonPopupMode]  # value = <ToolButtonPopupMode.DelayedPopup: 0>
        InstantPopup: typing.ClassVar[QToolButton.ToolButtonPopupMode]  # value = <ToolButtonPopupMode.InstantPopup: 2>
        MenuButtonPopup: typing.ClassVar[QToolButton.ToolButtonPopupMode]  # value = <ToolButtonPopupMode.MenuButtonPopup: 1>
    @staticmethod
    def actionEvent(*args, **kwargs):
        ...
    @staticmethod
    def arrowType(*args, **kwargs):
        ...
    @staticmethod
    def autoRaise(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def checkStateSet(*args, **kwargs):
        ...
    @staticmethod
    def defaultAction(*args, **kwargs):
        ...
    @staticmethod
    def enterEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def hitButton(*args, **kwargs):
        ...
    @staticmethod
    def initStyleOption(*args, **kwargs):
        ...
    @staticmethod
    def leaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def menu(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def nextCheckState(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def popupMode(*args, **kwargs):
        ...
    @staticmethod
    def setArrowType(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRaise(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultAction(*args, **kwargs):
        ...
    @staticmethod
    def setMenu(*args, **kwargs):
        ...
    @staticmethod
    def setPopupMode(*args, **kwargs):
        ...
    @staticmethod
    def setToolButtonStyle(*args, **kwargs):
        ...
    @staticmethod
    def showMenu(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def toolButtonStyle(*args, **kwargs):
        ...
    @staticmethod
    def triggered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QToolTip(PyQt6.sip.simplewrapper):
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def hideText(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def palette(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setPalette(*args, **kwargs):
        ...
    @staticmethod
    def showText(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
class QTreeView(QAbstractItemView):
    @staticmethod
    def allColumnsShowFocus(*args, **kwargs):
        ...
    @staticmethod
    def autoExpandDelay(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def collapse(*args, **kwargs):
        ...
    @staticmethod
    def collapseAll(*args, **kwargs):
        ...
    @staticmethod
    def collapsed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def columnAt(*args, **kwargs):
        ...
    @staticmethod
    def columnCountChanged(*args, **kwargs):
        ...
    @staticmethod
    def columnMoved(*args, **kwargs):
        ...
    @staticmethod
    def columnResized(*args, **kwargs):
        ...
    @staticmethod
    def columnViewportPosition(*args, **kwargs):
        ...
    @staticmethod
    def columnWidth(*args, **kwargs):
        ...
    @staticmethod
    def currentChanged(*args, **kwargs):
        ...
    @staticmethod
    def dataChanged(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def drawBranches(*args, **kwargs):
        ...
    @staticmethod
    def drawRow(*args, **kwargs):
        ...
    @staticmethod
    def drawTree(*args, **kwargs):
        ...
    @staticmethod
    def expand(*args, **kwargs):
        ...
    @staticmethod
    def expandAll(*args, **kwargs):
        ...
    @staticmethod
    def expandRecursively(*args, **kwargs):
        ...
    @staticmethod
    def expandToDepth(*args, **kwargs):
        ...
    @staticmethod
    def expanded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def expandsOnDoubleClick(*args, **kwargs):
        ...
    @staticmethod
    def header(*args, **kwargs):
        ...
    @staticmethod
    def hideColumn(*args, **kwargs):
        ...
    @staticmethod
    def horizontalOffset(*args, **kwargs):
        ...
    @staticmethod
    def horizontalScrollbarAction(*args, **kwargs):
        ...
    @staticmethod
    def indentation(*args, **kwargs):
        ...
    @staticmethod
    def indexAbove(*args, **kwargs):
        ...
    @staticmethod
    def indexAt(*args, **kwargs):
        ...
    @staticmethod
    def indexBelow(*args, **kwargs):
        ...
    @staticmethod
    def indexRowSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def isAnimated(*args, **kwargs):
        ...
    @staticmethod
    def isColumnHidden(*args, **kwargs):
        ...
    @staticmethod
    def isExpanded(*args, **kwargs):
        ...
    @staticmethod
    def isFirstColumnSpanned(*args, **kwargs):
        ...
    @staticmethod
    def isHeaderHidden(*args, **kwargs):
        ...
    @staticmethod
    def isIndexHidden(*args, **kwargs):
        ...
    @staticmethod
    def isRowHidden(*args, **kwargs):
        ...
    @staticmethod
    def isSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def itemsExpandable(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyboardSearch(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def moveCursor(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def reexpand(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def resetIndentation(*args, **kwargs):
        ...
    @staticmethod
    def resizeColumnToContents(*args, **kwargs):
        ...
    @staticmethod
    def rootIsDecorated(*args, **kwargs):
        ...
    @staticmethod
    def rowHeight(*args, **kwargs):
        ...
    @staticmethod
    def rowsAboutToBeRemoved(*args, **kwargs):
        ...
    @staticmethod
    def rowsInserted(*args, **kwargs):
        ...
    @staticmethod
    def rowsRemoved(*args, **kwargs):
        ...
    @staticmethod
    def scrollContentsBy(*args, **kwargs):
        ...
    @staticmethod
    def scrollTo(*args, **kwargs):
        ...
    @staticmethod
    def selectAll(*args, **kwargs):
        ...
    @staticmethod
    def selectedIndexes(*args, **kwargs):
        ...
    @staticmethod
    def selectionChanged(*args, **kwargs):
        ...
    @staticmethod
    def setAllColumnsShowFocus(*args, **kwargs):
        ...
    @staticmethod
    def setAnimated(*args, **kwargs):
        ...
    @staticmethod
    def setAutoExpandDelay(*args, **kwargs):
        ...
    @staticmethod
    def setColumnHidden(*args, **kwargs):
        ...
    @staticmethod
    def setColumnWidth(*args, **kwargs):
        ...
    @staticmethod
    def setExpanded(*args, **kwargs):
        ...
    @staticmethod
    def setExpandsOnDoubleClick(*args, **kwargs):
        ...
    @staticmethod
    def setFirstColumnSpanned(*args, **kwargs):
        ...
    @staticmethod
    def setHeader(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderHidden(*args, **kwargs):
        ...
    @staticmethod
    def setIndentation(*args, **kwargs):
        ...
    @staticmethod
    def setItemsExpandable(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setRootIndex(*args, **kwargs):
        ...
    @staticmethod
    def setRootIsDecorated(*args, **kwargs):
        ...
    @staticmethod
    def setRowHidden(*args, **kwargs):
        ...
    @staticmethod
    def setSelection(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionModel(*args, **kwargs):
        ...
    @staticmethod
    def setSortingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setTreePosition(*args, **kwargs):
        ...
    @staticmethod
    def setUniformRowHeights(*args, **kwargs):
        ...
    @staticmethod
    def setWordWrap(*args, **kwargs):
        ...
    @staticmethod
    def showColumn(*args, **kwargs):
        ...
    @staticmethod
    def sizeHintForColumn(*args, **kwargs):
        ...
    @staticmethod
    def sortByColumn(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def treePosition(*args, **kwargs):
        ...
    @staticmethod
    def uniformRowHeights(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometries(*args, **kwargs):
        ...
    @staticmethod
    def verticalOffset(*args, **kwargs):
        ...
    @staticmethod
    def viewportEvent(*args, **kwargs):
        ...
    @staticmethod
    def viewportSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def visualRect(*args, **kwargs):
        ...
    @staticmethod
    def visualRegionForSelection(*args, **kwargs):
        ...
    @staticmethod
    def wordWrap(*args, **kwargs):
        ...
class QTreeWidget(QTreeView):
    @staticmethod
    def addTopLevelItem(*args, **kwargs):
        ...
    @staticmethod
    def addTopLevelItems(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def closePersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def collapseItem(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def currentColumn(*args, **kwargs):
        ...
    @staticmethod
    def currentItem(*args, **kwargs):
        ...
    @staticmethod
    def currentItemChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def editItem(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def expandItem(*args, **kwargs):
        ...
    @staticmethod
    def findItems(*args, **kwargs):
        ...
    @staticmethod
    def headerItem(*args, **kwargs):
        ...
    @staticmethod
    def indexFromItem(*args, **kwargs):
        ...
    @staticmethod
    def indexOfTopLevelItem(*args, **kwargs):
        ...
    @staticmethod
    def insertTopLevelItem(*args, **kwargs):
        ...
    @staticmethod
    def insertTopLevelItems(*args, **kwargs):
        ...
    @staticmethod
    def invisibleRootItem(*args, **kwargs):
        ...
    @staticmethod
    def isPersistentEditorOpen(*args, **kwargs):
        ...
    @staticmethod
    def itemAbove(*args, **kwargs):
        ...
    @staticmethod
    def itemActivated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def itemBelow(*args, **kwargs):
        ...
    @staticmethod
    def itemChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemCollapsed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemDoubleClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemEntered(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemExpanded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemFromIndex(*args, **kwargs):
        ...
    @staticmethod
    def itemPressed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemSelectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def itemWidget(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def openPersistentEditor(*args, **kwargs):
        ...
    @staticmethod
    def removeItemWidget(*args, **kwargs):
        ...
    @staticmethod
    def scrollToItem(*args, **kwargs):
        ...
    @staticmethod
    def selectedItems(*args, **kwargs):
        ...
    @staticmethod
    def setColumnCount(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentItem(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderLabel(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderLabels(*args, **kwargs):
        ...
    @staticmethod
    def setItemWidget(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
    @staticmethod
    def setSelectionModel(*args, **kwargs):
        ...
    @staticmethod
    def sortColumn(*args, **kwargs):
        ...
    @staticmethod
    def sortItems(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
    @staticmethod
    def takeTopLevelItem(*args, **kwargs):
        ...
    @staticmethod
    def topLevelItem(*args, **kwargs):
        ...
    @staticmethod
    def topLevelItemCount(*args, **kwargs):
        ...
    @staticmethod
    def visualItemRect(*args, **kwargs):
        ...
class QTreeWidgetItem(PyQt6.sip.wrapper):
    class ChildIndicatorPolicy(enum.Enum):
        DontShowIndicator: typing.ClassVar[QTreeWidgetItem.ChildIndicatorPolicy]  # value = <ChildIndicatorPolicy.DontShowIndicator: 1>
        DontShowIndicatorWhenChildless: typing.ClassVar[QTreeWidgetItem.ChildIndicatorPolicy]  # value = <ChildIndicatorPolicy.DontShowIndicatorWhenChildless: 2>
        ShowIndicator: typing.ClassVar[QTreeWidgetItem.ChildIndicatorPolicy]  # value = <ChildIndicatorPolicy.ShowIndicator: 0>
    class ItemType(enum.IntEnum):
        Type: typing.ClassVar[QTreeWidgetItem.ItemType]  # value = <ItemType.Type: 0>
        UserType: typing.ClassVar[QTreeWidgetItem.ItemType]  # value = <ItemType.UserType: 1000>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def addChild(*args, **kwargs):
        ...
    @staticmethod
    def addChildren(*args, **kwargs):
        ...
    @staticmethod
    def background(*args, **kwargs):
        ...
    @staticmethod
    def checkState(*args, **kwargs):
        ...
    @staticmethod
    def child(*args, **kwargs):
        ...
    @staticmethod
    def childCount(*args, **kwargs):
        ...
    @staticmethod
    def childIndicatorPolicy(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def emitDataChanged(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def foreground(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def indexOfChild(*args, **kwargs):
        ...
    @staticmethod
    def insertChild(*args, **kwargs):
        ...
    @staticmethod
    def insertChildren(*args, **kwargs):
        ...
    @staticmethod
    def isDisabled(*args, **kwargs):
        ...
    @staticmethod
    def isExpanded(*args, **kwargs):
        ...
    @staticmethod
    def isFirstColumnSpanned(*args, **kwargs):
        ...
    @staticmethod
    def isHidden(*args, **kwargs):
        ...
    @staticmethod
    def isSelected(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def removeChild(*args, **kwargs):
        ...
    @staticmethod
    def setBackground(*args, **kwargs):
        ...
    @staticmethod
    def setCheckState(*args, **kwargs):
        ...
    @staticmethod
    def setChildIndicatorPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setDisabled(*args, **kwargs):
        ...
    @staticmethod
    def setExpanded(*args, **kwargs):
        ...
    @staticmethod
    def setFirstColumnSpanned(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setForeground(*args, **kwargs):
        ...
    @staticmethod
    def setHidden(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setSelected(*args, **kwargs):
        ...
    @staticmethod
    def setSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def setStatusTip(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sortChildren(*args, **kwargs):
        ...
    @staticmethod
    def statusTip(*args, **kwargs):
        ...
    @staticmethod
    def takeChild(*args, **kwargs):
        ...
    @staticmethod
    def takeChildren(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textAlignment(*args, **kwargs):
        ...
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
    @staticmethod
    def treeWidget(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def whatsThis(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QTreeWidgetItemIterator(PyQt6.sip.simplewrapper):
    class IteratorFlag(enum.Flag):
        Checked: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Checked: 4096>
        Disabled: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Disabled: 32768>
        DragDisabled: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.DragDisabled: 128>
        DragEnabled: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.DragEnabled: 64>
        DropDisabled: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.DropDisabled: 512>
        DropEnabled: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.DropEnabled: 256>
        Editable: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Editable: 65536>
        Enabled: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Enabled: 16384>
        HasChildren: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.HasChildren: 1024>
        Hidden: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Hidden: 1>
        NoChildren: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.NoChildren: 2048>
        NotChecked: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.NotChecked: 8192>
        NotEditable: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.NotEditable: 131072>
        NotHidden: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.NotHidden: 2>
        NotSelectable: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.NotSelectable: 32>
        Selectable: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Selectable: 16>
        Selected: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Selected: 4>
        Unselected: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.Unselected: 8>
        UserFlag: typing.ClassVar[QTreeWidgetItemIterator.IteratorFlag]  # value = <IteratorFlag.UserFlag: 16777216>
    @staticmethod
    def value(*args, **kwargs):
        ...
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
class QUndoView(QListView):
    @staticmethod
    def cleanIcon(*args, **kwargs):
        ...
    @staticmethod
    def emptyLabel(*args, **kwargs):
        ...
    @staticmethod
    def group(*args, **kwargs):
        ...
    @staticmethod
    def setCleanIcon(*args, **kwargs):
        ...
    @staticmethod
    def setEmptyLabel(*args, **kwargs):
        ...
    @staticmethod
    def setGroup(*args, **kwargs):
        ...
    @staticmethod
    def setStack(*args, **kwargs):
        ...
    @staticmethod
    def stack(*args, **kwargs):
        ...
class QVBoxLayout(QBoxLayout):
    pass
class QWhatsThis(PyQt6.sip.simplewrapper):
    @staticmethod
    def createAction(*args, **kwargs):
        ...
    @staticmethod
    def enterWhatsThisMode(*args, **kwargs):
        ...
    @staticmethod
    def hideText(*args, **kwargs):
        ...
    @staticmethod
    def inWhatsThisMode(*args, **kwargs):
        ...
    @staticmethod
    def leaveWhatsThisMode(*args, **kwargs):
        ...
    @staticmethod
    def showText(*args, **kwargs):
        ...
class QWidget(PyQt6.QtCore.QObject, PyQt6.QtGui.QPaintDevice):
    class RenderFlag(enum.Flag):
        DrawChildren: typing.ClassVar[QWidget.RenderFlag]  # value = <RenderFlag.DrawChildren: 2>
        DrawWindowBackground: typing.ClassVar[QWidget.RenderFlag]  # value = <RenderFlag.DrawWindowBackground: 1>
        IgnoreMask: typing.ClassVar[QWidget.RenderFlag]  # value = <RenderFlag.IgnoreMask: 4>
    @staticmethod
    def acceptDrops(*args, **kwargs):
        ...
    @staticmethod
    def accessibleDescription(*args, **kwargs):
        ...
    @staticmethod
    def accessibleName(*args, **kwargs):
        ...
    @staticmethod
    def actionEvent(*args, **kwargs):
        ...
    @staticmethod
    def actions(*args, **kwargs):
        ...
    @staticmethod
    def activateWindow(*args, **kwargs):
        ...
    @staticmethod
    def addAction(*args, **kwargs):
        ...
    @staticmethod
    def addActions(*args, **kwargs):
        ...
    @staticmethod
    def adjustSize(*args, **kwargs):
        ...
    @staticmethod
    def autoFillBackground(*args, **kwargs):
        ...
    @staticmethod
    def backgroundRole(*args, **kwargs):
        ...
    @staticmethod
    def baseSize(*args, **kwargs):
        ...
    @staticmethod
    def changeEvent(*args, **kwargs):
        ...
    @staticmethod
    def childAt(*args, **kwargs):
        ...
    @staticmethod
    def childrenRect(*args, **kwargs):
        ...
    @staticmethod
    def childrenRegion(*args, **kwargs):
        ...
    @staticmethod
    def clearFocus(*args, **kwargs):
        ...
    @staticmethod
    def clearMask(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def contentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def contentsRect(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuEvent(*args, **kwargs):
        ...
    @staticmethod
    def contextMenuPolicy(*args, **kwargs):
        ...
    @staticmethod
    def create(*args, **kwargs):
        ...
    @staticmethod
    def createWindowContainer(*args, **kwargs):
        ...
    @staticmethod
    def cursor(*args, **kwargs):
        ...
    @staticmethod
    def customContextMenuRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def destroy(*args, **kwargs):
        ...
    @staticmethod
    def devType(*args, **kwargs):
        ...
    @staticmethod
    def dragEnterEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragLeaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dragMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def dropEvent(*args, **kwargs):
        ...
    @staticmethod
    def effectiveWinId(*args, **kwargs):
        ...
    @staticmethod
    def ensurePolished(*args, **kwargs):
        ...
    @staticmethod
    def enterEvent(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def find(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusNextChild(*args, **kwargs):
        ...
    @staticmethod
    def focusNextPrevChild(*args, **kwargs):
        ...
    @staticmethod
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusPolicy(*args, **kwargs):
        ...
    @staticmethod
    def focusPreviousChild(*args, **kwargs):
        ...
    @staticmethod
    def focusProxy(*args, **kwargs):
        ...
    @staticmethod
    def focusWidget(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def fontInfo(*args, **kwargs):
        ...
    @staticmethod
    def fontMetrics(*args, **kwargs):
        ...
    @staticmethod
    def foregroundRole(*args, **kwargs):
        ...
    @staticmethod
    def frameGeometry(*args, **kwargs):
        ...
    @staticmethod
    def frameSize(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def grab(*args, **kwargs):
        ...
    @staticmethod
    def grabGesture(*args, **kwargs):
        ...
    @staticmethod
    def grabKeyboard(*args, **kwargs):
        ...
    @staticmethod
    def grabMouse(*args, **kwargs):
        ...
    @staticmethod
    def grabShortcut(*args, **kwargs):
        ...
    @staticmethod
    def graphicsEffect(*args, **kwargs):
        ...
    @staticmethod
    def graphicsProxyWidget(*args, **kwargs):
        ...
    @staticmethod
    def hasFocus(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def hasMouseTracking(*args, **kwargs):
        ...
    @staticmethod
    def hasTabletTracking(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def hide(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def initPainter(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodEvent(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodHints(*args, **kwargs):
        ...
    @staticmethod
    def inputMethodQuery(*args, **kwargs):
        ...
    @staticmethod
    def insertAction(*args, **kwargs):
        ...
    @staticmethod
    def insertActions(*args, **kwargs):
        ...
    @staticmethod
    def isActiveWindow(*args, **kwargs):
        ...
    @staticmethod
    def isAncestorOf(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isEnabledTo(*args, **kwargs):
        ...
    @staticmethod
    def isFullScreen(*args, **kwargs):
        ...
    @staticmethod
    def isHidden(*args, **kwargs):
        ...
    @staticmethod
    def isLeftToRight(*args, **kwargs):
        ...
    @staticmethod
    def isMaximized(*args, **kwargs):
        ...
    @staticmethod
    def isMinimized(*args, **kwargs):
        ...
    @staticmethod
    def isModal(*args, **kwargs):
        ...
    @staticmethod
    def isRightToLeft(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def isVisibleTo(*args, **kwargs):
        ...
    @staticmethod
    def isWindow(*args, **kwargs):
        ...
    @staticmethod
    def isWindowModified(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyboardGrabber(*args, **kwargs):
        ...
    @staticmethod
    def layout(*args, **kwargs):
        ...
    @staticmethod
    def layoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def leaveEvent(*args, **kwargs):
        ...
    @staticmethod
    def locale(*args, **kwargs):
        ...
    @staticmethod
    def lower(*args, **kwargs):
        ...
    @staticmethod
    def mapFrom(*args, **kwargs):
        ...
    @staticmethod
    def mapFromGlobal(*args, **kwargs):
        ...
    @staticmethod
    def mapFromParent(*args, **kwargs):
        ...
    @staticmethod
    def mapTo(*args, **kwargs):
        ...
    @staticmethod
    def mapToGlobal(*args, **kwargs):
        ...
    @staticmethod
    def mapToParent(*args, **kwargs):
        ...
    @staticmethod
    def mask(*args, **kwargs):
        ...
    @staticmethod
    def maximumHeight(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def maximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def minimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumSizeHint(*args, **kwargs):
        ...
    @staticmethod
    def minimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseGrabber(*args, **kwargs):
        ...
    @staticmethod
    def mouseMoveEvent(*args, **kwargs):
        ...
    @staticmethod
    def mousePressEvent(*args, **kwargs):
        ...
    @staticmethod
    def mouseReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def move(*args, **kwargs):
        ...
    @staticmethod
    def moveEvent(*args, **kwargs):
        ...
    @staticmethod
    def nativeEvent(*args, **kwargs):
        ...
    @staticmethod
    def nativeParentWidget(*args, **kwargs):
        ...
    @staticmethod
    def nextInFocusChain(*args, **kwargs):
        ...
    @staticmethod
    def normalGeometry(*args, **kwargs):
        ...
    @staticmethod
    def overrideWindowFlags(*args, **kwargs):
        ...
    @staticmethod
    def overrideWindowState(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def palette(*args, **kwargs):
        ...
    @staticmethod
    def parentWidget(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def previousInFocusChain(*args, **kwargs):
        ...
    @staticmethod
    def raise_(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def releaseKeyboard(*args, **kwargs):
        ...
    @staticmethod
    def releaseMouse(*args, **kwargs):
        ...
    @staticmethod
    def releaseShortcut(*args, **kwargs):
        ...
    @staticmethod
    def removeAction(*args, **kwargs):
        ...
    @staticmethod
    def render(*args, **kwargs):
        ...
    @staticmethod
    def repaint(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def restoreGeometry(*args, **kwargs):
        ...
    @staticmethod
    def saveGeometry(*args, **kwargs):
        ...
    @staticmethod
    def screen(*args, **kwargs):
        ...
    @staticmethod
    def scroll(*args, **kwargs):
        ...
    @staticmethod
    def setAcceptDrops(*args, **kwargs):
        ...
    @staticmethod
    def setAccessibleDescription(*args, **kwargs):
        ...
    @staticmethod
    def setAccessibleName(*args, **kwargs):
        ...
    @staticmethod
    def setAttribute(*args, **kwargs):
        ...
    @staticmethod
    def setAutoFillBackground(*args, **kwargs):
        ...
    @staticmethod
    def setBackgroundRole(*args, **kwargs):
        ...
    @staticmethod
    def setBaseSize(*args, **kwargs):
        ...
    @staticmethod
    def setContentsMargins(*args, **kwargs):
        ...
    @staticmethod
    def setContextMenuPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setCursor(*args, **kwargs):
        ...
    @staticmethod
    def setDisabled(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setFixedHeight(*args, **kwargs):
        ...
    @staticmethod
    def setFixedSize(*args, **kwargs):
        ...
    @staticmethod
    def setFixedWidth(*args, **kwargs):
        ...
    @staticmethod
    def setFocus(*args, **kwargs):
        ...
    @staticmethod
    def setFocusPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setFocusProxy(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setForegroundRole(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setGraphicsEffect(*args, **kwargs):
        ...
    @staticmethod
    def setHidden(*args, **kwargs):
        ...
    @staticmethod
    def setInputMethodHints(*args, **kwargs):
        ...
    @staticmethod
    def setLayout(*args, **kwargs):
        ...
    @staticmethod
    def setLayoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def setLocale(*args, **kwargs):
        ...
    @staticmethod
    def setMask(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumHeight(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumSize(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumSize(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def setMouseTracking(*args, **kwargs):
        ...
    @staticmethod
    def setPalette(*args, **kwargs):
        ...
    @staticmethod
    def setParent(*args, **kwargs):
        ...
    @staticmethod
    def setScreen(*args, **kwargs):
        ...
    @staticmethod
    def setShortcutAutoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def setShortcutEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSizeIncrement(*args, **kwargs):
        ...
    @staticmethod
    def setSizePolicy(*args, **kwargs):
        ...
    @staticmethod
    def setStatusTip(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def setStyleSheet(*args, **kwargs):
        ...
    @staticmethod
    def setTabOrder(*args, **kwargs):
        ...
    @staticmethod
    def setTabletTracking(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setToolTipDuration(*args, **kwargs):
        ...
    @staticmethod
    def setUpdatesEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def setWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def setWindowFilePath(*args, **kwargs):
        ...
    @staticmethod
    def setWindowFlag(*args, **kwargs):
        ...
    @staticmethod
    def setWindowFlags(*args, **kwargs):
        ...
    @staticmethod
    def setWindowIcon(*args, **kwargs):
        ...
    @staticmethod
    def setWindowIconText(*args, **kwargs):
        ...
    @staticmethod
    def setWindowModality(*args, **kwargs):
        ...
    @staticmethod
    def setWindowModified(*args, **kwargs):
        ...
    @staticmethod
    def setWindowOpacity(*args, **kwargs):
        ...
    @staticmethod
    def setWindowRole(*args, **kwargs):
        ...
    @staticmethod
    def setWindowState(*args, **kwargs):
        ...
    @staticmethod
    def setWindowTitle(*args, **kwargs):
        ...
    @staticmethod
    def sharedPainter(*args, **kwargs):
        ...
    @staticmethod
    def show(*args, **kwargs):
        ...
    @staticmethod
    def showEvent(*args, **kwargs):
        ...
    @staticmethod
    def showFullScreen(*args, **kwargs):
        ...
    @staticmethod
    def showMaximized(*args, **kwargs):
        ...
    @staticmethod
    def showMinimized(*args, **kwargs):
        ...
    @staticmethod
    def showNormal(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def sizeIncrement(*args, **kwargs):
        ...
    @staticmethod
    def sizePolicy(*args, **kwargs):
        ...
    @staticmethod
    def stackUnder(*args, **kwargs):
        ...
    @staticmethod
    def statusTip(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def styleSheet(*args, **kwargs):
        ...
    @staticmethod
    def tabletEvent(*args, **kwargs):
        ...
    @staticmethod
    def testAttribute(*args, **kwargs):
        ...
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
    @staticmethod
    def toolTipDuration(*args, **kwargs):
        ...
    @staticmethod
    def underMouse(*args, **kwargs):
        ...
    @staticmethod
    def ungrabGesture(*args, **kwargs):
        ...
    @staticmethod
    def unsetCursor(*args, **kwargs):
        ...
    @staticmethod
    def unsetLayoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def unsetLocale(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
    @staticmethod
    def updateGeometry(*args, **kwargs):
        ...
    @staticmethod
    def updateMicroFocus(*args, **kwargs):
        ...
    @staticmethod
    def updatesEnabled(*args, **kwargs):
        ...
    @staticmethod
    def visibleRegion(*args, **kwargs):
        ...
    @staticmethod
    def whatsThis(*args, **kwargs):
        ...
    @staticmethod
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
    @staticmethod
    def winId(*args, **kwargs):
        ...
    @staticmethod
    def window(*args, **kwargs):
        ...
    @staticmethod
    def windowFilePath(*args, **kwargs):
        ...
    @staticmethod
    def windowFlags(*args, **kwargs):
        ...
    @staticmethod
    def windowHandle(*args, **kwargs):
        ...
    @staticmethod
    def windowIcon(*args, **kwargs):
        ...
    @staticmethod
    def windowIconChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def windowIconText(*args, **kwargs):
        ...
    @staticmethod
    def windowIconTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def windowModality(*args, **kwargs):
        ...
    @staticmethod
    def windowOpacity(*args, **kwargs):
        ...
    @staticmethod
    def windowRole(*args, **kwargs):
        ...
    @staticmethod
    def windowState(*args, **kwargs):
        ...
    @staticmethod
    def windowTitle(*args, **kwargs):
        ...
    @staticmethod
    def windowTitleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def windowType(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
class QWidgetAction(PyQt6.QtGui.QAction):
    @staticmethod
    def createWidget(*args, **kwargs):
        ...
    @staticmethod
    def createdWidgets(*args, **kwargs):
        ...
    @staticmethod
    def defaultWidget(*args, **kwargs):
        ...
    @staticmethod
    def deleteWidget(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def releaseWidget(*args, **kwargs):
        ...
    @staticmethod
    def requestWidget(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultWidget(*args, **kwargs):
        ...
class QWidgetItem(QLayoutItem):
    @staticmethod
    def controlTypes(*args, **kwargs):
        ...
    @staticmethod
    def expandingDirections(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def hasHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def heightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumHeightForWidth(*args, **kwargs):
        ...
    @staticmethod
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def widget(*args, **kwargs):
        ...
class QWizard(QDialog):
    class WizardButton(enum.Enum):
        BackButton: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.BackButton: 0>
        CancelButton: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.CancelButton: 4>
        CommitButton: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.CommitButton: 2>
        CustomButton1: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.CustomButton1: 6>
        CustomButton2: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.CustomButton2: 7>
        CustomButton3: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.CustomButton3: 8>
        FinishButton: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.FinishButton: 3>
        HelpButton: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.HelpButton: 5>
        NextButton: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.NextButton: 1>
        Stretch: typing.ClassVar[QWizard.WizardButton]  # value = <WizardButton.Stretch: 9>
    class WizardOption(enum.Flag):
        CancelButtonOnLeft: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.CancelButtonOnLeft: 1024>
        DisabledBackButtonOnLastPage: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.DisabledBackButtonOnLastPage: 64>
        ExtendedWatermarkPixmap: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.ExtendedWatermarkPixmap: 4>
        HaveCustomButton1: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.HaveCustomButton1: 8192>
        HaveCustomButton2: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.HaveCustomButton2: 16384>
        HaveCustomButton3: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.HaveCustomButton3: 32768>
        HaveFinishButtonOnEarlyPages: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.HaveFinishButtonOnEarlyPages: 256>
        HaveHelpButton: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.HaveHelpButton: 2048>
        HaveNextButtonOnLastPage: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.HaveNextButtonOnLastPage: 128>
        HelpButtonOnRight: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.HelpButtonOnRight: 4096>
        IgnoreSubTitles: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.IgnoreSubTitles: 2>
        IndependentPages: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.IndependentPages: 1>
        NoBackButtonOnLastPage: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.NoBackButtonOnLastPage: 32>
        NoBackButtonOnStartPage: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.NoBackButtonOnStartPage: 16>
        NoCancelButton: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.NoCancelButton: 512>
        NoCancelButtonOnLastPage: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.NoCancelButtonOnLastPage: 65536>
        NoDefaultButton: typing.ClassVar[QWizard.WizardOption]  # value = <WizardOption.NoDefaultButton: 8>
    class WizardPixmap(enum.Enum):
        BackgroundPixmap: typing.ClassVar[QWizard.WizardPixmap]  # value = <WizardPixmap.BackgroundPixmap: 3>
        BannerPixmap: typing.ClassVar[QWizard.WizardPixmap]  # value = <WizardPixmap.BannerPixmap: 2>
        LogoPixmap: typing.ClassVar[QWizard.WizardPixmap]  # value = <WizardPixmap.LogoPixmap: 1>
        WatermarkPixmap: typing.ClassVar[QWizard.WizardPixmap]  # value = <WizardPixmap.WatermarkPixmap: 0>
    class WizardStyle(enum.Enum):
        AeroStyle: typing.ClassVar[QWizard.WizardStyle]  # value = <WizardStyle.AeroStyle: 3>
        ClassicStyle: typing.ClassVar[QWizard.WizardStyle]  # value = <WizardStyle.ClassicStyle: 0>
        MacStyle: typing.ClassVar[QWizard.WizardStyle]  # value = <WizardStyle.MacStyle: 2>
        ModernStyle: typing.ClassVar[QWizard.WizardStyle]  # value = <WizardStyle.ModernStyle: 1>
    @staticmethod
    def addPage(*args, **kwargs):
        ...
    @staticmethod
    def back(*args, **kwargs):
        ...
    @staticmethod
    def button(*args, **kwargs):
        ...
    @staticmethod
    def buttonText(*args, **kwargs):
        ...
    @staticmethod
    def cleanupPage(*args, **kwargs):
        ...
    @staticmethod
    def currentId(*args, **kwargs):
        ...
    @staticmethod
    def currentIdChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentPage(*args, **kwargs):
        ...
    @staticmethod
    def customButtonClicked(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def field(*args, **kwargs):
        ...
    @staticmethod
    def hasVisitedPage(*args, **kwargs):
        ...
    @staticmethod
    def helpRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def initializePage(*args, **kwargs):
        ...
    @staticmethod
    def next(*args, **kwargs):
        ...
    @staticmethod
    def nextId(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def page(*args, **kwargs):
        ...
    @staticmethod
    def pageAdded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def pageIds(*args, **kwargs):
        ...
    @staticmethod
    def pageRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def removePage(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def restart(*args, **kwargs):
        ...
    @staticmethod
    def setButton(*args, **kwargs):
        ...
    @staticmethod
    def setButtonLayout(*args, **kwargs):
        ...
    @staticmethod
    def setButtonText(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentId(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultProperty(*args, **kwargs):
        ...
    @staticmethod
    def setField(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setPage(*args, **kwargs):
        ...
    @staticmethod
    def setPixmap(*args, **kwargs):
        ...
    @staticmethod
    def setSideWidget(*args, **kwargs):
        ...
    @staticmethod
    def setStartId(*args, **kwargs):
        ...
    @staticmethod
    def setSubTitleFormat(*args, **kwargs):
        ...
    @staticmethod
    def setTitleFormat(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def setWizardStyle(*args, **kwargs):
        ...
    @staticmethod
    def sideWidget(*args, **kwargs):
        ...
    @staticmethod
    def sizeHint(*args, **kwargs):
        ...
    @staticmethod
    def startId(*args, **kwargs):
        ...
    @staticmethod
    def subTitleFormat(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def titleFormat(*args, **kwargs):
        ...
    @staticmethod
    def validateCurrentPage(*args, **kwargs):
        ...
    @staticmethod
    def visitedIds(*args, **kwargs):
        ...
    @staticmethod
    def wizardStyle(*args, **kwargs):
        ...
class QWizardPage(QWidget):
    @staticmethod
    def buttonText(*args, **kwargs):
        ...
    @staticmethod
    def cleanupPage(*args, **kwargs):
        ...
    @staticmethod
    def completeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def field(*args, **kwargs):
        ...
    @staticmethod
    def initializePage(*args, **kwargs):
        ...
    @staticmethod
    def isCommitPage(*args, **kwargs):
        ...
    @staticmethod
    def isComplete(*args, **kwargs):
        ...
    @staticmethod
    def isFinalPage(*args, **kwargs):
        ...
    @staticmethod
    def nextId(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def registerField(*args, **kwargs):
        ...
    @staticmethod
    def setButtonText(*args, **kwargs):
        ...
    @staticmethod
    def setCommitPage(*args, **kwargs):
        ...
    @staticmethod
    def setField(*args, **kwargs):
        ...
    @staticmethod
    def setFinalPage(*args, **kwargs):
        ...
    @staticmethod
    def setPixmap(*args, **kwargs):
        ...
    @staticmethod
    def setSubTitle(*args, **kwargs):
        ...
    @staticmethod
    def setTitle(*args, **kwargs):
        ...
    @staticmethod
    def subTitle(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
    @staticmethod
    def validatePage(*args, **kwargs):
        ...
    @staticmethod
    def wizard(*args, **kwargs):
        ...
def qDrawBorderPixmap(*args, **kwargs):
    ...
def qDrawPlainRect(*args, **kwargs):
    ...
def qDrawPlainRoundedRect(*args, **kwargs):
    ...
def qDrawShadeLine(*args, **kwargs):
    ...
def qDrawShadePanel(*args, **kwargs):
    ...
def qDrawShadeRect(*args, **kwargs):
    ...
def qDrawWinButton(*args, **kwargs):
    ...
def qDrawWinPanel(*args, **kwargs):
    ...
QWIDGETSIZE_MAX: int = 16777215
