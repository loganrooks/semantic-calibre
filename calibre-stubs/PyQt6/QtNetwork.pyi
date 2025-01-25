import PyQt6.QtCore
import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['QAbstractNetworkCache', 'QAbstractSocket', 'QAuthenticator', 'QDnsDomainNameRecord', 'QDnsHostAddressRecord', 'QDnsLookup', 'QDnsMailExchangeRecord', 'QDnsServiceRecord', 'QDnsTextRecord', 'QHostAddress', 'QHostInfo', 'QHstsPolicy', 'QHttp1Configuration', 'QHttp2Configuration', 'QHttpHeaders', 'QHttpMultiPart', 'QHttpPart', 'QLocalServer', 'QLocalSocket', 'QNetworkAccessManager', 'QNetworkAddressEntry', 'QNetworkCacheMetaData', 'QNetworkCookie', 'QNetworkCookieJar', 'QNetworkDatagram', 'QNetworkDiskCache', 'QNetworkInformation', 'QNetworkInterface', 'QNetworkProxy', 'QNetworkProxyFactory', 'QNetworkProxyQuery', 'QNetworkReply', 'QNetworkRequest', 'QOcspCertificateStatus', 'QOcspResponse', 'QOcspRevocationReason', 'QPasswordDigestor', 'QSsl', 'QSslCertificate', 'QSslCertificateExtension', 'QSslCipher', 'QSslConfiguration', 'QSslDiffieHellmanParameters', 'QSslEllipticCurve', 'QSslError', 'QSslKey', 'QSslPreSharedKeyAuthenticator', 'QSslServer', 'QSslSocket', 'QTcpServer', 'QTcpSocket', 'QUdpSocket']
class QAbstractNetworkCache(PyQt6.QtCore.QObject):
    @staticmethod
    def cacheSize(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def metaData(*args, **kwargs):
        ...
    @staticmethod
    def prepare(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def updateMetaData(*args, **kwargs):
        ...
class QAbstractSocket(PyQt6.QtCore.QIODevice):
    class BindFlag(enum.Flag):
        DontShareAddress: typing.ClassVar[QAbstractSocket.BindFlag]  # value = <BindFlag.DontShareAddress: 2>
        ReuseAddressHint: typing.ClassVar[QAbstractSocket.BindFlag]  # value = <BindFlag.ReuseAddressHint: 4>
        ShareAddress: typing.ClassVar[QAbstractSocket.BindFlag]  # value = <BindFlag.ShareAddress: 1>
    class NetworkLayerProtocol(enum.Enum):
        AnyIPProtocol: typing.ClassVar[QAbstractSocket.NetworkLayerProtocol]  # value = <NetworkLayerProtocol.AnyIPProtocol: 2>
        IPv4Protocol: typing.ClassVar[QAbstractSocket.NetworkLayerProtocol]  # value = <NetworkLayerProtocol.IPv4Protocol: 0>
        IPv6Protocol: typing.ClassVar[QAbstractSocket.NetworkLayerProtocol]  # value = <NetworkLayerProtocol.IPv6Protocol: 1>
        UnknownNetworkLayerProtocol: typing.ClassVar[QAbstractSocket.NetworkLayerProtocol]  # value = <NetworkLayerProtocol.UnknownNetworkLayerProtocol: -1>
    class PauseMode(enum.Flag):
        PauseOnSslErrors: typing.ClassVar[QAbstractSocket.PauseMode]  # value = <PauseMode.PauseOnSslErrors: 1>
    class SocketError(enum.Enum):
        AddressInUseError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.AddressInUseError: 8>
        ConnectionRefusedError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.ConnectionRefusedError: 0>
        DatagramTooLargeError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.DatagramTooLargeError: 6>
        HostNotFoundError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.HostNotFoundError: 2>
        NetworkError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.NetworkError: 7>
        OperationError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.OperationError: 19>
        ProxyAuthenticationRequiredError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.ProxyAuthenticationRequiredError: 12>
        ProxyConnectionClosedError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.ProxyConnectionClosedError: 15>
        ProxyConnectionRefusedError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.ProxyConnectionRefusedError: 14>
        ProxyConnectionTimeoutError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.ProxyConnectionTimeoutError: 16>
        ProxyNotFoundError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.ProxyNotFoundError: 17>
        ProxyProtocolError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.ProxyProtocolError: 18>
        RemoteHostClosedError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.RemoteHostClosedError: 1>
        SocketAccessError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.SocketAccessError: 3>
        SocketAddressNotAvailableError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.SocketAddressNotAvailableError: 9>
        SocketResourceError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.SocketResourceError: 4>
        SocketTimeoutError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.SocketTimeoutError: 5>
        SslHandshakeFailedError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.SslHandshakeFailedError: 13>
        SslInternalError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.SslInternalError: 20>
        SslInvalidUserDataError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.SslInvalidUserDataError: 21>
        TemporaryError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.TemporaryError: 22>
        UnfinishedSocketOperationError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.UnfinishedSocketOperationError: 11>
        UnknownSocketError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.UnknownSocketError: -1>
        UnsupportedSocketOperationError: typing.ClassVar[QAbstractSocket.SocketError]  # value = <SocketError.UnsupportedSocketOperationError: 10>
    class SocketOption(enum.Enum):
        KeepAliveOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.KeepAliveOption: 1>
        LowDelayOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.LowDelayOption: 0>
        MulticastLoopbackOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.MulticastLoopbackOption: 3>
        MulticastTtlOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.MulticastTtlOption: 2>
        PathMtuSocketOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.PathMtuSocketOption: 7>
        ReceiveBufferSizeSocketOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.ReceiveBufferSizeSocketOption: 6>
        SendBufferSizeSocketOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.SendBufferSizeSocketOption: 5>
        TypeOfServiceOption: typing.ClassVar[QAbstractSocket.SocketOption]  # value = <SocketOption.TypeOfServiceOption: 4>
    class SocketState(enum.Enum):
        BoundState: typing.ClassVar[QAbstractSocket.SocketState]  # value = <SocketState.BoundState: 4>
        ClosingState: typing.ClassVar[QAbstractSocket.SocketState]  # value = <SocketState.ClosingState: 6>
        ConnectedState: typing.ClassVar[QAbstractSocket.SocketState]  # value = <SocketState.ConnectedState: 3>
        ConnectingState: typing.ClassVar[QAbstractSocket.SocketState]  # value = <SocketState.ConnectingState: 2>
        HostLookupState: typing.ClassVar[QAbstractSocket.SocketState]  # value = <SocketState.HostLookupState: 1>
        ListeningState: typing.ClassVar[QAbstractSocket.SocketState]  # value = <SocketState.ListeningState: 5>
        UnconnectedState: typing.ClassVar[QAbstractSocket.SocketState]  # value = <SocketState.UnconnectedState: 0>
    class SocketType(enum.Enum):
        SctpSocket: typing.ClassVar[QAbstractSocket.SocketType]  # value = <SocketType.SctpSocket: 2>
        TcpSocket: typing.ClassVar[QAbstractSocket.SocketType]  # value = <SocketType.TcpSocket: 0>
        UdpSocket: typing.ClassVar[QAbstractSocket.SocketType]  # value = <SocketType.UdpSocket: 1>
        UnknownSocketType: typing.ClassVar[QAbstractSocket.SocketType]  # value = <SocketType.UnknownSocketType: -1>
    @staticmethod
    def abort(*args, **kwargs):
        ...
    @staticmethod
    def bind(*args, **kwargs):
        ...
    @staticmethod
    def bytesAvailable(*args, **kwargs):
        ...
    @staticmethod
    def bytesToWrite(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def connectToHost(*args, **kwargs):
        ...
    @staticmethod
    def connected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def disconnectFromHost(*args, **kwargs):
        ...
    @staticmethod
    def disconnected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorOccurred(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def flush(*args, **kwargs):
        ...
    @staticmethod
    def hostFound(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def isSequential(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def localAddress(*args, **kwargs):
        ...
    @staticmethod
    def localPort(*args, **kwargs):
        ...
    @staticmethod
    def pauseMode(*args, **kwargs):
        ...
    @staticmethod
    def peerAddress(*args, **kwargs):
        ...
    @staticmethod
    def peerName(*args, **kwargs):
        ...
    @staticmethod
    def peerPort(*args, **kwargs):
        ...
    @staticmethod
    def protocolTag(*args, **kwargs):
        ...
    @staticmethod
    def proxy(*args, **kwargs):
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
    def readBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def readData(*args, **kwargs):
        ...
    @staticmethod
    def readLineData(*args, **kwargs):
        ...
    @staticmethod
    def resume(*args, **kwargs):
        ...
    @staticmethod
    def setLocalAddress(*args, **kwargs):
        ...
    @staticmethod
    def setLocalPort(*args, **kwargs):
        ...
    @staticmethod
    def setPauseMode(*args, **kwargs):
        ...
    @staticmethod
    def setPeerAddress(*args, **kwargs):
        ...
    @staticmethod
    def setPeerName(*args, **kwargs):
        ...
    @staticmethod
    def setPeerPort(*args, **kwargs):
        ...
    @staticmethod
    def setProtocolTag(*args, **kwargs):
        ...
    @staticmethod
    def setProxy(*args, **kwargs):
        ...
    @staticmethod
    def setReadBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setSocketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def setSocketError(*args, **kwargs):
        ...
    @staticmethod
    def setSocketOption(*args, **kwargs):
        ...
    @staticmethod
    def setSocketState(*args, **kwargs):
        ...
    @staticmethod
    def skipData(*args, **kwargs):
        ...
    @staticmethod
    def socketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def socketOption(*args, **kwargs):
        ...
    @staticmethod
    def socketType(*args, **kwargs):
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
    def waitForBytesWritten(*args, **kwargs):
        ...
    @staticmethod
    def waitForConnected(*args, **kwargs):
        ...
    @staticmethod
    def waitForDisconnected(*args, **kwargs):
        ...
    @staticmethod
    def waitForReadyRead(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QAuthenticator(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def option(*args, **kwargs):
        ...
    @staticmethod
    def options(*args, **kwargs):
        ...
    @staticmethod
    def password(*args, **kwargs):
        ...
    @staticmethod
    def realm(*args, **kwargs):
        ...
    @staticmethod
    def setOption(*args, **kwargs):
        ...
    @staticmethod
    def setPassword(*args, **kwargs):
        ...
    @staticmethod
    def setUser(*args, **kwargs):
        ...
    @staticmethod
    def user(*args, **kwargs):
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
class QDnsDomainNameRecord(PyQt6.sip.simplewrapper):
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def timeToLive(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QDnsHostAddressRecord(PyQt6.sip.simplewrapper):
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def timeToLive(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QDnsLookup(PyQt6.QtCore.QObject):
    class Error(enum.Enum):
        InvalidReplyError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.InvalidReplyError: 4>
        InvalidRequestError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.InvalidRequestError: 3>
        NoError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.NoError: 0>
        NotFoundError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.NotFoundError: 7>
        OperationCancelledError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.OperationCancelledError: 2>
        ResolverError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.ResolverError: 1>
        ServerFailureError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.ServerFailureError: 5>
        ServerRefusedError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.ServerRefusedError: 6>
        TimeoutError: typing.ClassVar[QDnsLookup.Error]  # value = <Error.TimeoutError: 8>
    class Type(enum.Enum):
        A: typing.ClassVar[QDnsLookup.Type]  # value = <Type.A: 1>
        AAAA: typing.ClassVar[QDnsLookup.Type]  # value = <Type.AAAA: 28>
        ANY: typing.ClassVar[QDnsLookup.Type]  # value = <Type.ANY: 255>
        CNAME: typing.ClassVar[QDnsLookup.Type]  # value = <Type.CNAME: 5>
        MX: typing.ClassVar[QDnsLookup.Type]  # value = <Type.MX: 15>
        NS: typing.ClassVar[QDnsLookup.Type]  # value = <Type.NS: 2>
        PTR: typing.ClassVar[QDnsLookup.Type]  # value = <Type.PTR: 12>
        SRV: typing.ClassVar[QDnsLookup.Type]  # value = <Type.SRV: 33>
        TXT: typing.ClassVar[QDnsLookup.Type]  # value = <Type.TXT: 16>
    @staticmethod
    def abort(*args, **kwargs):
        ...
    @staticmethod
    def canonicalNameRecords(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
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
    def hostAddressRecords(*args, **kwargs):
        ...
    @staticmethod
    def isFinished(*args, **kwargs):
        ...
    @staticmethod
    def lookup(*args, **kwargs):
        ...
    @staticmethod
    def mailExchangeRecords(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def nameChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def nameServerRecords(*args, **kwargs):
        ...
    @staticmethod
    def nameserver(*args, **kwargs):
        ...
    @staticmethod
    def nameserverChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def nameserverPort(*args, **kwargs):
        ...
    @staticmethod
    def nameserverPortChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def pointerRecords(*args, **kwargs):
        ...
    @staticmethod
    def serviceRecords(*args, **kwargs):
        ...
    @staticmethod
    def setName(*args, **kwargs):
        ...
    @staticmethod
    def setNameserver(*args, **kwargs):
        ...
    @staticmethod
    def setNameserverPort(*args, **kwargs):
        ...
    @staticmethod
    def setType(*args, **kwargs):
        ...
    @staticmethod
    def textRecords(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def typeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QDnsMailExchangeRecord(PyQt6.sip.simplewrapper):
    @staticmethod
    def exchange(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def preference(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def timeToLive(*args, **kwargs):
        ...
class QDnsServiceRecord(PyQt6.sip.simplewrapper):
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def port(*args, **kwargs):
        ...
    @staticmethod
    def priority(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def target(*args, **kwargs):
        ...
    @staticmethod
    def timeToLive(*args, **kwargs):
        ...
    @staticmethod
    def weight(*args, **kwargs):
        ...
class QDnsTextRecord(PyQt6.sip.simplewrapper):
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def timeToLive(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class QHostAddress(PyQt6.sip.simplewrapper):
    class ConversionModeFlag(enum.Flag):
        ConvertLocalHost: typing.ClassVar[QHostAddress.ConversionModeFlag]  # value = <ConversionModeFlag.ConvertLocalHost: 8>
        ConvertUnspecifiedAddress: typing.ClassVar[QHostAddress.ConversionModeFlag]  # value = <ConversionModeFlag.ConvertUnspecifiedAddress: 4>
        ConvertV4CompatToIPv4: typing.ClassVar[QHostAddress.ConversionModeFlag]  # value = <ConversionModeFlag.ConvertV4CompatToIPv4: 2>
        ConvertV4MappedToIPv4: typing.ClassVar[QHostAddress.ConversionModeFlag]  # value = <ConversionModeFlag.ConvertV4MappedToIPv4: 1>
    class SpecialAddress(enum.Enum):
        Any: typing.ClassVar[QHostAddress.SpecialAddress]  # value = <SpecialAddress.Any: 4>
        AnyIPv4: typing.ClassVar[QHostAddress.SpecialAddress]  # value = <SpecialAddress.AnyIPv4: 6>
        AnyIPv6: typing.ClassVar[QHostAddress.SpecialAddress]  # value = <SpecialAddress.AnyIPv6: 5>
        Broadcast: typing.ClassVar[QHostAddress.SpecialAddress]  # value = <SpecialAddress.Broadcast: 1>
        LocalHost: typing.ClassVar[QHostAddress.SpecialAddress]  # value = <SpecialAddress.LocalHost: 2>
        LocalHostIPv6: typing.ClassVar[QHostAddress.SpecialAddress]  # value = <SpecialAddress.LocalHostIPv6: 3>
        Null: typing.ClassVar[QHostAddress.SpecialAddress]  # value = <SpecialAddress.Null: 0>
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def isBroadcast(*args, **kwargs):
        ...
    @staticmethod
    def isEqual(*args, **kwargs):
        ...
    @staticmethod
    def isGlobal(*args, **kwargs):
        ...
    @staticmethod
    def isInSubnet(*args, **kwargs):
        ...
    @staticmethod
    def isLinkLocal(*args, **kwargs):
        ...
    @staticmethod
    def isLoopback(*args, **kwargs):
        ...
    @staticmethod
    def isMulticast(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isPrivateUse(*args, **kwargs):
        ...
    @staticmethod
    def isSiteLocal(*args, **kwargs):
        ...
    @staticmethod
    def isUniqueLocalUnicast(*args, **kwargs):
        ...
    @staticmethod
    def parseSubnet(*args, **kwargs):
        ...
    @staticmethod
    def protocol(*args, **kwargs):
        ...
    @staticmethod
    def scopeId(*args, **kwargs):
        ...
    @staticmethod
    def setAddress(*args, **kwargs):
        ...
    @staticmethod
    def setScopeId(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toIPv4Address(*args, **kwargs):
        ...
    @staticmethod
    def toIPv6Address(*args, **kwargs):
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
class QHostInfo(PyQt6.sip.simplewrapper):
    class HostInfoError(enum.Enum):
        HostNotFound: typing.ClassVar[QHostInfo.HostInfoError]  # value = <HostInfoError.HostNotFound: 1>
        NoError: typing.ClassVar[QHostInfo.HostInfoError]  # value = <HostInfoError.NoError: 0>
        UnknownError: typing.ClassVar[QHostInfo.HostInfoError]  # value = <HostInfoError.UnknownError: 2>
    @staticmethod
    def abortHostLookup(*args, **kwargs):
        ...
    @staticmethod
    def addresses(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fromName(*args, **kwargs):
        ...
    @staticmethod
    def hostName(*args, **kwargs):
        ...
    @staticmethod
    def localDomainName(*args, **kwargs):
        ...
    @staticmethod
    def localHostName(*args, **kwargs):
        ...
    @staticmethod
    def lookupHost(*args, **kwargs):
        ...
    @staticmethod
    def lookupId(*args, **kwargs):
        ...
    @staticmethod
    def setAddresses(*args, **kwargs):
        ...
    @staticmethod
    def setError(*args, **kwargs):
        ...
    @staticmethod
    def setErrorString(*args, **kwargs):
        ...
    @staticmethod
    def setHostName(*args, **kwargs):
        ...
    @staticmethod
    def setLookupId(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QHstsPolicy(PyQt6.sip.simplewrapper):
    class PolicyFlag(enum.Flag):
        IncludeSubDomains: typing.ClassVar[QHstsPolicy.PolicyFlag]  # value = <PolicyFlag.IncludeSubDomains: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def expiry(*args, **kwargs):
        ...
    @staticmethod
    def host(*args, **kwargs):
        ...
    @staticmethod
    def includesSubDomains(*args, **kwargs):
        ...
    @staticmethod
    def isExpired(*args, **kwargs):
        ...
    @staticmethod
    def setExpiry(*args, **kwargs):
        ...
    @staticmethod
    def setHost(*args, **kwargs):
        ...
    @staticmethod
    def setIncludesSubDomains(*args, **kwargs):
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
class QHttp1Configuration(PyQt6.sip.simplewrapper):
    @staticmethod
    def numberOfConnectionsPerHost(*args, **kwargs):
        ...
    @staticmethod
    def setNumberOfConnectionsPerHost(*args, **kwargs):
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
class QHttp2Configuration(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def huffmanCompressionEnabled(*args, **kwargs):
        ...
    @staticmethod
    def maxFrameSize(*args, **kwargs):
        ...
    @staticmethod
    def serverPushEnabled(*args, **kwargs):
        ...
    @staticmethod
    def sessionReceiveWindowSize(*args, **kwargs):
        ...
    @staticmethod
    def setHuffmanCompressionEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setMaxFrameSize(*args, **kwargs):
        ...
    @staticmethod
    def setServerPushEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSessionReceiveWindowSize(*args, **kwargs):
        ...
    @staticmethod
    def setStreamReceiveWindowSize(*args, **kwargs):
        ...
    @staticmethod
    def streamReceiveWindowSize(*args, **kwargs):
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
class QHttpHeaders(PyQt6.sip.simplewrapper):
    class WellKnownHeader(enum.Enum):
        AIM: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AIM: 0>
        ALPN: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ALPN: 22>
        Accept: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Accept: 1>
        AcceptAdditions: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptAdditions: 2>
        AcceptCH: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptCH: 3>
        AcceptCharset: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptCharset: 172>
        AcceptDatetime: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptDatetime: 4>
        AcceptEncoding: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptEncoding: 5>
        AcceptFeatures: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptFeatures: 6>
        AcceptLanguage: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptLanguage: 7>
        AcceptPatch: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptPatch: 8>
        AcceptPost: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptPost: 9>
        AcceptRanges: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptRanges: 10>
        AcceptSignature: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AcceptSignature: 11>
        AccessControlAllowCredentials: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlAllowCredentials: 12>
        AccessControlAllowHeaders: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlAllowHeaders: 13>
        AccessControlAllowMethods: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlAllowMethods: 14>
        AccessControlAllowOrigin: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlAllowOrigin: 15>
        AccessControlExposeHeaders: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlExposeHeaders: 16>
        AccessControlMaxAge: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlMaxAge: 17>
        AccessControlRequestHeaders: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlRequestHeaders: 18>
        AccessControlRequestMethod: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AccessControlRequestMethod: 19>
        Age: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Age: 20>
        Allow: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Allow: 21>
        AltSvc: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AltSvc: 23>
        AltUsed: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AltUsed: 24>
        Alternates: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Alternates: 25>
        ApplyToRedirectRef: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ApplyToRedirectRef: 26>
        AuthenticationControl: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AuthenticationControl: 27>
        AuthenticationInfo: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.AuthenticationInfo: 28>
        Authorization: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Authorization: 29>
        CDNCacheControl: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CDNCacheControl: 35>
        CDNLoop: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CDNLoop: 36>
        CPEPInfo: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CPEPInfo: 173>
        CacheControl: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CacheControl: 30>
        CacheStatus: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CacheStatus: 31>
        CalDAVTimezones: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CalDAVTimezones: 33>
        CalManagedID: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CalManagedID: 32>
        CapsuleProtocol: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CapsuleProtocol: 34>
        CertNotAfter: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CertNotAfter: 37>
        CertNotBefore: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CertNotBefore: 38>
        ClearSiteData: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ClearSiteData: 39>
        ClientCert: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ClientCert: 40>
        ClientCertChain: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ClientCertChain: 41>
        Close: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Close: 42>
        Connection: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Connection: 43>
        ContentDigest: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentDigest: 44>
        ContentDisposition: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentDisposition: 45>
        ContentEncoding: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentEncoding: 46>
        ContentID: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentID: 47>
        ContentLanguage: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentLanguage: 48>
        ContentLength: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentLength: 49>
        ContentLocation: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentLocation: 50>
        ContentRange: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentRange: 51>
        ContentSecurityPolicy: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentSecurityPolicy: 52>
        ContentSecurityPolicyReportOnly: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentSecurityPolicyReportOnly: 53>
        ContentType: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ContentType: 54>
        Cookie: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Cookie: 55>
        CrossOriginEmbedderPolicy: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CrossOriginEmbedderPolicy: 56>
        CrossOriginEmbedderPolicyReportOnly: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CrossOriginEmbedderPolicyReportOnly: 57>
        CrossOriginOpenerPolicy: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CrossOriginOpenerPolicy: 58>
        CrossOriginOpenerPolicyReportOnly: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CrossOriginOpenerPolicyReportOnly: 59>
        CrossOriginResourcePolicy: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.CrossOriginResourcePolicy: 60>
        DASL: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.DASL: 61>
        DAV: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.DAV: 63>
        DPoP: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.DPoP: 68>
        DPoPNonce: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.DPoPNonce: 69>
        Date: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Date: 62>
        DeltaBase: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.DeltaBase: 64>
        Depth: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Depth: 65>
        Destination: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Destination: 66>
        DifferentialID: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.DifferentialID: 67>
        ETag: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ETag: 71>
        EarlyData: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.EarlyData: 70>
        Expect: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Expect: 72>
        ExpectCT: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ExpectCT: 73>
        Expires: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Expires: 74>
        Forwarded: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Forwarded: 75>
        From: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.From: 76>
        Hobareg: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Hobareg: 77>
        Host: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Host: 78>
        IM: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IM: 86>
        If: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.If: 79>
        IfMatch: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IfMatch: 80>
        IfModifiedSince: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IfModifiedSince: 81>
        IfNoneMatch: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IfNoneMatch: 82>
        IfRange: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IfRange: 83>
        IfScheduleTagMatch: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IfScheduleTagMatch: 84>
        IfUnmodifiedSince: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IfUnmodifiedSince: 85>
        IncludeReferredTokenBindingID: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.IncludeReferredTokenBindingID: 87>
        KeepAlive: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.KeepAlive: 88>
        Label: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Label: 89>
        LastEventID: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.LastEventID: 90>
        LastModified: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.LastModified: 91>
        Link: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Link: 92>
        Location: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Location: 93>
        LockToken: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.LockToken: 94>
        MIMEVersion: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.MIMEVersion: 98>
        MaxForwards: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.MaxForwards: 95>
        MementoDatetime: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.MementoDatetime: 96>
        Meter: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Meter: 97>
        NEL: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.NEL: 100>
        Negotiate: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Negotiate: 99>
        ODataEntityId: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ODataEntityId: 101>
        ODataIsolation: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ODataIsolation: 102>
        ODataMaxVersion: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ODataMaxVersion: 103>
        ODataVersion: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ODataVersion: 104>
        OSCORE: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.OSCORE: 109>
        OSLCCoreVersion: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.OSLCCoreVersion: 110>
        OptionalWWWAuthenticate: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.OptionalWWWAuthenticate: 105>
        OrderingType: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.OrderingType: 106>
        Origin: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Origin: 107>
        OriginAgentCluster: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.OriginAgentCluster: 108>
        Overwrite: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Overwrite: 111>
        PingFrom: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.PingFrom: 112>
        PingTo: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.PingTo: 113>
        Position: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Position: 114>
        Pragma: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Pragma: 174>
        Prefer: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Prefer: 115>
        PreferenceApplied: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.PreferenceApplied: 116>
        Priority: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Priority: 117>
        ProtocolInfo: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ProtocolInfo: 175>
        ProtocolQuery: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ProtocolQuery: 176>
        ProxyAuthenticate: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ProxyAuthenticate: 118>
        ProxyAuthenticationInfo: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ProxyAuthenticationInfo: 119>
        ProxyAuthorization: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ProxyAuthorization: 120>
        ProxyStatus: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ProxyStatus: 121>
        PublicKeyPins: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.PublicKeyPins: 122>
        PublicKeyPinsReportOnly: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.PublicKeyPinsReportOnly: 123>
        Range: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Range: 124>
        RedirectRef: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.RedirectRef: 125>
        Referer: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Referer: 126>
        Refresh: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Refresh: 127>
        ReplayNonce: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ReplayNonce: 128>
        ReprDigest: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ReprDigest: 129>
        RetryAfter: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.RetryAfter: 130>
        SLUG: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SLUG: 145>
        ScheduleReply: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ScheduleReply: 131>
        ScheduleTag: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ScheduleTag: 132>
        SecPurpose: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SecPurpose: 133>
        SecTokenBinding: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SecTokenBinding: 134>
        SecWebSocketAccept: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SecWebSocketAccept: 135>
        SecWebSocketExtensions: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SecWebSocketExtensions: 136>
        SecWebSocketKey: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SecWebSocketKey: 137>
        SecWebSocketProtocol: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SecWebSocketProtocol: 138>
        SecWebSocketVersion: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SecWebSocketVersion: 139>
        Server: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Server: 140>
        ServerTiming: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.ServerTiming: 141>
        SetCookie: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SetCookie: 142>
        Signature: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Signature: 143>
        SignatureInput: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SignatureInput: 144>
        SoapAction: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SoapAction: 146>
        StatusURI: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.StatusURI: 147>
        StrictTransportSecurity: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.StrictTransportSecurity: 148>
        Sunset: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Sunset: 149>
        SurrogateCapability: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SurrogateCapability: 150>
        SurrogateControl: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.SurrogateControl: 151>
        TCN: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.TCN: 152>
        TE: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.TE: 153>
        TTL: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.TTL: 160>
        Timeout: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Timeout: 154>
        Topic: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Topic: 155>
        Traceparent: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Traceparent: 156>
        Tracestate: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Tracestate: 157>
        Trailer: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Trailer: 158>
        TransferEncoding: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.TransferEncoding: 159>
        Upgrade: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Upgrade: 161>
        Urgency: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Urgency: 162>
        UserAgent: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.UserAgent: 163>
        VariantVary: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.VariantVary: 164>
        Vary: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Vary: 165>
        Via: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.Via: 166>
        WWWAuthenticate: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.WWWAuthenticate: 169>
        WantContentDigest: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.WantContentDigest: 167>
        WantReprDigest: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.WantReprDigest: 168>
        XContentTypeOptions: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.XContentTypeOptions: 170>
        XFrameOptions: typing.ClassVar[QHttpHeaders.WellKnownHeader]  # value = <WellKnownHeader.XFrameOptions: 171>
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def combinedValue(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def fromListOfPairs(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def nameAt(*args, **kwargs):
        ...
    @staticmethod
    def removeAll(*args, **kwargs):
        ...
    @staticmethod
    def removeAt(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @staticmethod
    def reserve(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toListOfPairs(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def valueAt(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
    @staticmethod
    def wellKnownHeaderName(*args, **kwargs):
        ...
class QHttpMultiPart(PyQt6.QtCore.QObject):
    class ContentType(enum.Enum):
        AlternativeType: typing.ClassVar[QHttpMultiPart.ContentType]  # value = <ContentType.AlternativeType: 3>
        FormDataType: typing.ClassVar[QHttpMultiPart.ContentType]  # value = <ContentType.FormDataType: 2>
        MixedType: typing.ClassVar[QHttpMultiPart.ContentType]  # value = <ContentType.MixedType: 0>
        RelatedType: typing.ClassVar[QHttpMultiPart.ContentType]  # value = <ContentType.RelatedType: 1>
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def boundary(*args, **kwargs):
        ...
    @staticmethod
    def setBoundary(*args, **kwargs):
        ...
    @staticmethod
    def setContentType(*args, **kwargs):
        ...
class QHttpPart(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def setBody(*args, **kwargs):
        ...
    @staticmethod
    def setBodyDevice(*args, **kwargs):
        ...
    @staticmethod
    def setHeader(*args, **kwargs):
        ...
    @staticmethod
    def setRawHeader(*args, **kwargs):
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
class QLocalServer(PyQt6.QtCore.QObject):
    class SocketOption(enum.Flag):
        AbstractNamespaceOption: typing.ClassVar[QLocalServer.SocketOption]  # value = <SocketOption.AbstractNamespaceOption: 8>
        GroupAccessOption: typing.ClassVar[QLocalServer.SocketOption]  # value = <SocketOption.GroupAccessOption: 2>
        OtherAccessOption: typing.ClassVar[QLocalServer.SocketOption]  # value = <SocketOption.OtherAccessOption: 4>
        UserAccessOption: typing.ClassVar[QLocalServer.SocketOption]  # value = <SocketOption.UserAccessOption: 1>
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fullServerName(*args, **kwargs):
        ...
    @staticmethod
    def hasPendingConnections(*args, **kwargs):
        ...
    @staticmethod
    def incomingConnection(*args, **kwargs):
        ...
    @staticmethod
    def isListening(*args, **kwargs):
        ...
    @staticmethod
    def listen(*args, **kwargs):
        ...
    @staticmethod
    def listenBacklogSize(*args, **kwargs):
        ...
    @staticmethod
    def maxPendingConnections(*args, **kwargs):
        ...
    @staticmethod
    def newConnection(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def nextPendingConnection(*args, **kwargs):
        ...
    @staticmethod
    def removeServer(*args, **kwargs):
        ...
    @staticmethod
    def serverError(*args, **kwargs):
        ...
    @staticmethod
    def serverName(*args, **kwargs):
        ...
    @staticmethod
    def setListenBacklogSize(*args, **kwargs):
        ...
    @staticmethod
    def setMaxPendingConnections(*args, **kwargs):
        ...
    @staticmethod
    def setSocketOptions(*args, **kwargs):
        ...
    @staticmethod
    def socketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def socketOptions(*args, **kwargs):
        ...
    @staticmethod
    def waitForNewConnection(*args, **kwargs):
        ...
class QLocalSocket(PyQt6.QtCore.QIODevice):
    class LocalSocketError(enum.Enum):
        ConnectionError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.ConnectionError: 7>
        ConnectionRefusedError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.ConnectionRefusedError: 0>
        DatagramTooLargeError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.DatagramTooLargeError: 6>
        OperationError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.OperationError: 19>
        PeerClosedError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.PeerClosedError: 1>
        ServerNotFoundError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.ServerNotFoundError: 2>
        SocketAccessError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.SocketAccessError: 3>
        SocketResourceError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.SocketResourceError: 4>
        SocketTimeoutError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.SocketTimeoutError: 5>
        UnknownSocketError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.UnknownSocketError: -1>
        UnsupportedSocketOperationError: typing.ClassVar[QLocalSocket.LocalSocketError]  # value = <LocalSocketError.UnsupportedSocketOperationError: 10>
    class LocalSocketState(enum.Enum):
        ClosingState: typing.ClassVar[QLocalSocket.LocalSocketState]  # value = <LocalSocketState.ClosingState: 6>
        ConnectedState: typing.ClassVar[QLocalSocket.LocalSocketState]  # value = <LocalSocketState.ConnectedState: 3>
        ConnectingState: typing.ClassVar[QLocalSocket.LocalSocketState]  # value = <LocalSocketState.ConnectingState: 2>
        UnconnectedState: typing.ClassVar[QLocalSocket.LocalSocketState]  # value = <LocalSocketState.UnconnectedState: 0>
    class SocketOption(enum.Flag):
        AbstractNamespaceOption: typing.ClassVar[QLocalSocket.SocketOption]  # value = <SocketOption.AbstractNamespaceOption: 1>
    @staticmethod
    def abort(*args, **kwargs):
        ...
    @staticmethod
    def bytesAvailable(*args, **kwargs):
        ...
    @staticmethod
    def bytesToWrite(*args, **kwargs):
        ...
    @staticmethod
    def canReadLine(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def connectToServer(*args, **kwargs):
        ...
    @staticmethod
    def connected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def disconnectFromServer(*args, **kwargs):
        ...
    @staticmethod
    def disconnected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorOccurred(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def flush(*args, **kwargs):
        ...
    @staticmethod
    def fullServerName(*args, **kwargs):
        ...
    @staticmethod
    def isSequential(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def readBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def readData(*args, **kwargs):
        ...
    @staticmethod
    def readLineData(*args, **kwargs):
        ...
    @staticmethod
    def serverName(*args, **kwargs):
        ...
    @staticmethod
    def setReadBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setServerName(*args, **kwargs):
        ...
    @staticmethod
    def setSocketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def setSocketOptions(*args, **kwargs):
        ...
    @staticmethod
    def skipData(*args, **kwargs):
        ...
    @staticmethod
    def socketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def socketOptions(*args, **kwargs):
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
    def waitForBytesWritten(*args, **kwargs):
        ...
    @staticmethod
    def waitForConnected(*args, **kwargs):
        ...
    @staticmethod
    def waitForDisconnected(*args, **kwargs):
        ...
    @staticmethod
    def waitForReadyRead(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QNetworkAccessManager(PyQt6.QtCore.QObject):
    class Operation(enum.Enum):
        CustomOperation: typing.ClassVar[QNetworkAccessManager.Operation]  # value = <Operation.CustomOperation: 6>
        DeleteOperation: typing.ClassVar[QNetworkAccessManager.Operation]  # value = <Operation.DeleteOperation: 5>
        GetOperation: typing.ClassVar[QNetworkAccessManager.Operation]  # value = <Operation.GetOperation: 2>
        HeadOperation: typing.ClassVar[QNetworkAccessManager.Operation]  # value = <Operation.HeadOperation: 1>
        PostOperation: typing.ClassVar[QNetworkAccessManager.Operation]  # value = <Operation.PostOperation: 4>
        PutOperation: typing.ClassVar[QNetworkAccessManager.Operation]  # value = <Operation.PutOperation: 3>
    @staticmethod
    def addStrictTransportSecurityHosts(*args, **kwargs):
        ...
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
    def autoDeleteReplies(*args, **kwargs):
        ...
    @staticmethod
    def cache(*args, **kwargs):
        ...
    @staticmethod
    def clearAccessCache(*args, **kwargs):
        ...
    @staticmethod
    def clearConnectionCache(*args, **kwargs):
        ...
    @staticmethod
    def connectToHost(*args, **kwargs):
        ...
    @staticmethod
    def connectToHostEncrypted(*args, **kwargs):
        ...
    @staticmethod
    def cookieJar(*args, **kwargs):
        ...
    @staticmethod
    def createRequest(*args, **kwargs):
        ...
    @staticmethod
    def deleteResource(*args, **kwargs):
        ...
    @staticmethod
    def enableStrictTransportSecurityStore(*args, **kwargs):
        ...
    @staticmethod
    def encrypted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
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
    def get(*args, **kwargs):
        ...
    @staticmethod
    def head(*args, **kwargs):
        ...
    @staticmethod
    def isStrictTransportSecurityEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isStrictTransportSecurityStoreEnabled(*args, **kwargs):
        ...
    @staticmethod
    def post(*args, **kwargs):
        ...
    @staticmethod
    def preSharedKeyAuthenticationRequired(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def proxy(*args, **kwargs):
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
    def proxyFactory(*args, **kwargs):
        ...
    @staticmethod
    def put(*args, **kwargs):
        ...
    @staticmethod
    def redirectPolicy(*args, **kwargs):
        ...
    @staticmethod
    def sendCustomRequest(*args, **kwargs):
        ...
    @staticmethod
    def setAutoDeleteReplies(*args, **kwargs):
        ...
    @staticmethod
    def setCache(*args, **kwargs):
        ...
    @staticmethod
    def setCookieJar(*args, **kwargs):
        ...
    @staticmethod
    def setProxy(*args, **kwargs):
        ...
    @staticmethod
    def setProxyFactory(*args, **kwargs):
        ...
    @staticmethod
    def setRedirectPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setStrictTransportSecurityEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setTransferTimeout(*args, **kwargs):
        ...
    @staticmethod
    def sslErrors(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def strictTransportSecurityHosts(*args, **kwargs):
        ...
    @staticmethod
    def supportedSchemes(*args, **kwargs):
        ...
    @staticmethod
    def supportedSchemesImplementation(*args, **kwargs):
        ...
    @staticmethod
    def transferTimeout(*args, **kwargs):
        ...
class QNetworkAddressEntry(PyQt6.sip.simplewrapper):
    class DnsEligibilityStatus(enum.Enum):
        DnsEligibilityUnknown: typing.ClassVar[QNetworkAddressEntry.DnsEligibilityStatus]  # value = <DnsEligibilityStatus.DnsEligibilityUnknown: -1>
        DnsEligible: typing.ClassVar[QNetworkAddressEntry.DnsEligibilityStatus]  # value = <DnsEligibilityStatus.DnsEligible: 1>
        DnsIneligible: typing.ClassVar[QNetworkAddressEntry.DnsEligibilityStatus]  # value = <DnsEligibilityStatus.DnsIneligible: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def broadcast(*args, **kwargs):
        ...
    @staticmethod
    def clearAddressLifetime(*args, **kwargs):
        ...
    @staticmethod
    def dnsEligibility(*args, **kwargs):
        ...
    @staticmethod
    def ip(*args, **kwargs):
        ...
    @staticmethod
    def isLifetimeKnown(*args, **kwargs):
        ...
    @staticmethod
    def isPermanent(*args, **kwargs):
        ...
    @staticmethod
    def isTemporary(*args, **kwargs):
        ...
    @staticmethod
    def netmask(*args, **kwargs):
        ...
    @staticmethod
    def preferredLifetime(*args, **kwargs):
        ...
    @staticmethod
    def prefixLength(*args, **kwargs):
        ...
    @staticmethod
    def setAddressLifetime(*args, **kwargs):
        ...
    @staticmethod
    def setBroadcast(*args, **kwargs):
        ...
    @staticmethod
    def setDnsEligibility(*args, **kwargs):
        ...
    @staticmethod
    def setIp(*args, **kwargs):
        ...
    @staticmethod
    def setNetmask(*args, **kwargs):
        ...
    @staticmethod
    def setPrefixLength(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def validityLifetime(*args, **kwargs):
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
class QNetworkCacheMetaData(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def attributes(*args, **kwargs):
        ...
    @staticmethod
    def expirationDate(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastModified(*args, **kwargs):
        ...
    @staticmethod
    def rawHeaders(*args, **kwargs):
        ...
    @staticmethod
    def saveToDisk(*args, **kwargs):
        ...
    @staticmethod
    def setAttributes(*args, **kwargs):
        ...
    @staticmethod
    def setExpirationDate(*args, **kwargs):
        ...
    @staticmethod
    def setLastModified(*args, **kwargs):
        ...
    @staticmethod
    def setRawHeaders(*args, **kwargs):
        ...
    @staticmethod
    def setSaveToDisk(*args, **kwargs):
        ...
    @staticmethod
    def setUrl(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
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
class QNetworkCookie(PyQt6.sip.simplewrapper):
    class RawForm(enum.Enum):
        Full: typing.ClassVar[QNetworkCookie.RawForm]  # value = <RawForm.Full: 1>
        NameAndValueOnly: typing.ClassVar[QNetworkCookie.RawForm]  # value = <RawForm.NameAndValueOnly: 0>
    class SameSite(enum.Enum):
        Default: typing.ClassVar[QNetworkCookie.SameSite]  # value = <SameSite.Default: 0>
        Lax: typing.ClassVar[QNetworkCookie.SameSite]  # value = <SameSite.Lax: 2>
        None_: typing.ClassVar[QNetworkCookie.SameSite]  # value = <SameSite.None_: 1>
        Strict: typing.ClassVar[QNetworkCookie.SameSite]  # value = <SameSite.Strict: 3>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def domain(*args, **kwargs):
        ...
    @staticmethod
    def expirationDate(*args, **kwargs):
        ...
    @staticmethod
    def hasSameIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def isHttpOnly(*args, **kwargs):
        ...
    @staticmethod
    def isSecure(*args, **kwargs):
        ...
    @staticmethod
    def isSessionCookie(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def normalize(*args, **kwargs):
        ...
    @staticmethod
    def parseCookies(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
    @staticmethod
    def sameSitePolicy(*args, **kwargs):
        ...
    @staticmethod
    def setDomain(*args, **kwargs):
        ...
    @staticmethod
    def setExpirationDate(*args, **kwargs):
        ...
    @staticmethod
    def setHttpOnly(*args, **kwargs):
        ...
    @staticmethod
    def setName(*args, **kwargs):
        ...
    @staticmethod
    def setPath(*args, **kwargs):
        ...
    @staticmethod
    def setSameSitePolicy(*args, **kwargs):
        ...
    @staticmethod
    def setSecure(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toRawForm(*args, **kwargs):
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
class QNetworkCookieJar(PyQt6.QtCore.QObject):
    @staticmethod
    def allCookies(*args, **kwargs):
        ...
    @staticmethod
    def cookiesForUrl(*args, **kwargs):
        ...
    @staticmethod
    def deleteCookie(*args, **kwargs):
        ...
    @staticmethod
    def insertCookie(*args, **kwargs):
        ...
    @staticmethod
    def setAllCookies(*args, **kwargs):
        ...
    @staticmethod
    def setCookiesFromUrl(*args, **kwargs):
        ...
    @staticmethod
    def updateCookie(*args, **kwargs):
        ...
    @staticmethod
    def validateCookie(*args, **kwargs):
        ...
class QNetworkDatagram(PyQt6.sip.simplewrapper):
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def destinationAddress(*args, **kwargs):
        ...
    @staticmethod
    def destinationPort(*args, **kwargs):
        ...
    @staticmethod
    def hopLimit(*args, **kwargs):
        ...
    @staticmethod
    def interfaceIndex(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def makeReply(*args, **kwargs):
        ...
    @staticmethod
    def senderAddress(*args, **kwargs):
        ...
    @staticmethod
    def senderPort(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setDestination(*args, **kwargs):
        ...
    @staticmethod
    def setHopLimit(*args, **kwargs):
        ...
    @staticmethod
    def setInterfaceIndex(*args, **kwargs):
        ...
    @staticmethod
    def setSender(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QNetworkDiskCache(QAbstractNetworkCache):
    @staticmethod
    def cacheDirectory(*args, **kwargs):
        ...
    @staticmethod
    def cacheSize(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def expire(*args, **kwargs):
        ...
    @staticmethod
    def fileMetaData(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def maximumCacheSize(*args, **kwargs):
        ...
    @staticmethod
    def metaData(*args, **kwargs):
        ...
    @staticmethod
    def prepare(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def setCacheDirectory(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumCacheSize(*args, **kwargs):
        ...
    @staticmethod
    def updateMetaData(*args, **kwargs):
        ...
class QNetworkInformation(PyQt6.QtCore.QObject):
    class Feature(enum.Enum):
        CaptivePortal: typing.ClassVar[QNetworkInformation.Feature]  # value = <Feature.CaptivePortal: 2>
        Metered: typing.ClassVar[QNetworkInformation.Feature]  # value = <Feature.Metered: 8>
        Reachability: typing.ClassVar[QNetworkInformation.Feature]  # value = <Feature.Reachability: 1>
        TransportMedium: typing.ClassVar[QNetworkInformation.Feature]  # value = <Feature.TransportMedium: 4>
    class Reachability(enum.Enum):
        Disconnected: typing.ClassVar[QNetworkInformation.Reachability]  # value = <Reachability.Disconnected: 1>
        Local: typing.ClassVar[QNetworkInformation.Reachability]  # value = <Reachability.Local: 2>
        Online: typing.ClassVar[QNetworkInformation.Reachability]  # value = <Reachability.Online: 4>
        Site: typing.ClassVar[QNetworkInformation.Reachability]  # value = <Reachability.Site: 3>
        Unknown: typing.ClassVar[QNetworkInformation.Reachability]  # value = <Reachability.Unknown: 0>
    class TransportMedium(enum.Enum):
        Bluetooth: typing.ClassVar[QNetworkInformation.TransportMedium]  # value = <TransportMedium.Bluetooth: 4>
        Cellular: typing.ClassVar[QNetworkInformation.TransportMedium]  # value = <TransportMedium.Cellular: 2>
        Ethernet: typing.ClassVar[QNetworkInformation.TransportMedium]  # value = <TransportMedium.Ethernet: 1>
        Unknown: typing.ClassVar[QNetworkInformation.TransportMedium]  # value = <TransportMedium.Unknown: 0>
        WiFi: typing.ClassVar[QNetworkInformation.TransportMedium]  # value = <TransportMedium.WiFi: 3>
    @staticmethod
    def availableBackends(*args, **kwargs):
        ...
    @staticmethod
    def backendName(*args, **kwargs):
        ...
    @staticmethod
    def instance(*args, **kwargs):
        ...
    @staticmethod
    def isBehindCaptivePortal(*args, **kwargs):
        ...
    @staticmethod
    def isBehindCaptivePortalChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def isMetered(*args, **kwargs):
        ...
    @staticmethod
    def isMeteredChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def loadBackendByFeatures(*args, **kwargs):
        ...
    @staticmethod
    def loadBackendByName(*args, **kwargs):
        ...
    @staticmethod
    def loadDefaultBackend(*args, **kwargs):
        ...
    @staticmethod
    def reachability(*args, **kwargs):
        ...
    @staticmethod
    def reachabilityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def supportedFeatures(*args, **kwargs):
        ...
    @staticmethod
    def supports(*args, **kwargs):
        ...
    @staticmethod
    def transportMedium(*args, **kwargs):
        ...
    @staticmethod
    def transportMediumChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QNetworkInterface(PyQt6.sip.simplewrapper):
    class InterfaceFlag(enum.Flag):
        CanBroadcast: typing.ClassVar[QNetworkInterface.InterfaceFlag]  # value = <InterfaceFlag.CanBroadcast: 4>
        CanMulticast: typing.ClassVar[QNetworkInterface.InterfaceFlag]  # value = <InterfaceFlag.CanMulticast: 32>
        IsLoopBack: typing.ClassVar[QNetworkInterface.InterfaceFlag]  # value = <InterfaceFlag.IsLoopBack: 8>
        IsPointToPoint: typing.ClassVar[QNetworkInterface.InterfaceFlag]  # value = <InterfaceFlag.IsPointToPoint: 16>
        IsRunning: typing.ClassVar[QNetworkInterface.InterfaceFlag]  # value = <InterfaceFlag.IsRunning: 2>
        IsUp: typing.ClassVar[QNetworkInterface.InterfaceFlag]  # value = <InterfaceFlag.IsUp: 1>
    class InterfaceType(enum.Enum):
        CanBus: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.CanBus: 5>
        Ethernet: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Ethernet: 3>
        Fddi: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Fddi: 7>
        Ieee1394: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Ieee1394: 13>
        Ieee802154: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Ieee802154: 10>
        Ieee80216: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Ieee80216: 12>
        Loopback: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Loopback: 1>
        Phonet: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Phonet: 9>
        Ppp: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Ppp: 6>
        SixLoWPAN: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.SixLoWPAN: 11>
        Slip: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Slip: 4>
        Unknown: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Unknown: 0>
        Virtual: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Virtual: 2>
        Wifi: typing.ClassVar[QNetworkInterface.InterfaceType]  # value = <InterfaceType.Wifi: 8>
    @staticmethod
    def addressEntries(*args, **kwargs):
        ...
    @staticmethod
    def allAddresses(*args, **kwargs):
        ...
    @staticmethod
    def allInterfaces(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def hardwareAddress(*args, **kwargs):
        ...
    @staticmethod
    def humanReadableName(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def interfaceFromIndex(*args, **kwargs):
        ...
    @staticmethod
    def interfaceFromName(*args, **kwargs):
        ...
    @staticmethod
    def interfaceIndexFromName(*args, **kwargs):
        ...
    @staticmethod
    def interfaceNameFromIndex(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def maximumTransmissionUnit(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QNetworkProxy(PyQt6.sip.simplewrapper):
    class Capability(enum.Flag):
        CachingCapability: typing.ClassVar[QNetworkProxy.Capability]  # value = <Capability.CachingCapability: 8>
        HostNameLookupCapability: typing.ClassVar[QNetworkProxy.Capability]  # value = <Capability.HostNameLookupCapability: 16>
        ListeningCapability: typing.ClassVar[QNetworkProxy.Capability]  # value = <Capability.ListeningCapability: 2>
        SctpListeningCapability: typing.ClassVar[QNetworkProxy.Capability]  # value = <Capability.SctpListeningCapability: 64>
        SctpTunnelingCapability: typing.ClassVar[QNetworkProxy.Capability]  # value = <Capability.SctpTunnelingCapability: 32>
        TunnelingCapability: typing.ClassVar[QNetworkProxy.Capability]  # value = <Capability.TunnelingCapability: 1>
        UdpTunnelingCapability: typing.ClassVar[QNetworkProxy.Capability]  # value = <Capability.UdpTunnelingCapability: 4>
    class ProxyType(enum.Enum):
        DefaultProxy: typing.ClassVar[QNetworkProxy.ProxyType]  # value = <ProxyType.DefaultProxy: 0>
        FtpCachingProxy: typing.ClassVar[QNetworkProxy.ProxyType]  # value = <ProxyType.FtpCachingProxy: 5>
        HttpCachingProxy: typing.ClassVar[QNetworkProxy.ProxyType]  # value = <ProxyType.HttpCachingProxy: 4>
        HttpProxy: typing.ClassVar[QNetworkProxy.ProxyType]  # value = <ProxyType.HttpProxy: 3>
        NoProxy: typing.ClassVar[QNetworkProxy.ProxyType]  # value = <ProxyType.NoProxy: 2>
        Socks5Proxy: typing.ClassVar[QNetworkProxy.ProxyType]  # value = <ProxyType.Socks5Proxy: 1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def applicationProxy(*args, **kwargs):
        ...
    @staticmethod
    def capabilities(*args, **kwargs):
        ...
    @staticmethod
    def hasRawHeader(*args, **kwargs):
        ...
    @staticmethod
    def header(*args, **kwargs):
        ...
    @staticmethod
    def hostName(*args, **kwargs):
        ...
    @staticmethod
    def isCachingProxy(*args, **kwargs):
        ...
    @staticmethod
    def isTransparentProxy(*args, **kwargs):
        ...
    @staticmethod
    def password(*args, **kwargs):
        ...
    @staticmethod
    def port(*args, **kwargs):
        ...
    @staticmethod
    def rawHeader(*args, **kwargs):
        ...
    @staticmethod
    def rawHeaderList(*args, **kwargs):
        ...
    @staticmethod
    def setApplicationProxy(*args, **kwargs):
        ...
    @staticmethod
    def setCapabilities(*args, **kwargs):
        ...
    @staticmethod
    def setHeader(*args, **kwargs):
        ...
    @staticmethod
    def setHostName(*args, **kwargs):
        ...
    @staticmethod
    def setPassword(*args, **kwargs):
        ...
    @staticmethod
    def setPort(*args, **kwargs):
        ...
    @staticmethod
    def setRawHeader(*args, **kwargs):
        ...
    @staticmethod
    def setType(*args, **kwargs):
        ...
    @staticmethod
    def setUser(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def user(*args, **kwargs):
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
class QNetworkProxyFactory(PyQt6.sip.wrapper):
    @staticmethod
    def proxyForQuery(*args, **kwargs):
        ...
    @staticmethod
    def queryProxy(*args, **kwargs):
        ...
    @staticmethod
    def setApplicationProxyFactory(*args, **kwargs):
        ...
    @staticmethod
    def setUseSystemConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def systemProxyForQuery(*args, **kwargs):
        ...
    @staticmethod
    def usesSystemConfiguration(*args, **kwargs):
        ...
class QNetworkProxyQuery(PyQt6.sip.simplewrapper):
    class QueryType(enum.Enum):
        SctpServer: typing.ClassVar[QNetworkProxyQuery.QueryType]  # value = <QueryType.SctpServer: 102>
        SctpSocket: typing.ClassVar[QNetworkProxyQuery.QueryType]  # value = <QueryType.SctpSocket: 2>
        TcpServer: typing.ClassVar[QNetworkProxyQuery.QueryType]  # value = <QueryType.TcpServer: 100>
        TcpSocket: typing.ClassVar[QNetworkProxyQuery.QueryType]  # value = <QueryType.TcpSocket: 0>
        UdpSocket: typing.ClassVar[QNetworkProxyQuery.QueryType]  # value = <QueryType.UdpSocket: 1>
        UrlRequest: typing.ClassVar[QNetworkProxyQuery.QueryType]  # value = <QueryType.UrlRequest: 101>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def localPort(*args, **kwargs):
        ...
    @staticmethod
    def peerHostName(*args, **kwargs):
        ...
    @staticmethod
    def peerPort(*args, **kwargs):
        ...
    @staticmethod
    def protocolTag(*args, **kwargs):
        ...
    @staticmethod
    def queryType(*args, **kwargs):
        ...
    @staticmethod
    def setLocalPort(*args, **kwargs):
        ...
    @staticmethod
    def setPeerHostName(*args, **kwargs):
        ...
    @staticmethod
    def setPeerPort(*args, **kwargs):
        ...
    @staticmethod
    def setProtocolTag(*args, **kwargs):
        ...
    @staticmethod
    def setQueryType(*args, **kwargs):
        ...
    @staticmethod
    def setUrl(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
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
class QNetworkReply(PyQt6.QtCore.QIODevice):
    class NetworkError(enum.Enum):
        AuthenticationRequiredError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.AuthenticationRequiredError: 204>
        BackgroundRequestNotAllowedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.BackgroundRequestNotAllowedError: 9>
        ConnectionRefusedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ConnectionRefusedError: 1>
        ContentAccessDenied: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ContentAccessDenied: 201>
        ContentConflictError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ContentConflictError: 206>
        ContentGoneError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ContentGoneError: 207>
        ContentNotFoundError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ContentNotFoundError: 203>
        ContentOperationNotPermittedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ContentOperationNotPermittedError: 202>
        ContentReSendError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ContentReSendError: 205>
        HostNotFoundError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.HostNotFoundError: 3>
        InsecureRedirectError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.InsecureRedirectError: 11>
        InternalServerError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.InternalServerError: 401>
        NetworkSessionFailedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.NetworkSessionFailedError: 8>
        NoError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.NoError: 0>
        OperationCanceledError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.OperationCanceledError: 5>
        OperationNotImplementedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.OperationNotImplementedError: 402>
        ProtocolFailure: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProtocolFailure: 399>
        ProtocolInvalidOperationError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProtocolInvalidOperationError: 302>
        ProtocolUnknownError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProtocolUnknownError: 301>
        ProxyAuthenticationRequiredError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProxyAuthenticationRequiredError: 105>
        ProxyConnectionClosedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProxyConnectionClosedError: 102>
        ProxyConnectionRefusedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProxyConnectionRefusedError: 101>
        ProxyNotFoundError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProxyNotFoundError: 103>
        ProxyTimeoutError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ProxyTimeoutError: 104>
        RemoteHostClosedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.RemoteHostClosedError: 2>
        ServiceUnavailableError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.ServiceUnavailableError: 403>
        SslHandshakeFailedError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.SslHandshakeFailedError: 6>
        TemporaryNetworkFailureError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.TemporaryNetworkFailureError: 7>
        TimeoutError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.TimeoutError: 4>
        TooManyRedirectsError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.TooManyRedirectsError: 10>
        UnknownContentError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.UnknownContentError: 299>
        UnknownNetworkError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.UnknownNetworkError: 99>
        UnknownProxyError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.UnknownProxyError: 199>
        UnknownServerError: typing.ClassVar[QNetworkReply.NetworkError]  # value = <NetworkError.UnknownServerError: 499>
    @staticmethod
    def abort(*args, **kwargs):
        ...
    @staticmethod
    def attribute(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def downloadProgress(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def encrypted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorOccurred(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
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
    def hasRawHeader(*args, **kwargs):
        ...
    @staticmethod
    def header(*args, **kwargs):
        ...
    @staticmethod
    def ignoreSslErrors(*args, **kwargs):
        ...
    @staticmethod
    def ignoreSslErrorsImplementation(*args, **kwargs):
        ...
    @staticmethod
    def isFinished(*args, **kwargs):
        ...
    @staticmethod
    def isRunning(*args, **kwargs):
        ...
    @staticmethod
    def isSequential(*args, **kwargs):
        ...
    @staticmethod
    def manager(*args, **kwargs):
        ...
    @staticmethod
    def metaDataChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def operation(*args, **kwargs):
        ...
    @staticmethod
    def preSharedKeyAuthenticationRequired(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rawHeader(*args, **kwargs):
        ...
    @staticmethod
    def rawHeaderList(*args, **kwargs):
        ...
    @staticmethod
    def rawHeaderPairs(*args, **kwargs):
        ...
    @staticmethod
    def readBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def redirectAllowed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def redirected(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def request(*args, **kwargs):
        ...
    @staticmethod
    def requestSent(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setAttribute(*args, **kwargs):
        ...
    @staticmethod
    def setError(*args, **kwargs):
        ...
    @staticmethod
    def setFinished(*args, **kwargs):
        ...
    @staticmethod
    def setHeader(*args, **kwargs):
        ...
    @staticmethod
    def setOperation(*args, **kwargs):
        ...
    @staticmethod
    def setRawHeader(*args, **kwargs):
        ...
    @staticmethod
    def setReadBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setRequest(*args, **kwargs):
        ...
    @staticmethod
    def setSslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def setSslConfigurationImplementation(*args, **kwargs):
        ...
    @staticmethod
    def setUrl(*args, **kwargs):
        ...
    @staticmethod
    def socketStartedConnecting(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def sslConfigurationImplementation(*args, **kwargs):
        ...
    @staticmethod
    def sslErrors(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def uploadProgress(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QNetworkRequest(PyQt6.sip.simplewrapper):
    class Attribute(enum.Enum):
        AuthenticationReuseAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.AuthenticationReuseAttribute: 12>
        AutoDeleteReplyOnFinishAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.AutoDeleteReplyOnFinishAttribute: 25>
        BackgroundRequestAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.BackgroundRequestAttribute: 17>
        CacheLoadControlAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.CacheLoadControlAttribute: 4>
        CacheSaveControlAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.CacheSaveControlAttribute: 5>
        ConnectionCacheExpiryTimeoutSecondsAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.ConnectionCacheExpiryTimeoutSecondsAttribute: 26>
        ConnectionEncryptedAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.ConnectionEncryptedAttribute: 3>
        CookieLoadControlAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.CookieLoadControlAttribute: 11>
        CookieSaveControlAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.CookieSaveControlAttribute: 13>
        CustomVerbAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.CustomVerbAttribute: 10>
        DoNotBufferUploadDataAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.DoNotBufferUploadDataAttribute: 7>
        EmitAllUploadProgressSignalsAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.EmitAllUploadProgressSignalsAttribute: 18>
        Http2AllowedAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.Http2AllowedAttribute: 19>
        Http2CleartextAllowedAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.Http2CleartextAllowedAttribute: 27>
        Http2DirectAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.Http2DirectAttribute: 23>
        Http2WasUsedAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.Http2WasUsedAttribute: 20>
        HttpPipeliningAllowedAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.HttpPipeliningAllowedAttribute: 8>
        HttpPipeliningWasUsedAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.HttpPipeliningWasUsedAttribute: 9>
        HttpReasonPhraseAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.HttpReasonPhraseAttribute: 1>
        HttpStatusCodeAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.HttpStatusCodeAttribute: 0>
        OriginalContentLengthAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.OriginalContentLengthAttribute: 21>
        RedirectPolicyAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.RedirectPolicyAttribute: 22>
        RedirectionTargetAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.RedirectionTargetAttribute: 2>
        SourceIsFromCacheAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.SourceIsFromCacheAttribute: 6>
        UseCredentialsAttribute: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.UseCredentialsAttribute: 28>
        User: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.User: 1000>
        UserMax: typing.ClassVar[QNetworkRequest.Attribute]  # value = <Attribute.UserMax: 32767>
    class CacheLoadControl(enum.Enum):
        AlwaysCache: typing.ClassVar[QNetworkRequest.CacheLoadControl]  # value = <CacheLoadControl.AlwaysCache: 3>
        AlwaysNetwork: typing.ClassVar[QNetworkRequest.CacheLoadControl]  # value = <CacheLoadControl.AlwaysNetwork: 0>
        PreferCache: typing.ClassVar[QNetworkRequest.CacheLoadControl]  # value = <CacheLoadControl.PreferCache: 2>
        PreferNetwork: typing.ClassVar[QNetworkRequest.CacheLoadControl]  # value = <CacheLoadControl.PreferNetwork: 1>
    class KnownHeaders(enum.Enum):
        ContentDispositionHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.ContentDispositionHeader: 6>
        ContentLengthHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.ContentLengthHeader: 1>
        ContentTypeHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.ContentTypeHeader: 0>
        CookieHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.CookieHeader: 4>
        ETagHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.ETagHeader: 10>
        IfMatchHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.IfMatchHeader: 11>
        IfModifiedSinceHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.IfModifiedSinceHeader: 9>
        IfNoneMatchHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.IfNoneMatchHeader: 12>
        LastModifiedHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.LastModifiedHeader: 3>
        LocationHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.LocationHeader: 2>
        ServerHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.ServerHeader: 8>
        SetCookieHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.SetCookieHeader: 5>
        UserAgentHeader: typing.ClassVar[QNetworkRequest.KnownHeaders]  # value = <KnownHeaders.UserAgentHeader: 7>
    class LoadControl(enum.Enum):
        Automatic: typing.ClassVar[QNetworkRequest.LoadControl]  # value = <LoadControl.Automatic: 0>
        Manual: typing.ClassVar[QNetworkRequest.LoadControl]  # value = <LoadControl.Manual: 1>
    class Priority(enum.Enum):
        HighPriority: typing.ClassVar[QNetworkRequest.Priority]  # value = <Priority.HighPriority: 1>
        LowPriority: typing.ClassVar[QNetworkRequest.Priority]  # value = <Priority.LowPriority: 5>
        NormalPriority: typing.ClassVar[QNetworkRequest.Priority]  # value = <Priority.NormalPriority: 3>
    class RedirectPolicy(enum.Enum):
        ManualRedirectPolicy: typing.ClassVar[QNetworkRequest.RedirectPolicy]  # value = <RedirectPolicy.ManualRedirectPolicy: 0>
        NoLessSafeRedirectPolicy: typing.ClassVar[QNetworkRequest.RedirectPolicy]  # value = <RedirectPolicy.NoLessSafeRedirectPolicy: 1>
        SameOriginRedirectPolicy: typing.ClassVar[QNetworkRequest.RedirectPolicy]  # value = <RedirectPolicy.SameOriginRedirectPolicy: 2>
        UserVerifiedRedirectPolicy: typing.ClassVar[QNetworkRequest.RedirectPolicy]  # value = <RedirectPolicy.UserVerifiedRedirectPolicy: 3>
    class TransferTimeoutConstant(enum.Enum):
        DefaultTransferTimeoutConstant: typing.ClassVar[QNetworkRequest.TransferTimeoutConstant]  # value = <TransferTimeoutConstant.DefaultTransferTimeoutConstant: 30000>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def attribute(*args, **kwargs):
        ...
    @staticmethod
    def decompressedSafetyCheckThreshold(*args, **kwargs):
        ...
    @staticmethod
    def hasRawHeader(*args, **kwargs):
        ...
    @staticmethod
    def header(*args, **kwargs):
        ...
    @staticmethod
    def http1Configuration(*args, **kwargs):
        ...
    @staticmethod
    def http2Configuration(*args, **kwargs):
        ...
    @staticmethod
    def maximumRedirectsAllowed(*args, **kwargs):
        ...
    @staticmethod
    def originatingObject(*args, **kwargs):
        ...
    @staticmethod
    def peerVerifyName(*args, **kwargs):
        ...
    @staticmethod
    def priority(*args, **kwargs):
        ...
    @staticmethod
    def rawHeader(*args, **kwargs):
        ...
    @staticmethod
    def rawHeaderList(*args, **kwargs):
        ...
    @staticmethod
    def setAttribute(*args, **kwargs):
        ...
    @staticmethod
    def setDecompressedSafetyCheckThreshold(*args, **kwargs):
        ...
    @staticmethod
    def setHeader(*args, **kwargs):
        ...
    @staticmethod
    def setHttp1Configuration(*args, **kwargs):
        ...
    @staticmethod
    def setHttp2Configuration(*args, **kwargs):
        ...
    @staticmethod
    def setMaximumRedirectsAllowed(*args, **kwargs):
        ...
    @staticmethod
    def setOriginatingObject(*args, **kwargs):
        ...
    @staticmethod
    def setPeerVerifyName(*args, **kwargs):
        ...
    @staticmethod
    def setPriority(*args, **kwargs):
        ...
    @staticmethod
    def setRawHeader(*args, **kwargs):
        ...
    @staticmethod
    def setSslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def setTransferTimeout(*args, **kwargs):
        ...
    @staticmethod
    def setUrl(*args, **kwargs):
        ...
    @staticmethod
    def sslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def transferTimeout(*args, **kwargs):
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
class QOcspCertificateStatus(enum.Enum):
    Good: typing.ClassVar[QOcspCertificateStatus]  # value = <QOcspCertificateStatus.Good: 0>
    Revoked: typing.ClassVar[QOcspCertificateStatus]  # value = <QOcspCertificateStatus.Revoked: 1>
    Unknown: typing.ClassVar[QOcspCertificateStatus]  # value = <QOcspCertificateStatus.Unknown: 2>
class QOcspResponse(PyQt6.sip.simplewrapper):
    @staticmethod
    def certificateStatus(*args, **kwargs):
        ...
    @staticmethod
    def responder(*args, **kwargs):
        ...
    @staticmethod
    def revocationReason(*args, **kwargs):
        ...
    @staticmethod
    def subject(*args, **kwargs):
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
class QOcspRevocationReason(enum.Enum):
    AffiliationChanged: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.AffiliationChanged: 3>
    CACompromise: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.CACompromise: 2>
    CertificateHold: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.CertificateHold: 6>
    CessationOfOperation: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.CessationOfOperation: 5>
    KeyCompromise: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.KeyCompromise: 1>
    None_: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.None_: -1>
    RemoveFromCRL: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.RemoveFromCRL: 7>
    Superseded: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.Superseded: 4>
    Unspecified: typing.ClassVar[QOcspRevocationReason]  # value = <QOcspRevocationReason.Unspecified: 0>
class QPasswordDigestor(PyQt6.sip.simplewrapper):
    @staticmethod
    def deriveKeyPbkdf1(*args, **kwargs):
        ...
    @staticmethod
    def deriveKeyPbkdf2(*args, **kwargs):
        ...
class QSsl(PyQt6.sip.simplewrapper):
    class AlertLevel(enum.Enum):
        Fatal: typing.ClassVar[QSsl.AlertLevel]  # value = <AlertLevel.Fatal: 1>
        Unknown: typing.ClassVar[QSsl.AlertLevel]  # value = <AlertLevel.Unknown: 2>
        Warning: typing.ClassVar[QSsl.AlertLevel]  # value = <AlertLevel.Warning: 0>
    class AlertType(enum.Enum):
        AccessDenied: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.AccessDenied: 49>
        BadCertificate: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.BadCertificate: 42>
        BadCertificateHashValue: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.BadCertificateHashValue: 114>
        BadCertificateStatusResponse: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.BadCertificateStatusResponse: 113>
        BadRecordMac: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.BadRecordMac: 20>
        CertificateExpired: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.CertificateExpired: 45>
        CertificateRequired: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.CertificateRequired: 116>
        CertificateRevoked: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.CertificateRevoked: 44>
        CertificateUnknown: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.CertificateUnknown: 46>
        CertificateUnobtainable: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.CertificateUnobtainable: 111>
        CloseNotify: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.CloseNotify: 0>
        DecodeError: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.DecodeError: 50>
        DecompressionFailure: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.DecompressionFailure: 30>
        DecryptError: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.DecryptError: 51>
        ExportRestriction: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.ExportRestriction: 60>
        HandshakeFailure: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.HandshakeFailure: 40>
        IllegalParameter: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.IllegalParameter: 47>
        InappropriateFallback: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.InappropriateFallback: 86>
        InsufficientSecurity: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.InsufficientSecurity: 71>
        InternalError: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.InternalError: 80>
        MissingExtension: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.MissingExtension: 109>
        NoApplicationProtocol: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.NoApplicationProtocol: 120>
        NoCertificate: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.NoCertificate: 41>
        NoRenegotiation: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.NoRenegotiation: 100>
        ProtocolVersion: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.ProtocolVersion: 70>
        RecordOverflow: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.RecordOverflow: 22>
        UnexpectedMessage: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UnexpectedMessage: 10>
        UnknownAlertMessage: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UnknownAlertMessage: 255>
        UnknownCa: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UnknownCa: 48>
        UnknownPskIdentity: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UnknownPskIdentity: 115>
        UnrecognizedName: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UnrecognizedName: 112>
        UnsupportedCertificate: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UnsupportedCertificate: 43>
        UnsupportedExtension: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UnsupportedExtension: 110>
        UserCancelled: typing.ClassVar[QSsl.AlertType]  # value = <AlertType.UserCancelled: 90>
    class AlternativeNameEntryType(enum.Enum):
        DnsEntry: typing.ClassVar[QSsl.AlternativeNameEntryType]  # value = <AlternativeNameEntryType.DnsEntry: 1>
        EmailEntry: typing.ClassVar[QSsl.AlternativeNameEntryType]  # value = <AlternativeNameEntryType.EmailEntry: 0>
        IpAddressEntry: typing.ClassVar[QSsl.AlternativeNameEntryType]  # value = <AlternativeNameEntryType.IpAddressEntry: 2>
    class EncodingFormat(enum.Enum):
        Der: typing.ClassVar[QSsl.EncodingFormat]  # value = <EncodingFormat.Der: 1>
        Pem: typing.ClassVar[QSsl.EncodingFormat]  # value = <EncodingFormat.Pem: 0>
    class ImplementedClass(enum.Enum):
        Certificate: typing.ClassVar[QSsl.ImplementedClass]  # value = <ImplementedClass.Certificate: 1>
        DiffieHellman: typing.ClassVar[QSsl.ImplementedClass]  # value = <ImplementedClass.DiffieHellman: 3>
        Dtls: typing.ClassVar[QSsl.ImplementedClass]  # value = <ImplementedClass.Dtls: 5>
        DtlsCookie: typing.ClassVar[QSsl.ImplementedClass]  # value = <ImplementedClass.DtlsCookie: 6>
        EllipticCurve: typing.ClassVar[QSsl.ImplementedClass]  # value = <ImplementedClass.EllipticCurve: 4>
        Key: typing.ClassVar[QSsl.ImplementedClass]  # value = <ImplementedClass.Key: 0>
        Socket: typing.ClassVar[QSsl.ImplementedClass]  # value = <ImplementedClass.Socket: 2>
    class KeyAlgorithm(enum.Enum):
        Dh: typing.ClassVar[QSsl.KeyAlgorithm]  # value = <KeyAlgorithm.Dh: 4>
        Dsa: typing.ClassVar[QSsl.KeyAlgorithm]  # value = <KeyAlgorithm.Dsa: 2>
        Ec: typing.ClassVar[QSsl.KeyAlgorithm]  # value = <KeyAlgorithm.Ec: 3>
        Opaque: typing.ClassVar[QSsl.KeyAlgorithm]  # value = <KeyAlgorithm.Opaque: 0>
        Rsa: typing.ClassVar[QSsl.KeyAlgorithm]  # value = <KeyAlgorithm.Rsa: 1>
    class KeyType(enum.Enum):
        PrivateKey: typing.ClassVar[QSsl.KeyType]  # value = <KeyType.PrivateKey: 0>
        PublicKey: typing.ClassVar[QSsl.KeyType]  # value = <KeyType.PublicKey: 1>
    class SslOption(enum.Flag):
        SslOptionDisableCompression: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableCompression: 4>
        SslOptionDisableEmptyFragments: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableEmptyFragments: 1>
        SslOptionDisableLegacyRenegotiation: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableLegacyRenegotiation: 16>
        SslOptionDisableServerCipherPreference: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableServerCipherPreference: 128>
        SslOptionDisableServerNameIndication: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableServerNameIndication: 8>
        SslOptionDisableSessionPersistence: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableSessionPersistence: 64>
        SslOptionDisableSessionSharing: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableSessionSharing: 32>
        SslOptionDisableSessionTickets: typing.ClassVar[QSsl.SslOption]  # value = <SslOption.SslOptionDisableSessionTickets: 2>
    class SslProtocol(enum.Enum):
        AnyProtocol: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.AnyProtocol: 3>
        DtlsV1_0: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.DtlsV1_0: 8>
        DtlsV1_0OrLater: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.DtlsV1_0OrLater: 9>
        DtlsV1_2: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.DtlsV1_2: 10>
        DtlsV1_2OrLater: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.DtlsV1_2OrLater: 11>
        SecureProtocols: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.SecureProtocols: 4>
        TlsV1_0: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_0: 0>
        TlsV1_0OrLater: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_0OrLater: 5>
        TlsV1_1: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_1: 1>
        TlsV1_1OrLater: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_1OrLater: 6>
        TlsV1_2: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_2: 2>
        TlsV1_2OrLater: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_2OrLater: 7>
        TlsV1_3: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_3: 12>
        TlsV1_3OrLater: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.TlsV1_3OrLater: 13>
        UnknownProtocol: typing.ClassVar[QSsl.SslProtocol]  # value = <SslProtocol.UnknownProtocol: -1>
    class SupportedFeature(enum.Enum):
        Alerts: typing.ClassVar[QSsl.SupportedFeature]  # value = <SupportedFeature.Alerts: 6>
        CertificateVerification: typing.ClassVar[QSsl.SupportedFeature]  # value = <SupportedFeature.CertificateVerification: 0>
        ClientSideAlpn: typing.ClassVar[QSsl.SupportedFeature]  # value = <SupportedFeature.ClientSideAlpn: 1>
        Ocsp: typing.ClassVar[QSsl.SupportedFeature]  # value = <SupportedFeature.Ocsp: 3>
        Psk: typing.ClassVar[QSsl.SupportedFeature]  # value = <SupportedFeature.Psk: 4>
        ServerSideAlpn: typing.ClassVar[QSsl.SupportedFeature]  # value = <SupportedFeature.ServerSideAlpn: 2>
        SessionTicket: typing.ClassVar[QSsl.SupportedFeature]  # value = <SupportedFeature.SessionTicket: 5>
class QSslCertificate(PyQt6.sip.simplewrapper):
    class PatternSyntax(enum.Enum):
        FixedString: typing.ClassVar[QSslCertificate.PatternSyntax]  # value = <PatternSyntax.FixedString: 2>
        RegularExpression: typing.ClassVar[QSslCertificate.PatternSyntax]  # value = <PatternSyntax.RegularExpression: 0>
        Wildcard: typing.ClassVar[QSslCertificate.PatternSyntax]  # value = <PatternSyntax.Wildcard: 1>
    class SubjectInfo(enum.Enum):
        CommonName: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.CommonName: 1>
        CountryName: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.CountryName: 4>
        DistinguishedNameQualifier: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.DistinguishedNameQualifier: 6>
        EmailAddress: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.EmailAddress: 8>
        LocalityName: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.LocalityName: 2>
        Organization: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.Organization: 0>
        OrganizationalUnitName: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.OrganizationalUnitName: 3>
        SerialNumber: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.SerialNumber: 7>
        StateOrProvinceName: typing.ClassVar[QSslCertificate.SubjectInfo]  # value = <SubjectInfo.StateOrProvinceName: 5>
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def digest(*args, **kwargs):
        ...
    @staticmethod
    def effectiveDate(*args, **kwargs):
        ...
    @staticmethod
    def expiryDate(*args, **kwargs):
        ...
    @staticmethod
    def extensions(*args, **kwargs):
        ...
    @staticmethod
    def fromData(*args, **kwargs):
        ...
    @staticmethod
    def fromDevice(*args, **kwargs):
        ...
    @staticmethod
    def fromPath(*args, **kwargs):
        ...
    @staticmethod
    def handle(*args, **kwargs):
        ...
    @staticmethod
    def importPkcs12(*args, **kwargs):
        ...
    @staticmethod
    def isBlacklisted(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isSelfSigned(*args, **kwargs):
        ...
    @staticmethod
    def issuerDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def issuerInfo(*args, **kwargs):
        ...
    @staticmethod
    def issuerInfoAttributes(*args, **kwargs):
        ...
    @staticmethod
    def publicKey(*args, **kwargs):
        ...
    @staticmethod
    def serialNumber(*args, **kwargs):
        ...
    @staticmethod
    def subjectAlternativeNames(*args, **kwargs):
        ...
    @staticmethod
    def subjectDisplayName(*args, **kwargs):
        ...
    @staticmethod
    def subjectInfo(*args, **kwargs):
        ...
    @staticmethod
    def subjectInfoAttributes(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toDer(*args, **kwargs):
        ...
    @staticmethod
    def toPem(*args, **kwargs):
        ...
    @staticmethod
    def toText(*args, **kwargs):
        ...
    @staticmethod
    def verify(*args, **kwargs):
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
class QSslCertificateExtension(PyQt6.sip.simplewrapper):
    @staticmethod
    def isCritical(*args, **kwargs):
        ...
    @staticmethod
    def isSupported(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def oid(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QSslCipher(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def authenticationMethod(*args, **kwargs):
        ...
    @staticmethod
    def encryptionMethod(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def keyExchangeMethod(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def protocol(*args, **kwargs):
        ...
    @staticmethod
    def protocolString(*args, **kwargs):
        ...
    @staticmethod
    def supportedBits(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def usedBits(*args, **kwargs):
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
class QSslConfiguration(PyQt6.sip.simplewrapper):
    class NextProtocolNegotiationStatus(enum.Enum):
        NextProtocolNegotiationNegotiated: typing.ClassVar[QSslConfiguration.NextProtocolNegotiationStatus]  # value = <NextProtocolNegotiationStatus.NextProtocolNegotiationNegotiated: 1>
        NextProtocolNegotiationNone: typing.ClassVar[QSslConfiguration.NextProtocolNegotiationStatus]  # value = <NextProtocolNegotiationStatus.NextProtocolNegotiationNone: 0>
        NextProtocolNegotiationUnsupported: typing.ClassVar[QSslConfiguration.NextProtocolNegotiationStatus]  # value = <NextProtocolNegotiationStatus.NextProtocolNegotiationUnsupported: 2>
    NextProtocolHttp1_1: typing.ClassVar[bytes]  # value = b'http/1.1'
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def addCaCertificate(*args, **kwargs):
        ...
    @staticmethod
    def addCaCertificates(*args, **kwargs):
        ...
    @staticmethod
    def allowedNextProtocols(*args, **kwargs):
        ...
    @staticmethod
    def backendConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def caCertificates(*args, **kwargs):
        ...
    @staticmethod
    def ciphers(*args, **kwargs):
        ...
    @staticmethod
    def defaultConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def defaultDtlsConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def diffieHellmanParameters(*args, **kwargs):
        ...
    @staticmethod
    def dtlsCookieVerificationEnabled(*args, **kwargs):
        ...
    @staticmethod
    def ellipticCurves(*args, **kwargs):
        ...
    @staticmethod
    def ephemeralServerKey(*args, **kwargs):
        ...
    @staticmethod
    def handshakeMustInterruptOnError(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def localCertificate(*args, **kwargs):
        ...
    @staticmethod
    def localCertificateChain(*args, **kwargs):
        ...
    @staticmethod
    def missingCertificateIsFatal(*args, **kwargs):
        ...
    @staticmethod
    def nextNegotiatedProtocol(*args, **kwargs):
        ...
    @staticmethod
    def nextProtocolNegotiationStatus(*args, **kwargs):
        ...
    @staticmethod
    def ocspStaplingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def peerCertificate(*args, **kwargs):
        ...
    @staticmethod
    def peerCertificateChain(*args, **kwargs):
        ...
    @staticmethod
    def peerVerifyDepth(*args, **kwargs):
        ...
    @staticmethod
    def peerVerifyMode(*args, **kwargs):
        ...
    @staticmethod
    def preSharedKeyIdentityHint(*args, **kwargs):
        ...
    @staticmethod
    def privateKey(*args, **kwargs):
        ...
    @staticmethod
    def protocol(*args, **kwargs):
        ...
    @staticmethod
    def sessionCipher(*args, **kwargs):
        ...
    @staticmethod
    def sessionProtocol(*args, **kwargs):
        ...
    @staticmethod
    def sessionTicket(*args, **kwargs):
        ...
    @staticmethod
    def sessionTicketLifeTimeHint(*args, **kwargs):
        ...
    @staticmethod
    def setAllowedNextProtocols(*args, **kwargs):
        ...
    @staticmethod
    def setBackendConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def setBackendConfigurationOption(*args, **kwargs):
        ...
    @staticmethod
    def setCaCertificates(*args, **kwargs):
        ...
    @staticmethod
    def setCiphers(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultDtlsConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def setDiffieHellmanParameters(*args, **kwargs):
        ...
    @staticmethod
    def setDtlsCookieVerificationEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setEllipticCurves(*args, **kwargs):
        ...
    @staticmethod
    def setHandshakeMustInterruptOnError(*args, **kwargs):
        ...
    @staticmethod
    def setLocalCertificate(*args, **kwargs):
        ...
    @staticmethod
    def setLocalCertificateChain(*args, **kwargs):
        ...
    @staticmethod
    def setMissingCertificateIsFatal(*args, **kwargs):
        ...
    @staticmethod
    def setOcspStaplingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setPeerVerifyDepth(*args, **kwargs):
        ...
    @staticmethod
    def setPeerVerifyMode(*args, **kwargs):
        ...
    @staticmethod
    def setPreSharedKeyIdentityHint(*args, **kwargs):
        ...
    @staticmethod
    def setPrivateKey(*args, **kwargs):
        ...
    @staticmethod
    def setProtocol(*args, **kwargs):
        ...
    @staticmethod
    def setSessionTicket(*args, **kwargs):
        ...
    @staticmethod
    def setSslOption(*args, **kwargs):
        ...
    @staticmethod
    def supportedCiphers(*args, **kwargs):
        ...
    @staticmethod
    def supportedEllipticCurves(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def systemCaCertificates(*args, **kwargs):
        ...
    @staticmethod
    def testSslOption(*args, **kwargs):
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
class QSslDiffieHellmanParameters(PyQt6.sip.simplewrapper):
    class Error(enum.Enum):
        InvalidInputDataError: typing.ClassVar[QSslDiffieHellmanParameters.Error]  # value = <Error.InvalidInputDataError: 1>
        NoError: typing.ClassVar[QSslDiffieHellmanParameters.Error]  # value = <Error.NoError: 0>
        UnsafeParametersError: typing.ClassVar[QSslDiffieHellmanParameters.Error]  # value = <Error.UnsafeParametersError: 2>
    @staticmethod
    def defaultParameters(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fromEncoded(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
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
class QSslEllipticCurve(PyQt6.sip.simplewrapper):
    @staticmethod
    def fromLongName(*args, **kwargs):
        ...
    @staticmethod
    def fromShortName(*args, **kwargs):
        ...
    @staticmethod
    def isTlsNamedCurve(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def longName(*args, **kwargs):
        ...
    @staticmethod
    def shortName(*args, **kwargs):
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
class QSslError(PyQt6.sip.simplewrapper):
    class SslError(enum.Enum):
        AuthorityIssuerSerialNumberMismatch: typing.ClassVar[QSslError.SslError]  # value = <SslError.AuthorityIssuerSerialNumberMismatch: 20>
        CertificateBlacklisted: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateBlacklisted: 24>
        CertificateExpired: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateExpired: 6>
        CertificateNotYetValid: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateNotYetValid: 5>
        CertificateRejected: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateRejected: 18>
        CertificateRevoked: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateRevoked: 13>
        CertificateSignatureFailed: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateSignatureFailed: 4>
        CertificateStatusUnknown: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateStatusUnknown: 25>
        CertificateUntrusted: typing.ClassVar[QSslError.SslError]  # value = <SslError.CertificateUntrusted: 17>
        HostNameMismatch: typing.ClassVar[QSslError.SslError]  # value = <SslError.HostNameMismatch: 22>
        InvalidCaCertificate: typing.ClassVar[QSslError.SslError]  # value = <SslError.InvalidCaCertificate: 14>
        InvalidNotAfterField: typing.ClassVar[QSslError.SslError]  # value = <SslError.InvalidNotAfterField: 8>
        InvalidNotBeforeField: typing.ClassVar[QSslError.SslError]  # value = <SslError.InvalidNotBeforeField: 7>
        InvalidPurpose: typing.ClassVar[QSslError.SslError]  # value = <SslError.InvalidPurpose: 16>
        NoError: typing.ClassVar[QSslError.SslError]  # value = <SslError.NoError: 0>
        NoPeerCertificate: typing.ClassVar[QSslError.SslError]  # value = <SslError.NoPeerCertificate: 21>
        NoSslSupport: typing.ClassVar[QSslError.SslError]  # value = <SslError.NoSslSupport: 23>
        OcspInternalError: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspInternalError: 29>
        OcspMalformedRequest: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspMalformedRequest: 27>
        OcspMalformedResponse: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspMalformedResponse: 28>
        OcspNoResponseFound: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspNoResponseFound: 26>
        OcspResponseCannotBeTrusted: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspResponseCannotBeTrusted: 33>
        OcspResponseCertIdUnknown: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspResponseCertIdUnknown: 34>
        OcspResponseExpired: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspResponseExpired: 35>
        OcspSigRequred: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspSigRequred: 31>
        OcspStatusUnknown: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspStatusUnknown: 36>
        OcspTryLater: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspTryLater: 30>
        OcspUnauthorized: typing.ClassVar[QSslError.SslError]  # value = <SslError.OcspUnauthorized: 32>
        PathLengthExceeded: typing.ClassVar[QSslError.SslError]  # value = <SslError.PathLengthExceeded: 15>
        SelfSignedCertificate: typing.ClassVar[QSslError.SslError]  # value = <SslError.SelfSignedCertificate: 9>
        SelfSignedCertificateInChain: typing.ClassVar[QSslError.SslError]  # value = <SslError.SelfSignedCertificateInChain: 10>
        SubjectIssuerMismatch: typing.ClassVar[QSslError.SslError]  # value = <SslError.SubjectIssuerMismatch: 19>
        UnableToDecodeIssuerPublicKey: typing.ClassVar[QSslError.SslError]  # value = <SslError.UnableToDecodeIssuerPublicKey: 3>
        UnableToDecryptCertificateSignature: typing.ClassVar[QSslError.SslError]  # value = <SslError.UnableToDecryptCertificateSignature: 2>
        UnableToGetIssuerCertificate: typing.ClassVar[QSslError.SslError]  # value = <SslError.UnableToGetIssuerCertificate: 1>
        UnableToGetLocalIssuerCertificate: typing.ClassVar[QSslError.SslError]  # value = <SslError.UnableToGetLocalIssuerCertificate: 11>
        UnableToVerifyFirstCertificate: typing.ClassVar[QSslError.SslError]  # value = <SslError.UnableToVerifyFirstCertificate: 12>
        UnspecifiedError: typing.ClassVar[QSslError.SslError]  # value = <SslError.UnspecifiedError: -1>
    @staticmethod
    def certificate(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
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
class QSslKey(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def algorithm(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def handle(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toDer(*args, **kwargs):
        ...
    @staticmethod
    def toPem(*args, **kwargs):
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
class QSslPreSharedKeyAuthenticator(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def identity(*args, **kwargs):
        ...
    @staticmethod
    def identityHint(*args, **kwargs):
        ...
    @staticmethod
    def maximumIdentityLength(*args, **kwargs):
        ...
    @staticmethod
    def maximumPreSharedKeyLength(*args, **kwargs):
        ...
    @staticmethod
    def preSharedKey(*args, **kwargs):
        ...
    @staticmethod
    def setIdentity(*args, **kwargs):
        ...
    @staticmethod
    def setPreSharedKey(*args, **kwargs):
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
class QSslServer(QTcpServer):
    @staticmethod
    def alertReceived(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def alertSent(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def errorOccurred(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def handshakeInterruptedOnError(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def handshakeTimeout(*args, **kwargs):
        ...
    @staticmethod
    def incomingConnection(*args, **kwargs):
        ...
    @staticmethod
    def peerVerifyError(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def preSharedKeyAuthenticationRequired(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setHandshakeTimeout(*args, **kwargs):
        ...
    @staticmethod
    def setSslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def sslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def sslErrors(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def startedEncryptionHandshake(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
class QSslSocket(QTcpSocket):
    class PeerVerifyMode(enum.Enum):
        AutoVerifyPeer: typing.ClassVar[QSslSocket.PeerVerifyMode]  # value = <PeerVerifyMode.AutoVerifyPeer: 3>
        QueryPeer: typing.ClassVar[QSslSocket.PeerVerifyMode]  # value = <PeerVerifyMode.QueryPeer: 1>
        VerifyNone: typing.ClassVar[QSslSocket.PeerVerifyMode]  # value = <PeerVerifyMode.VerifyNone: 0>
        VerifyPeer: typing.ClassVar[QSslSocket.PeerVerifyMode]  # value = <PeerVerifyMode.VerifyPeer: 2>
    class SslMode(enum.Enum):
        SslClientMode: typing.ClassVar[QSslSocket.SslMode]  # value = <SslMode.SslClientMode: 1>
        SslServerMode: typing.ClassVar[QSslSocket.SslMode]  # value = <SslMode.SslServerMode: 2>
        UnencryptedMode: typing.ClassVar[QSslSocket.SslMode]  # value = <SslMode.UnencryptedMode: 0>
    @staticmethod
    def activeBackend(*args, **kwargs):
        ...
    @staticmethod
    def alertReceived(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def alertSent(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def atEnd(*args, **kwargs):
        ...
    @staticmethod
    def availableBackends(*args, **kwargs):
        ...
    @staticmethod
    def bytesAvailable(*args, **kwargs):
        ...
    @staticmethod
    def bytesToWrite(*args, **kwargs):
        ...
    @staticmethod
    def canReadLine(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def connectToHost(*args, **kwargs):
        ...
    @staticmethod
    def connectToHostEncrypted(*args, **kwargs):
        ...
    @staticmethod
    def continueInterruptedHandshake(*args, **kwargs):
        ...
    @staticmethod
    def disconnectFromHost(*args, **kwargs):
        ...
    @staticmethod
    def encrypted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def encryptedBytesAvailable(*args, **kwargs):
        ...
    @staticmethod
    def encryptedBytesToWrite(*args, **kwargs):
        ...
    @staticmethod
    def encryptedBytesWritten(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def handshakeInterruptedOnError(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def ignoreSslErrors(*args, **kwargs):
        ...
    @staticmethod
    def implementedClasses(*args, **kwargs):
        ...
    @staticmethod
    def isClassImplemented(*args, **kwargs):
        ...
    @staticmethod
    def isEncrypted(*args, **kwargs):
        ...
    @staticmethod
    def isFeatureSupported(*args, **kwargs):
        ...
    @staticmethod
    def isProtocolSupported(*args, **kwargs):
        ...
    @staticmethod
    def localCertificate(*args, **kwargs):
        ...
    @staticmethod
    def localCertificateChain(*args, **kwargs):
        ...
    @staticmethod
    def mode(*args, **kwargs):
        ...
    @staticmethod
    def modeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def newSessionTicketReceived(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def ocspResponses(*args, **kwargs):
        ...
    @staticmethod
    def peerCertificate(*args, **kwargs):
        ...
    @staticmethod
    def peerCertificateChain(*args, **kwargs):
        ...
    @staticmethod
    def peerVerifyDepth(*args, **kwargs):
        ...
    @staticmethod
    def peerVerifyError(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def peerVerifyMode(*args, **kwargs):
        ...
    @staticmethod
    def peerVerifyName(*args, **kwargs):
        ...
    @staticmethod
    def preSharedKeyAuthenticationRequired(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def privateKey(*args, **kwargs):
        ...
    @staticmethod
    def protocol(*args, **kwargs):
        ...
    @staticmethod
    def readData(*args, **kwargs):
        ...
    @staticmethod
    def resume(*args, **kwargs):
        ...
    @staticmethod
    def sessionCipher(*args, **kwargs):
        ...
    @staticmethod
    def sessionProtocol(*args, **kwargs):
        ...
    @staticmethod
    def setActiveBackend(*args, **kwargs):
        ...
    @staticmethod
    def setLocalCertificate(*args, **kwargs):
        ...
    @staticmethod
    def setLocalCertificateChain(*args, **kwargs):
        ...
    @staticmethod
    def setPeerVerifyDepth(*args, **kwargs):
        ...
    @staticmethod
    def setPeerVerifyMode(*args, **kwargs):
        ...
    @staticmethod
    def setPeerVerifyName(*args, **kwargs):
        ...
    @staticmethod
    def setPrivateKey(*args, **kwargs):
        ...
    @staticmethod
    def setProtocol(*args, **kwargs):
        ...
    @staticmethod
    def setReadBufferSize(*args, **kwargs):
        ...
    @staticmethod
    def setSocketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def setSocketOption(*args, **kwargs):
        ...
    @staticmethod
    def setSslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def skipData(*args, **kwargs):
        ...
    @staticmethod
    def socketOption(*args, **kwargs):
        ...
    @staticmethod
    def sslConfiguration(*args, **kwargs):
        ...
    @staticmethod
    def sslErrors(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sslHandshakeErrors(*args, **kwargs):
        ...
    @staticmethod
    def sslLibraryBuildVersionNumber(*args, **kwargs):
        ...
    @staticmethod
    def sslLibraryBuildVersionString(*args, **kwargs):
        ...
    @staticmethod
    def sslLibraryVersionNumber(*args, **kwargs):
        ...
    @staticmethod
    def sslLibraryVersionString(*args, **kwargs):
        ...
    @staticmethod
    def startClientEncryption(*args, **kwargs):
        ...
    @staticmethod
    def startServerEncryption(*args, **kwargs):
        ...
    @staticmethod
    def supportedFeatures(*args, **kwargs):
        ...
    @staticmethod
    def supportedProtocols(*args, **kwargs):
        ...
    @staticmethod
    def supportsSsl(*args, **kwargs):
        ...
    @staticmethod
    def waitForBytesWritten(*args, **kwargs):
        ...
    @staticmethod
    def waitForConnected(*args, **kwargs):
        ...
    @staticmethod
    def waitForDisconnected(*args, **kwargs):
        ...
    @staticmethod
    def waitForEncrypted(*args, **kwargs):
        ...
    @staticmethod
    def waitForReadyRead(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QTcpServer(PyQt6.QtCore.QObject):
    @staticmethod
    def acceptError(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def addPendingConnection(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def hasPendingConnections(*args, **kwargs):
        ...
    @staticmethod
    def incomingConnection(*args, **kwargs):
        ...
    @staticmethod
    def isListening(*args, **kwargs):
        ...
    @staticmethod
    def listen(*args, **kwargs):
        ...
    @staticmethod
    def listenBacklogSize(*args, **kwargs):
        ...
    @staticmethod
    def maxPendingConnections(*args, **kwargs):
        ...
    @staticmethod
    def newConnection(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def nextPendingConnection(*args, **kwargs):
        ...
    @staticmethod
    def pauseAccepting(*args, **kwargs):
        ...
    @staticmethod
    def pendingConnectionAvailable(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def proxy(*args, **kwargs):
        ...
    @staticmethod
    def resumeAccepting(*args, **kwargs):
        ...
    @staticmethod
    def serverAddress(*args, **kwargs):
        ...
    @staticmethod
    def serverError(*args, **kwargs):
        ...
    @staticmethod
    def serverPort(*args, **kwargs):
        ...
    @staticmethod
    def setListenBacklogSize(*args, **kwargs):
        ...
    @staticmethod
    def setMaxPendingConnections(*args, **kwargs):
        ...
    @staticmethod
    def setProxy(*args, **kwargs):
        ...
    @staticmethod
    def setSocketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def socketDescriptor(*args, **kwargs):
        ...
    @staticmethod
    def waitForNewConnection(*args, **kwargs):
        ...
class QTcpSocket(QAbstractSocket):
    pass
class QUdpSocket(QAbstractSocket):
    @staticmethod
    def hasPendingDatagrams(*args, **kwargs):
        ...
    @staticmethod
    def joinMulticastGroup(*args, **kwargs):
        ...
    @staticmethod
    def leaveMulticastGroup(*args, **kwargs):
        ...
    @staticmethod
    def multicastInterface(*args, **kwargs):
        ...
    @staticmethod
    def pendingDatagramSize(*args, **kwargs):
        ...
    @staticmethod
    def readDatagram(*args, **kwargs):
        ...
    @staticmethod
    def receiveDatagram(*args, **kwargs):
        ...
    @staticmethod
    def setMulticastInterface(*args, **kwargs):
        ...
    @staticmethod
    def writeDatagram(*args, **kwargs):
        ...
