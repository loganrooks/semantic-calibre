import PyQt6.QtCore
import PyQt6.QtGui
import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['QSvgGenerator', 'QSvgRenderer', 'QtSvg']
class QSvgGenerator(PyQt6.QtGui.QPaintDevice):
    class SvgVersion(enum.Enum):
        Svg11: typing.ClassVar[QSvgGenerator.SvgVersion]  # value = <SvgVersion.Svg11: 1>
        SvgTiny12: typing.ClassVar[QSvgGenerator.SvgVersion]  # value = <SvgVersion.SvgTiny12: 0>
    @staticmethod
    def description(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def outputDevice(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def resolution(*args, **kwargs):
        ...
    @staticmethod
    def setDescription(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setOutputDevice(*args, **kwargs):
        ...
    @staticmethod
    def setResolution(*args, **kwargs):
        ...
    @staticmethod
    def setSize(*args, **kwargs):
        ...
    @staticmethod
    def setTitle(*args, **kwargs):
        ...
    @staticmethod
    def setViewBox(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def svgVersion(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
    @staticmethod
    def viewBox(*args, **kwargs):
        ...
    @staticmethod
    def viewBoxF(*args, **kwargs):
        ...
class QSvgRenderer(PyQt6.QtCore.QObject):
    @staticmethod
    def animated(*args, **kwargs):
        ...
    @staticmethod
    def animationDuration(*args, **kwargs):
        ...
    @staticmethod
    def aspectRatioMode(*args, **kwargs):
        ...
    @staticmethod
    def boundsOnElement(*args, **kwargs):
        ...
    @staticmethod
    def currentFrame(*args, **kwargs):
        ...
    @staticmethod
    def defaultSize(*args, **kwargs):
        ...
    @staticmethod
    def elementExists(*args, **kwargs):
        ...
    @staticmethod
    def framesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def isAnimationEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def render(*args, **kwargs):
        ...
    @staticmethod
    def repaintNeeded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setAnimationEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setAspectRatioMode(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentFrame(*args, **kwargs):
        ...
    @staticmethod
    def setFramesPerSecond(*args, **kwargs):
        ...
    @staticmethod
    def setOptions(*args, **kwargs):
        ...
    @staticmethod
    def setViewBox(*args, **kwargs):
        ...
    @staticmethod
    def transformForElement(*args, **kwargs):
        ...
    @staticmethod
    def viewBox(*args, **kwargs):
        ...
    @staticmethod
    def viewBoxF(*args, **kwargs):
        ...
class QtSvg(PyQt6.sip.simplewrapper):
    class Option(enum.Enum):
        NoOption: typing.ClassVar[QtSvg.Option]  # value = <Option.NoOption: 0>
        Tiny12FeaturesOnly: typing.ClassVar[QtSvg.Option]  # value = <Option.Tiny12FeaturesOnly: 1>
