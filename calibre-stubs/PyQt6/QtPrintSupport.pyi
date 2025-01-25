import PyQt6.QtGui
import PyQt6.QtWidgets
import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['QAbstractPrintDialog', 'QPageSetupDialog', 'QPrintDialog', 'QPrintEngine', 'QPrintPreviewDialog', 'QPrintPreviewWidget', 'QPrinter', 'QPrinterInfo']
class QAbstractPrintDialog(PyQt6.QtWidgets.QDialog):
    class PrintDialogOption(enum.Flag):
        PrintCollateCopies: typing.ClassVar[QAbstractPrintDialog.PrintDialogOption]  # value = <PrintDialogOption.PrintCollateCopies: 16>
        PrintCurrentPage: typing.ClassVar[QAbstractPrintDialog.PrintDialogOption]  # value = <PrintDialogOption.PrintCurrentPage: 64>
        PrintPageRange: typing.ClassVar[QAbstractPrintDialog.PrintDialogOption]  # value = <PrintDialogOption.PrintPageRange: 4>
        PrintSelection: typing.ClassVar[QAbstractPrintDialog.PrintDialogOption]  # value = <PrintDialogOption.PrintSelection: 2>
        PrintShowPageSize: typing.ClassVar[QAbstractPrintDialog.PrintDialogOption]  # value = <PrintDialogOption.PrintShowPageSize: 8>
        PrintToFile: typing.ClassVar[QAbstractPrintDialog.PrintDialogOption]  # value = <PrintDialogOption.PrintToFile: 1>
    class PrintRange(enum.Enum):
        AllPages: typing.ClassVar[QAbstractPrintDialog.PrintRange]  # value = <PrintRange.AllPages: 0>
        CurrentPage: typing.ClassVar[QAbstractPrintDialog.PrintRange]  # value = <PrintRange.CurrentPage: 3>
        PageRange: typing.ClassVar[QAbstractPrintDialog.PrintRange]  # value = <PrintRange.PageRange: 2>
        Selection: typing.ClassVar[QAbstractPrintDialog.PrintRange]  # value = <PrintRange.Selection: 1>
    @staticmethod
    def fromPage(*args, **kwargs):
        ...
    @staticmethod
    def maxPage(*args, **kwargs):
        ...
    @staticmethod
    def minPage(*args, **kwargs):
        ...
    @staticmethod
    def printRange(*args, **kwargs):
        ...
    @staticmethod
    def printer(*args, **kwargs):
        ...
    @staticmethod
    def setFromTo(*args, **kwargs):
        ...
    @staticmethod
    def setMinMax(*args, **kwargs):
        ...
    @staticmethod
    def setOptionTabs(*args, **kwargs):
        ...
    @staticmethod
    def setPrintRange(*args, **kwargs):
        ...
    @staticmethod
    def toPage(*args, **kwargs):
        ...
