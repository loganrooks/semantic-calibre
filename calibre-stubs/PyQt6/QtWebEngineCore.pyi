import PyQt6.QtCore
import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['PYQT_WEBENGINE_VERSION', 'PYQT_WEBENGINE_VERSION_STR', 'QWebEngineCertificateError', 'QWebEngineClientCertificateSelection', 'QWebEngineClientCertificateStore', 'QWebEngineContextMenuRequest', 'QWebEngineCookieStore', 'QWebEngineDesktopMediaRequest', 'QWebEngineDownloadRequest', 'QWebEngineFileSystemAccessRequest', 'QWebEngineFindTextResult', 'QWebEngineFullScreenRequest', 'QWebEngineGlobalSettings', 'QWebEngineHistory', 'QWebEngineHistoryItem', 'QWebEngineHistoryModel', 'QWebEngineHttpRequest', 'QWebEngineLoadingInfo', 'QWebEngineNavigationRequest', 'QWebEngineNewWindowRequest', 'QWebEngineNotification', 'QWebEnginePage', 'QWebEngineProfile', 'QWebEngineQuotaRequest', 'QWebEngineRegisterProtocolHandlerRequest', 'QWebEngineScript', 'QWebEngineScriptCollection', 'QWebEngineSettings', 'QWebEngineUrlRequestInfo', 'QWebEngineUrlRequestInterceptor', 'QWebEngineUrlRequestJob', 'QWebEngineUrlScheme', 'QWebEngineUrlSchemeHandler', 'QWebEngineWebAuthPinRequest', 'QWebEngineWebAuthUxRequest', 'qWebEngineChromiumSecurityPatchVersion', 'qWebEngineChromiumVersion', 'qWebEngineGetDomainAndRegistry', 'qWebEngineProcessName', 'qWebEngineVersion']
class QWebEngineCertificateError(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        CertificateAuthorityInvalid: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateAuthorityInvalid: -202>
        CertificateCommonNameInvalid: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateCommonNameInvalid: -200>
        CertificateContainsErrors: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateContainsErrors: -203>
        CertificateDateInvalid: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateDateInvalid: -201>
        CertificateInvalid: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateInvalid: -207>
        CertificateKnownInterceptionBlocked: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateKnownInterceptionBlocked: -217>
        CertificateNameConstraintViolation: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateNameConstraintViolation: -212>
        CertificateNoRevocationMechanism: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateNoRevocationMechanism: -204>
        CertificateNonUniqueName: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateNonUniqueName: -210>
        CertificateRevoked: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateRevoked: -206>
        CertificateSymantecLegacy: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateSymantecLegacy: -215>
        CertificateTransparencyRequired: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateTransparencyRequired: -214>
        CertificateUnableToCheckRevocation: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateUnableToCheckRevocation: -205>
        CertificateValidityTooLong: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateValidityTooLong: -213>
        CertificateWeakKey: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateWeakKey: -211>
        CertificateWeakSignatureAlgorithm: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.CertificateWeakSignatureAlgorithm: -208>
        SslObsoleteVersion: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.SslObsoleteVersion: -218>
        SslPinnedKeyNotInCertificateChain: typing.ClassVar[QWebEngineCertificateError.Type]  # value = <Type.SslPinnedKeyNotInCertificateChain: -150>
    @staticmethod
    def acceptCertificate(*args, **kwargs):
        ...
    @staticmethod
    def certificateChain(*args, **kwargs):
        ...
    @staticmethod
    def defer(*args, **kwargs):
        ...
    @staticmethod
    def description(*args, **kwargs):
        ...
    @staticmethod
    def isOverridable(*args, **kwargs):
        ...
    @staticmethod
    def rejectCertificate(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
        ...
class QWebEngineClientCertificateSelection(PyQt6.sip.simplewrapper):
    @staticmethod
    def certificates(*args, **kwargs):
        ...
    @staticmethod
    def host(*args, **kwargs):
        ...
    @staticmethod
    def select(*args, **kwargs):
        ...
    @staticmethod
    def selectNone(*args, **kwargs):
        ...
class QWebEngineClientCertificateStore(PyQt6.sip.simplewrapper):
    @staticmethod
    def add(*args, **kwargs):
        ...
    @staticmethod
    def certificates(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
class QWebEngineContextMenuRequest(PyQt6.QtCore.QObject):
    class EditFlag(enum.Flag):
        CanCopy: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanCopy: 8>
        CanCut: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanCut: 4>
        CanDelete: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanDelete: 32>
        CanEditRichly: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanEditRichly: 256>
        CanPaste: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanPaste: 16>
        CanRedo: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanRedo: 2>
        CanSelectAll: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanSelectAll: 64>
        CanTranslate: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanTranslate: 128>
        CanUndo: typing.ClassVar[QWebEngineContextMenuRequest.EditFlag]  # value = <EditFlag.CanUndo: 1>
    class MediaFlag(enum.Flag):
        MediaCanPrint: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaCanPrint: 256>
        MediaCanRotate: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaCanRotate: 512>
        MediaCanSave: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaCanSave: 16>
        MediaCanToggleControls: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaCanToggleControls: 64>
        MediaControls: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaControls: 128>
        MediaHasAudio: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaHasAudio: 32>
        MediaInError: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaInError: 1>
        MediaLoop: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaLoop: 8>
        MediaMuted: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaMuted: 4>
        MediaPaused: typing.ClassVar[QWebEngineContextMenuRequest.MediaFlag]  # value = <MediaFlag.MediaPaused: 2>
    class MediaType(enum.Enum):
        MediaTypeAudio: typing.ClassVar[QWebEngineContextMenuRequest.MediaType]  # value = <MediaType.MediaTypeAudio: 3>
        MediaTypeCanvas: typing.ClassVar[QWebEngineContextMenuRequest.MediaType]  # value = <MediaType.MediaTypeCanvas: 4>
        MediaTypeFile: typing.ClassVar[QWebEngineContextMenuRequest.MediaType]  # value = <MediaType.MediaTypeFile: 5>
        MediaTypeImage: typing.ClassVar[QWebEngineContextMenuRequest.MediaType]  # value = <MediaType.MediaTypeImage: 1>
        MediaTypeNone: typing.ClassVar[QWebEngineContextMenuRequest.MediaType]  # value = <MediaType.MediaTypeNone: 0>
        MediaTypePlugin: typing.ClassVar[QWebEngineContextMenuRequest.MediaType]  # value = <MediaType.MediaTypePlugin: 6>
        MediaTypeVideo: typing.ClassVar[QWebEngineContextMenuRequest.MediaType]  # value = <MediaType.MediaTypeVideo: 2>
    @staticmethod
    def editFlags(*args, **kwargs):
        ...
    @staticmethod
    def isAccepted(*args, **kwargs):
        ...
    @staticmethod
    def isContentEditable(*args, **kwargs):
        ...
    @staticmethod
    def linkText(*args, **kwargs):
        ...
    @staticmethod
    def linkUrl(*args, **kwargs):
        ...
    @staticmethod
    def mediaFlags(*args, **kwargs):
        ...
    @staticmethod
    def mediaType(*args, **kwargs):
        ...
    @staticmethod
    def mediaUrl(*args, **kwargs):
        ...
    @staticmethod
    def misspelledWord(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def selectedText(*args, **kwargs):
        ...
    @staticmethod
    def setAccepted(*args, **kwargs):
        ...
    @staticmethod
    def spellCheckerSuggestions(*args, **kwargs):
        ...
class QWebEngineCookieStore(PyQt6.QtCore.QObject):
    class FilterRequest(PyQt6.sip.simplewrapper):
        pass
    @staticmethod
    def cookieAdded(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def cookieRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def deleteAllCookies(*args, **kwargs):
        ...
    @staticmethod
    def deleteCookie(*args, **kwargs):
        ...
    @staticmethod
    def deleteSessionCookies(*args, **kwargs):
        ...
    @staticmethod
    def loadAllCookies(*args, **kwargs):
        ...
    @staticmethod
    def setCookie(*args, **kwargs):
        ...
    @staticmethod
    def setCookieFilter(*args, **kwargs):
        ...
class QWebEngineDesktopMediaRequest(PyQt6.sip.simplewrapper):
    @staticmethod
    def cancel(*args, **kwargs):
        ...
    @staticmethod
    def screensModel(*args, **kwargs):
        ...
    @staticmethod
    def selectScreen(*args, **kwargs):
        ...
    @staticmethod
    def selectWindow(*args, **kwargs):
        ...
    @staticmethod
    def windowsModel(*args, **kwargs):
        ...
class QWebEngineDownloadRequest(PyQt6.QtCore.QObject):
    class DownloadInterruptReason(enum.Enum):
        FileAccessDenied: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileAccessDenied: 2>
        FileBlocked: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileBlocked: 11>
        FileFailed: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileFailed: 1>
        FileHashMismatch: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileHashMismatch: 14>
        FileNameTooLong: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileNameTooLong: 5>
        FileNoSpace: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileNoSpace: 3>
        FileSecurityCheckFailed: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileSecurityCheckFailed: 12>
        FileTooLarge: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileTooLarge: 6>
        FileTooShort: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileTooShort: 13>
        FileTransientError: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileTransientError: 10>
        FileVirusInfected: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.FileVirusInfected: 7>
        NetworkDisconnected: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.NetworkDisconnected: 22>
        NetworkFailed: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.NetworkFailed: 20>
        NetworkInvalidRequest: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.NetworkInvalidRequest: 24>
        NetworkServerDown: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.NetworkServerDown: 23>
        NetworkTimeout: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.NetworkTimeout: 21>
        NoReason: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.NoReason: 0>
        ServerBadContent: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.ServerBadContent: 33>
        ServerCertProblem: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.ServerCertProblem: 35>
        ServerFailed: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.ServerFailed: 30>
        ServerForbidden: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.ServerForbidden: 36>
        ServerUnauthorized: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.ServerUnauthorized: 34>
        ServerUnreachable: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.ServerUnreachable: 37>
        UserCanceled: typing.ClassVar[QWebEngineDownloadRequest.DownloadInterruptReason]  # value = <DownloadInterruptReason.UserCanceled: 40>
    class DownloadState(enum.Enum):
        DownloadCancelled: typing.ClassVar[QWebEngineDownloadRequest.DownloadState]  # value = <DownloadState.DownloadCancelled: 3>
        DownloadCompleted: typing.ClassVar[QWebEngineDownloadRequest.DownloadState]  # value = <DownloadState.DownloadCompleted: 2>
        DownloadInProgress: typing.ClassVar[QWebEngineDownloadRequest.DownloadState]  # value = <DownloadState.DownloadInProgress: 1>
        DownloadInterrupted: typing.ClassVar[QWebEngineDownloadRequest.DownloadState]  # value = <DownloadState.DownloadInterrupted: 4>
        DownloadRequested: typing.ClassVar[QWebEngineDownloadRequest.DownloadState]  # value = <DownloadState.DownloadRequested: 0>
    class SavePageFormat(enum.Enum):
        CompleteHtmlSaveFormat: typing.ClassVar[QWebEngineDownloadRequest.SavePageFormat]  # value = <SavePageFormat.CompleteHtmlSaveFormat: 1>
        MimeHtmlSaveFormat: typing.ClassVar[QWebEngineDownloadRequest.SavePageFormat]  # value = <SavePageFormat.MimeHtmlSaveFormat: 2>
        SingleHtmlSaveFormat: typing.ClassVar[QWebEngineDownloadRequest.SavePageFormat]  # value = <SavePageFormat.SingleHtmlSaveFormat: 0>
        UnknownSaveFormat: typing.ClassVar[QWebEngineDownloadRequest.SavePageFormat]  # value = <SavePageFormat.UnknownSaveFormat: -1>
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def cancel(*args, **kwargs):
        ...
    @staticmethod
    def downloadDirectory(*args, **kwargs):
        ...
    @staticmethod
    def downloadDirectoryChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def downloadFileName(*args, **kwargs):
        ...
    @staticmethod
    def downloadFileNameChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def id(*args, **kwargs):
        ...
    @staticmethod
    def interruptReason(*args, **kwargs):
        ...
    @staticmethod
    def interruptReasonChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def interruptReasonString(*args, **kwargs):
        ...
    @staticmethod
    def isFinished(*args, **kwargs):
        ...
    @staticmethod
    def isFinishedChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def isPaused(*args, **kwargs):
        ...
    @staticmethod
    def isPausedChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def isSavePageDownload(*args, **kwargs):
        ...
    @staticmethod
    def mimeType(*args, **kwargs):
        ...
    @staticmethod
    def page(*args, **kwargs):
        ...
    @staticmethod
    def pause(*args, **kwargs):
        ...
    @staticmethod
    def receivedBytes(*args, **kwargs):
        ...
    @staticmethod
    def receivedBytesChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def resume(*args, **kwargs):
        ...
    @staticmethod
    def savePageFormat(*args, **kwargs):
        ...
    @staticmethod
    def savePageFormatChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setDownloadDirectory(*args, **kwargs):
        ...
    @staticmethod
    def setDownloadFileName(*args, **kwargs):
        ...
    @staticmethod
    def setSavePageFormat(*args, **kwargs):
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
    def suggestedFileName(*args, **kwargs):
        ...
    @staticmethod
    def totalBytes(*args, **kwargs):
        ...
    @staticmethod
    def totalBytesChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def url(*args, **kwargs):
        ...
class QWebEngineFileSystemAccessRequest(PyQt6.sip.simplewrapper):
    class AccessFlag(enum.Flag):
        Read: typing.ClassVar[QWebEngineFileSystemAccessRequest.AccessFlag]  # value = <AccessFlag.Read: 1>
        Write: typing.ClassVar[QWebEngineFileSystemAccessRequest.AccessFlag]  # value = <AccessFlag.Write: 2>
    class HandleType(enum.Enum):
        Directory: typing.ClassVar[QWebEngineFileSystemAccessRequest.HandleType]  # value = <HandleType.Directory: 1>
        File: typing.ClassVar[QWebEngineFileSystemAccessRequest.HandleType]  # value = <HandleType.File: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def accessFlags(*args, **kwargs):
        ...
    @staticmethod
    def filePath(*args, **kwargs):
        ...
    @staticmethod
    def handleType(*args, **kwargs):
        ...
    @staticmethod
    def origin(*args, **kwargs):
        ...
    @staticmethod
    def reject(*args, **kwargs):
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
class QWebEngineFindTextResult(PyQt6.sip.simplewrapper):
    @staticmethod
    def activeMatch(*args, **kwargs):
        ...
    @staticmethod
    def numberOfMatches(*args, **kwargs):
        ...
class QWebEngineFullScreenRequest(PyQt6.sip.simplewrapper):
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def origin(*args, **kwargs):
        ...
    @staticmethod
    def reject(*args, **kwargs):
        ...
    @staticmethod
    def toggleOn(*args, **kwargs):
        ...
class QWebEngineGlobalSettings(PyQt6.sip.simplewrapper):
    class DnsMode(PyQt6.sip.simplewrapper):
        pass
    class SecureDnsMode(enum.Enum):
        SecureOnly: typing.ClassVar[QWebEngineGlobalSettings.SecureDnsMode]  # value = <SecureDnsMode.SecureOnly: 2>
        SecureWithFallback: typing.ClassVar[QWebEngineGlobalSettings.SecureDnsMode]  # value = <SecureDnsMode.SecureWithFallback: 1>
        SystemOnly: typing.ClassVar[QWebEngineGlobalSettings.SecureDnsMode]  # value = <SecureDnsMode.SystemOnly: 0>
class QWebEngineHistory(PyQt6.QtCore.QObject):
    @staticmethod
    def back(*args, **kwargs):
        ...
    @staticmethod
    def backItem(*args, **kwargs):
        ...
    @staticmethod
    def backItems(*args, **kwargs):
        ...
    @staticmethod
    def backItemsModel(*args, **kwargs):
        ...
    @staticmethod
    def canGoBack(*args, **kwargs):
        ...
    @staticmethod
    def canGoForward(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def currentItem(*args, **kwargs):
        ...
    @staticmethod
    def currentItemIndex(*args, **kwargs):
        ...
    @staticmethod
    def forward(*args, **kwargs):
        ...
    @staticmethod
    def forwardItem(*args, **kwargs):
        ...
    @staticmethod
    def forwardItems(*args, **kwargs):
        ...
    @staticmethod
    def forwardItemsModel(*args, **kwargs):
        ...
    @staticmethod
    def goToItem(*args, **kwargs):
        ...
    @staticmethod
    def itemAt(*args, **kwargs):
        ...
    @staticmethod
    def items(*args, **kwargs):
        ...
    @staticmethod
    def itemsModel(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QWebEngineHistoryItem(PyQt6.sip.simplewrapper):
    @staticmethod
    def iconUrl(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastVisited(*args, **kwargs):
        ...
    @staticmethod
    def originalUrl(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
        ...
class QWebEngineHistoryModel(PyQt6.QtCore.QAbstractListModel):
    class Roles(enum.Enum):
        IconUrlRole: typing.ClassVar[QWebEngineHistoryModel.Roles]  # value = <Roles.IconUrlRole: 259>
        OffsetRole: typing.ClassVar[QWebEngineHistoryModel.Roles]  # value = <Roles.OffsetRole: 258>
        TitleRole: typing.ClassVar[QWebEngineHistoryModel.Roles]  # value = <Roles.TitleRole: 257>
        UrlRole: typing.ClassVar[QWebEngineHistoryModel.Roles]  # value = <Roles.UrlRole: 256>
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def roleNames(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
class QWebEngineHttpRequest(PyQt6.sip.simplewrapper):
    class Method(enum.Enum):
        Get: typing.ClassVar[QWebEngineHttpRequest.Method]  # value = <Method.Get: 0>
        Post: typing.ClassVar[QWebEngineHttpRequest.Method]  # value = <Method.Post: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def hasHeader(*args, **kwargs):
        ...
    @staticmethod
    def header(*args, **kwargs):
        ...
    @staticmethod
    def headers(*args, **kwargs):
        ...
    @staticmethod
    def method(*args, **kwargs):
        ...
    @staticmethod
    def postData(*args, **kwargs):
        ...
    @staticmethod
    def postRequest(*args, **kwargs):
        ...
    @staticmethod
    def setHeader(*args, **kwargs):
        ...
    @staticmethod
    def setMethod(*args, **kwargs):
        ...
    @staticmethod
    def setPostData(*args, **kwargs):
        ...
    @staticmethod
    def setUrl(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def unsetHeader(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
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
class QWebEngineLoadingInfo(PyQt6.sip.simplewrapper):
    class ErrorDomain(enum.Enum):
        CertificateErrorDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.CertificateErrorDomain: 3>
        ConnectionErrorDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.ConnectionErrorDomain: 2>
        DnsErrorDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.DnsErrorDomain: 6>
        FtpErrorDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.FtpErrorDomain: 5>
        HttpErrorDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.HttpErrorDomain: 4>
        HttpStatusCodeDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.HttpStatusCodeDomain: 7>
        InternalErrorDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.InternalErrorDomain: 1>
        NoErrorDomain: typing.ClassVar[QWebEngineLoadingInfo.ErrorDomain]  # value = <ErrorDomain.NoErrorDomain: 0>
    class LoadStatus(enum.Enum):
        LoadFailedStatus: typing.ClassVar[QWebEngineLoadingInfo.LoadStatus]  # value = <LoadStatus.LoadFailedStatus: 3>
        LoadStartedStatus: typing.ClassVar[QWebEngineLoadingInfo.LoadStatus]  # value = <LoadStatus.LoadStartedStatus: 0>
        LoadStoppedStatus: typing.ClassVar[QWebEngineLoadingInfo.LoadStatus]  # value = <LoadStatus.LoadStoppedStatus: 1>
        LoadSucceededStatus: typing.ClassVar[QWebEngineLoadingInfo.LoadStatus]  # value = <LoadStatus.LoadSucceededStatus: 2>
    @staticmethod
    def errorCode(*args, **kwargs):
        ...
    @staticmethod
    def errorDomain(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def isErrorPage(*args, **kwargs):
        ...
    @staticmethod
    def responseHeaders(*args, **kwargs):
        ...
    @staticmethod
    def status(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
        ...
class QWebEngineNavigationRequest(PyQt6.QtCore.QObject):
    class NavigationType(enum.Enum):
        BackForwardNavigation: typing.ClassVar[QWebEngineNavigationRequest.NavigationType]  # value = <NavigationType.BackForwardNavigation: 3>
        FormSubmittedNavigation: typing.ClassVar[QWebEngineNavigationRequest.NavigationType]  # value = <NavigationType.FormSubmittedNavigation: 2>
        LinkClickedNavigation: typing.ClassVar[QWebEngineNavigationRequest.NavigationType]  # value = <NavigationType.LinkClickedNavigation: 0>
        OtherNavigation: typing.ClassVar[QWebEngineNavigationRequest.NavigationType]  # value = <NavigationType.OtherNavigation: 5>
        RedirectNavigation: typing.ClassVar[QWebEngineNavigationRequest.NavigationType]  # value = <NavigationType.RedirectNavigation: 6>
        ReloadNavigation: typing.ClassVar[QWebEngineNavigationRequest.NavigationType]  # value = <NavigationType.ReloadNavigation: 4>
        TypedNavigation: typing.ClassVar[QWebEngineNavigationRequest.NavigationType]  # value = <NavigationType.TypedNavigation: 1>
    @staticmethod
    def accept(*args, **kwargs):
        ...
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
    def isMainFrame(*args, **kwargs):
        ...
    @staticmethod
    def navigationType(*args, **kwargs):
        ...
    @staticmethod
    def reject(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
        ...
class QWebEngineNewWindowRequest(PyQt6.QtCore.QObject):
    class DestinationType(enum.Enum):
        InNewBackgroundTab: typing.ClassVar[QWebEngineNewWindowRequest.DestinationType]  # value = <DestinationType.InNewBackgroundTab: 3>
        InNewDialog: typing.ClassVar[QWebEngineNewWindowRequest.DestinationType]  # value = <DestinationType.InNewDialog: 2>
        InNewTab: typing.ClassVar[QWebEngineNewWindowRequest.DestinationType]  # value = <DestinationType.InNewTab: 1>
        InNewWindow: typing.ClassVar[QWebEngineNewWindowRequest.DestinationType]  # value = <DestinationType.InNewWindow: 0>
    @staticmethod
    def destination(*args, **kwargs):
        ...
    @staticmethod
    def isUserInitiated(*args, **kwargs):
        ...
    @staticmethod
    def openIn(*args, **kwargs):
        ...
    @staticmethod
    def requestedGeometry(*args, **kwargs):
        ...
    @staticmethod
    def requestedUrl(*args, **kwargs):
        ...
class QWebEngineNotification(PyQt6.QtCore.QObject):
    @staticmethod
    def click(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def closed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def direction(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def language(*args, **kwargs):
        ...
    @staticmethod
    def matches(*args, **kwargs):
        ...
    @staticmethod
    def message(*args, **kwargs):
        ...
    @staticmethod
    def origin(*args, **kwargs):
        ...
    @staticmethod
    def show(*args, **kwargs):
        ...
    @staticmethod
    def tag(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
class QWebEnginePage(PyQt6.QtCore.QObject):
    class Feature(enum.Enum):
        DesktopAudioVideoCapture: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.DesktopAudioVideoCapture: 7>
        DesktopVideoCapture: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.DesktopVideoCapture: 6>
        Geolocation: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.Geolocation: 1>
        MediaAudioCapture: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.MediaAudioCapture: 2>
        MediaAudioVideoCapture: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.MediaAudioVideoCapture: 4>
        MediaVideoCapture: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.MediaVideoCapture: 3>
        MouseLock: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.MouseLock: 5>
        Notifications: typing.ClassVar[QWebEnginePage.Feature]  # value = <Feature.Notifications: 0>
    class FileSelectionMode(enum.Enum):
        FileSelectOpen: typing.ClassVar[QWebEnginePage.FileSelectionMode]  # value = <FileSelectionMode.FileSelectOpen: 0>
        FileSelectOpenMultiple: typing.ClassVar[QWebEnginePage.FileSelectionMode]  # value = <FileSelectionMode.FileSelectOpenMultiple: 1>
        FileSelectSave: typing.ClassVar[QWebEnginePage.FileSelectionMode]  # value = <FileSelectionMode.FileSelectSave: 3>
        FileSelectUploadFolder: typing.ClassVar[QWebEnginePage.FileSelectionMode]  # value = <FileSelectionMode.FileSelectUploadFolder: 2>
    class FindFlag(enum.Flag):
        FindBackward: typing.ClassVar[QWebEnginePage.FindFlag]  # value = <FindFlag.FindBackward: 1>
        FindCaseSensitively: typing.ClassVar[QWebEnginePage.FindFlag]  # value = <FindFlag.FindCaseSensitively: 2>
    class JavaScriptConsoleMessageLevel(enum.Enum):
        ErrorMessageLevel: typing.ClassVar[QWebEnginePage.JavaScriptConsoleMessageLevel]  # value = <JavaScriptConsoleMessageLevel.ErrorMessageLevel: 2>
        InfoMessageLevel: typing.ClassVar[QWebEnginePage.JavaScriptConsoleMessageLevel]  # value = <JavaScriptConsoleMessageLevel.InfoMessageLevel: 0>
        WarningMessageLevel: typing.ClassVar[QWebEnginePage.JavaScriptConsoleMessageLevel]  # value = <JavaScriptConsoleMessageLevel.WarningMessageLevel: 1>
    class LifecycleState(enum.Enum):
        Active: typing.ClassVar[QWebEnginePage.LifecycleState]  # value = <LifecycleState.Active: 0>
        Discarded: typing.ClassVar[QWebEnginePage.LifecycleState]  # value = <LifecycleState.Discarded: 2>
        Frozen: typing.ClassVar[QWebEnginePage.LifecycleState]  # value = <LifecycleState.Frozen: 1>
    class NavigationType(enum.Enum):
        NavigationTypeBackForward: typing.ClassVar[QWebEnginePage.NavigationType]  # value = <NavigationType.NavigationTypeBackForward: 3>
        NavigationTypeFormSubmitted: typing.ClassVar[QWebEnginePage.NavigationType]  # value = <NavigationType.NavigationTypeFormSubmitted: 2>
        NavigationTypeLinkClicked: typing.ClassVar[QWebEnginePage.NavigationType]  # value = <NavigationType.NavigationTypeLinkClicked: 0>
        NavigationTypeOther: typing.ClassVar[QWebEnginePage.NavigationType]  # value = <NavigationType.NavigationTypeOther: 5>
        NavigationTypeRedirect: typing.ClassVar[QWebEnginePage.NavigationType]  # value = <NavigationType.NavigationTypeRedirect: 6>
        NavigationTypeReload: typing.ClassVar[QWebEnginePage.NavigationType]  # value = <NavigationType.NavigationTypeReload: 4>
        NavigationTypeTyped: typing.ClassVar[QWebEnginePage.NavigationType]  # value = <NavigationType.NavigationTypeTyped: 1>
    class PermissionPolicy(enum.Enum):
        PermissionDeniedByUser: typing.ClassVar[QWebEnginePage.PermissionPolicy]  # value = <PermissionPolicy.PermissionDeniedByUser: 2>
        PermissionGrantedByUser: typing.ClassVar[QWebEnginePage.PermissionPolicy]  # value = <PermissionPolicy.PermissionGrantedByUser: 1>
        PermissionUnknown: typing.ClassVar[QWebEnginePage.PermissionPolicy]  # value = <PermissionPolicy.PermissionUnknown: 0>
    class RenderProcessTerminationStatus(enum.Enum):
        AbnormalTerminationStatus: typing.ClassVar[QWebEnginePage.RenderProcessTerminationStatus]  # value = <RenderProcessTerminationStatus.AbnormalTerminationStatus: 1>
        CrashedTerminationStatus: typing.ClassVar[QWebEnginePage.RenderProcessTerminationStatus]  # value = <RenderProcessTerminationStatus.CrashedTerminationStatus: 2>
        KilledTerminationStatus: typing.ClassVar[QWebEnginePage.RenderProcessTerminationStatus]  # value = <RenderProcessTerminationStatus.KilledTerminationStatus: 3>
        NormalTerminationStatus: typing.ClassVar[QWebEnginePage.RenderProcessTerminationStatus]  # value = <RenderProcessTerminationStatus.NormalTerminationStatus: 0>
    class WebAction(enum.Enum):
        AlignCenter: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.AlignCenter: 38>
        AlignJustified: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.AlignJustified: 40>
        AlignLeft: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.AlignLeft: 37>
        AlignRight: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.AlignRight: 39>
        Back: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Back: 0>
        ChangeTextDirectionLTR: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ChangeTextDirectionLTR: 45>
        ChangeTextDirectionRTL: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ChangeTextDirectionRTL: 46>
        Copy: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Copy: 5>
        CopyImageToClipboard: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.CopyImageToClipboard: 17>
        CopyImageUrlToClipboard: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.CopyImageUrlToClipboard: 18>
        CopyLinkToClipboard: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.CopyLinkToClipboard: 15>
        CopyMediaUrlToClipboard: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.CopyMediaUrlToClipboard: 20>
        Cut: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Cut: 4>
        DownloadImageToDisk: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.DownloadImageToDisk: 19>
        DownloadLinkToDisk: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.DownloadLinkToDisk: 16>
        DownloadMediaToDisk: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.DownloadMediaToDisk: 25>
        ExitFullScreen: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ExitFullScreen: 27>
        Forward: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Forward: 1>
        Indent: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Indent: 41>
        InsertOrderedList: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.InsertOrderedList: 43>
        InsertUnorderedList: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.InsertUnorderedList: 44>
        InspectElement: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.InspectElement: 26>
        NoWebAction: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.NoWebAction: -1>
        OpenLinkInNewBackgroundTab: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.OpenLinkInNewBackgroundTab: 31>
        OpenLinkInNewTab: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.OpenLinkInNewTab: 14>
        OpenLinkInNewWindow: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.OpenLinkInNewWindow: 13>
        OpenLinkInThisWindow: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.OpenLinkInThisWindow: 12>
        Outdent: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Outdent: 42>
        Paste: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Paste: 6>
        PasteAndMatchStyle: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.PasteAndMatchStyle: 11>
        Redo: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Redo: 8>
        Reload: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Reload: 3>
        ReloadAndBypassCache: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ReloadAndBypassCache: 10>
        RequestClose: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.RequestClose: 28>
        SavePage: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.SavePage: 30>
        SelectAll: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.SelectAll: 9>
        Stop: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Stop: 2>
        ToggleBold: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleBold: 33>
        ToggleItalic: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleItalic: 34>
        ToggleMediaControls: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleMediaControls: 21>
        ToggleMediaLoop: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleMediaLoop: 22>
        ToggleMediaMute: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleMediaMute: 24>
        ToggleMediaPlayPause: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleMediaPlayPause: 23>
        ToggleStrikethrough: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleStrikethrough: 36>
        ToggleUnderline: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ToggleUnderline: 35>
        Undo: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Undo: 7>
        Unselect: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.Unselect: 29>
        ViewSource: typing.ClassVar[QWebEnginePage.WebAction]  # value = <WebAction.ViewSource: 32>
    class WebWindowType(enum.Enum):
        WebBrowserBackgroundTab: typing.ClassVar[QWebEnginePage.WebWindowType]  # value = <WebWindowType.WebBrowserBackgroundTab: 3>
        WebBrowserTab: typing.ClassVar[QWebEnginePage.WebWindowType]  # value = <WebWindowType.WebBrowserTab: 1>
        WebBrowserWindow: typing.ClassVar[QWebEnginePage.WebWindowType]  # value = <WebWindowType.WebBrowserWindow: 0>
        WebDialog: typing.ClassVar[QWebEnginePage.WebWindowType]  # value = <WebWindowType.WebDialog: 2>
    @staticmethod
    def acceptNavigationRequest(*args, **kwargs):
        ...
    @staticmethod
    def action(*args, **kwargs):
        ...
    @staticmethod
    def audioMutedChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def authenticationRequired(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def backgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def certificateError(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def chooseFiles(*args, **kwargs):
        ...
    @staticmethod
    def contentsSize(*args, **kwargs):
        ...
    @staticmethod
    def contentsSizeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def createWindow(*args, **kwargs):
        ...
    @staticmethod
    def desktopMediaRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def devToolsId(*args, **kwargs):
        ...
    @staticmethod
    def devToolsPage(*args, **kwargs):
        ...
    @staticmethod
    def download(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def featurePermissionRequestCanceled(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def featurePermissionRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def fileSystemAccessRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def findText(*args, **kwargs):
        ...
    @staticmethod
    def findTextFinished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def fullScreenRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def geometryChangeRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def hasSelection(*args, **kwargs):
        ...
    @staticmethod
    def history(*args, **kwargs):
        ...
    @staticmethod
    def icon(*args, **kwargs):
        ...
    @staticmethod
    def iconChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def iconUrl(*args, **kwargs):
        ...
    @staticmethod
    def iconUrlChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def inspectedPage(*args, **kwargs):
        ...
    @staticmethod
    def isAudioMuted(*args, **kwargs):
        ...
    @staticmethod
    def isLoading(*args, **kwargs):
        ...
    @staticmethod
    def isVisible(*args, **kwargs):
        ...
    @staticmethod
    def javaScriptAlert(*args, **kwargs):
        ...
    @staticmethod
    def javaScriptConfirm(*args, **kwargs):
        ...
    @staticmethod
    def javaScriptConsoleMessage(*args, **kwargs):
        ...
    @staticmethod
    def javaScriptPrompt(*args, **kwargs):
        ...
    @staticmethod
    def lifecycleState(*args, **kwargs):
        ...
    @staticmethod
    def lifecycleStateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def load(*args, **kwargs):
        ...
    @staticmethod
    def loadFinished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def loadProgress(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def loadStarted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def loadingChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def navigationRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def newWindowRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def pdfPrintingFinished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def printRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def printToPdf(*args, **kwargs):
        ...
    @staticmethod
    def profile(*args, **kwargs):
        ...
    @staticmethod
    def proxyAuthenticationRequired(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def quotaRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def recentlyAudible(*args, **kwargs):
        ...
    @staticmethod
    def recentlyAudibleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def recommendedState(*args, **kwargs):
        ...
    @staticmethod
    def recommendedStateChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def registerProtocolHandlerRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def renderProcessPid(*args, **kwargs):
        ...
    @staticmethod
    def renderProcessPidChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def renderProcessTerminated(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def replaceMisspelledWord(*args, **kwargs):
        ...
    @staticmethod
    def requestedUrl(*args, **kwargs):
        ...
    @staticmethod
    def runJavaScript(*args, **kwargs):
        ...
    @staticmethod
    def save(*args, **kwargs):
        ...
    @staticmethod
    def scripts(*args, **kwargs):
        ...
    @staticmethod
    def scrollPosition(*args, **kwargs):
        ...
    @staticmethod
    def scrollPositionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def selectClientCertificate(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
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
    def setAudioMuted(*args, **kwargs):
        ...
    @staticmethod
    def setBackgroundColor(*args, **kwargs):
        ...
    @staticmethod
    def setContent(*args, **kwargs):
        ...
    @staticmethod
    def setDevToolsPage(*args, **kwargs):
        ...
    @staticmethod
    def setFeaturePermission(*args, **kwargs):
        ...
    @staticmethod
    def setHtml(*args, **kwargs):
        ...
    @staticmethod
    def setInspectedPage(*args, **kwargs):
        ...
    @staticmethod
    def setLifecycleState(*args, **kwargs):
        ...
    @staticmethod
    def setUrl(*args, **kwargs):
        ...
    @staticmethod
    def setUrlRequestInterceptor(*args, **kwargs):
        ...
    @staticmethod
    def setVisible(*args, **kwargs):
        ...
    @staticmethod
    def setWebChannel(*args, **kwargs):
        ...
    @staticmethod
    def setZoomFactor(*args, **kwargs):
        ...
    @staticmethod
    def settings(*args, **kwargs):
        ...
    @staticmethod
    def title(*args, **kwargs):
        ...
    @staticmethod
    def titleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def toHtml(*args, **kwargs):
        ...
    @staticmethod
    def toPlainText(*args, **kwargs):
        ...
    @staticmethod
    def triggerAction(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
        ...
    @staticmethod
    def urlChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def webAuthUxRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def webChannel(*args, **kwargs):
        ...
    @staticmethod
    def windowCloseRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def zoomFactor(*args, **kwargs):
        ...
class QWebEngineProfile(PyQt6.QtCore.QObject):
    class HttpCacheType(enum.Enum):
        DiskHttpCache: typing.ClassVar[QWebEngineProfile.HttpCacheType]  # value = <HttpCacheType.DiskHttpCache: 1>
        MemoryHttpCache: typing.ClassVar[QWebEngineProfile.HttpCacheType]  # value = <HttpCacheType.MemoryHttpCache: 0>
        NoCache: typing.ClassVar[QWebEngineProfile.HttpCacheType]  # value = <HttpCacheType.NoCache: 2>
    class PersistentCookiesPolicy(enum.Enum):
        AllowPersistentCookies: typing.ClassVar[QWebEngineProfile.PersistentCookiesPolicy]  # value = <PersistentCookiesPolicy.AllowPersistentCookies: 1>
        ForcePersistentCookies: typing.ClassVar[QWebEngineProfile.PersistentCookiesPolicy]  # value = <PersistentCookiesPolicy.ForcePersistentCookies: 2>
        NoPersistentCookies: typing.ClassVar[QWebEngineProfile.PersistentCookiesPolicy]  # value = <PersistentCookiesPolicy.NoPersistentCookies: 0>
    @staticmethod
    def cachePath(*args, **kwargs):
        ...
    @staticmethod
    def clearAllVisitedLinks(*args, **kwargs):
        ...
    @staticmethod
    def clearHttpCache(*args, **kwargs):
        ...
    @staticmethod
    def clearHttpCacheCompleted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def clearVisitedLinks(*args, **kwargs):
        ...
    @staticmethod
    def clientCertificateStore(*args, **kwargs):
        ...
    @staticmethod
    def cookieStore(*args, **kwargs):
        ...
    @staticmethod
    def defaultProfile(*args, **kwargs):
        ...
    @staticmethod
    def downloadPath(*args, **kwargs):
        ...
    @staticmethod
    def downloadRequested(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def httpAcceptLanguage(*args, **kwargs):
        ...
    @staticmethod
    def httpCacheMaximumSize(*args, **kwargs):
        ...
    @staticmethod
    def httpCacheType(*args, **kwargs):
        ...
    @staticmethod
    def httpUserAgent(*args, **kwargs):
        ...
    @staticmethod
    def installUrlSchemeHandler(*args, **kwargs):
        ...
    @staticmethod
    def isOffTheRecord(*args, **kwargs):
        ...
    @staticmethod
    def isPushServiceEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isSpellCheckEnabled(*args, **kwargs):
        ...
    @staticmethod
    def persistentCookiesPolicy(*args, **kwargs):
        ...
    @staticmethod
    def persistentStoragePath(*args, **kwargs):
        ...
    @staticmethod
    def removeAllUrlSchemeHandlers(*args, **kwargs):
        ...
    @staticmethod
    def removeUrlScheme(*args, **kwargs):
        ...
    @staticmethod
    def removeUrlSchemeHandler(*args, **kwargs):
        ...
    @staticmethod
    def requestIconForIconURL(*args, **kwargs):
        ...
    @staticmethod
    def requestIconForPageURL(*args, **kwargs):
        ...
    @staticmethod
    def scripts(*args, **kwargs):
        ...
    @staticmethod
    def setCachePath(*args, **kwargs):
        ...
    @staticmethod
    def setDownloadPath(*args, **kwargs):
        ...
    @staticmethod
    def setHttpAcceptLanguage(*args, **kwargs):
        ...
    @staticmethod
    def setHttpCacheMaximumSize(*args, **kwargs):
        ...
    @staticmethod
    def setHttpCacheType(*args, **kwargs):
        ...
    @staticmethod
    def setHttpUserAgent(*args, **kwargs):
        ...
    @staticmethod
    def setNotificationPresenter(*args, **kwargs):
        ...
    @staticmethod
    def setPersistentCookiesPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setPersistentStoragePath(*args, **kwargs):
        ...
    @staticmethod
    def setPushServiceEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSpellCheckEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSpellCheckLanguages(*args, **kwargs):
        ...
    @staticmethod
    def setUrlRequestInterceptor(*args, **kwargs):
        ...
    @staticmethod
    def settings(*args, **kwargs):
        ...
    @staticmethod
    def spellCheckLanguages(*args, **kwargs):
        ...
    @staticmethod
    def storageName(*args, **kwargs):
        ...
    @staticmethod
    def urlSchemeHandler(*args, **kwargs):
        ...
    @staticmethod
    def visitedLinksContainsUrl(*args, **kwargs):
        ...
class QWebEngineQuotaRequest(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def origin(*args, **kwargs):
        ...
    @staticmethod
    def reject(*args, **kwargs):
        ...
    @staticmethod
    def requestedSize(*args, **kwargs):
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
class QWebEngineRegisterProtocolHandlerRequest(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def origin(*args, **kwargs):
        ...
    @staticmethod
    def reject(*args, **kwargs):
        ...
    @staticmethod
    def scheme(*args, **kwargs):
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
class QWebEngineScript(PyQt6.sip.simplewrapper):
    class InjectionPoint(enum.Enum):
        Deferred: typing.ClassVar[QWebEngineScript.InjectionPoint]  # value = <InjectionPoint.Deferred: 0>
        DocumentCreation: typing.ClassVar[QWebEngineScript.InjectionPoint]  # value = <InjectionPoint.DocumentCreation: 2>
        DocumentReady: typing.ClassVar[QWebEngineScript.InjectionPoint]  # value = <InjectionPoint.DocumentReady: 1>
    class ScriptWorldId(enum.IntEnum):
        ApplicationWorld: typing.ClassVar[QWebEngineScript.ScriptWorldId]  # value = <ScriptWorldId.ApplicationWorld: 1>
        MainWorld: typing.ClassVar[QWebEngineScript.ScriptWorldId]  # value = <ScriptWorldId.MainWorld: 0>
        UserWorld: typing.ClassVar[QWebEngineScript.ScriptWorldId]  # value = <ScriptWorldId.UserWorld: 2>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def injectionPoint(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def runsOnSubFrames(*args, **kwargs):
        ...
    @staticmethod
    def setInjectionPoint(*args, **kwargs):
        ...
    @staticmethod
    def setName(*args, **kwargs):
        ...
    @staticmethod
    def setRunsOnSubFrames(*args, **kwargs):
        ...
    @staticmethod
    def setSourceCode(*args, **kwargs):
        ...
    @staticmethod
    def setSourceUrl(*args, **kwargs):
        ...
    @staticmethod
    def setWorldId(*args, **kwargs):
        ...
    @staticmethod
    def sourceCode(*args, **kwargs):
        ...
    @staticmethod
    def sourceUrl(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def worldId(*args, **kwargs):
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
class QWebEngineScriptCollection(PyQt6.sip.simplewrapper):
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def find(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def toList(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QWebEngineSettings(PyQt6.sip.simplewrapper):
    class FontFamily(enum.Enum):
        CursiveFont: typing.ClassVar[QWebEngineSettings.FontFamily]  # value = <FontFamily.CursiveFont: 4>
        FantasyFont: typing.ClassVar[QWebEngineSettings.FontFamily]  # value = <FontFamily.FantasyFont: 5>
        FixedFont: typing.ClassVar[QWebEngineSettings.FontFamily]  # value = <FontFamily.FixedFont: 1>
        PictographFont: typing.ClassVar[QWebEngineSettings.FontFamily]  # value = <FontFamily.PictographFont: 6>
        SansSerifFont: typing.ClassVar[QWebEngineSettings.FontFamily]  # value = <FontFamily.SansSerifFont: 3>
        SerifFont: typing.ClassVar[QWebEngineSettings.FontFamily]  # value = <FontFamily.SerifFont: 2>
        StandardFont: typing.ClassVar[QWebEngineSettings.FontFamily]  # value = <FontFamily.StandardFont: 0>
    class FontSize(enum.Enum):
        DefaultFixedFontSize: typing.ClassVar[QWebEngineSettings.FontSize]  # value = <FontSize.DefaultFixedFontSize: 3>
        DefaultFontSize: typing.ClassVar[QWebEngineSettings.FontSize]  # value = <FontSize.DefaultFontSize: 2>
        MinimumFontSize: typing.ClassVar[QWebEngineSettings.FontSize]  # value = <FontSize.MinimumFontSize: 0>
        MinimumLogicalFontSize: typing.ClassVar[QWebEngineSettings.FontSize]  # value = <FontSize.MinimumLogicalFontSize: 1>
    class UnknownUrlSchemePolicy(enum.Enum):
        AllowAllUnknownUrlSchemes: typing.ClassVar[QWebEngineSettings.UnknownUrlSchemePolicy]  # value = <UnknownUrlSchemePolicy.AllowAllUnknownUrlSchemes: 3>
        AllowUnknownUrlSchemesFromUserInteraction: typing.ClassVar[QWebEngineSettings.UnknownUrlSchemePolicy]  # value = <UnknownUrlSchemePolicy.AllowUnknownUrlSchemesFromUserInteraction: 2>
        DisallowUnknownUrlSchemes: typing.ClassVar[QWebEngineSettings.UnknownUrlSchemePolicy]  # value = <UnknownUrlSchemePolicy.DisallowUnknownUrlSchemes: 1>
    class WebAttribute(enum.Enum):
        Accelerated2dCanvasEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.Accelerated2dCanvasEnabled: 17>
        AllowGeolocationOnInsecureOrigins: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.AllowGeolocationOnInsecureOrigins: 23>
        AllowRunningInsecureContent: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.AllowRunningInsecureContent: 22>
        AllowWindowActivationFromJavaScript: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.AllowWindowActivationFromJavaScript: 24>
        AutoLoadIconsForPage: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.AutoLoadIconsForPage: 18>
        AutoLoadImages: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.AutoLoadImages: 0>
        DnsPrefetchEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.DnsPrefetchEnabled: 29>
        ErrorPageEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.ErrorPageEnabled: 12>
        FocusOnNavigationEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.FocusOnNavigationEnabled: 20>
        ForceDarkMode: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.ForceDarkMode: 33>
        FullScreenSupportEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.FullScreenSupportEnabled: 14>
        HyperlinkAuditingEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.HyperlinkAuditingEnabled: 10>
        JavascriptCanAccessClipboard: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.JavascriptCanAccessClipboard: 3>
        JavascriptCanOpenWindows: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.JavascriptCanOpenWindows: 2>
        JavascriptCanPaste: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.JavascriptCanPaste: 28>
        JavascriptEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.JavascriptEnabled: 1>
        LinksIncludedInFocusChain: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.LinksIncludedInFocusChain: 4>
        LocalContentCanAccessFileUrls: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.LocalContentCanAccessFileUrls: 9>
        LocalContentCanAccessRemoteUrls: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.LocalContentCanAccessRemoteUrls: 6>
        LocalStorageEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.LocalStorageEnabled: 5>
        NavigateOnDropEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.NavigateOnDropEnabled: 31>
        PdfViewerEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.PdfViewerEnabled: 30>
        PlaybackRequiresUserGesture: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.PlaybackRequiresUserGesture: 26>
        PluginsEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.PluginsEnabled: 13>
        PrintElementBackgrounds: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.PrintElementBackgrounds: 21>
        ReadingFromCanvasEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.ReadingFromCanvasEnabled: 32>
        ScreenCaptureEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.ScreenCaptureEnabled: 15>
        ScrollAnimatorEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.ScrollAnimatorEnabled: 11>
        ShowScrollBars: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.ShowScrollBars: 25>
        SpatialNavigationEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.SpatialNavigationEnabled: 8>
        TouchIconsEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.TouchIconsEnabled: 19>
        WebGLEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.WebGLEnabled: 16>
        WebRTCPublicInterfacesOnly: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.WebRTCPublicInterfacesOnly: 27>
        XSSAuditingEnabled: typing.ClassVar[QWebEngineSettings.WebAttribute]  # value = <WebAttribute.XSSAuditingEnabled: 7>
    @staticmethod
    def defaultTextEncoding(*args, **kwargs):
        ...
    @staticmethod
    def fontFamily(*args, **kwargs):
        ...
    @staticmethod
    def fontSize(*args, **kwargs):
        ...
    @staticmethod
    def resetAttribute(*args, **kwargs):
        ...
    @staticmethod
    def resetFontFamily(*args, **kwargs):
        ...
    @staticmethod
    def resetFontSize(*args, **kwargs):
        ...
    @staticmethod
    def resetUnknownUrlSchemePolicy(*args, **kwargs):
        ...
    @staticmethod
    def setAttribute(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultTextEncoding(*args, **kwargs):
        ...
    @staticmethod
    def setFontFamily(*args, **kwargs):
        ...
    @staticmethod
    def setFontSize(*args, **kwargs):
        ...
    @staticmethod
    def setUnknownUrlSchemePolicy(*args, **kwargs):
        ...
    @staticmethod
    def testAttribute(*args, **kwargs):
        ...
    @staticmethod
    def unknownUrlSchemePolicy(*args, **kwargs):
        ...
class QWebEngineUrlRequestInfo(PyQt6.sip.simplewrapper):
    class NavigationType(enum.Enum):
        NavigationTypeBackForward: typing.ClassVar[QWebEngineUrlRequestInfo.NavigationType]  # value = <NavigationType.NavigationTypeBackForward: 3>
        NavigationTypeFormSubmitted: typing.ClassVar[QWebEngineUrlRequestInfo.NavigationType]  # value = <NavigationType.NavigationTypeFormSubmitted: 2>
        NavigationTypeLink: typing.ClassVar[QWebEngineUrlRequestInfo.NavigationType]  # value = <NavigationType.NavigationTypeLink: 0>
        NavigationTypeOther: typing.ClassVar[QWebEngineUrlRequestInfo.NavigationType]  # value = <NavigationType.NavigationTypeOther: 5>
        NavigationTypeRedirect: typing.ClassVar[QWebEngineUrlRequestInfo.NavigationType]  # value = <NavigationType.NavigationTypeRedirect: 6>
        NavigationTypeReload: typing.ClassVar[QWebEngineUrlRequestInfo.NavigationType]  # value = <NavigationType.NavigationTypeReload: 4>
        NavigationTypeTyped: typing.ClassVar[QWebEngineUrlRequestInfo.NavigationType]  # value = <NavigationType.NavigationTypeTyped: 1>
    class ResourceType(enum.Enum):
        ResourceTypeCspReport: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeCspReport: 16>
        ResourceTypeFavicon: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeFavicon: 12>
        ResourceTypeFontResource: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeFontResource: 5>
        ResourceTypeImage: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeImage: 4>
        ResourceTypeMainFrame: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeMainFrame: 0>
        ResourceTypeMedia: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeMedia: 8>
        ResourceTypeNavigationPreloadMainFrame: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeNavigationPreloadMainFrame: 19>
        ResourceTypeNavigationPreloadSubFrame: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeNavigationPreloadSubFrame: 20>
        ResourceTypeObject: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeObject: 7>
        ResourceTypePing: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypePing: 14>
        ResourceTypePluginResource: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypePluginResource: 17>
        ResourceTypePrefetch: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypePrefetch: 11>
        ResourceTypeScript: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeScript: 3>
        ResourceTypeServiceWorker: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeServiceWorker: 15>
        ResourceTypeSharedWorker: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeSharedWorker: 10>
        ResourceTypeStylesheet: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeStylesheet: 2>
        ResourceTypeSubFrame: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeSubFrame: 1>
        ResourceTypeSubResource: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeSubResource: 6>
        ResourceTypeUnknown: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeUnknown: 255>
        ResourceTypeWebSocket: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeWebSocket: 254>
        ResourceTypeWorker: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeWorker: 9>
        ResourceTypeXhr: typing.ClassVar[QWebEngineUrlRequestInfo.ResourceType]  # value = <ResourceType.ResourceTypeXhr: 13>
    @staticmethod
    def block(*args, **kwargs):
        ...
    @staticmethod
    def firstPartyUrl(*args, **kwargs):
        ...
    @staticmethod
    def httpHeaders(*args, **kwargs):
        ...
    @staticmethod
    def initiator(*args, **kwargs):
        ...
    @staticmethod
    def navigationType(*args, **kwargs):
        ...
    @staticmethod
    def redirect(*args, **kwargs):
        ...
    @staticmethod
    def requestBody(*args, **kwargs):
        ...
    @staticmethod
    def requestMethod(*args, **kwargs):
        ...
    @staticmethod
    def requestUrl(*args, **kwargs):
        ...
    @staticmethod
    def resourceType(*args, **kwargs):
        ...
    @staticmethod
    def setHttpHeader(*args, **kwargs):
        ...
class QWebEngineUrlRequestInterceptor(PyQt6.QtCore.QObject):
    @staticmethod
    def interceptRequest(*args, **kwargs):
        ...
class QWebEngineUrlRequestJob(PyQt6.QtCore.QObject):
    class Error(enum.Enum):
        NoError: typing.ClassVar[QWebEngineUrlRequestJob.Error]  # value = <Error.NoError: 0>
        RequestAborted: typing.ClassVar[QWebEngineUrlRequestJob.Error]  # value = <Error.RequestAborted: 3>
        RequestDenied: typing.ClassVar[QWebEngineUrlRequestJob.Error]  # value = <Error.RequestDenied: 4>
        RequestFailed: typing.ClassVar[QWebEngineUrlRequestJob.Error]  # value = <Error.RequestFailed: 5>
        UrlInvalid: typing.ClassVar[QWebEngineUrlRequestJob.Error]  # value = <Error.UrlInvalid: 2>
        UrlNotFound: typing.ClassVar[QWebEngineUrlRequestJob.Error]  # value = <Error.UrlNotFound: 1>
    @staticmethod
    def fail(*args, **kwargs):
        ...
    @staticmethod
    def initiator(*args, **kwargs):
        ...
    @staticmethod
    def redirect(*args, **kwargs):
        ...
    @staticmethod
    def reply(*args, **kwargs):
        ...
    @staticmethod
    def requestBody(*args, **kwargs):
        ...
    @staticmethod
    def requestHeaders(*args, **kwargs):
        ...
    @staticmethod
    def requestMethod(*args, **kwargs):
        ...
    @staticmethod
    def requestUrl(*args, **kwargs):
        ...
    @staticmethod
    def setAdditionalResponseHeaders(*args, **kwargs):
        ...
class QWebEngineUrlScheme(PyQt6.sip.simplewrapper):
    class Flag(enum.Flag):
        ContentSecurityPolicyIgnored: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.ContentSecurityPolicyIgnored: 64>
        CorsEnabled: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.CorsEnabled: 128>
        FetchApiAllowed: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.FetchApiAllowed: 256>
        LocalAccessAllowed: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.LocalAccessAllowed: 4>
        LocalScheme: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.LocalScheme: 2>
        NoAccessAllowed: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.NoAccessAllowed: 8>
        SecureScheme: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.SecureScheme: 1>
        ServiceWorkersAllowed: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.ServiceWorkersAllowed: 16>
        ViewSourceAllowed: typing.ClassVar[QWebEngineUrlScheme.Flag]  # value = <Flag.ViewSourceAllowed: 32>
    class SpecialPort(enum.Enum):
        PortUnspecified: typing.ClassVar[QWebEngineUrlScheme.SpecialPort]  # value = <SpecialPort.PortUnspecified: -1>
    class Syntax(enum.Enum):
        Host: typing.ClassVar[QWebEngineUrlScheme.Syntax]  # value = <Syntax.Host: 2>
        HostAndPort: typing.ClassVar[QWebEngineUrlScheme.Syntax]  # value = <Syntax.HostAndPort: 1>
        HostPortAndUserInformation: typing.ClassVar[QWebEngineUrlScheme.Syntax]  # value = <Syntax.HostPortAndUserInformation: 0>
        Path: typing.ClassVar[QWebEngineUrlScheme.Syntax]  # value = <Syntax.Path: 3>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def defaultPort(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def registerScheme(*args, **kwargs):
        ...
    @staticmethod
    def schemeByName(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultPort(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setName(*args, **kwargs):
        ...
    @staticmethod
    def setSyntax(*args, **kwargs):
        ...
    @staticmethod
    def syntax(*args, **kwargs):
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
class QWebEngineUrlSchemeHandler(PyQt6.QtCore.QObject):
    @staticmethod
    def requestStarted(*args, **kwargs):
        ...
class QWebEngineWebAuthPinRequest(PyQt6.sip.simplewrapper):
    pass
class QWebEngineWebAuthUxRequest(PyQt6.QtCore.QObject):
    class PinEntryError(enum.Enum):
        InternalUvLocked: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryError]  # value = <PinEntryError.InternalUvLocked: 1>
        InvalidCharacters: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryError]  # value = <PinEntryError.InvalidCharacters: 4>
        NoError: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryError]  # value = <PinEntryError.NoError: 0>
        SameAsCurrentPin: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryError]  # value = <PinEntryError.SameAsCurrentPin: 5>
        TooShort: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryError]  # value = <PinEntryError.TooShort: 3>
        WrongPin: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryError]  # value = <PinEntryError.WrongPin: 2>
    class PinEntryReason(enum.Enum):
        Challenge: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryReason]  # value = <PinEntryReason.Challenge: 2>
        Change: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryReason]  # value = <PinEntryReason.Change: 1>
        Set: typing.ClassVar[QWebEngineWebAuthUxRequest.PinEntryReason]  # value = <PinEntryReason.Set: 0>
    class RequestFailureReason(enum.Enum):
        AuthenticatorMissingLargeBlob: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.AuthenticatorMissingLargeBlob: 8>
        AuthenticatorMissingResidentKeys: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.AuthenticatorMissingResidentKeys: 6>
        AuthenticatorMissingUserVerification: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.AuthenticatorMissingUserVerification: 7>
        AuthenticatorRemovedDuringPinEntry: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.AuthenticatorRemovedDuringPinEntry: 5>
        HardPinBlock: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.HardPinBlock: 4>
        KeyAlreadyRegistered: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.KeyAlreadyRegistered: 2>
        KeyNotRegistered: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.KeyNotRegistered: 1>
        NoCommonAlgorithms: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.NoCommonAlgorithms: 9>
        SoftPinBlock: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.SoftPinBlock: 3>
        StorageFull: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.StorageFull: 10>
        Timeout: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.Timeout: 0>
        UserConsentDenied: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.UserConsentDenied: 11>
        WinUserCancelled: typing.ClassVar[QWebEngineWebAuthUxRequest.RequestFailureReason]  # value = <RequestFailureReason.WinUserCancelled: 12>
    class WebAuthUxState(enum.Enum):
        Cancelled: typing.ClassVar[QWebEngineWebAuthUxRequest.WebAuthUxState]  # value = <WebAuthUxState.Cancelled: 5>
        CollectPin: typing.ClassVar[QWebEngineWebAuthUxRequest.WebAuthUxState]  # value = <WebAuthUxState.CollectPin: 2>
        Completed: typing.ClassVar[QWebEngineWebAuthUxRequest.WebAuthUxState]  # value = <WebAuthUxState.Completed: 6>
        FinishTokenCollection: typing.ClassVar[QWebEngineWebAuthUxRequest.WebAuthUxState]  # value = <WebAuthUxState.FinishTokenCollection: 3>
        NotStarted: typing.ClassVar[QWebEngineWebAuthUxRequest.WebAuthUxState]  # value = <WebAuthUxState.NotStarted: 0>
        RequestFailed: typing.ClassVar[QWebEngineWebAuthUxRequest.WebAuthUxState]  # value = <WebAuthUxState.RequestFailed: 4>
        SelectAccount: typing.ClassVar[QWebEngineWebAuthUxRequest.WebAuthUxState]  # value = <WebAuthUxState.SelectAccount: 1>
    @staticmethod
    def cancel(*args, **kwargs):
        ...
    @staticmethod
    def pinRequest(*args, **kwargs):
        ...
    @staticmethod
    def relyingPartyId(*args, **kwargs):
        ...
    @staticmethod
    def requestFailureReason(*args, **kwargs):
        ...
    @staticmethod
    def retry(*args, **kwargs):
        ...
    @staticmethod
    def setPin(*args, **kwargs):
        ...
    @staticmethod
    def setSelectedAccount(*args, **kwargs):
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
    def userNames(*args, **kwargs):
        ...
def qWebEngineChromiumSecurityPatchVersion(*args, **kwargs):
    ...
def qWebEngineChromiumVersion(*args, **kwargs):
    ...
def qWebEngineGetDomainAndRegistry(*args, **kwargs):
    ...
def qWebEngineProcessName(*args, **kwargs):
    ...
def qWebEngineVersion(*args, **kwargs):
    ...
PYQT_WEBENGINE_VERSION: int = 395008
PYQT_WEBENGINE_VERSION_STR: str = '6.7.0'
