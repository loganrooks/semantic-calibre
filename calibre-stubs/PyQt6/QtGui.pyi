import PyQt6.QtCore
import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['QAbstractFileIconProvider', 'QAbstractTextDocumentLayout', 'QAction', 'QActionEvent', 'QActionGroup', 'QBackingStore', 'QBitmap', 'QBrush', 'QChildWindowEvent', 'QClipboard', 'QCloseEvent', 'QColor', 'QColorConstants', 'QColorSpace', 'QColorTransform', 'QConicalGradient', 'QContextMenuEvent', 'QCursor', 'QDesktopServices', 'QDoubleValidator', 'QDrag', 'QDragEnterEvent', 'QDragLeaveEvent', 'QDragMoveEvent', 'QDropEvent', 'QEnterEvent', 'QEventPoint', 'QExposeEvent', 'QFileOpenEvent', 'QFileSystemModel', 'QFocusEvent', 'QFont', 'QFontDatabase', 'QFontInfo', 'QFontMetrics', 'QFontMetricsF', 'QGlyphRun', 'QGradient', 'QGuiApplication', 'QHelpEvent', 'QHideEvent', 'QHoverEvent', 'QIcon', 'QIconDragEvent', 'QIconEngine', 'QImage', 'QImageIOHandler', 'QImageReader', 'QImageWriter', 'QInputDevice', 'QInputEvent', 'QInputMethod', 'QInputMethodEvent', 'QInputMethodQueryEvent', 'QIntValidator', 'QKeyEvent', 'QKeySequence', 'QLinearGradient', 'QMatrix2x2', 'QMatrix2x3', 'QMatrix2x4', 'QMatrix3x2', 'QMatrix3x3', 'QMatrix3x4', 'QMatrix4x2', 'QMatrix4x3', 'QMatrix4x4', 'QMouseEvent', 'QMoveEvent', 'QMovie', 'QNativeGestureEvent', 'QOffscreenSurface', 'QOpenGLContext', 'QOpenGLContextGroup', 'QPageLayout', 'QPageRanges', 'QPageSize', 'QPagedPaintDevice', 'QPaintDevice', 'QPaintDeviceWindow', 'QPaintEngine', 'QPaintEngineState', 'QPaintEvent', 'QPainter', 'QPainterPath', 'QPainterPathStroker', 'QPalette', 'QPdfWriter', 'QPen', 'QPicture', 'QPixelFormat', 'QPixmap', 'QPixmapCache', 'QPlatformSurfaceEvent', 'QPointerEvent', 'QPointingDevice', 'QPointingDeviceUniqueId', 'QPolygon', 'QPolygonF', 'QQuaternion', 'QRadialGradient', 'QRasterWindow', 'QRawFont', 'QRegion', 'QRegularExpressionValidator', 'QResizeEvent', 'QRgba64', 'QScreen', 'QScrollEvent', 'QScrollPrepareEvent', 'QSessionManager', 'QShortcut', 'QShortcutEvent', 'QShowEvent', 'QSinglePointEvent', 'QStandardItem', 'QStandardItemModel', 'QStaticText', 'QStatusTipEvent', 'QStyleHints', 'QSurface', 'QSurfaceFormat', 'QSyntaxHighlighter', 'QTabletEvent', 'QTextBlock', 'QTextBlockFormat', 'QTextBlockGroup', 'QTextBlockUserData', 'QTextCharFormat', 'QTextCursor', 'QTextDocument', 'QTextDocumentFragment', 'QTextDocumentWriter', 'QTextFormat', 'QTextFragment', 'QTextFrame', 'QTextFrameFormat', 'QTextImageFormat', 'QTextInlineObject', 'QTextItem', 'QTextLayout', 'QTextLength', 'QTextLine', 'QTextList', 'QTextListFormat', 'QTextObject', 'QTextObjectInterface', 'QTextOption', 'QTextTable', 'QTextTableCell', 'QTextTableCellFormat', 'QTextTableFormat', 'QTouchEvent', 'QTransform', 'QUndoCommand', 'QUndoGroup', 'QUndoStack', 'QValidator', 'QVector2D', 'QVector3D', 'QVector4D', 'QWhatsThisClickedEvent', 'QWheelEvent', 'QWindow', 'QWindowStateChangeEvent', 'qAlpha', 'qBlue', 'qFuzzyCompare', 'qGray', 'qGreen', 'qPixelFormatAlpha', 'qPixelFormatCmyk', 'qPixelFormatGrayscale', 'qPixelFormatHsl', 'qPixelFormatHsv', 'qPixelFormatRgba', 'qPixelFormatYuv', 'qPremultiply', 'qRed', 'qRgb', 'qRgba', 'qRgba64', 'qUnpremultiply', 'qt_set_sequence_auto_mnemonic']
class QAbstractFileIconProvider(PyQt6.sip.simplewrapper):
    class IconType(enum.Enum):
        Computer: typing.ClassVar[QAbstractFileIconProvider.IconType]  # value = <IconType.Computer: 0>
        Desktop: typing.ClassVar[QAbstractFileIconProvider.IconType]  # value = <IconType.Desktop: 1>
        Drive: typing.ClassVar[QAbstractFileIconProvider.IconType]  # value = <IconType.Drive: 4>
        File: typing.ClassVar[QAbstractFileIconProvider.IconType]  # value = <IconType.File: 6>
        Folder: typing.ClassVar[QAbstractFileIconProvider.IconType]  # value = <IconType.Folder: 5>
        Network: typing.ClassVar[QAbstractFileIconProvider.IconType]  # value = <IconType.Network: 3>
        Trashcan: typing.ClassVar[QAbstractFileIconProvider.IconType]  # value = <IconType.Trashcan: 2>
    class Option(enum.Flag):
        DontUseCustomDirectoryIcons: typing.ClassVar[QAbstractFileIconProvider.Option]  # value = <Option.DontUseCustomDirectoryIcons: 1>
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QAbstractTextDocumentLayout(PyQt6.QtCore.QObject):
    class PaintContext(PyQt6.sip.simplewrapper):
        pass
    class Selection(PyQt6.sip.simplewrapper):
        pass
    @staticmethod
    def anchorAt(*args, **kwargs):
        ...
    @staticmethod
    def blockBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def blockWithMarkerAt(*args, **kwargs):
        ...
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def documentChanged(*args, **kwargs):
        ...
    @staticmethod
    def documentSize(*args, **kwargs):
        ...
    @staticmethod
    def documentSizeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def drawInlineObject(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def formatAt(*args, **kwargs):
        ...
    @staticmethod
    def frameBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def handlerForObject(*args, **kwargs):
        ...
    @staticmethod
    def hitTest(*args, **kwargs):
        ...
    @staticmethod
    def imageAt(*args, **kwargs):
        ...
    @staticmethod
    def pageCount(*args, **kwargs):
        ...
    @staticmethod
    def pageCountChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def paintDevice(*args, **kwargs):
        ...
    @staticmethod
    def positionInlineObject(*args, **kwargs):
        ...
    @staticmethod
    def registerHandler(*args, **kwargs):
        ...
    @staticmethod
    def resizeInlineObject(*args, **kwargs):
        ...
    @staticmethod
    def setPaintDevice(*args, **kwargs):
        ...
    @staticmethod
    def unregisterHandler(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def updateBlock(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QAction(PyQt6.QtCore.QObject):
    class ActionEvent(enum.Enum):
        Hover: typing.ClassVar[QAction.ActionEvent]  # value = <ActionEvent.Hover: 1>
        Trigger: typing.ClassVar[QAction.ActionEvent]  # value = <ActionEvent.Trigger: 0>
    class MenuRole(enum.Enum):
        AboutQtRole: typing.ClassVar[QAction.MenuRole]  # value = <MenuRole.AboutQtRole: 3>
        AboutRole: typing.ClassVar[QAction.MenuRole]  # value = <MenuRole.AboutRole: 4>
        ApplicationSpecificRole: typing.ClassVar[QAction.MenuRole]  # value = <MenuRole.ApplicationSpecificRole: 2>
        NoRole: typing.ClassVar[QAction.MenuRole]  # value = <MenuRole.NoRole: 0>
        PreferencesRole: typing.ClassVar[QAction.MenuRole]  # value = <MenuRole.PreferencesRole: 5>
        QuitRole: typing.ClassVar[QAction.MenuRole]  # value = <MenuRole.QuitRole: 6>
        TextHeuristicRole: typing.ClassVar[QAction.MenuRole]  # value = <MenuRole.TextHeuristicRole: 1>
    class Priority(enum.Enum):
        HighPriority: typing.ClassVar[QAction.Priority]  # value = <Priority.HighPriority: 256>
        LowPriority: typing.ClassVar[QAction.Priority]  # value = <Priority.LowPriority: 0>
        NormalPriority: typing.ClassVar[QAction.Priority]  # value = <Priority.NormalPriority: 128>
    @staticmethod
    def actionGroup(*args, **kwargs):
        ...
    @staticmethod
    def activate(*args, **kwargs):
        ...
    @staticmethod
    def associatedObjects(*args, **kwargs):
        ...
    @staticmethod
    def autoRepeat(*args, **kwargs):
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
    def checkableChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def data(*args, **kwargs):
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
    def event(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def hover(*args, **kwargs):
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
    def iconText(*args, **kwargs):
        ...
    @staticmethod
    def isCheckable(*args, **kwargs):
        ...
    @staticmethod
    def isChecked(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isIconVisibleInMenu(*args, **kwargs):
        ...
    @staticmethod
    def isSeparator(*args, **kwargs):
        ...
    @staticmethod
    def isShortcutVisibleInContextMenu(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def menu(*args, **kwargs):
        ...
    @staticmethod
    def menuRole(*args, **kwargs):
        ...
    @staticmethod
    def priority(*args, **kwargs):
        ...
    @staticmethod
    def resetEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setActionGroup(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def setCheckable(*args, **kwargs):
        ...
    @staticmethod
    def setChecked(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setDisabled(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setIconText(*args, **kwargs):
        ...
    @staticmethod
    def setIconVisibleInMenu(*args, **kwargs):
        ...
    @staticmethod
    def setMenu(*args, **kwargs):
        ...
    @staticmethod
    def setMenuRole(*args, **kwargs):
        ...
    @staticmethod
    def setPriority(*args, **kwargs):
        ...
    @staticmethod
    def setSeparator(*args, **kwargs):
        ...
    @staticmethod
    def setShortcut(*args, **kwargs):
        ...
    @staticmethod
    def setShortcutContext(*args, **kwargs):
        ...
    @staticmethod
    def setShortcutVisibleInContextMenu(*args, **kwargs):
        ...
    @staticmethod
    def setShortcuts(*args, **kwargs):
        ...
    @staticmethod
    def setStatusTip(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def setWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def shortcut(*args, **kwargs):
        ...
    @staticmethod
    def shortcutContext(*args, **kwargs):
        ...
    @staticmethod
    def shortcuts(*args, **kwargs):
        ...
    @staticmethod
    def showStatusText(*args, **kwargs):
        ...
    @staticmethod
    def statusTip(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
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
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
    @staticmethod
    def trigger(*args, **kwargs):
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
    def whatsThis(*args, **kwargs):
        ...
class QActionEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def action(*args, **kwargs):
        ...
    @staticmethod
    def before(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QActionGroup(PyQt6.QtCore.QObject):
    class ExclusionPolicy(enum.Enum):
        Exclusive: typing.ClassVar[QActionGroup.ExclusionPolicy]  # value = <ExclusionPolicy.Exclusive: 1>
        ExclusiveOptional: typing.ClassVar[QActionGroup.ExclusionPolicy]  # value = <ExclusionPolicy.ExclusiveOptional: 2>
        None_: typing.ClassVar[QActionGroup.ExclusionPolicy]  # value = <ExclusionPolicy.None_: 0>
    @staticmethod
    def actions(*args, **kwargs):
        ...
    @staticmethod
    def addAction(*args, **kwargs):
        ...
    @staticmethod
    def checkedAction(*args, **kwargs):
        ...
    @staticmethod
    def exclusionPolicy(*args, **kwargs):
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
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isExclusive(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def removeAction(*args, **kwargs):
        ...
    @staticmethod
    def setDisabled(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setExclusionPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setExclusive(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
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
class QBackingStore(PyQt6.sip.simplewrapper):
    @staticmethod
    def beginPaint(*args, **kwargs):
        ...
    @staticmethod
    def endPaint(*args, **kwargs):
        ...
    @staticmethod
    def flush(*args, **kwargs):
        ...
    @staticmethod
    def hasStaticContents(*args, **kwargs):
        ...
    @staticmethod
    def paintDevice(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def scroll(*args, **kwargs):
        ...
    @staticmethod
    def setStaticContents(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def staticContents(*args, **kwargs):
        ...
    @staticmethod
    def window(*args, **kwargs):
        ...
class QBitmap(QPixmap):
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def fromData(*args, **kwargs):
        ...
    @staticmethod
    def fromImage(*args, **kwargs):
        ...
    @staticmethod
    def fromPixmap(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def transformed(*args, **kwargs):
        ...
class QBrush(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def color(*args, **kwargs):
        ...
    @staticmethod
    def gradient(*args, **kwargs):
        ...
    @staticmethod
    def isOpaque(*args, **kwargs):
        ...
    @staticmethod
    def setColor(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def setTexture(*args, **kwargs):
        ...
    @staticmethod
    def setTextureImage(*args, **kwargs):
        ...
    @staticmethod
    def setTransform(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def texture(*args, **kwargs):
        ...
    @staticmethod
    def textureImage(*args, **kwargs):
        ...
    @staticmethod
    def transform(*args, **kwargs):
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
class QChildWindowEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def child(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QClipboard(PyQt6.QtCore.QObject):
    class Mode(enum.Enum):
        Clipboard: typing.ClassVar[QClipboard.Mode]  # value = <Mode.Clipboard: 0>
        FindBuffer: typing.ClassVar[QClipboard.Mode]  # value = <Mode.FindBuffer: 2>
        Selection: typing.ClassVar[QClipboard.Mode]  # value = <Mode.Selection: 1>
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
    def dataChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def findBufferChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def image(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def ownsClipboard(*args, **kwargs):
        ...
    @staticmethod
    def ownsFindBuffer(*args, **kwargs):
        ...
    @staticmethod
    def ownsSelection(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
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
    def setImage(*args, **kwargs):
        ...
    @staticmethod
    def setMimeData(*args, **kwargs):
        ...
    @staticmethod
    def setPixmap(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def supportsFindBuffer(*args, **kwargs):
        ...
    @staticmethod
    def supportsSelection(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
class QCloseEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QColor(PyQt6.sip.simplewrapper):
    class NameFormat(enum.Enum):
        HexArgb: typing.ClassVar[QColor.NameFormat]  # value = <NameFormat.HexArgb: 1>
        HexRgb: typing.ClassVar[QColor.NameFormat]  # value = <NameFormat.HexRgb: 0>
    class Spec(enum.Enum):
        Cmyk: typing.ClassVar[QColor.Spec]  # value = <Spec.Cmyk: 3>
        ExtendedRgb: typing.ClassVar[QColor.Spec]  # value = <Spec.ExtendedRgb: 5>
        Hsl: typing.ClassVar[QColor.Spec]  # value = <Spec.Hsl: 4>
        Hsv: typing.ClassVar[QColor.Spec]  # value = <Spec.Hsv: 2>
        Invalid: typing.ClassVar[QColor.Spec]  # value = <Spec.Invalid: 0>
        Rgb: typing.ClassVar[QColor.Spec]  # value = <Spec.Rgb: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def alpha(*args, **kwargs):
        ...
    @staticmethod
    def alphaF(*args, **kwargs):
        ...
    @staticmethod
    def black(*args, **kwargs):
        ...
    @staticmethod
    def blackF(*args, **kwargs):
        ...
    @staticmethod
    def blue(*args, **kwargs):
        ...
    @staticmethod
    def blueF(*args, **kwargs):
        ...
    @staticmethod
    def colorNames(*args, **kwargs):
        ...
    @staticmethod
    def convertTo(*args, **kwargs):
        ...
    @staticmethod
    def cyan(*args, **kwargs):
        ...
    @staticmethod
    def cyanF(*args, **kwargs):
        ...
    @staticmethod
    def darker(*args, **kwargs):
        ...
    @staticmethod
    def fromCmyk(*args, **kwargs):
        ...
    @staticmethod
    def fromCmykF(*args, **kwargs):
        ...
    @staticmethod
    def fromHsl(*args, **kwargs):
        ...
    @staticmethod
    def fromHslF(*args, **kwargs):
        ...
    @staticmethod
    def fromHsv(*args, **kwargs):
        ...
    @staticmethod
    def fromHsvF(*args, **kwargs):
        ...
    @staticmethod
    def fromRgb(*args, **kwargs):
        ...
    @staticmethod
    def fromRgbF(*args, **kwargs):
        ...
    @staticmethod
    def fromRgba(*args, **kwargs):
        ...
    @staticmethod
    def fromRgba64(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def getCmyk(*args, **kwargs):
        ...
    @staticmethod
    def getCmykF(*args, **kwargs):
        ...
    @staticmethod
    def getHsl(*args, **kwargs):
        ...
    @staticmethod
    def getHslF(*args, **kwargs):
        ...
    @staticmethod
    def getHsv(*args, **kwargs):
        ...
    @staticmethod
    def getHsvF(*args, **kwargs):
        ...
    @staticmethod
    def getRgb(*args, **kwargs):
        ...
    @staticmethod
    def getRgbF(*args, **kwargs):
        ...
    @staticmethod
    def green(*args, **kwargs):
        ...
    @staticmethod
    def greenF(*args, **kwargs):
        ...
    @staticmethod
    def hslHue(*args, **kwargs):
        ...
    @staticmethod
    def hslHueF(*args, **kwargs):
        ...
    @staticmethod
    def hslSaturation(*args, **kwargs):
        ...
    @staticmethod
    def hslSaturationF(*args, **kwargs):
        ...
    @staticmethod
    def hsvHue(*args, **kwargs):
        ...
    @staticmethod
    def hsvHueF(*args, **kwargs):
        ...
    @staticmethod
    def hsvSaturation(*args, **kwargs):
        ...
    @staticmethod
    def hsvSaturationF(*args, **kwargs):
        ...
    @staticmethod
    def hue(*args, **kwargs):
        ...
    @staticmethod
    def hueF(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def isValidColor(*args, **kwargs):
        ...
    @staticmethod
    def isValidColorName(*args, **kwargs):
        ...
    @staticmethod
    def lighter(*args, **kwargs):
        ...
    @staticmethod
    def lightness(*args, **kwargs):
        ...
    @staticmethod
    def lightnessF(*args, **kwargs):
        ...
    @staticmethod
    def magenta(*args, **kwargs):
        ...
    @staticmethod
    def magentaF(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def red(*args, **kwargs):
        ...
    @staticmethod
    def redF(*args, **kwargs):
        ...
    @staticmethod
    def rgb(*args, **kwargs):
        ...
    @staticmethod
    def rgba(*args, **kwargs):
        ...
    @staticmethod
    def rgba64(*args, **kwargs):
        ...
    @staticmethod
    def saturation(*args, **kwargs):
        ...
    @staticmethod
    def saturationF(*args, **kwargs):
        ...
    @staticmethod
    def setAlpha(*args, **kwargs):
        ...
    @staticmethod
    def setAlphaF(*args, **kwargs):
        ...
    @staticmethod
    def setBlue(*args, **kwargs):
        ...
    @staticmethod
    def setBlueF(*args, **kwargs):
        ...
    @staticmethod
    def setCmyk(*args, **kwargs):
        ...
    @staticmethod
    def setCmykF(*args, **kwargs):
        ...
    @staticmethod
    def setGreen(*args, **kwargs):
        ...
    @staticmethod
    def setGreenF(*args, **kwargs):
        ...
    @staticmethod
    def setHsl(*args, **kwargs):
        ...
    @staticmethod
    def setHslF(*args, **kwargs):
        ...
    @staticmethod
    def setHsv(*args, **kwargs):
        ...
    @staticmethod
    def setHsvF(*args, **kwargs):
        ...
    @staticmethod
    def setNamedColor(*args, **kwargs):
        ...
    @staticmethod
    def setRed(*args, **kwargs):
        ...
    @staticmethod
    def setRedF(*args, **kwargs):
        ...
    @staticmethod
    def setRgb(*args, **kwargs):
        ...
    @staticmethod
    def setRgbF(*args, **kwargs):
        ...
    @staticmethod
    def setRgba(*args, **kwargs):
        ...
    @staticmethod
    def setRgba64(*args, **kwargs):
        ...
    @staticmethod
    def spec(*args, **kwargs):
        ...
    @staticmethod
    def toCmyk(*args, **kwargs):
        ...
    @staticmethod
    def toExtendedRgb(*args, **kwargs):
        ...
    @staticmethod
    def toHsl(*args, **kwargs):
        ...
    @staticmethod
    def toHsv(*args, **kwargs):
        ...
    @staticmethod
    def toRgb(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def valueF(*args, **kwargs):
        ...
    @staticmethod
    def yellow(*args, **kwargs):
        ...
    @staticmethod
    def yellowF(*args, **kwargs):
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
class QColorConstants(PyQt6.sip.simplewrapper):
    class Svg(PyQt6.sip.simplewrapper):
        aliceblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        antiquewhite: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        aqua: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        aquamarine: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        azure: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        beige: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        bisque: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        black: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        blanchedalmond: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        blue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        blueviolet: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        brown: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        burlywood: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        cadetblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        chartreuse: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        chocolate: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        coral: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        cornflowerblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        cornsilk: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        crimson: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        cyan: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkcyan: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkgoldenrod: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkgray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkgreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkgrey: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkkhaki: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkmagenta: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkolivegreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkorange: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkorchid: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkred: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darksalmon: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkseagreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkslateblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkslategray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkslategrey: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkturquoise: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        darkviolet: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        deeppink: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        deepskyblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        dimgray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        dimgrey: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        dodgerblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        firebrick: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        floralwhite: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        forestgreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        fuchsia: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        gainsboro: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        ghostwhite: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        gold: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        goldenrod: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        gray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        green: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        greenyellow: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        grey: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        honeydew: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        hotpink: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        indianred: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        indigo: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        ivory: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        khaki: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lavender: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lavenderblush: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lawngreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lemonchiffon: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightcoral: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightcyan: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightgoldenrodyellow: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightgray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightgreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightgrey: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightpink: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightsalmon: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightseagreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightskyblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightslategray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightslategrey: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightsteelblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lightyellow: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        lime: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        limegreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        linen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        magenta: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        maroon: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumaquamarine: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumorchid: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumpurple: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumseagreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumslateblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumspringgreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumturquoise: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mediumvioletred: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        midnightblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mintcream: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        mistyrose: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        moccasin: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        navajowhite: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        navy: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        oldlace: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        olive: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        olivedrab: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        orange: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        orangered: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        orchid: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        palegoldenrod: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        palegreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        paleturquoise: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        palevioletred: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        papayawhip: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        peachpuff: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        peru: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        pink: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        plum: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        powderblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        purple: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        red: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        rosybrown: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        royalblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        saddlebrown: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        salmon: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        sandybrown: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        seagreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        seashell: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        sienna: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        silver: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        skyblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        slateblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        slategray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        slategrey: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        snow: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        springgreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        steelblue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        tan: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        teal: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        thistle: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        tomato: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        turquoise: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        violet: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        wheat: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        white: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        whitesmoke: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        yellow: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
        yellowgreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Black: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Blue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Color0: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Color1: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Cyan: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    DarkBlue: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    DarkCyan: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    DarkGray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    DarkGreen: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    DarkMagenta: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    DarkRed: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    DarkYellow: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Gray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Green: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    LightGray: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Magenta: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Red: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Transparent: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    White: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
    Yellow: typing.ClassVar[QColor]  # value = <PyQt6.QtGui.QColor object>
class QColorSpace(PyQt6.sip.simplewrapper):
    class NamedColorSpace(enum.Enum):
        AdobeRgb: typing.ClassVar[QColorSpace.NamedColorSpace]  # value = <NamedColorSpace.AdobeRgb: 3>
        DisplayP3: typing.ClassVar[QColorSpace.NamedColorSpace]  # value = <NamedColorSpace.DisplayP3: 4>
        ProPhotoRgb: typing.ClassVar[QColorSpace.NamedColorSpace]  # value = <NamedColorSpace.ProPhotoRgb: 5>
        SRgb: typing.ClassVar[QColorSpace.NamedColorSpace]  # value = <NamedColorSpace.SRgb: 1>
        SRgbLinear: typing.ClassVar[QColorSpace.NamedColorSpace]  # value = <NamedColorSpace.SRgbLinear: 2>
    class Primaries(enum.Enum):
        AdobeRgb: typing.ClassVar[QColorSpace.Primaries]  # value = <Primaries.AdobeRgb: 2>
        Custom: typing.ClassVar[QColorSpace.Primaries]  # value = <Primaries.Custom: 0>
        DciP3D65: typing.ClassVar[QColorSpace.Primaries]  # value = <Primaries.DciP3D65: 3>
        ProPhotoRgb: typing.ClassVar[QColorSpace.Primaries]  # value = <Primaries.ProPhotoRgb: 4>
        SRgb: typing.ClassVar[QColorSpace.Primaries]  # value = <Primaries.SRgb: 1>
    class TransferFunction(enum.Enum):
        Custom: typing.ClassVar[QColorSpace.TransferFunction]  # value = <TransferFunction.Custom: 0>
        Gamma: typing.ClassVar[QColorSpace.TransferFunction]  # value = <TransferFunction.Gamma: 2>
        Linear: typing.ClassVar[QColorSpace.TransferFunction]  # value = <TransferFunction.Linear: 1>
        ProPhotoRgb: typing.ClassVar[QColorSpace.TransferFunction]  # value = <TransferFunction.ProPhotoRgb: 4>
        SRgb: typing.ClassVar[QColorSpace.TransferFunction]  # value = <TransferFunction.SRgb: 3>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def description(*args, **kwargs):
        ...
    @staticmethod
    def fromIccProfile(*args, **kwargs):
        ...
    @staticmethod
    def gamma(*args, **kwargs):
        ...
    @staticmethod
    def iccProfile(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def primaries(*args, **kwargs):
        ...
    @staticmethod
    def setDescription(*args, **kwargs):
        ...
    @staticmethod
    def setPrimaries(*args, **kwargs):
        ...
    @staticmethod
    def setTransferFunction(*args, **kwargs):
        ...
    @staticmethod
    def setTransferFunctions(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def transferFunction(*args, **kwargs):
        ...
    @staticmethod
    def transformationToColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def withTransferFunction(*args, **kwargs):
        ...
    @staticmethod
    def withTransferFunctions(*args, **kwargs):
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
class QColorTransform(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def map(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
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
class QConicalGradient(QGradient):
    @staticmethod
    def angle(*args, **kwargs):
        ...
    @staticmethod
    def center(*args, **kwargs):
        ...
    @staticmethod
    def setAngle(*args, **kwargs):
        ...
    @staticmethod
    def setCenter(*args, **kwargs):
        ...
class QContextMenuEvent(QInputEvent):
    class Reason(enum.Enum):
        Keyboard: typing.ClassVar[QContextMenuEvent.Reason]  # value = <Reason.Keyboard: 1>
        Mouse: typing.ClassVar[QContextMenuEvent.Reason]  # value = <Reason.Mouse: 0>
        Other: typing.ClassVar[QContextMenuEvent.Reason]  # value = <Reason.Other: 2>
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def globalPos(*args, **kwargs):
        ...
    @staticmethod
    def globalX(*args, **kwargs):
        ...
    @staticmethod
    def globalY(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def reason(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
class QCursor(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def bitmap(*args, **kwargs):
        ...
    @staticmethod
    def hotSpot(*args, **kwargs):
        ...
    @staticmethod
    def mask(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def setPos(*args, **kwargs):
        ...
    @staticmethod
    def setShape(*args, **kwargs):
        ...
    @staticmethod
    def shape(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
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
class QDesktopServices(PyQt6.sip.simplewrapper):
    @staticmethod
    def openUrl(*args, **kwargs):
        ...
    @staticmethod
    def setUrlHandler(*args, **kwargs):
        ...
    @staticmethod
    def unsetUrlHandler(*args, **kwargs):
        ...
class QDoubleValidator(QValidator):
    class Notation(enum.Enum):
        ScientificNotation: typing.ClassVar[QDoubleValidator.Notation]  # value = <Notation.ScientificNotation: 1>
        StandardNotation: typing.ClassVar[QDoubleValidator.Notation]  # value = <Notation.StandardNotation: 0>
    @staticmethod
    def bottom(*args, **kwargs):
        ...
    @staticmethod
    def decimals(*args, **kwargs):
        ...
    @staticmethod
    def fixup(*args, **kwargs):
        ...
    @staticmethod
    def notation(*args, **kwargs):
        ...
    @staticmethod
    def setBottom(*args, **kwargs):
        ...
    @staticmethod
    def setDecimals(*args, **kwargs):
        ...
    @staticmethod
    def setNotation(*args, **kwargs):
        ...
    @staticmethod
    def setRange(*args, **kwargs):
        ...
    @staticmethod
    def setTop(*args, **kwargs):
        ...
    @staticmethod
    def top(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
class QDrag(PyQt6.QtCore.QObject):
    @staticmethod
    def actionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def cancel(*args, **kwargs):
        ...
    @staticmethod
    def defaultAction(*args, **kwargs):
        ...
    @staticmethod
    def dragCursor(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def hotSpot(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def setDragCursor(*args, **kwargs):
        ...
    @staticmethod
    def setHotSpot(*args, **kwargs):
        ...
    @staticmethod
    def setMimeData(*args, **kwargs):
        ...
    @staticmethod
    def setPixmap(*args, **kwargs):
        ...
    @staticmethod
    def source(*args, **kwargs):
        ...
    @staticmethod
    def supportedActions(*args, **kwargs):
        ...
    @staticmethod
    def target(*args, **kwargs):
        ...
    @staticmethod
    def targetChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QDragEnterEvent(QDragMoveEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QDragLeaveEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QDragMoveEvent(QDropEvent):
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def answerRect(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def ignore(*args, **kwargs):
        ...
class QDropEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def acceptProposedAction(*args, **kwargs):
        ...
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
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
    def position(*args, **kwargs):
        ...
    @staticmethod
    def possibleActions(*args, **kwargs):
        ...
    @staticmethod
    def proposedAction(*args, **kwargs):
        ...
    @staticmethod
    def setDropAction(*args, **kwargs):
        ...
    @staticmethod
    def source(*args, **kwargs):
        ...
class QEnterEvent(QSinglePointEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QEventPoint(PyQt6.sip.simplewrapper):
    class State(enum.Flag):
        Pressed: typing.ClassVar[QEventPoint.State]  # value = <State.Pressed: 1>
        Released: typing.ClassVar[QEventPoint.State]  # value = <State.Released: 8>
        Stationary: typing.ClassVar[QEventPoint.State]  # value = <State.Stationary: 4>
        Updated: typing.ClassVar[QEventPoint.State]  # value = <State.Updated: 2>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def ellipseDiameters(*args, **kwargs):
        ...
    @staticmethod
    def globalGrabPosition(*args, **kwargs):
        ...
    @staticmethod
    def globalLastPosition(*args, **kwargs):
        ...
    @staticmethod
    def globalPosition(*args, **kwargs):
        ...
    @staticmethod
    def globalPressPosition(*args, **kwargs):
        ...
    @staticmethod
    def grabPosition(*args, **kwargs):
        ...
    @staticmethod
    def id(*args, **kwargs):
        ...
    @staticmethod
    def isAccepted(*args, **kwargs):
        ...
    @staticmethod
    def lastPosition(*args, **kwargs):
        ...
    @staticmethod
    def lastTimestamp(*args, **kwargs):
        ...
    @staticmethod
    def normalizedPosition(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def pressPosition(*args, **kwargs):
        ...
    @staticmethod
    def pressTimestamp(*args, **kwargs):
        ...
    @staticmethod
    def pressure(*args, **kwargs):
        ...
    @staticmethod
    def rotation(*args, **kwargs):
        ...
    @staticmethod
    def sceneGrabPosition(*args, **kwargs):
        ...
    @staticmethod
    def sceneLastPosition(*args, **kwargs):
        ...
    @staticmethod
    def scenePosition(*args, **kwargs):
        ...
    @staticmethod
    def scenePressPosition(*args, **kwargs):
        ...
    @staticmethod
    def setAccepted(*args, **kwargs):
        ...
    @staticmethod
    def state(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def timeHeld(*args, **kwargs):
        ...
    @staticmethod
    def timestamp(*args, **kwargs):
        ...
    @staticmethod
    def uniqueId(*args, **kwargs):
        ...
    @staticmethod
    def velocity(*args, **kwargs):
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
class QExposeEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QFileOpenEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def file(*args, **kwargs):
        ...
    @staticmethod
    def openFile(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
        ...
class QFileSystemModel(PyQt6.QtCore.QAbstractItemModel):
    class Option(enum.Flag):
        DontResolveSymlinks: typing.ClassVar[QFileSystemModel.Option]  # value = <Option.DontResolveSymlinks: 2>
        DontUseCustomDirectoryIcons: typing.ClassVar[QFileSystemModel.Option]  # value = <Option.DontUseCustomDirectoryIcons: 4>
        DontWatchForChanges: typing.ClassVar[QFileSystemModel.Option]  # value = <Option.DontWatchForChanges: 1>
    class Roles(enum.IntEnum):
        FileIconRole: typing.ClassVar[QFileSystemModel.Roles]  # value = <Roles.FileIconRole: 1>
        FileNameRole: typing.ClassVar[QFileSystemModel.Roles]  # value = <Roles.FileNameRole: 258>
        FilePathRole: typing.ClassVar[QFileSystemModel.Roles]  # value = <Roles.FilePathRole: 257>
        FilePermissions: typing.ClassVar[QFileSystemModel.Roles]  # value = <Roles.FilePermissions: 259>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    @staticmethod
    def canFetchMore(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def directoryLoaded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def fetchMore(*args, **kwargs):
        ...
    @staticmethod
    def fileIcon(*args, **kwargs):
        ...
    @staticmethod
    def fileInfo(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def filePath(*args, **kwargs):
        ...
    @staticmethod
    def fileRenamed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def hasChildren(*args, **kwargs):
        ...
    @staticmethod
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def iconProvider(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def isDir(*args, **kwargs):
        ...
    @staticmethod
    def isReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def lastModified(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def mkdir(*args, **kwargs):
        ...
    @staticmethod
    def myComputer(*args, **kwargs):
        ...
    @staticmethod
    def nameFilterDisables(*args, **kwargs):
        ...
    @staticmethod
    def nameFilters(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def permissions(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def resolveSymlinks(*args, **kwargs):
        ...
    @staticmethod
    def rmdir(*args, **kwargs):
        ...
    @staticmethod
    def roleNames(*args, **kwargs):
        ...
    @staticmethod
    def rootDirectory(*args, **kwargs):
        ...
    @staticmethod
    def rootPath(*args, **kwargs):
        ...
    @staticmethod
    def rootPathChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setFilter(*args, **kwargs):
        ...
    @staticmethod
    def setIconProvider(*args, **kwargs):
        ...
    @staticmethod
    def setNameFilterDisables(*args, **kwargs):
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
    def setReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def setResolveSymlinks(*args, **kwargs):
        ...
    @staticmethod
    def setRootPath(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QFocusEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def gotFocus(*args, **kwargs):
        ...
    @staticmethod
    def lostFocus(*args, **kwargs):
        ...
    @staticmethod
    def reason(*args, **kwargs):
        ...
class QFont(PyQt6.sip.simplewrapper):
    class Capitalization(enum.Enum):
        AllLowercase: typing.ClassVar[QFont.Capitalization]  # value = <Capitalization.AllLowercase: 2>
        AllUppercase: typing.ClassVar[QFont.Capitalization]  # value = <Capitalization.AllUppercase: 1>
        Capitalize: typing.ClassVar[QFont.Capitalization]  # value = <Capitalization.Capitalize: 4>
        MixedCase: typing.ClassVar[QFont.Capitalization]  # value = <Capitalization.MixedCase: 0>
        SmallCaps: typing.ClassVar[QFont.Capitalization]  # value = <Capitalization.SmallCaps: 3>
    class HintingPreference(enum.Enum):
        PreferDefaultHinting: typing.ClassVar[QFont.HintingPreference]  # value = <HintingPreference.PreferDefaultHinting: 0>
        PreferFullHinting: typing.ClassVar[QFont.HintingPreference]  # value = <HintingPreference.PreferFullHinting: 3>
        PreferNoHinting: typing.ClassVar[QFont.HintingPreference]  # value = <HintingPreference.PreferNoHinting: 1>
        PreferVerticalHinting: typing.ClassVar[QFont.HintingPreference]  # value = <HintingPreference.PreferVerticalHinting: 2>
    class SpacingType(enum.Enum):
        AbsoluteSpacing: typing.ClassVar[QFont.SpacingType]  # value = <SpacingType.AbsoluteSpacing: 1>
        PercentageSpacing: typing.ClassVar[QFont.SpacingType]  # value = <SpacingType.PercentageSpacing: 0>
    class Stretch(enum.IntEnum):
        AnyStretch: typing.ClassVar[QFont.Stretch]  # value = <Stretch.AnyStretch: 0>
        Condensed: typing.ClassVar[QFont.Stretch]  # value = <Stretch.Condensed: 75>
        Expanded: typing.ClassVar[QFont.Stretch]  # value = <Stretch.Expanded: 125>
        ExtraCondensed: typing.ClassVar[QFont.Stretch]  # value = <Stretch.ExtraCondensed: 62>
        ExtraExpanded: typing.ClassVar[QFont.Stretch]  # value = <Stretch.ExtraExpanded: 150>
        SemiCondensed: typing.ClassVar[QFont.Stretch]  # value = <Stretch.SemiCondensed: 87>
        SemiExpanded: typing.ClassVar[QFont.Stretch]  # value = <Stretch.SemiExpanded: 112>
        UltraCondensed: typing.ClassVar[QFont.Stretch]  # value = <Stretch.UltraCondensed: 50>
        UltraExpanded: typing.ClassVar[QFont.Stretch]  # value = <Stretch.UltraExpanded: 200>
        Unstretched: typing.ClassVar[QFont.Stretch]  # value = <Stretch.Unstretched: 100>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class Style(enum.Enum):
        StyleItalic: typing.ClassVar[QFont.Style]  # value = <Style.StyleItalic: 1>
        StyleNormal: typing.ClassVar[QFont.Style]  # value = <Style.StyleNormal: 0>
        StyleOblique: typing.ClassVar[QFont.Style]  # value = <Style.StyleOblique: 2>
    class StyleHint(enum.Enum):
        AnyStyle: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.AnyStyle: 5>
        Courier: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.Courier: 2>
        Cursive: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.Cursive: 6>
        Fantasy: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.Fantasy: 8>
        Helvetica: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.Helvetica: 0>
        Monospace: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.Monospace: 7>
        OldEnglish: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.OldEnglish: 3>
        System: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.System: 4>
        Times: typing.ClassVar[QFont.StyleHint]  # value = <StyleHint.Times: 1>
    class StyleStrategy(enum.Flag):
        ForceOutline: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.ForceOutline: 16>
        NoAntialias: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.NoAntialias: 256>
        NoFontMerging: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.NoFontMerging: 32768>
        NoSubpixelAntialias: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.NoSubpixelAntialias: 2048>
        PreferAntialias: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferAntialias: 128>
        PreferBitmap: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferBitmap: 2>
        PreferDefault: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferDefault: 1>
        PreferDevice: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferDevice: 4>
        PreferMatch: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferMatch: 32>
        PreferNoShaping: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferNoShaping: 4096>
        PreferOutline: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferOutline: 8>
        PreferQuality: typing.ClassVar[QFont.StyleStrategy]  # value = <StyleStrategy.PreferQuality: 64>
    class Tag(PyQt6.sip.simplewrapper):
        @staticmethod
        def fromString(*args, **kwargs):
            ...
        @staticmethod
        def fromValue(*args, **kwargs):
            ...
        @staticmethod
        def isValid(*args, **kwargs):
            ...
        @staticmethod
        def toString(*args, **kwargs):
            ...
        @staticmethod
        def value(*args, **kwargs):
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
    class Weight(enum.IntEnum):
        Black: typing.ClassVar[QFont.Weight]  # value = <Weight.Black: 900>
        Bold: typing.ClassVar[QFont.Weight]  # value = <Weight.Bold: 700>
        DemiBold: typing.ClassVar[QFont.Weight]  # value = <Weight.DemiBold: 600>
        ExtraBold: typing.ClassVar[QFont.Weight]  # value = <Weight.ExtraBold: 800>
        ExtraLight: typing.ClassVar[QFont.Weight]  # value = <Weight.ExtraLight: 200>
        Light: typing.ClassVar[QFont.Weight]  # value = <Weight.Light: 300>
        Medium: typing.ClassVar[QFont.Weight]  # value = <Weight.Medium: 500>
        Normal: typing.ClassVar[QFont.Weight]  # value = <Weight.Normal: 400>
        Thin: typing.ClassVar[QFont.Weight]  # value = <Weight.Thin: 100>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    @staticmethod
    def bold(*args, **kwargs):
        ...
    @staticmethod
    def cacheStatistics(*args, **kwargs):
        ...
    @staticmethod
    def capitalization(*args, **kwargs):
        ...
    @staticmethod
    def cleanup(*args, **kwargs):
        ...
    @staticmethod
    def clearFeatures(*args, **kwargs):
        ...
    @staticmethod
    def clearVariableAxes(*args, **kwargs):
        ...
    @staticmethod
    def defaultFamily(*args, **kwargs):
        ...
    @staticmethod
    def exactMatch(*args, **kwargs):
        ...
    @staticmethod
    def families(*args, **kwargs):
        ...
    @staticmethod
    def family(*args, **kwargs):
        ...
    @staticmethod
    def featureTags(*args, **kwargs):
        ...
    @staticmethod
    def featureValue(*args, **kwargs):
        ...
    @staticmethod
    def fixedPitch(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def hintingPreference(*args, **kwargs):
        ...
    @staticmethod
    def initialize(*args, **kwargs):
        ...
    @staticmethod
    def insertSubstitution(*args, **kwargs):
        ...
    @staticmethod
    def insertSubstitutions(*args, **kwargs):
        ...
    @staticmethod
    def isCopyOf(*args, **kwargs):
        ...
    @staticmethod
    def isFeatureSet(*args, **kwargs):
        ...
    @staticmethod
    def isVariableAxisSet(*args, **kwargs):
        ...
    @staticmethod
    def italic(*args, **kwargs):
        ...
    @staticmethod
    def kerning(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def letterSpacing(*args, **kwargs):
        ...
    @staticmethod
    def letterSpacingType(*args, **kwargs):
        ...
    @staticmethod
    def overline(*args, **kwargs):
        ...
    @staticmethod
    def pixelSize(*args, **kwargs):
        ...
    @staticmethod
    def pointSize(*args, **kwargs):
        ...
    @staticmethod
    def pointSizeF(*args, **kwargs):
        ...
    @staticmethod
    def removeSubstitutions(*args, **kwargs):
        ...
    @staticmethod
    def resolve(*args, **kwargs):
        ...
    @staticmethod
    def setBold(*args, **kwargs):
        ...
    @staticmethod
    def setCapitalization(*args, **kwargs):
        ...
    @staticmethod
    def setFamilies(*args, **kwargs):
        ...
    @staticmethod
    def setFamily(*args, **kwargs):
        ...
    @staticmethod
    def setFeature(*args, **kwargs):
        ...
    @staticmethod
    def setFixedPitch(*args, **kwargs):
        ...
    @staticmethod
    def setHintingPreference(*args, **kwargs):
        ...
    @staticmethod
    def setItalic(*args, **kwargs):
        ...
    @staticmethod
    def setKerning(*args, **kwargs):
        ...
    @staticmethod
    def setLetterSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setOverline(*args, **kwargs):
        ...
    @staticmethod
    def setPixelSize(*args, **kwargs):
        ...
    @staticmethod
    def setPointSize(*args, **kwargs):
        ...
    @staticmethod
    def setPointSizeF(*args, **kwargs):
        ...
    @staticmethod
    def setStretch(*args, **kwargs):
        ...
    @staticmethod
    def setStrikeOut(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def setStyleHint(*args, **kwargs):
        ...
    @staticmethod
    def setStyleName(*args, **kwargs):
        ...
    @staticmethod
    def setStyleStrategy(*args, **kwargs):
        ...
    @staticmethod
    def setUnderline(*args, **kwargs):
        ...
    @staticmethod
    def setVariableAxis(*args, **kwargs):
        ...
    @staticmethod
    def setWeight(*args, **kwargs):
        ...
    @staticmethod
    def setWordSpacing(*args, **kwargs):
        ...
    @staticmethod
    def stretch(*args, **kwargs):
        ...
    @staticmethod
    def strikeOut(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def styleHint(*args, **kwargs):
        ...
    @staticmethod
    def styleName(*args, **kwargs):
        ...
    @staticmethod
    def styleStrategy(*args, **kwargs):
        ...
    @staticmethod
    def substitute(*args, **kwargs):
        ...
    @staticmethod
    def substitutes(*args, **kwargs):
        ...
    @staticmethod
    def substitutions(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    @staticmethod
    def underline(*args, **kwargs):
        ...
    @staticmethod
    def unsetFeature(*args, **kwargs):
        ...
    @staticmethod
    def unsetVariableAxis(*args, **kwargs):
        ...
    @staticmethod
    def variableAxisTags(*args, **kwargs):
        ...
    @staticmethod
    def variableAxisValue(*args, **kwargs):
        ...
    @staticmethod
    def weight(*args, **kwargs):
        ...
    @staticmethod
    def wordSpacing(*args, **kwargs):
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
class QFontDatabase(PyQt6.sip.simplewrapper):
    class SystemFont(enum.Enum):
        FixedFont: typing.ClassVar[QFontDatabase.SystemFont]  # value = <SystemFont.FixedFont: 1>
        GeneralFont: typing.ClassVar[QFontDatabase.SystemFont]  # value = <SystemFont.GeneralFont: 0>
        SmallestReadableFont: typing.ClassVar[QFontDatabase.SystemFont]  # value = <SystemFont.SmallestReadableFont: 3>
        TitleFont: typing.ClassVar[QFontDatabase.SystemFont]  # value = <SystemFont.TitleFont: 2>
    class WritingSystem(enum.Enum):
        Any: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Any: 0>
        Arabic: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Arabic: 6>
        Armenian: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Armenian: 4>
        Bengali: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Bengali: 10>
        Cyrillic: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Cyrillic: 3>
        Devanagari: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Devanagari: 9>
        Georgian: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Georgian: 23>
        Greek: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Greek: 2>
        Gujarati: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Gujarati: 12>
        Gurmukhi: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Gurmukhi: 11>
        Hebrew: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Hebrew: 5>
        Japanese: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Japanese: 27>
        Kannada: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Kannada: 16>
        Khmer: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Khmer: 24>
        Korean: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Korean: 28>
        Lao: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Lao: 20>
        Latin: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Latin: 1>
        Malayalam: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Malayalam: 17>
        Myanmar: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Myanmar: 22>
        Nko: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Nko: 33>
        Ogham: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Ogham: 31>
        Oriya: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Oriya: 13>
        Other: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Other: 30>
        Runic: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Runic: 32>
        SimplifiedChinese: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.SimplifiedChinese: 25>
        Sinhala: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Sinhala: 18>
        Syriac: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Syriac: 7>
        Tamil: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Tamil: 14>
        Telugu: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Telugu: 15>
        Thaana: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Thaana: 8>
        Thai: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Thai: 19>
        Tibetan: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Tibetan: 21>
        TraditionalChinese: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.TraditionalChinese: 26>
        Vietnamese: typing.ClassVar[QFontDatabase.WritingSystem]  # value = <WritingSystem.Vietnamese: 29>
    @staticmethod
    def addApplicationFont(*args, **kwargs):
        ...
    @staticmethod
    def addApplicationFontFromData(*args, **kwargs):
        ...
    @staticmethod
    def applicationFontFamilies(*args, **kwargs):
        ...
    @staticmethod
    def bold(*args, **kwargs):
        ...
    @staticmethod
    def families(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def isBitmapScalable(*args, **kwargs):
        ...
    @staticmethod
    def isFixedPitch(*args, **kwargs):
        ...
    @staticmethod
    def isPrivateFamily(*args, **kwargs):
        ...
    @staticmethod
    def isScalable(*args, **kwargs):
        ...
    @staticmethod
    def isSmoothlyScalable(*args, **kwargs):
        ...
    @staticmethod
    def italic(*args, **kwargs):
        ...
    @staticmethod
    def pointSizes(*args, **kwargs):
        ...
    @staticmethod
    def removeAllApplicationFonts(*args, **kwargs):
        ...
    @staticmethod
    def removeApplicationFont(*args, **kwargs):
        ...
    @staticmethod
    def smoothSizes(*args, **kwargs):
        ...
    @staticmethod
    def standardSizes(*args, **kwargs):
        ...
    @staticmethod
    def styleString(*args, **kwargs):
        ...
    @staticmethod
    def styles(*args, **kwargs):
        ...
    @staticmethod
    def systemFont(*args, **kwargs):
        ...
    @staticmethod
    def weight(*args, **kwargs):
        ...
    @staticmethod
    def writingSystemName(*args, **kwargs):
        ...
    @staticmethod
    def writingSystemSample(*args, **kwargs):
        ...
    @staticmethod
    def writingSystems(*args, **kwargs):
        ...
class QFontInfo(PyQt6.sip.simplewrapper):
    @staticmethod
    def bold(*args, **kwargs):
        ...
    @staticmethod
    def exactMatch(*args, **kwargs):
        ...
    @staticmethod
    def family(*args, **kwargs):
        ...
    @staticmethod
    def fixedPitch(*args, **kwargs):
        ...
    @staticmethod
    def italic(*args, **kwargs):
        ...
    @staticmethod
    def pixelSize(*args, **kwargs):
        ...
    @staticmethod
    def pointSize(*args, **kwargs):
        ...
    @staticmethod
    def pointSizeF(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def styleHint(*args, **kwargs):
        ...
    @staticmethod
    def styleName(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def weight(*args, **kwargs):
        ...
class QFontMetrics(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def ascent(*args, **kwargs):
        ...
    @staticmethod
    def averageCharWidth(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def boundingRectChar(*args, **kwargs):
        ...
    @staticmethod
    def capHeight(*args, **kwargs):
        ...
    @staticmethod
    def descent(*args, **kwargs):
        ...
    @staticmethod
    def elidedText(*args, **kwargs):
        ...
    @staticmethod
    def fontDpi(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def horizontalAdvance(*args, **kwargs):
        ...
    @staticmethod
    def inFont(*args, **kwargs):
        ...
    @staticmethod
    def inFontUcs4(*args, **kwargs):
        ...
    @staticmethod
    def leading(*args, **kwargs):
        ...
    @staticmethod
    def leftBearing(*args, **kwargs):
        ...
    @staticmethod
    def lineSpacing(*args, **kwargs):
        ...
    @staticmethod
    def lineWidth(*args, **kwargs):
        ...
    @staticmethod
    def maxWidth(*args, **kwargs):
        ...
    @staticmethod
    def minLeftBearing(*args, **kwargs):
        ...
    @staticmethod
    def minRightBearing(*args, **kwargs):
        ...
    @staticmethod
    def overlinePos(*args, **kwargs):
        ...
    @staticmethod
    def rightBearing(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def strikeOutPos(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def tightBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def underlinePos(*args, **kwargs):
        ...
    @staticmethod
    def xHeight(*args, **kwargs):
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
class QFontMetricsF(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def ascent(*args, **kwargs):
        ...
    @staticmethod
    def averageCharWidth(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def boundingRectChar(*args, **kwargs):
        ...
    @staticmethod
    def capHeight(*args, **kwargs):
        ...
    @staticmethod
    def descent(*args, **kwargs):
        ...
    @staticmethod
    def elidedText(*args, **kwargs):
        ...
    @staticmethod
    def fontDpi(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def horizontalAdvance(*args, **kwargs):
        ...
    @staticmethod
    def inFont(*args, **kwargs):
        ...
    @staticmethod
    def inFontUcs4(*args, **kwargs):
        ...
    @staticmethod
    def leading(*args, **kwargs):
        ...
    @staticmethod
    def leftBearing(*args, **kwargs):
        ...
    @staticmethod
    def lineSpacing(*args, **kwargs):
        ...
    @staticmethod
    def lineWidth(*args, **kwargs):
        ...
    @staticmethod
    def maxWidth(*args, **kwargs):
        ...
    @staticmethod
    def minLeftBearing(*args, **kwargs):
        ...
    @staticmethod
    def minRightBearing(*args, **kwargs):
        ...
    @staticmethod
    def overlinePos(*args, **kwargs):
        ...
    @staticmethod
    def rightBearing(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def strikeOutPos(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def tightBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def underlinePos(*args, **kwargs):
        ...
    @staticmethod
    def xHeight(*args, **kwargs):
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
class QGlyphRun(PyQt6.sip.simplewrapper):
    class GlyphRunFlag(enum.Flag):
        Overline: typing.ClassVar[QGlyphRun.GlyphRunFlag]  # value = <GlyphRunFlag.Overline: 1>
        RightToLeft: typing.ClassVar[QGlyphRun.GlyphRunFlag]  # value = <GlyphRunFlag.RightToLeft: 8>
        SplitLigature: typing.ClassVar[QGlyphRun.GlyphRunFlag]  # value = <GlyphRunFlag.SplitLigature: 16>
        StrikeOut: typing.ClassVar[QGlyphRun.GlyphRunFlag]  # value = <GlyphRunFlag.StrikeOut: 4>
        Underline: typing.ClassVar[QGlyphRun.GlyphRunFlag]  # value = <GlyphRunFlag.Underline: 2>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def glyphIndexes(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isRightToLeft(*args, **kwargs):
        ...
    @staticmethod
    def overline(*args, **kwargs):
        ...
    @staticmethod
    def positions(*args, **kwargs):
        ...
    @staticmethod
    def rawFont(*args, **kwargs):
        ...
    @staticmethod
    def setBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def setFlag(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setGlyphIndexes(*args, **kwargs):
        ...
    @staticmethod
    def setOverline(*args, **kwargs):
        ...
    @staticmethod
    def setPositions(*args, **kwargs):
        ...
    @staticmethod
    def setRawFont(*args, **kwargs):
        ...
    @staticmethod
    def setRightToLeft(*args, **kwargs):
        ...
    @staticmethod
    def setSourceString(*args, **kwargs):
        ...
    @staticmethod
    def setStrikeOut(*args, **kwargs):
        ...
    @staticmethod
    def setStringIndexes(*args, **kwargs):
        ...
    @staticmethod
    def setUnderline(*args, **kwargs):
        ...
    @staticmethod
    def sourceString(*args, **kwargs):
        ...
    @staticmethod
    def strikeOut(*args, **kwargs):
        ...
    @staticmethod
    def stringIndexes(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def underline(*args, **kwargs):
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
class QGradient(PyQt6.sip.simplewrapper):
    class CoordinateMode(enum.Enum):
        LogicalMode: typing.ClassVar[QGradient.CoordinateMode]  # value = <CoordinateMode.LogicalMode: 0>
        ObjectBoundingMode: typing.ClassVar[QGradient.CoordinateMode]  # value = <CoordinateMode.ObjectBoundingMode: 2>
        ObjectMode: typing.ClassVar[QGradient.CoordinateMode]  # value = <CoordinateMode.ObjectMode: 3>
        StretchToDeviceMode: typing.ClassVar[QGradient.CoordinateMode]  # value = <CoordinateMode.StretchToDeviceMode: 1>
    class Preset(enum.Enum):
        AboveTheSky: typing.ClassVar[QGradient.Preset]  # value = <Preset.AboveTheSky: 116>
        AfricanField: typing.ClassVar[QGradient.Preset]  # value = <Preset.AfricanField: 131>
        AlchemistLab: typing.ClassVar[QGradient.Preset]  # value = <Preset.AlchemistLab: 87>
        AmourAmour: typing.ClassVar[QGradient.Preset]  # value = <Preset.AmourAmour: 97>
        AmyCrisp: typing.ClassVar[QGradient.Preset]  # value = <Preset.AmyCrisp: 14>
        AngelCare: typing.ClassVar[QGradient.Preset]  # value = <Preset.AngelCare: 158>
        AquaGuidance: typing.ClassVar[QGradient.Preset]  # value = <Preset.AquaGuidance: 150>
        AquaSplash: typing.ClassVar[QGradient.Preset]  # value = <Preset.AquaSplash: 70>
        AwesomePine: typing.ClassVar[QGradient.Preset]  # value = <Preset.AwesomePine: 42>
        BigMango: typing.ClassVar[QGradient.Preset]  # value = <Preset.BigMango: 95>
        BlackSea: typing.ClassVar[QGradient.Preset]  # value = <Preset.BlackSea: 153>
        Blessing: typing.ClassVar[QGradient.Preset]  # value = <Preset.Blessing: 31>
        BurningSpring: typing.ClassVar[QGradient.Preset]  # value = <Preset.BurningSpring: 65>
        CheerfulCaramel: typing.ClassVar[QGradient.Preset]  # value = <Preset.CheerfulCaramel: 122>
        ChildCare: typing.ClassVar[QGradient.Preset]  # value = <Preset.ChildCare: 112>
        CleanMirror: typing.ClassVar[QGradient.Preset]  # value = <Preset.CleanMirror: 75>
        CloudyApple: typing.ClassVar[QGradient.Preset]  # value = <Preset.CloudyApple: 94>
        CloudyKnoxville: typing.ClassVar[QGradient.Preset]  # value = <Preset.CloudyKnoxville: 18>
        CochitiLake: typing.ClassVar[QGradient.Preset]  # value = <Preset.CochitiLake: 78>
        ColdEvening: typing.ClassVar[QGradient.Preset]  # value = <Preset.ColdEvening: 77>
        ColorfulPeach: typing.ClassVar[QGradient.Preset]  # value = <Preset.ColorfulPeach: 126>
        ConfidentCloud: typing.ClassVar[QGradient.Preset]  # value = <Preset.ConfidentCloud: 107>
        CrystalRiver: typing.ClassVar[QGradient.Preset]  # value = <Preset.CrystalRiver: 159>
        Crystalline: typing.ClassVar[QGradient.Preset]  # value = <Preset.Crystalline: 104>
        DeepBlue: typing.ClassVar[QGradient.Preset]  # value = <Preset.DeepBlue: 16>
        DeepRelief: typing.ClassVar[QGradient.Preset]  # value = <Preset.DeepRelief: 166>
        DenseWater: typing.ClassVar[QGradient.Preset]  # value = <Preset.DenseWater: 118>
        DesertHump: typing.ClassVar[QGradient.Preset]  # value = <Preset.DesertHump: 82>
        DirtyBeauty: typing.ClassVar[QGradient.Preset]  # value = <Preset.DirtyBeauty: 57>
        DustyGrass: typing.ClassVar[QGradient.Preset]  # value = <Preset.DustyGrass: 11>
        EternalConstance: typing.ClassVar[QGradient.Preset]  # value = <Preset.EternalConstance: 91>
        EverlastingSky: typing.ClassVar[QGradient.Preset]  # value = <Preset.EverlastingSky: 29>
        FabledSunset: typing.ClassVar[QGradient.Preset]  # value = <Preset.FabledSunset: 179>
        FarawayRiver: typing.ClassVar[QGradient.Preset]  # value = <Preset.FarawayRiver: 86>
        FebruaryInk: typing.ClassVar[QGradient.Preset]  # value = <Preset.FebruaryInk: 51>
        FlyHigh: typing.ClassVar[QGradient.Preset]  # value = <Preset.FlyHigh: 47>
        FlyingLemon: typing.ClassVar[QGradient.Preset]  # value = <Preset.FlyingLemon: 113>
        ForestInei: typing.ClassVar[QGradient.Preset]  # value = <Preset.ForestInei: 143>
        FreshMilk: typing.ClassVar[QGradient.Preset]  # value = <Preset.FreshMilk: 49>
        FreshOasis: typing.ClassVar[QGradient.Preset]  # value = <Preset.FreshOasis: 163>
        FrozenBerry: typing.ClassVar[QGradient.Preset]  # value = <Preset.FrozenBerry: 110>
        FrozenDreams: typing.ClassVar[QGradient.Preset]  # value = <Preset.FrozenDreams: 9>
        FrozenHeat: typing.ClassVar[QGradient.Preset]  # value = <Preset.FrozenHeat: 177>
        FruitBlend: typing.ClassVar[QGradient.Preset]  # value = <Preset.FruitBlend: 137>
        GagarinView: typing.ClassVar[QGradient.Preset]  # value = <Preset.GagarinView: 178>
        GentleCare: typing.ClassVar[QGradient.Preset]  # value = <Preset.GentleCare: 127>
        GlassWater: typing.ClassVar[QGradient.Preset]  # value = <Preset.GlassWater: 134>
        GrassShampoo: typing.ClassVar[QGradient.Preset]  # value = <Preset.GrassShampoo: 154>
        GreatWhale: typing.ClassVar[QGradient.Preset]  # value = <Preset.GreatWhale: 58>
        GrownEarly: typing.ClassVar[QGradient.Preset]  # value = <Preset.GrownEarly: 54>
        HappyAcid: typing.ClassVar[QGradient.Preset]  # value = <Preset.HappyAcid: 41>
        HappyFisher: typing.ClassVar[QGradient.Preset]  # value = <Preset.HappyFisher: 30>
        HappyMemories: typing.ClassVar[QGradient.Preset]  # value = <Preset.HappyMemories: 102>
        HappyUnicorn: typing.ClassVar[QGradient.Preset]  # value = <Preset.HappyUnicorn: 129>
        HealthyWater: typing.ClassVar[QGradient.Preset]  # value = <Preset.HealthyWater: 96>
        HeavenPeach: typing.ClassVar[QGradient.Preset]  # value = <Preset.HeavenPeach: 68>
        HeavyRain: typing.ClassVar[QGradient.Preset]  # value = <Preset.HeavyRain: 13>
        HiddenJaguar: typing.ClassVar[QGradient.Preset]  # value = <Preset.HiddenJaguar: 115>
        HighFlight: typing.ClassVar[QGradient.Preset]  # value = <Preset.HighFlight: 139>
        ItmeoBranding: typing.ClassVar[QGradient.Preset]  # value = <Preset.ItmeoBranding: 35>
        JapanBlush: typing.ClassVar[QGradient.Preset]  # value = <Preset.JapanBlush: 92>
        JuicyCake: typing.ClassVar[QGradient.Preset]  # value = <Preset.JuicyCake: 146>
        JuicyPeach: typing.ClassVar[QGradient.Preset]  # value = <Preset.JuicyPeach: 4>
        JungleDay: typing.ClassVar[QGradient.Preset]  # value = <Preset.JungleDay: 83>
        KindSteel: typing.ClassVar[QGradient.Preset]  # value = <Preset.KindSteel: 52>
        LadogaBottom: typing.ClassVar[QGradient.Preset]  # value = <Preset.LadogaBottom: 33>
        LadyLips: typing.ClassVar[QGradient.Preset]  # value = <Preset.LadyLips: 6>
        LandingAircraft: typing.ClassVar[QGradient.Preset]  # value = <Preset.LandingAircraft: 155>
        LeCocktail: typing.ClassVar[QGradient.Preset]  # value = <Preset.LeCocktail: 108>
        LemonGate: typing.ClassVar[QGradient.Preset]  # value = <Preset.LemonGate: 34>
        LightBlue: typing.ClassVar[QGradient.Preset]  # value = <Preset.LightBlue: 170>
        LilyMeadow: typing.ClassVar[QGradient.Preset]  # value = <Preset.LilyMeadow: 172>
        LoveKiss: typing.ClassVar[QGradient.Preset]  # value = <Preset.LoveKiss: 73>
        MagicLake: typing.ClassVar[QGradient.Preset]  # value = <Preset.MagicLake: 124>
        MagicRay: typing.ClassVar[QGradient.Preset]  # value = <Preset.MagicRay: 175>
        MalibuBeach: typing.ClassVar[QGradient.Preset]  # value = <Preset.MalibuBeach: 19>
        MarbleWall: typing.ClassVar[QGradient.Preset]  # value = <Preset.MarbleWall: 121>
        MarsParty: typing.ClassVar[QGradient.Preset]  # value = <Preset.MarsParty: 90>
        MeanFruit: typing.ClassVar[QGradient.Preset]  # value = <Preset.MeanFruit: 15>
        MidnightBloom: typing.ClassVar[QGradient.Preset]  # value = <Preset.MidnightBloom: 103>
        MillenniumPine: typing.ClassVar[QGradient.Preset]  # value = <Preset.MillenniumPine: 138>
        MindCrawl: typing.ClassVar[QGradient.Preset]  # value = <Preset.MindCrawl: 171>
        MixedHopes: typing.ClassVar[QGradient.Preset]  # value = <Preset.MixedHopes: 46>
        MoleHall: typing.ClassVar[QGradient.Preset]  # value = <Preset.MoleHall: 140>
        MorningSalad: typing.ClassVar[QGradient.Preset]  # value = <Preset.MorningSalad: 165>
        MorpheusDen: typing.ClassVar[QGradient.Preset]  # value = <Preset.MorpheusDen: 22>
        MountainRock: typing.ClassVar[QGradient.Preset]  # value = <Preset.MountainRock: 81>
        NearMoon: typing.ClassVar[QGradient.Preset]  # value = <Preset.NearMoon: 24>
        Nega: typing.ClassVar[QGradient.Preset]  # value = <Preset.Nega: 117>
        NewLife: typing.ClassVar[QGradient.Preset]  # value = <Preset.NewLife: 20>
        NewRetrowave: typing.ClassVar[QGradient.Preset]  # value = <Preset.NewRetrowave: 114>
        NewYork: typing.ClassVar[QGradient.Preset]  # value = <Preset.NewYork: 43>
        NightCall: typing.ClassVar[QGradient.Preset]  # value = <Preset.NightCall: 168>
        NightFade: typing.ClassVar[QGradient.Preset]  # value = <Preset.NightFade: 2>
        NightParty: typing.ClassVar[QGradient.Preset]  # value = <Preset.NightParty: 66>
        NightSky: typing.ClassVar[QGradient.Preset]  # value = <Preset.NightSky: 123>
        NorseBeauty: typing.ClassVar[QGradient.Preset]  # value = <Preset.NorseBeauty: 149>
        NorthMiracle: typing.ClassVar[QGradient.Preset]  # value = <Preset.NorthMiracle: 136>
        NumPresets: typing.ClassVar[QGradient.Preset]  # value = <Preset.NumPresets: 181>
        OctoberSilence: typing.ClassVar[QGradient.Preset]  # value = <Preset.OctoberSilence: 85>
        OldHat: typing.ClassVar[QGradient.Preset]  # value = <Preset.OldHat: 37>
        OrangeJuice: typing.ClassVar[QGradient.Preset]  # value = <Preset.OrangeJuice: 133>
        OverSun: typing.ClassVar[QGradient.Preset]  # value = <Preset.OverSun: 88>
        PaloAlto: typing.ClassVar[QGradient.Preset]  # value = <Preset.PaloAlto: 101>
        PartyBliss: typing.ClassVar[QGradient.Preset]  # value = <Preset.PartyBliss: 106>
        PassionateBed: typing.ClassVar[QGradient.Preset]  # value = <Preset.PassionateBed: 80>
        PerfectBlue: typing.ClassVar[QGradient.Preset]  # value = <Preset.PerfectBlue: 180>
        PerfectWhite: typing.ClassVar[QGradient.Preset]  # value = <Preset.PerfectWhite: 162>
        PhoenixStart: typing.ClassVar[QGradient.Preset]  # value = <Preset.PhoenixStart: 84>
        PlumBath: typing.ClassVar[QGradient.Preset]  # value = <Preset.PlumBath: 128>
        PlumPlate: typing.ClassVar[QGradient.Preset]  # value = <Preset.PlumPlate: 28>
        PoliteRumors: typing.ClassVar[QGradient.Preset]  # value = <Preset.PoliteRumors: 60>
        PremiumDark: typing.ClassVar[QGradient.Preset]  # value = <Preset.PremiumDark: 76>
        PremiumWhite: typing.ClassVar[QGradient.Preset]  # value = <Preset.PremiumWhite: 89>
        PurpleDivision: typing.ClassVar[QGradient.Preset]  # value = <Preset.PurpleDivision: 69>
        RainyAshville: typing.ClassVar[QGradient.Preset]  # value = <Preset.RainyAshville: 8>
        RareWind: typing.ClassVar[QGradient.Preset]  # value = <Preset.RareWind: 23>
        RedSalvation: typing.ClassVar[QGradient.Preset]  # value = <Preset.RedSalvation: 64>
        RichMetal: typing.ClassVar[QGradient.Preset]  # value = <Preset.RichMetal: 145>
        RipeMalinka: typing.ClassVar[QGradient.Preset]  # value = <Preset.RipeMalinka: 17>
        RiskyConcrete: typing.ClassVar[QGradient.Preset]  # value = <Preset.RiskyConcrete: 98>
        RiverCity: typing.ClassVar[QGradient.Preset]  # value = <Preset.RiverCity: 109>
        RoyalGarden: typing.ClassVar[QGradient.Preset]  # value = <Preset.RoyalGarden: 144>
        SaintPetersburg: typing.ClassVar[QGradient.Preset]  # value = <Preset.SaintPetersburg: 26>
        SaltMountain: typing.ClassVar[QGradient.Preset]  # value = <Preset.SaltMountain: 161>
        SandStrike: typing.ClassVar[QGradient.Preset]  # value = <Preset.SandStrike: 148>
        SeaLord: typing.ClassVar[QGradient.Preset]  # value = <Preset.SeaLord: 152>
        SeaStrike: typing.ClassVar[QGradient.Preset]  # value = <Preset.SeaStrike: 167>
        Seashore: typing.ClassVar[QGradient.Preset]  # value = <Preset.Seashore: 120>
        ShadyWater: typing.ClassVar[QGradient.Preset]  # value = <Preset.ShadyWater: 56>
        SharpBlues: typing.ClassVar[QGradient.Preset]  # value = <Preset.SharpBlues: 55>
        SharpeyeEagle: typing.ClassVar[QGradient.Preset]  # value = <Preset.SharpeyeEagle: 32>
        ShyRainbow: typing.ClassVar[QGradient.Preset]  # value = <Preset.ShyRainbow: 44>
        SkyGlider: typing.ClassVar[QGradient.Preset]  # value = <Preset.SkyGlider: 67>
        SleeplessNight: typing.ClassVar[QGradient.Preset]  # value = <Preset.SleeplessNight: 157>
        SmartIndigo: typing.ClassVar[QGradient.Preset]  # value = <Preset.SmartIndigo: 147>
        SmilingRain: typing.ClassVar[QGradient.Preset]  # value = <Preset.SmilingRain: 93>
        SnowAgain: typing.ClassVar[QGradient.Preset]  # value = <Preset.SnowAgain: 50>
        SoftCherish: typing.ClassVar[QGradient.Preset]  # value = <Preset.SoftCherish: 63>
        SoftGrass: typing.ClassVar[QGradient.Preset]  # value = <Preset.SoftGrass: 53>
        SoftLipstick: typing.ClassVar[QGradient.Preset]  # value = <Preset.SoftLipstick: 160>
        SolidStone: typing.ClassVar[QGradient.Preset]  # value = <Preset.SolidStone: 132>
        SpaceShift: typing.ClassVar[QGradient.Preset]  # value = <Preset.SpaceShift: 142>
        SpikyNaga: typing.ClassVar[QGradient.Preset]  # value = <Preset.SpikyNaga: 72>
        SpringWarmth: typing.ClassVar[QGradient.Preset]  # value = <Preset.SpringWarmth: 3>
        StarWine: typing.ClassVar[QGradient.Preset]  # value = <Preset.StarWine: 38>
        StrictNovember: typing.ClassVar[QGradient.Preset]  # value = <Preset.StrictNovember: 164>
        StrongBliss: typing.ClassVar[QGradient.Preset]  # value = <Preset.StrongBliss: 48>
        StrongStick: typing.ClassVar[QGradient.Preset]  # value = <Preset.StrongStick: 99>
        SugarLollipop: typing.ClassVar[QGradient.Preset]  # value = <Preset.SugarLollipop: 173>
        SummerGames: typing.ClassVar[QGradient.Preset]  # value = <Preset.SummerGames: 79>
        SunVeggie: typing.ClassVar[QGradient.Preset]  # value = <Preset.SunVeggie: 151>
        SunnyMorning: typing.ClassVar[QGradient.Preset]  # value = <Preset.SunnyMorning: 7>
        SupremeSky: typing.ClassVar[QGradient.Preset]  # value = <Preset.SupremeSky: 169>
        SweetDessert: typing.ClassVar[QGradient.Preset]  # value = <Preset.SweetDessert: 174>
        SweetPeriod: typing.ClassVar[QGradient.Preset]  # value = <Preset.SweetPeriod: 61>
        TeenNotebook: typing.ClassVar[QGradient.Preset]  # value = <Preset.TeenNotebook: 59>
        TeenParty: typing.ClassVar[QGradient.Preset]  # value = <Preset.TeenParty: 176>
        TemptingAzure: typing.ClassVar[QGradient.Preset]  # value = <Preset.TemptingAzure: 12>
        TrueSunset: typing.ClassVar[QGradient.Preset]  # value = <Preset.TrueSunset: 21>
        ViciousStance: typing.ClassVar[QGradient.Preset]  # value = <Preset.ViciousStance: 100>
        WarmFlame: typing.ClassVar[QGradient.Preset]  # value = <Preset.WarmFlame: 1>
        WideMatrix: typing.ClassVar[QGradient.Preset]  # value = <Preset.WideMatrix: 62>
        WildApple: typing.ClassVar[QGradient.Preset]  # value = <Preset.WildApple: 25>
        WinterNeva: typing.ClassVar[QGradient.Preset]  # value = <Preset.WinterNeva: 10>
        WitchDance: typing.ClassVar[QGradient.Preset]  # value = <Preset.WitchDance: 156>
        YoungGrass: typing.ClassVar[QGradient.Preset]  # value = <Preset.YoungGrass: 125>
        YoungPassion: typing.ClassVar[QGradient.Preset]  # value = <Preset.YoungPassion: 5>
        ZeusMiracle: typing.ClassVar[QGradient.Preset]  # value = <Preset.ZeusMiracle: 36>
    class Spread(enum.Enum):
        PadSpread: typing.ClassVar[QGradient.Spread]  # value = <Spread.PadSpread: 0>
        ReflectSpread: typing.ClassVar[QGradient.Spread]  # value = <Spread.ReflectSpread: 1>
        RepeatSpread: typing.ClassVar[QGradient.Spread]  # value = <Spread.RepeatSpread: 2>
    class Type(enum.Enum):
        ConicalGradient: typing.ClassVar[QGradient.Type]  # value = <Type.ConicalGradient: 2>
        LinearGradient: typing.ClassVar[QGradient.Type]  # value = <Type.LinearGradient: 0>
        NoGradient: typing.ClassVar[QGradient.Type]  # value = <Type.NoGradient: 3>
        RadialGradient: typing.ClassVar[QGradient.Type]  # value = <Type.RadialGradient: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def coordinateMode(*args, **kwargs):
        ...
    @staticmethod
    def setColorAt(*args, **kwargs):
        ...
    @staticmethod
    def setCoordinateMode(*args, **kwargs):
        ...
    @staticmethod
    def setSpread(*args, **kwargs):
        ...
    @staticmethod
    def setStops(*args, **kwargs):
        ...
    @staticmethod
    def spread(*args, **kwargs):
        ...
    @staticmethod
    def stops(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
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
class QGuiApplication(PyQt6.QtCore.QCoreApplication):
    @staticmethod
    def allWindows(*args, **kwargs):
        ...
    @staticmethod
    def applicationDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def applicationDisplayNameChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def applicationState(*args, **kwargs):
        ...
    @staticmethod
    def applicationStateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def changeOverrideCursor(*args, **kwargs):
        ...
    @staticmethod
    def clipboard(*args, **kwargs):
        ...
    @staticmethod
    def commitDataRequest(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def desktopFileName(*args, **kwargs):
        ...
    @staticmethod
    def desktopSettingsAware(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def focusObject(*args, **kwargs):
        ...
    @staticmethod
    def focusObjectChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def focusWindow(*args, **kwargs):
        ...
    @staticmethod
    def focusWindowChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def font(*args, **kwargs):
        ...
    @staticmethod
    def fontDatabaseChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def highDpiScaleFactorRoundingPolicy(*args, **kwargs):
        ...
    @staticmethod
    def inputMethod(*args, **kwargs):
        ...
    @staticmethod
    def isLeftToRight(*args, **kwargs):
        ...
    @staticmethod
    def isRightToLeft(*args, **kwargs):
        ...
    @staticmethod
    def isSavingSession(*args, **kwargs):
        ...
    @staticmethod
    def isSessionRestored(*args, **kwargs):
        ...
    @staticmethod
    def keyboardModifiers(*args, **kwargs):
        ...
    @staticmethod
    def lastWindowClosed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def layoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def layoutDirectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def modalWindow(*args, **kwargs):
        ...
    @staticmethod
    def mouseButtons(*args, **kwargs):
        ...
    @staticmethod
    def notify(*args, **kwargs):
        ...
    @staticmethod
    def overrideCursor(*args, **kwargs):
        ...
    @staticmethod
    def palette(*args, **kwargs):
        ...
    @staticmethod
    def platformName(*args, **kwargs):
        ...
    @staticmethod
    def primaryScreen(*args, **kwargs):
        ...
    @staticmethod
    def primaryScreenChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def queryKeyboardModifiers(*args, **kwargs):
        ...
    @staticmethod
    def quitOnLastWindowClosed(*args, **kwargs):
        ...
    @staticmethod
    def restoreOverrideCursor(*args, **kwargs):
        ...
    @staticmethod
    def saveStateRequest(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def screenAdded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def screenAt(*args, **kwargs):
        ...
    @staticmethod
    def screenRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def screens(*args, **kwargs):
        ...
    @staticmethod
    def sessionId(*args, **kwargs):
        ...
    @staticmethod
    def sessionKey(*args, **kwargs):
        ...
    @staticmethod
    def setApplicationDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def setBadgeNumber(*args, **kwargs):
        ...
    @staticmethod
    def setDesktopFileName(*args, **kwargs):
        ...
    @staticmethod
    def setDesktopSettingsAware(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setHighDpiScaleFactorRoundingPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setLayoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def setOverrideCursor(*args, **kwargs):
        ...
    @staticmethod
    def setPalette(*args, **kwargs):
        ...
    @staticmethod
    def setQuitOnLastWindowClosed(*args, **kwargs):
        ...
    @staticmethod
    def setWindowIcon(*args, **kwargs):
        ...
    @staticmethod
    def styleHints(*args, **kwargs):
        ...
    @staticmethod
    def sync(*args, **kwargs):
        ...
    @staticmethod
    def topLevelAt(*args, **kwargs):
        ...
    @staticmethod
    def topLevelWindows(*args, **kwargs):
        ...
    @staticmethod
    def windowIcon(*args, **kwargs):
        ...
class QHelpEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def globalPos(*args, **kwargs):
        ...
    @staticmethod
    def globalX(*args, **kwargs):
        ...
    @staticmethod
    def globalY(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
class QHideEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QHoverEvent(QSinglePointEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def isUpdateEvent(*args, **kwargs):
        ...
    @staticmethod
    def oldPos(*args, **kwargs):
        ...
    @staticmethod
    def oldPosF(*args, **kwargs):
        ...
class QIcon(PyQt6.sip.wrapper):
    class Mode(enum.Enum):
        Active: typing.ClassVar[QIcon.Mode]  # value = <Mode.Active: 2>
        Disabled: typing.ClassVar[QIcon.Mode]  # value = <Mode.Disabled: 1>
        Normal: typing.ClassVar[QIcon.Mode]  # value = <Mode.Normal: 0>
        Selected: typing.ClassVar[QIcon.Mode]  # value = <Mode.Selected: 3>
    class State(enum.Enum):
        Off: typing.ClassVar[QIcon.State]  # value = <State.Off: 1>
        On: typing.ClassVar[QIcon.State]  # value = <State.On: 0>
    class ThemeIcon(enum.Enum):
        AddressBookNew: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AddressBookNew: 0>
        ApplicationExit: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ApplicationExit: 1>
        AppointmentMissed: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AppointmentMissed: 108>
        AppointmentNew: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AppointmentNew: 2>
        AppointmentSoon: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AppointmentSoon: 109>
        AudioCard: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AudioCard: 85>
        AudioInputMicrophone: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AudioInputMicrophone: 86>
        AudioVolumeHigh: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AudioVolumeHigh: 110>
        AudioVolumeLow: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AudioVolumeLow: 111>
        AudioVolumeMedium: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AudioVolumeMedium: 112>
        AudioVolumeMuted: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.AudioVolumeMuted: 113>
        Battery: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.Battery: 87>
        BatteryCaution: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.BatteryCaution: 114>
        BatteryLow: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.BatteryLow: 115>
        CallStart: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.CallStart: 3>
        CallStop: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.CallStop: 4>
        CameraPhoto: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.CameraPhoto: 88>
        CameraVideo: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.CameraVideo: 89>
        CameraWeb: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.CameraWeb: 90>
        Computer: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.Computer: 91>
        ContactNew: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ContactNew: 5>
        DialogError: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DialogError: 116>
        DialogInformation: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DialogInformation: 117>
        DialogPassword: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DialogPassword: 118>
        DialogQuestion: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DialogQuestion: 119>
        DialogWarning: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DialogWarning: 120>
        DocumentNew: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentNew: 6>
        DocumentOpen: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentOpen: 7>
        DocumentOpenRecent: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentOpenRecent: 8>
        DocumentPageSetup: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentPageSetup: 9>
        DocumentPrint: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentPrint: 10>
        DocumentPrintPreview: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentPrintPreview: 11>
        DocumentProperties: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentProperties: 12>
        DocumentRevert: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentRevert: 13>
        DocumentSave: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentSave: 14>
        DocumentSaveAs: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentSaveAs: 15>
        DocumentSend: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DocumentSend: 16>
        DriveHarddisk: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DriveHarddisk: 92>
        DriveOptical: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.DriveOptical: 93>
        EditClear: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditClear: 17>
        EditCopy: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditCopy: 18>
        EditCut: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditCut: 19>
        EditDelete: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditDelete: 20>
        EditFind: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditFind: 21>
        EditPaste: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditPaste: 22>
        EditRedo: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditRedo: 23>
        EditSelectAll: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditSelectAll: 24>
        EditUndo: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.EditUndo: 25>
        FolderDragAccept: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FolderDragAccept: 121>
        FolderNew: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FolderNew: 26>
        FolderOpen: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FolderOpen: 122>
        FolderVisiting: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FolderVisiting: 123>
        FormatIndentLess: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatIndentLess: 27>
        FormatIndentMore: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatIndentMore: 28>
        FormatJustifyCenter: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatJustifyCenter: 29>
        FormatJustifyFill: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatJustifyFill: 30>
        FormatJustifyLeft: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatJustifyLeft: 31>
        FormatJustifyRight: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatJustifyRight: 32>
        FormatTextBold: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatTextBold: 35>
        FormatTextDirectionLtr: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatTextDirectionLtr: 33>
        FormatTextDirectionRtl: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatTextDirectionRtl: 34>
        FormatTextItalic: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatTextItalic: 36>
        FormatTextStrikethrough: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatTextStrikethrough: 38>
        FormatTextUnderline: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.FormatTextUnderline: 37>
        GoDown: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.GoDown: 39>
        GoHome: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.GoHome: 40>
        GoNext: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.GoNext: 41>
        GoPrevious: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.GoPrevious: 42>
        GoUp: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.GoUp: 43>
        HelpAbout: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.HelpAbout: 44>
        HelpFaq: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.HelpFaq: 45>
        ImageLoading: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ImageLoading: 124>
        ImageMissing: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ImageMissing: 125>
        InputGaming: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.InputGaming: 94>
        InputKeyboard: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.InputKeyboard: 95>
        InputMouse: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.InputMouse: 96>
        InputTablet: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.InputTablet: 97>
        InsertImage: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.InsertImage: 46>
        InsertLink: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.InsertLink: 47>
        InsertText: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.InsertText: 48>
        ListAdd: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ListAdd: 49>
        ListRemove: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ListRemove: 50>
        MailAttachment: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailAttachment: 126>
        MailForward: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailForward: 51>
        MailMarkImportant: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailMarkImportant: 52>
        MailMarkRead: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailMarkRead: 53>
        MailMarkUnread: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailMarkUnread: 54>
        MailMessageNew: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailMessageNew: 55>
        MailRead: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailRead: 128>
        MailReplied: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailReplied: 129>
        MailReplyAll: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailReplyAll: 56>
        MailReplySender: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailReplySender: 57>
        MailSend: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailSend: 58>
        MailUnread: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MailUnread: 127>
        MediaEject: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaEject: 59>
        MediaFlash: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaFlash: 98>
        MediaOptical: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaOptical: 99>
        MediaPlaybackPause: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaPlaybackPause: 60>
        MediaPlaybackStart: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaPlaybackStart: 61>
        MediaPlaybackStop: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaPlaybackStop: 62>
        MediaPlaylistRepeat: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaPlaylistRepeat: 130>
        MediaPlaylistShuffle: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaPlaylistShuffle: 131>
        MediaRecord: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaRecord: 63>
        MediaSeekBackward: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaSeekBackward: 64>
        MediaSeekForward: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaSeekForward: 65>
        MediaSkipBackward: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaSkipBackward: 66>
        MediaSkipForward: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaSkipForward: 67>
        MediaTape: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MediaTape: 100>
        MultimediaPlayer: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.MultimediaPlayer: 101>
        NetworkOffline: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.NetworkOffline: 132>
        NetworkWired: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.NetworkWired: 102>
        NetworkWireless: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.NetworkWireless: 103>
        ObjectRotateLeft: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ObjectRotateLeft: 68>
        ObjectRotateRight: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ObjectRotateRight: 69>
        Phone: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.Phone: 104>
        Printer: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.Printer: 105>
        PrinterPrinting: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.PrinterPrinting: 133>
        ProcessStop: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ProcessStop: 70>
        Scanner: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.Scanner: 106>
        SecurityHigh: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SecurityHigh: 134>
        SecurityLow: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SecurityLow: 135>
        SoftwareUpdateAvailable: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SoftwareUpdateAvailable: 136>
        SoftwareUpdateUrgent: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SoftwareUpdateUrgent: 137>
        SyncError: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SyncError: 138>
        SyncSynchronizing: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SyncSynchronizing: 139>
        SystemLockScreen: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SystemLockScreen: 71>
        SystemLogOut: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SystemLogOut: 72>
        SystemReboot: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SystemReboot: 74>
        SystemSearch: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SystemSearch: 73>
        SystemShutdown: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.SystemShutdown: 75>
        ToolsCheckSpelling: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ToolsCheckSpelling: 76>
        UserAvailable: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.UserAvailable: 140>
        UserOffline: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.UserOffline: 141>
        VideoDisplay: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.VideoDisplay: 107>
        ViewFullscreen: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ViewFullscreen: 77>
        ViewRefresh: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ViewRefresh: 78>
        ViewRestore: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ViewRestore: 79>
        WeatherClear: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherClear: 142>
        WeatherClearNight: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherClearNight: 143>
        WeatherFewClouds: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherFewClouds: 144>
        WeatherFewCloudsNight: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherFewCloudsNight: 145>
        WeatherFog: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherFog: 146>
        WeatherShowers: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherShowers: 147>
        WeatherSnow: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherSnow: 148>
        WeatherStorm: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WeatherStorm: 149>
        WindowClose: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WindowClose: 80>
        WindowNew: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.WindowNew: 81>
        ZoomFitBest: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ZoomFitBest: 82>
        ZoomIn: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ZoomIn: 83>
        ZoomOut: typing.ClassVar[QIcon.ThemeIcon]  # value = <ThemeIcon.ZoomOut: 84>
    @staticmethod
    def actualSize(*args, **kwargs):
        ...
    @staticmethod
    def addFile(*args, **kwargs):
        ...
    @staticmethod
    def addPixmap(*args, **kwargs):
        ...
    @staticmethod
    def availableSizes(*args, **kwargs):
        ...
    @staticmethod
    def cacheKey(*args, **kwargs):
        ...
    @staticmethod
    def fallbackSearchPaths(*args, **kwargs):
        ...
    @staticmethod
    def fallbackThemeName(*args, **kwargs):
        ...
    @staticmethod
    def fromTheme(*args, **kwargs):
        ...
    @staticmethod
    def hasThemeIcon(*args, **kwargs):
        ...
    @staticmethod
    def isDetached(*args, **kwargs):
        ...
    @staticmethod
    def isMask(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def setFallbackSearchPaths(*args, **kwargs):
        ...
    @staticmethod
    def setFallbackThemeName(*args, **kwargs):
        ...
    @staticmethod
    def setIsMask(*args, **kwargs):
        ...
    @staticmethod
    def setThemeName(*args, **kwargs):
        ...
    @staticmethod
    def setThemeSearchPaths(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def themeName(*args, **kwargs):
        ...
    @staticmethod
    def themeSearchPaths(*args, **kwargs):
        ...
class QIconDragEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QIconEngine(PyQt6.sip.wrapper):
    class IconEngineHook(enum.Enum):
        IsNullHook: typing.ClassVar[QIconEngine.IconEngineHook]  # value = <IconEngineHook.IsNullHook: 3>
        ScaledPixmapHook: typing.ClassVar[QIconEngine.IconEngineHook]  # value = <IconEngineHook.ScaledPixmapHook: 4>
    class ScaledPixmapArgument(PyQt6.sip.simplewrapper):
        pass
    @staticmethod
    def actualSize(*args, **kwargs):
        ...
    @staticmethod
    def addFile(*args, **kwargs):
        ...
    @staticmethod
    def addPixmap(*args, **kwargs):
        ...
    @staticmethod
    def availableSizes(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def iconName(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def paint(*args, **kwargs):
        ...
    @staticmethod
    def pixmap(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def scaledPixmap(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
class QImage(QPaintDevice):
    class Format(enum.Enum):
        Format_A2BGR30_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_A2BGR30_Premultiplied: 20>
        Format_A2RGB30_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_A2RGB30_Premultiplied: 22>
        Format_ARGB32: typing.ClassVar[QImage.Format]  # value = <Format.Format_ARGB32: 5>
        Format_ARGB32_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_ARGB32_Premultiplied: 6>
        Format_ARGB4444_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_ARGB4444_Premultiplied: 15>
        Format_ARGB6666_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_ARGB6666_Premultiplied: 10>
        Format_ARGB8555_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_ARGB8555_Premultiplied: 12>
        Format_ARGB8565_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_ARGB8565_Premultiplied: 8>
        Format_Alpha8: typing.ClassVar[QImage.Format]  # value = <Format.Format_Alpha8: 23>
        Format_BGR30: typing.ClassVar[QImage.Format]  # value = <Format.Format_BGR30: 19>
        Format_BGR888: typing.ClassVar[QImage.Format]  # value = <Format.Format_BGR888: 29>
        Format_Grayscale16: typing.ClassVar[QImage.Format]  # value = <Format.Format_Grayscale16: 28>
        Format_Grayscale8: typing.ClassVar[QImage.Format]  # value = <Format.Format_Grayscale8: 24>
        Format_Indexed8: typing.ClassVar[QImage.Format]  # value = <Format.Format_Indexed8: 3>
        Format_Invalid: typing.ClassVar[QImage.Format]  # value = <Format.Format_Invalid: 0>
        Format_Mono: typing.ClassVar[QImage.Format]  # value = <Format.Format_Mono: 1>
        Format_MonoLSB: typing.ClassVar[QImage.Format]  # value = <Format.Format_MonoLSB: 2>
        Format_RGB16: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGB16: 7>
        Format_RGB30: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGB30: 21>
        Format_RGB32: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGB32: 4>
        Format_RGB444: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGB444: 14>
        Format_RGB555: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGB555: 11>
        Format_RGB666: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGB666: 9>
        Format_RGB888: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGB888: 13>
        Format_RGBA16FPx4: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA16FPx4: 31>
        Format_RGBA16FPx4_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA16FPx4_Premultiplied: 32>
        Format_RGBA32FPx4: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA32FPx4: 34>
        Format_RGBA32FPx4_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA32FPx4_Premultiplied: 35>
        Format_RGBA64: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA64: 26>
        Format_RGBA64_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA64_Premultiplied: 27>
        Format_RGBA8888: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA8888: 17>
        Format_RGBA8888_Premultiplied: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBA8888_Premultiplied: 18>
        Format_RGBX16FPx4: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBX16FPx4: 30>
        Format_RGBX32FPx4: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBX32FPx4: 33>
        Format_RGBX64: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBX64: 25>
        Format_RGBX8888: typing.ClassVar[QImage.Format]  # value = <Format.Format_RGBX8888: 16>
    class InvertMode(enum.Enum):
        InvertRgb: typing.ClassVar[QImage.InvertMode]  # value = <InvertMode.InvertRgb: 0>
        InvertRgba: typing.ClassVar[QImage.InvertMode]  # value = <InvertMode.InvertRgba: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def allGray(*args, **kwargs):
        ...
    @staticmethod
    def applyColorTransform(*args, **kwargs):
        ...
    @staticmethod
    def bitPlaneCount(*args, **kwargs):
        ...
    @staticmethod
    def bits(*args, **kwargs):
        ...
    @staticmethod
    def bytesPerLine(*args, **kwargs):
        ...
    @staticmethod
    def cacheKey(*args, **kwargs):
        ...
    @staticmethod
    def color(*args, **kwargs):
        ...
    @staticmethod
    def colorCount(*args, **kwargs):
        ...
    @staticmethod
    def colorSpace(*args, **kwargs):
        ...
    @staticmethod
    def colorTable(*args, **kwargs):
        ...
    @staticmethod
    def colorTransformed(*args, **kwargs):
        ...
    @staticmethod
    def constBits(*args, **kwargs):
        ...
    @staticmethod
    def constScanLine(*args, **kwargs):
        ...
    @staticmethod
    def convertTo(*args, **kwargs):
        ...
    @staticmethod
    def convertToColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def convertToFormat(*args, **kwargs):
        ...
    @staticmethod
    def convertedTo(*args, **kwargs):
        ...
    @staticmethod
    def convertedToColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def createAlphaMask(*args, **kwargs):
        ...
    @staticmethod
    def createHeuristicMask(*args, **kwargs):
        ...
    @staticmethod
    def createMaskFromColor(*args, **kwargs):
        ...
    @staticmethod
    def depth(*args, **kwargs):
        ...
    @staticmethod
    def deviceIndependentSize(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def dotsPerMeterX(*args, **kwargs):
        ...
    @staticmethod
    def dotsPerMeterY(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def fromData(*args, **kwargs):
        ...
    @staticmethod
    def hasAlphaChannel(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def invertPixels(*args, **kwargs):
        ...
    @staticmethod
    def isGrayscale(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def loadFromData(*args, **kwargs):
        ...
    @staticmethod
    def mirror(*args, **kwargs):
        ...
    @staticmethod
    def mirrored(*args, **kwargs):
        ...
    @staticmethod
    def offset(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def pixel(*args, **kwargs):
        ...
    @staticmethod
    def pixelColor(*args, **kwargs):
        ...
    @staticmethod
    def pixelFormat(*args, **kwargs):
        ...
    @staticmethod
    def pixelIndex(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def reinterpretAsFormat(*args, **kwargs):
        ...
    @staticmethod
    def rgbSwap(*args, **kwargs):
        ...
    @staticmethod
    def rgbSwapped(*args, **kwargs):
        ...
    @staticmethod
    def save(*args, **kwargs):
        ...
    @staticmethod
    def scaled(*args, **kwargs):
        ...
    @staticmethod
    def scaledToHeight(*args, **kwargs):
        ...
    @staticmethod
    def scaledToWidth(*args, **kwargs):
        ...
    @staticmethod
    def scanLine(*args, **kwargs):
        ...
    @staticmethod
    def setAlphaChannel(*args, **kwargs):
        ...
    @staticmethod
    def setColor(*args, **kwargs):
        ...
    @staticmethod
    def setColorCount(*args, **kwargs):
        ...
    @staticmethod
    def setColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def setColorTable(*args, **kwargs):
        ...
    @staticmethod
    def setDevicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def setDotsPerMeterX(*args, **kwargs):
        ...
    @staticmethod
    def setDotsPerMeterY(*args, **kwargs):
        ...
    @staticmethod
    def setOffset(*args, **kwargs):
        ...
    @staticmethod
    def setPixel(*args, **kwargs):
        ...
    @staticmethod
    def setPixelColor(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def sizeInBytes(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textKeys(*args, **kwargs):
        ...
    @staticmethod
    def toImageFormat(*args, **kwargs):
        ...
    @staticmethod
    def toPixelFormat(*args, **kwargs):
        ...
    @staticmethod
    def transformed(*args, **kwargs):
        ...
    @staticmethod
    def trueMatrix(*args, **kwargs):
        ...
    @staticmethod
    def valid(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
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
class QImageIOHandler(PyQt6.sip.simplewrapper):
    class ImageOption(enum.Enum):
        Animation: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.Animation: 12>
        BackgroundColor: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.BackgroundColor: 13>
        ClipRect: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.ClipRect: 1>
        CompressionRatio: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.CompressionRatio: 5>
        Description: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.Description: 2>
        Endianness: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.Endianness: 11>
        Gamma: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.Gamma: 6>
        ImageTransformation: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.ImageTransformation: 18>
        IncrementalReading: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.IncrementalReading: 10>
        Name: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.Name: 8>
        OptimizedWrite: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.OptimizedWrite: 16>
        ProgressiveScanWrite: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.ProgressiveScanWrite: 17>
        Quality: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.Quality: 7>
        ScaledClipRect: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.ScaledClipRect: 3>
        ScaledSize: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.ScaledSize: 4>
        Size: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.Size: 0>
        SubType: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.SubType: 9>
        SupportedSubTypes: typing.ClassVar[QImageIOHandler.ImageOption]  # value = <ImageOption.SupportedSubTypes: 15>
    class Transformation(enum.Flag):
        TransformationFlip: typing.ClassVar[QImageIOHandler.Transformation]  # value = <Transformation.TransformationFlip: 2>
        TransformationMirror: typing.ClassVar[QImageIOHandler.Transformation]  # value = <Transformation.TransformationMirror: 1>
        TransformationRotate90: typing.ClassVar[QImageIOHandler.Transformation]  # value = <Transformation.TransformationRotate90: 4>
    @staticmethod
    def canRead(*args, **kwargs):
        ...
    @staticmethod
    def currentImageNumber(*args, **kwargs):
        ...
    @staticmethod
    def currentImageRect(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def imageCount(*args, **kwargs):
        ...
    @staticmethod
    def jumpToImage(*args, **kwargs):
        ...
    @staticmethod
    def jumpToNextImage(*args, **kwargs):
        ...
    @staticmethod
    def loopCount(*args, **kwargs):
        ...
    @staticmethod
    def nextImageDelay(*args, **kwargs):
        ...
    @staticmethod
    def option(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def supportsOption(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
class QImageReader(PyQt6.sip.simplewrapper):
    class ImageReaderError(enum.Enum):
        DeviceError: typing.ClassVar[QImageReader.ImageReaderError]  # value = <ImageReaderError.DeviceError: 2>
        FileNotFoundError: typing.ClassVar[QImageReader.ImageReaderError]  # value = <ImageReaderError.FileNotFoundError: 1>
        InvalidDataError: typing.ClassVar[QImageReader.ImageReaderError]  # value = <ImageReaderError.InvalidDataError: 4>
        UnknownError: typing.ClassVar[QImageReader.ImageReaderError]  # value = <ImageReaderError.UnknownError: 0>
        UnsupportedFormatError: typing.ClassVar[QImageReader.ImageReaderError]  # value = <ImageReaderError.UnsupportedFormatError: 3>
    @staticmethod
    def allocationLimit(*args, **kwargs):
        ...
    @staticmethod
    def autoDetectImageFormat(*args, **kwargs):
        ...
    @staticmethod
    def autoTransform(*args, **kwargs):
        ...
    @staticmethod
    def backgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def canRead(*args, **kwargs):
        ...
    @staticmethod
    def clipRect(*args, **kwargs):
        ...
    @staticmethod
    def currentImageNumber(*args, **kwargs):
        ...
    @staticmethod
    def currentImageRect(*args, **kwargs):
        ...
    @staticmethod
    def decideFormatFromContent(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def imageCount(*args, **kwargs):
        ...
    @staticmethod
    def imageFormat(*args, **kwargs):
        ...
    @staticmethod
    def imageFormatsForMimeType(*args, **kwargs):
        ...
    @staticmethod
    def jumpToImage(*args, **kwargs):
        ...
    @staticmethod
    def jumpToNextImage(*args, **kwargs):
        ...
    @staticmethod
    def loopCount(*args, **kwargs):
        ...
    @staticmethod
    def nextImageDelay(*args, **kwargs):
        ...
    @staticmethod
    def quality(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def scaledClipRect(*args, **kwargs):
        ...
    @staticmethod
    def scaledSize(*args, **kwargs):
        ...
    @staticmethod
    def setAllocationLimit(*args, **kwargs):
        ...
    @staticmethod
    def setAutoDetectImageFormat(*args, **kwargs):
        ...
    @staticmethod
    def setAutoTransform(*args, **kwargs):
        ...
    @staticmethod
    def setBackgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def setClipRect(*args, **kwargs):
        ...
    @staticmethod
    def setDecideFormatFromContent(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setQuality(*args, **kwargs):
        ...
    @staticmethod
    def setScaledClipRect(*args, **kwargs):
        ...
    @staticmethod
    def setScaledSize(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def subType(*args, **kwargs):
        ...
    @staticmethod
    def supportedImageFormats(*args, **kwargs):
        ...
    @staticmethod
    def supportedMimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def supportedSubTypes(*args, **kwargs):
        ...
    @staticmethod
    def supportsAnimation(*args, **kwargs):
        ...
    @staticmethod
    def supportsOption(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textKeys(*args, **kwargs):
        ...
    @staticmethod
    def transformation(*args, **kwargs):
        ...
class QImageWriter(PyQt6.sip.simplewrapper):
    class ImageWriterError(enum.Enum):
        DeviceError: typing.ClassVar[QImageWriter.ImageWriterError]  # value = <ImageWriterError.DeviceError: 1>
        InvalidImageError: typing.ClassVar[QImageWriter.ImageWriterError]  # value = <ImageWriterError.InvalidImageError: 3>
        UnknownError: typing.ClassVar[QImageWriter.ImageWriterError]  # value = <ImageWriterError.UnknownError: 0>
        UnsupportedFormatError: typing.ClassVar[QImageWriter.ImageWriterError]  # value = <ImageWriterError.UnsupportedFormatError: 2>
    @staticmethod
    def canWrite(*args, **kwargs):
        ...
    @staticmethod
    def compression(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def imageFormatsForMimeType(*args, **kwargs):
        ...
    @staticmethod
    def optimizedWrite(*args, **kwargs):
        ...
    @staticmethod
    def progressiveScanWrite(*args, **kwargs):
        ...
    @staticmethod
    def quality(*args, **kwargs):
        ...
    @staticmethod
    def setCompression(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setOptimizedWrite(*args, **kwargs):
        ...
    @staticmethod
    def setProgressiveScanWrite(*args, **kwargs):
        ...
    @staticmethod
    def setQuality(*args, **kwargs):
        ...
    @staticmethod
    def setSubType(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTransformation(*args, **kwargs):
        ...
    @staticmethod
    def subType(*args, **kwargs):
        ...
    @staticmethod
    def supportedImageFormats(*args, **kwargs):
        ...
    @staticmethod
    def supportedMimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def supportedSubTypes(*args, **kwargs):
        ...
    @staticmethod
    def supportsOption(*args, **kwargs):
        ...
    @staticmethod
    def transformation(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
class QInputDevice(PyQt6.QtCore.QObject):
    class Capability(enum.Flag):
        Area: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.Area: 2>
        Hover: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.Hover: 512>
        MouseEmulation: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.MouseEmulation: 64>
        NormalizedPosition: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.NormalizedPosition: 32>
        PixelScroll: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.PixelScroll: 128>
        Position: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.Position: 1>
        Pressure: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.Pressure: 4>
        Rotation: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.Rotation: 1024>
        Scroll: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.Scroll: 256>
        TangentialPressure: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.TangentialPressure: 8192>
        Velocity: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.Velocity: 8>
        XTilt: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.XTilt: 2048>
        YTilt: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.YTilt: 4096>
        ZPosition: typing.ClassVar[QInputDevice.Capability]  # value = <Capability.ZPosition: 16384>
    class DeviceType(enum.Flag):
        Airbrush: typing.ClassVar[QInputDevice.DeviceType]  # value = <DeviceType.Airbrush: 32>
        Keyboard: typing.ClassVar[QInputDevice.DeviceType]  # value = <DeviceType.Keyboard: 4096>
        Mouse: typing.ClassVar[QInputDevice.DeviceType]  # value = <DeviceType.Mouse: 1>
        Puck: typing.ClassVar[QInputDevice.DeviceType]  # value = <DeviceType.Puck: 8>
        Stylus: typing.ClassVar[QInputDevice.DeviceType]  # value = <DeviceType.Stylus: 16>
        TouchPad: typing.ClassVar[QInputDevice.DeviceType]  # value = <DeviceType.TouchPad: 4>
        TouchScreen: typing.ClassVar[QInputDevice.DeviceType]  # value = <DeviceType.TouchScreen: 2>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def availableVirtualGeometry(*args, **kwargs):
        ...
    @staticmethod
    def availableVirtualGeometryChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def capabilities(*args, **kwargs):
        ...
    @staticmethod
    def devices(*args, **kwargs):
        ...
    @staticmethod
    def hasCapability(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def primaryKeyboard(*args, **kwargs):
        ...
    @staticmethod
    def seatName(*args, **kwargs):
        ...
    @staticmethod
    def seatNames(*args, **kwargs):
        ...
    @staticmethod
    def systemId(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
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
class QInputEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def deviceType(*args, **kwargs):
        ...
    @staticmethod
    def modifiers(*args, **kwargs):
        ...
    @staticmethod
    def timestamp(*args, **kwargs):
        ...
class QInputMethod(PyQt6.QtCore.QObject):
    class Action(enum.Enum):
        Click: typing.ClassVar[QInputMethod.Action]  # value = <Action.Click: 0>
        ContextMenu: typing.ClassVar[QInputMethod.Action]  # value = <Action.ContextMenu: 1>
    @staticmethod
    def anchorRectangle(*args, **kwargs):
        ...
    @staticmethod
    def anchorRectangleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def animatingChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def commit(*args, **kwargs):
        ...
    @staticmethod
    def cursorRectangle(*args, **kwargs):
        ...
    @staticmethod
    def cursorRectangleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def hide(*args, **kwargs):
        ...
    @staticmethod
    def inputDirection(*args, **kwargs):
        ...
    @staticmethod
    def inputDirectionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def inputItemClipRectangle(*args, **kwargs):
        ...
    @staticmethod
    def inputItemClipRectangleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def inputItemRectangle(*args, **kwargs):
        ...
    @staticmethod
    def inputItemTransform(*args, **kwargs):
        ...
    @staticmethod
    def invokeAction(*args, **kwargs):
        ...
    @staticmethod
    def isAnimating(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def keyboardRectangle(*args, **kwargs):
        ...
    @staticmethod
    def keyboardRectangleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def locale(*args, **kwargs):
        ...
    @staticmethod
    def localeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def queryFocusObject(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def setInputItemRectangle(*args, **kwargs):
        ...
    @staticmethod
    def setInputItemTransform(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def show(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
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
class QInputMethodEvent(PyQt6.QtCore.QEvent):
    class Attribute(PyQt6.sip.simplewrapper):
        __hash__: typing.ClassVar[None] = None
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
    class AttributeType(enum.Enum):
        Cursor: typing.ClassVar[QInputMethodEvent.AttributeType]  # value = <AttributeType.Cursor: 1>
        Language: typing.ClassVar[QInputMethodEvent.AttributeType]  # value = <AttributeType.Language: 2>
        Ruby: typing.ClassVar[QInputMethodEvent.AttributeType]  # value = <AttributeType.Ruby: 3>
        Selection: typing.ClassVar[QInputMethodEvent.AttributeType]  # value = <AttributeType.Selection: 4>
        TextFormat: typing.ClassVar[QInputMethodEvent.AttributeType]  # value = <AttributeType.TextFormat: 0>
    @staticmethod
    def attributes(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def commitString(*args, **kwargs):
        ...
    @staticmethod
    def preeditString(*args, **kwargs):
        ...
    @staticmethod
    def replacementLength(*args, **kwargs):
        ...
    @staticmethod
    def replacementStart(*args, **kwargs):
        ...
    @staticmethod
    def setCommitString(*args, **kwargs):
        ...
class QInputMethodQueryEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def queries(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QIntValidator(QValidator):
    @staticmethod
    def bottom(*args, **kwargs):
        ...
    @staticmethod
    def fixup(*args, **kwargs):
        ...
    @staticmethod
    def setBottom(*args, **kwargs):
        ...
    @staticmethod
    def setRange(*args, **kwargs):
        ...
    @staticmethod
    def setTop(*args, **kwargs):
        ...
    @staticmethod
    def top(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
class QKeyEvent(QInputEvent):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def isAutoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def keyCombination(*args, **kwargs):
        ...
    @staticmethod
    def matches(*args, **kwargs):
        ...
    @staticmethod
    def modifiers(*args, **kwargs):
        ...
    @staticmethod
    def nativeModifiers(*args, **kwargs):
        ...
    @staticmethod
    def nativeScanCode(*args, **kwargs):
        ...
    @staticmethod
    def nativeVirtualKey(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
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
    def __len__(self):
        """
        Return len(self).
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QKeySequence(PyQt6.sip.simplewrapper):
    class SequenceFormat(enum.Enum):
        NativeText: typing.ClassVar[QKeySequence.SequenceFormat]  # value = <SequenceFormat.NativeText: 0>
        PortableText: typing.ClassVar[QKeySequence.SequenceFormat]  # value = <SequenceFormat.PortableText: 1>
    class SequenceMatch(enum.Enum):
        ExactMatch: typing.ClassVar[QKeySequence.SequenceMatch]  # value = <SequenceMatch.ExactMatch: 2>
        NoMatch: typing.ClassVar[QKeySequence.SequenceMatch]  # value = <SequenceMatch.NoMatch: 0>
        PartialMatch: typing.ClassVar[QKeySequence.SequenceMatch]  # value = <SequenceMatch.PartialMatch: 1>
    class StandardKey(enum.Enum):
        AddTab: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.AddTab: 19>
        Back: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Back: 13>
        Backspace: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Backspace: 69>
        Bold: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Bold: 27>
        Cancel: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Cancel: 70>
        Close: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Close: 4>
        Copy: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Copy: 9>
        Cut: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Cut: 8>
        Delete: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Delete: 7>
        DeleteCompleteLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.DeleteCompleteLine: 68>
        DeleteEndOfLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.DeleteEndOfLine: 60>
        DeleteEndOfWord: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.DeleteEndOfWord: 59>
        DeleteStartOfWord: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.DeleteStartOfWord: 58>
        Deselect: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Deselect: 67>
        Find: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Find: 22>
        FindNext: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.FindNext: 23>
        FindPrevious: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.FindPrevious: 24>
        Forward: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Forward: 14>
        FullScreen: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.FullScreen: 66>
        HelpContents: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.HelpContents: 1>
        InsertLineSeparator: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.InsertLineSeparator: 62>
        InsertParagraphSeparator: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.InsertParagraphSeparator: 61>
        Italic: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Italic: 28>
        MoveToEndOfBlock: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToEndOfBlock: 41>
        MoveToEndOfDocument: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToEndOfDocument: 43>
        MoveToEndOfLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToEndOfLine: 39>
        MoveToNextChar: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToNextChar: 30>
        MoveToNextLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToNextLine: 34>
        MoveToNextPage: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToNextPage: 36>
        MoveToNextWord: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToNextWord: 32>
        MoveToPreviousChar: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToPreviousChar: 31>
        MoveToPreviousLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToPreviousLine: 35>
        MoveToPreviousPage: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToPreviousPage: 37>
        MoveToPreviousWord: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToPreviousWord: 33>
        MoveToStartOfBlock: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToStartOfBlock: 40>
        MoveToStartOfDocument: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToStartOfDocument: 42>
        MoveToStartOfLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.MoveToStartOfLine: 38>
        New: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.New: 6>
        NextChild: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.NextChild: 20>
        Open: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Open: 3>
        Paste: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Paste: 10>
        Preferences: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Preferences: 64>
        PreviousChild: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.PreviousChild: 21>
        Print: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Print: 18>
        Quit: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Quit: 65>
        Redo: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Redo: 12>
        Refresh: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Refresh: 15>
        Replace: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Replace: 25>
        Save: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Save: 5>
        SaveAs: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SaveAs: 63>
        SelectAll: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectAll: 26>
        SelectEndOfBlock: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectEndOfBlock: 55>
        SelectEndOfDocument: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectEndOfDocument: 57>
        SelectEndOfLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectEndOfLine: 53>
        SelectNextChar: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectNextChar: 44>
        SelectNextLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectNextLine: 48>
        SelectNextPage: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectNextPage: 50>
        SelectNextWord: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectNextWord: 46>
        SelectPreviousChar: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectPreviousChar: 45>
        SelectPreviousLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectPreviousLine: 49>
        SelectPreviousPage: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectPreviousPage: 51>
        SelectPreviousWord: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectPreviousWord: 47>
        SelectStartOfBlock: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectStartOfBlock: 54>
        SelectStartOfDocument: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectStartOfDocument: 56>
        SelectStartOfLine: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.SelectStartOfLine: 52>
        Underline: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Underline: 29>
        Undo: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.Undo: 11>
        UnknownKey: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.UnknownKey: 0>
        WhatsThis: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.WhatsThis: 2>
        ZoomIn: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.ZoomIn: 16>
        ZoomOut: typing.ClassVar[QKeySequence.StandardKey]  # value = <StandardKey.ZoomOut: 17>
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def isDetached(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def keyBindings(*args, **kwargs):
        ...
    @staticmethod
    def listFromString(*args, **kwargs):
        ...
    @staticmethod
    def listToString(*args, **kwargs):
        ...
    @staticmethod
    def matches(*args, **kwargs):
        ...
    @staticmethod
    def mnemonic(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
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
    def __len__(self):
        """
        Return len(self).
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QLinearGradient(QGradient):
    @staticmethod
    def finalStop(*args, **kwargs):
        ...
    @staticmethod
    def setFinalStop(*args, **kwargs):
        ...
    @staticmethod
    def setStart(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
class QMatrix2x2(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix2x3(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix2x4(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix3x2(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix3x3(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix3x4(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix4x2(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix4x3(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QMatrix4x4(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def column(*args, **kwargs):
        ...
    @staticmethod
    def copyDataTo(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def determinant(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def frustum(*args, **kwargs):
        ...
    @staticmethod
    def inverted(*args, **kwargs):
        ...
    @staticmethod
    def isAffine(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def lookAt(*args, **kwargs):
        ...
    @staticmethod
    def map(*args, **kwargs):
        ...
    @staticmethod
    def mapRect(*args, **kwargs):
        ...
    @staticmethod
    def mapVector(*args, **kwargs):
        ...
    @staticmethod
    def normalMatrix(*args, **kwargs):
        ...
    @staticmethod
    def optimize(*args, **kwargs):
        ...
    @staticmethod
    def ortho(*args, **kwargs):
        ...
    @staticmethod
    def perspective(*args, **kwargs):
        ...
    @staticmethod
    def rotate(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def scale(*args, **kwargs):
        ...
    @staticmethod
    def setColumn(*args, **kwargs):
        ...
    @staticmethod
    def setRow(*args, **kwargs):
        ...
    @staticmethod
    def setToIdentity(*args, **kwargs):
        ...
    @staticmethod
    def toTransform(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    @staticmethod
    def viewport(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imatmul__(self, value):
        """
        Return self@=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __matmul__(self, value):
        """
        Return self@value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __neg__(self):
        """
        -self
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __rmatmul__(self, value):
        """
        Return value@self.
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __rtruediv__(self, value):
        """
        Return value/self.
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
    def __truediv__(self, value):
        """
        Return self/value.
        """
class QMouseEvent(QSinglePointEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
class QMoveEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def oldPos(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
class QMovie(PyQt6.QtCore.QObject):
    class CacheMode(enum.Enum):
        CacheAll: typing.ClassVar[QMovie.CacheMode]  # value = <CacheMode.CacheAll: 1>
        CacheNone: typing.ClassVar[QMovie.CacheMode]  # value = <CacheMode.CacheNone: 0>
    class MovieState(enum.Enum):
        NotRunning: typing.ClassVar[QMovie.MovieState]  # value = <MovieState.NotRunning: 0>
        Paused: typing.ClassVar[QMovie.MovieState]  # value = <MovieState.Paused: 1>
        Running: typing.ClassVar[QMovie.MovieState]  # value = <MovieState.Running: 2>
    @staticmethod
    def backgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def cacheMode(*args, **kwargs):
        ...
    @staticmethod
    def currentFrameNumber(*args, **kwargs):
        ...
    @staticmethod
    def currentImage(*args, **kwargs):
        ...
    @staticmethod
    def currentPixmap(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def fileName(*args, **kwargs):
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
    def format(*args, **kwargs):
        ...
    @staticmethod
    def frameChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def frameCount(*args, **kwargs):
        ...
    @staticmethod
    def frameRect(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def jumpToFrame(*args, **kwargs):
        ...
    @staticmethod
    def jumpToNextFrame(*args, **kwargs):
        ...
    @staticmethod
    def lastError(*args, **kwargs):
        ...
    @staticmethod
    def lastErrorString(*args, **kwargs):
        ...
    @staticmethod
    def loopCount(*args, **kwargs):
        ...
    @staticmethod
    def nextFrameDelay(*args, **kwargs):
        ...
    @staticmethod
    def resized(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def scaledSize(*args, **kwargs):
        ...
    @staticmethod
    def setBackgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def setCacheMode(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setPaused(*args, **kwargs):
        ...
    @staticmethod
    def setScaledSize(*args, **kwargs):
        ...
    @staticmethod
    def setSpeed(*args, **kwargs):
        ...
    @staticmethod
    def speed(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
    @staticmethod
    def started(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def supportedFormats(*args, **kwargs):
        ...
    @staticmethod
    def updated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QNativeGestureEvent(QSinglePointEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def delta(*args, **kwargs):
        ...
    @staticmethod
    def fingerCount(*args, **kwargs):
        ...
    @staticmethod
    def gestureType(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QOffscreenSurface(PyQt6.QtCore.QObject, QSurface):
    @staticmethod
    def create(*args, **kwargs):
        ...
    @staticmethod
    def destroy(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def requestedFormat(*args, **kwargs):
        ...
    @staticmethod
    def screen(*args, **kwargs):
        ...
    @staticmethod
    def screenChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setScreen(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def surfaceType(*args, **kwargs):
        ...
class QOpenGLContext(PyQt6.QtCore.QObject):
    class OpenGLModuleType(enum.Enum):
        LibGL: typing.ClassVar[QOpenGLContext.OpenGLModuleType]  # value = <OpenGLModuleType.LibGL: 0>
        LibGLES: typing.ClassVar[QOpenGLContext.OpenGLModuleType]  # value = <OpenGLModuleType.LibGLES: 1>
    @staticmethod
    def aboutToBeDestroyed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def areSharing(*args, **kwargs):
        ...
    @staticmethod
    def create(*args, **kwargs):
        ...
    @staticmethod
    def currentContext(*args, **kwargs):
        ...
    @staticmethod
    def defaultFramebufferObject(*args, **kwargs):
        ...
    @staticmethod
    def doneCurrent(*args, **kwargs):
        ...
    @staticmethod
    def extensions(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def getProcAddress(*args, **kwargs):
        ...
    @staticmethod
    def globalShareContext(*args, **kwargs):
        ...
    @staticmethod
    def hasExtension(*args, **kwargs):
        ...
    @staticmethod
    def isOpenGLES(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def makeCurrent(*args, **kwargs):
        ...
    @staticmethod
    def openGLModuleType(*args, **kwargs):
        ...
    @staticmethod
    def screen(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setScreen(*args, **kwargs):
        ...
    @staticmethod
    def setShareContext(*args, **kwargs):
        ...
    @staticmethod
    def shareContext(*args, **kwargs):
        ...
    @staticmethod
    def shareGroup(*args, **kwargs):
        ...
    @staticmethod
    def supportsThreadedOpenGL(*args, **kwargs):
        ...
    @staticmethod
    def surface(*args, **kwargs):
        ...
    @staticmethod
    def swapBuffers(*args, **kwargs):
        ...
class QOpenGLContextGroup(PyQt6.QtCore.QObject):
    @staticmethod
    def currentContextGroup(*args, **kwargs):
        ...
    @staticmethod
    def shares(*args, **kwargs):
        ...
class QPageLayout(PyQt6.sip.simplewrapper):
    class Mode(enum.Enum):
        FullPageMode: typing.ClassVar[QPageLayout.Mode]  # value = <Mode.FullPageMode: 1>
        StandardMode: typing.ClassVar[QPageLayout.Mode]  # value = <Mode.StandardMode: 0>
    class Orientation(enum.Enum):
        Landscape: typing.ClassVar[QPageLayout.Orientation]  # value = <Orientation.Landscape: 1>
        Portrait: typing.ClassVar[QPageLayout.Orientation]  # value = <Orientation.Portrait: 0>
    class Unit(enum.Enum):
        Cicero: typing.ClassVar[QPageLayout.Unit]  # value = <Unit.Cicero: 5>
        Didot: typing.ClassVar[QPageLayout.Unit]  # value = <Unit.Didot: 4>
        Inch: typing.ClassVar[QPageLayout.Unit]  # value = <Unit.Inch: 2>
        Millimeter: typing.ClassVar[QPageLayout.Unit]  # value = <Unit.Millimeter: 0>
        Pica: typing.ClassVar[QPageLayout.Unit]  # value = <Unit.Pica: 3>
        Point: typing.ClassVar[QPageLayout.Unit]  # value = <Unit.Point: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def fullRect(*args, **kwargs):
        ...
    @staticmethod
    def fullRectPixels(*args, **kwargs):
        ...
    @staticmethod
    def fullRectPoints(*args, **kwargs):
        ...
    @staticmethod
    def isEquivalentTo(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def margins(*args, **kwargs):
        ...
    @staticmethod
    def marginsPixels(*args, **kwargs):
        ...
    @staticmethod
    def marginsPoints(*args, **kwargs):
        ...
    @staticmethod
    def maximumMargins(*args, **kwargs):
        ...
    @staticmethod
    def minimumMargins(*args, **kwargs):
        ...
    @staticmethod
    def mode(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def pageSize(*args, **kwargs):
        ...
    @staticmethod
    def paintRect(*args, **kwargs):
        ...
    @staticmethod
    def paintRectPixels(*args, **kwargs):
        ...
    @staticmethod
    def paintRectPoints(*args, **kwargs):
        ...
    @staticmethod
    def setBottomMargin(*args, **kwargs):
        ...
    @staticmethod
    def setLeftMargin(*args, **kwargs):
        ...
    @staticmethod
    def setMargins(*args, **kwargs):
        ...
    @staticmethod
    def setMinimumMargins(*args, **kwargs):
        ...
    @staticmethod
    def setMode(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setPageSize(*args, **kwargs):
        ...
    @staticmethod
    def setRightMargin(*args, **kwargs):
        ...
    @staticmethod
    def setTopMargin(*args, **kwargs):
        ...
    @staticmethod
    def setUnits(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def units(*args, **kwargs):
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
class QPageRanges(PyQt6.sip.simplewrapper):
    class Range(PyQt6.sip.simplewrapper):
        __hash__: typing.ClassVar[None] = None
        @staticmethod
        def contains(*args, **kwargs):
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
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def addPage(*args, **kwargs):
        ...
    @staticmethod
    def addRange(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def firstPage(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def lastPage(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toRangeList(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
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
class QPageSize(PyQt6.sip.simplewrapper):
    class PageSizeId(enum.Enum):
        A0: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A0: 3>
        A1: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A1: 4>
        A10: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A10: 13>
        A2: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A2: 5>
        A3: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A3: 6>
        A3Extra: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A3Extra: 32>
        A4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A4: 7>
        A4Extra: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A4Extra: 33>
        A4Plus: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A4Plus: 34>
        A4Small: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A4Small: 35>
        A5: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A5: 8>
        A5Extra: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A5Extra: 36>
        A6: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A6: 9>
        A7: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A7: 10>
        A8: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A8: 11>
        A9: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.A9: 12>
        AnsiC: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.AnsiC: 49>
        AnsiD: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.AnsiD: 50>
        AnsiE: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.AnsiE: 51>
        ArchA: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.ArchA: 57>
        ArchB: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.ArchB: 58>
        ArchC: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.ArchC: 59>
        ArchD: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.ArchD: 60>
        ArchE: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.ArchE: 61>
        B0: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B0: 14>
        B1: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B1: 15>
        B10: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B10: 24>
        B2: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B2: 16>
        B3: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B3: 17>
        B4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B4: 18>
        B5: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B5: 19>
        B5Extra: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B5Extra: 37>
        B6: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B6: 20>
        B7: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B7: 21>
        B8: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B8: 22>
        B9: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.B9: 23>
        C5E: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.C5E: 25>
        Comm10E: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Comm10E: 26>
        Custom: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Custom: 31>
        DLE: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.DLE: 27>
        DoublePostcard: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.DoublePostcard: 78>
        Envelope11: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Envelope11: 97>
        Envelope12: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Envelope12: 98>
        Envelope14: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Envelope14: 99>
        Envelope9: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Envelope9: 96>
        EnvelopeB4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeB4: 85>
        EnvelopeB5: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeB5: 86>
        EnvelopeB6: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeB6: 87>
        EnvelopeC0: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC0: 88>
        EnvelopeC1: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC1: 89>
        EnvelopeC2: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC2: 90>
        EnvelopeC3: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC3: 91>
        EnvelopeC4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC4: 92>
        EnvelopeC6: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC6: 93>
        EnvelopeC65: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC65: 94>
        EnvelopeC7: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeC7: 95>
        EnvelopeChou3: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeChou3: 102>
        EnvelopeChou4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeChou4: 103>
        EnvelopeInvite: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeInvite: 104>
        EnvelopeItalian: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeItalian: 105>
        EnvelopeKaku2: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeKaku2: 106>
        EnvelopeKaku3: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeKaku3: 107>
        EnvelopeMonarch: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeMonarch: 100>
        EnvelopePersonal: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePersonal: 101>
        EnvelopePrc1: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc1: 108>
        EnvelopePrc10: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc10: 117>
        EnvelopePrc2: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc2: 109>
        EnvelopePrc3: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc3: 110>
        EnvelopePrc4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc4: 111>
        EnvelopePrc5: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc5: 112>
        EnvelopePrc6: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc6: 113>
        EnvelopePrc7: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc7: 114>
        EnvelopePrc8: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc8: 115>
        EnvelopePrc9: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopePrc9: 116>
        EnvelopeYou4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.EnvelopeYou4: 118>
        Executive: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Executive: 2>
        ExecutiveStandard: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.ExecutiveStandard: 71>
        FanFoldGerman: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.FanFoldGerman: 83>
        FanFoldGermanLegal: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.FanFoldGermanLegal: 84>
        FanFoldUS: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.FanFoldUS: 82>
        Folio: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Folio: 28>
        Imperial10x11: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial10x11: 66>
        Imperial10x13: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial10x13: 67>
        Imperial10x14: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial10x14: 68>
        Imperial12x11: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial12x11: 69>
        Imperial15x11: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial15x11: 70>
        Imperial7x9: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial7x9: 62>
        Imperial8x10: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial8x10: 63>
        Imperial9x11: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial9x11: 64>
        Imperial9x12: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Imperial9x12: 65>
        JisB0: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB0: 38>
        JisB1: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB1: 39>
        JisB10: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB10: 48>
        JisB2: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB2: 40>
        JisB3: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB3: 41>
        JisB4: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB4: 42>
        JisB5: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB5: 43>
        JisB6: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB6: 44>
        JisB7: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB7: 45>
        JisB8: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB8: 46>
        JisB9: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.JisB9: 47>
        Ledger: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Ledger: 29>
        Legal: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Legal: 1>
        LegalExtra: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.LegalExtra: 52>
        Letter: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Letter: 0>
        LetterExtra: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.LetterExtra: 53>
        LetterPlus: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.LetterPlus: 54>
        LetterSmall: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.LetterSmall: 55>
        Note: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Note: 72>
        Postcard: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Postcard: 77>
        Prc16K: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Prc16K: 79>
        Prc32K: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Prc32K: 80>
        Prc32KBig: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Prc32KBig: 81>
        Quarto: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Quarto: 73>
        Statement: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Statement: 74>
        SuperA: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.SuperA: 75>
        SuperB: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.SuperB: 76>
        Tabloid: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.Tabloid: 30>
        TabloidExtra: typing.ClassVar[QPageSize.PageSizeId]  # value = <PageSizeId.TabloidExtra: 56>
    class SizeMatchPolicy(enum.Enum):
        ExactMatch: typing.ClassVar[QPageSize.SizeMatchPolicy]  # value = <SizeMatchPolicy.ExactMatch: 2>
        FuzzyMatch: typing.ClassVar[QPageSize.SizeMatchPolicy]  # value = <SizeMatchPolicy.FuzzyMatch: 0>
        FuzzyOrientationMatch: typing.ClassVar[QPageSize.SizeMatchPolicy]  # value = <SizeMatchPolicy.FuzzyOrientationMatch: 1>
    class Unit(enum.Enum):
        Cicero: typing.ClassVar[QPageSize.Unit]  # value = <Unit.Cicero: 5>
        Didot: typing.ClassVar[QPageSize.Unit]  # value = <Unit.Didot: 4>
        Inch: typing.ClassVar[QPageSize.Unit]  # value = <Unit.Inch: 2>
        Millimeter: typing.ClassVar[QPageSize.Unit]  # value = <Unit.Millimeter: 0>
        Pica: typing.ClassVar[QPageSize.Unit]  # value = <Unit.Pica: 3>
        Point: typing.ClassVar[QPageSize.Unit]  # value = <Unit.Point: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def definitionSize(*args, **kwargs):
        ...
    @staticmethod
    def definitionUnits(*args, **kwargs):
        ...
    @staticmethod
    def id(*args, **kwargs):
        ...
    @staticmethod
    def isEquivalentTo(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def rectPixels(*args, **kwargs):
        ...
    @staticmethod
    def rectPoints(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def sizePixels(*args, **kwargs):
        ...
    @staticmethod
    def sizePoints(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def windowsId(*args, **kwargs):
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
class QPagedPaintDevice(QPaintDevice):
    class PdfVersion(enum.Enum):
        PdfVersion_1_4: typing.ClassVar[QPagedPaintDevice.PdfVersion]  # value = <PdfVersion.PdfVersion_1_4: 0>
        PdfVersion_1_6: typing.ClassVar[QPagedPaintDevice.PdfVersion]  # value = <PdfVersion.PdfVersion_1_6: 2>
        PdfVersion_A1b: typing.ClassVar[QPagedPaintDevice.PdfVersion]  # value = <PdfVersion.PdfVersion_A1b: 1>
    @staticmethod
    def newPage(*args, **kwargs):
        ...
    @staticmethod
    def pageLayout(*args, **kwargs):
        ...
    @staticmethod
    def pageRanges(*args, **kwargs):
        ...
    @staticmethod
    def setPageLayout(*args, **kwargs):
        ...
    @staticmethod
    def setPageMargins(*args, **kwargs):
        ...
    @staticmethod
    def setPageOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setPageRanges(*args, **kwargs):
        ...
    @staticmethod
    def setPageSize(*args, **kwargs):
        ...
class QPaintDevice(PyQt6.sip.simplewrapper):
    class PaintDeviceMetric(enum.Enum):
        PdmDepth: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmDepth: 6>
        PdmDevicePixelRatio: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmDevicePixelRatio: 11>
        PdmDevicePixelRatioScaled: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmDevicePixelRatioScaled: 12>
        PdmDpiX: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmDpiX: 7>
        PdmDpiY: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmDpiY: 8>
        PdmHeight: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmHeight: 2>
        PdmHeightMM: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmHeightMM: 4>
        PdmNumColors: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmNumColors: 5>
        PdmPhysicalDpiX: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmPhysicalDpiX: 9>
        PdmPhysicalDpiY: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmPhysicalDpiY: 10>
        PdmWidth: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmWidth: 1>
        PdmWidthMM: typing.ClassVar[QPaintDevice.PaintDeviceMetric]  # value = <PaintDeviceMetric.PdmWidthMM: 3>
    @staticmethod
    def colorCount(*args, **kwargs):
        ...
    @staticmethod
    def depth(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatioF(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatioFScale(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def heightMM(*args, **kwargs):
        ...
    @staticmethod
    def logicalDpiX(*args, **kwargs):
        ...
    @staticmethod
    def logicalDpiY(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def paintingActive(*args, **kwargs):
        ...
    @staticmethod
    def physicalDpiX(*args, **kwargs):
        ...
    @staticmethod
    def physicalDpiY(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
    @staticmethod
    def widthMM(*args, **kwargs):
        ...
class QPaintDeviceWindow(QWindow, QPaintDevice):
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def exposeEvent(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def update(*args, **kwargs):
        ...
class QPaintEngine(PyQt6.sip.simplewrapper):
    class DirtyFlag(enum.Flag):
        DirtyBackground: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyBackground: 16>
        DirtyBackgroundMode: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyBackgroundMode: 32>
        DirtyBrush: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyBrush: 2>
        DirtyBrushOrigin: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyBrushOrigin: 4>
        DirtyClipEnabled: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyClipEnabled: 2048>
        DirtyClipPath: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyClipPath: 256>
        DirtyClipRegion: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyClipRegion: 128>
        DirtyCompositionMode: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyCompositionMode: 1024>
        DirtyFont: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyFont: 8>
        DirtyHints: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyHints: 512>
        DirtyOpacity: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyOpacity: 4096>
        DirtyPen: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyPen: 1>
        DirtyTransform: typing.ClassVar[QPaintEngine.DirtyFlag]  # value = <DirtyFlag.DirtyTransform: 64>
    class PaintEngineFeature(enum.Flag):
        AlphaBlend: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.AlphaBlend: 128>
        Antialiasing: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.Antialiasing: 1024>
        BlendModes: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.BlendModes: 32768>
        BrushStroke: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.BrushStroke: 2048>
        ConicalGradientFill: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.ConicalGradientFill: 64>
        ConstantOpacity: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.ConstantOpacity: 4096>
        LinearGradientFill: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.LinearGradientFill: 16>
        MaskedBrush: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.MaskedBrush: 8192>
        ObjectBoundingModeGradients: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.ObjectBoundingModeGradients: 65536>
        PaintOutsidePaintEvent: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PaintOutsidePaintEvent: 536870912>
        PainterPaths: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PainterPaths: 512>
        PatternBrush: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PatternBrush: 8>
        PatternTransform: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PatternTransform: 2>
        PerspectiveTransform: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PerspectiveTransform: 16384>
        PixmapTransform: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PixmapTransform: 4>
        PorterDuff: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PorterDuff: 256>
        PrimitiveTransform: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.PrimitiveTransform: 1>
        RadialGradientFill: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.RadialGradientFill: 32>
        RasterOpModes: typing.ClassVar[QPaintEngine.PaintEngineFeature]  # value = <PaintEngineFeature.RasterOpModes: 131072>
    class PolygonDrawMode(enum.Enum):
        ConvexMode: typing.ClassVar[QPaintEngine.PolygonDrawMode]  # value = <PolygonDrawMode.ConvexMode: 2>
        OddEvenMode: typing.ClassVar[QPaintEngine.PolygonDrawMode]  # value = <PolygonDrawMode.OddEvenMode: 0>
        PolylineMode: typing.ClassVar[QPaintEngine.PolygonDrawMode]  # value = <PolygonDrawMode.PolylineMode: 3>
        WindingMode: typing.ClassVar[QPaintEngine.PolygonDrawMode]  # value = <PolygonDrawMode.WindingMode: 1>
    class Type(enum.Enum):
        Blitter: typing.ClassVar[QPaintEngine.Type]  # value = <Type.Blitter: 15>
        CoreGraphics: typing.ClassVar[QPaintEngine.Type]  # value = <Type.CoreGraphics: 3>
        Direct2D: typing.ClassVar[QPaintEngine.Type]  # value = <Type.Direct2D: 16>
        Direct3D: typing.ClassVar[QPaintEngine.Type]  # value = <Type.Direct3D: 10>
        MacPrinter: typing.ClassVar[QPaintEngine.Type]  # value = <Type.MacPrinter: 4>
        MaxUser: typing.ClassVar[QPaintEngine.Type]  # value = <Type.MaxUser: 100>
        OpenGL: typing.ClassVar[QPaintEngine.Type]  # value = <Type.OpenGL: 6>
        OpenGL2: typing.ClassVar[QPaintEngine.Type]  # value = <Type.OpenGL2: 13>
        OpenVG: typing.ClassVar[QPaintEngine.Type]  # value = <Type.OpenVG: 12>
        PaintBuffer: typing.ClassVar[QPaintEngine.Type]  # value = <Type.PaintBuffer: 14>
        Pdf: typing.ClassVar[QPaintEngine.Type]  # value = <Type.Pdf: 11>
        Picture: typing.ClassVar[QPaintEngine.Type]  # value = <Type.Picture: 7>
        QWindowSystem: typing.ClassVar[QPaintEngine.Type]  # value = <Type.QWindowSystem: 5>
        QuickDraw: typing.ClassVar[QPaintEngine.Type]  # value = <Type.QuickDraw: 2>
        Raster: typing.ClassVar[QPaintEngine.Type]  # value = <Type.Raster: 9>
        SVG: typing.ClassVar[QPaintEngine.Type]  # value = <Type.SVG: 8>
        User: typing.ClassVar[QPaintEngine.Type]  # value = <Type.User: 50>
        Windows: typing.ClassVar[QPaintEngine.Type]  # value = <Type.Windows: 1>
        X11: typing.ClassVar[QPaintEngine.Type]  # value = <Type.X11: 0>
    @staticmethod
    def begin(*args, **kwargs):
        ...
    @staticmethod
    def drawEllipse(*args, **kwargs):
        ...
    @staticmethod
    def drawImage(*args, **kwargs):
        ...
    @staticmethod
    def drawLines(*args, **kwargs):
        ...
    @staticmethod
    def drawPath(*args, **kwargs):
        ...
    @staticmethod
    def drawPixmap(*args, **kwargs):
        ...
    @staticmethod
    def drawPoints(*args, **kwargs):
        ...
    @staticmethod
    def drawPolygon(*args, **kwargs):
        ...
    @staticmethod
    def drawRects(*args, **kwargs):
        ...
    @staticmethod
    def drawTextItem(*args, **kwargs):
        ...
    @staticmethod
    def drawTiledPixmap(*args, **kwargs):
        ...
    @staticmethod
    def end(*args, **kwargs):
        ...
    @staticmethod
    def hasFeature(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def paintDevice(*args, **kwargs):
        ...
    @staticmethod
    def painter(*args, **kwargs):
        ...
    @staticmethod
    def setActive(*args, **kwargs):
        ...
    @staticmethod
    def setPaintDevice(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def updateState(*args, **kwargs):
        ...
class QPaintEngineState(PyQt6.sip.simplewrapper):
    @staticmethod
    def backgroundBrush(*args, **kwargs):
        ...
    @staticmethod
    def backgroundMode(*args, **kwargs):
        ...
    @staticmethod
    def brush(*args, **kwargs):
        ...
    @staticmethod
    def brushNeedsResolving(*args, **kwargs):
        ...
    @staticmethod
    def brushOrigin(*args, **kwargs):
        ...
    @staticmethod
    def clipOperation(*args, **kwargs):
        ...
    @staticmethod
    def clipPath(*args, **kwargs):
        ...
    @staticmethod
    def clipRegion(*args, **kwargs):
        ...
    @staticmethod
    def compositionMode(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def isClipEnabled(*args, **kwargs):
        ...
    @staticmethod
    def opacity(*args, **kwargs):
        ...
    @staticmethod
    def painter(*args, **kwargs):
        ...
    @staticmethod
    def pen(*args, **kwargs):
        ...
    @staticmethod
    def penNeedsResolving(*args, **kwargs):
        ...
    @staticmethod
    def renderHints(*args, **kwargs):
        ...
    @staticmethod
    def state(*args, **kwargs):
        ...
    @staticmethod
    def transform(*args, **kwargs):
        ...
class QPaintEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def region(*args, **kwargs):
        ...
class QPainter(PyQt6.sip.simplewrapper):
    class CompositionMode(enum.Enum):
        CompositionMode_Clear: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Clear: 2>
        CompositionMode_ColorBurn: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_ColorBurn: 19>
        CompositionMode_ColorDodge: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_ColorDodge: 18>
        CompositionMode_Darken: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Darken: 16>
        CompositionMode_Destination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Destination: 4>
        CompositionMode_DestinationAtop: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_DestinationAtop: 10>
        CompositionMode_DestinationIn: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_DestinationIn: 6>
        CompositionMode_DestinationOut: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_DestinationOut: 8>
        CompositionMode_DestinationOver: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_DestinationOver: 1>
        CompositionMode_Difference: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Difference: 22>
        CompositionMode_Exclusion: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Exclusion: 23>
        CompositionMode_HardLight: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_HardLight: 20>
        CompositionMode_Lighten: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Lighten: 17>
        CompositionMode_Multiply: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Multiply: 13>
        CompositionMode_Overlay: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Overlay: 15>
        CompositionMode_Plus: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Plus: 12>
        CompositionMode_Screen: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Screen: 14>
        CompositionMode_SoftLight: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_SoftLight: 21>
        CompositionMode_Source: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Source: 3>
        CompositionMode_SourceAtop: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_SourceAtop: 9>
        CompositionMode_SourceIn: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_SourceIn: 5>
        CompositionMode_SourceOut: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_SourceOut: 7>
        CompositionMode_SourceOver: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_SourceOver: 0>
        CompositionMode_Xor: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.CompositionMode_Xor: 11>
        RasterOp_ClearDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_ClearDestination: 35>
        RasterOp_NotDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_NotDestination: 37>
        RasterOp_NotSource: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_NotSource: 30>
        RasterOp_NotSourceAndDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_NotSourceAndDestination: 31>
        RasterOp_NotSourceAndNotDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_NotSourceAndNotDestination: 27>
        RasterOp_NotSourceOrDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_NotSourceOrDestination: 33>
        RasterOp_NotSourceOrNotDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_NotSourceOrNotDestination: 28>
        RasterOp_NotSourceXorDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_NotSourceXorDestination: 29>
        RasterOp_SetDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_SetDestination: 36>
        RasterOp_SourceAndDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_SourceAndDestination: 25>
        RasterOp_SourceAndNotDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_SourceAndNotDestination: 32>
        RasterOp_SourceOrDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_SourceOrDestination: 24>
        RasterOp_SourceOrNotDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_SourceOrNotDestination: 34>
        RasterOp_SourceXorDestination: typing.ClassVar[QPainter.CompositionMode]  # value = <CompositionMode.RasterOp_SourceXorDestination: 26>
    class PixmapFragment(PyQt6.sip.simplewrapper):
        @staticmethod
        def create(*args, **kwargs):
            ...
    class PixmapFragmentHint(enum.Flag):
        OpaqueHint: typing.ClassVar[QPainter.PixmapFragmentHint]  # value = <PixmapFragmentHint.OpaqueHint: 1>
    class RenderHint(enum.Flag):
        Antialiasing: typing.ClassVar[QPainter.RenderHint]  # value = <RenderHint.Antialiasing: 1>
        LosslessImageRendering: typing.ClassVar[QPainter.RenderHint]  # value = <RenderHint.LosslessImageRendering: 64>
        NonCosmeticBrushPatterns: typing.ClassVar[QPainter.RenderHint]  # value = <RenderHint.NonCosmeticBrushPatterns: 128>
        SmoothPixmapTransform: typing.ClassVar[QPainter.RenderHint]  # value = <RenderHint.SmoothPixmapTransform: 4>
        TextAntialiasing: typing.ClassVar[QPainter.RenderHint]  # value = <RenderHint.TextAntialiasing: 2>
        VerticalSubpixelPositioning: typing.ClassVar[QPainter.RenderHint]  # value = <RenderHint.VerticalSubpixelPositioning: 8>
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def background(*args, **kwargs):
        ...
    @staticmethod
    def backgroundMode(*args, **kwargs):
        ...
    @staticmethod
    def begin(*args, **kwargs):
        ...
    @staticmethod
    def beginNativePainting(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def brush(*args, **kwargs):
        ...
    @staticmethod
    def brushOrigin(*args, **kwargs):
        ...
    @staticmethod
    def clipBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def clipPath(*args, **kwargs):
        ...
    @staticmethod
    def clipRegion(*args, **kwargs):
        ...
    @staticmethod
    def combinedTransform(*args, **kwargs):
        ...
    @staticmethod
    def compositionMode(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def deviceTransform(*args, **kwargs):
        ...
    @staticmethod
    def drawArc(*args, **kwargs):
        ...
    @staticmethod
    def drawChord(*args, **kwargs):
        ...
    @staticmethod
    def drawConvexPolygon(*args, **kwargs):
        ...
    @staticmethod
    def drawEllipse(*args, **kwargs):
        ...
    @staticmethod
    def drawGlyphRun(*args, **kwargs):
        ...
    @staticmethod
    def drawImage(*args, **kwargs):
        ...
    @staticmethod
    def drawLine(*args, **kwargs):
        ...
    @staticmethod
    def drawLines(*args, **kwargs):
        ...
    @staticmethod
    def drawPath(*args, **kwargs):
        ...
    @staticmethod
    def drawPicture(*args, **kwargs):
        ...
    @staticmethod
    def drawPie(*args, **kwargs):
        ...
    @staticmethod
    def drawPixmap(*args, **kwargs):
        ...
    @staticmethod
    def drawPixmapFragments(*args, **kwargs):
        ...
    @staticmethod
    def drawPoint(*args, **kwargs):
        ...
    @staticmethod
    def drawPoints(*args, **kwargs):
        ...
    @staticmethod
    def drawPolygon(*args, **kwargs):
        ...
    @staticmethod
    def drawPolyline(*args, **kwargs):
        ...
    @staticmethod
    def drawRect(*args, **kwargs):
        ...
    @staticmethod
    def drawRects(*args, **kwargs):
        ...
    @staticmethod
    def drawRoundedRect(*args, **kwargs):
        ...
    @staticmethod
    def drawStaticText(*args, **kwargs):
        ...
    @staticmethod
    def drawText(*args, **kwargs):
        ...
    @staticmethod
    def drawTiledPixmap(*args, **kwargs):
        ...
    @staticmethod
    def end(*args, **kwargs):
        ...
    @staticmethod
    def endNativePainting(*args, **kwargs):
        ...
    @staticmethod
    def eraseRect(*args, **kwargs):
        ...
    @staticmethod
    def fillPath(*args, **kwargs):
        ...
    @staticmethod
    def fillRect(*args, **kwargs):
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
    def hasClipping(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def layoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def opacity(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def pen(*args, **kwargs):
        ...
    @staticmethod
    def renderHints(*args, **kwargs):
        ...
    @staticmethod
    def resetTransform(*args, **kwargs):
        ...
    @staticmethod
    def restore(*args, **kwargs):
        ...
    @staticmethod
    def rotate(*args, **kwargs):
        ...
    @staticmethod
    def save(*args, **kwargs):
        ...
    @staticmethod
    def scale(*args, **kwargs):
        ...
    @staticmethod
    def setBackground(*args, **kwargs):
        ...
    @staticmethod
    def setBackgroundMode(*args, **kwargs):
        ...
    @staticmethod
    def setBrush(*args, **kwargs):
        ...
    @staticmethod
    def setBrushOrigin(*args, **kwargs):
        ...
    @staticmethod
    def setClipPath(*args, **kwargs):
        ...
    @staticmethod
    def setClipRect(*args, **kwargs):
        ...
    @staticmethod
    def setClipRegion(*args, **kwargs):
        ...
    @staticmethod
    def setClipping(*args, **kwargs):
        ...
    @staticmethod
    def setCompositionMode(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setLayoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def setOpacity(*args, **kwargs):
        ...
    @staticmethod
    def setPen(*args, **kwargs):
        ...
    @staticmethod
    def setRenderHint(*args, **kwargs):
        ...
    @staticmethod
    def setRenderHints(*args, **kwargs):
        ...
    @staticmethod
    def setTransform(*args, **kwargs):
        ...
    @staticmethod
    def setViewTransformEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setViewport(*args, **kwargs):
        ...
    @staticmethod
    def setWindow(*args, **kwargs):
        ...
    @staticmethod
    def setWorldMatrixEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setWorldTransform(*args, **kwargs):
        ...
    @staticmethod
    def shear(*args, **kwargs):
        ...
    @staticmethod
    def strokePath(*args, **kwargs):
        ...
    @staticmethod
    def testRenderHint(*args, **kwargs):
        ...
    @staticmethod
    def transform(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def viewTransformEnabled(*args, **kwargs):
        ...
    @staticmethod
    def viewport(*args, **kwargs):
        ...
    @staticmethod
    def window(*args, **kwargs):
        ...
    @staticmethod
    def worldMatrixEnabled(*args, **kwargs):
        ...
    @staticmethod
    def worldTransform(*args, **kwargs):
        ...
class QPainterPath(PyQt6.sip.simplewrapper):
    class Element(PyQt6.sip.simplewrapper):
        __hash__: typing.ClassVar[None] = None
        @staticmethod
        def isCurveTo(*args, **kwargs):
            ...
        @staticmethod
        def isLineTo(*args, **kwargs):
            ...
        @staticmethod
        def isMoveTo(*args, **kwargs):
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
    class ElementType(enum.Enum):
        CurveToDataElement: typing.ClassVar[QPainterPath.ElementType]  # value = <ElementType.CurveToDataElement: 3>
        CurveToElement: typing.ClassVar[QPainterPath.ElementType]  # value = <ElementType.CurveToElement: 2>
        LineToElement: typing.ClassVar[QPainterPath.ElementType]  # value = <ElementType.LineToElement: 1>
        MoveToElement: typing.ClassVar[QPainterPath.ElementType]  # value = <ElementType.MoveToElement: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def addEllipse(*args, **kwargs):
        ...
    @staticmethod
    def addPath(*args, **kwargs):
        ...
    @staticmethod
    def addPolygon(*args, **kwargs):
        ...
    @staticmethod
    def addRect(*args, **kwargs):
        ...
    @staticmethod
    def addRegion(*args, **kwargs):
        ...
    @staticmethod
    def addRoundedRect(*args, **kwargs):
        ...
    @staticmethod
    def addText(*args, **kwargs):
        ...
    @staticmethod
    def angleAtPercent(*args, **kwargs):
        ...
    @staticmethod
    def arcMoveTo(*args, **kwargs):
        ...
    @staticmethod
    def arcTo(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def capacity(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def closeSubpath(*args, **kwargs):
        ...
    @staticmethod
    def connectPath(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def controlPointRect(*args, **kwargs):
        ...
    @staticmethod
    def cubicTo(*args, **kwargs):
        ...
    @staticmethod
    def currentPosition(*args, **kwargs):
        ...
    @staticmethod
    def elementAt(*args, **kwargs):
        ...
    @staticmethod
    def elementCount(*args, **kwargs):
        ...
    @staticmethod
    def fillRule(*args, **kwargs):
        ...
    @staticmethod
    def intersected(*args, **kwargs):
        ...
    @staticmethod
    def intersects(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def lineTo(*args, **kwargs):
        ...
    @staticmethod
    def moveTo(*args, **kwargs):
        ...
    @staticmethod
    def percentAtLength(*args, **kwargs):
        ...
    @staticmethod
    def pointAtPercent(*args, **kwargs):
        ...
    @staticmethod
    def quadTo(*args, **kwargs):
        ...
    @staticmethod
    def reserve(*args, **kwargs):
        ...
    @staticmethod
    def setElementPositionAt(*args, **kwargs):
        ...
    @staticmethod
    def setFillRule(*args, **kwargs):
        ...
    @staticmethod
    def simplified(*args, **kwargs):
        ...
    @staticmethod
    def slopeAtPercent(*args, **kwargs):
        ...
    @staticmethod
    def subtracted(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toFillPolygon(*args, **kwargs):
        ...
    @staticmethod
    def toFillPolygons(*args, **kwargs):
        ...
    @staticmethod
    def toReversed(*args, **kwargs):
        ...
    @staticmethod
    def toSubpathPolygons(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def united(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __and__(self, value):
        """
        Return self&value.
        """
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
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __iand__(self, value):
        """
        Return self&=value.
        """
    def __ior__(self, value):
        """
        Return self|=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
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
    def __or__(self, value):
        """
        Return self|value.
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __rand__(self, value):
        """
        Return value&self.
        """
    def __ror__(self, value):
        """
        Return value|self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
class QPainterPathStroker(PyQt6.sip.simplewrapper):
    @staticmethod
    def capStyle(*args, **kwargs):
        ...
    @staticmethod
    def createStroke(*args, **kwargs):
        ...
    @staticmethod
    def curveThreshold(*args, **kwargs):
        ...
    @staticmethod
    def dashOffset(*args, **kwargs):
        ...
    @staticmethod
    def dashPattern(*args, **kwargs):
        ...
    @staticmethod
    def joinStyle(*args, **kwargs):
        ...
    @staticmethod
    def miterLimit(*args, **kwargs):
        ...
    @staticmethod
    def setCapStyle(*args, **kwargs):
        ...
    @staticmethod
    def setCurveThreshold(*args, **kwargs):
        ...
    @staticmethod
    def setDashOffset(*args, **kwargs):
        ...
    @staticmethod
    def setDashPattern(*args, **kwargs):
        ...
    @staticmethod
    def setJoinStyle(*args, **kwargs):
        ...
    @staticmethod
    def setMiterLimit(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
class QPalette(PyQt6.sip.simplewrapper):
    class ColorGroup(enum.Enum):
        Active: typing.ClassVar[QPalette.ColorGroup]  # value = <ColorGroup.Active: 0>
        All: typing.ClassVar[QPalette.ColorGroup]  # value = <ColorGroup.All: 5>
        Current: typing.ClassVar[QPalette.ColorGroup]  # value = <ColorGroup.Current: 4>
        Disabled: typing.ClassVar[QPalette.ColorGroup]  # value = <ColorGroup.Disabled: 1>
        Inactive: typing.ClassVar[QPalette.ColorGroup]  # value = <ColorGroup.Inactive: 2>
        NColorGroups: typing.ClassVar[QPalette.ColorGroup]  # value = <ColorGroup.NColorGroups: 3>
    class ColorRole(enum.Enum):
        Accent: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Accent: 21>
        AlternateBase: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.AlternateBase: 16>
        Base: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Base: 9>
        BrightText: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.BrightText: 7>
        Button: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Button: 1>
        ButtonText: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.ButtonText: 8>
        Dark: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Dark: 4>
        Highlight: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Highlight: 12>
        HighlightedText: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.HighlightedText: 13>
        Light: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Light: 2>
        Link: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Link: 14>
        LinkVisited: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.LinkVisited: 15>
        Mid: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Mid: 5>
        Midlight: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Midlight: 3>
        NColorRoles: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.NColorRoles: 22>
        NoRole: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.NoRole: 17>
        PlaceholderText: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.PlaceholderText: 20>
        Shadow: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Shadow: 11>
        Text: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Text: 6>
        ToolTipBase: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.ToolTipBase: 18>
        ToolTipText: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.ToolTipText: 19>
        Window: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.Window: 10>
        WindowText: typing.ClassVar[QPalette.ColorRole]  # value = <ColorRole.WindowText: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def accent(*args, **kwargs):
        ...
    @staticmethod
    def alternateBase(*args, **kwargs):
        ...
    @staticmethod
    def base(*args, **kwargs):
        ...
    @staticmethod
    def brightText(*args, **kwargs):
        ...
    @staticmethod
    def brush(*args, **kwargs):
        ...
    @staticmethod
    def button(*args, **kwargs):
        ...
    @staticmethod
    def buttonText(*args, **kwargs):
        ...
    @staticmethod
    def cacheKey(*args, **kwargs):
        ...
    @staticmethod
    def color(*args, **kwargs):
        ...
    @staticmethod
    def currentColorGroup(*args, **kwargs):
        ...
    @staticmethod
    def dark(*args, **kwargs):
        ...
    @staticmethod
    def highlight(*args, **kwargs):
        ...
    @staticmethod
    def highlightedText(*args, **kwargs):
        ...
    @staticmethod
    def isBrushSet(*args, **kwargs):
        ...
    @staticmethod
    def isCopyOf(*args, **kwargs):
        ...
    @staticmethod
    def isEqual(*args, **kwargs):
        ...
    @staticmethod
    def light(*args, **kwargs):
        ...
    @staticmethod
    def link(*args, **kwargs):
        ...
    @staticmethod
    def linkVisited(*args, **kwargs):
        ...
    @staticmethod
    def mid(*args, **kwargs):
        ...
    @staticmethod
    def midlight(*args, **kwargs):
        ...
    @staticmethod
    def placeholderText(*args, **kwargs):
        ...
    @staticmethod
    def resolve(*args, **kwargs):
        ...
    @staticmethod
    def setBrush(*args, **kwargs):
        ...
    @staticmethod
    def setColor(*args, **kwargs):
        ...
    @staticmethod
    def setColorGroup(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentColorGroup(*args, **kwargs):
        ...
    @staticmethod
    def shadow(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def toolTipBase(*args, **kwargs):
        ...
    @staticmethod
    def toolTipText(*args, **kwargs):
        ...
    @staticmethod
    def window(*args, **kwargs):
        ...
    @staticmethod
    def windowText(*args, **kwargs):
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
class QPdfWriter(PyQt6.QtCore.QObject, QPagedPaintDevice):
    @staticmethod
    def addFileAttachment(*args, **kwargs):
        ...
    @staticmethod
    def creator(*args, **kwargs):
        ...
    @staticmethod
    def documentXmpMetadata(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def newPage(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def pdfVersion(*args, **kwargs):
        ...
    @staticmethod
    def resolution(*args, **kwargs):
        ...
    @staticmethod
    def setCreator(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentXmpMetadata(*args, **kwargs):
        ...
    @staticmethod
    def setPdfVersion(*args, **kwargs):
        ...
    @staticmethod
    def setResolution(*args, **kwargs):
        ...
    @staticmethod
    def setTitle(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
class QPen(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def brush(*args, **kwargs):
        ...
    @staticmethod
    def capStyle(*args, **kwargs):
        ...
    @staticmethod
    def color(*args, **kwargs):
        ...
    @staticmethod
    def dashOffset(*args, **kwargs):
        ...
    @staticmethod
    def dashPattern(*args, **kwargs):
        ...
    @staticmethod
    def isCosmetic(*args, **kwargs):
        ...
    @staticmethod
    def isSolid(*args, **kwargs):
        ...
    @staticmethod
    def joinStyle(*args, **kwargs):
        ...
    @staticmethod
    def miterLimit(*args, **kwargs):
        ...
    @staticmethod
    def setBrush(*args, **kwargs):
        ...
    @staticmethod
    def setCapStyle(*args, **kwargs):
        ...
    @staticmethod
    def setColor(*args, **kwargs):
        ...
    @staticmethod
    def setCosmetic(*args, **kwargs):
        ...
    @staticmethod
    def setDashOffset(*args, **kwargs):
        ...
    @staticmethod
    def setDashPattern(*args, **kwargs):
        ...
    @staticmethod
    def setJoinStyle(*args, **kwargs):
        ...
    @staticmethod
    def setMiterLimit(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def setWidthF(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
    @staticmethod
    def widthF(*args, **kwargs):
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
class QPicture(QPaintDevice):
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def detach(*args, **kwargs):
        ...
    @staticmethod
    def devType(*args, **kwargs):
        ...
    @staticmethod
    def isDetached(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def play(*args, **kwargs):
        ...
    @staticmethod
    def save(*args, **kwargs):
        ...
    @staticmethod
    def setBoundingRect(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QPixelFormat(PyQt6.sip.simplewrapper):
    class AlphaPosition(enum.Enum):
        AtBeginning: typing.ClassVar[QPixelFormat.AlphaPosition]  # value = <AlphaPosition.AtBeginning: 0>
        AtEnd: typing.ClassVar[QPixelFormat.AlphaPosition]  # value = <AlphaPosition.AtEnd: 1>
    class AlphaPremultiplied(enum.Enum):
        NotPremultiplied: typing.ClassVar[QPixelFormat.AlphaPremultiplied]  # value = <AlphaPremultiplied.NotPremultiplied: 0>
        Premultiplied: typing.ClassVar[QPixelFormat.AlphaPremultiplied]  # value = <AlphaPremultiplied.Premultiplied: 1>
    class AlphaUsage(enum.Enum):
        IgnoresAlpha: typing.ClassVar[QPixelFormat.AlphaUsage]  # value = <AlphaUsage.IgnoresAlpha: 1>
        UsesAlpha: typing.ClassVar[QPixelFormat.AlphaUsage]  # value = <AlphaUsage.UsesAlpha: 0>
    class ByteOrder(enum.Enum):
        BigEndian: typing.ClassVar[QPixelFormat.ByteOrder]  # value = <ByteOrder.BigEndian: 1>
        CurrentSystemEndian: typing.ClassVar[QPixelFormat.ByteOrder]  # value = <ByteOrder.CurrentSystemEndian: 2>
        LittleEndian: typing.ClassVar[QPixelFormat.ByteOrder]  # value = <ByteOrder.LittleEndian: 0>
    class ColorModel(enum.Enum):
        Alpha: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.Alpha: 8>
        BGR: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.BGR: 1>
        CMYK: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.CMYK: 4>
        Grayscale: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.Grayscale: 3>
        HSL: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.HSL: 5>
        HSV: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.HSV: 6>
        Indexed: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.Indexed: 2>
        RGB: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.RGB: 0>
        YUV: typing.ClassVar[QPixelFormat.ColorModel]  # value = <ColorModel.YUV: 7>
    class TypeInterpretation(enum.Enum):
        FloatingPoint: typing.ClassVar[QPixelFormat.TypeInterpretation]  # value = <TypeInterpretation.FloatingPoint: 3>
        UnsignedByte: typing.ClassVar[QPixelFormat.TypeInterpretation]  # value = <TypeInterpretation.UnsignedByte: 2>
        UnsignedInteger: typing.ClassVar[QPixelFormat.TypeInterpretation]  # value = <TypeInterpretation.UnsignedInteger: 0>
        UnsignedShort: typing.ClassVar[QPixelFormat.TypeInterpretation]  # value = <TypeInterpretation.UnsignedShort: 1>
    class YUVLayout(enum.Enum):
        IMC1: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.IMC1: 10>
        IMC2: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.IMC2: 11>
        IMC3: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.IMC3: 12>
        IMC4: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.IMC4: 13>
        NV12: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.NV12: 8>
        NV21: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.NV21: 9>
        UYVY: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.UYVY: 6>
        Y16: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.Y16: 15>
        Y8: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.Y8: 14>
        YUV411: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.YUV411: 2>
        YUV420P: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.YUV420P: 3>
        YUV420SP: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.YUV420SP: 4>
        YUV422: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.YUV422: 1>
        YUV444: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.YUV444: 0>
        YUYV: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.YUYV: 7>
        YV12: typing.ClassVar[QPixelFormat.YUVLayout]  # value = <YUVLayout.YV12: 5>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def alphaPosition(*args, **kwargs):
        ...
    @staticmethod
    def alphaSize(*args, **kwargs):
        ...
    @staticmethod
    def alphaUsage(*args, **kwargs):
        ...
    @staticmethod
    def bitsPerPixel(*args, **kwargs):
        ...
    @staticmethod
    def blackSize(*args, **kwargs):
        ...
    @staticmethod
    def blueSize(*args, **kwargs):
        ...
    @staticmethod
    def brightnessSize(*args, **kwargs):
        ...
    @staticmethod
    def byteOrder(*args, **kwargs):
        ...
    @staticmethod
    def channelCount(*args, **kwargs):
        ...
    @staticmethod
    def colorModel(*args, **kwargs):
        ...
    @staticmethod
    def cyanSize(*args, **kwargs):
        ...
    @staticmethod
    def greenSize(*args, **kwargs):
        ...
    @staticmethod
    def hueSize(*args, **kwargs):
        ...
    @staticmethod
    def lightnessSize(*args, **kwargs):
        ...
    @staticmethod
    def magentaSize(*args, **kwargs):
        ...
    @staticmethod
    def premultiplied(*args, **kwargs):
        ...
    @staticmethod
    def redSize(*args, **kwargs):
        ...
    @staticmethod
    def saturationSize(*args, **kwargs):
        ...
    @staticmethod
    def subEnum(*args, **kwargs):
        ...
    @staticmethod
    def typeInterpretation(*args, **kwargs):
        ...
    @staticmethod
    def yellowSize(*args, **kwargs):
        ...
    @staticmethod
    def yuvLayout(*args, **kwargs):
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
class QPixmap(QPaintDevice):
    @staticmethod
    def cacheKey(*args, **kwargs):
        ...
    @staticmethod
    def convertFromImage(*args, **kwargs):
        ...
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def createHeuristicMask(*args, **kwargs):
        ...
    @staticmethod
    def createMaskFromColor(*args, **kwargs):
        ...
    @staticmethod
    def defaultDepth(*args, **kwargs):
        ...
    @staticmethod
    def depth(*args, **kwargs):
        ...
    @staticmethod
    def detach(*args, **kwargs):
        ...
    @staticmethod
    def devType(*args, **kwargs):
        ...
    @staticmethod
    def deviceIndependentSize(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def fromImage(*args, **kwargs):
        ...
    @staticmethod
    def fromImageReader(*args, **kwargs):
        ...
    @staticmethod
    def hasAlpha(*args, **kwargs):
        ...
    @staticmethod
    def hasAlphaChannel(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isQBitmap(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def loadFromData(*args, **kwargs):
        ...
    @staticmethod
    def mask(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def save(*args, **kwargs):
        ...
    @staticmethod
    def scaled(*args, **kwargs):
        ...
    @staticmethod
    def scaledToHeight(*args, **kwargs):
        ...
    @staticmethod
    def scaledToWidth(*args, **kwargs):
        ...
    @staticmethod
    def scroll(*args, **kwargs):
        ...
    @staticmethod
    def setDevicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def setMask(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toImage(*args, **kwargs):
        ...
    @staticmethod
    def transformed(*args, **kwargs):
        ...
    @staticmethod
    def trueMatrix(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
class QPixmapCache(PyQt6.sip.simplewrapper):
    class Key(PyQt6.sip.simplewrapper):
        @staticmethod
        def isValid(*args, **kwargs):
            ...
        @staticmethod
        def swap(*args, **kwargs):
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
    @staticmethod
    def cacheLimit(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def find(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @staticmethod
    def setCacheLimit(*args, **kwargs):
        ...
class QPlatformSurfaceEvent(PyQt6.QtCore.QEvent):
    class SurfaceEventType(enum.Enum):
        SurfaceAboutToBeDestroyed: typing.ClassVar[QPlatformSurfaceEvent.SurfaceEventType]  # value = <SurfaceEventType.SurfaceAboutToBeDestroyed: 1>
        SurfaceCreated: typing.ClassVar[QPlatformSurfaceEvent.SurfaceEventType]  # value = <SurfaceEventType.SurfaceCreated: 0>
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def surfaceEventType(*args, **kwargs):
        ...
class QPointerEvent(QInputEvent):
    @staticmethod
    def allPointsAccepted(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def isBeginEvent(*args, **kwargs):
        ...
    @staticmethod
    def isEndEvent(*args, **kwargs):
        ...
    @staticmethod
    def isUpdateEvent(*args, **kwargs):
        ...
    @staticmethod
    def point(*args, **kwargs):
        ...
    @staticmethod
    def pointById(*args, **kwargs):
        ...
    @staticmethod
    def pointCount(*args, **kwargs):
        ...
    @staticmethod
    def pointerType(*args, **kwargs):
        ...
    @staticmethod
    def pointingDevice(*args, **kwargs):
        ...
    @staticmethod
    def points(*args, **kwargs):
        ...
    @staticmethod
    def setAccepted(*args, **kwargs):
        ...
class QPointingDevice(QInputDevice):
    class PointerType(enum.Flag):
        Cursor: typing.ClassVar[QPointingDevice.PointerType]  # value = <PointerType.Cursor: 16>
        Eraser: typing.ClassVar[QPointingDevice.PointerType]  # value = <PointerType.Eraser: 8>
        Finger: typing.ClassVar[QPointingDevice.PointerType]  # value = <PointerType.Finger: 2>
        Generic: typing.ClassVar[QPointingDevice.PointerType]  # value = <PointerType.Generic: 1>
        Pen: typing.ClassVar[QPointingDevice.PointerType]  # value = <PointerType.Pen: 4>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def buttonCount(*args, **kwargs):
        ...
    @staticmethod
    def maximumPoints(*args, **kwargs):
        ...
    @staticmethod
    def pointerType(*args, **kwargs):
        ...
    @staticmethod
    def primaryPointingDevice(*args, **kwargs):
        ...
    @staticmethod
    def uniqueId(*args, **kwargs):
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
class QPointingDeviceUniqueId(PyQt6.sip.simplewrapper):
    @staticmethod
    def fromNumericId(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def numericId(*args, **kwargs):
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
class QPolygon(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def at(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def containsPoint(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def first(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def intersected(*args, **kwargs):
        ...
    @staticmethod
    def intersects(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def last(*args, **kwargs):
        ...
    @staticmethod
    def lastIndexOf(*args, **kwargs):
        ...
    @staticmethod
    def mid(*args, **kwargs):
        ...
    @staticmethod
    def point(*args, **kwargs):
        ...
    @staticmethod
    def prepend(*args, **kwargs):
        ...
    @staticmethod
    def putPoints(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def setPoint(*args, **kwargs):
        ...
    @staticmethod
    def setPoints(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def subtracted(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toPolygonF(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def united(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __contains__(self, key):
        """
        Return key in self.
        """
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Implement self+=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __len__(self):
        """
        Return len(self).
        """
    def __lshift__(self, value):
        """
        Return self<<value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __rlshift__(self, value):
        """
        Return value<<self.
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QPolygonF(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def at(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def containsPoint(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def first(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def intersected(*args, **kwargs):
        ...
    @staticmethod
    def intersects(*args, **kwargs):
        ...
    @staticmethod
    def isClosed(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def last(*args, **kwargs):
        ...
    @staticmethod
    def lastIndexOf(*args, **kwargs):
        ...
    @staticmethod
    def mid(*args, **kwargs):
        ...
    @staticmethod
    def prepend(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def subtracted(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toPolygon(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def united(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __contains__(self, key):
        """
        Return key in self.
        """
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Implement self+=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __len__(self):
        """
        Return len(self).
        """
    def __lshift__(self, value):
        """
        Return self<<value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __rlshift__(self, value):
        """
        Return value<<self.
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QQuaternion(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def conjugated(*args, **kwargs):
        ...
    @staticmethod
    def dotProduct(*args, **kwargs):
        ...
    @staticmethod
    def fromAxes(*args, **kwargs):
        ...
    @staticmethod
    def fromAxisAndAngle(*args, **kwargs):
        ...
    @staticmethod
    def fromDirection(*args, **kwargs):
        ...
    @staticmethod
    def fromEulerAngles(*args, **kwargs):
        ...
    @staticmethod
    def fromRotationMatrix(*args, **kwargs):
        ...
    @staticmethod
    def getAxes(*args, **kwargs):
        ...
    @staticmethod
    def getAxisAndAngle(*args, **kwargs):
        ...
    @staticmethod
    def getEulerAngles(*args, **kwargs):
        ...
    @staticmethod
    def inverted(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def lengthSquared(*args, **kwargs):
        ...
    @staticmethod
    def nlerp(*args, **kwargs):
        ...
    @staticmethod
    def normalize(*args, **kwargs):
        ...
    @staticmethod
    def normalized(*args, **kwargs):
        ...
    @staticmethod
    def rotatedVector(*args, **kwargs):
        ...
    @staticmethod
    def rotationTo(*args, **kwargs):
        ...
    @staticmethod
    def scalar(*args, **kwargs):
        ...
    @staticmethod
    def setScalar(*args, **kwargs):
        ...
    @staticmethod
    def setVector(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def setZ(*args, **kwargs):
        ...
    @staticmethod
    def slerp(*args, **kwargs):
        ...
    @staticmethod
    def toEulerAngles(*args, **kwargs):
        ...
    @staticmethod
    def toRotationMatrix(*args, **kwargs):
        ...
    @staticmethod
    def toVector4D(*args, **kwargs):
        ...
    @staticmethod
    def vector(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
    @staticmethod
    def z(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
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
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __neg__(self):
        """
        -self
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __rtruediv__(self, value):
        """
        Return value/self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
    def __truediv__(self, value):
        """
        Return self/value.
        """
class QRadialGradient(QGradient):
    @staticmethod
    def center(*args, **kwargs):
        ...
    @staticmethod
    def centerRadius(*args, **kwargs):
        ...
    @staticmethod
    def focalPoint(*args, **kwargs):
        ...
    @staticmethod
    def focalRadius(*args, **kwargs):
        ...
    @staticmethod
    def radius(*args, **kwargs):
        ...
    @staticmethod
    def setCenter(*args, **kwargs):
        ...
    @staticmethod
    def setCenterRadius(*args, **kwargs):
        ...
    @staticmethod
    def setFocalPoint(*args, **kwargs):
        ...
    @staticmethod
    def setFocalRadius(*args, **kwargs):
        ...
    @staticmethod
    def setRadius(*args, **kwargs):
        ...
class QRasterWindow(QPaintDeviceWindow):
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
class QRawFont(PyQt6.sip.simplewrapper):
    class AntialiasingType(enum.Enum):
        PixelAntialiasing: typing.ClassVar[QRawFont.AntialiasingType]  # value = <AntialiasingType.PixelAntialiasing: 0>
        SubPixelAntialiasing: typing.ClassVar[QRawFont.AntialiasingType]  # value = <AntialiasingType.SubPixelAntialiasing: 1>
    class LayoutFlag(enum.Flag):
        KernedAdvances: typing.ClassVar[QRawFont.LayoutFlag]  # value = <LayoutFlag.KernedAdvances: 1>
        UseDesignMetrics: typing.ClassVar[QRawFont.LayoutFlag]  # value = <LayoutFlag.UseDesignMetrics: 2>
    @staticmethod
    def advancesForGlyphIndexes(*args, **kwargs):
        ...
    @staticmethod
    def alphaMapForGlyph(*args, **kwargs):
        ...
    @staticmethod
    def ascent(*args, **kwargs):
        ...
    @staticmethod
    def averageCharWidth(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def capHeight(*args, **kwargs):
        ...
    @staticmethod
    def descent(*args, **kwargs):
        ...
    @staticmethod
    def familyName(*args, **kwargs):
        ...
    @staticmethod
    def fontTable(*args, **kwargs):
        ...
    @staticmethod
    def fromFont(*args, **kwargs):
        ...
    @staticmethod
    def glyphIndexesForString(*args, **kwargs):
        ...
    @staticmethod
    def hintingPreference(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def leading(*args, **kwargs):
        ...
    @staticmethod
    def lineThickness(*args, **kwargs):
        ...
    @staticmethod
    def loadFromData(*args, **kwargs):
        ...
    @staticmethod
    def loadFromFile(*args, **kwargs):
        ...
    @staticmethod
    def maxCharWidth(*args, **kwargs):
        ...
    @staticmethod
    def pathForGlyph(*args, **kwargs):
        ...
    @staticmethod
    def pixelSize(*args, **kwargs):
        ...
    @staticmethod
    def setPixelSize(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
    @staticmethod
    def styleName(*args, **kwargs):
        ...
    @staticmethod
    def supportedWritingSystems(*args, **kwargs):
        ...
    @staticmethod
    def supportsCharacter(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def underlinePosition(*args, **kwargs):
        ...
    @staticmethod
    def unitsPerEm(*args, **kwargs):
        ...
    @staticmethod
    def weight(*args, **kwargs):
        ...
    @staticmethod
    def xHeight(*args, **kwargs):
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
class QRegion(PyQt6.sip.simplewrapper):
    class RegionType(enum.Enum):
        Ellipse: typing.ClassVar[QRegion.RegionType]  # value = <RegionType.Ellipse: 1>
        Rectangle: typing.ClassVar[QRegion.RegionType]  # value = <RegionType.Rectangle: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def intersected(*args, **kwargs):
        ...
    @staticmethod
    def intersects(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def rectCount(*args, **kwargs):
        ...
    @staticmethod
    def setRects(*args, **kwargs):
        ...
    @staticmethod
    def subtracted(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def united(*args, **kwargs):
        ...
    @staticmethod
    def xored(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __and__(self, value):
        """
        Return self&value.
        """
    def __bool__(self):
        """
        True if self else False
        """
    def __contains__(self, key):
        """
        Return key in self.
        """
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
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __iand__(self, value):
        """
        Return self&=value.
        """
    def __ior__(self, value):
        """
        Return self|=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __ixor__(self, value):
        """
        Return self^=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __or__(self, value):
        """
        Return self|value.
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __rand__(self, value):
        """
        Return value&self.
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __ror__(self, value):
        """
        Return value|self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __rxor__(self, value):
        """
        Return value^self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
    def __xor__(self, value):
        """
        Return self^value.
        """
class QRegularExpressionValidator(QValidator):
    @staticmethod
    def regularExpression(*args, **kwargs):
        ...
    @staticmethod
    def setRegularExpression(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
class QResizeEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def oldSize(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
class QRgba64(PyQt6.sip.simplewrapper):
    @staticmethod
    def alpha(*args, **kwargs):
        ...
    @staticmethod
    def alpha8(*args, **kwargs):
        ...
    @staticmethod
    def blue(*args, **kwargs):
        ...
    @staticmethod
    def blue8(*args, **kwargs):
        ...
    @staticmethod
    def fromArgb32(*args, **kwargs):
        ...
    @staticmethod
    def fromRgba(*args, **kwargs):
        ...
    @staticmethod
    def fromRgba64(*args, **kwargs):
        ...
    @staticmethod
    def green(*args, **kwargs):
        ...
    @staticmethod
    def green8(*args, **kwargs):
        ...
    @staticmethod
    def isOpaque(*args, **kwargs):
        ...
    @staticmethod
    def isTransparent(*args, **kwargs):
        ...
    @staticmethod
    def premultiplied(*args, **kwargs):
        ...
    @staticmethod
    def red(*args, **kwargs):
        ...
    @staticmethod
    def red8(*args, **kwargs):
        ...
    @staticmethod
    def setAlpha(*args, **kwargs):
        ...
    @staticmethod
    def setBlue(*args, **kwargs):
        ...
    @staticmethod
    def setGreen(*args, **kwargs):
        ...
    @staticmethod
    def setRed(*args, **kwargs):
        ...
    @staticmethod
    def toArgb32(*args, **kwargs):
        ...
    @staticmethod
    def toRgb16(*args, **kwargs):
        ...
    @staticmethod
    def unpremultiplied(*args, **kwargs):
        ...
    def __int__(self):
        """
        int(self)
        """
class QScreen(PyQt6.QtCore.QObject):
    @staticmethod
    def angleBetween(*args, **kwargs):
        ...
    @staticmethod
    def availableGeometry(*args, **kwargs):
        ...
    @staticmethod
    def availableGeometryChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def availableSize(*args, **kwargs):
        ...
    @staticmethod
    def availableVirtualGeometry(*args, **kwargs):
        ...
    @staticmethod
    def availableVirtualSize(*args, **kwargs):
        ...
    @staticmethod
    def depth(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
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
    def grabWindow(*args, **kwargs):
        ...
    @staticmethod
    def isLandscape(*args, **kwargs):
        ...
    @staticmethod
    def isPortrait(*args, **kwargs):
        ...
    @staticmethod
    def logicalDotsPerInch(*args, **kwargs):
        ...
    @staticmethod
    def logicalDotsPerInchChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def logicalDotsPerInchX(*args, **kwargs):
        ...
    @staticmethod
    def logicalDotsPerInchY(*args, **kwargs):
        ...
    @staticmethod
    def manufacturer(*args, **kwargs):
        ...
    @staticmethod
    def mapBetween(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def nativeOrientation(*args, **kwargs):
        ...
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
    def physicalDotsPerInch(*args, **kwargs):
        ...
    @staticmethod
    def physicalDotsPerInchChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def physicalDotsPerInchX(*args, **kwargs):
        ...
    @staticmethod
    def physicalDotsPerInchY(*args, **kwargs):
        ...
    @staticmethod
    def physicalSize(*args, **kwargs):
        ...
    @staticmethod
    def physicalSizeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def primaryOrientation(*args, **kwargs):
        ...
    @staticmethod
    def primaryOrientationChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def refreshRate(*args, **kwargs):
        ...
    @staticmethod
    def refreshRateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def serialNumber(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def transformBetween(*args, **kwargs):
        ...
    @staticmethod
    def virtualGeometry(*args, **kwargs):
        ...
    @staticmethod
    def virtualGeometryChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def virtualSiblingAt(*args, **kwargs):
        ...
    @staticmethod
    def virtualSiblings(*args, **kwargs):
        ...
    @staticmethod
    def virtualSize(*args, **kwargs):
        ...
class QScrollEvent(PyQt6.QtCore.QEvent):
    class ScrollState(enum.Enum):
        ScrollFinished: typing.ClassVar[QScrollEvent.ScrollState]  # value = <ScrollState.ScrollFinished: 2>
        ScrollStarted: typing.ClassVar[QScrollEvent.ScrollState]  # value = <ScrollState.ScrollStarted: 0>
        ScrollUpdated: typing.ClassVar[QScrollEvent.ScrollState]  # value = <ScrollState.ScrollUpdated: 1>
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def contentPos(*args, **kwargs):
        ...
    @staticmethod
    def overshootDistance(*args, **kwargs):
        ...
    @staticmethod
    def scrollState(*args, **kwargs):
        ...
class QScrollPrepareEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def contentPos(*args, **kwargs):
        ...
    @staticmethod
    def contentPosRange(*args, **kwargs):
        ...
    @staticmethod
    def setContentPos(*args, **kwargs):
        ...
    @staticmethod
    def setContentPosRange(*args, **kwargs):
        ...
    @staticmethod
    def setViewportSize(*args, **kwargs):
        ...
    @staticmethod
    def startPos(*args, **kwargs):
        ...
    @staticmethod
    def viewportSize(*args, **kwargs):
        ...
class QSessionManager(PyQt6.QtCore.QObject):
    class RestartHint(enum.Enum):
        RestartAnyway: typing.ClassVar[QSessionManager.RestartHint]  # value = <RestartHint.RestartAnyway: 1>
        RestartIfRunning: typing.ClassVar[QSessionManager.RestartHint]  # value = <RestartHint.RestartIfRunning: 0>
        RestartImmediately: typing.ClassVar[QSessionManager.RestartHint]  # value = <RestartHint.RestartImmediately: 2>
        RestartNever: typing.ClassVar[QSessionManager.RestartHint]  # value = <RestartHint.RestartNever: 3>
    @staticmethod
    def allowsErrorInteraction(*args, **kwargs):
        ...
    @staticmethod
    def allowsInteraction(*args, **kwargs):
        ...
    @staticmethod
    def cancel(*args, **kwargs):
        ...
    @staticmethod
    def discardCommand(*args, **kwargs):
        ...
    @staticmethod
    def isPhase2(*args, **kwargs):
        ...
    @staticmethod
    def release(*args, **kwargs):
        ...
    @staticmethod
    def requestPhase2(*args, **kwargs):
        ...
    @staticmethod
    def restartCommand(*args, **kwargs):
        ...
    @staticmethod
    def restartHint(*args, **kwargs):
        ...
    @staticmethod
    def sessionId(*args, **kwargs):
        ...
    @staticmethod
    def sessionKey(*args, **kwargs):
        ...
    @staticmethod
    def setDiscardCommand(*args, **kwargs):
        ...
    @staticmethod
    def setManagerProperty(*args, **kwargs):
        ...
    @staticmethod
    def setRestartCommand(*args, **kwargs):
        ...
    @staticmethod
    def setRestartHint(*args, **kwargs):
        ...
class QShortcut(PyQt6.QtCore.QObject):
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
    def activatedAmbiguously(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def autoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def context(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRepeat(*args, **kwargs):
        ...
    @staticmethod
    def setContext(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setKey(*args, **kwargs):
        ...
    @staticmethod
    def setKeys(*args, **kwargs):
        ...
    @staticmethod
    def setWhatsThis(*args, **kwargs):
        ...
    @staticmethod
    def whatsThis(*args, **kwargs):
        ...
class QShortcutEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def isAmbiguous(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def shortcutId(*args, **kwargs):
        ...
class QShowEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
class QSinglePointEvent(QPointerEvent):
    @staticmethod
    def button(*args, **kwargs):
        ...
    @staticmethod
    def buttons(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def exclusivePointGrabber(*args, **kwargs):
        ...
    @staticmethod
    def globalPosition(*args, **kwargs):
        ...
    @staticmethod
    def isBeginEvent(*args, **kwargs):
        ...
    @staticmethod
    def isEndEvent(*args, **kwargs):
        ...
    @staticmethod
    def isUpdateEvent(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def scenePosition(*args, **kwargs):
        ...
    @staticmethod
    def setExclusivePointGrabber(*args, **kwargs):
        ...
class QStandardItem(PyQt6.sip.wrapper):
    class ItemType(enum.Enum):
        Type: typing.ClassVar[QStandardItem.ItemType]  # value = <ItemType.Type: 0>
        UserType: typing.ClassVar[QStandardItem.ItemType]  # value = <ItemType.UserType: 1000>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def accessibleDescription(*args, **kwargs):
        ...
    @staticmethod
    def accessibleText(*args, **kwargs):
        ...
    @staticmethod
    def appendColumn(*args, **kwargs):
        ...
    @staticmethod
    def appendRow(*args, **kwargs):
        ...
    @staticmethod
    def appendRows(*args, **kwargs):
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
    def clearData(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def column(*args, **kwargs):
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
    def hasChildren(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insertColumn(*args, **kwargs):
        ...
    @staticmethod
    def insertColumns(*args, **kwargs):
        ...
    @staticmethod
    def insertRow(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def isAutoTristate(*args, **kwargs):
        ...
    @staticmethod
    def isCheckable(*args, **kwargs):
        ...
    @staticmethod
    def isDragEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isDropEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isEditable(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isSelectable(*args, **kwargs):
        ...
    @staticmethod
    def isUserTristate(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def removeColumn(*args, **kwargs):
        ...
    @staticmethod
    def removeColumns(*args, **kwargs):
        ...
    @staticmethod
    def removeRow(*args, **kwargs):
        ...
    @staticmethod
    def removeRows(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setAccessibleDescription(*args, **kwargs):
        ...
    @staticmethod
    def setAccessibleText(*args, **kwargs):
        ...
    @staticmethod
    def setAutoTristate(*args, **kwargs):
        ...
    @staticmethod
    def setBackground(*args, **kwargs):
        ...
    @staticmethod
    def setCheckState(*args, **kwargs):
        ...
    @staticmethod
    def setCheckable(*args, **kwargs):
        ...
    @staticmethod
    def setChild(*args, **kwargs):
        ...
    @staticmethod
    def setColumnCount(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setDragEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setDropEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setEditable(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
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
    def setRowCount(*args, **kwargs):
        ...
    @staticmethod
    def setSelectable(*args, **kwargs):
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
    def setUserTristate(*args, **kwargs):
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
    def takeColumn(*args, **kwargs):
        ...
    @staticmethod
    def takeRow(*args, **kwargs):
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
class QStandardItemModel(PyQt6.QtCore.QAbstractItemModel):
    @staticmethod
    def appendColumn(*args, **kwargs):
        ...
    @staticmethod
    def appendRow(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearItemData(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def findItems(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def hasChildren(*args, **kwargs):
        ...
    @staticmethod
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def horizontalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def indexFromItem(*args, **kwargs):
        ...
    @staticmethod
    def insertColumn(*args, **kwargs):
        ...
    @staticmethod
    def insertColumns(*args, **kwargs):
        ...
    @staticmethod
    def insertRow(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def invisibleRootItem(*args, **kwargs):
        ...
    @staticmethod
    def item(*args, **kwargs):
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
    def itemData(*args, **kwargs):
        ...
    @staticmethod
    def itemFromIndex(*args, **kwargs):
        ...
    @staticmethod
    def itemPrototype(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def removeColumns(*args, **kwargs):
        ...
    @staticmethod
    def removeRows(*args, **kwargs):
        ...
    @staticmethod
    def roleNames(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setColumnCount(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderData(*args, **kwargs):
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
    def setItemData(*args, **kwargs):
        ...
    @staticmethod
    def setItemPrototype(*args, **kwargs):
        ...
    @staticmethod
    def setItemRoleNames(*args, **kwargs):
        ...
    @staticmethod
    def setRowCount(*args, **kwargs):
        ...
    @staticmethod
    def setSortRole(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalHeaderLabels(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def sortRole(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
    @staticmethod
    def takeColumn(*args, **kwargs):
        ...
    @staticmethod
    def takeHorizontalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def takeItem(*args, **kwargs):
        ...
    @staticmethod
    def takeRow(*args, **kwargs):
        ...
    @staticmethod
    def takeVerticalHeaderItem(*args, **kwargs):
        ...
    @staticmethod
    def verticalHeaderItem(*args, **kwargs):
        ...
class QStaticText(PyQt6.sip.simplewrapper):
    class PerformanceHint(enum.Enum):
        AggressiveCaching: typing.ClassVar[QStaticText.PerformanceHint]  # value = <PerformanceHint.AggressiveCaching: 1>
        ModerateCaching: typing.ClassVar[QStaticText.PerformanceHint]  # value = <PerformanceHint.ModerateCaching: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def performanceHint(*args, **kwargs):
        ...
    @staticmethod
    def prepare(*args, **kwargs):
        ...
    @staticmethod
    def setPerformanceHint(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextFormat(*args, **kwargs):
        ...
    @staticmethod
    def setTextOption(*args, **kwargs):
        ...
    @staticmethod
    def setTextWidth(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textFormat(*args, **kwargs):
        ...
    @staticmethod
    def textOption(*args, **kwargs):
        ...
    @staticmethod
    def textWidth(*args, **kwargs):
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
class QStatusTipEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def tip(*args, **kwargs):
        ...
class QStyleHints(PyQt6.QtCore.QObject):
    @staticmethod
    def colorScheme(*args, **kwargs):
        ...
    @staticmethod
    def colorSchemeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def cursorFlashTime(*args, **kwargs):
        ...
    @staticmethod
    def cursorFlashTimeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def fontSmoothingGamma(*args, **kwargs):
        ...
    @staticmethod
    def keyboardAutoRepeatRate(*args, **kwargs):
        ...
    @staticmethod
    def keyboardAutoRepeatRateF(*args, **kwargs):
        ...
    @staticmethod
    def keyboardInputInterval(*args, **kwargs):
        ...
    @staticmethod
    def keyboardInputIntervalChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def mouseDoubleClickDistance(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickInterval(*args, **kwargs):
        ...
    @staticmethod
    def mouseDoubleClickIntervalChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def mousePressAndHoldInterval(*args, **kwargs):
        ...
    @staticmethod
    def mousePressAndHoldIntervalChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def mouseQuickSelectionThreshold(*args, **kwargs):
        ...
    @staticmethod
    def mouseQuickSelectionThresholdChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def passwordMaskCharacter(*args, **kwargs):
        ...
    @staticmethod
    def passwordMaskDelay(*args, **kwargs):
        ...
    @staticmethod
    def setFocusOnTouchRelease(*args, **kwargs):
        ...
    @staticmethod
    def setShowShortcutsInContextMenus(*args, **kwargs):
        ...
    @staticmethod
    def setUseHoverEffects(*args, **kwargs):
        ...
    @staticmethod
    def showIsFullScreen(*args, **kwargs):
        ...
    @staticmethod
    def showIsMaximized(*args, **kwargs):
        ...
    @staticmethod
    def showShortcutsInContextMenus(*args, **kwargs):
        ...
    @staticmethod
    def showShortcutsInContextMenusChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def singleClickActivation(*args, **kwargs):
        ...
    @staticmethod
    def startDragDistance(*args, **kwargs):
        ...
    @staticmethod
    def startDragDistanceChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def startDragTime(*args, **kwargs):
        ...
    @staticmethod
    def startDragTimeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def startDragVelocity(*args, **kwargs):
        ...
    @staticmethod
    def tabFocusBehavior(*args, **kwargs):
        ...
    @staticmethod
    def tabFocusBehaviorChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def touchDoubleTapDistance(*args, **kwargs):
        ...
    @staticmethod
    def useHoverEffects(*args, **kwargs):
        ...
    @staticmethod
    def useHoverEffectsChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def useRtlExtensions(*args, **kwargs):
        ...
    @staticmethod
    def wheelScrollLines(*args, **kwargs):
        ...
    @staticmethod
    def wheelScrollLinesChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QSurface(PyQt6.sip.simplewrapper):
    class SurfaceClass(enum.Enum):
        Offscreen: typing.ClassVar[QSurface.SurfaceClass]  # value = <SurfaceClass.Offscreen: 1>
        Window: typing.ClassVar[QSurface.SurfaceClass]  # value = <SurfaceClass.Window: 0>
    class SurfaceType(enum.Enum):
        Direct3DSurface: typing.ClassVar[QSurface.SurfaceType]  # value = <SurfaceType.Direct3DSurface: 6>
        MetalSurface: typing.ClassVar[QSurface.SurfaceType]  # value = <SurfaceType.MetalSurface: 5>
        OpenGLSurface: typing.ClassVar[QSurface.SurfaceType]  # value = <SurfaceType.OpenGLSurface: 1>
        OpenVGSurface: typing.ClassVar[QSurface.SurfaceType]  # value = <SurfaceType.OpenVGSurface: 3>
        RasterGLSurface: typing.ClassVar[QSurface.SurfaceType]  # value = <SurfaceType.RasterGLSurface: 2>
        RasterSurface: typing.ClassVar[QSurface.SurfaceType]  # value = <SurfaceType.RasterSurface: 0>
        VulkanSurface: typing.ClassVar[QSurface.SurfaceType]  # value = <SurfaceType.VulkanSurface: 4>
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def supportsOpenGL(*args, **kwargs):
        ...
    @staticmethod
    def surfaceClass(*args, **kwargs):
        ...
    @staticmethod
    def surfaceType(*args, **kwargs):
        ...
class QSurfaceFormat(PyQt6.sip.simplewrapper):
    class FormatOption(enum.Flag):
        DebugContext: typing.ClassVar[QSurfaceFormat.FormatOption]  # value = <FormatOption.DebugContext: 2>
        DeprecatedFunctions: typing.ClassVar[QSurfaceFormat.FormatOption]  # value = <FormatOption.DeprecatedFunctions: 4>
        ProtectedContent: typing.ClassVar[QSurfaceFormat.FormatOption]  # value = <FormatOption.ProtectedContent: 16>
        ResetNotification: typing.ClassVar[QSurfaceFormat.FormatOption]  # value = <FormatOption.ResetNotification: 8>
        StereoBuffers: typing.ClassVar[QSurfaceFormat.FormatOption]  # value = <FormatOption.StereoBuffers: 1>
    class OpenGLContextProfile(enum.Enum):
        CompatibilityProfile: typing.ClassVar[QSurfaceFormat.OpenGLContextProfile]  # value = <OpenGLContextProfile.CompatibilityProfile: 2>
        CoreProfile: typing.ClassVar[QSurfaceFormat.OpenGLContextProfile]  # value = <OpenGLContextProfile.CoreProfile: 1>
        NoProfile: typing.ClassVar[QSurfaceFormat.OpenGLContextProfile]  # value = <OpenGLContextProfile.NoProfile: 0>
    class RenderableType(enum.Enum):
        DefaultRenderableType: typing.ClassVar[QSurfaceFormat.RenderableType]  # value = <RenderableType.DefaultRenderableType: 0>
        OpenGL: typing.ClassVar[QSurfaceFormat.RenderableType]  # value = <RenderableType.OpenGL: 1>
        OpenGLES: typing.ClassVar[QSurfaceFormat.RenderableType]  # value = <RenderableType.OpenGLES: 2>
        OpenVG: typing.ClassVar[QSurfaceFormat.RenderableType]  # value = <RenderableType.OpenVG: 4>
    class SwapBehavior(enum.Enum):
        DefaultSwapBehavior: typing.ClassVar[QSurfaceFormat.SwapBehavior]  # value = <SwapBehavior.DefaultSwapBehavior: 0>
        DoubleBuffer: typing.ClassVar[QSurfaceFormat.SwapBehavior]  # value = <SwapBehavior.DoubleBuffer: 2>
        SingleBuffer: typing.ClassVar[QSurfaceFormat.SwapBehavior]  # value = <SwapBehavior.SingleBuffer: 1>
        TripleBuffer: typing.ClassVar[QSurfaceFormat.SwapBehavior]  # value = <SwapBehavior.TripleBuffer: 3>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def alphaBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def blueBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def colorSpace(*args, **kwargs):
        ...
    @staticmethod
    def defaultFormat(*args, **kwargs):
        ...
    @staticmethod
    def depthBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def greenBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def hasAlpha(*args, **kwargs):
        ...
    @staticmethod
    def majorVersion(*args, **kwargs):
        ...
    @staticmethod
    def minorVersion(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def profile(*args, **kwargs):
        ...
    @staticmethod
    def redBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def renderableType(*args, **kwargs):
        ...
    @staticmethod
    def samples(*args, **kwargs):
        ...
    @staticmethod
    def setAlphaBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setBlueBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setColorSpace(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultFormat(*args, **kwargs):
        ...
    @staticmethod
    def setDepthBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setGreenBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setMajorVersion(*args, **kwargs):
        ...
    @staticmethod
    def setMinorVersion(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setProfile(*args, **kwargs):
        ...
    @staticmethod
    def setRedBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setRenderableType(*args, **kwargs):
        ...
    @staticmethod
    def setSamples(*args, **kwargs):
        ...
    @staticmethod
    def setStencilBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setStereo(*args, **kwargs):
        ...
    @staticmethod
    def setSwapBehavior(*args, **kwargs):
        ...
    @staticmethod
    def setSwapInterval(*args, **kwargs):
        ...
    @staticmethod
    def setVersion(*args, **kwargs):
        ...
    @staticmethod
    def stencilBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def stereo(*args, **kwargs):
        ...
    @staticmethod
    def swapBehavior(*args, **kwargs):
        ...
    @staticmethod
    def swapInterval(*args, **kwargs):
        ...
    @staticmethod
    def testOption(*args, **kwargs):
        ...
    @staticmethod
    def version(*args, **kwargs):
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
class QSyntaxHighlighter(PyQt6.QtCore.QObject):
    @staticmethod
    def currentBlock(*args, **kwargs):
        ...
    @staticmethod
    def currentBlockState(*args, **kwargs):
        ...
    @staticmethod
    def currentBlockUserData(*args, **kwargs):
        ...
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def highlightBlock(*args, **kwargs):
        ...
    @staticmethod
    def previousBlockState(*args, **kwargs):
        ...
    @staticmethod
    def rehighlight(*args, **kwargs):
        ...
    @staticmethod
    def rehighlightBlock(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentBlockState(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentBlockUserData(*args, **kwargs):
        ...
    @staticmethod
    def setDocument(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
class QTabletEvent(QSinglePointEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def pressure(*args, **kwargs):
        ...
    @staticmethod
    def rotation(*args, **kwargs):
        ...
    @staticmethod
    def tangentialPressure(*args, **kwargs):
        ...
    @staticmethod
    def xTilt(*args, **kwargs):
        ...
    @staticmethod
    def yTilt(*args, **kwargs):
        ...
    @staticmethod
    def z(*args, **kwargs):
        ...
class QTextBlock(PyQt6.sip.wrapper):
    class iterator(PyQt6.sip.simplewrapper):
        __hash__: typing.ClassVar[None] = None
        @staticmethod
        def atEnd(*args, **kwargs):
            ...
        @staticmethod
        def fragment(*args, **kwargs):
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
        def __iadd__(self, value):
            """
            Return self+=value.
            """
        def __isub__(self, value):
            """
            Return self-=value.
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
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def begin(*args, **kwargs):
        ...
    @staticmethod
    def blockFormat(*args, **kwargs):
        ...
    @staticmethod
    def blockFormatIndex(*args, **kwargs):
        ...
    @staticmethod
    def blockNumber(*args, **kwargs):
        ...
    @staticmethod
    def charFormat(*args, **kwargs):
        ...
    @staticmethod
    def charFormatIndex(*args, **kwargs):
        ...
    @staticmethod
    def clearLayout(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def end(*args, **kwargs):
        ...
    @staticmethod
    def firstLineNumber(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def layout(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def lineCount(*args, **kwargs):
        ...
    @staticmethod
    def next(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def previous(*args, **kwargs):
        ...
    @staticmethod
    def revision(*args, **kwargs):
        ...
    @staticmethod
    def setLineCount(*args, **kwargs):
        ...
    @staticmethod
    def setRevision(*args, **kwargs):
        ...
    @staticmethod
    def setUserData(*args, **kwargs):
        ...
    @staticmethod
    def setUserState(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textDirection(*args, **kwargs):
        ...
    @staticmethod
    def textFormats(*args, **kwargs):
        ...
    @staticmethod
    def textList(*args, **kwargs):
        ...
    @staticmethod
    def userData(*args, **kwargs):
        ...
    @staticmethod
    def userState(*args, **kwargs):
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
class QTextBlockFormat(QTextFormat):
    class LineHeightTypes(enum.Enum):
        FixedHeight: typing.ClassVar[QTextBlockFormat.LineHeightTypes]  # value = <LineHeightTypes.FixedHeight: 2>
        LineDistanceHeight: typing.ClassVar[QTextBlockFormat.LineHeightTypes]  # value = <LineHeightTypes.LineDistanceHeight: 4>
        MinimumHeight: typing.ClassVar[QTextBlockFormat.LineHeightTypes]  # value = <LineHeightTypes.MinimumHeight: 3>
        ProportionalHeight: typing.ClassVar[QTextBlockFormat.LineHeightTypes]  # value = <LineHeightTypes.ProportionalHeight: 1>
        SingleHeight: typing.ClassVar[QTextBlockFormat.LineHeightTypes]  # value = <LineHeightTypes.SingleHeight: 0>
    class MarkerType(enum.Enum):
        Checked: typing.ClassVar[QTextBlockFormat.MarkerType]  # value = <MarkerType.Checked: 2>
        NoMarker: typing.ClassVar[QTextBlockFormat.MarkerType]  # value = <MarkerType.NoMarker: 0>
        Unchecked: typing.ClassVar[QTextBlockFormat.MarkerType]  # value = <MarkerType.Unchecked: 1>
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def bottomMargin(*args, **kwargs):
        ...
    @staticmethod
    def headingLevel(*args, **kwargs):
        ...
    @staticmethod
    def indent(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def leftMargin(*args, **kwargs):
        ...
    @staticmethod
    def lineHeight(*args, **kwargs):
        ...
    @staticmethod
    def lineHeightType(*args, **kwargs):
        ...
    @staticmethod
    def marker(*args, **kwargs):
        ...
    @staticmethod
    def nonBreakableLines(*args, **kwargs):
        ...
    @staticmethod
    def pageBreakPolicy(*args, **kwargs):
        ...
    @staticmethod
    def rightMargin(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setBottomMargin(*args, **kwargs):
        ...
    @staticmethod
    def setHeadingLevel(*args, **kwargs):
        ...
    @staticmethod
    def setIndent(*args, **kwargs):
        ...
    @staticmethod
    def setLeftMargin(*args, **kwargs):
        ...
    @staticmethod
    def setLineHeight(*args, **kwargs):
        ...
    @staticmethod
    def setMarker(*args, **kwargs):
        ...
    @staticmethod
    def setNonBreakableLines(*args, **kwargs):
        ...
    @staticmethod
    def setPageBreakPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setRightMargin(*args, **kwargs):
        ...
    @staticmethod
    def setTabPositions(*args, **kwargs):
        ...
    @staticmethod
    def setTextIndent(*args, **kwargs):
        ...
    @staticmethod
    def setTopMargin(*args, **kwargs):
        ...
    @staticmethod
    def tabPositions(*args, **kwargs):
        ...
    @staticmethod
    def textIndent(*args, **kwargs):
        ...
    @staticmethod
    def topMargin(*args, **kwargs):
        ...
class QTextBlockGroup(QTextObject):
    @staticmethod
    def blockFormatChanged(*args, **kwargs):
        ...
    @staticmethod
    def blockInserted(*args, **kwargs):
        ...
    @staticmethod
    def blockList(*args, **kwargs):
        ...
    @staticmethod
    def blockRemoved(*args, **kwargs):
        ...
class QTextBlockUserData(PyQt6.sip.wrapper):
    pass
class QTextCharFormat(QTextFormat):
    class FontPropertiesInheritanceBehavior(enum.Enum):
        FontPropertiesAll: typing.ClassVar[QTextCharFormat.FontPropertiesInheritanceBehavior]  # value = <FontPropertiesInheritanceBehavior.FontPropertiesAll: 1>
        FontPropertiesSpecifiedOnly: typing.ClassVar[QTextCharFormat.FontPropertiesInheritanceBehavior]  # value = <FontPropertiesInheritanceBehavior.FontPropertiesSpecifiedOnly: 0>
    class UnderlineStyle(enum.Enum):
        DashDotDotLine: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.DashDotDotLine: 5>
        DashDotLine: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.DashDotLine: 4>
        DashUnderline: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.DashUnderline: 2>
        DotLine: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.DotLine: 3>
        NoUnderline: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.NoUnderline: 0>
        SingleUnderline: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.SingleUnderline: 1>
        SpellCheckUnderline: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.SpellCheckUnderline: 7>
        WaveUnderline: typing.ClassVar[QTextCharFormat.UnderlineStyle]  # value = <UnderlineStyle.WaveUnderline: 6>
    class VerticalAlignment(enum.Enum):
        AlignBaseline: typing.ClassVar[QTextCharFormat.VerticalAlignment]  # value = <VerticalAlignment.AlignBaseline: 6>
        AlignBottom: typing.ClassVar[QTextCharFormat.VerticalAlignment]  # value = <VerticalAlignment.AlignBottom: 5>
        AlignMiddle: typing.ClassVar[QTextCharFormat.VerticalAlignment]  # value = <VerticalAlignment.AlignMiddle: 3>
        AlignNormal: typing.ClassVar[QTextCharFormat.VerticalAlignment]  # value = <VerticalAlignment.AlignNormal: 0>
        AlignSubScript: typing.ClassVar[QTextCharFormat.VerticalAlignment]  # value = <VerticalAlignment.AlignSubScript: 2>
        AlignSuperScript: typing.ClassVar[QTextCharFormat.VerticalAlignment]  # value = <VerticalAlignment.AlignSuperScript: 1>
        AlignTop: typing.ClassVar[QTextCharFormat.VerticalAlignment]  # value = <VerticalAlignment.AlignTop: 4>
    @staticmethod
    def anchorHref(*args, **kwargs):
        ...
    @staticmethod
    def anchorNames(*args, **kwargs):
        ...
    @staticmethod
    def baselineOffset(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def fontCapitalization(*args, **kwargs):
        ...
    @staticmethod
    def fontFamilies(*args, **kwargs):
        ...
    @staticmethod
    def fontFamily(*args, **kwargs):
        ...
    @staticmethod
    def fontFixedPitch(*args, **kwargs):
        ...
    @staticmethod
    def fontHintingPreference(*args, **kwargs):
        ...
    @staticmethod
    def fontItalic(*args, **kwargs):
        ...
    @staticmethod
    def fontKerning(*args, **kwargs):
        ...
    @staticmethod
    def fontLetterSpacing(*args, **kwargs):
        ...
    @staticmethod
    def fontLetterSpacingType(*args, **kwargs):
        ...
    @staticmethod
    def fontOverline(*args, **kwargs):
        ...
    @staticmethod
    def fontPointSize(*args, **kwargs):
        ...
    @staticmethod
    def fontStretch(*args, **kwargs):
        ...
    @staticmethod
    def fontStrikeOut(*args, **kwargs):
        ...
    @staticmethod
    def fontStyleHint(*args, **kwargs):
        ...
    @staticmethod
    def fontStyleName(*args, **kwargs):
        ...
    @staticmethod
    def fontStyleStrategy(*args, **kwargs):
        ...
    @staticmethod
    def fontUnderline(*args, **kwargs):
        ...
    @staticmethod
    def fontWeight(*args, **kwargs):
        ...
    @staticmethod
    def fontWordSpacing(*args, **kwargs):
        ...
    @staticmethod
    def isAnchor(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def setAnchor(*args, **kwargs):
        ...
    @staticmethod
    def setAnchorHref(*args, **kwargs):
        ...
    @staticmethod
    def setAnchorNames(*args, **kwargs):
        ...
    @staticmethod
    def setBaselineOffset(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setFontCapitalization(*args, **kwargs):
        ...
    @staticmethod
    def setFontFamilies(*args, **kwargs):
        ...
    @staticmethod
    def setFontFamily(*args, **kwargs):
        ...
    @staticmethod
    def setFontFixedPitch(*args, **kwargs):
        ...
    @staticmethod
    def setFontHintingPreference(*args, **kwargs):
        ...
    @staticmethod
    def setFontItalic(*args, **kwargs):
        ...
    @staticmethod
    def setFontKerning(*args, **kwargs):
        ...
    @staticmethod
    def setFontLetterSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setFontLetterSpacingType(*args, **kwargs):
        ...
    @staticmethod
    def setFontOverline(*args, **kwargs):
        ...
    @staticmethod
    def setFontPointSize(*args, **kwargs):
        ...
    @staticmethod
    def setFontStretch(*args, **kwargs):
        ...
    @staticmethod
    def setFontStrikeOut(*args, **kwargs):
        ...
    @staticmethod
    def setFontStyleHint(*args, **kwargs):
        ...
    @staticmethod
    def setFontStyleName(*args, **kwargs):
        ...
    @staticmethod
    def setFontStyleStrategy(*args, **kwargs):
        ...
    @staticmethod
    def setFontUnderline(*args, **kwargs):
        ...
    @staticmethod
    def setFontWeight(*args, **kwargs):
        ...
    @staticmethod
    def setFontWordSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setSubScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def setSuperScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def setTableCellColumnSpan(*args, **kwargs):
        ...
    @staticmethod
    def setTableCellRowSpan(*args, **kwargs):
        ...
    @staticmethod
    def setTextOutline(*args, **kwargs):
        ...
    @staticmethod
    def setToolTip(*args, **kwargs):
        ...
    @staticmethod
    def setUnderlineColor(*args, **kwargs):
        ...
    @staticmethod
    def setUnderlineStyle(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalAlignment(*args, **kwargs):
        ...
    @staticmethod
    def subScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def superScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def tableCellColumnSpan(*args, **kwargs):
        ...
    @staticmethod
    def tableCellRowSpan(*args, **kwargs):
        ...
    @staticmethod
    def textOutline(*args, **kwargs):
        ...
    @staticmethod
    def toolTip(*args, **kwargs):
        ...
    @staticmethod
    def underlineColor(*args, **kwargs):
        ...
    @staticmethod
    def underlineStyle(*args, **kwargs):
        ...
    @staticmethod
    def verticalAlignment(*args, **kwargs):
        ...
class QTextCursor(PyQt6.sip.simplewrapper):
    class MoveMode(enum.Enum):
        KeepAnchor: typing.ClassVar[QTextCursor.MoveMode]  # value = <MoveMode.KeepAnchor: 1>
        MoveAnchor: typing.ClassVar[QTextCursor.MoveMode]  # value = <MoveMode.MoveAnchor: 0>
    class MoveOperation(enum.Enum):
        Down: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.Down: 12>
        End: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.End: 11>
        EndOfBlock: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.EndOfBlock: 15>
        EndOfLine: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.EndOfLine: 13>
        EndOfWord: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.EndOfWord: 14>
        Left: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.Left: 9>
        NextBlock: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.NextBlock: 16>
        NextCell: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.NextCell: 21>
        NextCharacter: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.NextCharacter: 17>
        NextRow: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.NextRow: 23>
        NextWord: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.NextWord: 18>
        NoMove: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.NoMove: 0>
        PreviousBlock: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.PreviousBlock: 6>
        PreviousCell: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.PreviousCell: 22>
        PreviousCharacter: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.PreviousCharacter: 7>
        PreviousRow: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.PreviousRow: 24>
        PreviousWord: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.PreviousWord: 8>
        Right: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.Right: 19>
        Start: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.Start: 1>
        StartOfBlock: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.StartOfBlock: 4>
        StartOfLine: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.StartOfLine: 3>
        StartOfWord: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.StartOfWord: 5>
        Up: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.Up: 2>
        WordLeft: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.WordLeft: 10>
        WordRight: typing.ClassVar[QTextCursor.MoveOperation]  # value = <MoveOperation.WordRight: 20>
    class SelectionType(enum.Enum):
        BlockUnderCursor: typing.ClassVar[QTextCursor.SelectionType]  # value = <SelectionType.BlockUnderCursor: 2>
        Document: typing.ClassVar[QTextCursor.SelectionType]  # value = <SelectionType.Document: 3>
        LineUnderCursor: typing.ClassVar[QTextCursor.SelectionType]  # value = <SelectionType.LineUnderCursor: 1>
        WordUnderCursor: typing.ClassVar[QTextCursor.SelectionType]  # value = <SelectionType.WordUnderCursor: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def anchor(*args, **kwargs):
        ...
    @staticmethod
    def atBlockEnd(*args, **kwargs):
        ...
    @staticmethod
    def atBlockStart(*args, **kwargs):
        ...
    @staticmethod
    def atEnd(*args, **kwargs):
        ...
    @staticmethod
    def atStart(*args, **kwargs):
        ...
    @staticmethod
    def beginEditBlock(*args, **kwargs):
        ...
    @staticmethod
    def block(*args, **kwargs):
        ...
    @staticmethod
    def blockCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def blockFormat(*args, **kwargs):
        ...
    @staticmethod
    def blockNumber(*args, **kwargs):
        ...
    @staticmethod
    def charFormat(*args, **kwargs):
        ...
    @staticmethod
    def clearSelection(*args, **kwargs):
        ...
    @staticmethod
    def columnNumber(*args, **kwargs):
        ...
    @staticmethod
    def createList(*args, **kwargs):
        ...
    @staticmethod
    def currentFrame(*args, **kwargs):
        ...
    @staticmethod
    def currentList(*args, **kwargs):
        ...
    @staticmethod
    def currentTable(*args, **kwargs):
        ...
    @staticmethod
    def deleteChar(*args, **kwargs):
        ...
    @staticmethod
    def deletePreviousChar(*args, **kwargs):
        ...
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def endEditBlock(*args, **kwargs):
        ...
    @staticmethod
    def hasComplexSelection(*args, **kwargs):
        ...
    @staticmethod
    def hasSelection(*args, **kwargs):
        ...
    @staticmethod
    def insertBlock(*args, **kwargs):
        ...
    @staticmethod
    def insertFragment(*args, **kwargs):
        ...
    @staticmethod
    def insertFrame(*args, **kwargs):
        ...
    @staticmethod
    def insertHtml(*args, **kwargs):
        ...
    @staticmethod
    def insertImage(*args, **kwargs):
        ...
    @staticmethod
    def insertList(*args, **kwargs):
        ...
    @staticmethod
    def insertMarkdown(*args, **kwargs):
        ...
    @staticmethod
    def insertTable(*args, **kwargs):
        ...
    @staticmethod
    def insertText(*args, **kwargs):
        ...
    @staticmethod
    def isCopyOf(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def joinPreviousEditBlock(*args, **kwargs):
        ...
    @staticmethod
    def keepPositionOnInsert(*args, **kwargs):
        ...
    @staticmethod
    def mergeBlockCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def mergeBlockFormat(*args, **kwargs):
        ...
    @staticmethod
    def mergeCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def movePosition(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def positionInBlock(*args, **kwargs):
        ...
    @staticmethod
    def removeSelectedText(*args, **kwargs):
        ...
    @staticmethod
    def select(*args, **kwargs):
        ...
    @staticmethod
    def selectedTableCells(*args, **kwargs):
        ...
    @staticmethod
    def selectedText(*args, **kwargs):
        ...
    @staticmethod
    def selection(*args, **kwargs):
        ...
    @staticmethod
    def selectionEnd(*args, **kwargs):
        ...
    @staticmethod
    def selectionStart(*args, **kwargs):
        ...
    @staticmethod
    def setBlockCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def setBlockFormat(*args, **kwargs):
        ...
    @staticmethod
    def setCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def setKeepPositionOnInsert(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
    @staticmethod
    def setVerticalMovementX(*args, **kwargs):
        ...
    @staticmethod
    def setVisualNavigation(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def verticalMovementX(*args, **kwargs):
        ...
    @staticmethod
    def visualNavigation(*args, **kwargs):
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
class QTextDocument(PyQt6.QtCore.QObject):
    class FindFlag(enum.Flag):
        FindBackward: typing.ClassVar[QTextDocument.FindFlag]  # value = <FindFlag.FindBackward: 1>
        FindCaseSensitively: typing.ClassVar[QTextDocument.FindFlag]  # value = <FindFlag.FindCaseSensitively: 2>
        FindWholeWords: typing.ClassVar[QTextDocument.FindFlag]  # value = <FindFlag.FindWholeWords: 4>
    class MarkdownFeature(enum.Flag):
        pass
    class MetaInformation(enum.Enum):
        CssMedia: typing.ClassVar[QTextDocument.MetaInformation]  # value = <MetaInformation.CssMedia: 2>
        DocumentTitle: typing.ClassVar[QTextDocument.MetaInformation]  # value = <MetaInformation.DocumentTitle: 0>
        DocumentUrl: typing.ClassVar[QTextDocument.MetaInformation]  # value = <MetaInformation.DocumentUrl: 1>
    class ResourceType(enum.IntEnum):
        HtmlResource: typing.ClassVar[QTextDocument.ResourceType]  # value = <ResourceType.HtmlResource: 1>
        ImageResource: typing.ClassVar[QTextDocument.ResourceType]  # value = <ResourceType.ImageResource: 2>
        MarkdownResource: typing.ClassVar[QTextDocument.ResourceType]  # value = <ResourceType.MarkdownResource: 4>
        StyleSheetResource: typing.ClassVar[QTextDocument.ResourceType]  # value = <ResourceType.StyleSheetResource: 3>
        UnknownResource: typing.ClassVar[QTextDocument.ResourceType]  # value = <ResourceType.UnknownResource: 0>
        UserResource: typing.ClassVar[QTextDocument.ResourceType]  # value = <ResourceType.UserResource: 100>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class Stacks(enum.Enum):
        RedoStack: typing.ClassVar[QTextDocument.Stacks]  # value = <Stacks.RedoStack: 2>
        UndoAndRedoStacks: typing.ClassVar[QTextDocument.Stacks]  # value = <Stacks.UndoAndRedoStacks: 3>
        UndoStack: typing.ClassVar[QTextDocument.Stacks]  # value = <Stacks.UndoStack: 1>
    @staticmethod
    def addResource(*args, **kwargs):
        ...
    @staticmethod
    def adjustSize(*args, **kwargs):
        ...
    @staticmethod
    def allFormats(*args, **kwargs):
        ...
    @staticmethod
    def availableRedoSteps(*args, **kwargs):
        ...
    @staticmethod
    def availableUndoSteps(*args, **kwargs):
        ...
    @staticmethod
    def baseUrl(*args, **kwargs):
        ...
    @staticmethod
    def baseUrlChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def baselineOffset(*args, **kwargs):
        ...
    @staticmethod
    def begin(*args, **kwargs):
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
    def characterAt(*args, **kwargs):
        ...
    @staticmethod
    def characterCount(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearUndoRedoStacks(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def contentsChange(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def contentsChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def createObject(*args, **kwargs):
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
    def defaultCursorMoveStyle(*args, **kwargs):
        ...
    @staticmethod
    def defaultFont(*args, **kwargs):
        ...
    @staticmethod
    def defaultResourceProvider(*args, **kwargs):
        ...
    @staticmethod
    def defaultStyleSheet(*args, **kwargs):
        ...
    @staticmethod
    def defaultTextOption(*args, **kwargs):
        ...
    @staticmethod
    def documentLayout(*args, **kwargs):
        ...
    @staticmethod
    def documentLayoutChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def documentMargin(*args, **kwargs):
        ...
    @staticmethod
    def drawContents(*args, **kwargs):
        ...
    @staticmethod
    def end(*args, **kwargs):
        ...
    @staticmethod
    def find(*args, **kwargs):
        ...
    @staticmethod
    def findBlock(*args, **kwargs):
        ...
    @staticmethod
    def findBlockByLineNumber(*args, **kwargs):
        ...
    @staticmethod
    def findBlockByNumber(*args, **kwargs):
        ...
    @staticmethod
    def firstBlock(*args, **kwargs):
        ...
    @staticmethod
    def idealWidth(*args, **kwargs):
        ...
    @staticmethod
    def indentWidth(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isLayoutEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isModified(*args, **kwargs):
        ...
    @staticmethod
    def isRedoAvailable(*args, **kwargs):
        ...
    @staticmethod
    def isUndoAvailable(*args, **kwargs):
        ...
    @staticmethod
    def isUndoRedoEnabled(*args, **kwargs):
        ...
    @staticmethod
    def lastBlock(*args, **kwargs):
        ...
    @staticmethod
    def lineCount(*args, **kwargs):
        ...
    @staticmethod
    def loadResource(*args, **kwargs):
        ...
    @staticmethod
    def markContentsDirty(*args, **kwargs):
        ...
    @staticmethod
    def maximumBlockCount(*args, **kwargs):
        ...
    @staticmethod
    def metaInformation(*args, **kwargs):
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
    def object(*args, **kwargs):
        ...
    @staticmethod
    def objectForFormat(*args, **kwargs):
        ...
    @staticmethod
    def pageCount(*args, **kwargs):
        ...
    @staticmethod
    def pageSize(*args, **kwargs):
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
    def resource(*args, **kwargs):
        ...
    @staticmethod
    def resourceProvider(*args, **kwargs):
        ...
    @staticmethod
    def revision(*args, **kwargs):
        ...
    @staticmethod
    def rootFrame(*args, **kwargs):
        ...
    @staticmethod
    def setBaseUrl(*args, **kwargs):
        ...
    @staticmethod
    def setBaselineOffset(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultCursorMoveStyle(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultFont(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultResourceProvider(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultStyleSheet(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultTextOption(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentLayout(*args, **kwargs):
        ...
    @staticmethod
    def setDocumentMargin(*args, **kwargs):
        ...
    @staticmethod
    def setHtml(*args, **kwargs):
        ...
    @staticmethod
    def setIndentWidth(*args, **kwargs):
        ...
    @staticmethod
    def setLayoutEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setMarkdown(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumBlockCount(*args, **kwargs):
        ...
    @staticmethod
    def setMetaInformation(*args, **kwargs):
        ...
    @staticmethod
    def setModified(*args, **kwargs):
        ...
    @staticmethod
    def setPageSize(*args, **kwargs):
        ...
    @staticmethod
    def setPlainText(*args, **kwargs):
        ...
    @staticmethod
    def setResourceProvider(*args, **kwargs):
        ...
    @staticmethod
    def setSubScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def setSuperScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def setTextWidth(*args, **kwargs):
        ...
    @staticmethod
    def setUndoRedoEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setUseDesignMetrics(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def subScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def superScriptBaseline(*args, **kwargs):
        ...
    @staticmethod
    def textWidth(*args, **kwargs):
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
    def toRawText(*args, **kwargs):
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
    def undoCommandAdded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def useDesignMetrics(*args, **kwargs):
        ...
class QTextDocumentFragment(PyQt6.sip.simplewrapper):
    @staticmethod
    def fromHtml(*args, **kwargs):
        ...
    @staticmethod
    def fromMarkdown(*args, **kwargs):
        ...
    @staticmethod
    def fromPlainText(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
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
    def toRawText(*args, **kwargs):
        ...
class QTextDocumentWriter(PyQt6.sip.simplewrapper):
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def supportedDocumentFormats(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
class QTextFormat(PyQt6.sip.simplewrapper):
    class FormatType(enum.IntEnum):
        BlockFormat: typing.ClassVar[QTextFormat.FormatType]  # value = <FormatType.BlockFormat: 1>
        CharFormat: typing.ClassVar[QTextFormat.FormatType]  # value = <FormatType.CharFormat: 2>
        FrameFormat: typing.ClassVar[QTextFormat.FormatType]  # value = <FormatType.FrameFormat: 5>
        InvalidFormat: typing.ClassVar[QTextFormat.FormatType]  # value = <FormatType.InvalidFormat: -1>
        ListFormat: typing.ClassVar[QTextFormat.FormatType]  # value = <FormatType.ListFormat: 3>
        UserFormat: typing.ClassVar[QTextFormat.FormatType]  # value = <FormatType.UserFormat: 100>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class ObjectTypes(enum.IntEnum):
        ImageObject: typing.ClassVar[QTextFormat.ObjectTypes]  # value = <ObjectTypes.ImageObject: 1>
        NoObject: typing.ClassVar[QTextFormat.ObjectTypes]  # value = <ObjectTypes.NoObject: 0>
        TableCellObject: typing.ClassVar[QTextFormat.ObjectTypes]  # value = <ObjectTypes.TableCellObject: 3>
        TableObject: typing.ClassVar[QTextFormat.ObjectTypes]  # value = <ObjectTypes.TableObject: 2>
        UserObject: typing.ClassVar[QTextFormat.ObjectTypes]  # value = <ObjectTypes.UserObject: 4096>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class PageBreakFlag(enum.Flag):
        PageBreak_AlwaysAfter: typing.ClassVar[QTextFormat.PageBreakFlag]  # value = <PageBreakFlag.PageBreak_AlwaysAfter: 16>
        PageBreak_AlwaysBefore: typing.ClassVar[QTextFormat.PageBreakFlag]  # value = <PageBreakFlag.PageBreak_AlwaysBefore: 1>
    class Property(enum.IntEnum):
        AnchorHref: typing.ClassVar[QTextFormat.Property]  # value = <Property.AnchorHref: 8241>
        AnchorName: typing.ClassVar[QTextFormat.Property]  # value = <Property.AnchorName: 8242>
        BackgroundBrush: typing.ClassVar[QTextFormat.Property]  # value = <Property.BackgroundBrush: 2080>
        BackgroundImageUrl: typing.ClassVar[QTextFormat.Property]  # value = <Property.BackgroundImageUrl: 2083>
        BlockAlignment: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockAlignment: 4112>
        BlockBottomMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockBottomMargin: 4145>
        BlockCodeFence: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockCodeFence: 4241>
        BlockCodeLanguage: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockCodeLanguage: 4240>
        BlockIndent: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockIndent: 4160>
        BlockLeftMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockLeftMargin: 4146>
        BlockMarker: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockMarker: 4256>
        BlockNonBreakableLines: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockNonBreakableLines: 4176>
        BlockQuoteLevel: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockQuoteLevel: 4224>
        BlockRightMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockRightMargin: 4147>
        BlockTopMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockTopMargin: 4144>
        BlockTrailingHorizontalRulerWidth: typing.ClassVar[QTextFormat.Property]  # value = <Property.BlockTrailingHorizontalRulerWidth: 4192>
        CssFloat: typing.ClassVar[QTextFormat.Property]  # value = <Property.CssFloat: 2048>
        FirstFontProperty: typing.ClassVar[QTextFormat.Property]  # value = <Property.FirstFontProperty: 8160>
        FontFamilies: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontFamilies: 8167>
        FontFixedPitch: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontFixedPitch: 8200>
        FontHintingPreference: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontHintingPreference: 8166>
        FontItalic: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontItalic: 8196>
        FontKerning: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontKerning: 8165>
        FontLetterSpacing: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontLetterSpacing: 8161>
        FontLetterSpacingType: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontLetterSpacingType: 8169>
        FontOverline: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontOverline: 8198>
        FontPixelSize: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontPixelSize: 8201>
        FontPointSize: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontPointSize: 8193>
        FontSizeAdjustment: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontSizeAdjustment: 8194>
        FontStretch: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontStretch: 8170>
        FontStrikeOut: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontStrikeOut: 8199>
        FontStyleHint: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontStyleHint: 8163>
        FontStyleName: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontStyleName: 8168>
        FontStyleStrategy: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontStyleStrategy: 8164>
        FontUnderline: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontUnderline: 8197>
        FontWeight: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontWeight: 8195>
        FontWordSpacing: typing.ClassVar[QTextFormat.Property]  # value = <Property.FontWordSpacing: 8162>
        ForegroundBrush: typing.ClassVar[QTextFormat.Property]  # value = <Property.ForegroundBrush: 2081>
        FrameBorder: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameBorder: 16384>
        FrameBorderBrush: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameBorderBrush: 16393>
        FrameBorderStyle: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameBorderStyle: 16400>
        FrameBottomMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameBottomMargin: 16390>
        FrameHeight: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameHeight: 16388>
        FrameLeftMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameLeftMargin: 16391>
        FrameMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameMargin: 16385>
        FramePadding: typing.ClassVar[QTextFormat.Property]  # value = <Property.FramePadding: 16386>
        FrameRightMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameRightMargin: 16392>
        FrameTopMargin: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameTopMargin: 16389>
        FrameWidth: typing.ClassVar[QTextFormat.Property]  # value = <Property.FrameWidth: 16387>
        FullWidthSelection: typing.ClassVar[QTextFormat.Property]  # value = <Property.FullWidthSelection: 24576>
        HeadingLevel: typing.ClassVar[QTextFormat.Property]  # value = <Property.HeadingLevel: 4208>
        ImageAltText: typing.ClassVar[QTextFormat.Property]  # value = <Property.ImageAltText: 20482>
        ImageHeight: typing.ClassVar[QTextFormat.Property]  # value = <Property.ImageHeight: 20497>
        ImageName: typing.ClassVar[QTextFormat.Property]  # value = <Property.ImageName: 20480>
        ImageQuality: typing.ClassVar[QTextFormat.Property]  # value = <Property.ImageQuality: 20500>
        ImageTitle: typing.ClassVar[QTextFormat.Property]  # value = <Property.ImageTitle: 20481>
        ImageWidth: typing.ClassVar[QTextFormat.Property]  # value = <Property.ImageWidth: 20496>
        IsAnchor: typing.ClassVar[QTextFormat.Property]  # value = <Property.IsAnchor: 8240>
        LayoutDirection: typing.ClassVar[QTextFormat.Property]  # value = <Property.LayoutDirection: 2049>
        LineHeight: typing.ClassVar[QTextFormat.Property]  # value = <Property.LineHeight: 4168>
        LineHeightType: typing.ClassVar[QTextFormat.Property]  # value = <Property.LineHeightType: 4169>
        ListIndent: typing.ClassVar[QTextFormat.Property]  # value = <Property.ListIndent: 12289>
        ListNumberPrefix: typing.ClassVar[QTextFormat.Property]  # value = <Property.ListNumberPrefix: 12290>
        ListNumberSuffix: typing.ClassVar[QTextFormat.Property]  # value = <Property.ListNumberSuffix: 12291>
        ListStart: typing.ClassVar[QTextFormat.Property]  # value = <Property.ListStart: 12292>
        ListStyle: typing.ClassVar[QTextFormat.Property]  # value = <Property.ListStyle: 12288>
        ObjectIndex: typing.ClassVar[QTextFormat.Property]  # value = <Property.ObjectIndex: 0>
        ObjectType: typing.ClassVar[QTextFormat.Property]  # value = <Property.ObjectType: 12032>
        OldFontFamily: typing.ClassVar[QTextFormat.Property]  # value = <Property.OldFontFamily: 8192>
        OldFontLetterSpacingType: typing.ClassVar[QTextFormat.Property]  # value = <Property.OldFontLetterSpacingType: 8243>
        OldFontStretch: typing.ClassVar[QTextFormat.Property]  # value = <Property.OldFontStretch: 8244>
        OldTextUnderlineColor: typing.ClassVar[QTextFormat.Property]  # value = <Property.OldTextUnderlineColor: 8208>
        OutlinePen: typing.ClassVar[QTextFormat.Property]  # value = <Property.OutlinePen: 2064>
        PageBreakPolicy: typing.ClassVar[QTextFormat.Property]  # value = <Property.PageBreakPolicy: 28672>
        TabPositions: typing.ClassVar[QTextFormat.Property]  # value = <Property.TabPositions: 4149>
        TableBorderCollapse: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableBorderCollapse: 16645>
        TableCellBottomBorder: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellBottomBorder: 18455>
        TableCellBottomBorderBrush: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellBottomBorderBrush: 18463>
        TableCellBottomBorderStyle: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellBottomBorderStyle: 18459>
        TableCellBottomPadding: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellBottomPadding: 18451>
        TableCellColumnSpan: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellColumnSpan: 18449>
        TableCellLeftBorder: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellLeftBorder: 18456>
        TableCellLeftBorderBrush: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellLeftBorderBrush: 18464>
        TableCellLeftBorderStyle: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellLeftBorderStyle: 18460>
        TableCellLeftPadding: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellLeftPadding: 18452>
        TableCellPadding: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellPadding: 16643>
        TableCellRightBorder: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellRightBorder: 18457>
        TableCellRightBorderBrush: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellRightBorderBrush: 18465>
        TableCellRightBorderStyle: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellRightBorderStyle: 18461>
        TableCellRightPadding: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellRightPadding: 18453>
        TableCellRowSpan: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellRowSpan: 18448>
        TableCellSpacing: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellSpacing: 16642>
        TableCellTopBorder: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellTopBorder: 18454>
        TableCellTopBorderBrush: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellTopBorderBrush: 18462>
        TableCellTopBorderStyle: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellTopBorderStyle: 18458>
        TableCellTopPadding: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableCellTopPadding: 18450>
        TableColumnWidthConstraints: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableColumnWidthConstraints: 16641>
        TableColumns: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableColumns: 16640>
        TableHeaderRowCount: typing.ClassVar[QTextFormat.Property]  # value = <Property.TableHeaderRowCount: 16644>
        TextBaselineOffset: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextBaselineOffset: 8231>
        TextIndent: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextIndent: 4148>
        TextOutline: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextOutline: 8226>
        TextSubScriptBaseline: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextSubScriptBaseline: 8230>
        TextSuperScriptBaseline: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextSuperScriptBaseline: 8229>
        TextToolTip: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextToolTip: 8228>
        TextUnderlineColor: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextUnderlineColor: 8224>
        TextUnderlineStyle: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextUnderlineStyle: 8227>
        TextVerticalAlignment: typing.ClassVar[QTextFormat.Property]  # value = <Property.TextVerticalAlignment: 8225>
        UserProperty: typing.ClassVar[QTextFormat.Property]  # value = <Property.UserProperty: 1048576>
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
    def boolProperty(*args, **kwargs):
        ...
    @staticmethod
    def brushProperty(*args, **kwargs):
        ...
    @staticmethod
    def clearBackground(*args, **kwargs):
        ...
    @staticmethod
    def clearForeground(*args, **kwargs):
        ...
    @staticmethod
    def clearProperty(*args, **kwargs):
        ...
    @staticmethod
    def colorProperty(*args, **kwargs):
        ...
    @staticmethod
    def doubleProperty(*args, **kwargs):
        ...
    @staticmethod
    def foreground(*args, **kwargs):
        ...
    @staticmethod
    def hasProperty(*args, **kwargs):
        ...
    @staticmethod
    def intProperty(*args, **kwargs):
        ...
    @staticmethod
    def isBlockFormat(*args, **kwargs):
        ...
    @staticmethod
    def isCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isFrameFormat(*args, **kwargs):
        ...
    @staticmethod
    def isImageFormat(*args, **kwargs):
        ...
    @staticmethod
    def isListFormat(*args, **kwargs):
        ...
    @staticmethod
    def isTableCellFormat(*args, **kwargs):
        ...
    @staticmethod
    def isTableFormat(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def layoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def lengthProperty(*args, **kwargs):
        ...
    @staticmethod
    def lengthVectorProperty(*args, **kwargs):
        ...
    @staticmethod
    def merge(*args, **kwargs):
        ...
    @staticmethod
    def objectIndex(*args, **kwargs):
        ...
    @staticmethod
    def objectType(*args, **kwargs):
        ...
    @staticmethod
    def penProperty(*args, **kwargs):
        ...
    @staticmethod
    def properties(*args, **kwargs):
        ...
    @staticmethod
    def property(*args, **kwargs):
        ...
    @staticmethod
    def propertyCount(*args, **kwargs):
        ...
    @staticmethod
    def setBackground(*args, **kwargs):
        ...
    @staticmethod
    def setForeground(*args, **kwargs):
        ...
    @staticmethod
    def setLayoutDirection(*args, **kwargs):
        ...
    @staticmethod
    def setObjectIndex(*args, **kwargs):
        ...
    @staticmethod
    def setObjectType(*args, **kwargs):
        ...
    @staticmethod
    def setProperty(*args, **kwargs):
        ...
    @staticmethod
    def stringProperty(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toBlockFormat(*args, **kwargs):
        ...
    @staticmethod
    def toCharFormat(*args, **kwargs):
        ...
    @staticmethod
    def toFrameFormat(*args, **kwargs):
        ...
    @staticmethod
    def toImageFormat(*args, **kwargs):
        ...
    @staticmethod
    def toListFormat(*args, **kwargs):
        ...
    @staticmethod
    def toTableCellFormat(*args, **kwargs):
        ...
    @staticmethod
    def toTableFormat(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
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
class QTextFragment(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def charFormat(*args, **kwargs):
        ...
    @staticmethod
    def charFormatIndex(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def glyphRuns(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
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
class QTextFrame(QTextObject):
    class iterator(PyQt6.sip.simplewrapper):
        __hash__: typing.ClassVar[None] = None
        @staticmethod
        def atEnd(*args, **kwargs):
            ...
        @staticmethod
        def currentBlock(*args, **kwargs):
            ...
        @staticmethod
        def currentFrame(*args, **kwargs):
            ...
        @staticmethod
        def parentFrame(*args, **kwargs):
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
        def __iadd__(self, value):
            """
            Return self+=value.
            """
        def __isub__(self, value):
            """
            Return self-=value.
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
    @staticmethod
    def begin(*args, **kwargs):
        ...
    @staticmethod
    def childFrames(*args, **kwargs):
        ...
    @staticmethod
    def end(*args, **kwargs):
        ...
    @staticmethod
    def firstCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def firstPosition(*args, **kwargs):
        ...
    @staticmethod
    def frameFormat(*args, **kwargs):
        ...
    @staticmethod
    def lastCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def lastPosition(*args, **kwargs):
        ...
    @staticmethod
    def parentFrame(*args, **kwargs):
        ...
    @staticmethod
    def setFrameFormat(*args, **kwargs):
        ...
class QTextFrameFormat(QTextFormat):
    class BorderStyle(enum.Enum):
        BorderStyle_Dashed: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Dashed: 2>
        BorderStyle_DotDash: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_DotDash: 5>
        BorderStyle_DotDotDash: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_DotDotDash: 6>
        BorderStyle_Dotted: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Dotted: 1>
        BorderStyle_Double: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Double: 4>
        BorderStyle_Groove: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Groove: 7>
        BorderStyle_Inset: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Inset: 9>
        BorderStyle_None: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_None: 0>
        BorderStyle_Outset: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Outset: 10>
        BorderStyle_Ridge: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Ridge: 8>
        BorderStyle_Solid: typing.ClassVar[QTextFrameFormat.BorderStyle]  # value = <BorderStyle.BorderStyle_Solid: 3>
    class Position(enum.Enum):
        FloatLeft: typing.ClassVar[QTextFrameFormat.Position]  # value = <Position.FloatLeft: 1>
        FloatRight: typing.ClassVar[QTextFrameFormat.Position]  # value = <Position.FloatRight: 2>
        InFlow: typing.ClassVar[QTextFrameFormat.Position]  # value = <Position.InFlow: 0>
    @staticmethod
    def border(*args, **kwargs):
        ...
    @staticmethod
    def borderBrush(*args, **kwargs):
        ...
    @staticmethod
    def borderStyle(*args, **kwargs):
        ...
    @staticmethod
    def bottomMargin(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def leftMargin(*args, **kwargs):
        ...
    @staticmethod
    def margin(*args, **kwargs):
        ...
    @staticmethod
    def padding(*args, **kwargs):
        ...
    @staticmethod
    def pageBreakPolicy(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def rightMargin(*args, **kwargs):
        ...
    @staticmethod
    def setBorder(*args, **kwargs):
        ...
    @staticmethod
    def setBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def setBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def setBottomMargin(*args, **kwargs):
        ...
    @staticmethod
    def setHeight(*args, **kwargs):
        ...
    @staticmethod
    def setLeftMargin(*args, **kwargs):
        ...
    @staticmethod
    def setMargin(*args, **kwargs):
        ...
    @staticmethod
    def setPadding(*args, **kwargs):
        ...
    @staticmethod
    def setPageBreakPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
    @staticmethod
    def setRightMargin(*args, **kwargs):
        ...
    @staticmethod
    def setTopMargin(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def topMargin(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
class QTextImageFormat(QTextCharFormat):
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def quality(*args, **kwargs):
        ...
    @staticmethod
    def setHeight(*args, **kwargs):
        ...
    @staticmethod
    def setName(*args, **kwargs):
        ...
    @staticmethod
    def setQuality(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
class QTextInlineObject(PyQt6.sip.simplewrapper):
    @staticmethod
    def ascent(*args, **kwargs):
        ...
    @staticmethod
    def descent(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def formatIndex(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def setAscent(*args, **kwargs):
        ...
    @staticmethod
    def setDescent(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def textDirection(*args, **kwargs):
        ...
    @staticmethod
    def textPosition(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
class QTextItem(PyQt6.sip.simplewrapper):
    class RenderFlag(enum.Flag):
        Overline: typing.ClassVar[QTextItem.RenderFlag]  # value = <RenderFlag.Overline: 16>
        RightToLeft: typing.ClassVar[QTextItem.RenderFlag]  # value = <RenderFlag.RightToLeft: 1>
        StrikeOut: typing.ClassVar[QTextItem.RenderFlag]  # value = <RenderFlag.StrikeOut: 64>
        Underline: typing.ClassVar[QTextItem.RenderFlag]  # value = <RenderFlag.Underline: 32>
    @staticmethod
    def ascent(*args, **kwargs):
        ...
    @staticmethod
    def descent(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def renderFlags(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
class QTextLayout(PyQt6.sip.simplewrapper):
    class CursorMode(enum.Enum):
        SkipCharacters: typing.ClassVar[QTextLayout.CursorMode]  # value = <CursorMode.SkipCharacters: 0>
        SkipWords: typing.ClassVar[QTextLayout.CursorMode]  # value = <CursorMode.SkipWords: 1>
    class FormatRange(PyQt6.sip.simplewrapper):
        __hash__: typing.ClassVar[None] = None
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
    class GlyphRunRetrievalFlag(enum.Enum):
        RetrieveAll: typing.ClassVar[QTextLayout.GlyphRunRetrievalFlag]  # value = <GlyphRunRetrievalFlag.RetrieveAll: 65535>
        RetrieveGlyphIndexes: typing.ClassVar[QTextLayout.GlyphRunRetrievalFlag]  # value = <GlyphRunRetrievalFlag.RetrieveGlyphIndexes: 1>
        RetrieveGlyphPositions: typing.ClassVar[QTextLayout.GlyphRunRetrievalFlag]  # value = <GlyphRunRetrievalFlag.RetrieveGlyphPositions: 2>
        RetrieveString: typing.ClassVar[QTextLayout.GlyphRunRetrievalFlag]  # value = <GlyphRunRetrievalFlag.RetrieveString: 8>
        RetrieveStringIndexes: typing.ClassVar[QTextLayout.GlyphRunRetrievalFlag]  # value = <GlyphRunRetrievalFlag.RetrieveStringIndexes: 4>
    @staticmethod
    def beginLayout(*args, **kwargs):
        ...
    @staticmethod
    def boundingRect(*args, **kwargs):
        ...
    @staticmethod
    def cacheEnabled(*args, **kwargs):
        ...
    @staticmethod
    def clearFormats(*args, **kwargs):
        ...
    @staticmethod
    def clearLayout(*args, **kwargs):
        ...
    @staticmethod
    def createLine(*args, **kwargs):
        ...
    @staticmethod
    def cursorMoveStyle(*args, **kwargs):
        ...
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def drawCursor(*args, **kwargs):
        ...
    @staticmethod
    def endLayout(*args, **kwargs):
        ...
    @staticmethod
    def font(*args, **kwargs):
        ...
    @staticmethod
    def formats(*args, **kwargs):
        ...
    @staticmethod
    def glyphRuns(*args, **kwargs):
        ...
    @staticmethod
    def isValidCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def leftCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def lineAt(*args, **kwargs):
        ...
    @staticmethod
    def lineCount(*args, **kwargs):
        ...
    @staticmethod
    def lineForTextPosition(*args, **kwargs):
        ...
    @staticmethod
    def maximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def minimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def nextCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def preeditAreaPosition(*args, **kwargs):
        ...
    @staticmethod
    def preeditAreaText(*args, **kwargs):
        ...
    @staticmethod
    def previousCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def rightCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def setCacheEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setCursorMoveStyle(*args, **kwargs):
        ...
    @staticmethod
    def setFont(*args, **kwargs):
        ...
    @staticmethod
    def setFormats(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
    @staticmethod
    def setPreeditArea(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setTextOption(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def textOption(*args, **kwargs):
        ...
class QTextLength(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        FixedLength: typing.ClassVar[QTextLength.Type]  # value = <Type.FixedLength: 1>
        PercentageLength: typing.ClassVar[QTextLength.Type]  # value = <Type.PercentageLength: 2>
        VariableLength: typing.ClassVar[QTextLength.Type]  # value = <Type.VariableLength: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def rawValue(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
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
class QTextLine(PyQt6.sip.simplewrapper):
    class CursorPosition(enum.Enum):
        CursorBetweenCharacters: typing.ClassVar[QTextLine.CursorPosition]  # value = <CursorPosition.CursorBetweenCharacters: 0>
        CursorOnCharacter: typing.ClassVar[QTextLine.CursorPosition]  # value = <CursorPosition.CursorOnCharacter: 1>
    class Edge(enum.Enum):
        Leading: typing.ClassVar[QTextLine.Edge]  # value = <Edge.Leading: 0>
        Trailing: typing.ClassVar[QTextLine.Edge]  # value = <Edge.Trailing: 1>
    @staticmethod
    def ascent(*args, **kwargs):
        ...
    @staticmethod
    def cursorToX(*args, **kwargs):
        ...
    @staticmethod
    def descent(*args, **kwargs):
        ...
    @staticmethod
    def draw(*args, **kwargs):
        ...
    @staticmethod
    def glyphRuns(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def horizontalAdvance(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def leading(*args, **kwargs):
        ...
    @staticmethod
    def leadingIncluded(*args, **kwargs):
        ...
    @staticmethod
    def lineNumber(*args, **kwargs):
        ...
    @staticmethod
    def naturalTextRect(*args, **kwargs):
        ...
    @staticmethod
    def naturalTextWidth(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def rect(*args, **kwargs):
        ...
    @staticmethod
    def setLeadingIncluded(*args, **kwargs):
        ...
    @staticmethod
    def setLineWidth(*args, **kwargs):
        ...
    @staticmethod
    def setNumColumns(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
    @staticmethod
    def textLength(*args, **kwargs):
        ...
    @staticmethod
    def textStart(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def xToCursor(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
class QTextList(QTextBlockGroup):
    @staticmethod
    def add(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def item(*args, **kwargs):
        ...
    @staticmethod
    def itemNumber(*args, **kwargs):
        ...
    @staticmethod
    def itemText(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def removeItem(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QTextListFormat(QTextFormat):
    class Style(enum.Enum):
        ListCircle: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListCircle: -2>
        ListDecimal: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListDecimal: -4>
        ListDisc: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListDisc: -1>
        ListLowerAlpha: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListLowerAlpha: -5>
        ListLowerRoman: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListLowerRoman: -7>
        ListSquare: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListSquare: -3>
        ListUpperAlpha: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListUpperAlpha: -6>
        ListUpperRoman: typing.ClassVar[QTextListFormat.Style]  # value = <Style.ListUpperRoman: -8>
    @staticmethod
    def indent(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def numberPrefix(*args, **kwargs):
        ...
    @staticmethod
    def numberSuffix(*args, **kwargs):
        ...
    @staticmethod
    def setIndent(*args, **kwargs):
        ...
    @staticmethod
    def setNumberPrefix(*args, **kwargs):
        ...
    @staticmethod
    def setNumberSuffix(*args, **kwargs):
        ...
    @staticmethod
    def setStart(*args, **kwargs):
        ...
    @staticmethod
    def setStyle(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
    @staticmethod
    def style(*args, **kwargs):
        ...
class QTextObject(PyQt6.QtCore.QObject):
    @staticmethod
    def document(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def formatIndex(*args, **kwargs):
        ...
    @staticmethod
    def objectIndex(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
class QTextObjectInterface(PyQt6.sip.simplewrapper):
    @staticmethod
    def drawObject(*args, **kwargs):
        ...
    @staticmethod
    def intrinsicSize(*args, **kwargs):
        ...
class QTextOption(PyQt6.sip.simplewrapper):
    class Flag(enum.Flag):
        AddSpaceForLineAndParagraphSeparators: typing.ClassVar[QTextOption.Flag]  # value = <Flag.AddSpaceForLineAndParagraphSeparators: 4>
        IncludeTrailingSpaces: typing.ClassVar[QTextOption.Flag]  # value = <Flag.IncludeTrailingSpaces: 2147483648>
        ShowDocumentTerminator: typing.ClassVar[QTextOption.Flag]  # value = <Flag.ShowDocumentTerminator: 16>
        ShowLineAndParagraphSeparators: typing.ClassVar[QTextOption.Flag]  # value = <Flag.ShowLineAndParagraphSeparators: 2>
        ShowTabsAndSpaces: typing.ClassVar[QTextOption.Flag]  # value = <Flag.ShowTabsAndSpaces: 1>
        SuppressColors: typing.ClassVar[QTextOption.Flag]  # value = <Flag.SuppressColors: 8>
    class Tab(PyQt6.sip.simplewrapper):
        __hash__: typing.ClassVar[None] = None
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
    class TabType(enum.Enum):
        CenterTab: typing.ClassVar[QTextOption.TabType]  # value = <TabType.CenterTab: 2>
        DelimiterTab: typing.ClassVar[QTextOption.TabType]  # value = <TabType.DelimiterTab: 3>
        LeftTab: typing.ClassVar[QTextOption.TabType]  # value = <TabType.LeftTab: 0>
        RightTab: typing.ClassVar[QTextOption.TabType]  # value = <TabType.RightTab: 1>
    class WrapMode(enum.Enum):
        ManualWrap: typing.ClassVar[QTextOption.WrapMode]  # value = <WrapMode.ManualWrap: 2>
        NoWrap: typing.ClassVar[QTextOption.WrapMode]  # value = <WrapMode.NoWrap: 0>
        WordWrap: typing.ClassVar[QTextOption.WrapMode]  # value = <WrapMode.WordWrap: 1>
        WrapAnywhere: typing.ClassVar[QTextOption.WrapMode]  # value = <WrapMode.WrapAnywhere: 3>
        WrapAtWordBoundaryOrAnywhere: typing.ClassVar[QTextOption.WrapMode]  # value = <WrapMode.WrapAtWordBoundaryOrAnywhere: 4>
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setTabArray(*args, **kwargs):
        ...
    @staticmethod
    def setTabStopDistance(*args, **kwargs):
        ...
    @staticmethod
    def setTabs(*args, **kwargs):
        ...
    @staticmethod
    def setTextDirection(*args, **kwargs):
        ...
    @staticmethod
    def setUseDesignMetrics(*args, **kwargs):
        ...
    @staticmethod
    def setWrapMode(*args, **kwargs):
        ...
    @staticmethod
    def tabArray(*args, **kwargs):
        ...
    @staticmethod
    def tabStopDistance(*args, **kwargs):
        ...
    @staticmethod
    def tabs(*args, **kwargs):
        ...
    @staticmethod
    def textDirection(*args, **kwargs):
        ...
    @staticmethod
    def useDesignMetrics(*args, **kwargs):
        ...
    @staticmethod
    def wrapMode(*args, **kwargs):
        ...
class QTextTable(QTextFrame):
    @staticmethod
    def appendColumns(*args, **kwargs):
        ...
    @staticmethod
    def appendRows(*args, **kwargs):
        ...
    @staticmethod
    def cellAt(*args, **kwargs):
        ...
    @staticmethod
    def columns(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def insertColumns(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def mergeCells(*args, **kwargs):
        ...
    @staticmethod
    def removeColumns(*args, **kwargs):
        ...
    @staticmethod
    def removeRows(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def rowEnd(*args, **kwargs):
        ...
    @staticmethod
    def rowStart(*args, **kwargs):
        ...
    @staticmethod
    def rows(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def splitCell(*args, **kwargs):
        ...
class QTextTableCell(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def column(*args, **kwargs):
        ...
    @staticmethod
    def columnSpan(*args, **kwargs):
        ...
    @staticmethod
    def firstCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastCursorPosition(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def rowSpan(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def tableCellFormatIndex(*args, **kwargs):
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
class QTextTableCellFormat(QTextCharFormat):
    @staticmethod
    def bottomBorder(*args, **kwargs):
        ...
    @staticmethod
    def bottomBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def bottomBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def bottomPadding(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def leftBorder(*args, **kwargs):
        ...
    @staticmethod
    def leftBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def leftBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def leftPadding(*args, **kwargs):
        ...
    @staticmethod
    def rightBorder(*args, **kwargs):
        ...
    @staticmethod
    def rightBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def rightBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def rightPadding(*args, **kwargs):
        ...
    @staticmethod
    def setBorder(*args, **kwargs):
        ...
    @staticmethod
    def setBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def setBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def setBottomBorder(*args, **kwargs):
        ...
    @staticmethod
    def setBottomBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def setBottomBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def setBottomPadding(*args, **kwargs):
        ...
    @staticmethod
    def setLeftBorder(*args, **kwargs):
        ...
    @staticmethod
    def setLeftBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def setLeftBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def setLeftPadding(*args, **kwargs):
        ...
    @staticmethod
    def setPadding(*args, **kwargs):
        ...
    @staticmethod
    def setRightBorder(*args, **kwargs):
        ...
    @staticmethod
    def setRightBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def setRightBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def setRightPadding(*args, **kwargs):
        ...
    @staticmethod
    def setTopBorder(*args, **kwargs):
        ...
    @staticmethod
    def setTopBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def setTopBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def setTopPadding(*args, **kwargs):
        ...
    @staticmethod
    def topBorder(*args, **kwargs):
        ...
    @staticmethod
    def topBorderBrush(*args, **kwargs):
        ...
    @staticmethod
    def topBorderStyle(*args, **kwargs):
        ...
    @staticmethod
    def topPadding(*args, **kwargs):
        ...
class QTextTableFormat(QTextFrameFormat):
    @staticmethod
    def alignment(*args, **kwargs):
        ...
    @staticmethod
    def borderCollapse(*args, **kwargs):
        ...
    @staticmethod
    def cellPadding(*args, **kwargs):
        ...
    @staticmethod
    def cellSpacing(*args, **kwargs):
        ...
    @staticmethod
    def clearColumnWidthConstraints(*args, **kwargs):
        ...
    @staticmethod
    def columnWidthConstraints(*args, **kwargs):
        ...
    @staticmethod
    def columns(*args, **kwargs):
        ...
    @staticmethod
    def headerRowCount(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def setAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setBorderCollapse(*args, **kwargs):
        ...
    @staticmethod
    def setCellPadding(*args, **kwargs):
        ...
    @staticmethod
    def setCellSpacing(*args, **kwargs):
        ...
    @staticmethod
    def setColumnWidthConstraints(*args, **kwargs):
        ...
    @staticmethod
    def setColumns(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderRowCount(*args, **kwargs):
        ...
class QTouchEvent(QPointerEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def isBeginEvent(*args, **kwargs):
        ...
    @staticmethod
    def isEndEvent(*args, **kwargs):
        ...
    @staticmethod
    def isUpdateEvent(*args, **kwargs):
        ...
    @staticmethod
    def target(*args, **kwargs):
        ...
    @staticmethod
    def touchPointStates(*args, **kwargs):
        ...
class QTransform(PyQt6.sip.simplewrapper):
    class TransformationType(enum.Enum):
        TxNone: typing.ClassVar[QTransform.TransformationType]  # value = <TransformationType.TxNone: 0>
        TxProject: typing.ClassVar[QTransform.TransformationType]  # value = <TransformationType.TxProject: 16>
        TxRotate: typing.ClassVar[QTransform.TransformationType]  # value = <TransformationType.TxRotate: 4>
        TxScale: typing.ClassVar[QTransform.TransformationType]  # value = <TransformationType.TxScale: 2>
        TxShear: typing.ClassVar[QTransform.TransformationType]  # value = <TransformationType.TxShear: 8>
        TxTranslate: typing.ClassVar[QTransform.TransformationType]  # value = <TransformationType.TxTranslate: 1>
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def adjoint(*args, **kwargs):
        ...
    @staticmethod
    def determinant(*args, **kwargs):
        ...
    @staticmethod
    def dx(*args, **kwargs):
        ...
    @staticmethod
    def dy(*args, **kwargs):
        ...
    @staticmethod
    def fromScale(*args, **kwargs):
        ...
    @staticmethod
    def fromTranslate(*args, **kwargs):
        ...
    @staticmethod
    def inverted(*args, **kwargs):
        ...
    @staticmethod
    def isAffine(*args, **kwargs):
        ...
    @staticmethod
    def isIdentity(*args, **kwargs):
        ...
    @staticmethod
    def isInvertible(*args, **kwargs):
        ...
    @staticmethod
    def isRotating(*args, **kwargs):
        ...
    @staticmethod
    def isScaling(*args, **kwargs):
        ...
    @staticmethod
    def isTranslating(*args, **kwargs):
        ...
    @staticmethod
    def m11(*args, **kwargs):
        ...
    @staticmethod
    def m12(*args, **kwargs):
        ...
    @staticmethod
    def m13(*args, **kwargs):
        ...
    @staticmethod
    def m21(*args, **kwargs):
        ...
    @staticmethod
    def m22(*args, **kwargs):
        ...
    @staticmethod
    def m23(*args, **kwargs):
        ...
    @staticmethod
    def m31(*args, **kwargs):
        ...
    @staticmethod
    def m32(*args, **kwargs):
        ...
    @staticmethod
    def m33(*args, **kwargs):
        ...
    @staticmethod
    def map(*args, **kwargs):
        ...
    @staticmethod
    def mapRect(*args, **kwargs):
        ...
    @staticmethod
    def mapToPolygon(*args, **kwargs):
        ...
    @staticmethod
    def quadToQuad(*args, **kwargs):
        ...
    @staticmethod
    def quadToSquare(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def rotate(*args, **kwargs):
        ...
    @staticmethod
    def rotateRadians(*args, **kwargs):
        ...
    @staticmethod
    def scale(*args, **kwargs):
        ...
    @staticmethod
    def setMatrix(*args, **kwargs):
        ...
    @staticmethod
    def shear(*args, **kwargs):
        ...
    @staticmethod
    def squareToQuad(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
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
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imatmul__(self, value):
        """
        Return self@=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __matmul__(self, value):
        """
        Return self@value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __rmatmul__(self, value):
        """
        Return value@self.
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __rtruediv__(self, value):
        """
        Return value/self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
    def __truediv__(self, value):
        """
        Return self/value.
        """
class QUndoCommand(PyQt6.sip.wrapper):
    @staticmethod
    def actionText(*args, **kwargs):
        ...
    @staticmethod
    def child(*args, **kwargs):
        ...
    @staticmethod
    def childCount(*args, **kwargs):
        ...
    @staticmethod
    def id(*args, **kwargs):
        ...
    @staticmethod
    def isObsolete(*args, **kwargs):
        ...
    @staticmethod
    def mergeWith(*args, **kwargs):
        ...
    @staticmethod
    def redo(*args, **kwargs):
        ...
    @staticmethod
    def setObsolete(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def undo(*args, **kwargs):
        ...
class QUndoGroup(PyQt6.QtCore.QObject):
    @staticmethod
    def activeStack(*args, **kwargs):
        ...
    @staticmethod
    def activeStackChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def addStack(*args, **kwargs):
        ...
    @staticmethod
    def canRedo(*args, **kwargs):
        ...
    @staticmethod
    def canRedoChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def canUndo(*args, **kwargs):
        ...
    @staticmethod
    def canUndoChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def cleanChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def createRedoAction(*args, **kwargs):
        ...
    @staticmethod
    def createUndoAction(*args, **kwargs):
        ...
    @staticmethod
    def indexChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def isClean(*args, **kwargs):
        ...
    @staticmethod
    def redo(*args, **kwargs):
        ...
    @staticmethod
    def redoText(*args, **kwargs):
        ...
    @staticmethod
    def redoTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def removeStack(*args, **kwargs):
        ...
    @staticmethod
    def setActiveStack(*args, **kwargs):
        ...
    @staticmethod
    def stacks(*args, **kwargs):
        ...
    @staticmethod
    def undo(*args, **kwargs):
        ...
    @staticmethod
    def undoText(*args, **kwargs):
        ...
    @staticmethod
    def undoTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QUndoStack(PyQt6.QtCore.QObject):
    @staticmethod
    def beginMacro(*args, **kwargs):
        ...
    @staticmethod
    def canRedo(*args, **kwargs):
        ...
    @staticmethod
    def canRedoChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def canUndo(*args, **kwargs):
        ...
    @staticmethod
    def canUndoChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def cleanChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def cleanIndex(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def command(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def createRedoAction(*args, **kwargs):
        ...
    @staticmethod
    def createUndoAction(*args, **kwargs):
        ...
    @staticmethod
    def endMacro(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def indexChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def isClean(*args, **kwargs):
        ...
    @staticmethod
    def push(*args, **kwargs):
        ...
    @staticmethod
    def redo(*args, **kwargs):
        ...
    @staticmethod
    def redoText(*args, **kwargs):
        ...
    @staticmethod
    def redoTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def resetClean(*args, **kwargs):
        ...
    @staticmethod
    def setActive(*args, **kwargs):
        ...
    @staticmethod
    def setClean(*args, **kwargs):
        ...
    @staticmethod
    def setIndex(*args, **kwargs):
        ...
    @staticmethod
    def setUndoLimit(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def undo(*args, **kwargs):
        ...
    @staticmethod
    def undoLimit(*args, **kwargs):
        ...
    @staticmethod
    def undoText(*args, **kwargs):
        ...
    @staticmethod
    def undoTextChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
class QValidator(PyQt6.QtCore.QObject):
    class State(enum.Enum):
        Acceptable: typing.ClassVar[QValidator.State]  # value = <State.Acceptable: 2>
        Intermediate: typing.ClassVar[QValidator.State]  # value = <State.Intermediate: 1>
        Invalid: typing.ClassVar[QValidator.State]  # value = <State.Invalid: 0>
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
    def fixup(*args, **kwargs):
        ...
    @staticmethod
    def locale(*args, **kwargs):
        ...
    @staticmethod
    def setLocale(*args, **kwargs):
        ...
    @staticmethod
    def validate(*args, **kwargs):
        ...
class QVector2D(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def distanceToLine(*args, **kwargs):
        ...
    @staticmethod
    def distanceToPoint(*args, **kwargs):
        ...
    @staticmethod
    def dotProduct(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def lengthSquared(*args, **kwargs):
        ...
    @staticmethod
    def normalize(*args, **kwargs):
        ...
    @staticmethod
    def normalized(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def toPoint(*args, **kwargs):
        ...
    @staticmethod
    def toPointF(*args, **kwargs):
        ...
    @staticmethod
    def toVector3D(*args, **kwargs):
        ...
    @staticmethod
    def toVector4D(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __neg__(self):
        """
        -self
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __rtruediv__(self, value):
        """
        Return value/self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
    def __truediv__(self, value):
        """
        Return self/value.
        """
class QVector3D(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def crossProduct(*args, **kwargs):
        ...
    @staticmethod
    def distanceToLine(*args, **kwargs):
        ...
    @staticmethod
    def distanceToPlane(*args, **kwargs):
        ...
    @staticmethod
    def distanceToPoint(*args, **kwargs):
        ...
    @staticmethod
    def dotProduct(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def lengthSquared(*args, **kwargs):
        ...
    @staticmethod
    def normal(*args, **kwargs):
        ...
    @staticmethod
    def normalize(*args, **kwargs):
        ...
    @staticmethod
    def normalized(*args, **kwargs):
        ...
    @staticmethod
    def project(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def setZ(*args, **kwargs):
        ...
    @staticmethod
    def toPoint(*args, **kwargs):
        ...
    @staticmethod
    def toPointF(*args, **kwargs):
        ...
    @staticmethod
    def toVector2D(*args, **kwargs):
        ...
    @staticmethod
    def toVector4D(*args, **kwargs):
        ...
    @staticmethod
    def unproject(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
    @staticmethod
    def z(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __neg__(self):
        """
        -self
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __rtruediv__(self, value):
        """
        Return value/self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
    def __truediv__(self, value):
        """
        Return self/value.
        """
class QVector4D(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def dotProduct(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def lengthSquared(*args, **kwargs):
        ...
    @staticmethod
    def normalize(*args, **kwargs):
        ...
    @staticmethod
    def normalized(*args, **kwargs):
        ...
    @staticmethod
    def setW(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def setZ(*args, **kwargs):
        ...
    @staticmethod
    def toPoint(*args, **kwargs):
        ...
    @staticmethod
    def toPointF(*args, **kwargs):
        ...
    @staticmethod
    def toVector2D(*args, **kwargs):
        ...
    @staticmethod
    def toVector2DAffine(*args, **kwargs):
        ...
    @staticmethod
    def toVector3D(*args, **kwargs):
        ...
    @staticmethod
    def toVector3DAffine(*args, **kwargs):
        ...
    @staticmethod
    def w(*args, **kwargs):
        ...
    @staticmethod
    def x(*args, **kwargs):
        ...
    @staticmethod
    def y(*args, **kwargs):
        ...
    @staticmethod
    def z(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __eq__(self, value):
        """
        Return self==value.
        """
    def __ge__(self, value):
        """
        Return self>=value.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __gt__(self, value):
        """
        Return self>value.
        """
    def __iadd__(self, value):
        """
        Return self+=value.
        """
    def __imul__(self, value):
        """
        Return self*=value.
        """
    def __isub__(self, value):
        """
        Return self-=value.
        """
    def __itruediv__(self, value):
        """
        Return self/=value.
        """
    def __le__(self, value):
        """
        Return self<=value.
        """
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __mul__(self, value):
        """
        Return self*value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __neg__(self):
        """
        -self
        """
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __rtruediv__(self, value):
        """
        Return value/self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
    def __truediv__(self, value):
        """
        Return self/value.
        """
class QWhatsThisClickedEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def href(*args, **kwargs):
        ...
class QWheelEvent(QSinglePointEvent):
    @staticmethod
    def angleDelta(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def inverted(*args, **kwargs):
        ...
    @staticmethod
    def isBeginEvent(*args, **kwargs):
        ...
    @staticmethod
    def isEndEvent(*args, **kwargs):
        ...
    @staticmethod
    def isUpdateEvent(*args, **kwargs):
        ...
    @staticmethod
    def phase(*args, **kwargs):
        ...
    @staticmethod
    def pixelDelta(*args, **kwargs):
        ...
class QWindow(PyQt6.QtCore.QObject, QSurface):
    class AncestorMode(enum.Enum):
        ExcludeTransients: typing.ClassVar[QWindow.AncestorMode]  # value = <AncestorMode.ExcludeTransients: 0>
        IncludeTransients: typing.ClassVar[QWindow.AncestorMode]  # value = <AncestorMode.IncludeTransients: 1>
    class Visibility(enum.Enum):
        AutomaticVisibility: typing.ClassVar[QWindow.Visibility]  # value = <Visibility.AutomaticVisibility: 1>
        FullScreen: typing.ClassVar[QWindow.Visibility]  # value = <Visibility.FullScreen: 5>
        Hidden: typing.ClassVar[QWindow.Visibility]  # value = <Visibility.Hidden: 0>
        Maximized: typing.ClassVar[QWindow.Visibility]  # value = <Visibility.Maximized: 4>
        Minimized: typing.ClassVar[QWindow.Visibility]  # value = <Visibility.Minimized: 3>
        Windowed: typing.ClassVar[QWindow.Visibility]  # value = <Visibility.Windowed: 2>
    @staticmethod
    def activeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def alert(*args, **kwargs):
        ...
    @staticmethod
    def baseSize(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def closeEvent(*args, **kwargs):
        ...
    @staticmethod
    def contentOrientation(*args, **kwargs):
        ...
    @staticmethod
    def contentOrientationChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def create(*args, **kwargs):
        ...
    @staticmethod
    def cursor(*args, **kwargs):
        ...
    @staticmethod
    def destroy(*args, **kwargs):
        ...
    @staticmethod
    def devicePixelRatio(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def exposeEvent(*args, **kwargs):
        ...
    @staticmethod
    def filePath(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def focusInEvent(*args, **kwargs):
        ...
    @staticmethod
    def focusObject(*args, **kwargs):
        ...
    @staticmethod
    def focusObjectChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def focusOutEvent(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def frameGeometry(*args, **kwargs):
        ...
    @staticmethod
    def frameMargins(*args, **kwargs):
        ...
    @staticmethod
    def framePosition(*args, **kwargs):
        ...
    @staticmethod
    def fromWinId(*args, **kwargs):
        ...
    @staticmethod
    def geometry(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def heightChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def hide(*args, **kwargs):
        ...
    @staticmethod
    def hideEvent(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def isAncestorOf(*args, **kwargs):
        ...
    @staticmethod
    def isExposed(*args, **kwargs):
        ...
    @staticmethod
    def isModal(*args, **kwargs):
        ...
    @staticmethod
    def isTopLevel(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def keyPressEvent(*args, **kwargs):
        ...
    @staticmethod
    def keyReleaseEvent(*args, **kwargs):
        ...
    @staticmethod
    def lower(*args, **kwargs):
        ...
    @staticmethod
    def mapFromGlobal(*args, **kwargs):
        ...
    @staticmethod
    def mapToGlobal(*args, **kwargs):
        ...
    @staticmethod
    def mask(*args, **kwargs):
        ...
    @staticmethod
    def maximumHeight(*args, **kwargs):
        ...
    @staticmethod
    def maximumHeightChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def maximumSize(*args, **kwargs):
        ...
    @staticmethod
    def maximumWidth(*args, **kwargs):
        ...
    @staticmethod
    def maximumWidthChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def minimumHeight(*args, **kwargs):
        ...
    @staticmethod
    def minimumHeightChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def minimumSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumWidth(*args, **kwargs):
        ...
    @staticmethod
    def minimumWidthChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def modality(*args, **kwargs):
        ...
    @staticmethod
    def modalityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def moveEvent(*args, **kwargs):
        ...
    @staticmethod
    def nativeEvent(*args, **kwargs):
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
    def paintEvent(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def raise_(*args, **kwargs):
        ...
    @staticmethod
    def reportContentOrientationChange(*args, **kwargs):
        ...
    @staticmethod
    def requestActivate(*args, **kwargs):
        ...
    @staticmethod
    def requestUpdate(*args, **kwargs):
        ...
    @staticmethod
    def requestedFormat(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def resizeEvent(*args, **kwargs):
        ...
    @staticmethod
    def screen(*args, **kwargs):
        ...
    @staticmethod
    def screenChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def setBaseSize(*args, **kwargs):
        ...
    @staticmethod
    def setCursor(*args, **kwargs):
        ...
    @staticmethod
    def setFilePath(*args, **kwargs):
        ...
    @staticmethod
    def setFlag(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setFormat(*args, **kwargs):
        ...
    @staticmethod
    def setFramePosition(*args, **kwargs):
        ...
    @staticmethod
    def setGeometry(*args, **kwargs):
        ...
    @staticmethod
    def setHeight(*args, **kwargs):
        ...
    @staticmethod
    def setIcon(*args, **kwargs):
        ...
    @staticmethod
    def setKeyboardGrabEnabled(*args, **kwargs):
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
    def setModality(*args, **kwargs):
        ...
    @staticmethod
    def setMouseGrabEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setOpacity(*args, **kwargs):
        ...
    @staticmethod
    def setParent(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
    @staticmethod
    def setScreen(*args, **kwargs):
        ...
    @staticmethod
    def setSizeIncrement(*args, **kwargs):
        ...
    @staticmethod
    def setSurfaceType(*args, **kwargs):
        ...
    @staticmethod
    def setTitle(*args, **kwargs):
        ...
    @staticmethod
    def setTransientParent(*args, **kwargs):
        ...
    @staticmethod
    def setVisibility(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def setWindowState(*args, **kwargs):
        ...
    @staticmethod
    def setWindowStates(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
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
    def sizeIncrement(*args, **kwargs):
        ...
    @staticmethod
    def startSystemMove(*args, **kwargs):
        ...
    @staticmethod
    def startSystemResize(*args, **kwargs):
        ...
    @staticmethod
    def surfaceType(*args, **kwargs):
        ...
    @staticmethod
    def tabletEvent(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
    @staticmethod
    def touchEvent(*args, **kwargs):
        ...
    @staticmethod
    def transientParent(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def unsetCursor(*args, **kwargs):
        ...
    @staticmethod
    def visibility(*args, **kwargs):
        ...
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
    def wheelEvent(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
    @staticmethod
    def widthChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
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
    def winId(*args, **kwargs):
        ...
    @staticmethod
    def windowState(*args, **kwargs):
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
    @staticmethod
    def windowStates(*args, **kwargs):
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
    def x(*args, **kwargs):
        ...
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
    def y(*args, **kwargs):
        ...
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
class QWindowStateChangeEvent(PyQt6.QtCore.QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def oldState(*args, **kwargs):
        ...
def qAlpha(*args, **kwargs):
    ...
def qBlue(*args, **kwargs):
    ...
def qFuzzyCompare(*args, **kwargs):
    ...
def qGray(*args, **kwargs):
    ...
def qGreen(*args, **kwargs):
    ...
def qPixelFormatAlpha(*args, **kwargs):
    ...
def qPixelFormatCmyk(*args, **kwargs):
    ...
def qPixelFormatGrayscale(*args, **kwargs):
    ...
def qPixelFormatHsl(*args, **kwargs):
    ...
def qPixelFormatHsv(*args, **kwargs):
    ...
def qPixelFormatRgba(*args, **kwargs):
    ...
def qPixelFormatYuv(*args, **kwargs):
    ...
def qPremultiply(*args, **kwargs):
    ...
def qRed(*args, **kwargs):
    ...
def qRgb(*args, **kwargs):
    ...
def qRgba(*args, **kwargs):
    ...
def qRgba64(*args, **kwargs):
    ...
def qUnpremultiply(*args, **kwargs):
    ...
def qt_set_sequence_auto_mnemonic(*args, **kwargs):
    ...