class QPageSetupDialog(PyQt6.QtWidgets.QDialog):
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def printer(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
class QPrintDialog(QAbstractPrintDialog):
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
    def done(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
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
class QPrintEngine(PyQt6.sip.simplewrapper):
    class PrintEnginePropertyKey(enum.Enum):
        PPK_CollateCopies: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_CollateCopies: 0>
        PPK_ColorMode: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_ColorMode: 1>
        PPK_CopyCount: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_CopyCount: 24>
        PPK_Creator: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_Creator: 2>
        PPK_CustomBase: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_CustomBase: 65280>
        PPK_CustomPaperSize: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_CustomPaperSize: 22>
        PPK_DocumentName: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_DocumentName: 3>
        PPK_Duplex: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_Duplex: 20>
        PPK_FontEmbedding: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_FontEmbedding: 19>
        PPK_FullPage: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_FullPage: 4>
        PPK_NumberOfCopies: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_NumberOfCopies: 5>
        PPK_Orientation: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_Orientation: 6>
        PPK_OutputFileName: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_OutputFileName: 7>
        PPK_PageMargins: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PageMargins: 23>
        PPK_PageOrder: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PageOrder: 8>
        PPK_PageRect: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PageRect: 9>
        PPK_PageSize: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PageSize: 10>
        PPK_PaperName: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PaperName: 26>
        PPK_PaperRect: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PaperRect: 11>
        PPK_PaperSource: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PaperSource: 12>
        PPK_PaperSources: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PaperSources: 21>
        PPK_PrinterName: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PrinterName: 13>
        PPK_PrinterProgram: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_PrinterProgram: 14>
        PPK_QPageLayout: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_QPageLayout: 29>
        PPK_QPageMargins: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_QPageMargins: 28>
        PPK_QPageSize: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_QPageSize: 27>
        PPK_Resolution: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_Resolution: 15>
        PPK_SelectionOption: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_SelectionOption: 16>
        PPK_SupportedResolutions: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_SupportedResolutions: 17>
        PPK_SupportsMultipleCopies: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_SupportsMultipleCopies: 25>
        PPK_WindowsPageSize: typing.ClassVar[QPrintEngine.PrintEnginePropertyKey]  # value = <PrintEnginePropertyKey.PPK_WindowsPageSize: 18>
    @staticmethod
    def abort(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def newPage(*args, **kwargs):
        ...
    @staticmethod
    def printerState(*args, **kwargs):
        ...
    @staticmethod
    def property(*args, **kwargs):
        ...
    @staticmethod
    def setProperty(*args, **kwargs):
        ...
class QPrintPreviewDialog(PyQt6.QtWidgets.QDialog):
    @staticmethod
    def done(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def paintRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def printer(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
class QPrintPreviewWidget(PyQt6.QtWidgets.QWidget):
    class ViewMode(enum.Enum):
        AllPagesView: typing.ClassVar[QPrintPreviewWidget.ViewMode]  # value = <ViewMode.AllPagesView: 2>
        FacingPagesView: typing.ClassVar[QPrintPreviewWidget.ViewMode]  # value = <ViewMode.FacingPagesView: 1>
        SinglePageView: typing.ClassVar[QPrintPreviewWidget.ViewMode]  # value = <ViewMode.SinglePageView: 0>
    class ZoomMode(enum.Enum):
        CustomZoom: typing.ClassVar[QPrintPreviewWidget.ZoomMode]  # value = <ZoomMode.CustomZoom: 0>
        FitInView: typing.ClassVar[QPrintPreviewWidget.ZoomMode]  # value = <ZoomMode.FitInView: 2>
        FitToWidth: typing.ClassVar[QPrintPreviewWidget.ZoomMode]  # value = <ZoomMode.FitToWidth: 1>
    @staticmethod
    def currentPage(*args, **kwargs):
        ...
    @staticmethod
    def fitInView(*args, **kwargs):
        ...
    @staticmethod
    def fitToWidth(*args, **kwargs):
        ...
    @staticmethod
    def orientation(*args, **kwargs):
        ...
    @staticmethod
    def pageCount(*args, **kwargs):
        ...
    @staticmethod
    def paintRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def previewChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def print(*args, **kwargs):
        ...
    @staticmethod
    def setAllPagesViewMode(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentPage(*args, **kwargs):
        ...
    @staticmethod
    def setFacingPagesViewMode(*args, **kwargs):
        ...
    @staticmethod
    def setLandscapeOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setPortraitOrientation(*args, **kwargs):
        ...
    @staticmethod
    def setSinglePageViewMode(*args, **kwargs):
        ...
    @staticmethod
    def setViewMode(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def setZoomFactor(*args, **kwargs):
        ...
    @staticmethod
    def setZoomMode(*args, **kwargs):
        ...
    @staticmethod
    def updatePreview(*args, **kwargs):
        ...
    @staticmethod
    def viewMode(*args, **kwargs):
        ...
    @staticmethod
    def zoomFactor(*args, **kwargs):
        ...
    @staticmethod
    def zoomIn(*args, **kwargs):
        ...
    @staticmethod
    def zoomMode(*args, **kwargs):
        ...
    @staticmethod
    def zoomOut(*args, **kwargs):
        ...
class QPrinter(PyQt6.QtGui.QPagedPaintDevice):
    class ColorMode(enum.Enum):
        Color: typing.ClassVar[QPrinter.ColorMode]  # value = <ColorMode.Color: 1>
        GrayScale: typing.ClassVar[QPrinter.ColorMode]  # value = <ColorMode.GrayScale: 0>
    class DuplexMode(enum.Enum):
        DuplexAuto: typing.ClassVar[QPrinter.DuplexMode]  # value = <DuplexMode.DuplexAuto: 1>
        DuplexLongSide: typing.ClassVar[QPrinter.DuplexMode]  # value = <DuplexMode.DuplexLongSide: 2>
        DuplexNone: typing.ClassVar[QPrinter.DuplexMode]  # value = <DuplexMode.DuplexNone: 0>
        DuplexShortSide: typing.ClassVar[QPrinter.DuplexMode]  # value = <DuplexMode.DuplexShortSide: 3>
    class OutputFormat(enum.Enum):
        NativeFormat: typing.ClassVar[QPrinter.OutputFormat]  # value = <OutputFormat.NativeFormat: 0>
        PdfFormat: typing.ClassVar[QPrinter.OutputFormat]  # value = <OutputFormat.PdfFormat: 1>
    class PageOrder(enum.Enum):
        FirstPageFirst: typing.ClassVar[QPrinter.PageOrder]  # value = <PageOrder.FirstPageFirst: 0>
        LastPageFirst: typing.ClassVar[QPrinter.PageOrder]  # value = <PageOrder.LastPageFirst: 1>
    class PaperSource(enum.Enum):
        Auto: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.Auto: 6>
        Cassette: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.Cassette: 11>
        CustomSource: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.CustomSource: 14>
        Envelope: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.Envelope: 4>
        EnvelopeManual: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.EnvelopeManual: 5>
        FormSource: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.FormSource: 12>
        LargeCapacity: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.LargeCapacity: 10>
        LargeFormat: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.LargeFormat: 9>
        Lower: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.Lower: 1>
        Manual: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.Manual: 3>
        MaxPageSource: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.MaxPageSource: 13>
        Middle: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.Middle: 2>
        OnlyOne: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.OnlyOne: 0>
        SmallFormat: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.SmallFormat: 8>
        Tractor: typing.ClassVar[QPrinter.PaperSource]  # value = <PaperSource.Tractor: 7>
    class PrintRange(enum.Enum):
        AllPages: typing.ClassVar[QPrinter.PrintRange]  # value = <PrintRange.AllPages: 0>
        CurrentPage: typing.ClassVar[QPrinter.PrintRange]  # value = <PrintRange.CurrentPage: 3>
        PageRange: typing.ClassVar[QPrinter.PrintRange]  # value = <PrintRange.PageRange: 2>
        Selection: typing.ClassVar[QPrinter.PrintRange]  # value = <PrintRange.Selection: 1>
    class PrinterMode(enum.Enum):
        HighResolution: typing.ClassVar[QPrinter.PrinterMode]  # value = <PrinterMode.HighResolution: 2>
        PrinterResolution: typing.ClassVar[QPrinter.PrinterMode]  # value = <PrinterMode.PrinterResolution: 1>
        ScreenResolution: typing.ClassVar[QPrinter.PrinterMode]  # value = <PrinterMode.ScreenResolution: 0>
    class PrinterState(enum.Enum):
        Aborted: typing.ClassVar[QPrinter.PrinterState]  # value = <PrinterState.Aborted: 2>
        Active: typing.ClassVar[QPrinter.PrinterState]  # value = <PrinterState.Active: 1>
        Error: typing.ClassVar[QPrinter.PrinterState]  # value = <PrinterState.Error: 3>
        Idle: typing.ClassVar[QPrinter.PrinterState]  # value = <PrinterState.Idle: 0>
    class Unit(enum.Enum):
        Cicero: typing.ClassVar[QPrinter.Unit]  # value = <Unit.Cicero: 5>
        DevicePixel: typing.ClassVar[QPrinter.Unit]  # value = <Unit.DevicePixel: 6>
        Didot: typing.ClassVar[QPrinter.Unit]  # value = <Unit.Didot: 4>
        Inch: typing.ClassVar[QPrinter.Unit]  # value = <Unit.Inch: 2>
        Millimeter: typing.ClassVar[QPrinter.Unit]  # value = <Unit.Millimeter: 0>
        Pica: typing.ClassVar[QPrinter.Unit]  # value = <Unit.Pica: 3>
        Point: typing.ClassVar[QPrinter.Unit]  # value = <Unit.Point: 1>
    @staticmethod
    def abort(*args, **kwargs):
        ...
    @staticmethod
    def collateCopies(*args, **kwargs):
        ...
    @staticmethod
    def colorMode(*args, **kwargs):
        ...
    @staticmethod
    def copyCount(*args, **kwargs):
        ...
    @staticmethod
    def creator(*args, **kwargs):
        ...
    @staticmethod
    def docName(*args, **kwargs):
        ...
    @staticmethod
    def duplex(*args, **kwargs):
        ...
    @staticmethod
    def fontEmbeddingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def fromPage(*args, **kwargs):
        ...
    @staticmethod
    def fullPage(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def metric(*args, **kwargs):
        ...
    @staticmethod
    def newPage(*args, **kwargs):
        ...
    @staticmethod
    def outputFileName(*args, **kwargs):
        ...
    @staticmethod
    def outputFormat(*args, **kwargs):
        ...
    @staticmethod
    def pageOrder(*args, **kwargs):
        ...
    @staticmethod
    def pageRect(*args, **kwargs):
        ...
    @staticmethod
    def paintEngine(*args, **kwargs):
        ...
    @staticmethod
    def paperRect(*args, **kwargs):
        ...
    @staticmethod
    def paperSource(*args, **kwargs):
        ...
    @staticmethod
    def pdfVersion(*args, **kwargs):
        ...
    @staticmethod
    def printEngine(*args, **kwargs):
        ...
    @staticmethod
    def printProgram(*args, **kwargs):
        ...
    @staticmethod
    def printRange(*args, **kwargs):
        ...
    @staticmethod
    def printerName(*args, **kwargs):
        ...
    @staticmethod
    def printerSelectionOption(*args, **kwargs):
        ...
    @staticmethod
    def printerState(*args, **kwargs):
        ...
    @staticmethod
    def resolution(*args, **kwargs):
        ...
    @staticmethod
    def setCollateCopies(*args, **kwargs):
        ...
    @staticmethod
    def setColorMode(*args, **kwargs):
        ...
    @staticmethod
    def setCopyCount(*args, **kwargs):
        ...
    @staticmethod
    def setCreator(*args, **kwargs):
        ...
    @staticmethod
    def setDocName(*args, **kwargs):
        ...
    @staticmethod
    def setDuplex(*args, **kwargs):
        ...
    @staticmethod
    def setEngines(*args, **kwargs):
        ...
    @staticmethod
    def setFontEmbeddingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setFromTo(*args, **kwargs):
        ...
    @staticmethod
    def setFullPage(*args, **kwargs):
        ...
    @staticmethod
    def setOutputFileName(*args, **kwargs):
        ...
    @staticmethod
    def setOutputFormat(*args, **kwargs):
        ...
    @staticmethod
    def setPageOrder(*args, **kwargs):
        ...
    @staticmethod
    def setPaperSource(*args, **kwargs):
        ...
    @staticmethod
    def setPdfVersion(*args, **kwargs):
        ...
    @staticmethod
    def setPrintProgram(*args, **kwargs):
        ...
    @staticmethod
    def setPrintRange(*args, **kwargs):
        ...
    @staticmethod
    def setPrinterName(*args, **kwargs):
        ...
    @staticmethod
    def setPrinterSelectionOption(*args, **kwargs):
        ...
    @staticmethod
    def setResolution(*args, **kwargs):
        ...
    @staticmethod
    def supportedResolutions(*args, **kwargs):
        ...
    @staticmethod
    def supportsMultipleCopies(*args, **kwargs):
        ...
    @staticmethod
    def toPage(*args, **kwargs):
        ...
class QPrinterInfo(PyQt6.sip.simplewrapper):
    @staticmethod
    def availablePrinterNames(*args, **kwargs):
        ...
    @staticmethod
    def availablePrinters(*args, **kwargs):
        ...
    @staticmethod
    def defaultColorMode(*args, **kwargs):
        ...
    @staticmethod
    def defaultDuplexMode(*args, **kwargs):
        ...
    @staticmethod
    def defaultPageSize(*args, **kwargs):
        ...
    @staticmethod
    def defaultPrinter(*args, **kwargs):
        ...
    @staticmethod
    def defaultPrinterName(*args, **kwargs):
        ...
    @staticmethod
    def description(*args, **kwargs):
        ...
    @staticmethod
    def isDefault(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isRemote(*args, **kwargs):
        ...
    @staticmethod
    def location(*args, **kwargs):
        ...
    @staticmethod
    def makeAndModel(*args, **kwargs):
        ...
    @staticmethod
    def maximumPhysicalPageSize(*args, **kwargs):
        ...
    @staticmethod
    def minimumPhysicalPageSize(*args, **kwargs):
        ...
    @staticmethod
    def printerInfo(*args, **kwargs):
        ...
    @staticmethod
    def printerName(*args, **kwargs):
        ...
    @staticmethod
    def state(*args, **kwargs):
        ...
    @staticmethod
    def supportedColorModes(*args, **kwargs):
        ...
    @staticmethod
    def supportedDuplexModes(*args, **kwargs):
        ...
    @staticmethod
    def supportedPageSizes(*args, **kwargs):
        ...
    @staticmethod
    def supportedResolutions(*args, **kwargs):
        ...
    @staticmethod
    def supportsCustomPageSizes(*args, **kwargs):
        ...
