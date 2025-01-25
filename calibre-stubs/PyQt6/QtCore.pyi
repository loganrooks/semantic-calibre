import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['PYQT_VERSION', 'PYQT_VERSION_STR', 'QAbstractAnimation', 'QAbstractEventDispatcher', 'QAbstractItemModel', 'QAbstractListModel', 'QAbstractNativeEventFilter', 'QAbstractProxyModel', 'QAbstractTableModel', 'QAnimationGroup', 'QBasicTimer', 'QBitArray', 'QBluetoothPermission', 'QBuffer', 'QByteArray', 'QByteArrayMatcher', 'QCalendar', 'QCalendarPermission', 'QCameraPermission', 'QCborError', 'QCborKnownTags', 'QCborSimpleType', 'QCborStreamReader', 'QCborStreamWriter', 'QChildEvent', 'QCollator', 'QCollatorSortKey', 'QCommandLineOption', 'QCommandLineParser', 'QConcatenateTablesProxyModel', 'QContactsPermission', 'QCoreApplication', 'QCryptographicHash', 'QDataStream', 'QDate', 'QDateTime', 'QDeadlineTimer', 'QDir', 'QDirIterator', 'QDynamicPropertyChangeEvent', 'QEasingCurve', 'QElapsedTimer', 'QEvent', 'QEventLoop', 'QEventLoopLocker', 'QFile', 'QFileDevice', 'QFileInfo', 'QFileSelector', 'QFileSystemWatcher', 'QGenericArgument', 'QGenericReturnArgument', 'QIODevice', 'QIODeviceBase', 'QIdentityProxyModel', 'QItemSelection', 'QItemSelectionModel', 'QItemSelectionRange', 'QJsonDocument', 'QJsonParseError', 'QJsonValue', 'QKeyCombination', 'QLibrary', 'QLibraryInfo', 'QLine', 'QLineF', 'QLocale', 'QLocationPermission', 'QLockFile', 'QLoggingCategory', 'QMargins', 'QMarginsF', 'QMessageAuthenticationCode', 'QMessageLogContext', 'QMessageLogger', 'QMetaClassInfo', 'QMetaEnum', 'QMetaMethod', 'QMetaObject', 'QMetaProperty', 'QMetaType', 'QMicrophonePermission', 'QMimeData', 'QMimeDatabase', 'QMimeType', 'QModelIndex', 'QModelRoleData', 'QModelRoleDataSpan', 'QMutex', 'QMutexLocker', 'QNativeIpcKey', 'QObject', 'QObjectCleanupHandler', 'QOperatingSystemVersion', 'QOperatingSystemVersionBase', 'QParallelAnimationGroup', 'QPauseAnimation', 'QPermission', 'QPersistentModelIndex', 'QPluginLoader', 'QPoint', 'QPointF', 'QProcess', 'QProcessEnvironment', 'QPropertyAnimation', 'QRandomGenerator', 'QReadLocker', 'QReadWriteLock', 'QRect', 'QRectF', 'QRecursiveMutex', 'QRegularExpression', 'QRegularExpressionMatch', 'QRegularExpressionMatchIterator', 'QResource', 'QRunnable', 'QSaveFile', 'QSemaphore', 'QSemaphoreReleaser', 'QSequentialAnimationGroup', 'QSettings', 'QSharedMemory', 'QSignalBlocker', 'QSignalMapper', 'QSize', 'QSizeF', 'QSocketNotifier', 'QSortFilterProxyModel', 'QStandardPaths', 'QStorageInfo', 'QStringConverter', 'QStringConverterBase', 'QStringDecoder', 'QStringEncoder', 'QStringListModel', 'QSysInfo', 'QSystemSemaphore', 'QT_TRANSLATE_NOOP', 'QT_TR_NOOP', 'QT_VERSION', 'QT_VERSION_STR', 'QTemporaryDir', 'QTemporaryFile', 'QTextBoundaryFinder', 'QTextStream', 'QTextStreamManipulator', 'QThread', 'QThreadPool', 'QTime', 'QTimeLine', 'QTimeZone', 'QTimer', 'QTimerEvent', 'QTranslator', 'QTransposeProxyModel', 'QTypeRevision', 'QUrl', 'QUrlQuery', 'QUuid', 'QVariant', 'QVariantAnimation', 'QVersionNumber', 'QWaitCondition', 'QWriteLocker', 'QXmlStreamAttribute', 'QXmlStreamAttributes', 'QXmlStreamEntityDeclaration', 'QXmlStreamEntityResolver', 'QXmlStreamNamespaceDeclaration', 'QXmlStreamNotationDeclaration', 'QXmlStreamReader', 'QXmlStreamWriter', 'Q_ARG', 'Q_RETURN_ARG', 'Qt', 'QtMsgType', 'pyqtBoundSignal', 'pyqtClassInfo', 'pyqtEnum', 'pyqtPickleProtocol', 'pyqtProperty', 'pyqtRemoveInputHook', 'pyqtRestoreInputHook', 'pyqtSetPickleProtocol', 'pyqtSignal', 'pyqtSlot', 'qAbs', 'qAddPostRoutine', 'qAddPreRoutine', 'qChecksum', 'qCompress', 'qCritical', 'qDebug', 'qEnvironmentVariable', 'qEnvironmentVariableIntValue', 'qEnvironmentVariableIsEmpty', 'qEnvironmentVariableIsSet', 'qFatal', 'qFloatDistance', 'qFormatLogMessage', 'qFuzzyCompare', 'qFuzzyIsNull', 'qInf', 'qInfo', 'qInstallMessageHandler', 'qIsFinite', 'qIsInf', 'qIsNaN', 'qQNaN', 'qRegisterResourceData', 'qRemovePostRoutine', 'qRound', 'qRound64', 'qSNaN', 'qSetFieldWidth', 'qSetMessagePattern', 'qSetPadChar', 'qSetRealNumberPrecision', 'qUncompress', 'qUnregisterResourceData', 'qVersion', 'qWarning', 'qYieldCpu']
class QAbstractAnimation(QObject):
    class DeletionPolicy(enum.Enum):
        DeleteWhenStopped: typing.ClassVar[QAbstractAnimation.DeletionPolicy]  # value = <DeletionPolicy.DeleteWhenStopped: 1>
        KeepWhenStopped: typing.ClassVar[QAbstractAnimation.DeletionPolicy]  # value = <DeletionPolicy.KeepWhenStopped: 0>
    class Direction(enum.Enum):
        Backward: typing.ClassVar[QAbstractAnimation.Direction]  # value = <Direction.Backward: 1>
        Forward: typing.ClassVar[QAbstractAnimation.Direction]  # value = <Direction.Forward: 0>
    class State(enum.Enum):
        Paused: typing.ClassVar[QAbstractAnimation.State]  # value = <State.Paused: 1>
        Running: typing.ClassVar[QAbstractAnimation.State]  # value = <State.Running: 2>
        Stopped: typing.ClassVar[QAbstractAnimation.State]  # value = <State.Stopped: 0>
    @staticmethod
    def currentLoop(*args, **kwargs):
        ...
    @staticmethod
    def currentLoopChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def currentLoopTime(*args, **kwargs):
        ...
    @staticmethod
    def currentTime(*args, **kwargs):
        ...
    @staticmethod
    def direction(*args, **kwargs):
        ...
    @staticmethod
    def directionChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def duration(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
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
    def group(*args, **kwargs):
        ...
    @staticmethod
    def loopCount(*args, **kwargs):
        ...
    @staticmethod
    def pause(*args, **kwargs):
        ...
    @staticmethod
    def resume(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentTime(*args, **kwargs):
        ...
    @staticmethod
    def setDirection(*args, **kwargs):
        ...
    @staticmethod
    def setLoopCount(*args, **kwargs):
        ...
    @staticmethod
    def setPaused(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
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
    def totalDuration(*args, **kwargs):
        ...
    @staticmethod
    def updateCurrentTime(*args, **kwargs):
        ...
    @staticmethod
    def updateDirection(*args, **kwargs):
        ...
    @staticmethod
    def updateState(*args, **kwargs):
        ...
class QAbstractEventDispatcher(QObject):
    class TimerInfo(PyQt6.sip.simplewrapper):
        pass
    @staticmethod
    def aboutToBlock(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def awake(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def closingDown(*args, **kwargs):
        ...
    @staticmethod
    def filterNativeEvent(*args, **kwargs):
        ...
    @staticmethod
    def installNativeEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def instance(*args, **kwargs):
        ...
    @staticmethod
    def interrupt(*args, **kwargs):
        ...
    @staticmethod
    def processEvents(*args, **kwargs):
        ...
    @staticmethod
    def registerTimer(*args, **kwargs):
        ...
    @staticmethod
    def registeredTimers(*args, **kwargs):
        ...
    @staticmethod
    def remainingTime(*args, **kwargs):
        ...
    @staticmethod
    def removeNativeEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def startingUp(*args, **kwargs):
        ...
    @staticmethod
    def unregisterTimer(*args, **kwargs):
        ...
    @staticmethod
    def unregisterTimers(*args, **kwargs):
        ...
    @staticmethod
    def wakeUp(*args, **kwargs):
        ...
class QAbstractItemModel(QObject):
    class CheckIndexOption(enum.Flag):
        DoNotUseParent: typing.ClassVar[QAbstractItemModel.CheckIndexOption]  # value = <CheckIndexOption.DoNotUseParent: 2>
        IndexIsValid: typing.ClassVar[QAbstractItemModel.CheckIndexOption]  # value = <CheckIndexOption.IndexIsValid: 1>
        ParentIsInvalid: typing.ClassVar[QAbstractItemModel.CheckIndexOption]  # value = <CheckIndexOption.ParentIsInvalid: 4>
    class LayoutChangeHint(enum.Enum):
        HorizontalSortHint: typing.ClassVar[QAbstractItemModel.LayoutChangeHint]  # value = <LayoutChangeHint.HorizontalSortHint: 2>
        NoLayoutChangeHint: typing.ClassVar[QAbstractItemModel.LayoutChangeHint]  # value = <LayoutChangeHint.NoLayoutChangeHint: 0>
        VerticalSortHint: typing.ClassVar[QAbstractItemModel.LayoutChangeHint]  # value = <LayoutChangeHint.VerticalSortHint: 1>
    @staticmethod
    def beginInsertColumns(*args, **kwargs):
        ...
    @staticmethod
    def beginInsertRows(*args, **kwargs):
        ...
    @staticmethod
    def beginMoveColumns(*args, **kwargs):
        ...
    @staticmethod
    def beginMoveRows(*args, **kwargs):
        ...
    @staticmethod
    def beginRemoveColumns(*args, **kwargs):
        ...
    @staticmethod
    def beginRemoveRows(*args, **kwargs):
        ...
    @staticmethod
    def beginResetModel(*args, **kwargs):
        ...
    @staticmethod
    def buddy(*args, **kwargs):
        ...
    @staticmethod
    def canDropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def canFetchMore(*args, **kwargs):
        ...
    @staticmethod
    def changePersistentIndex(*args, **kwargs):
        ...
    @staticmethod
    def changePersistentIndexList(*args, **kwargs):
        ...
    @staticmethod
    def checkIndex(*args, **kwargs):
        ...
    @staticmethod
    def clearItemData(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def columnsAboutToBeInserted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def columnsAboutToBeMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def columnsAboutToBeRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def columnsInserted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def columnsMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def columnsRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def createIndex(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
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
    def decodeData(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def encodeData(*args, **kwargs):
        ...
    @staticmethod
    def endInsertColumns(*args, **kwargs):
        ...
    @staticmethod
    def endInsertRows(*args, **kwargs):
        ...
    @staticmethod
    def endMoveColumns(*args, **kwargs):
        ...
    @staticmethod
    def endMoveRows(*args, **kwargs):
        ...
    @staticmethod
    def endRemoveColumns(*args, **kwargs):
        ...
    @staticmethod
    def endRemoveRows(*args, **kwargs):
        ...
    @staticmethod
    def endResetModel(*args, **kwargs):
        ...
    @staticmethod
    def fetchMore(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def hasChildren(*args, **kwargs):
        ...
    @staticmethod
    def hasIndex(*args, **kwargs):
        ...
    @staticmethod
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def headerDataChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
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
    def itemData(*args, **kwargs):
        ...
    @staticmethod
    def layoutAboutToBeChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def layoutChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def match(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def modelAboutToBeReset(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def modelReset(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def moveColumn(*args, **kwargs):
        ...
    @staticmethod
    def moveColumns(*args, **kwargs):
        ...
    @staticmethod
    def moveRow(*args, **kwargs):
        ...
    @staticmethod
    def moveRows(*args, **kwargs):
        ...
    @staticmethod
    def multiData(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def persistentIndexList(*args, **kwargs):
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
    def resetInternalData(*args, **kwargs):
        ...
    @staticmethod
    def revert(*args, **kwargs):
        ...
    @staticmethod
    def roleNames(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def rowsAboutToBeInserted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rowsAboutToBeMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rowsAboutToBeRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rowsInserted(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rowsMoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def rowsRemoved(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderData(*args, **kwargs):
        ...
    @staticmethod
    def setItemData(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def span(*args, **kwargs):
        ...
    @staticmethod
    def submit(*args, **kwargs):
        ...
    @staticmethod
    def supportedDragActions(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
class QAbstractListModel(QAbstractItemModel):
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def hasChildren(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
class QAbstractNativeEventFilter(PyQt6.sip.simplewrapper):
    @staticmethod
    def nativeEventFilter(*args, **kwargs):
        ...
class QAbstractProxyModel(QAbstractItemModel):
    @staticmethod
    def buddy(*args, **kwargs):
        ...
    @staticmethod
    def canDropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def canFetchMore(*args, **kwargs):
        ...
    @staticmethod
    def clearItemData(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def fetchMore(*args, **kwargs):
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
    def itemData(*args, **kwargs):
        ...
    @staticmethod
    def mapFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapSelectionFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapSelectionToSource(*args, **kwargs):
        ...
    @staticmethod
    def mapToSource(*args, **kwargs):
        ...
    @staticmethod
    def mimeData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def revert(*args, **kwargs):
        ...
    @staticmethod
    def roleNames(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderData(*args, **kwargs):
        ...
    @staticmethod
    def setItemData(*args, **kwargs):
        ...
    @staticmethod
    def setSourceModel(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def sourceModel(*args, **kwargs):
        ...
    @staticmethod
    def sourceModelChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def span(*args, **kwargs):
        ...
    @staticmethod
    def submit(*args, **kwargs):
        ...
    @staticmethod
    def supportedDragActions(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
class QAbstractTableModel(QAbstractItemModel):
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def hasChildren(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
class QAnimationGroup(QAbstractAnimation):
    @staticmethod
    def addAnimation(*args, **kwargs):
        ...
    @staticmethod
    def animationAt(*args, **kwargs):
        ...
    @staticmethod
    def animationCount(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def indexOfAnimation(*args, **kwargs):
        ...
    @staticmethod
    def insertAnimation(*args, **kwargs):
        ...
    @staticmethod
    def removeAnimation(*args, **kwargs):
        ...
    @staticmethod
    def takeAnimation(*args, **kwargs):
        ...
class QBasicTimer(PyQt6.sip.simplewrapper):
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
    @staticmethod
    def stop(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def timerId(*args, **kwargs):
        ...
class QBitArray(PyQt6.sip.simplewrapper):
    @staticmethod
    def at(*args, **kwargs):
        ...
    @staticmethod
    def bits(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearBit(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def detach(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def fromBits(*args, **kwargs):
        ...
    @staticmethod
    def isDetached(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def setBit(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def testBit(*args, **kwargs):
        ...
    @staticmethod
    def toUInt32(*args, **kwargs):
        ...
    @staticmethod
    def toggleBit(*args, **kwargs):
        ...
    @staticmethod
    def truncate(*args, **kwargs):
        ...
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
    def __iand__(self, value):
        """
        Return self&=value.
        """
    def __ior__(self, value):
        """
        Return self|=value.
        """
    def __ixor__(self, value):
        """
        Return self^=value.
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
    def __or__(self, value):
        """
        Return self|value.
        """
    def __rand__(self, value):
        """
        Return value&self.
        """
    def __ror__(self, value):
        """
        Return value|self.
        """
    def __rxor__(self, value):
        """
        Return value^self.
        """
    def __xor__(self, value):
        """
        Return self^value.
        """
class QBluetoothPermission(PyQt6.sip.simplewrapper):
    class CommunicationMode(enum.Enum):
        Access: typing.ClassVar[QBluetoothPermission.CommunicationMode]  # value = <CommunicationMode.Access: 1>
        Advertise: typing.ClassVar[QBluetoothPermission.CommunicationMode]  # value = <CommunicationMode.Advertise: 2>
        Default: typing.ClassVar[QBluetoothPermission.CommunicationMode]  # value = <CommunicationMode.Default: 3>
    @staticmethod
    def communicationModes(*args, **kwargs):
        ...
    @staticmethod
    def setCommunicationModes(*args, **kwargs):
        ...
class QBuffer(QIODevice):
    @staticmethod
    def atEnd(*args, **kwargs):
        ...
    @staticmethod
    def buffer(*args, **kwargs):
        ...
    @staticmethod
    def canReadLine(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def readData(*args, **kwargs):
        ...
    @staticmethod
    def seek(*args, **kwargs):
        ...
    @staticmethod
    def setBuffer(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QByteArray(PyQt6.sip.simplewrapper):
    class Base64DecodingStatus(enum.Enum):
        IllegalCharacter: typing.ClassVar[QByteArray.Base64DecodingStatus]  # value = <Base64DecodingStatus.IllegalCharacter: 2>
        IllegalInputLength: typing.ClassVar[QByteArray.Base64DecodingStatus]  # value = <Base64DecodingStatus.IllegalInputLength: 1>
        IllegalPadding: typing.ClassVar[QByteArray.Base64DecodingStatus]  # value = <Base64DecodingStatus.IllegalPadding: 3>
        Ok: typing.ClassVar[QByteArray.Base64DecodingStatus]  # value = <Base64DecodingStatus.Ok: 0>
    class Base64Option(enum.Flag):
        AbortOnBase64DecodingErrors: typing.ClassVar[QByteArray.Base64Option]  # value = <Base64Option.AbortOnBase64DecodingErrors: 4>
        Base64UrlEncoding: typing.ClassVar[QByteArray.Base64Option]  # value = <Base64Option.Base64UrlEncoding: 1>
        OmitTrailingEquals: typing.ClassVar[QByteArray.Base64Option]  # value = <Base64Option.OmitTrailingEquals: 2>
    class FromBase64Result(PyQt6.sip.simplewrapper):
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
        def __int__(self):
            """
            int(self)
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
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def assign(*args, **kwargs):
        ...
    @staticmethod
    def at(*args, **kwargs):
        ...
    @staticmethod
    def capacity(*args, **kwargs):
        ...
    @staticmethod
    def chop(*args, **kwargs):
        ...
    @staticmethod
    def chopped(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def compare(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def endsWith(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def first(*args, **kwargs):
        ...
    @staticmethod
    def fromBase64(*args, **kwargs):
        ...
    @staticmethod
    def fromBase64Encoding(*args, **kwargs):
        ...
    @staticmethod
    def fromHex(*args, **kwargs):
        ...
    @staticmethod
    def fromPercentEncoding(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isLower(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isUpper(*args, **kwargs):
        ...
    @staticmethod
    def isValidUtf8(*args, **kwargs):
        ...
    @staticmethod
    def last(*args, **kwargs):
        ...
    @staticmethod
    def lastIndexOf(*args, **kwargs):
        ...
    @staticmethod
    def left(*args, **kwargs):
        ...
    @staticmethod
    def leftJustified(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def mid(*args, **kwargs):
        ...
    @staticmethod
    def number(*args, **kwargs):
        ...
    @staticmethod
    def percentDecoded(*args, **kwargs):
        ...
    @staticmethod
    def prepend(*args, **kwargs):
        ...
    @staticmethod
    def push_back(*args, **kwargs):
        ...
    @staticmethod
    def push_front(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def removeAt(*args, **kwargs):
        ...
    @staticmethod
    def removeFirst(*args, **kwargs):
        ...
    @staticmethod
    def removeLast(*args, **kwargs):
        ...
    @staticmethod
    def repeated(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @staticmethod
    def reserve(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def right(*args, **kwargs):
        ...
    @staticmethod
    def rightJustified(*args, **kwargs):
        ...
    @staticmethod
    def setNum(*args, **kwargs):
        ...
    @staticmethod
    def simplified(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def sliced(*args, **kwargs):
        ...
    @staticmethod
    def split(*args, **kwargs):
        ...
    @staticmethod
    def squeeze(*args, **kwargs):
        ...
    @staticmethod
    def startsWith(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toBase64(*args, **kwargs):
        ...
    @staticmethod
    def toDouble(*args, **kwargs):
        ...
    @staticmethod
    def toFloat(*args, **kwargs):
        ...
    @staticmethod
    def toHex(*args, **kwargs):
        ...
    @staticmethod
    def toInt(*args, **kwargs):
        ...
    @staticmethod
    def toLong(*args, **kwargs):
        ...
    @staticmethod
    def toLongLong(*args, **kwargs):
        ...
    @staticmethod
    def toLower(*args, **kwargs):
        ...
    @staticmethod
    def toPercentEncoding(*args, **kwargs):
        ...
    @staticmethod
    def toShort(*args, **kwargs):
        ...
    @staticmethod
    def toUInt(*args, **kwargs):
        ...
    @staticmethod
    def toULong(*args, **kwargs):
        ...
    @staticmethod
    def toULongLong(*args, **kwargs):
        ...
    @staticmethod
    def toUShort(*args, **kwargs):
        ...
    @staticmethod
    def toUpper(*args, **kwargs):
        ...
    @staticmethod
    def trimmed(*args, **kwargs):
        ...
    @staticmethod
    def truncate(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
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
    def __iadd__(self, value):
        """
        Implement self+=value.
        """
    def __imul__(self, value):
        """
        Implement self*=value.
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
    def __repr__(self):
        """
        Return repr(self).
        """
    def __rmul__(self, value):
        """
        Return value*self.
        """
    def __str__(self):
        """
        Return str(self).
        """
class QByteArrayMatcher(PyQt6.sip.simplewrapper):
    @staticmethod
    def indexIn(*args, **kwargs):
        ...
    @staticmethod
    def pattern(*args, **kwargs):
        ...
    @staticmethod
    def setPattern(*args, **kwargs):
        ...
class QCalendar(PyQt6.sip.simplewrapper):
    class System(enum.Enum):
        Gregorian: typing.ClassVar[QCalendar.System]  # value = <System.Gregorian: 0>
        IslamicCivil: typing.ClassVar[QCalendar.System]  # value = <System.IslamicCivil: 11>
        Jalali: typing.ClassVar[QCalendar.System]  # value = <System.Jalali: 10>
        Julian: typing.ClassVar[QCalendar.System]  # value = <System.Julian: 8>
        Milankovic: typing.ClassVar[QCalendar.System]  # value = <System.Milankovic: 9>
    class YearMonthDay(PyQt6.sip.simplewrapper):
        @staticmethod
        def isValid(*args, **kwargs):
            ...
    Unspecified: typing.ClassVar[int] = -2147483648
    @staticmethod
    def availableCalendars(*args, **kwargs):
        ...
    @staticmethod
    def dateFromParts(*args, **kwargs):
        ...
    @staticmethod
    def dateTimeToString(*args, **kwargs):
        ...
    @staticmethod
    def dayOfWeek(*args, **kwargs):
        ...
    @staticmethod
    def daysInMonth(*args, **kwargs):
        ...
    @staticmethod
    def daysInYear(*args, **kwargs):
        ...
    @staticmethod
    def hasYearZero(*args, **kwargs):
        ...
    @staticmethod
    def isDateValid(*args, **kwargs):
        ...
    @staticmethod
    def isGregorian(*args, **kwargs):
        ...
    @staticmethod
    def isLeapYear(*args, **kwargs):
        ...
    @staticmethod
    def isLunar(*args, **kwargs):
        ...
    @staticmethod
    def isLuniSolar(*args, **kwargs):
        ...
    @staticmethod
    def isProleptic(*args, **kwargs):
        ...
    @staticmethod
    def isSolar(*args, **kwargs):
        ...
    @staticmethod
    def matchCenturyToWeekday(*args, **kwargs):
        ...
    @staticmethod
    def maximumDaysInMonth(*args, **kwargs):
        ...
    @staticmethod
    def maximumMonthsInYear(*args, **kwargs):
        ...
    @staticmethod
    def minimumDaysInMonth(*args, **kwargs):
        ...
    @staticmethod
    def monthName(*args, **kwargs):
        ...
    @staticmethod
    def monthsInYear(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def partsFromDate(*args, **kwargs):
        ...
    @staticmethod
    def standaloneMonthName(*args, **kwargs):
        ...
    @staticmethod
    def standaloneWeekDayName(*args, **kwargs):
        ...
    @staticmethod
    def weekDayName(*args, **kwargs):
        ...
class QCalendarPermission(PyQt6.sip.simplewrapper):
    class AccessMode(enum.Enum):
        ReadOnly: typing.ClassVar[QCalendarPermission.AccessMode]  # value = <AccessMode.ReadOnly: 0>
        ReadWrite: typing.ClassVar[QCalendarPermission.AccessMode]  # value = <AccessMode.ReadWrite: 1>
    @staticmethod
    def accessMode(*args, **kwargs):
        ...
    @staticmethod
    def setAccessMode(*args, **kwargs):
        ...
class QCameraPermission(PyQt6.sip.simplewrapper):
    pass
class QCborError(PyQt6.sip.simplewrapper):
    class Code(enum.Enum):
        AdvancePastEnd: typing.ClassVar[QCborError.Code]  # value = <Code.AdvancePastEnd: 3>
        DataTooLarge: typing.ClassVar[QCborError.Code]  # value = <Code.DataTooLarge: 1024>
        EndOfFile: typing.ClassVar[QCborError.Code]  # value = <Code.EndOfFile: 257>
        GarbageAtEnd: typing.ClassVar[QCborError.Code]  # value = <Code.GarbageAtEnd: 256>
        IllegalNumber: typing.ClassVar[QCborError.Code]  # value = <Code.IllegalNumber: 261>
        IllegalSimpleType: typing.ClassVar[QCborError.Code]  # value = <Code.IllegalSimpleType: 262>
        IllegalType: typing.ClassVar[QCborError.Code]  # value = <Code.IllegalType: 260>
        InputOutputError: typing.ClassVar[QCborError.Code]  # value = <Code.InputOutputError: 4>
        InvalidUtf8String: typing.ClassVar[QCborError.Code]  # value = <Code.InvalidUtf8String: 516>
        NestingTooDeep: typing.ClassVar[QCborError.Code]  # value = <Code.NestingTooDeep: 1025>
        NoError: typing.ClassVar[QCborError.Code]  # value = <Code.NoError: 0>
        UnexpectedBreak: typing.ClassVar[QCborError.Code]  # value = <Code.UnexpectedBreak: 258>
        UnknownError: typing.ClassVar[QCborError.Code]  # value = <Code.UnknownError: 1>
        UnknownType: typing.ClassVar[QCborError.Code]  # value = <Code.UnknownType: 259>
        UnsupportedType: typing.ClassVar[QCborError.Code]  # value = <Code.UnsupportedType: 1026>
    @staticmethod
    def code(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
class QCborKnownTags(enum.Enum):
    Base64: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.Base64: 34>
    Base64url: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.Base64url: 33>
    Bigfloat: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.Bigfloat: 5>
    COSE_Encrypt: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.COSE_Encrypt: 96>
    COSE_Encrypt0: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.COSE_Encrypt0: 16>
    COSE_Mac: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.COSE_Mac: 97>
    COSE_Mac0: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.COSE_Mac0: 17>
    COSE_Sign: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.COSE_Sign: 98>
    COSE_Sign1: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.COSE_Sign1: 18>
    DateTimeString: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.DateTimeString: 0>
    Decimal: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.Decimal: 4>
    EncodedCbor: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.EncodedCbor: 24>
    ExpectedBase16: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.ExpectedBase16: 23>
    ExpectedBase64: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.ExpectedBase64: 22>
    ExpectedBase64url: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.ExpectedBase64url: 21>
    MimeMessage: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.MimeMessage: 36>
    NegativeBignum: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.NegativeBignum: 3>
    PositiveBignum: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.PositiveBignum: 2>
    RegularExpression: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.RegularExpression: 35>
    Signature: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.Signature: 55799>
    UnixTime_t: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.UnixTime_t: 1>
    Url: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.Url: 32>
    Uuid: typing.ClassVar[QCborKnownTags]  # value = <QCborKnownTags.Uuid: 37>
class QCborSimpleType(enum.Enum):
    False_: typing.ClassVar[QCborSimpleType]  # value = <QCborSimpleType.False_: 20>
    Null: typing.ClassVar[QCborSimpleType]  # value = <QCborSimpleType.Null: 22>
    True_: typing.ClassVar[QCborSimpleType]  # value = <QCborSimpleType.True_: 21>
    Undefined: typing.ClassVar[QCborSimpleType]  # value = <QCborSimpleType.Undefined: 23>
class QCborStreamReader(PyQt6.sip.simplewrapper):
    class StringResultCode(enum.Enum):
        EndOfString: typing.ClassVar[QCborStreamReader.StringResultCode]  # value = <StringResultCode.EndOfString: 0>
        Error: typing.ClassVar[QCborStreamReader.StringResultCode]  # value = <StringResultCode.Error: -1>
        Ok: typing.ClassVar[QCborStreamReader.StringResultCode]  # value = <StringResultCode.Ok: 1>
    class Type(enum.Enum):
        Array: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.Array: 128>
        ByteString: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.ByteString: 64>
        Double: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.Double: 251>
        Float: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.Float: 250>
        HalfFloat: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.HalfFloat: 249>
        Invalid: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.Invalid: 255>
        Map: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.Map: 160>
        NegativeInteger: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.NegativeInteger: 32>
        SimpleType: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.SimpleType: 224>
        Tag: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.Tag: 192>
        TextString: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.TextString: 96>
        UnsignedInteger: typing.ClassVar[QCborStreamReader.Type]  # value = <Type.UnsignedInteger: 0>
    @staticmethod
    def addData(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def containerDepth(*args, **kwargs):
        ...
    @staticmethod
    def currentOffset(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def enterContainer(*args, **kwargs):
        ...
    @staticmethod
    def hasNext(*args, **kwargs):
        ...
    @staticmethod
    def isArray(*args, **kwargs):
        ...
    @staticmethod
    def isBool(*args, **kwargs):
        ...
    @staticmethod
    def isByteArray(*args, **kwargs):
        ...
    @staticmethod
    def isContainer(*args, **kwargs):
        ...
    @staticmethod
    def isDouble(*args, **kwargs):
        ...
    @staticmethod
    def isFalse(*args, **kwargs):
        ...
    @staticmethod
    def isFloat(*args, **kwargs):
        ...
    @staticmethod
    def isFloat16(*args, **kwargs):
        ...
    @staticmethod
    def isInteger(*args, **kwargs):
        ...
    @staticmethod
    def isInvalid(*args, **kwargs):
        ...
    @staticmethod
    def isLengthKnown(*args, **kwargs):
        ...
    @staticmethod
    def isMap(*args, **kwargs):
        ...
    @staticmethod
    def isNegativeInteger(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isSimpleType(*args, **kwargs):
        ...
    @staticmethod
    def isString(*args, **kwargs):
        ...
    @staticmethod
    def isTag(*args, **kwargs):
        ...
    @staticmethod
    def isTrue(*args, **kwargs):
        ...
    @staticmethod
    def isUndefined(*args, **kwargs):
        ...
    @staticmethod
    def isUnsignedInteger(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastError(*args, **kwargs):
        ...
    @staticmethod
    def leaveContainer(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def next(*args, **kwargs):
        ...
    @staticmethod
    def parentContainerType(*args, **kwargs):
        ...
    @staticmethod
    def readAllByteArray(*args, **kwargs):
        ...
    @staticmethod
    def readAllString(*args, **kwargs):
        ...
    @staticmethod
    def readAllUtf8String(*args, **kwargs):
        ...
    @staticmethod
    def readAndAppendToByteArray(*args, **kwargs):
        ...
    @staticmethod
    def readAndAppendToString(*args, **kwargs):
        ...
    @staticmethod
    def readAndAppendToUtf8String(*args, **kwargs):
        ...
    @staticmethod
    def readByteArray(*args, **kwargs):
        ...
    @staticmethod
    def readString(*args, **kwargs):
        ...
    @staticmethod
    def readUtf8String(*args, **kwargs):
        ...
    @staticmethod
    def reparse(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def toBool(*args, **kwargs):
        ...
    @staticmethod
    def toDouble(*args, **kwargs):
        ...
    @staticmethod
    def toInteger(*args, **kwargs):
        ...
    @staticmethod
    def toSimpleType(*args, **kwargs):
        ...
    @staticmethod
    def toUnsignedInteger(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    def __len__(self):
        """
        Return len(self).
        """
class QCborStreamWriter(PyQt6.sip.simplewrapper):
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def appendNull(*args, **kwargs):
        ...
    @staticmethod
    def appendUndefined(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def endArray(*args, **kwargs):
        ...
    @staticmethod
    def endMap(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def startArray(*args, **kwargs):
        ...
    @staticmethod
    def startMap(*args, **kwargs):
        ...
class QChildEvent(QEvent):
    @staticmethod
    def added(*args, **kwargs):
        ...
    @staticmethod
    def child(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def polished(*args, **kwargs):
        ...
    @staticmethod
    def removed(*args, **kwargs):
        ...
class QCollator(PyQt6.sip.simplewrapper):
    @staticmethod
    def caseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def compare(*args, **kwargs):
        ...
    @staticmethod
    def defaultCompare(*args, **kwargs):
        ...
    @staticmethod
    def defaultSortKey(*args, **kwargs):
        ...
    @staticmethod
    def ignorePunctuation(*args, **kwargs):
        ...
    @staticmethod
    def locale(*args, **kwargs):
        ...
    @staticmethod
    def numericMode(*args, **kwargs):
        ...
    @staticmethod
    def setCaseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def setIgnorePunctuation(*args, **kwargs):
        ...
    @staticmethod
    def setLocale(*args, **kwargs):
        ...
    @staticmethod
    def setNumericMode(*args, **kwargs):
        ...
    @staticmethod
    def sortKey(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QCollatorSortKey(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def compare(*args, **kwargs):
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
class QCommandLineOption(PyQt6.sip.simplewrapper):
    class Flag(enum.Flag):
        HiddenFromHelp: typing.ClassVar[QCommandLineOption.Flag]  # value = <Flag.HiddenFromHelp: 1>
        ShortOptionStyle: typing.ClassVar[QCommandLineOption.Flag]  # value = <Flag.ShortOptionStyle: 2>
    @staticmethod
    def defaultValues(*args, **kwargs):
        ...
    @staticmethod
    def description(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def names(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultValue(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultValues(*args, **kwargs):
        ...
    @staticmethod
    def setDescription(*args, **kwargs):
        ...
    @staticmethod
    def setFlags(*args, **kwargs):
        ...
    @staticmethod
    def setValueName(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def valueName(*args, **kwargs):
        ...
class QCommandLineParser(PyQt6.sip.simplewrapper):
    class OptionsAfterPositionalArgumentsMode(enum.Enum):
        ParseAsOptions: typing.ClassVar[QCommandLineParser.OptionsAfterPositionalArgumentsMode]  # value = <OptionsAfterPositionalArgumentsMode.ParseAsOptions: 0>
        ParseAsPositionalArguments: typing.ClassVar[QCommandLineParser.OptionsAfterPositionalArgumentsMode]  # value = <OptionsAfterPositionalArgumentsMode.ParseAsPositionalArguments: 1>
    class SingleDashWordOptionMode(enum.Enum):
        ParseAsCompactedShortOptions: typing.ClassVar[QCommandLineParser.SingleDashWordOptionMode]  # value = <SingleDashWordOptionMode.ParseAsCompactedShortOptions: 0>
        ParseAsLongOptions: typing.ClassVar[QCommandLineParser.SingleDashWordOptionMode]  # value = <SingleDashWordOptionMode.ParseAsLongOptions: 1>
    @staticmethod
    def addHelpOption(*args, **kwargs):
        ...
    @staticmethod
    def addOption(*args, **kwargs):
        ...
    @staticmethod
    def addOptions(*args, **kwargs):
        ...
    @staticmethod
    def addPositionalArgument(*args, **kwargs):
        ...
    @staticmethod
    def addVersionOption(*args, **kwargs):
        ...
    @staticmethod
    def applicationDescription(*args, **kwargs):
        ...
    @staticmethod
    def clearPositionalArguments(*args, **kwargs):
        ...
    @staticmethod
    def errorText(*args, **kwargs):
        ...
    @staticmethod
    def helpText(*args, **kwargs):
        ...
    @staticmethod
    def isSet(*args, **kwargs):
        ...
    @staticmethod
    def optionNames(*args, **kwargs):
        ...
    @staticmethod
    def parse(*args, **kwargs):
        ...
    @staticmethod
    def positionalArguments(*args, **kwargs):
        ...
    @staticmethod
    def process(*args, **kwargs):
        ...
    @staticmethod
    def setApplicationDescription(*args, **kwargs):
        ...
    @staticmethod
    def setOptionsAfterPositionalArgumentsMode(*args, **kwargs):
        ...
    @staticmethod
    def setSingleDashWordOptionMode(*args, **kwargs):
        ...
    @staticmethod
    def showHelp(*args, **kwargs):
        ...
    @staticmethod
    def showVersion(*args, **kwargs):
        ...
    @staticmethod
    def unknownOptionNames(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def values(*args, **kwargs):
        ...
class QConcatenateTablesProxyModel(QAbstractItemModel):
    @staticmethod
    def addSourceModel(*args, **kwargs):
        ...
    @staticmethod
    def canDropMimeData(*args, **kwargs):
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
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def itemData(*args, **kwargs):
        ...
    @staticmethod
    def mapFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapToSource(*args, **kwargs):
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
    def removeSourceModel(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setItemData(*args, **kwargs):
        ...
    @staticmethod
    def sourceModels(*args, **kwargs):
        ...
    @staticmethod
    def span(*args, **kwargs):
        ...
class QContactsPermission(PyQt6.sip.simplewrapper):
    class AccessMode(enum.Enum):
        ReadOnly: typing.ClassVar[QContactsPermission.AccessMode]  # value = <AccessMode.ReadOnly: 0>
        ReadWrite: typing.ClassVar[QContactsPermission.AccessMode]  # value = <AccessMode.ReadWrite: 1>
    @staticmethod
    def accessMode(*args, **kwargs):
        ...
    @staticmethod
    def setAccessMode(*args, **kwargs):
        ...
class QCoreApplication(QObject):
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def aboutToQuit(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def addLibraryPath(*args, **kwargs):
        ...
    @staticmethod
    def applicationDirPath(*args, **kwargs):
        ...
    @staticmethod
    def applicationFilePath(*args, **kwargs):
        ...
    @staticmethod
    def applicationName(*args, **kwargs):
        ...
    @staticmethod
    def applicationPid(*args, **kwargs):
        ...
    @staticmethod
    def applicationVersion(*args, **kwargs):
        ...
    @staticmethod
    def arguments(*args, **kwargs):
        ...
    @staticmethod
    def checkPermission(*args, **kwargs):
        ...
    @staticmethod
    def closingDown(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventDispatcher(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def exit(*args, **kwargs):
        ...
    @staticmethod
    def installNativeEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def installTranslator(*args, **kwargs):
        ...
    @staticmethod
    def instance(*args, **kwargs):
        ...
    @staticmethod
    def isQuitLockEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isSetuidAllowed(*args, **kwargs):
        ...
    @staticmethod
    def libraryPaths(*args, **kwargs):
        ...
    @staticmethod
    def notify(*args, **kwargs):
        ...
    @staticmethod
    def organizationDomain(*args, **kwargs):
        ...
    @staticmethod
    def organizationName(*args, **kwargs):
        ...
    @staticmethod
    def postEvent(*args, **kwargs):
        ...
    @staticmethod
    def processEvents(*args, **kwargs):
        ...
    @staticmethod
    def quit(*args, **kwargs):
        ...
    @staticmethod
    def removeLibraryPath(*args, **kwargs):
        ...
    @staticmethod
    def removeNativeEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def removePostedEvents(*args, **kwargs):
        ...
    @staticmethod
    def removeTranslator(*args, **kwargs):
        ...
    @staticmethod
    def requestPermission(*args, **kwargs):
        ...
    @staticmethod
    def sendEvent(*args, **kwargs):
        ...
    @staticmethod
    def sendPostedEvents(*args, **kwargs):
        ...
    @staticmethod
    def setApplicationName(*args, **kwargs):
        ...
    @staticmethod
    def setApplicationVersion(*args, **kwargs):
        ...
    @staticmethod
    def setAttribute(*args, **kwargs):
        ...
    @staticmethod
    def setEventDispatcher(*args, **kwargs):
        ...
    @staticmethod
    def setLibraryPaths(*args, **kwargs):
        ...
    @staticmethod
    def setOrganizationDomain(*args, **kwargs):
        ...
    @staticmethod
    def setOrganizationName(*args, **kwargs):
        ...
    @staticmethod
    def setQuitLockEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSetuidAllowed(*args, **kwargs):
        ...
    @staticmethod
    def startingUp(*args, **kwargs):
        ...
    @staticmethod
    def testAttribute(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
class QCryptographicHash(PyQt6.sip.simplewrapper):
    class Algorithm(enum.Enum):
        Blake2b_160: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2b_160: 15>
        Blake2b_256: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2b_256: 16>
        Blake2b_384: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2b_384: 17>
        Blake2b_512: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2b_512: 18>
        Blake2s_128: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2s_128: 19>
        Blake2s_160: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2s_160: 20>
        Blake2s_224: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2s_224: 21>
        Blake2s_256: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Blake2s_256: 22>
        Keccak_224: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Keccak_224: 7>
        Keccak_256: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Keccak_256: 8>
        Keccak_384: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Keccak_384: 9>
        Keccak_512: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Keccak_512: 10>
        Md4: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Md4: 0>
        Md5: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Md5: 1>
        Sha1: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha1: 2>
        Sha224: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha224: 3>
        Sha256: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha256: 4>
        Sha384: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha384: 5>
        Sha3_224: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha3_224: 11>
        Sha3_256: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha3_256: 12>
        Sha3_384: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha3_384: 13>
        Sha3_512: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha3_512: 14>
        Sha512: typing.ClassVar[QCryptographicHash.Algorithm]  # value = <Algorithm.Sha512: 6>
    @staticmethod
    def addData(*args, **kwargs):
        ...
    @staticmethod
    def algorithm(*args, **kwargs):
        ...
    @staticmethod
    def hash(*args, **kwargs):
        ...
    @staticmethod
    def hashLength(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def result(*args, **kwargs):
        ...
    @staticmethod
    def resultView(*args, **kwargs):
        ...
    @staticmethod
    def supportsAlgorithm(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QDataStream(QIODeviceBase):
    class ByteOrder(enum.Enum):
        BigEndian: typing.ClassVar[QDataStream.ByteOrder]  # value = <ByteOrder.BigEndian: 0>
        LittleEndian: typing.ClassVar[QDataStream.ByteOrder]  # value = <ByteOrder.LittleEndian: 1>
    class FloatingPointPrecision(enum.Enum):
        DoublePrecision: typing.ClassVar[QDataStream.FloatingPointPrecision]  # value = <FloatingPointPrecision.DoublePrecision: 1>
        SinglePrecision: typing.ClassVar[QDataStream.FloatingPointPrecision]  # value = <FloatingPointPrecision.SinglePrecision: 0>
    class Status(enum.Enum):
        Ok: typing.ClassVar[QDataStream.Status]  # value = <Status.Ok: 0>
        ReadCorruptData: typing.ClassVar[QDataStream.Status]  # value = <Status.ReadCorruptData: 2>
        ReadPastEnd: typing.ClassVar[QDataStream.Status]  # value = <Status.ReadPastEnd: 1>
        SizeLimitExceeded: typing.ClassVar[QDataStream.Status]  # value = <Status.SizeLimitExceeded: 4>
        WriteFailed: typing.ClassVar[QDataStream.Status]  # value = <Status.WriteFailed: 3>
    class Version(enum.IntEnum):
        Qt_1_0: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_1_0: 1>
        Qt_2_0: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_2_0: 2>
        Qt_2_1: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_2_1: 3>
        Qt_3_0: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_3_0: 4>
        Qt_3_1: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_3_1: 5>
        Qt_3_3: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_3_3: 6>
        Qt_4_0: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_4_0: 7>
        Qt_4_2: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_4_2: 8>
        Qt_4_3: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_4_3: 9>
        Qt_4_4: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_4_4: 10>
        Qt_4_5: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_4_5: 11>
        Qt_4_6: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_4_6: 12>
        Qt_5_0: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_5_0: 13>
        Qt_5_1: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_5_1: 14>
        Qt_5_12: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_5_12: 18>
        Qt_5_13: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_5_13: 19>
        Qt_5_2: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_5_2: 15>
        Qt_5_4: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_5_4: 16>
        Qt_5_6: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_5_6: 17>
        Qt_6_0: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_6_0: 20>
        Qt_6_6: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_6_6: 21>
        Qt_6_7: typing.ClassVar[QDataStream.Version]  # value = <Version.Qt_6_7: 22>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    @staticmethod
    def abortTransaction(*args, **kwargs):
        ...
    @staticmethod
    def atEnd(*args, **kwargs):
        ...
    @staticmethod
    def byteOrder(*args, **kwargs):
        ...
    @staticmethod
    def commitTransaction(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def floatingPointPrecision(*args, **kwargs):
        ...
    @staticmethod
    def readBool(*args, **kwargs):
        ...
    @staticmethod
    def readBytes(*args, **kwargs):
        ...
    @staticmethod
    def readDouble(*args, **kwargs):
        ...
    @staticmethod
    def readFloat(*args, **kwargs):
        ...
    @staticmethod
    def readInt(*args, **kwargs):
        ...
    @staticmethod
    def readInt16(*args, **kwargs):
        ...
    @staticmethod
    def readInt32(*args, **kwargs):
        ...
    @staticmethod
    def readInt64(*args, **kwargs):
        ...
    @staticmethod
    def readInt8(*args, **kwargs):
        ...
    @staticmethod
    def readQString(*args, **kwargs):
        ...
    @staticmethod
    def readQStringList(*args, **kwargs):
        ...
    @staticmethod
    def readQVariant(*args, **kwargs):
        ...
    @staticmethod
    def readQVariantHash(*args, **kwargs):
        ...
    @staticmethod
    def readQVariantList(*args, **kwargs):
        ...
    @staticmethod
    def readQVariantMap(*args, **kwargs):
        ...
    @staticmethod
    def readRawData(*args, **kwargs):
        ...
    @staticmethod
    def readString(*args, **kwargs):
        ...
    @staticmethod
    def readUInt16(*args, **kwargs):
        ...
    @staticmethod
    def readUInt32(*args, **kwargs):
        ...
    @staticmethod
    def readUInt64(*args, **kwargs):
        ...
    @staticmethod
    def readUInt8(*args, **kwargs):
        ...
    @staticmethod
    def resetStatus(*args, **kwargs):
        ...
    @staticmethod
    def rollbackTransaction(*args, **kwargs):
        ...
    @staticmethod
    def setByteOrder(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setFloatingPointPrecision(*args, **kwargs):
        ...
    @staticmethod
    def setStatus(*args, **kwargs):
        ...
    @staticmethod
    def setVersion(*args, **kwargs):
        ...
    @staticmethod
    def skipRawData(*args, **kwargs):
        ...
    @staticmethod
    def startTransaction(*args, **kwargs):
        ...
    @staticmethod
    def status(*args, **kwargs):
        ...
    @staticmethod
    def version(*args, **kwargs):
        ...
    @staticmethod
    def writeBool(*args, **kwargs):
        ...
    @staticmethod
    def writeBytes(*args, **kwargs):
        ...
    @staticmethod
    def writeDouble(*args, **kwargs):
        ...
    @staticmethod
    def writeFloat(*args, **kwargs):
        ...
    @staticmethod
    def writeInt(*args, **kwargs):
        ...
    @staticmethod
    def writeInt16(*args, **kwargs):
        ...
    @staticmethod
    def writeInt32(*args, **kwargs):
        ...
    @staticmethod
    def writeInt64(*args, **kwargs):
        ...
    @staticmethod
    def writeInt8(*args, **kwargs):
        ...
    @staticmethod
    def writeQString(*args, **kwargs):
        ...
    @staticmethod
    def writeQStringList(*args, **kwargs):
        ...
    @staticmethod
    def writeQVariant(*args, **kwargs):
        ...
    @staticmethod
    def writeQVariantHash(*args, **kwargs):
        ...
    @staticmethod
    def writeQVariantList(*args, **kwargs):
        ...
    @staticmethod
    def writeQVariantMap(*args, **kwargs):
        ...
    @staticmethod
    def writeRawData(*args, **kwargs):
        ...
    @staticmethod
    def writeString(*args, **kwargs):
        ...
    @staticmethod
    def writeUInt16(*args, **kwargs):
        ...
    @staticmethod
    def writeUInt32(*args, **kwargs):
        ...
    @staticmethod
    def writeUInt64(*args, **kwargs):
        ...
    @staticmethod
    def writeUInt8(*args, **kwargs):
        ...
    def __lshift__(self, value):
        """
        Return self<<value.
        """
    def __rlshift__(self, value):
        """
        Return value<<self.
        """
    def __rrshift__(self, value):
        """
        Return value>>self.
        """
    def __rshift__(self, value):
        """
        Return self>>value.
        """
class QDate(PyQt6.sip.simplewrapper):
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def addDays(*args, **kwargs):
        ...
    @staticmethod
    def addMonths(*args, **kwargs):
        ...
    @staticmethod
    def addYears(*args, **kwargs):
        ...
    @staticmethod
    def currentDate(*args, **kwargs):
        ...
    @staticmethod
    def day(*args, **kwargs):
        ...
    @staticmethod
    def dayOfWeek(*args, **kwargs):
        ...
    @staticmethod
    def dayOfYear(*args, **kwargs):
        ...
    @staticmethod
    def daysInMonth(*args, **kwargs):
        ...
    @staticmethod
    def daysInYear(*args, **kwargs):
        ...
    @staticmethod
    def daysTo(*args, **kwargs):
        ...
    @staticmethod
    def endOfDay(*args, **kwargs):
        ...
    @staticmethod
    def fromJulianDay(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def getDate(*args, **kwargs):
        ...
    @staticmethod
    def isLeapYear(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def month(*args, **kwargs):
        ...
    @staticmethod
    def setDate(*args, **kwargs):
        ...
    @staticmethod
    def startOfDay(*args, **kwargs):
        ...
    @staticmethod
    def toJulianDay(*args, **kwargs):
        ...
    @staticmethod
    def toPyDate(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    @staticmethod
    def weekNumber(*args, **kwargs):
        ...
    @staticmethod
    def year(*args, **kwargs):
        ...
    def __bool__(self):
        """
        True if self else False
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
class QDateTime(PyQt6.sip.simplewrapper):
    class TransitionResolution(enum.Enum):
        PreferAfter: typing.ClassVar[QDateTime.TransitionResolution]  # value = <TransitionResolution.PreferAfter: 4>
        PreferBefore: typing.ClassVar[QDateTime.TransitionResolution]  # value = <TransitionResolution.PreferBefore: 3>
        PreferDaylightSaving: typing.ClassVar[QDateTime.TransitionResolution]  # value = <TransitionResolution.PreferDaylightSaving: 6>
        PreferStandard: typing.ClassVar[QDateTime.TransitionResolution]  # value = <TransitionResolution.PreferStandard: 5>
        Reject: typing.ClassVar[QDateTime.TransitionResolution]  # value = <TransitionResolution.Reject: 0>
        RelativeToAfter: typing.ClassVar[QDateTime.TransitionResolution]  # value = <TransitionResolution.RelativeToAfter: 2>
        RelativeToBefore: typing.ClassVar[QDateTime.TransitionResolution]  # value = <TransitionResolution.RelativeToBefore: 1>
    class YearRange(enum.Enum):
        First: typing.ClassVar[QDateTime.YearRange]  # value = <YearRange.First: -292275056>
        Last: typing.ClassVar[QDateTime.YearRange]  # value = <YearRange.Last: 292278994>
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def addDays(*args, **kwargs):
        ...
    @staticmethod
    def addMSecs(*args, **kwargs):
        ...
    @staticmethod
    def addMonths(*args, **kwargs):
        ...
    @staticmethod
    def addSecs(*args, **kwargs):
        ...
    @staticmethod
    def addYears(*args, **kwargs):
        ...
    @staticmethod
    def currentDateTime(*args, **kwargs):
        ...
    @staticmethod
    def currentDateTimeUtc(*args, **kwargs):
        ...
    @staticmethod
    def currentMSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def currentSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def date(*args, **kwargs):
        ...
    @staticmethod
    def daysTo(*args, **kwargs):
        ...
    @staticmethod
    def fromMSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def fromSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def isDaylightTime(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def msecsTo(*args, **kwargs):
        ...
    @staticmethod
    def offsetFromUtc(*args, **kwargs):
        ...
    @staticmethod
    def secsTo(*args, **kwargs):
        ...
    @staticmethod
    def setDate(*args, **kwargs):
        ...
    @staticmethod
    def setMSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def setOffsetFromUtc(*args, **kwargs):
        ...
    @staticmethod
    def setSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def setTime(*args, **kwargs):
        ...
    @staticmethod
    def setTimeSpec(*args, **kwargs):
        ...
    @staticmethod
    def setTimeZone(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def time(*args, **kwargs):
        ...
    @staticmethod
    def timeRepresentation(*args, **kwargs):
        ...
    @staticmethod
    def timeSpec(*args, **kwargs):
        ...
    @staticmethod
    def timeZone(*args, **kwargs):
        ...
    @staticmethod
    def timeZoneAbbreviation(*args, **kwargs):
        ...
    @staticmethod
    def toLocalTime(*args, **kwargs):
        ...
    @staticmethod
    def toMSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def toOffsetFromUtc(*args, **kwargs):
        ...
    @staticmethod
    def toPyDateTime(*args, **kwargs):
        ...
    @staticmethod
    def toSecsSinceEpoch(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    @staticmethod
    def toTimeSpec(*args, **kwargs):
        ...
    @staticmethod
    def toTimeZone(*args, **kwargs):
        ...
    @staticmethod
    def toUTC(*args, **kwargs):
        ...
    def __bool__(self):
        """
        True if self else False
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
class QDeadlineTimer(PyQt6.sip.simplewrapper):
    class ForeverConstant(enum.Enum):
        Forever: typing.ClassVar[QDeadlineTimer.ForeverConstant]  # value = <ForeverConstant.Forever: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def addNSecs(*args, **kwargs):
        ...
    @staticmethod
    def current(*args, **kwargs):
        ...
    @staticmethod
    def deadline(*args, **kwargs):
        ...
    @staticmethod
    def deadlineNSecs(*args, **kwargs):
        ...
    @staticmethod
    def hasExpired(*args, **kwargs):
        ...
    @staticmethod
    def isForever(*args, **kwargs):
        ...
    @staticmethod
    def remainingTime(*args, **kwargs):
        ...
    @staticmethod
    def remainingTimeNSecs(*args, **kwargs):
        ...
    @staticmethod
    def setDeadline(*args, **kwargs):
        ...
    @staticmethod
    def setPreciseDeadline(*args, **kwargs):
        ...
    @staticmethod
    def setPreciseRemainingTime(*args, **kwargs):
        ...
    @staticmethod
    def setRemainingTime(*args, **kwargs):
        ...
    @staticmethod
    def setTimerType(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def timerType(*args, **kwargs):
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
    def __radd__(self, value):
        """
        Return value+self.
        """
    def __rsub__(self, value):
        """
        Return value-self.
        """
    def __sub__(self, value):
        """
        Return self-value.
        """
class QDir(PyQt6.sip.simplewrapper):
    class Filter(enum.Flag):
        AllDirs: typing.ClassVar[QDir.Filter]  # value = <Filter.AllDirs: 1024>
        CaseSensitive: typing.ClassVar[QDir.Filter]  # value = <Filter.CaseSensitive: 2048>
        Dirs: typing.ClassVar[QDir.Filter]  # value = <Filter.Dirs: 1>
        Drives: typing.ClassVar[QDir.Filter]  # value = <Filter.Drives: 4>
        Executable: typing.ClassVar[QDir.Filter]  # value = <Filter.Executable: 64>
        Files: typing.ClassVar[QDir.Filter]  # value = <Filter.Files: 2>
        Hidden: typing.ClassVar[QDir.Filter]  # value = <Filter.Hidden: 256>
        Modified: typing.ClassVar[QDir.Filter]  # value = <Filter.Modified: 128>
        NoDot: typing.ClassVar[QDir.Filter]  # value = <Filter.NoDot: 8192>
        NoDotDot: typing.ClassVar[QDir.Filter]  # value = <Filter.NoDotDot: 16384>
        NoSymLinks: typing.ClassVar[QDir.Filter]  # value = <Filter.NoSymLinks: 8>
        Readable: typing.ClassVar[QDir.Filter]  # value = <Filter.Readable: 16>
        System: typing.ClassVar[QDir.Filter]  # value = <Filter.System: 512>
        Writable: typing.ClassVar[QDir.Filter]  # value = <Filter.Writable: 32>
    class SortFlag(enum.Flag):
        DirsFirst: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.DirsFirst: 4>
        DirsLast: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.DirsLast: 32>
        IgnoreCase: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.IgnoreCase: 16>
        LocaleAware: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.LocaleAware: 64>
        Reversed: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.Reversed: 8>
        Size: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.Size: 2>
        Time: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.Time: 1>
        Type: typing.ClassVar[QDir.SortFlag]  # value = <SortFlag.Type: 128>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def absoluteFilePath(*args, **kwargs):
        ...
    @staticmethod
    def absolutePath(*args, **kwargs):
        ...
    @staticmethod
    def addSearchPath(*args, **kwargs):
        ...
    @staticmethod
    def canonicalPath(*args, **kwargs):
        ...
    @staticmethod
    def cd(*args, **kwargs):
        ...
    @staticmethod
    def cdUp(*args, **kwargs):
        ...
    @staticmethod
    def cleanPath(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def current(*args, **kwargs):
        ...
    @staticmethod
    def currentPath(*args, **kwargs):
        ...
    @staticmethod
    def dirName(*args, **kwargs):
        ...
    @staticmethod
    def drives(*args, **kwargs):
        ...
    @staticmethod
    def entryInfoList(*args, **kwargs):
        ...
    @staticmethod
    def entryList(*args, **kwargs):
        ...
    @staticmethod
    def exists(*args, **kwargs):
        ...
    @staticmethod
    def filePath(*args, **kwargs):
        ...
    @staticmethod
    def filter(*args, **kwargs):
        ...
    @staticmethod
    def fromNativeSeparators(*args, **kwargs):
        ...
    @staticmethod
    def home(*args, **kwargs):
        ...
    @staticmethod
    def homePath(*args, **kwargs):
        ...
    @staticmethod
    def isAbsolute(*args, **kwargs):
        ...
    @staticmethod
    def isAbsolutePath(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isReadable(*args, **kwargs):
        ...
    @staticmethod
    def isRelative(*args, **kwargs):
        ...
    @staticmethod
    def isRelativePath(*args, **kwargs):
        ...
    @staticmethod
    def isRoot(*args, **kwargs):
        ...
    @staticmethod
    def listSeparator(*args, **kwargs):
        ...
    @staticmethod
    def makeAbsolute(*args, **kwargs):
        ...
    @staticmethod
    def match(*args, **kwargs):
        ...
    @staticmethod
    def mkdir(*args, **kwargs):
        ...
    @staticmethod
    def mkpath(*args, **kwargs):
        ...
    @staticmethod
    def nameFilters(*args, **kwargs):
        ...
    @staticmethod
    def nameFiltersFromString(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
    @staticmethod
    def refresh(*args, **kwargs):
        ...
    @staticmethod
    def relativeFilePath(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def removeRecursively(*args, **kwargs):
        ...
    @staticmethod
    def rename(*args, **kwargs):
        ...
    @staticmethod
    def rmdir(*args, **kwargs):
        ...
    @staticmethod
    def rmpath(*args, **kwargs):
        ...
    @staticmethod
    def root(*args, **kwargs):
        ...
    @staticmethod
    def rootPath(*args, **kwargs):
        ...
    @staticmethod
    def searchPaths(*args, **kwargs):
        ...
    @staticmethod
    def separator(*args, **kwargs):
        ...
    @staticmethod
    def setCurrent(*args, **kwargs):
        ...
    @staticmethod
    def setFilter(*args, **kwargs):
        ...
    @staticmethod
    def setNameFilters(*args, **kwargs):
        ...
    @staticmethod
    def setPath(*args, **kwargs):
        ...
    @staticmethod
    def setSearchPaths(*args, **kwargs):
        ...
    @staticmethod
    def setSorting(*args, **kwargs):
        ...
    @staticmethod
    def sorting(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def temp(*args, **kwargs):
        ...
    @staticmethod
    def tempPath(*args, **kwargs):
        ...
    @staticmethod
    def toNativeSeparators(*args, **kwargs):
        ...
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
    def __getitem__(self, key):
        """
        Return self[key].
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
class QDirIterator(PyQt6.sip.simplewrapper):
    class IteratorFlag(enum.Flag):
        FollowSymlinks: typing.ClassVar[QDirIterator.IteratorFlag]  # value = <IteratorFlag.FollowSymlinks: 1>
        Subdirectories: typing.ClassVar[QDirIterator.IteratorFlag]  # value = <IteratorFlag.Subdirectories: 2>
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
    def hasNext(*args, **kwargs):
        ...
    @staticmethod
    def next(*args, **kwargs):
        ...
    @staticmethod
    def nextFileInfo(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
class QDynamicPropertyChangeEvent(QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def propertyName(*args, **kwargs):
        ...
class QEasingCurve(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        BezierSpline: typing.ClassVar[QEasingCurve.Type]  # value = <Type.BezierSpline: 45>
        CosineCurve: typing.ClassVar[QEasingCurve.Type]  # value = <Type.CosineCurve: 44>
        Custom: typing.ClassVar[QEasingCurve.Type]  # value = <Type.Custom: 47>
        InBack: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InBack: 33>
        InBounce: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InBounce: 37>
        InCirc: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InCirc: 25>
        InCubic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InCubic: 5>
        InCurve: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InCurve: 41>
        InElastic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InElastic: 29>
        InExpo: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InExpo: 21>
        InOutBack: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutBack: 35>
        InOutBounce: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutBounce: 39>
        InOutCirc: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutCirc: 27>
        InOutCubic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutCubic: 7>
        InOutElastic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutElastic: 31>
        InOutExpo: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutExpo: 23>
        InOutQuad: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutQuad: 3>
        InOutQuart: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutQuart: 11>
        InOutQuint: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutQuint: 15>
        InOutSine: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InOutSine: 19>
        InQuad: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InQuad: 1>
        InQuart: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InQuart: 9>
        InQuint: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InQuint: 13>
        InSine: typing.ClassVar[QEasingCurve.Type]  # value = <Type.InSine: 17>
        Linear: typing.ClassVar[QEasingCurve.Type]  # value = <Type.Linear: 0>
        OutBack: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutBack: 34>
        OutBounce: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutBounce: 38>
        OutCirc: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutCirc: 26>
        OutCubic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutCubic: 6>
        OutCurve: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutCurve: 42>
        OutElastic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutElastic: 30>
        OutExpo: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutExpo: 22>
        OutInBack: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInBack: 36>
        OutInBounce: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInBounce: 40>
        OutInCirc: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInCirc: 28>
        OutInCubic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInCubic: 8>
        OutInElastic: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInElastic: 32>
        OutInExpo: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInExpo: 24>
        OutInQuad: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInQuad: 4>
        OutInQuart: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInQuart: 12>
        OutInQuint: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInQuint: 16>
        OutInSine: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutInSine: 20>
        OutQuad: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutQuad: 2>
        OutQuart: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutQuart: 10>
        OutQuint: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutQuint: 14>
        OutSine: typing.ClassVar[QEasingCurve.Type]  # value = <Type.OutSine: 18>
        SineCurve: typing.ClassVar[QEasingCurve.Type]  # value = <Type.SineCurve: 43>
        TCBSpline: typing.ClassVar[QEasingCurve.Type]  # value = <Type.TCBSpline: 46>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def addCubicBezierSegment(*args, **kwargs):
        ...
    @staticmethod
    def addTCBSegment(*args, **kwargs):
        ...
    @staticmethod
    def amplitude(*args, **kwargs):
        ...
    @staticmethod
    def customType(*args, **kwargs):
        ...
    @staticmethod
    def overshoot(*args, **kwargs):
        ...
    @staticmethod
    def period(*args, **kwargs):
        ...
    @staticmethod
    def setAmplitude(*args, **kwargs):
        ...
    @staticmethod
    def setCustomType(*args, **kwargs):
        ...
    @staticmethod
    def setOvershoot(*args, **kwargs):
        ...
    @staticmethod
    def setPeriod(*args, **kwargs):
        ...
    @staticmethod
    def setType(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toCubicSpline(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def valueForProgress(*args, **kwargs):
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
class QElapsedTimer(PyQt6.sip.simplewrapper):
    class ClockType(enum.Enum):
        MachAbsoluteTime: typing.ClassVar[QElapsedTimer.ClockType]  # value = <ClockType.MachAbsoluteTime: 3>
        MonotonicClock: typing.ClassVar[QElapsedTimer.ClockType]  # value = <ClockType.MonotonicClock: 1>
        PerformanceCounter: typing.ClassVar[QElapsedTimer.ClockType]  # value = <ClockType.PerformanceCounter: 4>
        SystemTime: typing.ClassVar[QElapsedTimer.ClockType]  # value = <ClockType.SystemTime: 0>
        TickCounter: typing.ClassVar[QElapsedTimer.ClockType]  # value = <ClockType.TickCounter: 2>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def clockType(*args, **kwargs):
        ...
    @staticmethod
    def elapsed(*args, **kwargs):
        ...
    @staticmethod
    def hasExpired(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def isMonotonic(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def msecsSinceReference(*args, **kwargs):
        ...
    @staticmethod
    def msecsTo(*args, **kwargs):
        ...
    @staticmethod
    def nsecsElapsed(*args, **kwargs):
        ...
    @staticmethod
    def restart(*args, **kwargs):
        ...
    @staticmethod
    def secsTo(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
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
class QEvent(PyQt6.sip.wrapper):
    class Type(enum.IntEnum):
        ActionAdded: typing.ClassVar[QEvent.Type]  # value = <Type.ActionAdded: 114>
        ActionChanged: typing.ClassVar[QEvent.Type]  # value = <Type.ActionChanged: 113>
        ActionRemoved: typing.ClassVar[QEvent.Type]  # value = <Type.ActionRemoved: 115>
        ActivationChange: typing.ClassVar[QEvent.Type]  # value = <Type.ActivationChange: 99>
        ApplicationActivate: typing.ClassVar[QEvent.Type]  # value = <Type.ApplicationActivate: 121>
        ApplicationDeactivate: typing.ClassVar[QEvent.Type]  # value = <Type.ApplicationDeactivate: 122>
        ApplicationFontChange: typing.ClassVar[QEvent.Type]  # value = <Type.ApplicationFontChange: 36>
        ApplicationLayoutDirectionChange: typing.ClassVar[QEvent.Type]  # value = <Type.ApplicationLayoutDirectionChange: 37>
        ApplicationPaletteChange: typing.ClassVar[QEvent.Type]  # value = <Type.ApplicationPaletteChange: 38>
        ApplicationStateChange: typing.ClassVar[QEvent.Type]  # value = <Type.ApplicationStateChange: 214>
        ApplicationWindowIconChange: typing.ClassVar[QEvent.Type]  # value = <Type.ApplicationWindowIconChange: 35>
        ChildAdded: typing.ClassVar[QEvent.Type]  # value = <Type.ChildAdded: 68>
        ChildPolished: typing.ClassVar[QEvent.Type]  # value = <Type.ChildPolished: 69>
        ChildRemoved: typing.ClassVar[QEvent.Type]  # value = <Type.ChildRemoved: 71>
        ChildWindowAdded: typing.ClassVar[QEvent.Type]  # value = <Type.ChildWindowAdded: 223>
        ChildWindowRemoved: typing.ClassVar[QEvent.Type]  # value = <Type.ChildWindowRemoved: 224>
        Clipboard: typing.ClassVar[QEvent.Type]  # value = <Type.Clipboard: 40>
        Close: typing.ClassVar[QEvent.Type]  # value = <Type.Close: 19>
        CloseSoftwareInputPanel: typing.ClassVar[QEvent.Type]  # value = <Type.CloseSoftwareInputPanel: 200>
        ContentsRectChange: typing.ClassVar[QEvent.Type]  # value = <Type.ContentsRectChange: 178>
        ContextMenu: typing.ClassVar[QEvent.Type]  # value = <Type.ContextMenu: 82>
        CursorChange: typing.ClassVar[QEvent.Type]  # value = <Type.CursorChange: 183>
        DeferredDelete: typing.ClassVar[QEvent.Type]  # value = <Type.DeferredDelete: 52>
        DevicePixelRatioChange: typing.ClassVar[QEvent.Type]  # value = <Type.DevicePixelRatioChange: 222>
        DragEnter: typing.ClassVar[QEvent.Type]  # value = <Type.DragEnter: 60>
        DragLeave: typing.ClassVar[QEvent.Type]  # value = <Type.DragLeave: 62>
        DragMove: typing.ClassVar[QEvent.Type]  # value = <Type.DragMove: 61>
        Drop: typing.ClassVar[QEvent.Type]  # value = <Type.Drop: 63>
        DynamicPropertyChange: typing.ClassVar[QEvent.Type]  # value = <Type.DynamicPropertyChange: 170>
        EnabledChange: typing.ClassVar[QEvent.Type]  # value = <Type.EnabledChange: 98>
        Enter: typing.ClassVar[QEvent.Type]  # value = <Type.Enter: 10>
        EnterEditFocus: typing.ClassVar[QEvent.Type]  # value = <Type.EnterEditFocus: 150>
        EnterWhatsThisMode: typing.ClassVar[QEvent.Type]  # value = <Type.EnterWhatsThisMode: 124>
        Expose: typing.ClassVar[QEvent.Type]  # value = <Type.Expose: 206>
        FileOpen: typing.ClassVar[QEvent.Type]  # value = <Type.FileOpen: 116>
        FocusAboutToChange: typing.ClassVar[QEvent.Type]  # value = <Type.FocusAboutToChange: 23>
        FocusIn: typing.ClassVar[QEvent.Type]  # value = <Type.FocusIn: 8>
        FocusOut: typing.ClassVar[QEvent.Type]  # value = <Type.FocusOut: 9>
        FontChange: typing.ClassVar[QEvent.Type]  # value = <Type.FontChange: 97>
        Gesture: typing.ClassVar[QEvent.Type]  # value = <Type.Gesture: 198>
        GestureOverride: typing.ClassVar[QEvent.Type]  # value = <Type.GestureOverride: 202>
        GrabKeyboard: typing.ClassVar[QEvent.Type]  # value = <Type.GrabKeyboard: 188>
        GrabMouse: typing.ClassVar[QEvent.Type]  # value = <Type.GrabMouse: 186>
        GraphicsSceneContextMenu: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneContextMenu: 159>
        GraphicsSceneDragEnter: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneDragEnter: 164>
        GraphicsSceneDragLeave: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneDragLeave: 166>
        GraphicsSceneDragMove: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneDragMove: 165>
        GraphicsSceneDrop: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneDrop: 167>
        GraphicsSceneHelp: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneHelp: 163>
        GraphicsSceneHoverEnter: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneHoverEnter: 160>
        GraphicsSceneHoverLeave: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneHoverLeave: 162>
        GraphicsSceneHoverMove: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneHoverMove: 161>
        GraphicsSceneLeave: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneLeave: 220>
        GraphicsSceneMouseDoubleClick: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneMouseDoubleClick: 158>
        GraphicsSceneMouseMove: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneMouseMove: 155>
        GraphicsSceneMousePress: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneMousePress: 156>
        GraphicsSceneMouseRelease: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneMouseRelease: 157>
        GraphicsSceneMove: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneMove: 182>
        GraphicsSceneResize: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneResize: 181>
        GraphicsSceneWheel: typing.ClassVar[QEvent.Type]  # value = <Type.GraphicsSceneWheel: 168>
        Hide: typing.ClassVar[QEvent.Type]  # value = <Type.Hide: 18>
        HideToParent: typing.ClassVar[QEvent.Type]  # value = <Type.HideToParent: 27>
        HoverEnter: typing.ClassVar[QEvent.Type]  # value = <Type.HoverEnter: 127>
        HoverLeave: typing.ClassVar[QEvent.Type]  # value = <Type.HoverLeave: 128>
        HoverMove: typing.ClassVar[QEvent.Type]  # value = <Type.HoverMove: 129>
        IconDrag: typing.ClassVar[QEvent.Type]  # value = <Type.IconDrag: 96>
        IconTextChange: typing.ClassVar[QEvent.Type]  # value = <Type.IconTextChange: 101>
        InputMethod: typing.ClassVar[QEvent.Type]  # value = <Type.InputMethod: 83>
        InputMethodQuery: typing.ClassVar[QEvent.Type]  # value = <Type.InputMethodQuery: 207>
        KeyPress: typing.ClassVar[QEvent.Type]  # value = <Type.KeyPress: 6>
        KeyRelease: typing.ClassVar[QEvent.Type]  # value = <Type.KeyRelease: 7>
        KeyboardLayoutChange: typing.ClassVar[QEvent.Type]  # value = <Type.KeyboardLayoutChange: 169>
        LanguageChange: typing.ClassVar[QEvent.Type]  # value = <Type.LanguageChange: 89>
        LayoutDirectionChange: typing.ClassVar[QEvent.Type]  # value = <Type.LayoutDirectionChange: 90>
        LayoutRequest: typing.ClassVar[QEvent.Type]  # value = <Type.LayoutRequest: 76>
        Leave: typing.ClassVar[QEvent.Type]  # value = <Type.Leave: 11>
        LeaveEditFocus: typing.ClassVar[QEvent.Type]  # value = <Type.LeaveEditFocus: 151>
        LeaveWhatsThisMode: typing.ClassVar[QEvent.Type]  # value = <Type.LeaveWhatsThisMode: 125>
        LocaleChange: typing.ClassVar[QEvent.Type]  # value = <Type.LocaleChange: 88>
        MacSizeChange: typing.ClassVar[QEvent.Type]  # value = <Type.MacSizeChange: 177>
        MaxUser: typing.ClassVar[QEvent.Type]  # value = <Type.MaxUser: 65535>
        MetaCall: typing.ClassVar[QEvent.Type]  # value = <Type.MetaCall: 43>
        ModifiedChange: typing.ClassVar[QEvent.Type]  # value = <Type.ModifiedChange: 102>
        MouseButtonDblClick: typing.ClassVar[QEvent.Type]  # value = <Type.MouseButtonDblClick: 4>
        MouseButtonPress: typing.ClassVar[QEvent.Type]  # value = <Type.MouseButtonPress: 2>
        MouseButtonRelease: typing.ClassVar[QEvent.Type]  # value = <Type.MouseButtonRelease: 3>
        MouseMove: typing.ClassVar[QEvent.Type]  # value = <Type.MouseMove: 5>
        MouseTrackingChange: typing.ClassVar[QEvent.Type]  # value = <Type.MouseTrackingChange: 109>
        Move: typing.ClassVar[QEvent.Type]  # value = <Type.Move: 13>
        NativeGesture: typing.ClassVar[QEvent.Type]  # value = <Type.NativeGesture: 197>
        NonClientAreaMouseButtonDblClick: typing.ClassVar[QEvent.Type]  # value = <Type.NonClientAreaMouseButtonDblClick: 176>
        NonClientAreaMouseButtonPress: typing.ClassVar[QEvent.Type]  # value = <Type.NonClientAreaMouseButtonPress: 174>
        NonClientAreaMouseButtonRelease: typing.ClassVar[QEvent.Type]  # value = <Type.NonClientAreaMouseButtonRelease: 175>
        NonClientAreaMouseMove: typing.ClassVar[QEvent.Type]  # value = <Type.NonClientAreaMouseMove: 173>
        None_: typing.ClassVar[QEvent.Type]  # value = <Type.None_: 0>
        OkRequest: typing.ClassVar[QEvent.Type]  # value = <Type.OkRequest: 94>
        OrientationChange: typing.ClassVar[QEvent.Type]  # value = <Type.OrientationChange: 208>
        Paint: typing.ClassVar[QEvent.Type]  # value = <Type.Paint: 12>
        PaletteChange: typing.ClassVar[QEvent.Type]  # value = <Type.PaletteChange: 39>
        ParentAboutToChange: typing.ClassVar[QEvent.Type]  # value = <Type.ParentAboutToChange: 131>
        ParentChange: typing.ClassVar[QEvent.Type]  # value = <Type.ParentChange: 21>
        ParentWindowAboutToChange: typing.ClassVar[QEvent.Type]  # value = <Type.ParentWindowAboutToChange: 225>
        ParentWindowChange: typing.ClassVar[QEvent.Type]  # value = <Type.ParentWindowChange: 226>
        PlatformPanel: typing.ClassVar[QEvent.Type]  # value = <Type.PlatformPanel: 212>
        PlatformSurface: typing.ClassVar[QEvent.Type]  # value = <Type.PlatformSurface: 217>
        Polish: typing.ClassVar[QEvent.Type]  # value = <Type.Polish: 75>
        PolishRequest: typing.ClassVar[QEvent.Type]  # value = <Type.PolishRequest: 74>
        QueryWhatsThis: typing.ClassVar[QEvent.Type]  # value = <Type.QueryWhatsThis: 123>
        Quit: typing.ClassVar[QEvent.Type]  # value = <Type.Quit: 20>
        ReadOnlyChange: typing.ClassVar[QEvent.Type]  # value = <Type.ReadOnlyChange: 106>
        RequestSoftwareInputPanel: typing.ClassVar[QEvent.Type]  # value = <Type.RequestSoftwareInputPanel: 199>
        Resize: typing.ClassVar[QEvent.Type]  # value = <Type.Resize: 14>
        Scroll: typing.ClassVar[QEvent.Type]  # value = <Type.Scroll: 205>
        ScrollPrepare: typing.ClassVar[QEvent.Type]  # value = <Type.ScrollPrepare: 204>
        Shortcut: typing.ClassVar[QEvent.Type]  # value = <Type.Shortcut: 117>
        ShortcutOverride: typing.ClassVar[QEvent.Type]  # value = <Type.ShortcutOverride: 51>
        Show: typing.ClassVar[QEvent.Type]  # value = <Type.Show: 17>
        ShowToParent: typing.ClassVar[QEvent.Type]  # value = <Type.ShowToParent: 26>
        SockAct: typing.ClassVar[QEvent.Type]  # value = <Type.SockAct: 50>
        StateMachineSignal: typing.ClassVar[QEvent.Type]  # value = <Type.StateMachineSignal: 192>
        StateMachineWrapped: typing.ClassVar[QEvent.Type]  # value = <Type.StateMachineWrapped: 193>
        StatusTip: typing.ClassVar[QEvent.Type]  # value = <Type.StatusTip: 112>
        StyleChange: typing.ClassVar[QEvent.Type]  # value = <Type.StyleChange: 100>
        TabletEnterProximity: typing.ClassVar[QEvent.Type]  # value = <Type.TabletEnterProximity: 171>
        TabletLeaveProximity: typing.ClassVar[QEvent.Type]  # value = <Type.TabletLeaveProximity: 172>
        TabletMove: typing.ClassVar[QEvent.Type]  # value = <Type.TabletMove: 87>
        TabletPress: typing.ClassVar[QEvent.Type]  # value = <Type.TabletPress: 92>
        TabletRelease: typing.ClassVar[QEvent.Type]  # value = <Type.TabletRelease: 93>
        TabletTrackingChange: typing.ClassVar[QEvent.Type]  # value = <Type.TabletTrackingChange: 219>
        ThreadChange: typing.ClassVar[QEvent.Type]  # value = <Type.ThreadChange: 22>
        Timer: typing.ClassVar[QEvent.Type]  # value = <Type.Timer: 1>
        ToolBarChange: typing.ClassVar[QEvent.Type]  # value = <Type.ToolBarChange: 120>
        ToolTip: typing.ClassVar[QEvent.Type]  # value = <Type.ToolTip: 110>
        ToolTipChange: typing.ClassVar[QEvent.Type]  # value = <Type.ToolTipChange: 184>
        TouchBegin: typing.ClassVar[QEvent.Type]  # value = <Type.TouchBegin: 194>
        TouchCancel: typing.ClassVar[QEvent.Type]  # value = <Type.TouchCancel: 209>
        TouchEnd: typing.ClassVar[QEvent.Type]  # value = <Type.TouchEnd: 196>
        TouchUpdate: typing.ClassVar[QEvent.Type]  # value = <Type.TouchUpdate: 195>
        UngrabKeyboard: typing.ClassVar[QEvent.Type]  # value = <Type.UngrabKeyboard: 189>
        UngrabMouse: typing.ClassVar[QEvent.Type]  # value = <Type.UngrabMouse: 187>
        UpdateLater: typing.ClassVar[QEvent.Type]  # value = <Type.UpdateLater: 78>
        UpdateRequest: typing.ClassVar[QEvent.Type]  # value = <Type.UpdateRequest: 77>
        User: typing.ClassVar[QEvent.Type]  # value = <Type.User: 1000>
        WhatsThis: typing.ClassVar[QEvent.Type]  # value = <Type.WhatsThis: 111>
        WhatsThisClicked: typing.ClassVar[QEvent.Type]  # value = <Type.WhatsThisClicked: 118>
        Wheel: typing.ClassVar[QEvent.Type]  # value = <Type.Wheel: 31>
        WinEventAct: typing.ClassVar[QEvent.Type]  # value = <Type.WinEventAct: 132>
        WinIdChange: typing.ClassVar[QEvent.Type]  # value = <Type.WinIdChange: 203>
        WindowActivate: typing.ClassVar[QEvent.Type]  # value = <Type.WindowActivate: 24>
        WindowBlocked: typing.ClassVar[QEvent.Type]  # value = <Type.WindowBlocked: 103>
        WindowDeactivate: typing.ClassVar[QEvent.Type]  # value = <Type.WindowDeactivate: 25>
        WindowIconChange: typing.ClassVar[QEvent.Type]  # value = <Type.WindowIconChange: 34>
        WindowStateChange: typing.ClassVar[QEvent.Type]  # value = <Type.WindowStateChange: 105>
        WindowTitleChange: typing.ClassVar[QEvent.Type]  # value = <Type.WindowTitleChange: 33>
        WindowUnblocked: typing.ClassVar[QEvent.Type]  # value = <Type.WindowUnblocked: 104>
        ZOrderChange: typing.ClassVar[QEvent.Type]  # value = <Type.ZOrderChange: 126>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    @staticmethod
    def accept(*args, **kwargs):
        ...
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def ignore(*args, **kwargs):
        ...
    @staticmethod
    def isAccepted(*args, **kwargs):
        ...
    @staticmethod
    def isInputEvent(*args, **kwargs):
        ...
    @staticmethod
    def isPointerEvent(*args, **kwargs):
        ...
    @staticmethod
    def isSinglePointEvent(*args, **kwargs):
        ...
    @staticmethod
    def registerEventType(*args, **kwargs):
        ...
    @staticmethod
    def setAccepted(*args, **kwargs):
        ...
    @staticmethod
    def spontaneous(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QEventLoop(QObject):
    class ProcessEventsFlag(enum.Flag):
        ExcludeSocketNotifiers: typing.ClassVar[QEventLoop.ProcessEventsFlag]  # value = <ProcessEventsFlag.ExcludeSocketNotifiers: 2>
        ExcludeUserInputEvents: typing.ClassVar[QEventLoop.ProcessEventsFlag]  # value = <ProcessEventsFlag.ExcludeUserInputEvents: 1>
        WaitForMoreEvents: typing.ClassVar[QEventLoop.ProcessEventsFlag]  # value = <ProcessEventsFlag.WaitForMoreEvents: 4>
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def exit(*args, **kwargs):
        ...
    @staticmethod
    def isRunning(*args, **kwargs):
        ...
    @staticmethod
    def processEvents(*args, **kwargs):
        ...
    @staticmethod
    def quit(*args, **kwargs):
        ...
    @staticmethod
    def wakeUp(*args, **kwargs):
        ...
class QEventLoopLocker(PyQt6.sip.simplewrapper):
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QFile(QFileDevice):
    @staticmethod
    def copy(*args, **kwargs):
        ...
    @staticmethod
    def decodeName(*args, **kwargs):
        ...
    @staticmethod
    def encodeName(*args, **kwargs):
        ...
    @staticmethod
    def exists(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def link(*args, **kwargs):
        ...
    @staticmethod
    def moveToTrash(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def permissions(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def rename(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setPermissions(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def symLinkTarget(*args, **kwargs):
        ...
class QFileDevice(QIODevice):
    class FileError(enum.Enum):
        AbortError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.AbortError: 6>
        CopyError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.CopyError: 14>
        FatalError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.FatalError: 3>
        NoError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.NoError: 0>
        OpenError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.OpenError: 5>
        PermissionsError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.PermissionsError: 13>
        PositionError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.PositionError: 11>
        ReadError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.ReadError: 1>
        RemoveError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.RemoveError: 9>
        RenameError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.RenameError: 10>
        ResizeError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.ResizeError: 12>
        ResourceError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.ResourceError: 4>
        TimeOutError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.TimeOutError: 7>
        UnspecifiedError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.UnspecifiedError: 8>
        WriteError: typing.ClassVar[QFileDevice.FileError]  # value = <FileError.WriteError: 2>
    class FileHandleFlag(enum.Flag):
        AutoCloseHandle: typing.ClassVar[QFileDevice.FileHandleFlag]  # value = <FileHandleFlag.AutoCloseHandle: 1>
    class FileTime(enum.Enum):
        FileAccessTime: typing.ClassVar[QFileDevice.FileTime]  # value = <FileTime.FileAccessTime: 0>
        FileBirthTime: typing.ClassVar[QFileDevice.FileTime]  # value = <FileTime.FileBirthTime: 1>
        FileMetadataChangeTime: typing.ClassVar[QFileDevice.FileTime]  # value = <FileTime.FileMetadataChangeTime: 2>
        FileModificationTime: typing.ClassVar[QFileDevice.FileTime]  # value = <FileTime.FileModificationTime: 3>
    class MemoryMapFlag(enum.Flag):
        MapPrivateOption: typing.ClassVar[QFileDevice.MemoryMapFlag]  # value = <MemoryMapFlag.MapPrivateOption: 1>
    class Permission(enum.Flag):
        ExeGroup: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ExeGroup: 16>
        ExeOther: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ExeOther: 1>
        ExeOwner: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ExeOwner: 4096>
        ExeUser: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ExeUser: 256>
        ReadGroup: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ReadGroup: 64>
        ReadOther: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ReadOther: 4>
        ReadOwner: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ReadOwner: 16384>
        ReadUser: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.ReadUser: 1024>
        WriteGroup: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.WriteGroup: 32>
        WriteOther: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.WriteOther: 2>
        WriteOwner: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.WriteOwner: 8192>
        WriteUser: typing.ClassVar[QFileDevice.Permission]  # value = <Permission.WriteUser: 512>
    @staticmethod
    def atEnd(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def fileTime(*args, **kwargs):
        ...
    @staticmethod
    def flush(*args, **kwargs):
        ...
    @staticmethod
    def handle(*args, **kwargs):
        ...
    @staticmethod
    def isSequential(*args, **kwargs):
        ...
    @staticmethod
    def map(*args, **kwargs):
        ...
    @staticmethod
    def permissions(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def readData(*args, **kwargs):
        ...
    @staticmethod
    def readLineData(*args, **kwargs):
        ...
    @staticmethod
    def resize(*args, **kwargs):
        ...
    @staticmethod
    def seek(*args, **kwargs):
        ...
    @staticmethod
    def setFileTime(*args, **kwargs):
        ...
    @staticmethod
    def setPermissions(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def unmap(*args, **kwargs):
        ...
    @staticmethod
    def unsetError(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QFileInfo(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __fspath__(*args, **kwargs):
        ...
    @staticmethod
    def absoluteDir(*args, **kwargs):
        ...
    @staticmethod
    def absoluteFilePath(*args, **kwargs):
        ...
    @staticmethod
    def absolutePath(*args, **kwargs):
        ...
    @staticmethod
    def baseName(*args, **kwargs):
        ...
    @staticmethod
    def birthTime(*args, **kwargs):
        ...
    @staticmethod
    def bundleName(*args, **kwargs):
        ...
    @staticmethod
    def caching(*args, **kwargs):
        ...
    @staticmethod
    def canonicalFilePath(*args, **kwargs):
        ...
    @staticmethod
    def canonicalPath(*args, **kwargs):
        ...
    @staticmethod
    def completeBaseName(*args, **kwargs):
        ...
    @staticmethod
    def completeSuffix(*args, **kwargs):
        ...
    @staticmethod
    def dir(*args, **kwargs):
        ...
    @staticmethod
    def exists(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def filePath(*args, **kwargs):
        ...
    @staticmethod
    def fileTime(*args, **kwargs):
        ...
    @staticmethod
    def group(*args, **kwargs):
        ...
    @staticmethod
    def groupId(*args, **kwargs):
        ...
    @staticmethod
    def isAbsolute(*args, **kwargs):
        ...
    @staticmethod
    def isAlias(*args, **kwargs):
        ...
    @staticmethod
    def isBundle(*args, **kwargs):
        ...
    @staticmethod
    def isDir(*args, **kwargs):
        ...
    @staticmethod
    def isExecutable(*args, **kwargs):
        ...
    @staticmethod
    def isFile(*args, **kwargs):
        ...
    @staticmethod
    def isHidden(*args, **kwargs):
        ...
    @staticmethod
    def isJunction(*args, **kwargs):
        ...
    @staticmethod
    def isNativePath(*args, **kwargs):
        ...
    @staticmethod
    def isReadable(*args, **kwargs):
        ...
    @staticmethod
    def isRelative(*args, **kwargs):
        ...
    @staticmethod
    def isRoot(*args, **kwargs):
        ...
    @staticmethod
    def isShortcut(*args, **kwargs):
        ...
    @staticmethod
    def isSymLink(*args, **kwargs):
        ...
    @staticmethod
    def isSymbolicLink(*args, **kwargs):
        ...
    @staticmethod
    def isWritable(*args, **kwargs):
        ...
    @staticmethod
    def junctionTarget(*args, **kwargs):
        ...
    @staticmethod
    def lastModified(*args, **kwargs):
        ...
    @staticmethod
    def lastRead(*args, **kwargs):
        ...
    @staticmethod
    def makeAbsolute(*args, **kwargs):
        ...
    @staticmethod
    def metadataChangeTime(*args, **kwargs):
        ...
    @staticmethod
    def owner(*args, **kwargs):
        ...
    @staticmethod
    def ownerId(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
    @staticmethod
    def permission(*args, **kwargs):
        ...
    @staticmethod
    def permissions(*args, **kwargs):
        ...
    @staticmethod
    def readSymLink(*args, **kwargs):
        ...
    @staticmethod
    def refresh(*args, **kwargs):
        ...
    @staticmethod
    def setCaching(*args, **kwargs):
        ...
    @staticmethod
    def setFile(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def stat(*args, **kwargs):
        ...
    @staticmethod
    def suffix(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def symLinkTarget(*args, **kwargs):
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
class QFileSelector(QObject):
    @staticmethod
    def allSelectors(*args, **kwargs):
        ...
    @staticmethod
    def extraSelectors(*args, **kwargs):
        ...
    @staticmethod
    def select(*args, **kwargs):
        ...
    @staticmethod
    def setExtraSelectors(*args, **kwargs):
        ...
class QFileSystemWatcher(QObject):
    @staticmethod
    def addPath(*args, **kwargs):
        ...
    @staticmethod
    def addPaths(*args, **kwargs):
        ...
    @staticmethod
    def directories(*args, **kwargs):
        ...
    @staticmethod
    def directoryChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def fileChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def files(*args, **kwargs):
        ...
    @staticmethod
    def removePath(*args, **kwargs):
        ...
    @staticmethod
    def removePaths(*args, **kwargs):
        ...
class QGenericArgument(PyQt6.sip.simplewrapper):
    pass
class QGenericReturnArgument(PyQt6.sip.simplewrapper):
    pass
class QIODevice(QObject, QIODeviceBase):
    @staticmethod
    def aboutToClose(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def bytesAvailable(*args, **kwargs):
        ...
    @staticmethod
    def bytesToWrite(*args, **kwargs):
        ...
    @staticmethod
    def bytesWritten(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def canReadLine(*args, **kwargs):
        ...
    @staticmethod
    def channelBytesWritten(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def channelReadyRead(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def commitTransaction(*args, **kwargs):
        ...
    @staticmethod
    def currentReadChannel(*args, **kwargs):
        ...
    @staticmethod
    def currentWriteChannel(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def getChar(*args, **kwargs):
        ...
    @staticmethod
    def isOpen(*args, **kwargs):
        ...
    @staticmethod
    def isReadable(*args, **kwargs):
        ...
    @staticmethod
    def isSequential(*args, **kwargs):
        ...
    @staticmethod
    def isTextModeEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isTransactionStarted(*args, **kwargs):
        ...
    @staticmethod
    def isWritable(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def openMode(*args, **kwargs):
        ...
    @staticmethod
    def peek(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def putChar(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def readAll(*args, **kwargs):
        ...
    @staticmethod
    def readChannelCount(*args, **kwargs):
        ...
    @staticmethod
    def readChannelFinished(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def readData(*args, **kwargs):
        ...
    @staticmethod
    def readLine(*args, **kwargs):
        ...
    @staticmethod
    def readLineData(*args, **kwargs):
        ...
    @staticmethod
    def readyRead(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def rollbackTransaction(*args, **kwargs):
        ...
    @staticmethod
    def seek(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentReadChannel(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentWriteChannel(*args, **kwargs):
        ...
    @staticmethod
    def setErrorString(*args, **kwargs):
        ...
    @staticmethod
    def setOpenMode(*args, **kwargs):
        ...
    @staticmethod
    def setTextModeEnabled(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def skip(*args, **kwargs):
        ...
    @staticmethod
    def skipData(*args, **kwargs):
        ...
    @staticmethod
    def startTransaction(*args, **kwargs):
        ...
    @staticmethod
    def ungetChar(*args, **kwargs):
        ...
    @staticmethod
    def waitForBytesWritten(*args, **kwargs):
        ...
    @staticmethod
    def waitForReadyRead(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
    @staticmethod
    def writeChannelCount(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QIODeviceBase(PyQt6.sip.simplewrapper):
    class OpenModeFlag(enum.Flag):
        Append: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.Append: 4>
        ExistingOnly: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.ExistingOnly: 128>
        NewOnly: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.NewOnly: 64>
        ReadOnly: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.ReadOnly: 1>
        Text: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.Text: 16>
        Truncate: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.Truncate: 8>
        Unbuffered: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.Unbuffered: 32>
        WriteOnly: typing.ClassVar[QIODeviceBase.OpenModeFlag]  # value = <OpenModeFlag.WriteOnly: 2>
class QIdentityProxyModel(QAbstractProxyModel):
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insertColumns(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def mapFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapSelectionFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapSelectionToSource(*args, **kwargs):
        ...
    @staticmethod
    def mapToSource(*args, **kwargs):
        ...
    @staticmethod
    def match(*args, **kwargs):
        ...
    @staticmethod
    def moveColumns(*args, **kwargs):
        ...
    @staticmethod
    def moveRows(*args, **kwargs):
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
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setSourceModel(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
class QItemSelection(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def append(*args, **kwargs):
        ...
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
    def first(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def indexes(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
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
    def merge(*args, **kwargs):
        ...
    @staticmethod
    def move(*args, **kwargs):
        ...
    @staticmethod
    def prepend(*args, **kwargs):
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
    def select(*args, **kwargs):
        ...
    @staticmethod
    def split(*args, **kwargs):
        ...
    @staticmethod
    def takeAt(*args, **kwargs):
        ...
    @staticmethod
    def takeFirst(*args, **kwargs):
        ...
    @staticmethod
    def takeLast(*args, **kwargs):
        ...
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
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QItemSelectionModel(QObject):
    class SelectionFlag(enum.Flag):
        Clear: typing.ClassVar[QItemSelectionModel.SelectionFlag]  # value = <SelectionFlag.Clear: 1>
        Columns: typing.ClassVar[QItemSelectionModel.SelectionFlag]  # value = <SelectionFlag.Columns: 64>
        Current: typing.ClassVar[QItemSelectionModel.SelectionFlag]  # value = <SelectionFlag.Current: 16>
        Deselect: typing.ClassVar[QItemSelectionModel.SelectionFlag]  # value = <SelectionFlag.Deselect: 4>
        Rows: typing.ClassVar[QItemSelectionModel.SelectionFlag]  # value = <SelectionFlag.Rows: 32>
        Select: typing.ClassVar[QItemSelectionModel.SelectionFlag]  # value = <SelectionFlag.Select: 2>
        Toggle: typing.ClassVar[QItemSelectionModel.SelectionFlag]  # value = <SelectionFlag.Toggle: 8>
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def clearSelection(*args, **kwargs):
        ...
    @staticmethod
    def columnIntersectsSelection(*args, **kwargs):
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
    def currentColumnChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def emitSelectionChanged(*args, **kwargs):
        ...
    @staticmethod
    def hasSelection(*args, **kwargs):
        ...
    @staticmethod
    def isColumnSelected(*args, **kwargs):
        ...
    @staticmethod
    def isRowSelected(*args, **kwargs):
        ...
    @staticmethod
    def isSelected(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def modelChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def rowIntersectsSelection(*args, **kwargs):
        ...
    @staticmethod
    def select(*args, **kwargs):
        ...
    @staticmethod
    def selectedColumns(*args, **kwargs):
        ...
    @staticmethod
    def selectedIndexes(*args, **kwargs):
        ...
    @staticmethod
    def selectedRows(*args, **kwargs):
        ...
    @staticmethod
    def selection(*args, **kwargs):
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
    def setCurrentIndex(*args, **kwargs):
        ...
    @staticmethod
    def setModel(*args, **kwargs):
        ...
class QItemSelectionRange(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def bottom(*args, **kwargs):
        ...
    @staticmethod
    def bottomRight(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def indexes(*args, **kwargs):
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
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def left(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def right(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def top(*args, **kwargs):
        ...
    @staticmethod
    def topLeft(*args, **kwargs):
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
class QJsonDocument(PyQt6.sip.simplewrapper):
    class JsonFormat(enum.Enum):
        Compact: typing.ClassVar[QJsonDocument.JsonFormat]  # value = <JsonFormat.Compact: 1>
        Indented: typing.ClassVar[QJsonDocument.JsonFormat]  # value = <JsonFormat.Indented: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def array(*args, **kwargs):
        ...
    @staticmethod
    def fromJson(*args, **kwargs):
        ...
    @staticmethod
    def fromVariant(*args, **kwargs):
        ...
    @staticmethod
    def isArray(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isObject(*args, **kwargs):
        ...
    @staticmethod
    def object(*args, **kwargs):
        ...
    @staticmethod
    def setArray(*args, **kwargs):
        ...
    @staticmethod
    def setObject(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toJson(*args, **kwargs):
        ...
    @staticmethod
    def toVariant(*args, **kwargs):
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
class QJsonParseError(PyQt6.sip.simplewrapper):
    class ParseError(enum.Enum):
        DeepNesting: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.DeepNesting: 12>
        DocumentTooLarge: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.DocumentTooLarge: 13>
        GarbageAtEnd: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.GarbageAtEnd: 14>
        IllegalEscapeSequence: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.IllegalEscapeSequence: 8>
        IllegalNumber: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.IllegalNumber: 7>
        IllegalUTF8String: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.IllegalUTF8String: 9>
        IllegalValue: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.IllegalValue: 5>
        MissingNameSeparator: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.MissingNameSeparator: 2>
        MissingObject: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.MissingObject: 11>
        MissingValueSeparator: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.MissingValueSeparator: 4>
        NoError: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.NoError: 0>
        TerminationByNumber: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.TerminationByNumber: 6>
        UnterminatedArray: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.UnterminatedArray: 3>
        UnterminatedObject: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.UnterminatedObject: 1>
        UnterminatedString: typing.ClassVar[QJsonParseError.ParseError]  # value = <ParseError.UnterminatedString: 10>
    @staticmethod
    def errorString(*args, **kwargs):
        ...
class QJsonValue(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        Array: typing.ClassVar[QJsonValue.Type]  # value = <Type.Array: 4>
        Bool: typing.ClassVar[QJsonValue.Type]  # value = <Type.Bool: 1>
        Double: typing.ClassVar[QJsonValue.Type]  # value = <Type.Double: 2>
        Null: typing.ClassVar[QJsonValue.Type]  # value = <Type.Null: 0>
        Object: typing.ClassVar[QJsonValue.Type]  # value = <Type.Object: 5>
        String: typing.ClassVar[QJsonValue.Type]  # value = <Type.String: 3>
        Undefined: typing.ClassVar[QJsonValue.Type]  # value = <Type.Undefined: 128>
    @staticmethod
    def fromVariant(*args, **kwargs):
        ...
    @staticmethod
    def isArray(*args, **kwargs):
        ...
    @staticmethod
    def isBool(*args, **kwargs):
        ...
    @staticmethod
    def isDouble(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isObject(*args, **kwargs):
        ...
    @staticmethod
    def isString(*args, **kwargs):
        ...
    @staticmethod
    def isUndefined(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toArray(*args, **kwargs):
        ...
    @staticmethod
    def toBool(*args, **kwargs):
        ...
    @staticmethod
    def toDouble(*args, **kwargs):
        ...
    @staticmethod
    def toInt(*args, **kwargs):
        ...
    @staticmethod
    def toInteger(*args, **kwargs):
        ...
    @staticmethod
    def toObject(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    @staticmethod
    def toVariant(*args, **kwargs):
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
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
class QKeyCombination(PyQt6.sip.simplewrapper):
    @staticmethod
    def fromCombined(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def keyboardModifiers(*args, **kwargs):
        ...
    @staticmethod
    def toCombined(*args, **kwargs):
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
class QLibrary(QObject):
    class LoadHint(enum.Flag):
        DeepBindHint: typing.ClassVar[QLibrary.LoadHint]  # value = <LoadHint.DeepBindHint: 16>
        ExportExternalSymbolsHint: typing.ClassVar[QLibrary.LoadHint]  # value = <LoadHint.ExportExternalSymbolsHint: 2>
        LoadArchiveMemberHint: typing.ClassVar[QLibrary.LoadHint]  # value = <LoadHint.LoadArchiveMemberHint: 4>
        PreventUnloadHint: typing.ClassVar[QLibrary.LoadHint]  # value = <LoadHint.PreventUnloadHint: 8>
        ResolveAllSymbolsHint: typing.ClassVar[QLibrary.LoadHint]  # value = <LoadHint.ResolveAllSymbolsHint: 1>
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def isLibrary(*args, **kwargs):
        ...
    @staticmethod
    def isLoaded(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def loadHints(*args, **kwargs):
        ...
    @staticmethod
    def resolve(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setFileNameAndVersion(*args, **kwargs):
        ...
    @staticmethod
    def setLoadHints(*args, **kwargs):
        ...
    @staticmethod
    def unload(*args, **kwargs):
        ...
class QLibraryInfo(PyQt6.sip.simplewrapper):
    class LibraryPath(enum.Enum):
        ArchDataPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.ArchDataPath: 8>
        BinariesPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.BinariesPath: 5>
        DataPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.DataPath: 9>
        DocumentationPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.DocumentationPath: 1>
        ExamplesPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.ExamplesPath: 11>
        HeadersPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.HeadersPath: 2>
        LibrariesPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.LibrariesPath: 3>
        LibraryExecutablesPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.LibraryExecutablesPath: 4>
        PluginsPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.PluginsPath: 6>
        PrefixPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.PrefixPath: 0>
        Qml2ImportsPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.Qml2ImportsPath: 7>
        SettingsPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.SettingsPath: 100>
        TestsPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.TestsPath: 12>
        TranslationsPath: typing.ClassVar[QLibraryInfo.LibraryPath]  # value = <LibraryPath.TranslationsPath: 10>
    @staticmethod
    def isDebugBuild(*args, **kwargs):
        ...
    @staticmethod
    def isSharedBuild(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
    @staticmethod
    def version(*args, **kwargs):
        ...
class QLine(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def center(*args, **kwargs):
        ...
    @staticmethod
    def dx(*args, **kwargs):
        ...
    @staticmethod
    def dy(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def p1(*args, **kwargs):
        ...
    @staticmethod
    def p2(*args, **kwargs):
        ...
    @staticmethod
    def setLine(*args, **kwargs):
        ...
    @staticmethod
    def setP1(*args, **kwargs):
        ...
    @staticmethod
    def setP2(*args, **kwargs):
        ...
    @staticmethod
    def setPoints(*args, **kwargs):
        ...
    @staticmethod
    def toLineF(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def x1(*args, **kwargs):
        ...
    @staticmethod
    def x2(*args, **kwargs):
        ...
    @staticmethod
    def y1(*args, **kwargs):
        ...
    @staticmethod
    def y2(*args, **kwargs):
        ...
    def __bool__(self):
        """
        True if self else False
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
class QLineF(PyQt6.sip.simplewrapper):
    class IntersectionType(enum.Enum):
        BoundedIntersection: typing.ClassVar[QLineF.IntersectionType]  # value = <IntersectionType.BoundedIntersection: 1>
        NoIntersection: typing.ClassVar[QLineF.IntersectionType]  # value = <IntersectionType.NoIntersection: 0>
        UnboundedIntersection: typing.ClassVar[QLineF.IntersectionType]  # value = <IntersectionType.UnboundedIntersection: 2>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def angle(*args, **kwargs):
        ...
    @staticmethod
    def angleTo(*args, **kwargs):
        ...
    @staticmethod
    def center(*args, **kwargs):
        ...
    @staticmethod
    def dx(*args, **kwargs):
        ...
    @staticmethod
    def dy(*args, **kwargs):
        ...
    @staticmethod
    def fromPolar(*args, **kwargs):
        ...
    @staticmethod
    def intersects(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def normalVector(*args, **kwargs):
        ...
    @staticmethod
    def p1(*args, **kwargs):
        ...
    @staticmethod
    def p2(*args, **kwargs):
        ...
    @staticmethod
    def pointAt(*args, **kwargs):
        ...
    @staticmethod
    def setAngle(*args, **kwargs):
        ...
    @staticmethod
    def setLength(*args, **kwargs):
        ...
    @staticmethod
    def setLine(*args, **kwargs):
        ...
    @staticmethod
    def setP1(*args, **kwargs):
        ...
    @staticmethod
    def setP2(*args, **kwargs):
        ...
    @staticmethod
    def setPoints(*args, **kwargs):
        ...
    @staticmethod
    def toLine(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def unitVector(*args, **kwargs):
        ...
    @staticmethod
    def x1(*args, **kwargs):
        ...
    @staticmethod
    def x2(*args, **kwargs):
        ...
    @staticmethod
    def y1(*args, **kwargs):
        ...
    @staticmethod
    def y2(*args, **kwargs):
        ...
    def __bool__(self):
        """
        True if self else False
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
class QLocale(PyQt6.sip.simplewrapper):
    class Country(enum.Enum):
        Afghanistan: typing.ClassVar[QLocale.Country]  # value = <Country.Afghanistan: 1>
        AlandIslands: typing.ClassVar[QLocale.Country]  # value = <Country.AlandIslands: 2>
        Albania: typing.ClassVar[QLocale.Country]  # value = <Country.Albania: 3>
        Algeria: typing.ClassVar[QLocale.Country]  # value = <Country.Algeria: 4>
        AmericanSamoa: typing.ClassVar[QLocale.Country]  # value = <Country.AmericanSamoa: 5>
        Andorra: typing.ClassVar[QLocale.Country]  # value = <Country.Andorra: 6>
        Angola: typing.ClassVar[QLocale.Country]  # value = <Country.Angola: 7>
        Anguilla: typing.ClassVar[QLocale.Country]  # value = <Country.Anguilla: 8>
        Antarctica: typing.ClassVar[QLocale.Country]  # value = <Country.Antarctica: 9>
        AntiguaAndBarbuda: typing.ClassVar[QLocale.Country]  # value = <Country.AntiguaAndBarbuda: 10>
        AnyCountry: typing.ClassVar[QLocale.Country]  # value = <Country.AnyCountry: 0>
        Argentina: typing.ClassVar[QLocale.Country]  # value = <Country.Argentina: 11>
        Armenia: typing.ClassVar[QLocale.Country]  # value = <Country.Armenia: 12>
        Aruba: typing.ClassVar[QLocale.Country]  # value = <Country.Aruba: 13>
        AscensionIsland: typing.ClassVar[QLocale.Country]  # value = <Country.AscensionIsland: 14>
        Australia: typing.ClassVar[QLocale.Country]  # value = <Country.Australia: 15>
        Austria: typing.ClassVar[QLocale.Country]  # value = <Country.Austria: 16>
        Azerbaijan: typing.ClassVar[QLocale.Country]  # value = <Country.Azerbaijan: 17>
        Bahamas: typing.ClassVar[QLocale.Country]  # value = <Country.Bahamas: 18>
        Bahrain: typing.ClassVar[QLocale.Country]  # value = <Country.Bahrain: 19>
        Bangladesh: typing.ClassVar[QLocale.Country]  # value = <Country.Bangladesh: 20>
        Barbados: typing.ClassVar[QLocale.Country]  # value = <Country.Barbados: 21>
        Belarus: typing.ClassVar[QLocale.Country]  # value = <Country.Belarus: 22>
        Belgium: typing.ClassVar[QLocale.Country]  # value = <Country.Belgium: 23>
        Belize: typing.ClassVar[QLocale.Country]  # value = <Country.Belize: 24>
        Benin: typing.ClassVar[QLocale.Country]  # value = <Country.Benin: 25>
        Bermuda: typing.ClassVar[QLocale.Country]  # value = <Country.Bermuda: 26>
        Bhutan: typing.ClassVar[QLocale.Country]  # value = <Country.Bhutan: 27>
        Bolivia: typing.ClassVar[QLocale.Country]  # value = <Country.Bolivia: 28>
        Bonaire: typing.ClassVar[QLocale.Country]  # value = <Country.Bonaire: 44>
        BosniaAndHerzegowina: typing.ClassVar[QLocale.Country]  # value = <Country.BosniaAndHerzegowina: 29>
        Botswana: typing.ClassVar[QLocale.Country]  # value = <Country.Botswana: 30>
        BouvetIsland: typing.ClassVar[QLocale.Country]  # value = <Country.BouvetIsland: 31>
        Brazil: typing.ClassVar[QLocale.Country]  # value = <Country.Brazil: 32>
        BritishIndianOceanTerritory: typing.ClassVar[QLocale.Country]  # value = <Country.BritishIndianOceanTerritory: 33>
        BritishVirginIslands: typing.ClassVar[QLocale.Country]  # value = <Country.BritishVirginIslands: 34>
        Brunei: typing.ClassVar[QLocale.Country]  # value = <Country.Brunei: 35>
        Bulgaria: typing.ClassVar[QLocale.Country]  # value = <Country.Bulgaria: 36>
        BurkinaFaso: typing.ClassVar[QLocale.Country]  # value = <Country.BurkinaFaso: 37>
        Burundi: typing.ClassVar[QLocale.Country]  # value = <Country.Burundi: 38>
        Cambodia: typing.ClassVar[QLocale.Country]  # value = <Country.Cambodia: 39>
        Cameroon: typing.ClassVar[QLocale.Country]  # value = <Country.Cameroon: 40>
        Canada: typing.ClassVar[QLocale.Country]  # value = <Country.Canada: 41>
        CanaryIslands: typing.ClassVar[QLocale.Country]  # value = <Country.CanaryIslands: 42>
        CapeVerde: typing.ClassVar[QLocale.Country]  # value = <Country.CapeVerde: 43>
        CaymanIslands: typing.ClassVar[QLocale.Country]  # value = <Country.CaymanIslands: 45>
        CentralAfricanRepublic: typing.ClassVar[QLocale.Country]  # value = <Country.CentralAfricanRepublic: 46>
        CeutaAndMelilla: typing.ClassVar[QLocale.Country]  # value = <Country.CeutaAndMelilla: 47>
        Chad: typing.ClassVar[QLocale.Country]  # value = <Country.Chad: 48>
        Chile: typing.ClassVar[QLocale.Country]  # value = <Country.Chile: 49>
        China: typing.ClassVar[QLocale.Country]  # value = <Country.China: 50>
        ChristmasIsland: typing.ClassVar[QLocale.Country]  # value = <Country.ChristmasIsland: 51>
        ClippertonIsland: typing.ClassVar[QLocale.Country]  # value = <Country.ClippertonIsland: 52>
        CocosIslands: typing.ClassVar[QLocale.Country]  # value = <Country.CocosIslands: 53>
        Colombia: typing.ClassVar[QLocale.Country]  # value = <Country.Colombia: 54>
        Comoros: typing.ClassVar[QLocale.Country]  # value = <Country.Comoros: 55>
        CookIslands: typing.ClassVar[QLocale.Country]  # value = <Country.CookIslands: 58>
        CostaRica: typing.ClassVar[QLocale.Country]  # value = <Country.CostaRica: 59>
        Croatia: typing.ClassVar[QLocale.Country]  # value = <Country.Croatia: 60>
        Cuba: typing.ClassVar[QLocale.Country]  # value = <Country.Cuba: 61>
        CuraSao: typing.ClassVar[QLocale.Country]  # value = <Country.CuraSao: 62>
        Cyprus: typing.ClassVar[QLocale.Country]  # value = <Country.Cyprus: 63>
        CzechRepublic: typing.ClassVar[QLocale.Country]  # value = <Country.CzechRepublic: 64>
        DemocraticRepublicOfCongo: typing.ClassVar[QLocale.Country]  # value = <Country.DemocraticRepublicOfCongo: 57>
        DemocraticRepublicOfKorea: typing.ClassVar[QLocale.Country]  # value = <Country.DemocraticRepublicOfKorea: 174>
        Denmark: typing.ClassVar[QLocale.Country]  # value = <Country.Denmark: 65>
        DiegoGarcia: typing.ClassVar[QLocale.Country]  # value = <Country.DiegoGarcia: 66>
        Djibouti: typing.ClassVar[QLocale.Country]  # value = <Country.Djibouti: 67>
        Dominica: typing.ClassVar[QLocale.Country]  # value = <Country.Dominica: 68>
        DominicanRepublic: typing.ClassVar[QLocale.Country]  # value = <Country.DominicanRepublic: 69>
        EastTimor: typing.ClassVar[QLocale.Country]  # value = <Country.EastTimor: 232>
        Ecuador: typing.ClassVar[QLocale.Country]  # value = <Country.Ecuador: 70>
        Egypt: typing.ClassVar[QLocale.Country]  # value = <Country.Egypt: 71>
        ElSalvador: typing.ClassVar[QLocale.Country]  # value = <Country.ElSalvador: 72>
        EquatorialGuinea: typing.ClassVar[QLocale.Country]  # value = <Country.EquatorialGuinea: 73>
        Eritrea: typing.ClassVar[QLocale.Country]  # value = <Country.Eritrea: 74>
        Estonia: typing.ClassVar[QLocale.Country]  # value = <Country.Estonia: 75>
        Ethiopia: typing.ClassVar[QLocale.Country]  # value = <Country.Ethiopia: 77>
        Europe: typing.ClassVar[QLocale.Country]  # value = <Country.Europe: 78>
        EuropeanUnion: typing.ClassVar[QLocale.Country]  # value = <Country.EuropeanUnion: 79>
        FalklandIslands: typing.ClassVar[QLocale.Country]  # value = <Country.FalklandIslands: 80>
        FaroeIslands: typing.ClassVar[QLocale.Country]  # value = <Country.FaroeIslands: 81>
        Fiji: typing.ClassVar[QLocale.Country]  # value = <Country.Fiji: 82>
        Finland: typing.ClassVar[QLocale.Country]  # value = <Country.Finland: 83>
        France: typing.ClassVar[QLocale.Country]  # value = <Country.France: 84>
        FrenchGuiana: typing.ClassVar[QLocale.Country]  # value = <Country.FrenchGuiana: 85>
        FrenchPolynesia: typing.ClassVar[QLocale.Country]  # value = <Country.FrenchPolynesia: 86>
        FrenchSouthernTerritories: typing.ClassVar[QLocale.Country]  # value = <Country.FrenchSouthernTerritories: 87>
        Gabon: typing.ClassVar[QLocale.Country]  # value = <Country.Gabon: 88>
        Gambia: typing.ClassVar[QLocale.Country]  # value = <Country.Gambia: 89>
        Georgia: typing.ClassVar[QLocale.Country]  # value = <Country.Georgia: 90>
        Germany: typing.ClassVar[QLocale.Country]  # value = <Country.Germany: 91>
        Ghana: typing.ClassVar[QLocale.Country]  # value = <Country.Ghana: 92>
        Gibraltar: typing.ClassVar[QLocale.Country]  # value = <Country.Gibraltar: 93>
        Greece: typing.ClassVar[QLocale.Country]  # value = <Country.Greece: 94>
        Greenland: typing.ClassVar[QLocale.Country]  # value = <Country.Greenland: 95>
        Grenada: typing.ClassVar[QLocale.Country]  # value = <Country.Grenada: 96>
        Guadeloupe: typing.ClassVar[QLocale.Country]  # value = <Country.Guadeloupe: 97>
        Guam: typing.ClassVar[QLocale.Country]  # value = <Country.Guam: 98>
        Guatemala: typing.ClassVar[QLocale.Country]  # value = <Country.Guatemala: 99>
        Guernsey: typing.ClassVar[QLocale.Country]  # value = <Country.Guernsey: 100>
        Guinea: typing.ClassVar[QLocale.Country]  # value = <Country.Guinea: 102>
        GuineaBissau: typing.ClassVar[QLocale.Country]  # value = <Country.GuineaBissau: 101>
        Guyana: typing.ClassVar[QLocale.Country]  # value = <Country.Guyana: 103>
        Haiti: typing.ClassVar[QLocale.Country]  # value = <Country.Haiti: 104>
        HeardAndMcDonaldIslands: typing.ClassVar[QLocale.Country]  # value = <Country.HeardAndMcDonaldIslands: 105>
        Honduras: typing.ClassVar[QLocale.Country]  # value = <Country.Honduras: 106>
        HongKong: typing.ClassVar[QLocale.Country]  # value = <Country.HongKong: 107>
        Hungary: typing.ClassVar[QLocale.Country]  # value = <Country.Hungary: 108>
        Iceland: typing.ClassVar[QLocale.Country]  # value = <Country.Iceland: 109>
        India: typing.ClassVar[QLocale.Country]  # value = <Country.India: 110>
        Indonesia: typing.ClassVar[QLocale.Country]  # value = <Country.Indonesia: 111>
        Iran: typing.ClassVar[QLocale.Country]  # value = <Country.Iran: 112>
        Iraq: typing.ClassVar[QLocale.Country]  # value = <Country.Iraq: 113>
        Ireland: typing.ClassVar[QLocale.Country]  # value = <Country.Ireland: 114>
        IsleOfMan: typing.ClassVar[QLocale.Country]  # value = <Country.IsleOfMan: 115>
        Israel: typing.ClassVar[QLocale.Country]  # value = <Country.Israel: 116>
        Italy: typing.ClassVar[QLocale.Country]  # value = <Country.Italy: 117>
        IvoryCoast: typing.ClassVar[QLocale.Country]  # value = <Country.IvoryCoast: 118>
        Jamaica: typing.ClassVar[QLocale.Country]  # value = <Country.Jamaica: 119>
        Japan: typing.ClassVar[QLocale.Country]  # value = <Country.Japan: 120>
        Jersey: typing.ClassVar[QLocale.Country]  # value = <Country.Jersey: 121>
        Jordan: typing.ClassVar[QLocale.Country]  # value = <Country.Jordan: 122>
        Kazakhstan: typing.ClassVar[QLocale.Country]  # value = <Country.Kazakhstan: 123>
        Kenya: typing.ClassVar[QLocale.Country]  # value = <Country.Kenya: 124>
        Kiribati: typing.ClassVar[QLocale.Country]  # value = <Country.Kiribati: 125>
        Kosovo: typing.ClassVar[QLocale.Country]  # value = <Country.Kosovo: 126>
        Kuwait: typing.ClassVar[QLocale.Country]  # value = <Country.Kuwait: 127>
        Kyrgyzstan: typing.ClassVar[QLocale.Country]  # value = <Country.Kyrgyzstan: 128>
        Laos: typing.ClassVar[QLocale.Country]  # value = <Country.Laos: 129>
        LatinAmericaAndTheCaribbean: typing.ClassVar[QLocale.Country]  # value = <Country.LatinAmericaAndTheCaribbean: 130>
        Latvia: typing.ClassVar[QLocale.Country]  # value = <Country.Latvia: 131>
        Lebanon: typing.ClassVar[QLocale.Country]  # value = <Country.Lebanon: 132>
        Lesotho: typing.ClassVar[QLocale.Country]  # value = <Country.Lesotho: 133>
        Liberia: typing.ClassVar[QLocale.Country]  # value = <Country.Liberia: 134>
        Libya: typing.ClassVar[QLocale.Country]  # value = <Country.Libya: 135>
        Liechtenstein: typing.ClassVar[QLocale.Country]  # value = <Country.Liechtenstein: 136>
        Lithuania: typing.ClassVar[QLocale.Country]  # value = <Country.Lithuania: 137>
        Luxembourg: typing.ClassVar[QLocale.Country]  # value = <Country.Luxembourg: 138>
        Macau: typing.ClassVar[QLocale.Country]  # value = <Country.Macau: 139>
        Macedonia: typing.ClassVar[QLocale.Country]  # value = <Country.Macedonia: 140>
        Madagascar: typing.ClassVar[QLocale.Country]  # value = <Country.Madagascar: 141>
        Malawi: typing.ClassVar[QLocale.Country]  # value = <Country.Malawi: 142>
        Malaysia: typing.ClassVar[QLocale.Country]  # value = <Country.Malaysia: 143>
        Maldives: typing.ClassVar[QLocale.Country]  # value = <Country.Maldives: 144>
        Mali: typing.ClassVar[QLocale.Country]  # value = <Country.Mali: 145>
        Malta: typing.ClassVar[QLocale.Country]  # value = <Country.Malta: 146>
        MarshallIslands: typing.ClassVar[QLocale.Country]  # value = <Country.MarshallIslands: 147>
        Martinique: typing.ClassVar[QLocale.Country]  # value = <Country.Martinique: 148>
        Mauritania: typing.ClassVar[QLocale.Country]  # value = <Country.Mauritania: 149>
        Mauritius: typing.ClassVar[QLocale.Country]  # value = <Country.Mauritius: 150>
        Mayotte: typing.ClassVar[QLocale.Country]  # value = <Country.Mayotte: 151>
        Mexico: typing.ClassVar[QLocale.Country]  # value = <Country.Mexico: 152>
        Micronesia: typing.ClassVar[QLocale.Country]  # value = <Country.Micronesia: 153>
        Moldova: typing.ClassVar[QLocale.Country]  # value = <Country.Moldova: 154>
        Monaco: typing.ClassVar[QLocale.Country]  # value = <Country.Monaco: 155>
        Mongolia: typing.ClassVar[QLocale.Country]  # value = <Country.Mongolia: 156>
        Montenegro: typing.ClassVar[QLocale.Country]  # value = <Country.Montenegro: 157>
        Montserrat: typing.ClassVar[QLocale.Country]  # value = <Country.Montserrat: 158>
        Morocco: typing.ClassVar[QLocale.Country]  # value = <Country.Morocco: 159>
        Mozambique: typing.ClassVar[QLocale.Country]  # value = <Country.Mozambique: 160>
        Myanmar: typing.ClassVar[QLocale.Country]  # value = <Country.Myanmar: 161>
        Namibia: typing.ClassVar[QLocale.Country]  # value = <Country.Namibia: 162>
        NauruCountry: typing.ClassVar[QLocale.Country]  # value = <Country.NauruCountry: 163>
        Nepal: typing.ClassVar[QLocale.Country]  # value = <Country.Nepal: 164>
        Netherlands: typing.ClassVar[QLocale.Country]  # value = <Country.Netherlands: 165>
        NewCaledonia: typing.ClassVar[QLocale.Country]  # value = <Country.NewCaledonia: 166>
        NewZealand: typing.ClassVar[QLocale.Country]  # value = <Country.NewZealand: 167>
        Nicaragua: typing.ClassVar[QLocale.Country]  # value = <Country.Nicaragua: 168>
        Niger: typing.ClassVar[QLocale.Country]  # value = <Country.Niger: 170>
        Nigeria: typing.ClassVar[QLocale.Country]  # value = <Country.Nigeria: 169>
        Niue: typing.ClassVar[QLocale.Country]  # value = <Country.Niue: 171>
        NorfolkIsland: typing.ClassVar[QLocale.Country]  # value = <Country.NorfolkIsland: 172>
        NorthernMarianaIslands: typing.ClassVar[QLocale.Country]  # value = <Country.NorthernMarianaIslands: 173>
        Norway: typing.ClassVar[QLocale.Country]  # value = <Country.Norway: 175>
        Oman: typing.ClassVar[QLocale.Country]  # value = <Country.Oman: 176>
        OutlyingOceania: typing.ClassVar[QLocale.Country]  # value = <Country.OutlyingOceania: 177>
        Pakistan: typing.ClassVar[QLocale.Country]  # value = <Country.Pakistan: 178>
        Palau: typing.ClassVar[QLocale.Country]  # value = <Country.Palau: 179>
        PalestinianTerritories: typing.ClassVar[QLocale.Country]  # value = <Country.PalestinianTerritories: 180>
        Panama: typing.ClassVar[QLocale.Country]  # value = <Country.Panama: 181>
        PapuaNewGuinea: typing.ClassVar[QLocale.Country]  # value = <Country.PapuaNewGuinea: 182>
        Paraguay: typing.ClassVar[QLocale.Country]  # value = <Country.Paraguay: 183>
        PeoplesRepublicOfCongo: typing.ClassVar[QLocale.Country]  # value = <Country.PeoplesRepublicOfCongo: 56>
        Peru: typing.ClassVar[QLocale.Country]  # value = <Country.Peru: 184>
        Philippines: typing.ClassVar[QLocale.Country]  # value = <Country.Philippines: 185>
        Pitcairn: typing.ClassVar[QLocale.Country]  # value = <Country.Pitcairn: 186>
        Poland: typing.ClassVar[QLocale.Country]  # value = <Country.Poland: 187>
        Portugal: typing.ClassVar[QLocale.Country]  # value = <Country.Portugal: 188>
        PuertoRico: typing.ClassVar[QLocale.Country]  # value = <Country.PuertoRico: 189>
        Qatar: typing.ClassVar[QLocale.Country]  # value = <Country.Qatar: 190>
        RepublicOfKorea: typing.ClassVar[QLocale.Country]  # value = <Country.RepublicOfKorea: 218>
        Reunion: typing.ClassVar[QLocale.Country]  # value = <Country.Reunion: 191>
        Romania: typing.ClassVar[QLocale.Country]  # value = <Country.Romania: 192>
        RussianFederation: typing.ClassVar[QLocale.Country]  # value = <Country.RussianFederation: 193>
        Rwanda: typing.ClassVar[QLocale.Country]  # value = <Country.Rwanda: 194>
        SaintBarthelemy: typing.ClassVar[QLocale.Country]  # value = <Country.SaintBarthelemy: 195>
        SaintHelena: typing.ClassVar[QLocale.Country]  # value = <Country.SaintHelena: 196>
        SaintKittsAndNevis: typing.ClassVar[QLocale.Country]  # value = <Country.SaintKittsAndNevis: 197>
        SaintLucia: typing.ClassVar[QLocale.Country]  # value = <Country.SaintLucia: 198>
        SaintMartin: typing.ClassVar[QLocale.Country]  # value = <Country.SaintMartin: 199>
        SaintPierreAndMiquelon: typing.ClassVar[QLocale.Country]  # value = <Country.SaintPierreAndMiquelon: 200>
        SaintVincentAndTheGrenadines: typing.ClassVar[QLocale.Country]  # value = <Country.SaintVincentAndTheGrenadines: 201>
        Samoa: typing.ClassVar[QLocale.Country]  # value = <Country.Samoa: 202>
        SanMarino: typing.ClassVar[QLocale.Country]  # value = <Country.SanMarino: 203>
        SaoTomeAndPrincipe: typing.ClassVar[QLocale.Country]  # value = <Country.SaoTomeAndPrincipe: 204>
        SaudiArabia: typing.ClassVar[QLocale.Country]  # value = <Country.SaudiArabia: 205>
        Senegal: typing.ClassVar[QLocale.Country]  # value = <Country.Senegal: 206>
        Serbia: typing.ClassVar[QLocale.Country]  # value = <Country.Serbia: 207>
        Seychelles: typing.ClassVar[QLocale.Country]  # value = <Country.Seychelles: 208>
        SierraLeone: typing.ClassVar[QLocale.Country]  # value = <Country.SierraLeone: 209>
        Singapore: typing.ClassVar[QLocale.Country]  # value = <Country.Singapore: 210>
        SintMaarten: typing.ClassVar[QLocale.Country]  # value = <Country.SintMaarten: 211>
        Slovakia: typing.ClassVar[QLocale.Country]  # value = <Country.Slovakia: 212>
        Slovenia: typing.ClassVar[QLocale.Country]  # value = <Country.Slovenia: 213>
        SolomonIslands: typing.ClassVar[QLocale.Country]  # value = <Country.SolomonIslands: 214>
        Somalia: typing.ClassVar[QLocale.Country]  # value = <Country.Somalia: 215>
        SouthAfrica: typing.ClassVar[QLocale.Country]  # value = <Country.SouthAfrica: 216>
        SouthGeorgiaAndTheSouthSandwichIslands: typing.ClassVar[QLocale.Country]  # value = <Country.SouthGeorgiaAndTheSouthSandwichIslands: 217>
        SouthSudan: typing.ClassVar[QLocale.Country]  # value = <Country.SouthSudan: 219>
        Spain: typing.ClassVar[QLocale.Country]  # value = <Country.Spain: 220>
        SriLanka: typing.ClassVar[QLocale.Country]  # value = <Country.SriLanka: 221>
        Sudan: typing.ClassVar[QLocale.Country]  # value = <Country.Sudan: 222>
        Suriname: typing.ClassVar[QLocale.Country]  # value = <Country.Suriname: 223>
        SvalbardAndJanMayenIslands: typing.ClassVar[QLocale.Country]  # value = <Country.SvalbardAndJanMayenIslands: 224>
        Swaziland: typing.ClassVar[QLocale.Country]  # value = <Country.Swaziland: 76>
        Sweden: typing.ClassVar[QLocale.Country]  # value = <Country.Sweden: 225>
        Switzerland: typing.ClassVar[QLocale.Country]  # value = <Country.Switzerland: 226>
        SyrianArabRepublic: typing.ClassVar[QLocale.Country]  # value = <Country.SyrianArabRepublic: 227>
        Taiwan: typing.ClassVar[QLocale.Country]  # value = <Country.Taiwan: 228>
        Tajikistan: typing.ClassVar[QLocale.Country]  # value = <Country.Tajikistan: 229>
        Tanzania: typing.ClassVar[QLocale.Country]  # value = <Country.Tanzania: 230>
        Thailand: typing.ClassVar[QLocale.Country]  # value = <Country.Thailand: 231>
        Togo: typing.ClassVar[QLocale.Country]  # value = <Country.Togo: 233>
        TokelauCountry: typing.ClassVar[QLocale.Country]  # value = <Country.TokelauCountry: 234>
        Tonga: typing.ClassVar[QLocale.Country]  # value = <Country.Tonga: 235>
        TrinidadAndTobago: typing.ClassVar[QLocale.Country]  # value = <Country.TrinidadAndTobago: 236>
        TristanDaCunha: typing.ClassVar[QLocale.Country]  # value = <Country.TristanDaCunha: 237>
        Tunisia: typing.ClassVar[QLocale.Country]  # value = <Country.Tunisia: 238>
        Turkey: typing.ClassVar[QLocale.Country]  # value = <Country.Turkey: 239>
        Turkmenistan: typing.ClassVar[QLocale.Country]  # value = <Country.Turkmenistan: 240>
        TurksAndCaicosIslands: typing.ClassVar[QLocale.Country]  # value = <Country.TurksAndCaicosIslands: 241>
        TuvaluCountry: typing.ClassVar[QLocale.Country]  # value = <Country.TuvaluCountry: 242>
        Uganda: typing.ClassVar[QLocale.Country]  # value = <Country.Uganda: 243>
        Ukraine: typing.ClassVar[QLocale.Country]  # value = <Country.Ukraine: 244>
        UnitedArabEmirates: typing.ClassVar[QLocale.Country]  # value = <Country.UnitedArabEmirates: 245>
        UnitedKingdom: typing.ClassVar[QLocale.Country]  # value = <Country.UnitedKingdom: 246>
        UnitedStates: typing.ClassVar[QLocale.Country]  # value = <Country.UnitedStates: 248>
        UnitedStatesMinorOutlyingIslands: typing.ClassVar[QLocale.Country]  # value = <Country.UnitedStatesMinorOutlyingIslands: 247>
        UnitedStatesVirginIslands: typing.ClassVar[QLocale.Country]  # value = <Country.UnitedStatesVirginIslands: 249>
        Uruguay: typing.ClassVar[QLocale.Country]  # value = <Country.Uruguay: 250>
        Uzbekistan: typing.ClassVar[QLocale.Country]  # value = <Country.Uzbekistan: 251>
        Vanuatu: typing.ClassVar[QLocale.Country]  # value = <Country.Vanuatu: 252>
        VaticanCityState: typing.ClassVar[QLocale.Country]  # value = <Country.VaticanCityState: 253>
        Venezuela: typing.ClassVar[QLocale.Country]  # value = <Country.Venezuela: 254>
        Vietnam: typing.ClassVar[QLocale.Country]  # value = <Country.Vietnam: 255>
        WallisAndFutunaIslands: typing.ClassVar[QLocale.Country]  # value = <Country.WallisAndFutunaIslands: 256>
        WesternSahara: typing.ClassVar[QLocale.Country]  # value = <Country.WesternSahara: 257>
        World: typing.ClassVar[QLocale.Country]  # value = <Country.World: 258>
        Yemen: typing.ClassVar[QLocale.Country]  # value = <Country.Yemen: 259>
        Zambia: typing.ClassVar[QLocale.Country]  # value = <Country.Zambia: 260>
        Zimbabwe: typing.ClassVar[QLocale.Country]  # value = <Country.Zimbabwe: 261>
    class CurrencySymbolFormat(enum.Enum):
        CurrencyDisplayName: typing.ClassVar[QLocale.CurrencySymbolFormat]  # value = <CurrencySymbolFormat.CurrencyDisplayName: 2>
        CurrencyIsoCode: typing.ClassVar[QLocale.CurrencySymbolFormat]  # value = <CurrencySymbolFormat.CurrencyIsoCode: 0>
        CurrencySymbol: typing.ClassVar[QLocale.CurrencySymbolFormat]  # value = <CurrencySymbolFormat.CurrencySymbol: 1>
    class DataSizeFormat(enum.Flag):
        DataSizeTraditionalFormat: typing.ClassVar[QLocale.DataSizeFormat]  # value = <DataSizeFormat.DataSizeTraditionalFormat: 2>
    class FloatingPointPrecisionOption(enum.IntEnum):
        FloatingPointShortest: typing.ClassVar[QLocale.FloatingPointPrecisionOption]  # value = <FloatingPointPrecisionOption.FloatingPointShortest: -128>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class FormatType(enum.Enum):
        LongFormat: typing.ClassVar[QLocale.FormatType]  # value = <FormatType.LongFormat: 0>
        NarrowFormat: typing.ClassVar[QLocale.FormatType]  # value = <FormatType.NarrowFormat: 2>
        ShortFormat: typing.ClassVar[QLocale.FormatType]  # value = <FormatType.ShortFormat: 1>
    class Language(enum.Enum):
        Abkhazian: typing.ClassVar[QLocale.Language]  # value = <Language.Abkhazian: 2>
        Afan: typing.ClassVar[QLocale.Language]  # value = <Language.Afan: 220>
        Afar: typing.ClassVar[QLocale.Language]  # value = <Language.Afar: 3>
        Afrikaans: typing.ClassVar[QLocale.Language]  # value = <Language.Afrikaans: 4>
        Aghem: typing.ClassVar[QLocale.Language]  # value = <Language.Aghem: 5>
        Akan: typing.ClassVar[QLocale.Language]  # value = <Language.Akan: 6>
        Akkadian: typing.ClassVar[QLocale.Language]  # value = <Language.Akkadian: 7>
        Akoose: typing.ClassVar[QLocale.Language]  # value = <Language.Akoose: 8>
        Albanian: typing.ClassVar[QLocale.Language]  # value = <Language.Albanian: 9>
        AmericanSignLanguage: typing.ClassVar[QLocale.Language]  # value = <Language.AmericanSignLanguage: 10>
        Amharic: typing.ClassVar[QLocale.Language]  # value = <Language.Amharic: 11>
        AncientEgyptian: typing.ClassVar[QLocale.Language]  # value = <Language.AncientEgyptian: 12>
        AncientGreek: typing.ClassVar[QLocale.Language]  # value = <Language.AncientGreek: 13>
        Anii: typing.ClassVar[QLocale.Language]  # value = <Language.Anii: 341>
        AnyLanguage: typing.ClassVar[QLocale.Language]  # value = <Language.AnyLanguage: 0>
        Arabic: typing.ClassVar[QLocale.Language]  # value = <Language.Arabic: 14>
        Aragonese: typing.ClassVar[QLocale.Language]  # value = <Language.Aragonese: 15>
        Aramaic: typing.ClassVar[QLocale.Language]  # value = <Language.Aramaic: 16>
        Armenian: typing.ClassVar[QLocale.Language]  # value = <Language.Armenian: 17>
        Assamese: typing.ClassVar[QLocale.Language]  # value = <Language.Assamese: 18>
        Asturian: typing.ClassVar[QLocale.Language]  # value = <Language.Asturian: 19>
        Asu: typing.ClassVar[QLocale.Language]  # value = <Language.Asu: 20>
        Atsam: typing.ClassVar[QLocale.Language]  # value = <Language.Atsam: 21>
        Avaric: typing.ClassVar[QLocale.Language]  # value = <Language.Avaric: 22>
        Avestan: typing.ClassVar[QLocale.Language]  # value = <Language.Avestan: 23>
        Aymara: typing.ClassVar[QLocale.Language]  # value = <Language.Aymara: 24>
        Azerbaijani: typing.ClassVar[QLocale.Language]  # value = <Language.Azerbaijani: 25>
        Bafia: typing.ClassVar[QLocale.Language]  # value = <Language.Bafia: 26>
        Balinese: typing.ClassVar[QLocale.Language]  # value = <Language.Balinese: 27>
        Baluchi: typing.ClassVar[QLocale.Language]  # value = <Language.Baluchi: 337>
        Bambara: typing.ClassVar[QLocale.Language]  # value = <Language.Bambara: 28>
        Bamun: typing.ClassVar[QLocale.Language]  # value = <Language.Bamun: 29>
        Basaa: typing.ClassVar[QLocale.Language]  # value = <Language.Basaa: 31>
        Bashkir: typing.ClassVar[QLocale.Language]  # value = <Language.Bashkir: 32>
        Basque: typing.ClassVar[QLocale.Language]  # value = <Language.Basque: 33>
        BatakToba: typing.ClassVar[QLocale.Language]  # value = <Language.BatakToba: 34>
        Bemba: typing.ClassVar[QLocale.Language]  # value = <Language.Bemba: 36>
        Bena: typing.ClassVar[QLocale.Language]  # value = <Language.Bena: 37>
        Bengali: typing.ClassVar[QLocale.Language]  # value = <Language.Bengali: 30>
        Bhojpuri: typing.ClassVar[QLocale.Language]  # value = <Language.Bhojpuri: 38>
        Bhutani: typing.ClassVar[QLocale.Language]  # value = <Language.Bhutani: 73>
        Bislama: typing.ClassVar[QLocale.Language]  # value = <Language.Bislama: 39>
        Blin: typing.ClassVar[QLocale.Language]  # value = <Language.Blin: 40>
        Bodo: typing.ClassVar[QLocale.Language]  # value = <Language.Bodo: 41>
        Bosnian: typing.ClassVar[QLocale.Language]  # value = <Language.Bosnian: 42>
        Breton: typing.ClassVar[QLocale.Language]  # value = <Language.Breton: 43>
        Buginese: typing.ClassVar[QLocale.Language]  # value = <Language.Buginese: 44>
        Bulgarian: typing.ClassVar[QLocale.Language]  # value = <Language.Bulgarian: 45>
        Burmese: typing.ClassVar[QLocale.Language]  # value = <Language.Burmese: 46>
        Byelorussian: typing.ClassVar[QLocale.Language]  # value = <Language.Byelorussian: 35>
        C: typing.ClassVar[QLocale.Language]  # value = <Language.C: 1>
        Cambodian: typing.ClassVar[QLocale.Language]  # value = <Language.Cambodian: 135>
        Cantonese: typing.ClassVar[QLocale.Language]  # value = <Language.Cantonese: 47>
        Catalan: typing.ClassVar[QLocale.Language]  # value = <Language.Catalan: 48>
        Cebuano: typing.ClassVar[QLocale.Language]  # value = <Language.Cebuano: 49>
        CentralKurdish: typing.ClassVar[QLocale.Language]  # value = <Language.CentralKurdish: 51>
        CentralMoroccoTamazight: typing.ClassVar[QLocale.Language]  # value = <Language.CentralMoroccoTamazight: 50>
        Chakma: typing.ClassVar[QLocale.Language]  # value = <Language.Chakma: 52>
        Chamorro: typing.ClassVar[QLocale.Language]  # value = <Language.Chamorro: 53>
        Chechen: typing.ClassVar[QLocale.Language]  # value = <Language.Chechen: 54>
        Cherokee: typing.ClassVar[QLocale.Language]  # value = <Language.Cherokee: 55>
        Chewa: typing.ClassVar[QLocale.Language]  # value = <Language.Chewa: 212>
        Chickasaw: typing.ClassVar[QLocale.Language]  # value = <Language.Chickasaw: 56>
        Chiga: typing.ClassVar[QLocale.Language]  # value = <Language.Chiga: 57>
        Chinese: typing.ClassVar[QLocale.Language]  # value = <Language.Chinese: 58>
        Church: typing.ClassVar[QLocale.Language]  # value = <Language.Church: 59>
        Chuvash: typing.ClassVar[QLocale.Language]  # value = <Language.Chuvash: 60>
        Colognian: typing.ClassVar[QLocale.Language]  # value = <Language.Colognian: 61>
        Coptic: typing.ClassVar[QLocale.Language]  # value = <Language.Coptic: 62>
        Cornish: typing.ClassVar[QLocale.Language]  # value = <Language.Cornish: 63>
        Corsican: typing.ClassVar[QLocale.Language]  # value = <Language.Corsican: 64>
        Cree: typing.ClassVar[QLocale.Language]  # value = <Language.Cree: 65>
        Croatian: typing.ClassVar[QLocale.Language]  # value = <Language.Croatian: 66>
        Czech: typing.ClassVar[QLocale.Language]  # value = <Language.Czech: 67>
        Danish: typing.ClassVar[QLocale.Language]  # value = <Language.Danish: 68>
        Divehi: typing.ClassVar[QLocale.Language]  # value = <Language.Divehi: 69>
        Dogri: typing.ClassVar[QLocale.Language]  # value = <Language.Dogri: 70>
        Duala: typing.ClassVar[QLocale.Language]  # value = <Language.Duala: 71>
        Dutch: typing.ClassVar[QLocale.Language]  # value = <Language.Dutch: 72>
        Embu: typing.ClassVar[QLocale.Language]  # value = <Language.Embu: 74>
        English: typing.ClassVar[QLocale.Language]  # value = <Language.English: 75>
        Erzya: typing.ClassVar[QLocale.Language]  # value = <Language.Erzya: 76>
        Esperanto: typing.ClassVar[QLocale.Language]  # value = <Language.Esperanto: 77>
        Estonian: typing.ClassVar[QLocale.Language]  # value = <Language.Estonian: 78>
        Ewe: typing.ClassVar[QLocale.Language]  # value = <Language.Ewe: 79>
        Ewondo: typing.ClassVar[QLocale.Language]  # value = <Language.Ewondo: 80>
        Faroese: typing.ClassVar[QLocale.Language]  # value = <Language.Faroese: 81>
        Fijian: typing.ClassVar[QLocale.Language]  # value = <Language.Fijian: 82>
        Filipino: typing.ClassVar[QLocale.Language]  # value = <Language.Filipino: 83>
        Finnish: typing.ClassVar[QLocale.Language]  # value = <Language.Finnish: 84>
        French: typing.ClassVar[QLocale.Language]  # value = <Language.French: 85>
        Frisian: typing.ClassVar[QLocale.Language]  # value = <Language.Frisian: 318>
        Friulian: typing.ClassVar[QLocale.Language]  # value = <Language.Friulian: 86>
        Fulah: typing.ClassVar[QLocale.Language]  # value = <Language.Fulah: 87>
        Ga: typing.ClassVar[QLocale.Language]  # value = <Language.Ga: 89>
        Gaelic: typing.ClassVar[QLocale.Language]  # value = <Language.Gaelic: 88>
        Galician: typing.ClassVar[QLocale.Language]  # value = <Language.Galician: 90>
        Ganda: typing.ClassVar[QLocale.Language]  # value = <Language.Ganda: 91>
        Geez: typing.ClassVar[QLocale.Language]  # value = <Language.Geez: 92>
        Georgian: typing.ClassVar[QLocale.Language]  # value = <Language.Georgian: 93>
        German: typing.ClassVar[QLocale.Language]  # value = <Language.German: 94>
        Gothic: typing.ClassVar[QLocale.Language]  # value = <Language.Gothic: 95>
        Greek: typing.ClassVar[QLocale.Language]  # value = <Language.Greek: 96>
        Greenlandic: typing.ClassVar[QLocale.Language]  # value = <Language.Greenlandic: 127>
        Guarani: typing.ClassVar[QLocale.Language]  # value = <Language.Guarani: 97>
        Gujarati: typing.ClassVar[QLocale.Language]  # value = <Language.Gujarati: 98>
        Gusii: typing.ClassVar[QLocale.Language]  # value = <Language.Gusii: 99>
        Haitian: typing.ClassVar[QLocale.Language]  # value = <Language.Haitian: 100>
        Haryanvi: typing.ClassVar[QLocale.Language]  # value = <Language.Haryanvi: 330>
        Hausa: typing.ClassVar[QLocale.Language]  # value = <Language.Hausa: 101>
        Hawaiian: typing.ClassVar[QLocale.Language]  # value = <Language.Hawaiian: 102>
        Hebrew: typing.ClassVar[QLocale.Language]  # value = <Language.Hebrew: 103>
        Herero: typing.ClassVar[QLocale.Language]  # value = <Language.Herero: 104>
        Hindi: typing.ClassVar[QLocale.Language]  # value = <Language.Hindi: 105>
        HiriMotu: typing.ClassVar[QLocale.Language]  # value = <Language.HiriMotu: 106>
        Hungarian: typing.ClassVar[QLocale.Language]  # value = <Language.Hungarian: 107>
        Icelandic: typing.ClassVar[QLocale.Language]  # value = <Language.Icelandic: 108>
        Ido: typing.ClassVar[QLocale.Language]  # value = <Language.Ido: 109>
        Igbo: typing.ClassVar[QLocale.Language]  # value = <Language.Igbo: 110>
        InariSami: typing.ClassVar[QLocale.Language]  # value = <Language.InariSami: 111>
        Indonesian: typing.ClassVar[QLocale.Language]  # value = <Language.Indonesian: 112>
        Ingush: typing.ClassVar[QLocale.Language]  # value = <Language.Ingush: 113>
        Interlingua: typing.ClassVar[QLocale.Language]  # value = <Language.Interlingua: 114>
        Interlingue: typing.ClassVar[QLocale.Language]  # value = <Language.Interlingue: 115>
        Inuktitut: typing.ClassVar[QLocale.Language]  # value = <Language.Inuktitut: 116>
        Inupiak: typing.ClassVar[QLocale.Language]  # value = <Language.Inupiak: 117>
        Irish: typing.ClassVar[QLocale.Language]  # value = <Language.Irish: 118>
        Italian: typing.ClassVar[QLocale.Language]  # value = <Language.Italian: 119>
        Japanese: typing.ClassVar[QLocale.Language]  # value = <Language.Japanese: 120>
        Javanese: typing.ClassVar[QLocale.Language]  # value = <Language.Javanese: 121>
        Jju: typing.ClassVar[QLocale.Language]  # value = <Language.Jju: 122>
        JolaFonyi: typing.ClassVar[QLocale.Language]  # value = <Language.JolaFonyi: 123>
        Kabuverdianu: typing.ClassVar[QLocale.Language]  # value = <Language.Kabuverdianu: 124>
        Kabyle: typing.ClassVar[QLocale.Language]  # value = <Language.Kabyle: 125>
        Kaingang: typing.ClassVar[QLocale.Language]  # value = <Language.Kaingang: 328>
        Kako: typing.ClassVar[QLocale.Language]  # value = <Language.Kako: 126>
        Kalenjin: typing.ClassVar[QLocale.Language]  # value = <Language.Kalenjin: 128>
        Kamba: typing.ClassVar[QLocale.Language]  # value = <Language.Kamba: 129>
        Kangri: typing.ClassVar[QLocale.Language]  # value = <Language.Kangri: 342>
        Kannada: typing.ClassVar[QLocale.Language]  # value = <Language.Kannada: 130>
        Kanuri: typing.ClassVar[QLocale.Language]  # value = <Language.Kanuri: 131>
        Kashmiri: typing.ClassVar[QLocale.Language]  # value = <Language.Kashmiri: 132>
        Kazakh: typing.ClassVar[QLocale.Language]  # value = <Language.Kazakh: 133>
        Kenyang: typing.ClassVar[QLocale.Language]  # value = <Language.Kenyang: 134>
        Kiche: typing.ClassVar[QLocale.Language]  # value = <Language.Kiche: 136>
        Kikuyu: typing.ClassVar[QLocale.Language]  # value = <Language.Kikuyu: 137>
        Kinyarwanda: typing.ClassVar[QLocale.Language]  # value = <Language.Kinyarwanda: 138>
        Kirghiz: typing.ClassVar[QLocale.Language]  # value = <Language.Kirghiz: 150>
        Komi: typing.ClassVar[QLocale.Language]  # value = <Language.Komi: 139>
        Kongo: typing.ClassVar[QLocale.Language]  # value = <Language.Kongo: 140>
        Konkani: typing.ClassVar[QLocale.Language]  # value = <Language.Konkani: 141>
        Korean: typing.ClassVar[QLocale.Language]  # value = <Language.Korean: 142>
        Koro: typing.ClassVar[QLocale.Language]  # value = <Language.Koro: 143>
        KoyraChiini: typing.ClassVar[QLocale.Language]  # value = <Language.KoyraChiini: 145>
        KoyraboroSenni: typing.ClassVar[QLocale.Language]  # value = <Language.KoyraboroSenni: 144>
        Kpelle: typing.ClassVar[QLocale.Language]  # value = <Language.Kpelle: 146>
        Kurdish: typing.ClassVar[QLocale.Language]  # value = <Language.Kurdish: 148>
        Kurundi: typing.ClassVar[QLocale.Language]  # value = <Language.Kurundi: 238>
        Kwanyama: typing.ClassVar[QLocale.Language]  # value = <Language.Kwanyama: 147>
        Kwasio: typing.ClassVar[QLocale.Language]  # value = <Language.Kwasio: 149>
        Lakota: typing.ClassVar[QLocale.Language]  # value = <Language.Lakota: 151>
        Langi: typing.ClassVar[QLocale.Language]  # value = <Language.Langi: 152>
        Lao: typing.ClassVar[QLocale.Language]  # value = <Language.Lao: 153>
        LastLanguage: typing.ClassVar[QLocale.Language]  # value = <Language.LastLanguage: 343>
        Latin: typing.ClassVar[QLocale.Language]  # value = <Language.Latin: 154>
        Latvian: typing.ClassVar[QLocale.Language]  # value = <Language.Latvian: 155>
        Lezghian: typing.ClassVar[QLocale.Language]  # value = <Language.Lezghian: 156>
        Ligurian: typing.ClassVar[QLocale.Language]  # value = <Language.Ligurian: 338>
        Limburgish: typing.ClassVar[QLocale.Language]  # value = <Language.Limburgish: 157>
        Lingala: typing.ClassVar[QLocale.Language]  # value = <Language.Lingala: 158>
        LiteraryChinese: typing.ClassVar[QLocale.Language]  # value = <Language.LiteraryChinese: 159>
        Lithuanian: typing.ClassVar[QLocale.Language]  # value = <Language.Lithuanian: 160>
        Lojban: typing.ClassVar[QLocale.Language]  # value = <Language.Lojban: 161>
        LowGerman: typing.ClassVar[QLocale.Language]  # value = <Language.LowGerman: 163>
        LowerSorbian: typing.ClassVar[QLocale.Language]  # value = <Language.LowerSorbian: 162>
        LubaKatanga: typing.ClassVar[QLocale.Language]  # value = <Language.LubaKatanga: 164>
        LuleSami: typing.ClassVar[QLocale.Language]  # value = <Language.LuleSami: 165>
        Luo: typing.ClassVar[QLocale.Language]  # value = <Language.Luo: 166>
        Luxembourgish: typing.ClassVar[QLocale.Language]  # value = <Language.Luxembourgish: 167>
        Luyia: typing.ClassVar[QLocale.Language]  # value = <Language.Luyia: 168>
        Macedonian: typing.ClassVar[QLocale.Language]  # value = <Language.Macedonian: 169>
        Machame: typing.ClassVar[QLocale.Language]  # value = <Language.Machame: 170>
        Maithili: typing.ClassVar[QLocale.Language]  # value = <Language.Maithili: 171>
        MakhuwaMeetto: typing.ClassVar[QLocale.Language]  # value = <Language.MakhuwaMeetto: 172>
        Makonde: typing.ClassVar[QLocale.Language]  # value = <Language.Makonde: 173>
        Malagasy: typing.ClassVar[QLocale.Language]  # value = <Language.Malagasy: 174>
        Malay: typing.ClassVar[QLocale.Language]  # value = <Language.Malay: 176>
        Malayalam: typing.ClassVar[QLocale.Language]  # value = <Language.Malayalam: 175>
        Maltese: typing.ClassVar[QLocale.Language]  # value = <Language.Maltese: 177>
        Mandingo: typing.ClassVar[QLocale.Language]  # value = <Language.Mandingo: 178>
        Manipuri: typing.ClassVar[QLocale.Language]  # value = <Language.Manipuri: 179>
        Manx: typing.ClassVar[QLocale.Language]  # value = <Language.Manx: 180>
        Maori: typing.ClassVar[QLocale.Language]  # value = <Language.Maori: 181>
        Mapuche: typing.ClassVar[QLocale.Language]  # value = <Language.Mapuche: 182>
        Marathi: typing.ClassVar[QLocale.Language]  # value = <Language.Marathi: 183>
        Marshallese: typing.ClassVar[QLocale.Language]  # value = <Language.Marshallese: 184>
        Masai: typing.ClassVar[QLocale.Language]  # value = <Language.Masai: 185>
        Mazanderani: typing.ClassVar[QLocale.Language]  # value = <Language.Mazanderani: 186>
        Mende: typing.ClassVar[QLocale.Language]  # value = <Language.Mende: 187>
        Meru: typing.ClassVar[QLocale.Language]  # value = <Language.Meru: 188>
        Meta: typing.ClassVar[QLocale.Language]  # value = <Language.Meta: 189>
        Mohawk: typing.ClassVar[QLocale.Language]  # value = <Language.Mohawk: 190>
        Moksha: typing.ClassVar[QLocale.Language]  # value = <Language.Moksha: 333>
        Mongolian: typing.ClassVar[QLocale.Language]  # value = <Language.Mongolian: 191>
        Morisyen: typing.ClassVar[QLocale.Language]  # value = <Language.Morisyen: 192>
        Mundang: typing.ClassVar[QLocale.Language]  # value = <Language.Mundang: 193>
        Muscogee: typing.ClassVar[QLocale.Language]  # value = <Language.Muscogee: 194>
        Nama: typing.ClassVar[QLocale.Language]  # value = <Language.Nama: 195>
        NauruLanguage: typing.ClassVar[QLocale.Language]  # value = <Language.NauruLanguage: 196>
        Navaho: typing.ClassVar[QLocale.Language]  # value = <Language.Navaho: 197>
        Ndonga: typing.ClassVar[QLocale.Language]  # value = <Language.Ndonga: 198>
        Nepali: typing.ClassVar[QLocale.Language]  # value = <Language.Nepali: 199>
        Newari: typing.ClassVar[QLocale.Language]  # value = <Language.Newari: 200>
        Ngiemboon: typing.ClassVar[QLocale.Language]  # value = <Language.Ngiemboon: 201>
        Ngomba: typing.ClassVar[QLocale.Language]  # value = <Language.Ngomba: 202>
        Nheengatu: typing.ClassVar[QLocale.Language]  # value = <Language.Nheengatu: 329>
        NigerianPidgin: typing.ClassVar[QLocale.Language]  # value = <Language.NigerianPidgin: 203>
        Nko: typing.ClassVar[QLocale.Language]  # value = <Language.Nko: 204>
        NorthNdebele: typing.ClassVar[QLocale.Language]  # value = <Language.NorthNdebele: 208>
        NorthernFrisian: typing.ClassVar[QLocale.Language]  # value = <Language.NorthernFrisian: 331>
        NorthernLuri: typing.ClassVar[QLocale.Language]  # value = <Language.NorthernLuri: 205>
        NorthernSami: typing.ClassVar[QLocale.Language]  # value = <Language.NorthernSami: 206>
        NorthernSotho: typing.ClassVar[QLocale.Language]  # value = <Language.NorthernSotho: 207>
        NorwegianBokmal: typing.ClassVar[QLocale.Language]  # value = <Language.NorwegianBokmal: 209>
        NorwegianNynorsk: typing.ClassVar[QLocale.Language]  # value = <Language.NorwegianNynorsk: 210>
        Nuer: typing.ClassVar[QLocale.Language]  # value = <Language.Nuer: 211>
        Nyankole: typing.ClassVar[QLocale.Language]  # value = <Language.Nyankole: 213>
        Obolo: typing.ClassVar[QLocale.Language]  # value = <Language.Obolo: 336>
        Occitan: typing.ClassVar[QLocale.Language]  # value = <Language.Occitan: 214>
        Ojibwa: typing.ClassVar[QLocale.Language]  # value = <Language.Ojibwa: 216>
        OldIrish: typing.ClassVar[QLocale.Language]  # value = <Language.OldIrish: 217>
        OldNorse: typing.ClassVar[QLocale.Language]  # value = <Language.OldNorse: 218>
        OldPersian: typing.ClassVar[QLocale.Language]  # value = <Language.OldPersian: 219>
        Oriya: typing.ClassVar[QLocale.Language]  # value = <Language.Oriya: 215>
        Osage: typing.ClassVar[QLocale.Language]  # value = <Language.Osage: 221>
        Ossetic: typing.ClassVar[QLocale.Language]  # value = <Language.Ossetic: 222>
        Pahlavi: typing.ClassVar[QLocale.Language]  # value = <Language.Pahlavi: 223>
        Palauan: typing.ClassVar[QLocale.Language]  # value = <Language.Palauan: 224>
        Pali: typing.ClassVar[QLocale.Language]  # value = <Language.Pali: 225>
        Papiamento: typing.ClassVar[QLocale.Language]  # value = <Language.Papiamento: 226>
        Pashto: typing.ClassVar[QLocale.Language]  # value = <Language.Pashto: 227>
        Persian: typing.ClassVar[QLocale.Language]  # value = <Language.Persian: 228>
        Phoenician: typing.ClassVar[QLocale.Language]  # value = <Language.Phoenician: 229>
        Pijin: typing.ClassVar[QLocale.Language]  # value = <Language.Pijin: 335>
        Polish: typing.ClassVar[QLocale.Language]  # value = <Language.Polish: 230>
        Portuguese: typing.ClassVar[QLocale.Language]  # value = <Language.Portuguese: 231>
        Prussian: typing.ClassVar[QLocale.Language]  # value = <Language.Prussian: 232>
        Punjabi: typing.ClassVar[QLocale.Language]  # value = <Language.Punjabi: 233>
        Quechua: typing.ClassVar[QLocale.Language]  # value = <Language.Quechua: 234>
        Rajasthani: typing.ClassVar[QLocale.Language]  # value = <Language.Rajasthani: 332>
        RhaetoRomance: typing.ClassVar[QLocale.Language]  # value = <Language.RhaetoRomance: 236>
        Rohingya: typing.ClassVar[QLocale.Language]  # value = <Language.Rohingya: 339>
        Romanian: typing.ClassVar[QLocale.Language]  # value = <Language.Romanian: 235>
        Rombo: typing.ClassVar[QLocale.Language]  # value = <Language.Rombo: 237>
        Russian: typing.ClassVar[QLocale.Language]  # value = <Language.Russian: 239>
        Rwa: typing.ClassVar[QLocale.Language]  # value = <Language.Rwa: 240>
        Saho: typing.ClassVar[QLocale.Language]  # value = <Language.Saho: 241>
        Sakha: typing.ClassVar[QLocale.Language]  # value = <Language.Sakha: 242>
        Samburu: typing.ClassVar[QLocale.Language]  # value = <Language.Samburu: 243>
        Samoan: typing.ClassVar[QLocale.Language]  # value = <Language.Samoan: 244>
        Sango: typing.ClassVar[QLocale.Language]  # value = <Language.Sango: 245>
        Sangu: typing.ClassVar[QLocale.Language]  # value = <Language.Sangu: 246>
        Sanskrit: typing.ClassVar[QLocale.Language]  # value = <Language.Sanskrit: 247>
        Santali: typing.ClassVar[QLocale.Language]  # value = <Language.Santali: 248>
        Sardinian: typing.ClassVar[QLocale.Language]  # value = <Language.Sardinian: 249>
        Saurashtra: typing.ClassVar[QLocale.Language]  # value = <Language.Saurashtra: 250>
        Sena: typing.ClassVar[QLocale.Language]  # value = <Language.Sena: 251>
        Serbian: typing.ClassVar[QLocale.Language]  # value = <Language.Serbian: 252>
        Shambala: typing.ClassVar[QLocale.Language]  # value = <Language.Shambala: 253>
        Shona: typing.ClassVar[QLocale.Language]  # value = <Language.Shona: 254>
        SichuanYi: typing.ClassVar[QLocale.Language]  # value = <Language.SichuanYi: 255>
        Sicilian: typing.ClassVar[QLocale.Language]  # value = <Language.Sicilian: 256>
        Sidamo: typing.ClassVar[QLocale.Language]  # value = <Language.Sidamo: 257>
        Silesian: typing.ClassVar[QLocale.Language]  # value = <Language.Silesian: 258>
        Sindhi: typing.ClassVar[QLocale.Language]  # value = <Language.Sindhi: 259>
        Sinhala: typing.ClassVar[QLocale.Language]  # value = <Language.Sinhala: 260>
        SkoltSami: typing.ClassVar[QLocale.Language]  # value = <Language.SkoltSami: 261>
        Slovak: typing.ClassVar[QLocale.Language]  # value = <Language.Slovak: 262>
        Slovenian: typing.ClassVar[QLocale.Language]  # value = <Language.Slovenian: 263>
        Soga: typing.ClassVar[QLocale.Language]  # value = <Language.Soga: 264>
        Somali: typing.ClassVar[QLocale.Language]  # value = <Language.Somali: 265>
        SouthNdebele: typing.ClassVar[QLocale.Language]  # value = <Language.SouthNdebele: 269>
        SouthernKurdish: typing.ClassVar[QLocale.Language]  # value = <Language.SouthernKurdish: 266>
        SouthernSami: typing.ClassVar[QLocale.Language]  # value = <Language.SouthernSami: 267>
        SouthernSotho: typing.ClassVar[QLocale.Language]  # value = <Language.SouthernSotho: 268>
        Spanish: typing.ClassVar[QLocale.Language]  # value = <Language.Spanish: 270>
        StandardMoroccanTamazight: typing.ClassVar[QLocale.Language]  # value = <Language.StandardMoroccanTamazight: 271>
        Sundanese: typing.ClassVar[QLocale.Language]  # value = <Language.Sundanese: 272>
        Swahili: typing.ClassVar[QLocale.Language]  # value = <Language.Swahili: 273>
        Swati: typing.ClassVar[QLocale.Language]  # value = <Language.Swati: 274>
        Swedish: typing.ClassVar[QLocale.Language]  # value = <Language.Swedish: 275>
        SwissGerman: typing.ClassVar[QLocale.Language]  # value = <Language.SwissGerman: 276>
        Syriac: typing.ClassVar[QLocale.Language]  # value = <Language.Syriac: 277>
        Tachelhit: typing.ClassVar[QLocale.Language]  # value = <Language.Tachelhit: 278>
        Tahitian: typing.ClassVar[QLocale.Language]  # value = <Language.Tahitian: 279>
        TaiDam: typing.ClassVar[QLocale.Language]  # value = <Language.TaiDam: 280>
        Taita: typing.ClassVar[QLocale.Language]  # value = <Language.Taita: 281>
        Tajik: typing.ClassVar[QLocale.Language]  # value = <Language.Tajik: 282>
        Tamil: typing.ClassVar[QLocale.Language]  # value = <Language.Tamil: 283>
        Taroko: typing.ClassVar[QLocale.Language]  # value = <Language.Taroko: 284>
        Tasawaq: typing.ClassVar[QLocale.Language]  # value = <Language.Tasawaq: 285>
        Tatar: typing.ClassVar[QLocale.Language]  # value = <Language.Tatar: 286>
        Telugu: typing.ClassVar[QLocale.Language]  # value = <Language.Telugu: 287>
        Teso: typing.ClassVar[QLocale.Language]  # value = <Language.Teso: 288>
        Thai: typing.ClassVar[QLocale.Language]  # value = <Language.Thai: 289>
        Tibetan: typing.ClassVar[QLocale.Language]  # value = <Language.Tibetan: 290>
        Tigre: typing.ClassVar[QLocale.Language]  # value = <Language.Tigre: 291>
        Tigrinya: typing.ClassVar[QLocale.Language]  # value = <Language.Tigrinya: 292>
        TokPisin: typing.ClassVar[QLocale.Language]  # value = <Language.TokPisin: 294>
        TokelauLanguage: typing.ClassVar[QLocale.Language]  # value = <Language.TokelauLanguage: 293>
        TokiPona: typing.ClassVar[QLocale.Language]  # value = <Language.TokiPona: 334>
        Tongan: typing.ClassVar[QLocale.Language]  # value = <Language.Tongan: 295>
        Torwali: typing.ClassVar[QLocale.Language]  # value = <Language.Torwali: 340>
        Tsonga: typing.ClassVar[QLocale.Language]  # value = <Language.Tsonga: 296>
        Tswana: typing.ClassVar[QLocale.Language]  # value = <Language.Tswana: 297>
        Turkish: typing.ClassVar[QLocale.Language]  # value = <Language.Turkish: 298>
        Turkmen: typing.ClassVar[QLocale.Language]  # value = <Language.Turkmen: 299>
        TuvaluLanguage: typing.ClassVar[QLocale.Language]  # value = <Language.TuvaluLanguage: 300>
        Tyap: typing.ClassVar[QLocale.Language]  # value = <Language.Tyap: 301>
        Ugaritic: typing.ClassVar[QLocale.Language]  # value = <Language.Ugaritic: 302>
        Uigur: typing.ClassVar[QLocale.Language]  # value = <Language.Uigur: 306>
        Ukrainian: typing.ClassVar[QLocale.Language]  # value = <Language.Ukrainian: 303>
        UpperSorbian: typing.ClassVar[QLocale.Language]  # value = <Language.UpperSorbian: 304>
        Urdu: typing.ClassVar[QLocale.Language]  # value = <Language.Urdu: 305>
        Uzbek: typing.ClassVar[QLocale.Language]  # value = <Language.Uzbek: 307>
        Vai: typing.ClassVar[QLocale.Language]  # value = <Language.Vai: 308>
        Venda: typing.ClassVar[QLocale.Language]  # value = <Language.Venda: 309>
        Vietnamese: typing.ClassVar[QLocale.Language]  # value = <Language.Vietnamese: 310>
        Volapuk: typing.ClassVar[QLocale.Language]  # value = <Language.Volapuk: 311>
        Vunjo: typing.ClassVar[QLocale.Language]  # value = <Language.Vunjo: 312>
        Walamo: typing.ClassVar[QLocale.Language]  # value = <Language.Walamo: 319>
        Walloon: typing.ClassVar[QLocale.Language]  # value = <Language.Walloon: 313>
        Walser: typing.ClassVar[QLocale.Language]  # value = <Language.Walser: 314>
        Warlpiri: typing.ClassVar[QLocale.Language]  # value = <Language.Warlpiri: 315>
        Welsh: typing.ClassVar[QLocale.Language]  # value = <Language.Welsh: 316>
        WesternBalochi: typing.ClassVar[QLocale.Language]  # value = <Language.WesternBalochi: 317>
        Wolof: typing.ClassVar[QLocale.Language]  # value = <Language.Wolof: 320>
        Xhosa: typing.ClassVar[QLocale.Language]  # value = <Language.Xhosa: 321>
        Yangben: typing.ClassVar[QLocale.Language]  # value = <Language.Yangben: 322>
        Yiddish: typing.ClassVar[QLocale.Language]  # value = <Language.Yiddish: 323>
        Yoruba: typing.ClassVar[QLocale.Language]  # value = <Language.Yoruba: 324>
        Zarma: typing.ClassVar[QLocale.Language]  # value = <Language.Zarma: 325>
        Zhuang: typing.ClassVar[QLocale.Language]  # value = <Language.Zhuang: 326>
        Zulu: typing.ClassVar[QLocale.Language]  # value = <Language.Zulu: 327>
    class LanguageCodeType(enum.IntFlag):
        ISO639Part1: typing.ClassVar[QLocale.LanguageCodeType]  # value = <LanguageCodeType.ISO639Part1: 1>
        ISO639Part2B: typing.ClassVar[QLocale.LanguageCodeType]  # value = <LanguageCodeType.ISO639Part2B: 2>
        ISO639Part2T: typing.ClassVar[QLocale.LanguageCodeType]  # value = <LanguageCodeType.ISO639Part2T: 4>
        ISO639Part3: typing.ClassVar[QLocale.LanguageCodeType]  # value = <LanguageCodeType.ISO639Part3: 8>
        LegacyLanguageCode: typing.ClassVar[QLocale.LanguageCodeType]  # value = <LanguageCodeType.LegacyLanguageCode: 32768>
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
    class MeasurementSystem(enum.Enum):
        ImperialSystem: typing.ClassVar[QLocale.MeasurementSystem]  # value = <MeasurementSystem.ImperialSystem: 1>
        ImperialUKSystem: typing.ClassVar[QLocale.MeasurementSystem]  # value = <MeasurementSystem.ImperialUKSystem: 2>
        MetricSystem: typing.ClassVar[QLocale.MeasurementSystem]  # value = <MeasurementSystem.MetricSystem: 0>
    class NumberOption(enum.Flag):
        IncludeTrailingZeroesAfterDot: typing.ClassVar[QLocale.NumberOption]  # value = <NumberOption.IncludeTrailingZeroesAfterDot: 16>
        OmitGroupSeparator: typing.ClassVar[QLocale.NumberOption]  # value = <NumberOption.OmitGroupSeparator: 1>
        OmitLeadingZeroInExponent: typing.ClassVar[QLocale.NumberOption]  # value = <NumberOption.OmitLeadingZeroInExponent: 4>
        RejectGroupSeparator: typing.ClassVar[QLocale.NumberOption]  # value = <NumberOption.RejectGroupSeparator: 2>
        RejectLeadingZeroInExponent: typing.ClassVar[QLocale.NumberOption]  # value = <NumberOption.RejectLeadingZeroInExponent: 8>
        RejectTrailingZeroesAfterDot: typing.ClassVar[QLocale.NumberOption]  # value = <NumberOption.RejectTrailingZeroesAfterDot: 32>
    class QuotationStyle(enum.Enum):
        AlternateQuotation: typing.ClassVar[QLocale.QuotationStyle]  # value = <QuotationStyle.AlternateQuotation: 1>
        StandardQuotation: typing.ClassVar[QLocale.QuotationStyle]  # value = <QuotationStyle.StandardQuotation: 0>
    class Script(enum.Enum):
        AdlamScript: typing.ClassVar[QLocale.Script]  # value = <Script.AdlamScript: 1>
        AhomScript: typing.ClassVar[QLocale.Script]  # value = <Script.AhomScript: 2>
        AnatolianHieroglyphsScript: typing.ClassVar[QLocale.Script]  # value = <Script.AnatolianHieroglyphsScript: 3>
        AnyScript: typing.ClassVar[QLocale.Script]  # value = <Script.AnyScript: 0>
        ArabicScript: typing.ClassVar[QLocale.Script]  # value = <Script.ArabicScript: 4>
        ArmenianScript: typing.ClassVar[QLocale.Script]  # value = <Script.ArmenianScript: 5>
        AvestanScript: typing.ClassVar[QLocale.Script]  # value = <Script.AvestanScript: 6>
        BalineseScript: typing.ClassVar[QLocale.Script]  # value = <Script.BalineseScript: 7>
        BamumScript: typing.ClassVar[QLocale.Script]  # value = <Script.BamumScript: 8>
        BassaVahScript: typing.ClassVar[QLocale.Script]  # value = <Script.BassaVahScript: 10>
        BatakScript: typing.ClassVar[QLocale.Script]  # value = <Script.BatakScript: 11>
        BengaliScript: typing.ClassVar[QLocale.Script]  # value = <Script.BengaliScript: 9>
        BhaiksukiScript: typing.ClassVar[QLocale.Script]  # value = <Script.BhaiksukiScript: 12>
        BopomofoScript: typing.ClassVar[QLocale.Script]  # value = <Script.BopomofoScript: 13>
        BrahmiScript: typing.ClassVar[QLocale.Script]  # value = <Script.BrahmiScript: 14>
        BrailleScript: typing.ClassVar[QLocale.Script]  # value = <Script.BrailleScript: 15>
        BugineseScript: typing.ClassVar[QLocale.Script]  # value = <Script.BugineseScript: 16>
        BuhidScript: typing.ClassVar[QLocale.Script]  # value = <Script.BuhidScript: 17>
        CanadianAboriginalScript: typing.ClassVar[QLocale.Script]  # value = <Script.CanadianAboriginalScript: 18>
        CarianScript: typing.ClassVar[QLocale.Script]  # value = <Script.CarianScript: 19>
        CaucasianAlbanianScript: typing.ClassVar[QLocale.Script]  # value = <Script.CaucasianAlbanianScript: 20>
        ChakmaScript: typing.ClassVar[QLocale.Script]  # value = <Script.ChakmaScript: 21>
        ChamScript: typing.ClassVar[QLocale.Script]  # value = <Script.ChamScript: 22>
        CherokeeScript: typing.ClassVar[QLocale.Script]  # value = <Script.CherokeeScript: 23>
        CopticScript: typing.ClassVar[QLocale.Script]  # value = <Script.CopticScript: 24>
        CuneiformScript: typing.ClassVar[QLocale.Script]  # value = <Script.CuneiformScript: 25>
        CypriotScript: typing.ClassVar[QLocale.Script]  # value = <Script.CypriotScript: 26>
        CyrillicScript: typing.ClassVar[QLocale.Script]  # value = <Script.CyrillicScript: 27>
        DeseretScript: typing.ClassVar[QLocale.Script]  # value = <Script.DeseretScript: 28>
        DevanagariScript: typing.ClassVar[QLocale.Script]  # value = <Script.DevanagariScript: 29>
        DuployanScript: typing.ClassVar[QLocale.Script]  # value = <Script.DuployanScript: 30>
        EgyptianHieroglyphsScript: typing.ClassVar[QLocale.Script]  # value = <Script.EgyptianHieroglyphsScript: 31>
        ElbasanScript: typing.ClassVar[QLocale.Script]  # value = <Script.ElbasanScript: 32>
        EthiopicScript: typing.ClassVar[QLocale.Script]  # value = <Script.EthiopicScript: 33>
        FraserScript: typing.ClassVar[QLocale.Script]  # value = <Script.FraserScript: 34>
        GeorgianScript: typing.ClassVar[QLocale.Script]  # value = <Script.GeorgianScript: 35>
        GlagoliticScript: typing.ClassVar[QLocale.Script]  # value = <Script.GlagoliticScript: 36>
        GothicScript: typing.ClassVar[QLocale.Script]  # value = <Script.GothicScript: 37>
        GranthaScript: typing.ClassVar[QLocale.Script]  # value = <Script.GranthaScript: 38>
        GreekScript: typing.ClassVar[QLocale.Script]  # value = <Script.GreekScript: 39>
        GujaratiScript: typing.ClassVar[QLocale.Script]  # value = <Script.GujaratiScript: 40>
        GurmukhiScript: typing.ClassVar[QLocale.Script]  # value = <Script.GurmukhiScript: 41>
        HanScript: typing.ClassVar[QLocale.Script]  # value = <Script.HanScript: 43>
        HanWithBopomofoScript: typing.ClassVar[QLocale.Script]  # value = <Script.HanWithBopomofoScript: 45>
        HangulScript: typing.ClassVar[QLocale.Script]  # value = <Script.HangulScript: 42>
        HanifiScript: typing.ClassVar[QLocale.Script]  # value = <Script.HanifiScript: 142>
        HanunooScript: typing.ClassVar[QLocale.Script]  # value = <Script.HanunooScript: 44>
        HatranScript: typing.ClassVar[QLocale.Script]  # value = <Script.HatranScript: 46>
        HebrewScript: typing.ClassVar[QLocale.Script]  # value = <Script.HebrewScript: 47>
        HiraganaScript: typing.ClassVar[QLocale.Script]  # value = <Script.HiraganaScript: 48>
        ImperialAramaicScript: typing.ClassVar[QLocale.Script]  # value = <Script.ImperialAramaicScript: 49>
        InscriptionalPahlaviScript: typing.ClassVar[QLocale.Script]  # value = <Script.InscriptionalPahlaviScript: 50>
        InscriptionalParthianScript: typing.ClassVar[QLocale.Script]  # value = <Script.InscriptionalParthianScript: 51>
        JamoScript: typing.ClassVar[QLocale.Script]  # value = <Script.JamoScript: 52>
        JapaneseScript: typing.ClassVar[QLocale.Script]  # value = <Script.JapaneseScript: 53>
        JavaneseScript: typing.ClassVar[QLocale.Script]  # value = <Script.JavaneseScript: 54>
        KaithiScript: typing.ClassVar[QLocale.Script]  # value = <Script.KaithiScript: 55>
        KannadaScript: typing.ClassVar[QLocale.Script]  # value = <Script.KannadaScript: 56>
        KatakanaScript: typing.ClassVar[QLocale.Script]  # value = <Script.KatakanaScript: 57>
        KayahLiScript: typing.ClassVar[QLocale.Script]  # value = <Script.KayahLiScript: 58>
        KharoshthiScript: typing.ClassVar[QLocale.Script]  # value = <Script.KharoshthiScript: 59>
        KhmerScript: typing.ClassVar[QLocale.Script]  # value = <Script.KhmerScript: 60>
        KhojkiScript: typing.ClassVar[QLocale.Script]  # value = <Script.KhojkiScript: 61>
        KhudawadiScript: typing.ClassVar[QLocale.Script]  # value = <Script.KhudawadiScript: 62>
        KoreanScript: typing.ClassVar[QLocale.Script]  # value = <Script.KoreanScript: 63>
        LannaScript: typing.ClassVar[QLocale.Script]  # value = <Script.LannaScript: 64>
        LaoScript: typing.ClassVar[QLocale.Script]  # value = <Script.LaoScript: 65>
        LatinScript: typing.ClassVar[QLocale.Script]  # value = <Script.LatinScript: 66>
        LepchaScript: typing.ClassVar[QLocale.Script]  # value = <Script.LepchaScript: 67>
        LimbuScript: typing.ClassVar[QLocale.Script]  # value = <Script.LimbuScript: 68>
        LinearAScript: typing.ClassVar[QLocale.Script]  # value = <Script.LinearAScript: 69>
        LinearBScript: typing.ClassVar[QLocale.Script]  # value = <Script.LinearBScript: 70>
        LycianScript: typing.ClassVar[QLocale.Script]  # value = <Script.LycianScript: 71>
        LydianScript: typing.ClassVar[QLocale.Script]  # value = <Script.LydianScript: 72>
        MahajaniScript: typing.ClassVar[QLocale.Script]  # value = <Script.MahajaniScript: 73>
        MalayalamScript: typing.ClassVar[QLocale.Script]  # value = <Script.MalayalamScript: 74>
        MandaeanScript: typing.ClassVar[QLocale.Script]  # value = <Script.MandaeanScript: 75>
        ManichaeanScript: typing.ClassVar[QLocale.Script]  # value = <Script.ManichaeanScript: 76>
        MarchenScript: typing.ClassVar[QLocale.Script]  # value = <Script.MarchenScript: 77>
        MeiteiMayekScript: typing.ClassVar[QLocale.Script]  # value = <Script.MeiteiMayekScript: 78>
        MendeKikakuiScript: typing.ClassVar[QLocale.Script]  # value = <Script.MendeKikakuiScript: 79>
        MeroiticCursiveScript: typing.ClassVar[QLocale.Script]  # value = <Script.MeroiticCursiveScript: 80>
        MeroiticScript: typing.ClassVar[QLocale.Script]  # value = <Script.MeroiticScript: 81>
        ModiScript: typing.ClassVar[QLocale.Script]  # value = <Script.ModiScript: 82>
        MongolianScript: typing.ClassVar[QLocale.Script]  # value = <Script.MongolianScript: 83>
        MroScript: typing.ClassVar[QLocale.Script]  # value = <Script.MroScript: 84>
        MultaniScript: typing.ClassVar[QLocale.Script]  # value = <Script.MultaniScript: 85>
        MyanmarScript: typing.ClassVar[QLocale.Script]  # value = <Script.MyanmarScript: 86>
        NabataeanScript: typing.ClassVar[QLocale.Script]  # value = <Script.NabataeanScript: 87>
        NewTaiLueScript: typing.ClassVar[QLocale.Script]  # value = <Script.NewTaiLueScript: 89>
        NewaScript: typing.ClassVar[QLocale.Script]  # value = <Script.NewaScript: 88>
        NkoScript: typing.ClassVar[QLocale.Script]  # value = <Script.NkoScript: 90>
        OghamScript: typing.ClassVar[QLocale.Script]  # value = <Script.OghamScript: 92>
        OlChikiScript: typing.ClassVar[QLocale.Script]  # value = <Script.OlChikiScript: 93>
        OldHungarianScript: typing.ClassVar[QLocale.Script]  # value = <Script.OldHungarianScript: 94>
        OldItalicScript: typing.ClassVar[QLocale.Script]  # value = <Script.OldItalicScript: 95>
        OldNorthArabianScript: typing.ClassVar[QLocale.Script]  # value = <Script.OldNorthArabianScript: 96>
        OldPermicScript: typing.ClassVar[QLocale.Script]  # value = <Script.OldPermicScript: 97>
        OldPersianScript: typing.ClassVar[QLocale.Script]  # value = <Script.OldPersianScript: 98>
        OldSouthArabianScript: typing.ClassVar[QLocale.Script]  # value = <Script.OldSouthArabianScript: 99>
        OriyaScript: typing.ClassVar[QLocale.Script]  # value = <Script.OriyaScript: 91>
        OrkhonScript: typing.ClassVar[QLocale.Script]  # value = <Script.OrkhonScript: 100>
        OsageScript: typing.ClassVar[QLocale.Script]  # value = <Script.OsageScript: 101>
        OsmanyaScript: typing.ClassVar[QLocale.Script]  # value = <Script.OsmanyaScript: 102>
        PahawhHmongScript: typing.ClassVar[QLocale.Script]  # value = <Script.PahawhHmongScript: 103>
        PalmyreneScript: typing.ClassVar[QLocale.Script]  # value = <Script.PalmyreneScript: 104>
        PauCinHauScript: typing.ClassVar[QLocale.Script]  # value = <Script.PauCinHauScript: 105>
        PhagsPaScript: typing.ClassVar[QLocale.Script]  # value = <Script.PhagsPaScript: 106>
        PhoenicianScript: typing.ClassVar[QLocale.Script]  # value = <Script.PhoenicianScript: 107>
        PollardPhoneticScript: typing.ClassVar[QLocale.Script]  # value = <Script.PollardPhoneticScript: 108>
        PsalterPahlaviScript: typing.ClassVar[QLocale.Script]  # value = <Script.PsalterPahlaviScript: 109>
        RejangScript: typing.ClassVar[QLocale.Script]  # value = <Script.RejangScript: 110>
        RunicScript: typing.ClassVar[QLocale.Script]  # value = <Script.RunicScript: 111>
        SamaritanScript: typing.ClassVar[QLocale.Script]  # value = <Script.SamaritanScript: 112>
        SaurashtraScript: typing.ClassVar[QLocale.Script]  # value = <Script.SaurashtraScript: 113>
        SharadaScript: typing.ClassVar[QLocale.Script]  # value = <Script.SharadaScript: 114>
        ShavianScript: typing.ClassVar[QLocale.Script]  # value = <Script.ShavianScript: 115>
        SiddhamScript: typing.ClassVar[QLocale.Script]  # value = <Script.SiddhamScript: 116>
        SignWritingScript: typing.ClassVar[QLocale.Script]  # value = <Script.SignWritingScript: 117>
        SimplifiedHanScript: typing.ClassVar[QLocale.Script]  # value = <Script.SimplifiedHanScript: 118>
        SinhalaScript: typing.ClassVar[QLocale.Script]  # value = <Script.SinhalaScript: 119>
        SoraSompengScript: typing.ClassVar[QLocale.Script]  # value = <Script.SoraSompengScript: 120>
        SundaneseScript: typing.ClassVar[QLocale.Script]  # value = <Script.SundaneseScript: 121>
        SylotiNagriScript: typing.ClassVar[QLocale.Script]  # value = <Script.SylotiNagriScript: 122>
        SyriacScript: typing.ClassVar[QLocale.Script]  # value = <Script.SyriacScript: 123>
        TagalogScript: typing.ClassVar[QLocale.Script]  # value = <Script.TagalogScript: 124>
        TagbanwaScript: typing.ClassVar[QLocale.Script]  # value = <Script.TagbanwaScript: 125>
        TaiLeScript: typing.ClassVar[QLocale.Script]  # value = <Script.TaiLeScript: 126>
        TaiVietScript: typing.ClassVar[QLocale.Script]  # value = <Script.TaiVietScript: 127>
        TakriScript: typing.ClassVar[QLocale.Script]  # value = <Script.TakriScript: 128>
        TamilScript: typing.ClassVar[QLocale.Script]  # value = <Script.TamilScript: 129>
        TangutScript: typing.ClassVar[QLocale.Script]  # value = <Script.TangutScript: 130>
        TeluguScript: typing.ClassVar[QLocale.Script]  # value = <Script.TeluguScript: 131>
        ThaanaScript: typing.ClassVar[QLocale.Script]  # value = <Script.ThaanaScript: 132>
        ThaiScript: typing.ClassVar[QLocale.Script]  # value = <Script.ThaiScript: 133>
        TibetanScript: typing.ClassVar[QLocale.Script]  # value = <Script.TibetanScript: 134>
        TifinaghScript: typing.ClassVar[QLocale.Script]  # value = <Script.TifinaghScript: 135>
        TirhutaScript: typing.ClassVar[QLocale.Script]  # value = <Script.TirhutaScript: 136>
        TraditionalHanScript: typing.ClassVar[QLocale.Script]  # value = <Script.TraditionalHanScript: 137>
        UgariticScript: typing.ClassVar[QLocale.Script]  # value = <Script.UgariticScript: 138>
        VaiScript: typing.ClassVar[QLocale.Script]  # value = <Script.VaiScript: 139>
        VarangKshitiScript: typing.ClassVar[QLocale.Script]  # value = <Script.VarangKshitiScript: 140>
        YiScript: typing.ClassVar[QLocale.Script]  # value = <Script.YiScript: 141>
    class TagSeparator(enum.Enum):
        Dash: typing.ClassVar[QLocale.TagSeparator]  # value = <TagSeparator.Dash: 45>
        Underscore: typing.ClassVar[QLocale.TagSeparator]  # value = <TagSeparator.Underscore: 95>
    DefaultTwoDigitBaseYear: typing.ClassVar[int] = 1900
    @staticmethod
    def amText(*args, **kwargs):
        ...
    @staticmethod
    def bcp47Name(*args, **kwargs):
        ...
    @staticmethod
    def c(*args, **kwargs):
        ...
    @staticmethod
    def codeToCountry(*args, **kwargs):
        ...
    @staticmethod
    def codeToLanguage(*args, **kwargs):
        ...
    @staticmethod
    def codeToScript(*args, **kwargs):
        ...
    @staticmethod
    def codeToTerritory(*args, **kwargs):
        ...
    @staticmethod
    def collation(*args, **kwargs):
        ...
    @staticmethod
    def country(*args, **kwargs):
        ...
    @staticmethod
    def countryToCode(*args, **kwargs):
        ...
    @staticmethod
    def countryToString(*args, **kwargs):
        ...
    @staticmethod
    def createSeparatedList(*args, **kwargs):
        ...
    @staticmethod
    def currencySymbol(*args, **kwargs):
        ...
    @staticmethod
    def dateFormat(*args, **kwargs):
        ...
    @staticmethod
    def dateTimeFormat(*args, **kwargs):
        ...
    @staticmethod
    def dayName(*args, **kwargs):
        ...
    @staticmethod
    def decimalPoint(*args, **kwargs):
        ...
    @staticmethod
    def exponential(*args, **kwargs):
        ...
    @staticmethod
    def firstDayOfWeek(*args, **kwargs):
        ...
    @staticmethod
    def formattedDataSize(*args, **kwargs):
        ...
    @staticmethod
    def groupSeparator(*args, **kwargs):
        ...
    @staticmethod
    def language(*args, **kwargs):
        ...
    @staticmethod
    def languageToCode(*args, **kwargs):
        ...
    @staticmethod
    def languageToString(*args, **kwargs):
        ...
    @staticmethod
    def matchingLocales(*args, **kwargs):
        ...
    @staticmethod
    def measurementSystem(*args, **kwargs):
        ...
    @staticmethod
    def monthName(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def nativeCountryName(*args, **kwargs):
        ...
    @staticmethod
    def nativeLanguageName(*args, **kwargs):
        ...
    @staticmethod
    def nativeTerritoryName(*args, **kwargs):
        ...
    @staticmethod
    def negativeSign(*args, **kwargs):
        ...
    @staticmethod
    def numberOptions(*args, **kwargs):
        ...
    @staticmethod
    def percent(*args, **kwargs):
        ...
    @staticmethod
    def pmText(*args, **kwargs):
        ...
    @staticmethod
    def positiveSign(*args, **kwargs):
        ...
    @staticmethod
    def quoteString(*args, **kwargs):
        ...
    @staticmethod
    def script(*args, **kwargs):
        ...
    @staticmethod
    def scriptToCode(*args, **kwargs):
        ...
    @staticmethod
    def scriptToString(*args, **kwargs):
        ...
    @staticmethod
    def setDefault(*args, **kwargs):
        ...
    @staticmethod
    def setNumberOptions(*args, **kwargs):
        ...
    @staticmethod
    def standaloneDayName(*args, **kwargs):
        ...
    @staticmethod
    def standaloneMonthName(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def system(*args, **kwargs):
        ...
    @staticmethod
    def territory(*args, **kwargs):
        ...
    @staticmethod
    def territoryToCode(*args, **kwargs):
        ...
    @staticmethod
    def territoryToString(*args, **kwargs):
        ...
    @staticmethod
    def textDirection(*args, **kwargs):
        ...
    @staticmethod
    def timeFormat(*args, **kwargs):
        ...
    @staticmethod
    def toCurrencyString(*args, **kwargs):
        ...
    @staticmethod
    def toDate(*args, **kwargs):
        ...
    @staticmethod
    def toDateTime(*args, **kwargs):
        ...
    @staticmethod
    def toDouble(*args, **kwargs):
        ...
    @staticmethod
    def toFloat(*args, **kwargs):
        ...
    @staticmethod
    def toInt(*args, **kwargs):
        ...
    @staticmethod
    def toLong(*args, **kwargs):
        ...
    @staticmethod
    def toLongLong(*args, **kwargs):
        ...
    @staticmethod
    def toLower(*args, **kwargs):
        ...
    @staticmethod
    def toShort(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    @staticmethod
    def toTime(*args, **kwargs):
        ...
    @staticmethod
    def toUInt(*args, **kwargs):
        ...
    @staticmethod
    def toULong(*args, **kwargs):
        ...
    @staticmethod
    def toULongLong(*args, **kwargs):
        ...
    @staticmethod
    def toUShort(*args, **kwargs):
        ...
    @staticmethod
    def toUpper(*args, **kwargs):
        ...
    @staticmethod
    def uiLanguages(*args, **kwargs):
        ...
    @staticmethod
    def weekdays(*args, **kwargs):
        ...
    @staticmethod
    def zeroDigit(*args, **kwargs):
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
class QLocationPermission(PyQt6.sip.simplewrapper):
    class Accuracy(enum.Enum):
        Approximate: typing.ClassVar[QLocationPermission.Accuracy]  # value = <Accuracy.Approximate: 0>
        Precise: typing.ClassVar[QLocationPermission.Accuracy]  # value = <Accuracy.Precise: 1>
    class Availability(enum.Enum):
        Always: typing.ClassVar[QLocationPermission.Availability]  # value = <Availability.Always: 1>
        WhenInUse: typing.ClassVar[QLocationPermission.Availability]  # value = <Availability.WhenInUse: 0>
    @staticmethod
    def accuracy(*args, **kwargs):
        ...
    @staticmethod
    def availability(*args, **kwargs):
        ...
    @staticmethod
    def setAccuracy(*args, **kwargs):
        ...
    @staticmethod
    def setAvailability(*args, **kwargs):
        ...
class QLockFile(PyQt6.sip.simplewrapper):
    class LockError(enum.Enum):
        LockFailedError: typing.ClassVar[QLockFile.LockError]  # value = <LockError.LockFailedError: 1>
        NoError: typing.ClassVar[QLockFile.LockError]  # value = <LockError.NoError: 0>
        PermissionError: typing.ClassVar[QLockFile.LockError]  # value = <LockError.PermissionError: 2>
        UnknownError: typing.ClassVar[QLockFile.LockError]  # value = <LockError.UnknownError: 3>
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def getLockInfo(*args, **kwargs):
        ...
    @staticmethod
    def isLocked(*args, **kwargs):
        ...
    @staticmethod
    def lock(*args, **kwargs):
        ...
    @staticmethod
    def removeStaleLockFile(*args, **kwargs):
        ...
    @staticmethod
    def setStaleLockTime(*args, **kwargs):
        ...
    @staticmethod
    def staleLockTime(*args, **kwargs):
        ...
    @staticmethod
    def tryLock(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QLoggingCategory(PyQt6.sip.simplewrapper):
    @staticmethod
    def categoryName(*args, **kwargs):
        ...
    @staticmethod
    def defaultCategory(*args, **kwargs):
        ...
    @staticmethod
    def isCriticalEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isDebugEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isInfoEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isWarningEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setFilterRules(*args, **kwargs):
        ...
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
        """
class QMargins(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def bottom(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def left(*args, **kwargs):
        ...
    @staticmethod
    def right(*args, **kwargs):
        ...
    @staticmethod
    def setBottom(*args, **kwargs):
        ...
    @staticmethod
    def setLeft(*args, **kwargs):
        ...
    @staticmethod
    def setRight(*args, **kwargs):
        ...
    @staticmethod
    def setTop(*args, **kwargs):
        ...
    @staticmethod
    def toMarginsF(*args, **kwargs):
        ...
    @staticmethod
    def top(*args, **kwargs):
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
    def __or__(self, value):
        """
        Return self|value.
        """
    def __pos__(self):
        """
        +self
        """
    def __radd__(self, value):
        """
        Return value+self.
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
class QMarginsF(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def bottom(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def left(*args, **kwargs):
        ...
    @staticmethod
    def right(*args, **kwargs):
        ...
    @staticmethod
    def setBottom(*args, **kwargs):
        ...
    @staticmethod
    def setLeft(*args, **kwargs):
        ...
    @staticmethod
    def setRight(*args, **kwargs):
        ...
    @staticmethod
    def setTop(*args, **kwargs):
        ...
    @staticmethod
    def toMargins(*args, **kwargs):
        ...
    @staticmethod
    def top(*args, **kwargs):
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
    def __or__(self, value):
        """
        Return self|value.
        """
    def __pos__(self):
        """
        +self
        """
    def __radd__(self, value):
        """
        Return value+self.
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
class QMessageAuthenticationCode(PyQt6.sip.simplewrapper):
    @staticmethod
    def addData(*args, **kwargs):
        ...
    @staticmethod
    def hash(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def result(*args, **kwargs):
        ...
    @staticmethod
    def setKey(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QMessageLogContext(PyQt6.sip.simplewrapper):
    pass
class QMessageLogger(PyQt6.sip.simplewrapper):
    @staticmethod
    def critical(*args, **kwargs):
        ...
    @staticmethod
    def debug(*args, **kwargs):
        ...
    @staticmethod
    def fatal(*args, **kwargs):
        ...
    @staticmethod
    def info(*args, **kwargs):
        ...
    @staticmethod
    def warning(*args, **kwargs):
        ...
class QMetaClassInfo(PyQt6.sip.simplewrapper):
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QMetaEnum(PyQt6.sip.simplewrapper):
    @staticmethod
    def enumName(*args, **kwargs):
        ...
    @staticmethod
    def isFlag(*args, **kwargs):
        ...
    @staticmethod
    def isScoped(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def keyCount(*args, **kwargs):
        ...
    @staticmethod
    def keyToValue(*args, **kwargs):
        ...
    @staticmethod
    def keysToValue(*args, **kwargs):
        ...
    @staticmethod
    def metaType(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def scope(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
    @staticmethod
    def valueToKey(*args, **kwargs):
        ...
    @staticmethod
    def valueToKeys(*args, **kwargs):
        ...
class QMetaMethod(PyQt6.sip.simplewrapper):
    class Access(enum.Enum):
        Private: typing.ClassVar[QMetaMethod.Access]  # value = <Access.Private: 0>
        Protected: typing.ClassVar[QMetaMethod.Access]  # value = <Access.Protected: 1>
        Public: typing.ClassVar[QMetaMethod.Access]  # value = <Access.Public: 2>
    class MethodType(enum.Enum):
        Constructor: typing.ClassVar[QMetaMethod.MethodType]  # value = <MethodType.Constructor: 3>
        Method: typing.ClassVar[QMetaMethod.MethodType]  # value = <MethodType.Method: 0>
        Signal: typing.ClassVar[QMetaMethod.MethodType]  # value = <MethodType.Signal: 1>
        Slot: typing.ClassVar[QMetaMethod.MethodType]  # value = <MethodType.Slot: 2>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def access(*args, **kwargs):
        ...
    @staticmethod
    def invoke(*args, **kwargs):
        ...
    @staticmethod
    def isConst(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def methodIndex(*args, **kwargs):
        ...
    @staticmethod
    def methodSignature(*args, **kwargs):
        ...
    @staticmethod
    def methodType(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def parameterCount(*args, **kwargs):
        ...
    @staticmethod
    def parameterMetaType(*args, **kwargs):
        ...
    @staticmethod
    def parameterNames(*args, **kwargs):
        ...
    @staticmethod
    def parameterType(*args, **kwargs):
        ...
    @staticmethod
    def parameterTypeName(*args, **kwargs):
        ...
    @staticmethod
    def parameterTypes(*args, **kwargs):
        ...
    @staticmethod
    def relativeMethodIndex(*args, **kwargs):
        ...
    @staticmethod
    def returnMetaType(*args, **kwargs):
        ...
    @staticmethod
    def returnType(*args, **kwargs):
        ...
    @staticmethod
    def revision(*args, **kwargs):
        ...
    @staticmethod
    def tag(*args, **kwargs):
        ...
    @staticmethod
    def typeName(*args, **kwargs):
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
class QMetaObject(PyQt6.sip.simplewrapper):
    class Connection(PyQt6.sip.simplewrapper):
        @staticmethod
        def swap(*args, **kwargs):
            ...
    @staticmethod
    def checkConnectArgs(*args, **kwargs):
        ...
    @staticmethod
    def classInfo(*args, **kwargs):
        ...
    @staticmethod
    def classInfoCount(*args, **kwargs):
        ...
    @staticmethod
    def classInfoOffset(*args, **kwargs):
        ...
    @staticmethod
    def className(*args, **kwargs):
        ...
    @staticmethod
    def connectSlotsByName(*args, **kwargs):
        ...
    @staticmethod
    def constructor(*args, **kwargs):
        ...
    @staticmethod
    def constructorCount(*args, **kwargs):
        ...
    @staticmethod
    def enumerator(*args, **kwargs):
        ...
    @staticmethod
    def enumeratorCount(*args, **kwargs):
        ...
    @staticmethod
    def enumeratorOffset(*args, **kwargs):
        ...
    @staticmethod
    def indexOfClassInfo(*args, **kwargs):
        ...
    @staticmethod
    def indexOfConstructor(*args, **kwargs):
        ...
    @staticmethod
    def indexOfEnumerator(*args, **kwargs):
        ...
    @staticmethod
    def indexOfMethod(*args, **kwargs):
        ...
    @staticmethod
    def indexOfProperty(*args, **kwargs):
        ...
    @staticmethod
    def indexOfSignal(*args, **kwargs):
        ...
    @staticmethod
    def indexOfSlot(*args, **kwargs):
        ...
    @staticmethod
    def inherits(*args, **kwargs):
        ...
    @staticmethod
    def invokeMethod(*args, **kwargs):
        ...
    @staticmethod
    def metaType(*args, **kwargs):
        ...
    @staticmethod
    def method(*args, **kwargs):
        ...
    @staticmethod
    def methodCount(*args, **kwargs):
        ...
    @staticmethod
    def methodOffset(*args, **kwargs):
        ...
    @staticmethod
    def newInstance(*args, **kwargs):
        ...
    @staticmethod
    def normalizedSignature(*args, **kwargs):
        ...
    @staticmethod
    def normalizedType(*args, **kwargs):
        ...
    @staticmethod
    def property(*args, **kwargs):
        ...
    @staticmethod
    def propertyCount(*args, **kwargs):
        ...
    @staticmethod
    def propertyOffset(*args, **kwargs):
        ...
    @staticmethod
    def superClass(*args, **kwargs):
        ...
    @staticmethod
    def userProperty(*args, **kwargs):
        ...
class QMetaProperty(PyQt6.sip.simplewrapper):
    @staticmethod
    def enumerator(*args, **kwargs):
        ...
    @staticmethod
    def hasNotifySignal(*args, **kwargs):
        ...
    @staticmethod
    def hasStdCppSet(*args, **kwargs):
        ...
    @staticmethod
    def isBindable(*args, **kwargs):
        ...
    @staticmethod
    def isConstant(*args, **kwargs):
        ...
    @staticmethod
    def isDesignable(*args, **kwargs):
        ...
    @staticmethod
    def isEnumType(*args, **kwargs):
        ...
    @staticmethod
    def isFinal(*args, **kwargs):
        ...
    @staticmethod
    def isFlagType(*args, **kwargs):
        ...
    @staticmethod
    def isReadable(*args, **kwargs):
        ...
    @staticmethod
    def isRequired(*args, **kwargs):
        ...
    @staticmethod
    def isResettable(*args, **kwargs):
        ...
    @staticmethod
    def isScriptable(*args, **kwargs):
        ...
    @staticmethod
    def isStored(*args, **kwargs):
        ...
    @staticmethod
    def isUser(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def isWritable(*args, **kwargs):
        ...
    @staticmethod
    def metaType(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def notifySignal(*args, **kwargs):
        ...
    @staticmethod
    def notifySignalIndex(*args, **kwargs):
        ...
    @staticmethod
    def propertyIndex(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def relativePropertyIndex(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def revision(*args, **kwargs):
        ...
    @staticmethod
    def typeId(*args, **kwargs):
        ...
    @staticmethod
    def typeName(*args, **kwargs):
        ...
    @staticmethod
    def userType(*args, **kwargs):
        ...
    @staticmethod
    def write(*args, **kwargs):
        ...
class QMetaType(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        Bool: typing.ClassVar[QMetaType.Type]  # value = <Type.Bool: 1>
        Char: typing.ClassVar[QMetaType.Type]  # value = <Type.Char: 34>
        Char16: typing.ClassVar[QMetaType.Type]  # value = <Type.Char16: 56>
        Char32: typing.ClassVar[QMetaType.Type]  # value = <Type.Char32: 57>
        Double: typing.ClassVar[QMetaType.Type]  # value = <Type.Double: 6>
        FirstGuiType: typing.ClassVar[QMetaType.Type]  # value = <Type.FirstGuiType: 4096>
        Float: typing.ClassVar[QMetaType.Type]  # value = <Type.Float: 38>
        Int: typing.ClassVar[QMetaType.Type]  # value = <Type.Int: 2>
        LastCoreType: typing.ClassVar[QMetaType.Type]  # value = <Type.LastCoreType: 63>
        Long: typing.ClassVar[QMetaType.Type]  # value = <Type.Long: 32>
        LongLong: typing.ClassVar[QMetaType.Type]  # value = <Type.LongLong: 4>
        QBitArray: typing.ClassVar[QMetaType.Type]  # value = <Type.QBitArray: 13>
        QBitmap: typing.ClassVar[QMetaType.Type]  # value = <Type.QBitmap: 4105>
        QBrush: typing.ClassVar[QMetaType.Type]  # value = <Type.QBrush: 4098>
        QByteArray: typing.ClassVar[QMetaType.Type]  # value = <Type.QByteArray: 12>
        QByteArrayList: typing.ClassVar[QMetaType.Type]  # value = <Type.QByteArrayList: 49>
        QCborArray: typing.ClassVar[QMetaType.Type]  # value = <Type.QCborArray: 54>
        QCborMap: typing.ClassVar[QMetaType.Type]  # value = <Type.QCborMap: 55>
        QCborSimpleType: typing.ClassVar[QMetaType.Type]  # value = <Type.QCborSimpleType: 52>
        QCborValue: typing.ClassVar[QMetaType.Type]  # value = <Type.QCborValue: 53>
        QChar: typing.ClassVar[QMetaType.Type]  # value = <Type.QChar: 7>
        QColor: typing.ClassVar[QMetaType.Type]  # value = <Type.QColor: 4099>
        QColorSpace: typing.ClassVar[QMetaType.Type]  # value = <Type.QColorSpace: 4119>
        QCursor: typing.ClassVar[QMetaType.Type]  # value = <Type.QCursor: 4106>
        QDate: typing.ClassVar[QMetaType.Type]  # value = <Type.QDate: 14>
        QDateTime: typing.ClassVar[QMetaType.Type]  # value = <Type.QDateTime: 16>
        QEasingCurve: typing.ClassVar[QMetaType.Type]  # value = <Type.QEasingCurve: 29>
        QIcon: typing.ClassVar[QMetaType.Type]  # value = <Type.QIcon: 4101>
        QImage: typing.ClassVar[QMetaType.Type]  # value = <Type.QImage: 4102>
        QJsonArray: typing.ClassVar[QMetaType.Type]  # value = <Type.QJsonArray: 47>
        QJsonDocument: typing.ClassVar[QMetaType.Type]  # value = <Type.QJsonDocument: 48>
        QJsonObject: typing.ClassVar[QMetaType.Type]  # value = <Type.QJsonObject: 46>
        QJsonValue: typing.ClassVar[QMetaType.Type]  # value = <Type.QJsonValue: 45>
        QKeySequence: typing.ClassVar[QMetaType.Type]  # value = <Type.QKeySequence: 4107>
        QLine: typing.ClassVar[QMetaType.Type]  # value = <Type.QLine: 23>
        QLineF: typing.ClassVar[QMetaType.Type]  # value = <Type.QLineF: 24>
        QLocale: typing.ClassVar[QMetaType.Type]  # value = <Type.QLocale: 18>
        QMatrix4x4: typing.ClassVar[QMetaType.Type]  # value = <Type.QMatrix4x4: 4113>
        QModelIndex: typing.ClassVar[QMetaType.Type]  # value = <Type.QModelIndex: 42>
        QObjectStar: typing.ClassVar[QMetaType.Type]  # value = <Type.QObjectStar: 39>
        QPalette: typing.ClassVar[QMetaType.Type]  # value = <Type.QPalette: 4100>
        QPen: typing.ClassVar[QMetaType.Type]  # value = <Type.QPen: 4108>
        QPersistentModelIndex: typing.ClassVar[QMetaType.Type]  # value = <Type.QPersistentModelIndex: 50>
        QPixmap: typing.ClassVar[QMetaType.Type]  # value = <Type.QPixmap: 4097>
        QPoint: typing.ClassVar[QMetaType.Type]  # value = <Type.QPoint: 25>
        QPointF: typing.ClassVar[QMetaType.Type]  # value = <Type.QPointF: 26>
        QPolygon: typing.ClassVar[QMetaType.Type]  # value = <Type.QPolygon: 4103>
        QPolygonF: typing.ClassVar[QMetaType.Type]  # value = <Type.QPolygonF: 4118>
        QQuaternion: typing.ClassVar[QMetaType.Type]  # value = <Type.QQuaternion: 4117>
        QRect: typing.ClassVar[QMetaType.Type]  # value = <Type.QRect: 19>
        QRectF: typing.ClassVar[QMetaType.Type]  # value = <Type.QRectF: 20>
        QRegion: typing.ClassVar[QMetaType.Type]  # value = <Type.QRegion: 4104>
        QRegularExpression: typing.ClassVar[QMetaType.Type]  # value = <Type.QRegularExpression: 44>
        QSize: typing.ClassVar[QMetaType.Type]  # value = <Type.QSize: 21>
        QSizeF: typing.ClassVar[QMetaType.Type]  # value = <Type.QSizeF: 22>
        QSizePolicy: typing.ClassVar[QMetaType.Type]  # value = <Type.QSizePolicy: 8192>
        QString: typing.ClassVar[QMetaType.Type]  # value = <Type.QString: 10>
        QStringList: typing.ClassVar[QMetaType.Type]  # value = <Type.QStringList: 11>
        QTextFormat: typing.ClassVar[QMetaType.Type]  # value = <Type.QTextFormat: 4110>
        QTextLength: typing.ClassVar[QMetaType.Type]  # value = <Type.QTextLength: 4109>
        QTime: typing.ClassVar[QMetaType.Type]  # value = <Type.QTime: 15>
        QTransform: typing.ClassVar[QMetaType.Type]  # value = <Type.QTransform: 4112>
        QUrl: typing.ClassVar[QMetaType.Type]  # value = <Type.QUrl: 17>
        QUuid: typing.ClassVar[QMetaType.Type]  # value = <Type.QUuid: 30>
        QVariant: typing.ClassVar[QMetaType.Type]  # value = <Type.QVariant: 41>
        QVariantHash: typing.ClassVar[QMetaType.Type]  # value = <Type.QVariantHash: 28>
        QVariantList: typing.ClassVar[QMetaType.Type]  # value = <Type.QVariantList: 9>
        QVariantMap: typing.ClassVar[QMetaType.Type]  # value = <Type.QVariantMap: 8>
        QVariantPair: typing.ClassVar[QMetaType.Type]  # value = <Type.QVariantPair: 58>
        QVector2D: typing.ClassVar[QMetaType.Type]  # value = <Type.QVector2D: 4114>
        QVector3D: typing.ClassVar[QMetaType.Type]  # value = <Type.QVector3D: 4115>
        QVector4D: typing.ClassVar[QMetaType.Type]  # value = <Type.QVector4D: 4116>
        SChar: typing.ClassVar[QMetaType.Type]  # value = <Type.SChar: 40>
        Short: typing.ClassVar[QMetaType.Type]  # value = <Type.Short: 33>
        UChar: typing.ClassVar[QMetaType.Type]  # value = <Type.UChar: 37>
        UInt: typing.ClassVar[QMetaType.Type]  # value = <Type.UInt: 3>
        ULong: typing.ClassVar[QMetaType.Type]  # value = <Type.ULong: 35>
        ULongLong: typing.ClassVar[QMetaType.Type]  # value = <Type.ULongLong: 5>
        UShort: typing.ClassVar[QMetaType.Type]  # value = <Type.UShort: 36>
        UnknownType: typing.ClassVar[QMetaType.Type]  # value = <Type.UnknownType: 0>
        User: typing.ClassVar[QMetaType.Type]  # value = <Type.User: 65536>
        Void: typing.ClassVar[QMetaType.Type]  # value = <Type.Void: 43>
        VoidStar: typing.ClassVar[QMetaType.Type]  # value = <Type.VoidStar: 31>
    class TypeFlag(enum.Flag):
        IsConst: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.IsConst: 8192>
        IsEnumeration: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.IsEnumeration: 16>
        IsPointer: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.IsPointer: 2048>
        IsQmlList: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.IsQmlList: 4096>
        IsUnsignedEnumeration: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.IsUnsignedEnumeration: 256>
        NeedsConstruction: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.NeedsConstruction: 1>
        NeedsCopyConstruction: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.NeedsCopyConstruction: 16384>
        NeedsDestruction: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.NeedsDestruction: 2>
        NeedsMoveConstruction: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.NeedsMoveConstruction: 32768>
        PointerToQObject: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.PointerToQObject: 8>
        RelocatableType: typing.ClassVar[QMetaType.TypeFlag]  # value = <TypeFlag.RelocatableType: 4>
    @staticmethod
    def alignOf(*args, **kwargs):
        ...
    @staticmethod
    def canConvert(*args, **kwargs):
        ...
    @staticmethod
    def canView(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def fromName(*args, **kwargs):
        ...
    @staticmethod
    def hasRegisteredDataStreamOperators(*args, **kwargs):
        ...
    @staticmethod
    def hasRegisteredDebugStreamOperator(*args, **kwargs):
        ...
    @staticmethod
    def id(*args, **kwargs):
        ...
    @staticmethod
    def isCopyConstructible(*args, **kwargs):
        ...
    @staticmethod
    def isDefaultConstructible(*args, **kwargs):
        ...
    @staticmethod
    def isDestructible(*args, **kwargs):
        ...
    @staticmethod
    def isEqualityComparable(*args, **kwargs):
        ...
    @staticmethod
    def isMoveConstructible(*args, **kwargs):
        ...
    @staticmethod
    def isOrdered(*args, **kwargs):
        ...
    @staticmethod
    def isRegistered(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def registerType(*args, **kwargs):
        ...
    @staticmethod
    def sizeOf(*args, **kwargs):
        ...
    @staticmethod
    def underlyingType(*args, **kwargs):
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
class QMicrophonePermission(PyQt6.sip.simplewrapper):
    pass
class QMimeData(QObject):
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def colorData(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def formats(*args, **kwargs):
        ...
    @staticmethod
    def hasColor(*args, **kwargs):
        ...
    @staticmethod
    def hasFormat(*args, **kwargs):
        ...
    @staticmethod
    def hasHtml(*args, **kwargs):
        ...
    @staticmethod
    def hasImage(*args, **kwargs):
        ...
    @staticmethod
    def hasText(*args, **kwargs):
        ...
    @staticmethod
    def hasUrls(*args, **kwargs):
        ...
    @staticmethod
    def html(*args, **kwargs):
        ...
    @staticmethod
    def imageData(*args, **kwargs):
        ...
    @staticmethod
    def removeFormat(*args, **kwargs):
        ...
    @staticmethod
    def retrieveData(*args, **kwargs):
        ...
    @staticmethod
    def setColorData(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setHtml(*args, **kwargs):
        ...
    @staticmethod
    def setImageData(*args, **kwargs):
        ...
    @staticmethod
    def setText(*args, **kwargs):
        ...
    @staticmethod
    def setUrls(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def urls(*args, **kwargs):
        ...
class QMimeDatabase(PyQt6.sip.simplewrapper):
    class MatchMode(enum.Enum):
        MatchContent: typing.ClassVar[QMimeDatabase.MatchMode]  # value = <MatchMode.MatchContent: 2>
        MatchDefault: typing.ClassVar[QMimeDatabase.MatchMode]  # value = <MatchMode.MatchDefault: 0>
        MatchExtension: typing.ClassVar[QMimeDatabase.MatchMode]  # value = <MatchMode.MatchExtension: 1>
    @staticmethod
    def allMimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypeForData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypeForFile(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypeForFileNameAndData(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypeForName(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypeForUrl(*args, **kwargs):
        ...
    @staticmethod
    def mimeTypesForFileName(*args, **kwargs):
        ...
    @staticmethod
    def suffixForFileName(*args, **kwargs):
        ...
class QMimeType(PyQt6.sip.simplewrapper):
    @staticmethod
    def aliases(*args, **kwargs):
        ...
    @staticmethod
    def allAncestors(*args, **kwargs):
        ...
    @staticmethod
    def comment(*args, **kwargs):
        ...
    @staticmethod
    def filterString(*args, **kwargs):
        ...
    @staticmethod
    def genericIconName(*args, **kwargs):
        ...
    @staticmethod
    def globPatterns(*args, **kwargs):
        ...
    @staticmethod
    def iconName(*args, **kwargs):
        ...
    @staticmethod
    def inherits(*args, **kwargs):
        ...
    @staticmethod
    def isDefault(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def parentMimeTypes(*args, **kwargs):
        ...
    @staticmethod
    def preferredSuffix(*args, **kwargs):
        ...
    @staticmethod
    def suffixes(*args, **kwargs):
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
class QModelIndex(PyQt6.sip.simplewrapper):
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
    def internalId(*args, **kwargs):
        ...
    @staticmethod
    def internalPointer(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
    @staticmethod
    def siblingAtColumn(*args, **kwargs):
        ...
    @staticmethod
    def siblingAtRow(*args, **kwargs):
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
class QModelRoleData(PyQt6.sip.simplewrapper):
    @staticmethod
    def clearData(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def role(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
class QModelRoleDataSpan(PyQt6.sip.simplewrapper):
    @staticmethod
    def begin(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def dataForRole(*args, **kwargs):
        ...
    @staticmethod
    def end(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __len__(self):
        """
        Return len(self).
        """
class QMutex(PyQt6.sip.simplewrapper):
    @staticmethod
    def lock(*args, **kwargs):
        ...
    @staticmethod
    def tryLock(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QMutexLocker(PyQt6.sip.simplewrapper):
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def mutex(*args, **kwargs):
        ...
    @staticmethod
    def relock(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QNativeIpcKey(PyQt6.sip.simplewrapper):
    class Type(enum.Enum):
        PosixRealtime: typing.ClassVar[QNativeIpcKey.Type]  # value = <Type.PosixRealtime: 256>
        SystemV: typing.ClassVar[QNativeIpcKey.Type]  # value = <Type.SystemV: 81>
        Windows: typing.ClassVar[QNativeIpcKey.Type]  # value = <Type.Windows: 257>
    DefaultTypeForOs: typing.ClassVar[QNativeIpcKey.Type]  # value = <Type.PosixRealtime: 256>
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def legacyDefaultTypeForOs(*args, **kwargs):
        ...
    @staticmethod
    def nativeKey(*args, **kwargs):
        ...
    @staticmethod
    def setNativeKey(*args, **kwargs):
        ...
    @staticmethod
    def setType(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
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
class QObject(PyQt6.sip.wrapper):
    staticMetaObject: typing.ClassVar[QMetaObject]  # value = <PyQt6.QtCore.QMetaObject object>
    @staticmethod
    def __getattr__(*args, **kwargs):
        ...
    @staticmethod
    def blockSignals(*args, **kwargs):
        ...
    @staticmethod
    def childEvent(*args, **kwargs):
        ...
    @staticmethod
    def children(*args, **kwargs):
        ...
    @staticmethod
    def connectNotify(*args, **kwargs):
        ...
    @staticmethod
    def customEvent(*args, **kwargs):
        ...
    @staticmethod
    def deleteLater(*args, **kwargs):
        ...
    @staticmethod
    def destroyed(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def disconnect(*args, **kwargs):
        ...
    @staticmethod
    def disconnectNotify(*args, **kwargs):
        ...
    @staticmethod
    def dumpObjectInfo(*args, **kwargs):
        ...
    @staticmethod
    def dumpObjectTree(*args, **kwargs):
        ...
    @staticmethod
    def dynamicPropertyNames(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventFilter(*args, **kwargs):
        ...
    @staticmethod
    def findChild(*args, **kwargs):
        ...
    @staticmethod
    def findChildren(*args, **kwargs):
        ...
    @staticmethod
    def inherits(*args, **kwargs):
        ...
    @staticmethod
    def installEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def isQuickItemType(*args, **kwargs):
        ...
    @staticmethod
    def isSignalConnected(*args, **kwargs):
        ...
    @staticmethod
    def isWidgetType(*args, **kwargs):
        ...
    @staticmethod
    def isWindowType(*args, **kwargs):
        ...
    @staticmethod
    def killTimer(*args, **kwargs):
        ...
    @staticmethod
    def metaObject(*args, **kwargs):
        ...
    @staticmethod
    def moveToThread(*args, **kwargs):
        ...
    @staticmethod
    def objectName(*args, **kwargs):
        ...
    @staticmethod
    def objectNameChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def property(*args, **kwargs):
        ...
    @staticmethod
    def pyqtConfigure(*args, **kwargs):
        """
        QObject.pyqtConfigure(...)
        
        Each keyword argument is either the name of a Qt property or a Qt signal.
        For properties the property is set to the given value which should be of an
        appropriate type.
        For signals the signal is connected to the given value which should be a
        callable.
        """
    @staticmethod
    def receivers(*args, **kwargs):
        ...
    @staticmethod
    def removeEventFilter(*args, **kwargs):
        ...
    @staticmethod
    def sender(*args, **kwargs):
        ...
    @staticmethod
    def senderSignalIndex(*args, **kwargs):
        ...
    @staticmethod
    def setObjectName(*args, **kwargs):
        ...
    @staticmethod
    def setParent(*args, **kwargs):
        ...
    @staticmethod
    def setProperty(*args, **kwargs):
        ...
    @staticmethod
    def signalsBlocked(*args, **kwargs):
        ...
    @staticmethod
    def startTimer(*args, **kwargs):
        ...
    @staticmethod
    def thread(*args, **kwargs):
        ...
    @staticmethod
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def tr(*args, **kwargs):
        ...
class QObjectCleanupHandler(QObject):
    @staticmethod
    def add(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
class QOperatingSystemVersion(QOperatingSystemVersionBase):
    class OSType(enum.Enum):
        Android: typing.ClassVar[QOperatingSystemVersion.OSType]  # value = <OSType.Android: 6>
        IOS: typing.ClassVar[QOperatingSystemVersion.OSType]  # value = <OSType.IOS: 3>
        MacOS: typing.ClassVar[QOperatingSystemVersion.OSType]  # value = <OSType.MacOS: 2>
        TvOS: typing.ClassVar[QOperatingSystemVersion.OSType]  # value = <OSType.TvOS: 4>
        Unknown: typing.ClassVar[QOperatingSystemVersion.OSType]  # value = <OSType.Unknown: 0>
        WatchOS: typing.ClassVar[QOperatingSystemVersion.OSType]  # value = <OSType.WatchOS: 5>
        Windows: typing.ClassVar[QOperatingSystemVersion.OSType]  # value = <OSType.Windows: 1>
    Android10: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    Android11: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    Android12: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Android12L: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Android13: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    AndroidJellyBean: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidJellyBean_MR1: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidJellyBean_MR2: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidKitKat: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidLollipop: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidLollipop_MR1: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidMarshmallow: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidNougat: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidNougat_MR1: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidOreo: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidOreo_MR1: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    AndroidPie: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    MacOSBigSur: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    MacOSCatalina: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    MacOSHighSierra: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    MacOSMojave: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    MacOSMonterey: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    MacOSSierra: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    MacOSSonoma: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    MacOSVentura: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    OSXElCapitan: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    OSXMavericks: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    OSXYosemite: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    Windows10: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    Windows10_1809: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows10_1903: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows10_1909: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows10_2004: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows10_20H2: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows10_21H1: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows10_21H2: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows10_22H2: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows11: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows11_21H2: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows11_22H2: typing.ClassVar[QOperatingSystemVersionBase]  # value = <PyQt6.QtCore.QOperatingSystemVersionBase object>
    Windows7: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    Windows8: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    Windows8_1: typing.ClassVar[QOperatingSystemVersion]  # value = <PyQt6.QtCore.QOperatingSystemVersion object>
    @staticmethod
    def current(*args, **kwargs):
        ...
    @staticmethod
    def currentType(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QOperatingSystemVersionBase(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def majorVersion(*args, **kwargs):
        ...
    @staticmethod
    def microVersion(*args, **kwargs):
        ...
    @staticmethod
    def minorVersion(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def segmentCount(*args, **kwargs):
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
class QParallelAnimationGroup(QAnimationGroup):
    @staticmethod
    def duration(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def updateCurrentTime(*args, **kwargs):
        ...
    @staticmethod
    def updateDirection(*args, **kwargs):
        ...
    @staticmethod
    def updateState(*args, **kwargs):
        ...
class QPauseAnimation(QAbstractAnimation):
    @staticmethod
    def duration(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def setDuration(*args, **kwargs):
        ...
    @staticmethod
    def updateCurrentTime(*args, **kwargs):
        ...
class QPermission(PyQt6.sip.simplewrapper):
    @staticmethod
    def status(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QPersistentModelIndex(PyQt6.sip.simplewrapper):
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
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def model(*args, **kwargs):
        ...
    @staticmethod
    def parent(*args, **kwargs):
        ...
    @staticmethod
    def row(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
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
class QPluginLoader(QObject):
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def instance(*args, **kwargs):
        ...
    @staticmethod
    def isLoaded(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def loadHints(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setLoadHints(*args, **kwargs):
        ...
    @staticmethod
    def staticInstances(*args, **kwargs):
        ...
    @staticmethod
    def unload(*args, **kwargs):
        ...
class QPoint(PyQt6.sip.simplewrapper):
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def dotProduct(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def manhattanLength(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def toPointF(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
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
    def __bool__(self):
        """
        True if self else False
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
    def __pos__(self):
        """
        +self
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
class QPointF(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def dotProduct(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def manhattanLength(*args, **kwargs):
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
    def transposed(*args, **kwargs):
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
    def __bool__(self):
        """
        True if self else False
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
    def __pos__(self):
        """
        +self
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
class QProcess(QIODevice):
    class ExitStatus(enum.Enum):
        CrashExit: typing.ClassVar[QProcess.ExitStatus]  # value = <ExitStatus.CrashExit: 1>
        NormalExit: typing.ClassVar[QProcess.ExitStatus]  # value = <ExitStatus.NormalExit: 0>
    class InputChannelMode(enum.Enum):
        ForwardedInputChannel: typing.ClassVar[QProcess.InputChannelMode]  # value = <InputChannelMode.ForwardedInputChannel: 1>
        ManagedInputChannel: typing.ClassVar[QProcess.InputChannelMode]  # value = <InputChannelMode.ManagedInputChannel: 0>
    class ProcessChannel(enum.Enum):
        StandardError: typing.ClassVar[QProcess.ProcessChannel]  # value = <ProcessChannel.StandardError: 1>
        StandardOutput: typing.ClassVar[QProcess.ProcessChannel]  # value = <ProcessChannel.StandardOutput: 0>
    class ProcessChannelMode(enum.Enum):
        ForwardedChannels: typing.ClassVar[QProcess.ProcessChannelMode]  # value = <ProcessChannelMode.ForwardedChannels: 2>
        ForwardedErrorChannel: typing.ClassVar[QProcess.ProcessChannelMode]  # value = <ProcessChannelMode.ForwardedErrorChannel: 4>
        ForwardedOutputChannel: typing.ClassVar[QProcess.ProcessChannelMode]  # value = <ProcessChannelMode.ForwardedOutputChannel: 3>
        MergedChannels: typing.ClassVar[QProcess.ProcessChannelMode]  # value = <ProcessChannelMode.MergedChannels: 1>
        SeparateChannels: typing.ClassVar[QProcess.ProcessChannelMode]  # value = <ProcessChannelMode.SeparateChannels: 0>
    class ProcessError(enum.Enum):
        Crashed: typing.ClassVar[QProcess.ProcessError]  # value = <ProcessError.Crashed: 1>
        FailedToStart: typing.ClassVar[QProcess.ProcessError]  # value = <ProcessError.FailedToStart: 0>
        ReadError: typing.ClassVar[QProcess.ProcessError]  # value = <ProcessError.ReadError: 3>
        Timedout: typing.ClassVar[QProcess.ProcessError]  # value = <ProcessError.Timedout: 2>
        UnknownError: typing.ClassVar[QProcess.ProcessError]  # value = <ProcessError.UnknownError: 5>
        WriteError: typing.ClassVar[QProcess.ProcessError]  # value = <ProcessError.WriteError: 4>
    class ProcessState(enum.Enum):
        NotRunning: typing.ClassVar[QProcess.ProcessState]  # value = <ProcessState.NotRunning: 0>
        Running: typing.ClassVar[QProcess.ProcessState]  # value = <ProcessState.Running: 2>
        Starting: typing.ClassVar[QProcess.ProcessState]  # value = <ProcessState.Starting: 1>
    class UnixProcessFlag(enum.Enum):
        CloseFileDescriptors: typing.ClassVar[QProcess.UnixProcessFlag]  # value = <UnixProcessFlag.CloseFileDescriptors: 16>
        CreateNewSession: typing.ClassVar[QProcess.UnixProcessFlag]  # value = <UnixProcessFlag.CreateNewSession: 64>
        DisconnectControllingTerminal: typing.ClassVar[QProcess.UnixProcessFlag]  # value = <UnixProcessFlag.DisconnectControllingTerminal: 128>
        IgnoreSigPipe: typing.ClassVar[QProcess.UnixProcessFlag]  # value = <UnixProcessFlag.IgnoreSigPipe: 2>
        ResetIds: typing.ClassVar[QProcess.UnixProcessFlag]  # value = <UnixProcessFlag.ResetIds: 256>
        ResetSignalHandlers: typing.ClassVar[QProcess.UnixProcessFlag]  # value = <UnixProcessFlag.ResetSignalHandlers: 1>
        UseVFork: typing.ClassVar[QProcess.UnixProcessFlag]  # value = <UnixProcessFlag.UseVFork: 32>
    class UnixProcessParameters(PyQt6.sip.simplewrapper):
        pass
    @staticmethod
    def arguments(*args, **kwargs):
        ...
    @staticmethod
    def bytesToWrite(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def closeReadChannel(*args, **kwargs):
        ...
    @staticmethod
    def closeWriteChannel(*args, **kwargs):
        ...
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
    def execute(*args, **kwargs):
        ...
    @staticmethod
    def exitCode(*args, **kwargs):
        ...
    @staticmethod
    def exitStatus(*args, **kwargs):
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
    def inputChannelMode(*args, **kwargs):
        ...
    @staticmethod
    def isSequential(*args, **kwargs):
        ...
    @staticmethod
    def kill(*args, **kwargs):
        ...
    @staticmethod
    def nullDevice(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def processChannelMode(*args, **kwargs):
        ...
    @staticmethod
    def processEnvironment(*args, **kwargs):
        ...
    @staticmethod
    def processId(*args, **kwargs):
        ...
    @staticmethod
    def program(*args, **kwargs):
        ...
    @staticmethod
    def readAllStandardError(*args, **kwargs):
        ...
    @staticmethod
    def readAllStandardOutput(*args, **kwargs):
        ...
    @staticmethod
    def readChannel(*args, **kwargs):
        ...
    @staticmethod
    def readData(*args, **kwargs):
        ...
    @staticmethod
    def readyReadStandardError(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def readyReadStandardOutput(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def setArguments(*args, **kwargs):
        ...
    @staticmethod
    def setInputChannelMode(*args, **kwargs):
        ...
    @staticmethod
    def setProcessChannelMode(*args, **kwargs):
        ...
    @staticmethod
    def setProcessEnvironment(*args, **kwargs):
        ...
    @staticmethod
    def setProcessState(*args, **kwargs):
        ...
    @staticmethod
    def setProgram(*args, **kwargs):
        ...
    @staticmethod
    def setReadChannel(*args, **kwargs):
        ...
    @staticmethod
    def setStandardErrorFile(*args, **kwargs):
        ...
    @staticmethod
    def setStandardInputFile(*args, **kwargs):
        ...
    @staticmethod
    def setStandardOutputFile(*args, **kwargs):
        ...
    @staticmethod
    def setStandardOutputProcess(*args, **kwargs):
        ...
    @staticmethod
    def setUnixProcessParameters(*args, **kwargs):
        ...
    @staticmethod
    def setWorkingDirectory(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
    @staticmethod
    def startCommand(*args, **kwargs):
        ...
    @staticmethod
    def startDetached(*args, **kwargs):
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
    def systemEnvironment(*args, **kwargs):
        ...
    @staticmethod
    def terminate(*args, **kwargs):
        ...
    @staticmethod
    def unixProcessParameters(*args, **kwargs):
        ...
    @staticmethod
    def waitForBytesWritten(*args, **kwargs):
        ...
    @staticmethod
    def waitForFinished(*args, **kwargs):
        ...
    @staticmethod
    def waitForReadyRead(*args, **kwargs):
        ...
    @staticmethod
    def waitForStarted(*args, **kwargs):
        ...
    @staticmethod
    def workingDirectory(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QProcessEnvironment(PyQt6.sip.simplewrapper):
    class Initialization(enum.Enum):
        InheritFromParent: typing.ClassVar[QProcessEnvironment.Initialization]  # value = <Initialization.InheritFromParent: 0>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def inheritsFromParent(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def keys(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def systemEnvironment(*args, **kwargs):
        ...
    @staticmethod
    def toStringList(*args, **kwargs):
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
class QPropertyAnimation(QVariantAnimation):
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def propertyName(*args, **kwargs):
        ...
    @staticmethod
    def setPropertyName(*args, **kwargs):
        ...
    @staticmethod
    def setTargetObject(*args, **kwargs):
        ...
    @staticmethod
    def targetObject(*args, **kwargs):
        ...
    @staticmethod
    def updateCurrentValue(*args, **kwargs):
        ...
    @staticmethod
    def updateState(*args, **kwargs):
        ...
class QRandomGenerator(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def bounded(*args, **kwargs):
        ...
    @staticmethod
    def discard(*args, **kwargs):
        ...
    @staticmethod
    def generate(*args, **kwargs):
        ...
    @staticmethod
    def generate64(*args, **kwargs):
        ...
    @staticmethod
    def generateDouble(*args, **kwargs):
        ...
    @staticmethod
    def global_(*args, **kwargs):
        ...
    @staticmethod
    def max(*args, **kwargs):
        ...
    @staticmethod
    def min(*args, **kwargs):
        ...
    @staticmethod
    def securelySeeded(*args, **kwargs):
        ...
    @staticmethod
    def seed(*args, **kwargs):
        ...
    @staticmethod
    def system(*args, **kwargs):
        ...
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
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
class QReadLocker(PyQt6.sip.simplewrapper):
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def readWriteLock(*args, **kwargs):
        ...
    @staticmethod
    def relock(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QReadWriteLock(PyQt6.sip.simplewrapper):
    class RecursionMode(enum.Enum):
        NonRecursive: typing.ClassVar[QReadWriteLock.RecursionMode]  # value = <RecursionMode.NonRecursive: 0>
        Recursive: typing.ClassVar[QReadWriteLock.RecursionMode]  # value = <RecursionMode.Recursive: 1>
    @staticmethod
    def lockForRead(*args, **kwargs):
        ...
    @staticmethod
    def lockForWrite(*args, **kwargs):
        ...
    @staticmethod
    def tryLockForRead(*args, **kwargs):
        ...
    @staticmethod
    def tryLockForWrite(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QRect(PyQt6.sip.simplewrapper):
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def adjust(*args, **kwargs):
        ...
    @staticmethod
    def adjusted(*args, **kwargs):
        ...
    @staticmethod
    def bottom(*args, **kwargs):
        ...
    @staticmethod
    def bottomLeft(*args, **kwargs):
        ...
    @staticmethod
    def bottomRight(*args, **kwargs):
        ...
    @staticmethod
    def center(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def getCoords(*args, **kwargs):
        ...
    @staticmethod
    def getRect(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
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
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def left(*args, **kwargs):
        ...
    @staticmethod
    def marginsAdded(*args, **kwargs):
        ...
    @staticmethod
    def marginsRemoved(*args, **kwargs):
        ...
    @staticmethod
    def moveBottom(*args, **kwargs):
        ...
    @staticmethod
    def moveBottomLeft(*args, **kwargs):
        ...
    @staticmethod
    def moveBottomRight(*args, **kwargs):
        ...
    @staticmethod
    def moveCenter(*args, **kwargs):
        ...
    @staticmethod
    def moveLeft(*args, **kwargs):
        ...
    @staticmethod
    def moveRight(*args, **kwargs):
        ...
    @staticmethod
    def moveTo(*args, **kwargs):
        ...
    @staticmethod
    def moveTop(*args, **kwargs):
        ...
    @staticmethod
    def moveTopLeft(*args, **kwargs):
        ...
    @staticmethod
    def moveTopRight(*args, **kwargs):
        ...
    @staticmethod
    def normalized(*args, **kwargs):
        ...
    @staticmethod
    def right(*args, **kwargs):
        ...
    @staticmethod
    def setBottom(*args, **kwargs):
        ...
    @staticmethod
    def setBottomLeft(*args, **kwargs):
        ...
    @staticmethod
    def setBottomRight(*args, **kwargs):
        ...
    @staticmethod
    def setCoords(*args, **kwargs):
        ...
    @staticmethod
    def setHeight(*args, **kwargs):
        ...
    @staticmethod
    def setLeft(*args, **kwargs):
        ...
    @staticmethod
    def setRect(*args, **kwargs):
        ...
    @staticmethod
    def setRight(*args, **kwargs):
        ...
    @staticmethod
    def setSize(*args, **kwargs):
        ...
    @staticmethod
    def setTop(*args, **kwargs):
        ...
    @staticmethod
    def setTopLeft(*args, **kwargs):
        ...
    @staticmethod
    def setTopRight(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def span(*args, **kwargs):
        ...
    @staticmethod
    def toRectF(*args, **kwargs):
        ...
    @staticmethod
    def top(*args, **kwargs):
        ...
    @staticmethod
    def topLeft(*args, **kwargs):
        ...
    @staticmethod
    def topRight(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    @staticmethod
    def united(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
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
    def __hash__(self):
        """
        Return hash(self).
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
    def __repr__(self):
        """
        Return repr(self).
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
class QRectF(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def adjust(*args, **kwargs):
        ...
    @staticmethod
    def adjusted(*args, **kwargs):
        ...
    @staticmethod
    def bottom(*args, **kwargs):
        ...
    @staticmethod
    def bottomLeft(*args, **kwargs):
        ...
    @staticmethod
    def bottomRight(*args, **kwargs):
        ...
    @staticmethod
    def center(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def getCoords(*args, **kwargs):
        ...
    @staticmethod
    def getRect(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
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
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def left(*args, **kwargs):
        ...
    @staticmethod
    def marginsAdded(*args, **kwargs):
        ...
    @staticmethod
    def marginsRemoved(*args, **kwargs):
        ...
    @staticmethod
    def moveBottom(*args, **kwargs):
        ...
    @staticmethod
    def moveBottomLeft(*args, **kwargs):
        ...
    @staticmethod
    def moveBottomRight(*args, **kwargs):
        ...
    @staticmethod
    def moveCenter(*args, **kwargs):
        ...
    @staticmethod
    def moveLeft(*args, **kwargs):
        ...
    @staticmethod
    def moveRight(*args, **kwargs):
        ...
    @staticmethod
    def moveTo(*args, **kwargs):
        ...
    @staticmethod
    def moveTop(*args, **kwargs):
        ...
    @staticmethod
    def moveTopLeft(*args, **kwargs):
        ...
    @staticmethod
    def moveTopRight(*args, **kwargs):
        ...
    @staticmethod
    def normalized(*args, **kwargs):
        ...
    @staticmethod
    def right(*args, **kwargs):
        ...
    @staticmethod
    def setBottom(*args, **kwargs):
        ...
    @staticmethod
    def setBottomLeft(*args, **kwargs):
        ...
    @staticmethod
    def setBottomRight(*args, **kwargs):
        ...
    @staticmethod
    def setCoords(*args, **kwargs):
        ...
    @staticmethod
    def setHeight(*args, **kwargs):
        ...
    @staticmethod
    def setLeft(*args, **kwargs):
        ...
    @staticmethod
    def setRect(*args, **kwargs):
        ...
    @staticmethod
    def setRight(*args, **kwargs):
        ...
    @staticmethod
    def setSize(*args, **kwargs):
        ...
    @staticmethod
    def setTop(*args, **kwargs):
        ...
    @staticmethod
    def setTopLeft(*args, **kwargs):
        ...
    @staticmethod
    def setTopRight(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def setX(*args, **kwargs):
        ...
    @staticmethod
    def setY(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def toAlignedRect(*args, **kwargs):
        ...
    @staticmethod
    def toRect(*args, **kwargs):
        ...
    @staticmethod
    def top(*args, **kwargs):
        ...
    @staticmethod
    def topLeft(*args, **kwargs):
        ...
    @staticmethod
    def topRight(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
    @staticmethod
    def translated(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    @staticmethod
    def united(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
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
    def __repr__(self):
        """
        Return repr(self).
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
class QRecursiveMutex(PyQt6.sip.simplewrapper):
    @staticmethod
    def lock(*args, **kwargs):
        ...
    @staticmethod
    def tryLock(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QRegularExpression(PyQt6.sip.simplewrapper):
    class MatchOption(enum.Flag):
        AnchorAtOffsetMatchOption: typing.ClassVar[QRegularExpression.MatchOption]  # value = <MatchOption.AnchorAtOffsetMatchOption: 1>
        DontCheckSubjectStringMatchOption: typing.ClassVar[QRegularExpression.MatchOption]  # value = <MatchOption.DontCheckSubjectStringMatchOption: 2>
    class MatchType(enum.Enum):
        NoMatch: typing.ClassVar[QRegularExpression.MatchType]  # value = <MatchType.NoMatch: 3>
        NormalMatch: typing.ClassVar[QRegularExpression.MatchType]  # value = <MatchType.NormalMatch: 0>
        PartialPreferCompleteMatch: typing.ClassVar[QRegularExpression.MatchType]  # value = <MatchType.PartialPreferCompleteMatch: 1>
        PartialPreferFirstMatch: typing.ClassVar[QRegularExpression.MatchType]  # value = <MatchType.PartialPreferFirstMatch: 2>
    class PatternOption(enum.Flag):
        CaseInsensitiveOption: typing.ClassVar[QRegularExpression.PatternOption]  # value = <PatternOption.CaseInsensitiveOption: 1>
        DontCaptureOption: typing.ClassVar[QRegularExpression.PatternOption]  # value = <PatternOption.DontCaptureOption: 32>
        DotMatchesEverythingOption: typing.ClassVar[QRegularExpression.PatternOption]  # value = <PatternOption.DotMatchesEverythingOption: 2>
        ExtendedPatternSyntaxOption: typing.ClassVar[QRegularExpression.PatternOption]  # value = <PatternOption.ExtendedPatternSyntaxOption: 8>
        InvertedGreedinessOption: typing.ClassVar[QRegularExpression.PatternOption]  # value = <PatternOption.InvertedGreedinessOption: 16>
        MultilineOption: typing.ClassVar[QRegularExpression.PatternOption]  # value = <PatternOption.MultilineOption: 4>
        UseUnicodePropertiesOption: typing.ClassVar[QRegularExpression.PatternOption]  # value = <PatternOption.UseUnicodePropertiesOption: 64>
    class WildcardConversionOption(enum.Flag):
        NonPathWildcardConversion: typing.ClassVar[QRegularExpression.WildcardConversionOption]  # value = <WildcardConversionOption.NonPathWildcardConversion: 2>
        UnanchoredWildcardConversion: typing.ClassVar[QRegularExpression.WildcardConversionOption]  # value = <WildcardConversionOption.UnanchoredWildcardConversion: 1>
    @staticmethod
    def anchoredPattern(*args, **kwargs):
        ...
    @staticmethod
    def captureCount(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def escape(*args, **kwargs):
        ...
    @staticmethod
    def fromWildcard(*args, **kwargs):
        ...
    @staticmethod
    def globalMatch(*args, **kwargs):
        ...
    @staticmethod
    def globalMatchView(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def match(*args, **kwargs):
        ...
    @staticmethod
    def matchView(*args, **kwargs):
        ...
    @staticmethod
    def namedCaptureGroups(*args, **kwargs):
        ...
    @staticmethod
    def optimize(*args, **kwargs):
        ...
    @staticmethod
    def pattern(*args, **kwargs):
        ...
    @staticmethod
    def patternErrorOffset(*args, **kwargs):
        ...
    @staticmethod
    def patternOptions(*args, **kwargs):
        ...
    @staticmethod
    def setPattern(*args, **kwargs):
        ...
    @staticmethod
    def setPatternOptions(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def wildcardToRegularExpression(*args, **kwargs):
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
    def __repr__(self):
        """
        Return repr(self).
        """
class QRegularExpressionMatch(PyQt6.sip.simplewrapper):
    @staticmethod
    def captured(*args, **kwargs):
        ...
    @staticmethod
    def capturedEnd(*args, **kwargs):
        ...
    @staticmethod
    def capturedLength(*args, **kwargs):
        ...
    @staticmethod
    def capturedStart(*args, **kwargs):
        ...
    @staticmethod
    def capturedTexts(*args, **kwargs):
        ...
    @staticmethod
    def hasCaptured(*args, **kwargs):
        ...
    @staticmethod
    def hasMatch(*args, **kwargs):
        ...
    @staticmethod
    def hasPartialMatch(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastCapturedIndex(*args, **kwargs):
        ...
    @staticmethod
    def matchOptions(*args, **kwargs):
        ...
    @staticmethod
    def matchType(*args, **kwargs):
        ...
    @staticmethod
    def regularExpression(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QRegularExpressionMatchIterator(PyQt6.sip.simplewrapper):
    @staticmethod
    def hasNext(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def matchOptions(*args, **kwargs):
        ...
    @staticmethod
    def matchType(*args, **kwargs):
        ...
    @staticmethod
    def next(*args, **kwargs):
        ...
    @staticmethod
    def peekNext(*args, **kwargs):
        ...
    @staticmethod
    def regularExpression(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QResource(PyQt6.sip.simplewrapper):
    class Compression(enum.Enum):
        NoCompression: typing.ClassVar[QResource.Compression]  # value = <Compression.NoCompression: 0>
        ZlibCompression: typing.ClassVar[QResource.Compression]  # value = <Compression.ZlibCompression: 1>
        ZstdCompression: typing.ClassVar[QResource.Compression]  # value = <Compression.ZstdCompression: 2>
    @staticmethod
    def absoluteFilePath(*args, **kwargs):
        ...
    @staticmethod
    def children(*args, **kwargs):
        ...
    @staticmethod
    def compressionAlgorithm(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def isDir(*args, **kwargs):
        ...
    @staticmethod
    def isFile(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastModified(*args, **kwargs):
        ...
    @staticmethod
    def locale(*args, **kwargs):
        ...
    @staticmethod
    def registerResource(*args, **kwargs):
        ...
    @staticmethod
    def registerResourceData(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def setLocale(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def uncompressedData(*args, **kwargs):
        ...
    @staticmethod
    def uncompressedSize(*args, **kwargs):
        ...
    @staticmethod
    def unregisterResource(*args, **kwargs):
        ...
    @staticmethod
    def unregisterResourceData(*args, **kwargs):
        ...
class QRunnable(PyQt6.sip.wrapper):
    @staticmethod
    def autoDelete(*args, **kwargs):
        ...
    @staticmethod
    def create(*args, **kwargs):
        ...
    @staticmethod
    def run(*args, **kwargs):
        ...
    @staticmethod
    def setAutoDelete(*args, **kwargs):
        ...
class QSaveFile(QFileDevice):
    @staticmethod
    def cancelWriting(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def commit(*args, **kwargs):
        ...
    @staticmethod
    def directWriteFallback(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def setDirectWriteFallback(*args, **kwargs):
        ...
    @staticmethod
    def setFileName(*args, **kwargs):
        ...
    @staticmethod
    def writeData(*args, **kwargs):
        ...
class QSemaphore(PyQt6.sip.simplewrapper):
    @staticmethod
    def acquire(*args, **kwargs):
        ...
    @staticmethod
    def available(*args, **kwargs):
        ...
    @staticmethod
    def release(*args, **kwargs):
        ...
    @staticmethod
    def tryAcquire(*args, **kwargs):
        ...
class QSemaphoreReleaser(PyQt6.sip.simplewrapper):
    @staticmethod
    def cancel(*args, **kwargs):
        ...
    @staticmethod
    def semaphore(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QSequentialAnimationGroup(QAnimationGroup):
    @staticmethod
    def addPause(*args, **kwargs):
        ...
    @staticmethod
    def currentAnimation(*args, **kwargs):
        ...
    @staticmethod
    def currentAnimationChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def duration(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def insertPause(*args, **kwargs):
        ...
    @staticmethod
    def updateCurrentTime(*args, **kwargs):
        ...
    @staticmethod
    def updateDirection(*args, **kwargs):
        ...
    @staticmethod
    def updateState(*args, **kwargs):
        ...
class QSettings(QObject):
    class Format(enum.Enum):
        IniFormat: typing.ClassVar[QSettings.Format]  # value = <Format.IniFormat: 1>
        InvalidFormat: typing.ClassVar[QSettings.Format]  # value = <Format.InvalidFormat: 16>
        NativeFormat: typing.ClassVar[QSettings.Format]  # value = <Format.NativeFormat: 0>
    class Scope(enum.Enum):
        SystemScope: typing.ClassVar[QSettings.Scope]  # value = <Scope.SystemScope: 1>
        UserScope: typing.ClassVar[QSettings.Scope]  # value = <Scope.UserScope: 0>
    class Status(enum.Enum):
        AccessError: typing.ClassVar[QSettings.Status]  # value = <Status.AccessError: 1>
        FormatError: typing.ClassVar[QSettings.Status]  # value = <Status.FormatError: 2>
        NoError: typing.ClassVar[QSettings.Status]  # value = <Status.NoError: 0>
    @staticmethod
    def allKeys(*args, **kwargs):
        ...
    @staticmethod
    def applicationName(*args, **kwargs):
        ...
    @staticmethod
    def beginGroup(*args, **kwargs):
        ...
    @staticmethod
    def beginReadArray(*args, **kwargs):
        ...
    @staticmethod
    def beginWriteArray(*args, **kwargs):
        ...
    @staticmethod
    def childGroups(*args, **kwargs):
        ...
    @staticmethod
    def childKeys(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def defaultFormat(*args, **kwargs):
        ...
    @staticmethod
    def endArray(*args, **kwargs):
        ...
    @staticmethod
    def endGroup(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def fallbacksEnabled(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def format(*args, **kwargs):
        ...
    @staticmethod
    def group(*args, **kwargs):
        ...
    @staticmethod
    def isAtomicSyncRequired(*args, **kwargs):
        ...
    @staticmethod
    def isWritable(*args, **kwargs):
        ...
    @staticmethod
    def organizationName(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def scope(*args, **kwargs):
        ...
    @staticmethod
    def setArrayIndex(*args, **kwargs):
        ...
    @staticmethod
    def setAtomicSyncRequired(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultFormat(*args, **kwargs):
        ...
    @staticmethod
    def setFallbacksEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setPath(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def status(*args, **kwargs):
        ...
    @staticmethod
    def sync(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QSharedMemory(QObject):
    class AccessMode(enum.Enum):
        ReadOnly: typing.ClassVar[QSharedMemory.AccessMode]  # value = <AccessMode.ReadOnly: 0>
        ReadWrite: typing.ClassVar[QSharedMemory.AccessMode]  # value = <AccessMode.ReadWrite: 1>
    class SharedMemoryError(enum.Enum):
        AlreadyExists: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.AlreadyExists: 4>
        InvalidSize: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.InvalidSize: 2>
        KeyError: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.KeyError: 3>
        LockError: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.LockError: 6>
        NoError: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.NoError: 0>
        NotFound: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.NotFound: 5>
        OutOfResources: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.OutOfResources: 7>
        PermissionDenied: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.PermissionDenied: 1>
        UnknownError: typing.ClassVar[QSharedMemory.SharedMemoryError]  # value = <SharedMemoryError.UnknownError: 8>
    @staticmethod
    def attach(*args, **kwargs):
        ...
    @staticmethod
    def constData(*args, **kwargs):
        ...
    @staticmethod
    def create(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def detach(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def isAttached(*args, **kwargs):
        ...
    @staticmethod
    def isKeyTypeSupported(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def legacyNativeKey(*args, **kwargs):
        ...
    @staticmethod
    def lock(*args, **kwargs):
        ...
    @staticmethod
    def nativeIpcKey(*args, **kwargs):
        ...
    @staticmethod
    def nativeKey(*args, **kwargs):
        ...
    @staticmethod
    def platformSafeKey(*args, **kwargs):
        ...
    @staticmethod
    def setKey(*args, **kwargs):
        ...
    @staticmethod
    def setNativeKey(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QSignalBlocker(PyQt6.sip.simplewrapper):
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def dismiss(*args, **kwargs):
        ...
    @staticmethod
    def reblock(*args, **kwargs):
        ...
    @staticmethod
    def unblock(*args, **kwargs):
        ...
class QSignalMapper(QObject):
    @staticmethod
    def map(*args, **kwargs):
        ...
    @staticmethod
    def mappedInt(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def mappedObject(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def mappedString(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def mapping(*args, **kwargs):
        ...
    @staticmethod
    def removeMappings(*args, **kwargs):
        ...
    @staticmethod
    def setMapping(*args, **kwargs):
        ...
class QSize(PyQt6.sip.simplewrapper):
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def boundedTo(*args, **kwargs):
        ...
    @staticmethod
    def expandedTo(*args, **kwargs):
        ...
    @staticmethod
    def grownBy(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def scale(*args, **kwargs):
        ...
    @staticmethod
    def scaled(*args, **kwargs):
        ...
    @staticmethod
    def setHeight(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def shrunkBy(*args, **kwargs):
        ...
    @staticmethod
    def toSizeF(*args, **kwargs):
        ...
    @staticmethod
    def transpose(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __bool__(self):
        """
        True if self else False
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
class QSizeF(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def boundedTo(*args, **kwargs):
        ...
    @staticmethod
    def expandedTo(*args, **kwargs):
        ...
    @staticmethod
    def grownBy(*args, **kwargs):
        ...
    @staticmethod
    def height(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def scale(*args, **kwargs):
        ...
    @staticmethod
    def scaled(*args, **kwargs):
        ...
    @staticmethod
    def setHeight(*args, **kwargs):
        ...
    @staticmethod
    def setWidth(*args, **kwargs):
        ...
    @staticmethod
    def shrunkBy(*args, **kwargs):
        ...
    @staticmethod
    def toSize(*args, **kwargs):
        ...
    @staticmethod
    def transpose(*args, **kwargs):
        ...
    @staticmethod
    def transposed(*args, **kwargs):
        ...
    @staticmethod
    def width(*args, **kwargs):
        ...
    def __add__(self, value):
        """
        Return self+value.
        """
    def __bool__(self):
        """
        True if self else False
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
class QSocketNotifier(QObject):
    class Type(enum.Enum):
        Exception: typing.ClassVar[QSocketNotifier.Type]  # value = <Type.Exception: 2>
        Read: typing.ClassVar[QSocketNotifier.Type]  # value = <Type.Read: 0>
        Write: typing.ClassVar[QSocketNotifier.Type]  # value = <Type.Write: 1>
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
    def event(*args, **kwargs):
        ...
    @staticmethod
    def isEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def setEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSocket(*args, **kwargs):
        ...
    @staticmethod
    def socket(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QSortFilterProxyModel(QAbstractProxyModel):
    @staticmethod
    def autoAcceptChildRows(*args, **kwargs):
        ...
    @staticmethod
    def autoAcceptChildRowsChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def buddy(*args, **kwargs):
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
    def dropMimeData(*args, **kwargs):
        ...
    @staticmethod
    def dynamicSortFilter(*args, **kwargs):
        ...
    @staticmethod
    def dynamicSortFilterChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def fetchMore(*args, **kwargs):
        ...
    @staticmethod
    def filterAcceptsColumn(*args, **kwargs):
        ...
    @staticmethod
    def filterAcceptsRow(*args, **kwargs):
        ...
    @staticmethod
    def filterCaseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def filterCaseSensitivityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def filterKeyColumn(*args, **kwargs):
        ...
    @staticmethod
    def filterRegularExpression(*args, **kwargs):
        ...
    @staticmethod
    def filterRole(*args, **kwargs):
        ...
    @staticmethod
    def filterRoleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
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
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insertColumns(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def invalidate(*args, **kwargs):
        ...
    @staticmethod
    def invalidateColumnsFilter(*args, **kwargs):
        ...
    @staticmethod
    def invalidateFilter(*args, **kwargs):
        ...
    @staticmethod
    def invalidateRowsFilter(*args, **kwargs):
        ...
    @staticmethod
    def isRecursiveFilteringEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isSortLocaleAware(*args, **kwargs):
        ...
    @staticmethod
    def lessThan(*args, **kwargs):
        ...
    @staticmethod
    def mapFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapSelectionFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapSelectionToSource(*args, **kwargs):
        ...
    @staticmethod
    def mapToSource(*args, **kwargs):
        ...
    @staticmethod
    def match(*args, **kwargs):
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
    def recursiveFilteringEnabledChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def removeColumns(*args, **kwargs):
        ...
    @staticmethod
    def removeRows(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setAutoAcceptChildRows(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setDynamicSortFilter(*args, **kwargs):
        ...
    @staticmethod
    def setFilterCaseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def setFilterFixedString(*args, **kwargs):
        ...
    @staticmethod
    def setFilterKeyColumn(*args, **kwargs):
        ...
    @staticmethod
    def setFilterRegularExpression(*args, **kwargs):
        ...
    @staticmethod
    def setFilterRole(*args, **kwargs):
        ...
    @staticmethod
    def setFilterWildcard(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderData(*args, **kwargs):
        ...
    @staticmethod
    def setRecursiveFilteringEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setSortCaseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def setSortLocaleAware(*args, **kwargs):
        ...
    @staticmethod
    def setSortRole(*args, **kwargs):
        ...
    @staticmethod
    def setSourceModel(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def sortCaseSensitivity(*args, **kwargs):
        ...
    @staticmethod
    def sortCaseSensitivityChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sortColumn(*args, **kwargs):
        ...
    @staticmethod
    def sortLocaleAwareChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def sortOrder(*args, **kwargs):
        ...
    @staticmethod
    def sortRole(*args, **kwargs):
        ...
    @staticmethod
    def sortRoleChanged(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def span(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
class QStandardPaths(PyQt6.sip.simplewrapper):
    class LocateOption(enum.Flag):
        LocateDirectory: typing.ClassVar[QStandardPaths.LocateOption]  # value = <LocateOption.LocateDirectory: 1>
    class StandardLocation(enum.Enum):
        AppConfigLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.AppConfigLocation: 18>
        AppDataLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.AppDataLocation: 17>
        AppLocalDataLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.AppLocalDataLocation: 9>
        ApplicationsLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.ApplicationsLocation: 3>
        CacheLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.CacheLocation: 10>
        ConfigLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.ConfigLocation: 13>
        DesktopLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.DesktopLocation: 0>
        DocumentsLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.DocumentsLocation: 1>
        DownloadLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.DownloadLocation: 14>
        FontsLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.FontsLocation: 2>
        GenericCacheLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.GenericCacheLocation: 15>
        GenericConfigLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.GenericConfigLocation: 16>
        GenericDataLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.GenericDataLocation: 11>
        GenericStateLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.GenericStateLocation: 22>
        HomeLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.HomeLocation: 8>
        MoviesLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.MoviesLocation: 5>
        MusicLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.MusicLocation: 4>
        PicturesLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.PicturesLocation: 6>
        PublicShareLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.PublicShareLocation: 19>
        RuntimeLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.RuntimeLocation: 12>
        StateLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.StateLocation: 21>
        TempLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.TempLocation: 7>
        TemplatesLocation: typing.ClassVar[QStandardPaths.StandardLocation]  # value = <StandardLocation.TemplatesLocation: 20>
    @staticmethod
    def displayName(*args, **kwargs):
        ...
    @staticmethod
    def findExecutable(*args, **kwargs):
        ...
    @staticmethod
    def locate(*args, **kwargs):
        ...
    @staticmethod
    def locateAll(*args, **kwargs):
        ...
    @staticmethod
    def setTestModeEnabled(*args, **kwargs):
        ...
    @staticmethod
    def standardLocations(*args, **kwargs):
        ...
    @staticmethod
    def writableLocation(*args, **kwargs):
        ...
class QStorageInfo(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def blockSize(*args, **kwargs):
        ...
    @staticmethod
    def bytesAvailable(*args, **kwargs):
        ...
    @staticmethod
    def bytesFree(*args, **kwargs):
        ...
    @staticmethod
    def bytesTotal(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def displayName(*args, **kwargs):
        ...
    @staticmethod
    def fileSystemType(*args, **kwargs):
        ...
    @staticmethod
    def isReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def isReady(*args, **kwargs):
        ...
    @staticmethod
    def isRoot(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def mountedVolumes(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def refresh(*args, **kwargs):
        ...
    @staticmethod
    def root(*args, **kwargs):
        ...
    @staticmethod
    def rootPath(*args, **kwargs):
        ...
    @staticmethod
    def setPath(*args, **kwargs):
        ...
    @staticmethod
    def subvolume(*args, **kwargs):
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
class QStringConverter(QStringConverterBase):
    class Encoding(enum.Enum):
        Latin1: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Latin1: 7>
        System: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.System: 8>
        Utf16: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Utf16: 1>
        Utf16BE: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Utf16BE: 3>
        Utf16LE: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Utf16LE: 2>
        Utf32: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Utf32: 4>
        Utf32BE: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Utf32BE: 6>
        Utf32LE: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Utf32LE: 5>
        Utf8: typing.ClassVar[QStringConverter.Encoding]  # value = <Encoding.Utf8: 0>
    @staticmethod
    def availableCodecs(*args, **kwargs):
        ...
    @staticmethod
    def hasError(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def nameForEncoding(*args, **kwargs):
        ...
    @staticmethod
    def resetState(*args, **kwargs):
        ...
class QStringConverterBase(PyQt6.sip.simplewrapper):
    class Flag(enum.Flag):
        ConvertInitialBom: typing.ClassVar[QStringConverterBase.Flag]  # value = <Flag.ConvertInitialBom: 8>
        ConvertInvalidToNull: typing.ClassVar[QStringConverterBase.Flag]  # value = <Flag.ConvertInvalidToNull: 2>
        Stateless: typing.ClassVar[QStringConverterBase.Flag]  # value = <Flag.Stateless: 1>
        UsesIcu: typing.ClassVar[QStringConverterBase.Flag]  # value = <Flag.UsesIcu: 16>
        WriteBom: typing.ClassVar[QStringConverterBase.Flag]  # value = <Flag.WriteBom: 4>
class QStringDecoder(QStringConverter):
    @staticmethod
    def decode(*args, **kwargs):
        ...
    @staticmethod
    def decoderForHtml(*args, **kwargs):
        ...
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
        """
class QStringEncoder(QStringConverter):
    @staticmethod
    def encode(*args, **kwargs):
        ...
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
        """
class QStringListModel(QAbstractListModel):
    @staticmethod
    def clearItemData(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def itemData(*args, **kwargs):
        ...
    @staticmethod
    def moveRows(*args, **kwargs):
        ...
    @staticmethod
    def removeRows(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setItemData(*args, **kwargs):
        ...
    @staticmethod
    def setStringList(*args, **kwargs):
        ...
    @staticmethod
    def sibling(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def stringList(*args, **kwargs):
        ...
    @staticmethod
    def supportedDropActions(*args, **kwargs):
        ...
class QSysInfo(PyQt6.sip.simplewrapper):
    class Endian(enum.Enum):
        BigEndian: typing.ClassVar[QSysInfo.Endian]  # value = <Endian.BigEndian: 0>
        LittleEndian: typing.ClassVar[QSysInfo.Endian]  # value = <Endian.LittleEndian: 1>
    class Sizes(enum.Enum):
        WordSize: typing.ClassVar[QSysInfo.Sizes]  # value = <Sizes.WordSize: 64>
    @staticmethod
    def bootUniqueId(*args, **kwargs):
        ...
    @staticmethod
    def buildAbi(*args, **kwargs):
        ...
    @staticmethod
    def buildCpuArchitecture(*args, **kwargs):
        ...
    @staticmethod
    def currentCpuArchitecture(*args, **kwargs):
        ...
    @staticmethod
    def kernelType(*args, **kwargs):
        ...
    @staticmethod
    def kernelVersion(*args, **kwargs):
        ...
    @staticmethod
    def machineHostName(*args, **kwargs):
        ...
    @staticmethod
    def machineUniqueId(*args, **kwargs):
        ...
    @staticmethod
    def prettyProductName(*args, **kwargs):
        ...
    @staticmethod
    def productType(*args, **kwargs):
        ...
    @staticmethod
    def productVersion(*args, **kwargs):
        ...
class QSystemSemaphore(PyQt6.sip.simplewrapper):
    class AccessMode(enum.Enum):
        Create: typing.ClassVar[QSystemSemaphore.AccessMode]  # value = <AccessMode.Create: 1>
        Open: typing.ClassVar[QSystemSemaphore.AccessMode]  # value = <AccessMode.Open: 0>
    class SystemSemaphoreError(enum.Enum):
        AlreadyExists: typing.ClassVar[QSystemSemaphore.SystemSemaphoreError]  # value = <SystemSemaphoreError.AlreadyExists: 3>
        KeyError: typing.ClassVar[QSystemSemaphore.SystemSemaphoreError]  # value = <SystemSemaphoreError.KeyError: 2>
        NoError: typing.ClassVar[QSystemSemaphore.SystemSemaphoreError]  # value = <SystemSemaphoreError.NoError: 0>
        NotFound: typing.ClassVar[QSystemSemaphore.SystemSemaphoreError]  # value = <SystemSemaphoreError.NotFound: 4>
        OutOfResources: typing.ClassVar[QSystemSemaphore.SystemSemaphoreError]  # value = <SystemSemaphoreError.OutOfResources: 5>
        PermissionDenied: typing.ClassVar[QSystemSemaphore.SystemSemaphoreError]  # value = <SystemSemaphoreError.PermissionDenied: 1>
        UnknownError: typing.ClassVar[QSystemSemaphore.SystemSemaphoreError]  # value = <SystemSemaphoreError.UnknownError: 6>
    @staticmethod
    def acquire(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def isKeyTypeSupported(*args, **kwargs):
        ...
    @staticmethod
    def key(*args, **kwargs):
        ...
    @staticmethod
    def legacyNativeKey(*args, **kwargs):
        ...
    @staticmethod
    def nativeIpcKey(*args, **kwargs):
        ...
    @staticmethod
    def platformSafeKey(*args, **kwargs):
        ...
    @staticmethod
    def release(*args, **kwargs):
        ...
    @staticmethod
    def setKey(*args, **kwargs):
        ...
    @staticmethod
    def setNativeKey(*args, **kwargs):
        ...
class QTemporaryDir(PyQt6.sip.simplewrapper):
    @staticmethod
    def autoRemove(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def filePath(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRemove(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QTemporaryFile(QFile):
    @staticmethod
    def autoRemove(*args, **kwargs):
        ...
    @staticmethod
    def createNativeFile(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def fileTemplate(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def rename(*args, **kwargs):
        ...
    @staticmethod
    def setAutoRemove(*args, **kwargs):
        ...
    @staticmethod
    def setFileTemplate(*args, **kwargs):
        ...
class QTextBoundaryFinder(PyQt6.sip.simplewrapper):
    class BoundaryReason(enum.Flag):
        EndOfItem: typing.ClassVar[QTextBoundaryFinder.BoundaryReason]  # value = <BoundaryReason.EndOfItem: 64>
        MandatoryBreak: typing.ClassVar[QTextBoundaryFinder.BoundaryReason]  # value = <BoundaryReason.MandatoryBreak: 128>
        SoftHyphen: typing.ClassVar[QTextBoundaryFinder.BoundaryReason]  # value = <BoundaryReason.SoftHyphen: 256>
        StartOfItem: typing.ClassVar[QTextBoundaryFinder.BoundaryReason]  # value = <BoundaryReason.StartOfItem: 32>
    class BoundaryType(enum.Enum):
        Grapheme: typing.ClassVar[QTextBoundaryFinder.BoundaryType]  # value = <BoundaryType.Grapheme: 0>
        Line: typing.ClassVar[QTextBoundaryFinder.BoundaryType]  # value = <BoundaryType.Line: 3>
        Sentence: typing.ClassVar[QTextBoundaryFinder.BoundaryType]  # value = <BoundaryType.Sentence: 2>
        Word: typing.ClassVar[QTextBoundaryFinder.BoundaryType]  # value = <BoundaryType.Word: 1>
    @staticmethod
    def boundaryReasons(*args, **kwargs):
        ...
    @staticmethod
    def isAtBoundary(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def position(*args, **kwargs):
        ...
    @staticmethod
    def setPosition(*args, **kwargs):
        ...
    @staticmethod
    def string(*args, **kwargs):
        ...
    @staticmethod
    def toEnd(*args, **kwargs):
        ...
    @staticmethod
    def toNextBoundary(*args, **kwargs):
        ...
    @staticmethod
    def toPreviousBoundary(*args, **kwargs):
        ...
    @staticmethod
    def toStart(*args, **kwargs):
        ...
    @staticmethod
    def type(*args, **kwargs):
        ...
class QTextStream(QIODeviceBase):
    class FieldAlignment(enum.Enum):
        AlignAccountingStyle: typing.ClassVar[QTextStream.FieldAlignment]  # value = <FieldAlignment.AlignAccountingStyle: 3>
        AlignCenter: typing.ClassVar[QTextStream.FieldAlignment]  # value = <FieldAlignment.AlignCenter: 2>
        AlignLeft: typing.ClassVar[QTextStream.FieldAlignment]  # value = <FieldAlignment.AlignLeft: 0>
        AlignRight: typing.ClassVar[QTextStream.FieldAlignment]  # value = <FieldAlignment.AlignRight: 1>
    class NumberFlag(enum.Flag):
        ForcePoint: typing.ClassVar[QTextStream.NumberFlag]  # value = <NumberFlag.ForcePoint: 2>
        ForceSign: typing.ClassVar[QTextStream.NumberFlag]  # value = <NumberFlag.ForceSign: 4>
        ShowBase: typing.ClassVar[QTextStream.NumberFlag]  # value = <NumberFlag.ShowBase: 1>
        UppercaseBase: typing.ClassVar[QTextStream.NumberFlag]  # value = <NumberFlag.UppercaseBase: 8>
        UppercaseDigits: typing.ClassVar[QTextStream.NumberFlag]  # value = <NumberFlag.UppercaseDigits: 16>
    class RealNumberNotation(enum.Enum):
        FixedNotation: typing.ClassVar[QTextStream.RealNumberNotation]  # value = <RealNumberNotation.FixedNotation: 1>
        ScientificNotation: typing.ClassVar[QTextStream.RealNumberNotation]  # value = <RealNumberNotation.ScientificNotation: 2>
        SmartNotation: typing.ClassVar[QTextStream.RealNumberNotation]  # value = <RealNumberNotation.SmartNotation: 0>
    class Status(enum.Enum):
        Ok: typing.ClassVar[QTextStream.Status]  # value = <Status.Ok: 0>
        ReadCorruptData: typing.ClassVar[QTextStream.Status]  # value = <Status.ReadCorruptData: 2>
        ReadPastEnd: typing.ClassVar[QTextStream.Status]  # value = <Status.ReadPastEnd: 1>
        WriteFailed: typing.ClassVar[QTextStream.Status]  # value = <Status.WriteFailed: 3>
    @staticmethod
    def atEnd(*args, **kwargs):
        ...
    @staticmethod
    def autoDetectUnicode(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def encoding(*args, **kwargs):
        ...
    @staticmethod
    def fieldAlignment(*args, **kwargs):
        ...
    @staticmethod
    def fieldWidth(*args, **kwargs):
        ...
    @staticmethod
    def flush(*args, **kwargs):
        ...
    @staticmethod
    def generateByteOrderMark(*args, **kwargs):
        ...
    @staticmethod
    def integerBase(*args, **kwargs):
        ...
    @staticmethod
    def locale(*args, **kwargs):
        ...
    @staticmethod
    def numberFlags(*args, **kwargs):
        ...
    @staticmethod
    def padChar(*args, **kwargs):
        ...
    @staticmethod
    def pos(*args, **kwargs):
        ...
    @staticmethod
    def read(*args, **kwargs):
        ...
    @staticmethod
    def readAll(*args, **kwargs):
        ...
    @staticmethod
    def readLine(*args, **kwargs):
        ...
    @staticmethod
    def realNumberNotation(*args, **kwargs):
        ...
    @staticmethod
    def realNumberPrecision(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def resetStatus(*args, **kwargs):
        ...
    @staticmethod
    def seek(*args, **kwargs):
        ...
    @staticmethod
    def setAutoDetectUnicode(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setEncoding(*args, **kwargs):
        ...
    @staticmethod
    def setFieldAlignment(*args, **kwargs):
        ...
    @staticmethod
    def setFieldWidth(*args, **kwargs):
        ...
    @staticmethod
    def setGenerateByteOrderMark(*args, **kwargs):
        ...
    @staticmethod
    def setIntegerBase(*args, **kwargs):
        ...
    @staticmethod
    def setLocale(*args, **kwargs):
        ...
    @staticmethod
    def setNumberFlags(*args, **kwargs):
        ...
    @staticmethod
    def setPadChar(*args, **kwargs):
        ...
    @staticmethod
    def setRealNumberNotation(*args, **kwargs):
        ...
    @staticmethod
    def setRealNumberPrecision(*args, **kwargs):
        ...
    @staticmethod
    def setStatus(*args, **kwargs):
        ...
    @staticmethod
    def skipWhiteSpace(*args, **kwargs):
        ...
    @staticmethod
    def status(*args, **kwargs):
        ...
    def __lshift__(self, value):
        """
        Return self<<value.
        """
    def __rlshift__(self, value):
        """
        Return value<<self.
        """
    def __rrshift__(self, value):
        """
        Return value>>self.
        """
    def __rshift__(self, value):
        """
        Return self>>value.
        """
class QTextStreamManipulator(PyQt6.sip.simplewrapper):
    pass
class QThread(QObject):
    class Priority(enum.Enum):
        HighPriority: typing.ClassVar[QThread.Priority]  # value = <Priority.HighPriority: 4>
        HighestPriority: typing.ClassVar[QThread.Priority]  # value = <Priority.HighestPriority: 5>
        IdlePriority: typing.ClassVar[QThread.Priority]  # value = <Priority.IdlePriority: 0>
        InheritPriority: typing.ClassVar[QThread.Priority]  # value = <Priority.InheritPriority: 7>
        LowPriority: typing.ClassVar[QThread.Priority]  # value = <Priority.LowPriority: 2>
        LowestPriority: typing.ClassVar[QThread.Priority]  # value = <Priority.LowestPriority: 1>
        NormalPriority: typing.ClassVar[QThread.Priority]  # value = <Priority.NormalPriority: 3>
        TimeCriticalPriority: typing.ClassVar[QThread.Priority]  # value = <Priority.TimeCriticalPriority: 6>
    @staticmethod
    def currentThread(*args, **kwargs):
        ...
    @staticmethod
    def currentThreadId(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def eventDispatcher(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def exit(*args, **kwargs):
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
    def idealThreadCount(*args, **kwargs):
        ...
    @staticmethod
    def isFinished(*args, **kwargs):
        ...
    @staticmethod
    def isInterruptionRequested(*args, **kwargs):
        ...
    @staticmethod
    def isRunning(*args, **kwargs):
        ...
    @staticmethod
    def loopLevel(*args, **kwargs):
        ...
    @staticmethod
    def msleep(*args, **kwargs):
        ...
    @staticmethod
    def priority(*args, **kwargs):
        ...
    @staticmethod
    def quit(*args, **kwargs):
        ...
    @staticmethod
    def requestInterruption(*args, **kwargs):
        ...
    @staticmethod
    def run(*args, **kwargs):
        ...
    @staticmethod
    def setEventDispatcher(*args, **kwargs):
        ...
    @staticmethod
    def setPriority(*args, **kwargs):
        ...
    @staticmethod
    def setStackSize(*args, **kwargs):
        ...
    @staticmethod
    def setTerminationEnabled(*args, **kwargs):
        ...
    @staticmethod
    def sleep(*args, **kwargs):
        ...
    @staticmethod
    def stackSize(*args, **kwargs):
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
    def terminate(*args, **kwargs):
        ...
    @staticmethod
    def usleep(*args, **kwargs):
        ...
    @staticmethod
    def wait(*args, **kwargs):
        ...
    @staticmethod
    def yieldCurrentThread(*args, **kwargs):
        ...
class QThreadPool(QObject):
    @staticmethod
    def activeThreadCount(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def expiryTimeout(*args, **kwargs):
        ...
    @staticmethod
    def globalInstance(*args, **kwargs):
        ...
    @staticmethod
    def maxThreadCount(*args, **kwargs):
        ...
    @staticmethod
    def releaseThread(*args, **kwargs):
        ...
    @staticmethod
    def reserveThread(*args, **kwargs):
        ...
    @staticmethod
    def setExpiryTimeout(*args, **kwargs):
        ...
    @staticmethod
    def setMaxThreadCount(*args, **kwargs):
        ...
    @staticmethod
    def setStackSize(*args, **kwargs):
        ...
    @staticmethod
    def setThreadPriority(*args, **kwargs):
        ...
    @staticmethod
    def stackSize(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
    @staticmethod
    def startOnReservedThread(*args, **kwargs):
        ...
    @staticmethod
    def threadPriority(*args, **kwargs):
        ...
    @staticmethod
    def tryStart(*args, **kwargs):
        ...
    @staticmethod
    def tryTake(*args, **kwargs):
        ...
    @staticmethod
    def waitForDone(*args, **kwargs):
        ...
class QTime(PyQt6.sip.simplewrapper):
    @staticmethod
    def __reduce__(*args, **kwargs):
        ...
    @staticmethod
    def addMSecs(*args, **kwargs):
        ...
    @staticmethod
    def addSecs(*args, **kwargs):
        ...
    @staticmethod
    def currentTime(*args, **kwargs):
        ...
    @staticmethod
    def fromMSecsSinceStartOfDay(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def hour(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def minute(*args, **kwargs):
        ...
    @staticmethod
    def msec(*args, **kwargs):
        ...
    @staticmethod
    def msecsSinceStartOfDay(*args, **kwargs):
        ...
    @staticmethod
    def msecsTo(*args, **kwargs):
        ...
    @staticmethod
    def second(*args, **kwargs):
        ...
    @staticmethod
    def secsTo(*args, **kwargs):
        ...
    @staticmethod
    def setHMS(*args, **kwargs):
        ...
    @staticmethod
    def toPyTime(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    def __bool__(self):
        """
        True if self else False
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
class QTimeLine(QObject):
    class Direction(enum.Enum):
        Backward: typing.ClassVar[QTimeLine.Direction]  # value = <Direction.Backward: 1>
        Forward: typing.ClassVar[QTimeLine.Direction]  # value = <Direction.Forward: 0>
    class State(enum.Enum):
        NotRunning: typing.ClassVar[QTimeLine.State]  # value = <State.NotRunning: 0>
        Paused: typing.ClassVar[QTimeLine.State]  # value = <State.Paused: 1>
        Running: typing.ClassVar[QTimeLine.State]  # value = <State.Running: 2>
    @staticmethod
    def currentFrame(*args, **kwargs):
        ...
    @staticmethod
    def currentTime(*args, **kwargs):
        ...
    @staticmethod
    def currentValue(*args, **kwargs):
        ...
    @staticmethod
    def direction(*args, **kwargs):
        ...
    @staticmethod
    def duration(*args, **kwargs):
        ...
    @staticmethod
    def easingCurve(*args, **kwargs):
        ...
    @staticmethod
    def endFrame(*args, **kwargs):
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
    def frameForTime(*args, **kwargs):
        ...
    @staticmethod
    def loopCount(*args, **kwargs):
        ...
    @staticmethod
    def resume(*args, **kwargs):
        ...
    @staticmethod
    def setCurrentTime(*args, **kwargs):
        ...
    @staticmethod
    def setDirection(*args, **kwargs):
        ...
    @staticmethod
    def setDuration(*args, **kwargs):
        ...
    @staticmethod
    def setEasingCurve(*args, **kwargs):
        ...
    @staticmethod
    def setEndFrame(*args, **kwargs):
        ...
    @staticmethod
    def setFrameRange(*args, **kwargs):
        ...
    @staticmethod
    def setLoopCount(*args, **kwargs):
        ...
    @staticmethod
    def setPaused(*args, **kwargs):
        ...
    @staticmethod
    def setStartFrame(*args, **kwargs):
        ...
    @staticmethod
    def setUpdateInterval(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
    @staticmethod
    def startFrame(*args, **kwargs):
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
    def timerEvent(*args, **kwargs):
        ...
    @staticmethod
    def toggleDirection(*args, **kwargs):
        ...
    @staticmethod
    def updateInterval(*args, **kwargs):
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
    def valueForTime(*args, **kwargs):
        ...
class QTimeZone(PyQt6.sip.simplewrapper):
    class Initialization(enum.Enum):
        LocalTime: typing.ClassVar[QTimeZone.Initialization]  # value = <Initialization.LocalTime: 0>
        UTC: typing.ClassVar[QTimeZone.Initialization]  # value = <Initialization.UTC: 1>
    class NameType(enum.Enum):
        DefaultName: typing.ClassVar[QTimeZone.NameType]  # value = <NameType.DefaultName: 0>
        LongName: typing.ClassVar[QTimeZone.NameType]  # value = <NameType.LongName: 1>
        OffsetName: typing.ClassVar[QTimeZone.NameType]  # value = <NameType.OffsetName: 3>
        ShortName: typing.ClassVar[QTimeZone.NameType]  # value = <NameType.ShortName: 2>
    class OffsetData(PyQt6.sip.simplewrapper):
        pass
    class TimeType(enum.Enum):
        DaylightTime: typing.ClassVar[QTimeZone.TimeType]  # value = <TimeType.DaylightTime: 1>
        GenericTime: typing.ClassVar[QTimeZone.TimeType]  # value = <TimeType.GenericTime: 2>
        StandardTime: typing.ClassVar[QTimeZone.TimeType]  # value = <TimeType.StandardTime: 0>
    MaxUtcOffsetSecs: typing.ClassVar[int] = 57600
    MinUtcOffsetSecs: typing.ClassVar[int] = -57600
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def abbreviation(*args, **kwargs):
        ...
    @staticmethod
    def asBackendZone(*args, **kwargs):
        ...
    @staticmethod
    def availableTimeZoneIds(*args, **kwargs):
        ...
    @staticmethod
    def comment(*args, **kwargs):
        ...
    @staticmethod
    def country(*args, **kwargs):
        ...
    @staticmethod
    def daylightTimeOffset(*args, **kwargs):
        ...
    @staticmethod
    def displayName(*args, **kwargs):
        ...
    @staticmethod
    def fixedSecondsAheadOfUtc(*args, **kwargs):
        ...
    @staticmethod
    def fromSecondsAheadOfUtc(*args, **kwargs):
        ...
    @staticmethod
    def hasDaylightTime(*args, **kwargs):
        ...
    @staticmethod
    def hasTransitions(*args, **kwargs):
        ...
    @staticmethod
    def ianaIdToWindowsId(*args, **kwargs):
        ...
    @staticmethod
    def id(*args, **kwargs):
        ...
    @staticmethod
    def isDaylightTime(*args, **kwargs):
        ...
    @staticmethod
    def isTimeZoneIdAvailable(*args, **kwargs):
        ...
    @staticmethod
    def isUtcOrFixedOffset(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def nextTransition(*args, **kwargs):
        ...
    @staticmethod
    def offsetData(*args, **kwargs):
        ...
    @staticmethod
    def offsetFromUtc(*args, **kwargs):
        ...
    @staticmethod
    def previousTransition(*args, **kwargs):
        ...
    @staticmethod
    def standardTimeOffset(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def systemTimeZone(*args, **kwargs):
        ...
    @staticmethod
    def systemTimeZoneId(*args, **kwargs):
        ...
    @staticmethod
    def territory(*args, **kwargs):
        ...
    @staticmethod
    def timeSpec(*args, **kwargs):
        ...
    @staticmethod
    def transitions(*args, **kwargs):
        ...
    @staticmethod
    def utc(*args, **kwargs):
        ...
    @staticmethod
    def windowsIdToDefaultIanaId(*args, **kwargs):
        ...
    @staticmethod
    def windowsIdToIanaIds(*args, **kwargs):
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
class QTimer(QObject):
    @staticmethod
    def interval(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def isSingleShot(*args, **kwargs):
        ...
    @staticmethod
    def remainingTime(*args, **kwargs):
        ...
    @staticmethod
    def setInterval(*args, **kwargs):
        ...
    @staticmethod
    def setSingleShot(*args, **kwargs):
        ...
    @staticmethod
    def setTimerType(*args, **kwargs):
        ...
    @staticmethod
    def singleShot(*args, **kwargs):
        ...
    @staticmethod
    def start(*args, **kwargs):
        ...
    @staticmethod
    def stop(*args, **kwargs):
        ...
    @staticmethod
    def timeout(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def timerId(*args, **kwargs):
        ...
    @staticmethod
    def timerType(*args, **kwargs):
        ...
class QTimerEvent(QEvent):
    @staticmethod
    def clone(*args, **kwargs):
        ...
    @staticmethod
    def timerId(*args, **kwargs):
        ...
class QTranslator(QObject):
    @staticmethod
    def filePath(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def language(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def loadFromData(*args, **kwargs):
        ...
    @staticmethod
    def translate(*args, **kwargs):
        ...
class QTransposeProxyModel(QAbstractProxyModel):
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def index(*args, **kwargs):
        ...
    @staticmethod
    def insertColumns(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def itemData(*args, **kwargs):
        ...
    @staticmethod
    def mapFromSource(*args, **kwargs):
        ...
    @staticmethod
    def mapToSource(*args, **kwargs):
        ...
    @staticmethod
    def moveColumns(*args, **kwargs):
        ...
    @staticmethod
    def moveRows(*args, **kwargs):
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
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderData(*args, **kwargs):
        ...
    @staticmethod
    def setItemData(*args, **kwargs):
        ...
    @staticmethod
    def setSourceModel(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def span(*args, **kwargs):
        ...
class QTypeRevision(PyQt6.sip.simplewrapper):
    @staticmethod
    def fromEncodedVersion(*args, **kwargs):
        ...
    @staticmethod
    def hasMajorVersion(*args, **kwargs):
        ...
    @staticmethod
    def hasMinorVersion(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def majorVersion(*args, **kwargs):
        ...
    @staticmethod
    def minorVersion(*args, **kwargs):
        ...
    @staticmethod
    def toEncodedVersion(*args, **kwargs):
        ...
    @staticmethod
    def zero(*args, **kwargs):
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
class QUrl(PyQt6.sip.simplewrapper):
    class AceProcessingOption(enum.Flag):
        AceTransitionalProcessing: typing.ClassVar[QUrl.AceProcessingOption]  # value = <AceProcessingOption.AceTransitionalProcessing: 2>
        IgnoreIDNWhitelist: typing.ClassVar[QUrl.AceProcessingOption]  # value = <AceProcessingOption.IgnoreIDNWhitelist: 1>
    class ComponentFormattingOption(enum.IntFlag):
        DecodeReserved: typing.ClassVar[QUrl.ComponentFormattingOption]  # value = <ComponentFormattingOption.DecodeReserved: 33554432>
        EncodeReserved: typing.ClassVar[QUrl.ComponentFormattingOption]  # value = <ComponentFormattingOption.EncodeReserved: 16777216>
        EncodeSpaces: typing.ClassVar[QUrl.ComponentFormattingOption]  # value = <ComponentFormattingOption.EncodeSpaces: 1048576>
        EncodeUnicode: typing.ClassVar[QUrl.ComponentFormattingOption]  # value = <ComponentFormattingOption.EncodeUnicode: 2097152>
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
    class ParsingMode(enum.Enum):
        DecodedMode: typing.ClassVar[QUrl.ParsingMode]  # value = <ParsingMode.DecodedMode: 2>
        StrictMode: typing.ClassVar[QUrl.ParsingMode]  # value = <ParsingMode.StrictMode: 1>
        TolerantMode: typing.ClassVar[QUrl.ParsingMode]  # value = <ParsingMode.TolerantMode: 0>
    class UrlFormattingOption(enum.IntFlag):
        NormalizePathSegments: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.NormalizePathSegments: 4096>
        PreferLocalFile: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.PreferLocalFile: 512>
        RemoveFilename: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.RemoveFilename: 2048>
        RemoveFragment: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.RemoveFragment: 128>
        RemovePassword: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.RemovePassword: 2>
        RemovePath: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.RemovePath: 32>
        RemovePort: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.RemovePort: 8>
        RemoveQuery: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.RemoveQuery: 64>
        RemoveScheme: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.RemoveScheme: 1>
        StripTrailingSlash: typing.ClassVar[QUrl.UrlFormattingOption]  # value = <UrlFormattingOption.StripTrailingSlash: 1024>
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
    class UserInputResolutionOption(enum.Flag):
        AssumeLocalFile: typing.ClassVar[QUrl.UserInputResolutionOption]  # value = <UserInputResolutionOption.AssumeLocalFile: 1>
    @staticmethod
    def adjusted(*args, **kwargs):
        ...
    @staticmethod
    def authority(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def detach(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def fileName(*args, **kwargs):
        ...
    @staticmethod
    def fragment(*args, **kwargs):
        ...
    @staticmethod
    def fromAce(*args, **kwargs):
        ...
    @staticmethod
    def fromEncoded(*args, **kwargs):
        ...
    @staticmethod
    def fromLocalFile(*args, **kwargs):
        ...
    @staticmethod
    def fromPercentEncoding(*args, **kwargs):
        ...
    @staticmethod
    def fromStringList(*args, **kwargs):
        ...
    @staticmethod
    def fromUserInput(*args, **kwargs):
        ...
    @staticmethod
    def hasFragment(*args, **kwargs):
        ...
    @staticmethod
    def hasQuery(*args, **kwargs):
        ...
    @staticmethod
    def host(*args, **kwargs):
        ...
    @staticmethod
    def idnWhitelist(*args, **kwargs):
        ...
    @staticmethod
    def isDetached(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def isLocalFile(*args, **kwargs):
        ...
    @staticmethod
    def isParentOf(*args, **kwargs):
        ...
    @staticmethod
    def isRelative(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def matches(*args, **kwargs):
        ...
    @staticmethod
    def password(*args, **kwargs):
        ...
    @staticmethod
    def path(*args, **kwargs):
        ...
    @staticmethod
    def port(*args, **kwargs):
        ...
    @staticmethod
    def query(*args, **kwargs):
        ...
    @staticmethod
    def resolved(*args, **kwargs):
        ...
    @staticmethod
    def scheme(*args, **kwargs):
        ...
    @staticmethod
    def setAuthority(*args, **kwargs):
        ...
    @staticmethod
    def setFragment(*args, **kwargs):
        ...
    @staticmethod
    def setHost(*args, **kwargs):
        ...
    @staticmethod
    def setIdnWhitelist(*args, **kwargs):
        ...
    @staticmethod
    def setPassword(*args, **kwargs):
        ...
    @staticmethod
    def setPath(*args, **kwargs):
        ...
    @staticmethod
    def setPort(*args, **kwargs):
        ...
    @staticmethod
    def setQuery(*args, **kwargs):
        ...
    @staticmethod
    def setScheme(*args, **kwargs):
        ...
    @staticmethod
    def setUrl(*args, **kwargs):
        ...
    @staticmethod
    def setUserInfo(*args, **kwargs):
        ...
    @staticmethod
    def setUserName(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def toAce(*args, **kwargs):
        ...
    @staticmethod
    def toDisplayString(*args, **kwargs):
        ...
    @staticmethod
    def toEncoded(*args, **kwargs):
        ...
    @staticmethod
    def toLocalFile(*args, **kwargs):
        ...
    @staticmethod
    def toPercentEncoding(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    @staticmethod
    def toStringList(*args, **kwargs):
        ...
    @staticmethod
    def url(*args, **kwargs):
        ...
    @staticmethod
    def userInfo(*args, **kwargs):
        ...
    @staticmethod
    def userName(*args, **kwargs):
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
    def __repr__(self):
        """
        Return repr(self).
        """
class QUrlQuery(PyQt6.sip.simplewrapper):
    @staticmethod
    def addQueryItem(*args, **kwargs):
        ...
    @staticmethod
    def allQueryItemValues(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def defaultQueryPairDelimiter(*args, **kwargs):
        ...
    @staticmethod
    def defaultQueryValueDelimiter(*args, **kwargs):
        ...
    @staticmethod
    def hasQueryItem(*args, **kwargs):
        ...
    @staticmethod
    def isDetached(*args, **kwargs):
        ...
    @staticmethod
    def isEmpty(*args, **kwargs):
        ...
    @staticmethod
    def query(*args, **kwargs):
        ...
    @staticmethod
    def queryItemValue(*args, **kwargs):
        ...
    @staticmethod
    def queryItems(*args, **kwargs):
        ...
    @staticmethod
    def queryPairDelimiter(*args, **kwargs):
        ...
    @staticmethod
    def queryValueDelimiter(*args, **kwargs):
        ...
    @staticmethod
    def removeAllQueryItems(*args, **kwargs):
        ...
    @staticmethod
    def removeQueryItem(*args, **kwargs):
        ...
    @staticmethod
    def setQuery(*args, **kwargs):
        ...
    @staticmethod
    def setQueryDelimiters(*args, **kwargs):
        ...
    @staticmethod
    def setQueryItems(*args, **kwargs):
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
class QUuid(PyQt6.sip.simplewrapper):
    class Id128Bytes(PyQt6.sip.simplewrapper):
        pass
    class StringFormat(enum.Enum):
        Id128: typing.ClassVar[QUuid.StringFormat]  # value = <StringFormat.Id128: 3>
        WithBraces: typing.ClassVar[QUuid.StringFormat]  # value = <StringFormat.WithBraces: 0>
        WithoutBraces: typing.ClassVar[QUuid.StringFormat]  # value = <StringFormat.WithoutBraces: 1>
    class Variant(enum.Enum):
        DCE: typing.ClassVar[QUuid.Variant]  # value = <Variant.DCE: 2>
        Microsoft: typing.ClassVar[QUuid.Variant]  # value = <Variant.Microsoft: 6>
        NCS: typing.ClassVar[QUuid.Variant]  # value = <Variant.NCS: 0>
        Reserved: typing.ClassVar[QUuid.Variant]  # value = <Variant.Reserved: 7>
        VarUnknown: typing.ClassVar[QUuid.Variant]  # value = <Variant.VarUnknown: -1>
    class Version(enum.Enum):
        EmbeddedPOSIX: typing.ClassVar[QUuid.Version]  # value = <Version.EmbeddedPOSIX: 2>
        Md5: typing.ClassVar[QUuid.Version]  # value = <Version.Md5: 3>
        Random: typing.ClassVar[QUuid.Version]  # value = <Version.Random: 4>
        Sha1: typing.ClassVar[QUuid.Version]  # value = <Version.Sha1: 5>
        Time: typing.ClassVar[QUuid.Version]  # value = <Version.Time: 1>
        VerUnknown: typing.ClassVar[QUuid.Version]  # value = <Version.VerUnknown: -1>
    @staticmethod
    def createUuid(*args, **kwargs):
        ...
    @staticmethod
    def createUuidV3(*args, **kwargs):
        ...
    @staticmethod
    def createUuidV5(*args, **kwargs):
        ...
    @staticmethod
    def fromRfc4122(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def toByteArray(*args, **kwargs):
        ...
    @staticmethod
    def toRfc4122(*args, **kwargs):
        ...
    @staticmethod
    def toString(*args, **kwargs):
        ...
    @staticmethod
    def variant(*args, **kwargs):
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
    def __repr__(self):
        """
        Return repr(self).
        """
class QVariant(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def canConvert(*args, **kwargs):
        ...
    @staticmethod
    def canView(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def convert(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def load(*args, **kwargs):
        ...
    @staticmethod
    def metaType(*args, **kwargs):
        ...
    @staticmethod
    def save(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def typeId(*args, **kwargs):
        ...
    @staticmethod
    def typeName(*args, **kwargs):
        ...
    @staticmethod
    def userType(*args, **kwargs):
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
class QVariantAnimation(QAbstractAnimation):
    @staticmethod
    def currentValue(*args, **kwargs):
        ...
    @staticmethod
    def duration(*args, **kwargs):
        ...
    @staticmethod
    def easingCurve(*args, **kwargs):
        ...
    @staticmethod
    def endValue(*args, **kwargs):
        ...
    @staticmethod
    def event(*args, **kwargs):
        ...
    @staticmethod
    def interpolated(*args, **kwargs):
        ...
    @staticmethod
    def keyValueAt(*args, **kwargs):
        ...
    @staticmethod
    def keyValues(*args, **kwargs):
        ...
    @staticmethod
    def setDuration(*args, **kwargs):
        ...
    @staticmethod
    def setEasingCurve(*args, **kwargs):
        ...
    @staticmethod
    def setEndValue(*args, **kwargs):
        ...
    @staticmethod
    def setKeyValueAt(*args, **kwargs):
        ...
    @staticmethod
    def setKeyValues(*args, **kwargs):
        ...
    @staticmethod
    def setStartValue(*args, **kwargs):
        ...
    @staticmethod
    def startValue(*args, **kwargs):
        ...
    @staticmethod
    def updateCurrentTime(*args, **kwargs):
        ...
    @staticmethod
    def updateCurrentValue(*args, **kwargs):
        ...
    @staticmethod
    def updateState(*args, **kwargs):
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
class QVersionNumber(PyQt6.sip.simplewrapper):
    @staticmethod
    def commonPrefix(*args, **kwargs):
        ...
    @staticmethod
    def compare(*args, **kwargs):
        ...
    @staticmethod
    def fromString(*args, **kwargs):
        ...
    @staticmethod
    def isNormalized(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isPrefixOf(*args, **kwargs):
        ...
    @staticmethod
    def majorVersion(*args, **kwargs):
        ...
    @staticmethod
    def microVersion(*args, **kwargs):
        ...
    @staticmethod
    def minorVersion(*args, **kwargs):
        ...
    @staticmethod
    def normalized(*args, **kwargs):
        ...
    @staticmethod
    def segmentAt(*args, **kwargs):
        ...
    @staticmethod
    def segmentCount(*args, **kwargs):
        ...
    @staticmethod
    def segments(*args, **kwargs):
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
class QWaitCondition(PyQt6.sip.simplewrapper):
    @staticmethod
    def wait(*args, **kwargs):
        ...
    @staticmethod
    def wakeAll(*args, **kwargs):
        ...
    @staticmethod
    def wakeOne(*args, **kwargs):
        ...
class QWriteLocker(PyQt6.sip.simplewrapper):
    @staticmethod
    def __enter__(*args, **kwargs):
        ...
    @staticmethod
    def __exit__(*args, **kwargs):
        ...
    @staticmethod
    def readWriteLock(*args, **kwargs):
        ...
    @staticmethod
    def relock(*args, **kwargs):
        ...
    @staticmethod
    def unlock(*args, **kwargs):
        ...
class QXmlStreamAttribute(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def isDefault(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def namespaceUri(*args, **kwargs):
        ...
    @staticmethod
    def prefix(*args, **kwargs):
        ...
    @staticmethod
    def qualifiedName(*args, **kwargs):
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
class QXmlStreamAttributes(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def at(*args, **kwargs):
        ...
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
    def data(*args, **kwargs):
        ...
    @staticmethod
    def fill(*args, **kwargs):
        ...
    @staticmethod
    def first(*args, **kwargs):
        ...
    @staticmethod
    def hasAttribute(*args, **kwargs):
        ...
    @staticmethod
    def indexOf(*args, **kwargs):
        ...
    @staticmethod
    def insert(*args, **kwargs):
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
    def value(*args, **kwargs):
        ...
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
    def __lt__(self, value):
        """
        Return self<value.
        """
    def __ne__(self, value):
        """
        Return self!=value.
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class QXmlStreamEntityDeclaration(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def notationName(*args, **kwargs):
        ...
    @staticmethod
    def publicId(*args, **kwargs):
        ...
    @staticmethod
    def systemId(*args, **kwargs):
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
class QXmlStreamEntityResolver(PyQt6.sip.simplewrapper):
    @staticmethod
    def resolveUndeclaredEntity(*args, **kwargs):
        ...
class QXmlStreamNamespaceDeclaration(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def namespaceUri(*args, **kwargs):
        ...
    @staticmethod
    def prefix(*args, **kwargs):
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
class QXmlStreamNotationDeclaration(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def publicId(*args, **kwargs):
        ...
    @staticmethod
    def systemId(*args, **kwargs):
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
class QXmlStreamReader(PyQt6.sip.simplewrapper):
    class Error(enum.Enum):
        CustomError: typing.ClassVar[QXmlStreamReader.Error]  # value = <Error.CustomError: 2>
        NoError: typing.ClassVar[QXmlStreamReader.Error]  # value = <Error.NoError: 0>
        NotWellFormedError: typing.ClassVar[QXmlStreamReader.Error]  # value = <Error.NotWellFormedError: 3>
        PrematureEndOfDocumentError: typing.ClassVar[QXmlStreamReader.Error]  # value = <Error.PrematureEndOfDocumentError: 4>
        UnexpectedElementError: typing.ClassVar[QXmlStreamReader.Error]  # value = <Error.UnexpectedElementError: 1>
    class ReadElementTextBehaviour(enum.Enum):
        ErrorOnUnexpectedElement: typing.ClassVar[QXmlStreamReader.ReadElementTextBehaviour]  # value = <ReadElementTextBehaviour.ErrorOnUnexpectedElement: 0>
        IncludeChildElements: typing.ClassVar[QXmlStreamReader.ReadElementTextBehaviour]  # value = <ReadElementTextBehaviour.IncludeChildElements: 1>
        SkipChildElements: typing.ClassVar[QXmlStreamReader.ReadElementTextBehaviour]  # value = <ReadElementTextBehaviour.SkipChildElements: 2>
    class TokenType(enum.Enum):
        Characters: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.Characters: 6>
        Comment: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.Comment: 7>
        DTD: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.DTD: 8>
        EndDocument: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.EndDocument: 3>
        EndElement: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.EndElement: 5>
        EntityReference: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.EntityReference: 9>
        Invalid: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.Invalid: 1>
        NoToken: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.NoToken: 0>
        ProcessingInstruction: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.ProcessingInstruction: 10>
        StartDocument: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.StartDocument: 2>
        StartElement: typing.ClassVar[QXmlStreamReader.TokenType]  # value = <TokenType.StartElement: 4>
    @staticmethod
    def addData(*args, **kwargs):
        ...
    @staticmethod
    def addExtraNamespaceDeclaration(*args, **kwargs):
        ...
    @staticmethod
    def addExtraNamespaceDeclarations(*args, **kwargs):
        ...
    @staticmethod
    def atEnd(*args, **kwargs):
        ...
    @staticmethod
    def attributes(*args, **kwargs):
        ...
    @staticmethod
    def characterOffset(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def columnNumber(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def documentEncoding(*args, **kwargs):
        ...
    @staticmethod
    def documentVersion(*args, **kwargs):
        ...
    @staticmethod
    def dtdName(*args, **kwargs):
        ...
    @staticmethod
    def dtdPublicId(*args, **kwargs):
        ...
    @staticmethod
    def dtdSystemId(*args, **kwargs):
        ...
    @staticmethod
    def entityDeclarations(*args, **kwargs):
        ...
    @staticmethod
    def entityExpansionLimit(*args, **kwargs):
        ...
    @staticmethod
    def entityResolver(*args, **kwargs):
        ...
    @staticmethod
    def error(*args, **kwargs):
        ...
    @staticmethod
    def errorString(*args, **kwargs):
        ...
    @staticmethod
    def hasError(*args, **kwargs):
        ...
    @staticmethod
    def hasStandaloneDeclaration(*args, **kwargs):
        ...
    @staticmethod
    def isCDATA(*args, **kwargs):
        ...
    @staticmethod
    def isCharacters(*args, **kwargs):
        ...
    @staticmethod
    def isComment(*args, **kwargs):
        ...
    @staticmethod
    def isDTD(*args, **kwargs):
        ...
    @staticmethod
    def isEndDocument(*args, **kwargs):
        ...
    @staticmethod
    def isEndElement(*args, **kwargs):
        ...
    @staticmethod
    def isEntityReference(*args, **kwargs):
        ...
    @staticmethod
    def isProcessingInstruction(*args, **kwargs):
        ...
    @staticmethod
    def isStandaloneDocument(*args, **kwargs):
        ...
    @staticmethod
    def isStartDocument(*args, **kwargs):
        ...
    @staticmethod
    def isStartElement(*args, **kwargs):
        ...
    @staticmethod
    def isWhitespace(*args, **kwargs):
        ...
    @staticmethod
    def lineNumber(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def namespaceDeclarations(*args, **kwargs):
        ...
    @staticmethod
    def namespaceProcessing(*args, **kwargs):
        ...
    @staticmethod
    def namespaceUri(*args, **kwargs):
        ...
    @staticmethod
    def notationDeclarations(*args, **kwargs):
        ...
    @staticmethod
    def prefix(*args, **kwargs):
        ...
    @staticmethod
    def processingInstructionData(*args, **kwargs):
        ...
    @staticmethod
    def processingInstructionTarget(*args, **kwargs):
        ...
    @staticmethod
    def qualifiedName(*args, **kwargs):
        ...
    @staticmethod
    def raiseError(*args, **kwargs):
        ...
    @staticmethod
    def readElementText(*args, **kwargs):
        ...
    @staticmethod
    def readNext(*args, **kwargs):
        ...
    @staticmethod
    def readNextStartElement(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def setEntityExpansionLimit(*args, **kwargs):
        ...
    @staticmethod
    def setEntityResolver(*args, **kwargs):
        ...
    @staticmethod
    def setNamespaceProcessing(*args, **kwargs):
        ...
    @staticmethod
    def skipCurrentElement(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
        ...
    @staticmethod
    def tokenString(*args, **kwargs):
        ...
    @staticmethod
    def tokenType(*args, **kwargs):
        ...
class QXmlStreamWriter(PyQt6.sip.simplewrapper):
    @staticmethod
    def autoFormatting(*args, **kwargs):
        ...
    @staticmethod
    def autoFormattingIndent(*args, **kwargs):
        ...
    @staticmethod
    def device(*args, **kwargs):
        ...
    @staticmethod
    def hasError(*args, **kwargs):
        ...
    @staticmethod
    def setAutoFormatting(*args, **kwargs):
        ...
    @staticmethod
    def setAutoFormattingIndent(*args, **kwargs):
        ...
    @staticmethod
    def setDevice(*args, **kwargs):
        ...
    @staticmethod
    def writeAttribute(*args, **kwargs):
        ...
    @staticmethod
    def writeAttributes(*args, **kwargs):
        ...
    @staticmethod
    def writeCDATA(*args, **kwargs):
        ...
    @staticmethod
    def writeCharacters(*args, **kwargs):
        ...
    @staticmethod
    def writeComment(*args, **kwargs):
        ...
    @staticmethod
    def writeCurrentToken(*args, **kwargs):
        ...
    @staticmethod
    def writeDTD(*args, **kwargs):
        ...
    @staticmethod
    def writeDefaultNamespace(*args, **kwargs):
        ...
    @staticmethod
    def writeEmptyElement(*args, **kwargs):
        ...
    @staticmethod
    def writeEndDocument(*args, **kwargs):
        ...
    @staticmethod
    def writeEndElement(*args, **kwargs):
        ...
    @staticmethod
    def writeEntityReference(*args, **kwargs):
        ...
    @staticmethod
    def writeNamespace(*args, **kwargs):
        ...
    @staticmethod
    def writeProcessingInstruction(*args, **kwargs):
        ...
    @staticmethod
    def writeStartDocument(*args, **kwargs):
        ...
    @staticmethod
    def writeStartElement(*args, **kwargs):
        ...
    @staticmethod
    def writeTextElement(*args, **kwargs):
        ...
class Qt(PyQt6.sip.simplewrapper):
    class AlignmentFlag(enum.IntFlag):
        AlignAbsolute: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignAbsolute: 16>
        AlignBaseline: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignBaseline: 256>
        AlignBottom: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignBottom: 64>
        AlignHCenter: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignHCenter: 4>
        AlignJustify: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignJustify: 8>
        AlignLeft: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignLeft: 1>
        AlignRight: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignRight: 2>
        AlignTop: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignTop: 32>
        AlignVCenter: typing.ClassVar[Qt.AlignmentFlag]  # value = <AlignmentFlag.AlignVCenter: 128>
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
    class AnchorPoint(enum.Enum):
        AnchorBottom: typing.ClassVar[Qt.AnchorPoint]  # value = <AnchorPoint.AnchorBottom: 5>
        AnchorHorizontalCenter: typing.ClassVar[Qt.AnchorPoint]  # value = <AnchorPoint.AnchorHorizontalCenter: 1>
        AnchorLeft: typing.ClassVar[Qt.AnchorPoint]  # value = <AnchorPoint.AnchorLeft: 0>
        AnchorRight: typing.ClassVar[Qt.AnchorPoint]  # value = <AnchorPoint.AnchorRight: 2>
        AnchorTop: typing.ClassVar[Qt.AnchorPoint]  # value = <AnchorPoint.AnchorTop: 3>
        AnchorVerticalCenter: typing.ClassVar[Qt.AnchorPoint]  # value = <AnchorPoint.AnchorVerticalCenter: 4>
    class ApplicationAttribute(enum.Enum):
        AA_CompressHighFrequencyEvents: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_CompressHighFrequencyEvents: 25>
        AA_CompressTabletEvents: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_CompressTabletEvents: 29>
        AA_DisableNativeVirtualKeyboard: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DisableNativeVirtualKeyboard: 9>
        AA_DisableSessionManager: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DisableSessionManager: 31>
        AA_DisableShaderDiskCache: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DisableShaderDiskCache: 27>
        AA_DontCheckOpenGLContextThreadAffinity: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DontCheckOpenGLContextThreadAffinity: 26>
        AA_DontCreateNativeWidgetSiblings: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DontCreateNativeWidgetSiblings: 4>
        AA_DontShowIconsInMenus: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DontShowIconsInMenus: 2>
        AA_DontShowShortcutsInContextMenus: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DontShowShortcutsInContextMenus: 28>
        AA_DontUseNativeDialogs: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DontUseNativeDialogs: 23>
        AA_DontUseNativeMenuBar: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_DontUseNativeMenuBar: 6>
        AA_ForceRasterWidgets: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_ForceRasterWidgets: 14>
        AA_MacDontSwapCtrlAndMeta: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_MacDontSwapCtrlAndMeta: 7>
        AA_NativeWindows: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_NativeWindows: 3>
        AA_PluginApplication: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_PluginApplication: 5>
        AA_QtQuickUseDefaultSizePolicy: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_QtQuickUseDefaultSizePolicy: 1>
        AA_SetPalette: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_SetPalette: 19>
        AA_ShareOpenGLContexts: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_ShareOpenGLContexts: 18>
        AA_SynthesizeMouseForUnhandledTabletEvents: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_SynthesizeMouseForUnhandledTabletEvents: 24>
        AA_SynthesizeMouseForUnhandledTouchEvents: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_SynthesizeMouseForUnhandledTouchEvents: 12>
        AA_SynthesizeTouchForUnhandledMouseEvents: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_SynthesizeTouchForUnhandledMouseEvents: 11>
        AA_Use96Dpi: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_Use96Dpi: 8>
        AA_UseDesktopOpenGL: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_UseDesktopOpenGL: 15>
        AA_UseOpenGLES: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_UseOpenGLES: 16>
        AA_UseSoftwareOpenGL: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_UseSoftwareOpenGL: 17>
        AA_UseStyleSheetPropagationInWidgetStyles: typing.ClassVar[Qt.ApplicationAttribute]  # value = <ApplicationAttribute.AA_UseStyleSheetPropagationInWidgetStyles: 22>
    class ApplicationState(enum.Flag):
        ApplicationActive: typing.ClassVar[Qt.ApplicationState]  # value = <ApplicationState.ApplicationActive: 4>
        ApplicationHidden: typing.ClassVar[Qt.ApplicationState]  # value = <ApplicationState.ApplicationHidden: 1>
        ApplicationInactive: typing.ClassVar[Qt.ApplicationState]  # value = <ApplicationState.ApplicationInactive: 2>
    class ArrowType(enum.Enum):
        DownArrow: typing.ClassVar[Qt.ArrowType]  # value = <ArrowType.DownArrow: 2>
        LeftArrow: typing.ClassVar[Qt.ArrowType]  # value = <ArrowType.LeftArrow: 3>
        NoArrow: typing.ClassVar[Qt.ArrowType]  # value = <ArrowType.NoArrow: 0>
        RightArrow: typing.ClassVar[Qt.ArrowType]  # value = <ArrowType.RightArrow: 4>
        UpArrow: typing.ClassVar[Qt.ArrowType]  # value = <ArrowType.UpArrow: 1>
    class AspectRatioMode(enum.Enum):
        IgnoreAspectRatio: typing.ClassVar[Qt.AspectRatioMode]  # value = <AspectRatioMode.IgnoreAspectRatio: 0>
        KeepAspectRatio: typing.ClassVar[Qt.AspectRatioMode]  # value = <AspectRatioMode.KeepAspectRatio: 1>
        KeepAspectRatioByExpanding: typing.ClassVar[Qt.AspectRatioMode]  # value = <AspectRatioMode.KeepAspectRatioByExpanding: 2>
    class Axis(enum.Enum):
        XAxis: typing.ClassVar[Qt.Axis]  # value = <Axis.XAxis: 0>
        YAxis: typing.ClassVar[Qt.Axis]  # value = <Axis.YAxis: 1>
        ZAxis: typing.ClassVar[Qt.Axis]  # value = <Axis.ZAxis: 2>
    class BGMode(enum.Enum):
        OpaqueMode: typing.ClassVar[Qt.BGMode]  # value = <BGMode.OpaqueMode: 1>
        TransparentMode: typing.ClassVar[Qt.BGMode]  # value = <BGMode.TransparentMode: 0>
    class BrushStyle(enum.Enum):
        BDiagPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.BDiagPattern: 12>
        ConicalGradientPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.ConicalGradientPattern: 17>
        CrossPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.CrossPattern: 11>
        Dense1Pattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.Dense1Pattern: 2>
        Dense2Pattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.Dense2Pattern: 3>
        Dense3Pattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.Dense3Pattern: 4>
        Dense4Pattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.Dense4Pattern: 5>
        Dense5Pattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.Dense5Pattern: 6>
        Dense6Pattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.Dense6Pattern: 7>
        Dense7Pattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.Dense7Pattern: 8>
        DiagCrossPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.DiagCrossPattern: 14>
        FDiagPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.FDiagPattern: 13>
        HorPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.HorPattern: 9>
        LinearGradientPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.LinearGradientPattern: 15>
        NoBrush: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.NoBrush: 0>
        RadialGradientPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.RadialGradientPattern: 16>
        SolidPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.SolidPattern: 1>
        TexturePattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.TexturePattern: 24>
        VerPattern: typing.ClassVar[Qt.BrushStyle]  # value = <BrushStyle.VerPattern: 10>
    class CaseSensitivity(enum.Enum):
        CaseInsensitive: typing.ClassVar[Qt.CaseSensitivity]  # value = <CaseSensitivity.CaseInsensitive: 0>
        CaseSensitive: typing.ClassVar[Qt.CaseSensitivity]  # value = <CaseSensitivity.CaseSensitive: 1>
    class CheckState(enum.Enum):
        Checked: typing.ClassVar[Qt.CheckState]  # value = <CheckState.Checked: 2>
        PartiallyChecked: typing.ClassVar[Qt.CheckState]  # value = <CheckState.PartiallyChecked: 1>
        Unchecked: typing.ClassVar[Qt.CheckState]  # value = <CheckState.Unchecked: 0>
    class ChecksumType(enum.Enum):
        ChecksumIso3309: typing.ClassVar[Qt.ChecksumType]  # value = <ChecksumType.ChecksumIso3309: 0>
        ChecksumItuV41: typing.ClassVar[Qt.ChecksumType]  # value = <ChecksumType.ChecksumItuV41: 1>
    class ClipOperation(enum.Enum):
        IntersectClip: typing.ClassVar[Qt.ClipOperation]  # value = <ClipOperation.IntersectClip: 2>
        NoClip: typing.ClassVar[Qt.ClipOperation]  # value = <ClipOperation.NoClip: 0>
        ReplaceClip: typing.ClassVar[Qt.ClipOperation]  # value = <ClipOperation.ReplaceClip: 1>
    class ColorScheme(enum.Enum):
        Dark: typing.ClassVar[Qt.ColorScheme]  # value = <ColorScheme.Dark: 2>
        Light: typing.ClassVar[Qt.ColorScheme]  # value = <ColorScheme.Light: 1>
        Unknown: typing.ClassVar[Qt.ColorScheme]  # value = <ColorScheme.Unknown: 0>
    class ConnectionType(enum.Enum):
        AutoConnection: typing.ClassVar[Qt.ConnectionType]  # value = <ConnectionType.AutoConnection: 0>
        BlockingQueuedConnection: typing.ClassVar[Qt.ConnectionType]  # value = <ConnectionType.BlockingQueuedConnection: 3>
        DirectConnection: typing.ClassVar[Qt.ConnectionType]  # value = <ConnectionType.DirectConnection: 1>
        QueuedConnection: typing.ClassVar[Qt.ConnectionType]  # value = <ConnectionType.QueuedConnection: 2>
        SingleShotConnection: typing.ClassVar[Qt.ConnectionType]  # value = <ConnectionType.SingleShotConnection: 256>
        UniqueConnection: typing.ClassVar[Qt.ConnectionType]  # value = <ConnectionType.UniqueConnection: 128>
    class ContextMenuPolicy(enum.Enum):
        ActionsContextMenu: typing.ClassVar[Qt.ContextMenuPolicy]  # value = <ContextMenuPolicy.ActionsContextMenu: 2>
        CustomContextMenu: typing.ClassVar[Qt.ContextMenuPolicy]  # value = <ContextMenuPolicy.CustomContextMenu: 3>
        DefaultContextMenu: typing.ClassVar[Qt.ContextMenuPolicy]  # value = <ContextMenuPolicy.DefaultContextMenu: 1>
        NoContextMenu: typing.ClassVar[Qt.ContextMenuPolicy]  # value = <ContextMenuPolicy.NoContextMenu: 0>
        PreventContextMenu: typing.ClassVar[Qt.ContextMenuPolicy]  # value = <ContextMenuPolicy.PreventContextMenu: 4>
    class CoordinateSystem(enum.Enum):
        DeviceCoordinates: typing.ClassVar[Qt.CoordinateSystem]  # value = <CoordinateSystem.DeviceCoordinates: 0>
        LogicalCoordinates: typing.ClassVar[Qt.CoordinateSystem]  # value = <CoordinateSystem.LogicalCoordinates: 1>
    class Corner(enum.Enum):
        BottomLeftCorner: typing.ClassVar[Qt.Corner]  # value = <Corner.BottomLeftCorner: 2>
        BottomRightCorner: typing.ClassVar[Qt.Corner]  # value = <Corner.BottomRightCorner: 3>
        TopLeftCorner: typing.ClassVar[Qt.Corner]  # value = <Corner.TopLeftCorner: 0>
        TopRightCorner: typing.ClassVar[Qt.Corner]  # value = <Corner.TopRightCorner: 1>
    class CursorMoveStyle(enum.Enum):
        LogicalMoveStyle: typing.ClassVar[Qt.CursorMoveStyle]  # value = <CursorMoveStyle.LogicalMoveStyle: 0>
        VisualMoveStyle: typing.ClassVar[Qt.CursorMoveStyle]  # value = <CursorMoveStyle.VisualMoveStyle: 1>
    class CursorShape(enum.Enum):
        ArrowCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.ArrowCursor: 0>
        BitmapCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.BitmapCursor: 24>
        BlankCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.BlankCursor: 10>
        BusyCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.BusyCursor: 16>
        ClosedHandCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.ClosedHandCursor: 18>
        CrossCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.CrossCursor: 2>
        CustomCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.CustomCursor: 25>
        DragCopyCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.DragCopyCursor: 19>
        DragMoveCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.DragMoveCursor: 20>
        ForbiddenCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.ForbiddenCursor: 14>
        IBeamCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.IBeamCursor: 4>
        LastCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.LastCursor: 21>
        OpenHandCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.OpenHandCursor: 17>
        PointingHandCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.PointingHandCursor: 13>
        SizeAllCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.SizeAllCursor: 9>
        SizeBDiagCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.SizeBDiagCursor: 7>
        SizeFDiagCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.SizeFDiagCursor: 8>
        SizeHorCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.SizeHorCursor: 6>
        SizeVerCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.SizeVerCursor: 5>
        SplitHCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.SplitHCursor: 12>
        SplitVCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.SplitVCursor: 11>
        UpArrowCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.UpArrowCursor: 1>
        WaitCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.WaitCursor: 3>
        WhatsThisCursor: typing.ClassVar[Qt.CursorShape]  # value = <CursorShape.WhatsThisCursor: 15>
    class DateFormat(enum.Enum):
        ISODate: typing.ClassVar[Qt.DateFormat]  # value = <DateFormat.ISODate: 1>
        ISODateWithMs: typing.ClassVar[Qt.DateFormat]  # value = <DateFormat.ISODateWithMs: 9>
        RFC2822Date: typing.ClassVar[Qt.DateFormat]  # value = <DateFormat.RFC2822Date: 8>
        TextDate: typing.ClassVar[Qt.DateFormat]  # value = <DateFormat.TextDate: 0>
    class DayOfWeek(enum.Enum):
        Friday: typing.ClassVar[Qt.DayOfWeek]  # value = <DayOfWeek.Friday: 5>
        Monday: typing.ClassVar[Qt.DayOfWeek]  # value = <DayOfWeek.Monday: 1>
        Saturday: typing.ClassVar[Qt.DayOfWeek]  # value = <DayOfWeek.Saturday: 6>
        Sunday: typing.ClassVar[Qt.DayOfWeek]  # value = <DayOfWeek.Sunday: 7>
        Thursday: typing.ClassVar[Qt.DayOfWeek]  # value = <DayOfWeek.Thursday: 4>
        Tuesday: typing.ClassVar[Qt.DayOfWeek]  # value = <DayOfWeek.Tuesday: 2>
        Wednesday: typing.ClassVar[Qt.DayOfWeek]  # value = <DayOfWeek.Wednesday: 3>
    class DockWidgetArea(enum.Flag):
        BottomDockWidgetArea: typing.ClassVar[Qt.DockWidgetArea]  # value = <DockWidgetArea.BottomDockWidgetArea: 8>
        LeftDockWidgetArea: typing.ClassVar[Qt.DockWidgetArea]  # value = <DockWidgetArea.LeftDockWidgetArea: 1>
        RightDockWidgetArea: typing.ClassVar[Qt.DockWidgetArea]  # value = <DockWidgetArea.RightDockWidgetArea: 2>
        TopDockWidgetArea: typing.ClassVar[Qt.DockWidgetArea]  # value = <DockWidgetArea.TopDockWidgetArea: 4>
    class DropAction(enum.Flag):
        CopyAction: typing.ClassVar[Qt.DropAction]  # value = <DropAction.CopyAction: 1>
        LinkAction: typing.ClassVar[Qt.DropAction]  # value = <DropAction.LinkAction: 4>
        MoveAction: typing.ClassVar[Qt.DropAction]  # value = <DropAction.MoveAction: 2>
    class Edge(enum.Flag):
        BottomEdge: typing.ClassVar[Qt.Edge]  # value = <Edge.BottomEdge: 8>
        LeftEdge: typing.ClassVar[Qt.Edge]  # value = <Edge.LeftEdge: 2>
        RightEdge: typing.ClassVar[Qt.Edge]  # value = <Edge.RightEdge: 4>
        TopEdge: typing.ClassVar[Qt.Edge]  # value = <Edge.TopEdge: 1>
    class EnterKeyType(enum.Enum):
        EnterKeyDefault: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeyDefault: 0>
        EnterKeyDone: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeyDone: 2>
        EnterKeyGo: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeyGo: 3>
        EnterKeyNext: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeyNext: 6>
        EnterKeyPrevious: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeyPrevious: 7>
        EnterKeyReturn: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeyReturn: 1>
        EnterKeySearch: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeySearch: 5>
        EnterKeySend: typing.ClassVar[Qt.EnterKeyType]  # value = <EnterKeyType.EnterKeySend: 4>
    class EventPriority(enum.Enum):
        HighEventPriority: typing.ClassVar[Qt.EventPriority]  # value = <EventPriority.HighEventPriority: 1>
        LowEventPriority: typing.ClassVar[Qt.EventPriority]  # value = <EventPriority.LowEventPriority: -1>
        NormalEventPriority: typing.ClassVar[Qt.EventPriority]  # value = <EventPriority.NormalEventPriority: 0>
    class FillRule(enum.Enum):
        OddEvenFill: typing.ClassVar[Qt.FillRule]  # value = <FillRule.OddEvenFill: 0>
        WindingFill: typing.ClassVar[Qt.FillRule]  # value = <FillRule.WindingFill: 1>
    class FindChildOption(enum.Flag):
        FindChildrenRecursively: typing.ClassVar[Qt.FindChildOption]  # value = <FindChildOption.FindChildrenRecursively: 1>
    class FocusPolicy(enum.IntFlag):
        ClickFocus: typing.ClassVar[Qt.FocusPolicy]  # value = <FocusPolicy.ClickFocus: 2>
        TabFocus: typing.ClassVar[Qt.FocusPolicy]  # value = <FocusPolicy.TabFocus: 1>
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
    class FocusReason(enum.Enum):
        ActiveWindowFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.ActiveWindowFocusReason: 3>
        BacktabFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.BacktabFocusReason: 2>
        MenuBarFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.MenuBarFocusReason: 6>
        MouseFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.MouseFocusReason: 0>
        NoFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.NoFocusReason: 8>
        OtherFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.OtherFocusReason: 7>
        PopupFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.PopupFocusReason: 4>
        ShortcutFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.ShortcutFocusReason: 5>
        TabFocusReason: typing.ClassVar[Qt.FocusReason]  # value = <FocusReason.TabFocusReason: 1>
    class GestureFlag(enum.Flag):
        DontStartGestureOnChildren: typing.ClassVar[Qt.GestureFlag]  # value = <GestureFlag.DontStartGestureOnChildren: 1>
        IgnoredGesturesPropagateToParent: typing.ClassVar[Qt.GestureFlag]  # value = <GestureFlag.IgnoredGesturesPropagateToParent: 4>
        ReceivePartialGestures: typing.ClassVar[Qt.GestureFlag]  # value = <GestureFlag.ReceivePartialGestures: 2>
    class GestureState(enum.Enum):
        GestureCanceled: typing.ClassVar[Qt.GestureState]  # value = <GestureState.GestureCanceled: 4>
        GestureFinished: typing.ClassVar[Qt.GestureState]  # value = <GestureState.GestureFinished: 3>
        GestureStarted: typing.ClassVar[Qt.GestureState]  # value = <GestureState.GestureStarted: 1>
        GestureUpdated: typing.ClassVar[Qt.GestureState]  # value = <GestureState.GestureUpdated: 2>
    class GestureType(enum.IntEnum):
        CustomGesture: typing.ClassVar[Qt.GestureType]  # value = <GestureType.CustomGesture: 256>
        PanGesture: typing.ClassVar[Qt.GestureType]  # value = <GestureType.PanGesture: 3>
        PinchGesture: typing.ClassVar[Qt.GestureType]  # value = <GestureType.PinchGesture: 4>
        SwipeGesture: typing.ClassVar[Qt.GestureType]  # value = <GestureType.SwipeGesture: 5>
        TapAndHoldGesture: typing.ClassVar[Qt.GestureType]  # value = <GestureType.TapAndHoldGesture: 2>
        TapGesture: typing.ClassVar[Qt.GestureType]  # value = <GestureType.TapGesture: 1>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class GlobalColor(enum.Enum):
        black: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.black: 2>
        blue: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.blue: 9>
        color0: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.color0: 0>
        color1: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.color1: 1>
        cyan: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.cyan: 10>
        darkBlue: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.darkBlue: 15>
        darkCyan: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.darkCyan: 16>
        darkGray: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.darkGray: 4>
        darkGreen: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.darkGreen: 14>
        darkMagenta: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.darkMagenta: 17>
        darkRed: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.darkRed: 13>
        darkYellow: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.darkYellow: 18>
        gray: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.gray: 5>
        green: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.green: 8>
        lightGray: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.lightGray: 6>
        magenta: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.magenta: 11>
        red: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.red: 7>
        transparent: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.transparent: 19>
        white: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.white: 3>
        yellow: typing.ClassVar[Qt.GlobalColor]  # value = <GlobalColor.yellow: 12>
    class HighDpiScaleFactorRoundingPolicy(enum.Enum):
        Ceil: typing.ClassVar[Qt.HighDpiScaleFactorRoundingPolicy]  # value = <HighDpiScaleFactorRoundingPolicy.Ceil: 2>
        Floor: typing.ClassVar[Qt.HighDpiScaleFactorRoundingPolicy]  # value = <HighDpiScaleFactorRoundingPolicy.Floor: 3>
        PassThrough: typing.ClassVar[Qt.HighDpiScaleFactorRoundingPolicy]  # value = <HighDpiScaleFactorRoundingPolicy.PassThrough: 5>
        Round: typing.ClassVar[Qt.HighDpiScaleFactorRoundingPolicy]  # value = <HighDpiScaleFactorRoundingPolicy.Round: 1>
        RoundPreferFloor: typing.ClassVar[Qt.HighDpiScaleFactorRoundingPolicy]  # value = <HighDpiScaleFactorRoundingPolicy.RoundPreferFloor: 4>
    class HitTestAccuracy(enum.Enum):
        ExactHit: typing.ClassVar[Qt.HitTestAccuracy]  # value = <HitTestAccuracy.ExactHit: 0>
        FuzzyHit: typing.ClassVar[Qt.HitTestAccuracy]  # value = <HitTestAccuracy.FuzzyHit: 1>
    class ImageConversionFlag(enum.Flag):
        AvoidDither: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.AvoidDither: 128>
        DiffuseAlphaDither: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.DiffuseAlphaDither: 8>
        MonoOnly: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.MonoOnly: 2>
        NoFormatConversion: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.NoFormatConversion: 512>
        NoOpaqueDetection: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.NoOpaqueDetection: 256>
        OrderedAlphaDither: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.OrderedAlphaDither: 4>
        OrderedDither: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.OrderedDither: 16>
        PreferDither: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.PreferDither: 64>
        ThresholdDither: typing.ClassVar[Qt.ImageConversionFlag]  # value = <ImageConversionFlag.ThresholdDither: 32>
    class InputMethodHint(enum.Flag):
        ImhDate: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhDate: 128>
        ImhDialableCharactersOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhDialableCharactersOnly: 1048576>
        ImhDigitsOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhDigitsOnly: 65536>
        ImhEmailCharactersOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhEmailCharactersOnly: 2097152>
        ImhFormattedNumbersOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhFormattedNumbersOnly: 131072>
        ImhHiddenText: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhHiddenText: 1>
        ImhLatinOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhLatinOnly: 8388608>
        ImhLowercaseOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhLowercaseOnly: 524288>
        ImhMultiLine: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhMultiLine: 1024>
        ImhNoAutoUppercase: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhNoAutoUppercase: 4>
        ImhNoEditMenu: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhNoEditMenu: 2048>
        ImhNoPredictiveText: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhNoPredictiveText: 64>
        ImhNoTextHandles: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhNoTextHandles: 4096>
        ImhPreferLatin: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhPreferLatin: 512>
        ImhPreferLowercase: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhPreferLowercase: 32>
        ImhPreferNumbers: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhPreferNumbers: 8>
        ImhPreferUppercase: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhPreferUppercase: 16>
        ImhSensitiveData: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhSensitiveData: 2>
        ImhTime: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhTime: 256>
        ImhUppercaseOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhUppercaseOnly: 262144>
        ImhUrlCharactersOnly: typing.ClassVar[Qt.InputMethodHint]  # value = <InputMethodHint.ImhUrlCharactersOnly: 4194304>
    class InputMethodQuery(enum.Flag):
        ImAbsolutePosition: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImAbsolutePosition: 1024>
        ImAnchorPosition: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImAnchorPosition: 128>
        ImAnchorRectangle: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImAnchorRectangle: 16384>
        ImCurrentSelection: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImCurrentSelection: 32>
        ImCursorPosition: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImCursorPosition: 8>
        ImCursorRectangle: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImCursorRectangle: 2>
        ImEnabled: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImEnabled: 1>
        ImEnterKeyType: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImEnterKeyType: 8192>
        ImFont: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImFont: 4>
        ImHints: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImHints: 256>
        ImInputItemClipRectangle: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImInputItemClipRectangle: 32768>
        ImMaximumTextLength: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImMaximumTextLength: 64>
        ImPlatformData: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImPlatformData: 2147483648>
        ImPreferredLanguage: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImPreferredLanguage: 512>
        ImReadOnly: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImReadOnly: 65536>
        ImSurroundingText: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImSurroundingText: 16>
        ImTextAfterCursor: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImTextAfterCursor: 4096>
        ImTextBeforeCursor: typing.ClassVar[Qt.InputMethodQuery]  # value = <InputMethodQuery.ImTextBeforeCursor: 2048>
    class ItemDataRole(enum.IntEnum):
        AccessibleDescriptionRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.AccessibleDescriptionRole: 12>
        AccessibleTextRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.AccessibleTextRole: 11>
        BackgroundRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.BackgroundRole: 8>
        CheckStateRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.CheckStateRole: 10>
        DecorationRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.DecorationRole: 1>
        DisplayRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.DisplayRole: 0>
        EditRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.EditRole: 2>
        FontRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.FontRole: 6>
        ForegroundRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.ForegroundRole: 9>
        InitialSortOrderRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.InitialSortOrderRole: 14>
        SizeHintRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.SizeHintRole: 13>
        StatusTipRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.StatusTipRole: 4>
        TextAlignmentRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.TextAlignmentRole: 7>
        ToolTipRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.ToolTipRole: 3>
        UserRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.UserRole: 256>
        WhatsThisRole: typing.ClassVar[Qt.ItemDataRole]  # value = <ItemDataRole.WhatsThisRole: 5>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class ItemFlag(enum.Flag):
        ItemIsAutoTristate: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsAutoTristate: 64>
        ItemIsDragEnabled: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsDragEnabled: 4>
        ItemIsDropEnabled: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsDropEnabled: 8>
        ItemIsEditable: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsEditable: 2>
        ItemIsEnabled: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsEnabled: 32>
        ItemIsSelectable: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsSelectable: 1>
        ItemIsUserCheckable: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsUserCheckable: 16>
        ItemIsUserTristate: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemIsUserTristate: 256>
        ItemNeverHasChildren: typing.ClassVar[Qt.ItemFlag]  # value = <ItemFlag.ItemNeverHasChildren: 128>
    class ItemSelectionMode(enum.Enum):
        ContainsItemBoundingRect: typing.ClassVar[Qt.ItemSelectionMode]  # value = <ItemSelectionMode.ContainsItemBoundingRect: 2>
        ContainsItemShape: typing.ClassVar[Qt.ItemSelectionMode]  # value = <ItemSelectionMode.ContainsItemShape: 0>
        IntersectsItemBoundingRect: typing.ClassVar[Qt.ItemSelectionMode]  # value = <ItemSelectionMode.IntersectsItemBoundingRect: 3>
        IntersectsItemShape: typing.ClassVar[Qt.ItemSelectionMode]  # value = <ItemSelectionMode.IntersectsItemShape: 1>
    class ItemSelectionOperation(enum.Enum):
        AddToSelection: typing.ClassVar[Qt.ItemSelectionOperation]  # value = <ItemSelectionOperation.AddToSelection: 1>
        ReplaceSelection: typing.ClassVar[Qt.ItemSelectionOperation]  # value = <ItemSelectionOperation.ReplaceSelection: 0>
    class Key(enum.IntEnum):
        Key_0: typing.ClassVar[Qt.Key]  # value = <Key.Key_0: 48>
        Key_1: typing.ClassVar[Qt.Key]  # value = <Key.Key_1: 49>
        Key_2: typing.ClassVar[Qt.Key]  # value = <Key.Key_2: 50>
        Key_3: typing.ClassVar[Qt.Key]  # value = <Key.Key_3: 51>
        Key_4: typing.ClassVar[Qt.Key]  # value = <Key.Key_4: 52>
        Key_5: typing.ClassVar[Qt.Key]  # value = <Key.Key_5: 53>
        Key_6: typing.ClassVar[Qt.Key]  # value = <Key.Key_6: 54>
        Key_7: typing.ClassVar[Qt.Key]  # value = <Key.Key_7: 55>
        Key_8: typing.ClassVar[Qt.Key]  # value = <Key.Key_8: 56>
        Key_9: typing.ClassVar[Qt.Key]  # value = <Key.Key_9: 57>
        Key_A: typing.ClassVar[Qt.Key]  # value = <Key.Key_A: 65>
        Key_AE: typing.ClassVar[Qt.Key]  # value = <Key.Key_AE: 198>
        Key_Aacute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Aacute: 193>
        Key_Acircumflex: typing.ClassVar[Qt.Key]  # value = <Key.Key_Acircumflex: 194>
        Key_AddFavorite: typing.ClassVar[Qt.Key]  # value = <Key.Key_AddFavorite: 16777408>
        Key_Adiaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_Adiaeresis: 196>
        Key_Agrave: typing.ClassVar[Qt.Key]  # value = <Key.Key_Agrave: 192>
        Key_Alt: typing.ClassVar[Qt.Key]  # value = <Key.Key_Alt: 16777251>
        Key_AltGr: typing.ClassVar[Qt.Key]  # value = <Key.Key_AltGr: 16781571>
        Key_Ampersand: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ampersand: 38>
        Key_Apostrophe: typing.ClassVar[Qt.Key]  # value = <Key.Key_Apostrophe: 39>
        Key_ApplicationLeft: typing.ClassVar[Qt.Key]  # value = <Key.Key_ApplicationLeft: 16777415>
        Key_ApplicationRight: typing.ClassVar[Qt.Key]  # value = <Key.Key_ApplicationRight: 16777416>
        Key_Aring: typing.ClassVar[Qt.Key]  # value = <Key.Key_Aring: 197>
        Key_AsciiCircum: typing.ClassVar[Qt.Key]  # value = <Key.Key_AsciiCircum: 94>
        Key_AsciiTilde: typing.ClassVar[Qt.Key]  # value = <Key.Key_AsciiTilde: 126>
        Key_Asterisk: typing.ClassVar[Qt.Key]  # value = <Key.Key_Asterisk: 42>
        Key_At: typing.ClassVar[Qt.Key]  # value = <Key.Key_At: 64>
        Key_Atilde: typing.ClassVar[Qt.Key]  # value = <Key.Key_Atilde: 195>
        Key_AudioCycleTrack: typing.ClassVar[Qt.Key]  # value = <Key.Key_AudioCycleTrack: 16777478>
        Key_AudioForward: typing.ClassVar[Qt.Key]  # value = <Key.Key_AudioForward: 16777474>
        Key_AudioRandomPlay: typing.ClassVar[Qt.Key]  # value = <Key.Key_AudioRandomPlay: 16777476>
        Key_AudioRepeat: typing.ClassVar[Qt.Key]  # value = <Key.Key_AudioRepeat: 16777475>
        Key_AudioRewind: typing.ClassVar[Qt.Key]  # value = <Key.Key_AudioRewind: 16777413>
        Key_Away: typing.ClassVar[Qt.Key]  # value = <Key.Key_Away: 16777464>
        Key_B: typing.ClassVar[Qt.Key]  # value = <Key.Key_B: 66>
        Key_Back: typing.ClassVar[Qt.Key]  # value = <Key.Key_Back: 16777313>
        Key_BackForward: typing.ClassVar[Qt.Key]  # value = <Key.Key_BackForward: 16777414>
        Key_Backslash: typing.ClassVar[Qt.Key]  # value = <Key.Key_Backslash: 92>
        Key_Backspace: typing.ClassVar[Qt.Key]  # value = <Key.Key_Backspace: 16777219>
        Key_Backtab: typing.ClassVar[Qt.Key]  # value = <Key.Key_Backtab: 16777218>
        Key_Bar: typing.ClassVar[Qt.Key]  # value = <Key.Key_Bar: 124>
        Key_BassBoost: typing.ClassVar[Qt.Key]  # value = <Key.Key_BassBoost: 16777331>
        Key_BassDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_BassDown: 16777333>
        Key_BassUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_BassUp: 16777332>
        Key_Battery: typing.ClassVar[Qt.Key]  # value = <Key.Key_Battery: 16777470>
        Key_Blue: typing.ClassVar[Qt.Key]  # value = <Key.Key_Blue: 16777495>
        Key_Bluetooth: typing.ClassVar[Qt.Key]  # value = <Key.Key_Bluetooth: 16777471>
        Key_Book: typing.ClassVar[Qt.Key]  # value = <Key.Key_Book: 16777417>
        Key_BraceLeft: typing.ClassVar[Qt.Key]  # value = <Key.Key_BraceLeft: 123>
        Key_BraceRight: typing.ClassVar[Qt.Key]  # value = <Key.Key_BraceRight: 125>
        Key_BracketLeft: typing.ClassVar[Qt.Key]  # value = <Key.Key_BracketLeft: 91>
        Key_BracketRight: typing.ClassVar[Qt.Key]  # value = <Key.Key_BracketRight: 93>
        Key_BrightnessAdjust: typing.ClassVar[Qt.Key]  # value = <Key.Key_BrightnessAdjust: 16777410>
        Key_C: typing.ClassVar[Qt.Key]  # value = <Key.Key_C: 67>
        Key_CD: typing.ClassVar[Qt.Key]  # value = <Key.Key_CD: 16777418>
        Key_Calculator: typing.ClassVar[Qt.Key]  # value = <Key.Key_Calculator: 16777419>
        Key_Calendar: typing.ClassVar[Qt.Key]  # value = <Key.Key_Calendar: 16777444>
        Key_Call: typing.ClassVar[Qt.Key]  # value = <Key.Key_Call: 17825796>
        Key_Camera: typing.ClassVar[Qt.Key]  # value = <Key.Key_Camera: 17825824>
        Key_CameraFocus: typing.ClassVar[Qt.Key]  # value = <Key.Key_CameraFocus: 17825825>
        Key_Cancel: typing.ClassVar[Qt.Key]  # value = <Key.Key_Cancel: 16908289>
        Key_CapsLock: typing.ClassVar[Qt.Key]  # value = <Key.Key_CapsLock: 16777252>
        Key_Ccedilla: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ccedilla: 199>
        Key_ChannelDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_ChannelDown: 16777497>
        Key_ChannelUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_ChannelUp: 16777496>
        Key_Clear: typing.ClassVar[Qt.Key]  # value = <Key.Key_Clear: 16777227>
        Key_ClearGrab: typing.ClassVar[Qt.Key]  # value = <Key.Key_ClearGrab: 16777421>
        Key_Close: typing.ClassVar[Qt.Key]  # value = <Key.Key_Close: 16777422>
        Key_Codeinput: typing.ClassVar[Qt.Key]  # value = <Key.Key_Codeinput: 16781623>
        Key_Colon: typing.ClassVar[Qt.Key]  # value = <Key.Key_Colon: 58>
        Key_Comma: typing.ClassVar[Qt.Key]  # value = <Key.Key_Comma: 44>
        Key_Community: typing.ClassVar[Qt.Key]  # value = <Key.Key_Community: 16777412>
        Key_Context1: typing.ClassVar[Qt.Key]  # value = <Key.Key_Context1: 17825792>
        Key_Context2: typing.ClassVar[Qt.Key]  # value = <Key.Key_Context2: 17825793>
        Key_Context3: typing.ClassVar[Qt.Key]  # value = <Key.Key_Context3: 17825794>
        Key_Context4: typing.ClassVar[Qt.Key]  # value = <Key.Key_Context4: 17825795>
        Key_ContrastAdjust: typing.ClassVar[Qt.Key]  # value = <Key.Key_ContrastAdjust: 16777485>
        Key_Control: typing.ClassVar[Qt.Key]  # value = <Key.Key_Control: 16777249>
        Key_Copy: typing.ClassVar[Qt.Key]  # value = <Key.Key_Copy: 16777423>
        Key_Cut: typing.ClassVar[Qt.Key]  # value = <Key.Key_Cut: 16777424>
        Key_D: typing.ClassVar[Qt.Key]  # value = <Key.Key_D: 68>
        Key_DOS: typing.ClassVar[Qt.Key]  # value = <Key.Key_DOS: 16777426>
        Key_Dead_A: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_A: 16781953>
        Key_Dead_Abovecomma: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Abovecomma: 16781924>
        Key_Dead_Abovedot: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Abovedot: 16781910>
        Key_Dead_Abovereversedcomma: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Abovereversedcomma: 16781925>
        Key_Dead_Abovering: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Abovering: 16781912>
        Key_Dead_Aboveverticalline: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Aboveverticalline: 16781969>
        Key_Dead_Acute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Acute: 16781905>
        Key_Dead_Belowbreve: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowbreve: 16781931>
        Key_Dead_Belowcircumflex: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowcircumflex: 16781929>
        Key_Dead_Belowcomma: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowcomma: 16781934>
        Key_Dead_Belowdiaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowdiaeresis: 16781932>
        Key_Dead_Belowdot: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowdot: 16781920>
        Key_Dead_Belowmacron: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowmacron: 16781928>
        Key_Dead_Belowring: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowring: 16781927>
        Key_Dead_Belowtilde: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowtilde: 16781930>
        Key_Dead_Belowverticalline: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Belowverticalline: 16781970>
        Key_Dead_Breve: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Breve: 16781909>
        Key_Dead_Capital_Schwa: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Capital_Schwa: 16781963>
        Key_Dead_Caron: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Caron: 16781914>
        Key_Dead_Cedilla: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Cedilla: 16781915>
        Key_Dead_Circumflex: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Circumflex: 16781906>
        Key_Dead_Currency: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Currency: 16781935>
        Key_Dead_Diaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Diaeresis: 16781911>
        Key_Dead_Doubleacute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Doubleacute: 16781913>
        Key_Dead_Doublegrave: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Doublegrave: 16781926>
        Key_Dead_E: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_E: 16781955>
        Key_Dead_Grave: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Grave: 16781904>
        Key_Dead_Greek: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Greek: 16781964>
        Key_Dead_Hook: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Hook: 16781921>
        Key_Dead_Horn: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Horn: 16781922>
        Key_Dead_I: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_I: 16781957>
        Key_Dead_Invertedbreve: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Invertedbreve: 16781933>
        Key_Dead_Iota: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Iota: 16781917>
        Key_Dead_Longsolidusoverlay: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Longsolidusoverlay: 16781971>
        Key_Dead_Lowline: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Lowline: 16781968>
        Key_Dead_Macron: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Macron: 16781908>
        Key_Dead_O: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_O: 16781959>
        Key_Dead_Ogonek: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Ogonek: 16781916>
        Key_Dead_Semivoiced_Sound: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Semivoiced_Sound: 16781919>
        Key_Dead_Small_Schwa: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Small_Schwa: 16781962>
        Key_Dead_Stroke: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Stroke: 16781923>
        Key_Dead_Tilde: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Tilde: 16781907>
        Key_Dead_U: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_U: 16781961>
        Key_Dead_Voiced_Sound: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_Voiced_Sound: 16781918>
        Key_Dead_a: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_a: 16781952>
        Key_Dead_e: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_e: 16781954>
        Key_Dead_i: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_i: 16781956>
        Key_Dead_o: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_o: 16781958>
        Key_Dead_u: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dead_u: 16781960>
        Key_Delete: typing.ClassVar[Qt.Key]  # value = <Key.Key_Delete: 16777223>
        Key_Direction_L: typing.ClassVar[Qt.Key]  # value = <Key.Key_Direction_L: 16777305>
        Key_Direction_R: typing.ClassVar[Qt.Key]  # value = <Key.Key_Direction_R: 16777312>
        Key_Display: typing.ClassVar[Qt.Key]  # value = <Key.Key_Display: 16777425>
        Key_Documents: typing.ClassVar[Qt.Key]  # value = <Key.Key_Documents: 16777427>
        Key_Dollar: typing.ClassVar[Qt.Key]  # value = <Key.Key_Dollar: 36>
        Key_Down: typing.ClassVar[Qt.Key]  # value = <Key.Key_Down: 16777237>
        Key_E: typing.ClassVar[Qt.Key]  # value = <Key.Key_E: 69>
        Key_ETH: typing.ClassVar[Qt.Key]  # value = <Key.Key_ETH: 208>
        Key_Eacute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Eacute: 201>
        Key_Ecircumflex: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ecircumflex: 202>
        Key_Ediaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ediaeresis: 203>
        Key_Egrave: typing.ClassVar[Qt.Key]  # value = <Key.Key_Egrave: 200>
        Key_Eisu_Shift: typing.ClassVar[Qt.Key]  # value = <Key.Key_Eisu_Shift: 16781615>
        Key_Eisu_toggle: typing.ClassVar[Qt.Key]  # value = <Key.Key_Eisu_toggle: 16781616>
        Key_Eject: typing.ClassVar[Qt.Key]  # value = <Key.Key_Eject: 16777401>
        Key_End: typing.ClassVar[Qt.Key]  # value = <Key.Key_End: 16777233>
        Key_Enter: typing.ClassVar[Qt.Key]  # value = <Key.Key_Enter: 16777221>
        Key_Equal: typing.ClassVar[Qt.Key]  # value = <Key.Key_Equal: 61>
        Key_Escape: typing.ClassVar[Qt.Key]  # value = <Key.Key_Escape: 16777216>
        Key_Excel: typing.ClassVar[Qt.Key]  # value = <Key.Key_Excel: 16777428>
        Key_Exclam: typing.ClassVar[Qt.Key]  # value = <Key.Key_Exclam: 33>
        Key_Execute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Execute: 16908291>
        Key_Exit: typing.ClassVar[Qt.Key]  # value = <Key.Key_Exit: 16908298>
        Key_Explorer: typing.ClassVar[Qt.Key]  # value = <Key.Key_Explorer: 16777429>
        Key_F: typing.ClassVar[Qt.Key]  # value = <Key.Key_F: 70>
        Key_F1: typing.ClassVar[Qt.Key]  # value = <Key.Key_F1: 16777264>
        Key_F10: typing.ClassVar[Qt.Key]  # value = <Key.Key_F10: 16777273>
        Key_F11: typing.ClassVar[Qt.Key]  # value = <Key.Key_F11: 16777274>
        Key_F12: typing.ClassVar[Qt.Key]  # value = <Key.Key_F12: 16777275>
        Key_F13: typing.ClassVar[Qt.Key]  # value = <Key.Key_F13: 16777276>
        Key_F14: typing.ClassVar[Qt.Key]  # value = <Key.Key_F14: 16777277>
        Key_F15: typing.ClassVar[Qt.Key]  # value = <Key.Key_F15: 16777278>
        Key_F16: typing.ClassVar[Qt.Key]  # value = <Key.Key_F16: 16777279>
        Key_F17: typing.ClassVar[Qt.Key]  # value = <Key.Key_F17: 16777280>
        Key_F18: typing.ClassVar[Qt.Key]  # value = <Key.Key_F18: 16777281>
        Key_F19: typing.ClassVar[Qt.Key]  # value = <Key.Key_F19: 16777282>
        Key_F2: typing.ClassVar[Qt.Key]  # value = <Key.Key_F2: 16777265>
        Key_F20: typing.ClassVar[Qt.Key]  # value = <Key.Key_F20: 16777283>
        Key_F21: typing.ClassVar[Qt.Key]  # value = <Key.Key_F21: 16777284>
        Key_F22: typing.ClassVar[Qt.Key]  # value = <Key.Key_F22: 16777285>
        Key_F23: typing.ClassVar[Qt.Key]  # value = <Key.Key_F23: 16777286>
        Key_F24: typing.ClassVar[Qt.Key]  # value = <Key.Key_F24: 16777287>
        Key_F25: typing.ClassVar[Qt.Key]  # value = <Key.Key_F25: 16777288>
        Key_F26: typing.ClassVar[Qt.Key]  # value = <Key.Key_F26: 16777289>
        Key_F27: typing.ClassVar[Qt.Key]  # value = <Key.Key_F27: 16777290>
        Key_F28: typing.ClassVar[Qt.Key]  # value = <Key.Key_F28: 16777291>
        Key_F29: typing.ClassVar[Qt.Key]  # value = <Key.Key_F29: 16777292>
        Key_F3: typing.ClassVar[Qt.Key]  # value = <Key.Key_F3: 16777266>
        Key_F30: typing.ClassVar[Qt.Key]  # value = <Key.Key_F30: 16777293>
        Key_F31: typing.ClassVar[Qt.Key]  # value = <Key.Key_F31: 16777294>
        Key_F32: typing.ClassVar[Qt.Key]  # value = <Key.Key_F32: 16777295>
        Key_F33: typing.ClassVar[Qt.Key]  # value = <Key.Key_F33: 16777296>
        Key_F34: typing.ClassVar[Qt.Key]  # value = <Key.Key_F34: 16777297>
        Key_F35: typing.ClassVar[Qt.Key]  # value = <Key.Key_F35: 16777298>
        Key_F4: typing.ClassVar[Qt.Key]  # value = <Key.Key_F4: 16777267>
        Key_F5: typing.ClassVar[Qt.Key]  # value = <Key.Key_F5: 16777268>
        Key_F6: typing.ClassVar[Qt.Key]  # value = <Key.Key_F6: 16777269>
        Key_F7: typing.ClassVar[Qt.Key]  # value = <Key.Key_F7: 16777270>
        Key_F8: typing.ClassVar[Qt.Key]  # value = <Key.Key_F8: 16777271>
        Key_F9: typing.ClassVar[Qt.Key]  # value = <Key.Key_F9: 16777272>
        Key_Favorites: typing.ClassVar[Qt.Key]  # value = <Key.Key_Favorites: 16777361>
        Key_Finance: typing.ClassVar[Qt.Key]  # value = <Key.Key_Finance: 16777411>
        Key_Find: typing.ClassVar[Qt.Key]  # value = <Key.Key_Find: 16777506>
        Key_Flip: typing.ClassVar[Qt.Key]  # value = <Key.Key_Flip: 17825798>
        Key_Forward: typing.ClassVar[Qt.Key]  # value = <Key.Key_Forward: 16777314>
        Key_G: typing.ClassVar[Qt.Key]  # value = <Key.Key_G: 71>
        Key_Game: typing.ClassVar[Qt.Key]  # value = <Key.Key_Game: 16777430>
        Key_Go: typing.ClassVar[Qt.Key]  # value = <Key.Key_Go: 16777431>
        Key_Greater: typing.ClassVar[Qt.Key]  # value = <Key.Key_Greater: 62>
        Key_Green: typing.ClassVar[Qt.Key]  # value = <Key.Key_Green: 16777493>
        Key_Guide: typing.ClassVar[Qt.Key]  # value = <Key.Key_Guide: 16777498>
        Key_H: typing.ClassVar[Qt.Key]  # value = <Key.Key_H: 72>
        Key_Hangul: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul: 16781617>
        Key_Hangul_Banja: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_Banja: 16781625>
        Key_Hangul_End: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_End: 16781619>
        Key_Hangul_Hanja: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_Hanja: 16781620>
        Key_Hangul_Jamo: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_Jamo: 16781621>
        Key_Hangul_Jeonja: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_Jeonja: 16781624>
        Key_Hangul_PostHanja: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_PostHanja: 16781627>
        Key_Hangul_PreHanja: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_PreHanja: 16781626>
        Key_Hangul_Romaja: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_Romaja: 16781622>
        Key_Hangul_Special: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_Special: 16781631>
        Key_Hangul_Start: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangul_Start: 16781618>
        Key_Hangup: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hangup: 17825797>
        Key_Hankaku: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hankaku: 16781609>
        Key_Help: typing.ClassVar[Qt.Key]  # value = <Key.Key_Help: 16777304>
        Key_Henkan: typing.ClassVar[Qt.Key]  # value = <Key.Key_Henkan: 16781603>
        Key_Hibernate: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hibernate: 16777480>
        Key_Hiragana: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hiragana: 16781605>
        Key_Hiragana_Katakana: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hiragana_Katakana: 16781607>
        Key_History: typing.ClassVar[Qt.Key]  # value = <Key.Key_History: 16777407>
        Key_Home: typing.ClassVar[Qt.Key]  # value = <Key.Key_Home: 16777232>
        Key_HomePage: typing.ClassVar[Qt.Key]  # value = <Key.Key_HomePage: 16777360>
        Key_HotLinks: typing.ClassVar[Qt.Key]  # value = <Key.Key_HotLinks: 16777409>
        Key_Hyper_L: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hyper_L: 16777302>
        Key_Hyper_R: typing.ClassVar[Qt.Key]  # value = <Key.Key_Hyper_R: 16777303>
        Key_I: typing.ClassVar[Qt.Key]  # value = <Key.Key_I: 73>
        Key_Iacute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Iacute: 205>
        Key_Icircumflex: typing.ClassVar[Qt.Key]  # value = <Key.Key_Icircumflex: 206>
        Key_Idiaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_Idiaeresis: 207>
        Key_Igrave: typing.ClassVar[Qt.Key]  # value = <Key.Key_Igrave: 204>
        Key_Info: typing.ClassVar[Qt.Key]  # value = <Key.Key_Info: 16777499>
        Key_Insert: typing.ClassVar[Qt.Key]  # value = <Key.Key_Insert: 16777222>
        Key_J: typing.ClassVar[Qt.Key]  # value = <Key.Key_J: 74>
        Key_K: typing.ClassVar[Qt.Key]  # value = <Key.Key_K: 75>
        Key_Kana_Lock: typing.ClassVar[Qt.Key]  # value = <Key.Key_Kana_Lock: 16781613>
        Key_Kana_Shift: typing.ClassVar[Qt.Key]  # value = <Key.Key_Kana_Shift: 16781614>
        Key_Kanji: typing.ClassVar[Qt.Key]  # value = <Key.Key_Kanji: 16781601>
        Key_Katakana: typing.ClassVar[Qt.Key]  # value = <Key.Key_Katakana: 16781606>
        Key_KeyboardBrightnessDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_KeyboardBrightnessDown: 16777398>
        Key_KeyboardBrightnessUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_KeyboardBrightnessUp: 16777397>
        Key_KeyboardLightOnOff: typing.ClassVar[Qt.Key]  # value = <Key.Key_KeyboardLightOnOff: 16777396>
        Key_L: typing.ClassVar[Qt.Key]  # value = <Key.Key_L: 76>
        Key_LastNumberRedial: typing.ClassVar[Qt.Key]  # value = <Key.Key_LastNumberRedial: 17825801>
        Key_Launch0: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch0: 16777378>
        Key_Launch1: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch1: 16777379>
        Key_Launch2: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch2: 16777380>
        Key_Launch3: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch3: 16777381>
        Key_Launch4: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch4: 16777382>
        Key_Launch5: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch5: 16777383>
        Key_Launch6: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch6: 16777384>
        Key_Launch7: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch7: 16777385>
        Key_Launch8: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch8: 16777386>
        Key_Launch9: typing.ClassVar[Qt.Key]  # value = <Key.Key_Launch9: 16777387>
        Key_LaunchA: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchA: 16777388>
        Key_LaunchB: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchB: 16777389>
        Key_LaunchC: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchC: 16777390>
        Key_LaunchD: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchD: 16777391>
        Key_LaunchE: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchE: 16777392>
        Key_LaunchF: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchF: 16777393>
        Key_LaunchG: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchG: 16777486>
        Key_LaunchH: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchH: 16777487>
        Key_LaunchMail: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchMail: 16777376>
        Key_LaunchMedia: typing.ClassVar[Qt.Key]  # value = <Key.Key_LaunchMedia: 16777377>
        Key_Left: typing.ClassVar[Qt.Key]  # value = <Key.Key_Left: 16777234>
        Key_Less: typing.ClassVar[Qt.Key]  # value = <Key.Key_Less: 60>
        Key_LightBulb: typing.ClassVar[Qt.Key]  # value = <Key.Key_LightBulb: 16777405>
        Key_LogOff: typing.ClassVar[Qt.Key]  # value = <Key.Key_LogOff: 16777433>
        Key_M: typing.ClassVar[Qt.Key]  # value = <Key.Key_M: 77>
        Key_MailForward: typing.ClassVar[Qt.Key]  # value = <Key.Key_MailForward: 16777467>
        Key_Market: typing.ClassVar[Qt.Key]  # value = <Key.Key_Market: 16777434>
        Key_Massyo: typing.ClassVar[Qt.Key]  # value = <Key.Key_Massyo: 16781612>
        Key_MediaLast: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaLast: 16842751>
        Key_MediaNext: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaNext: 16777347>
        Key_MediaPause: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaPause: 16777349>
        Key_MediaPlay: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaPlay: 16777344>
        Key_MediaPrevious: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaPrevious: 16777346>
        Key_MediaRecord: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaRecord: 16777348>
        Key_MediaStop: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaStop: 16777345>
        Key_MediaTogglePlayPause: typing.ClassVar[Qt.Key]  # value = <Key.Key_MediaTogglePlayPause: 16777350>
        Key_Meeting: typing.ClassVar[Qt.Key]  # value = <Key.Key_Meeting: 16777435>
        Key_Memo: typing.ClassVar[Qt.Key]  # value = <Key.Key_Memo: 16777404>
        Key_Menu: typing.ClassVar[Qt.Key]  # value = <Key.Key_Menu: 16777301>
        Key_MenuKB: typing.ClassVar[Qt.Key]  # value = <Key.Key_MenuKB: 16777436>
        Key_MenuPB: typing.ClassVar[Qt.Key]  # value = <Key.Key_MenuPB: 16777437>
        Key_Messenger: typing.ClassVar[Qt.Key]  # value = <Key.Key_Messenger: 16777465>
        Key_Meta: typing.ClassVar[Qt.Key]  # value = <Key.Key_Meta: 16777250>
        Key_MicMute: typing.ClassVar[Qt.Key]  # value = <Key.Key_MicMute: 16777491>
        Key_MicVolumeDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_MicVolumeDown: 16777502>
        Key_MicVolumeUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_MicVolumeUp: 16777501>
        Key_Minus: typing.ClassVar[Qt.Key]  # value = <Key.Key_Minus: 45>
        Key_Mode_switch: typing.ClassVar[Qt.Key]  # value = <Key.Key_Mode_switch: 16781694>
        Key_MonBrightnessDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_MonBrightnessDown: 16777395>
        Key_MonBrightnessUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_MonBrightnessUp: 16777394>
        Key_Muhenkan: typing.ClassVar[Qt.Key]  # value = <Key.Key_Muhenkan: 16781602>
        Key_Multi_key: typing.ClassVar[Qt.Key]  # value = <Key.Key_Multi_key: 16781600>
        Key_MultipleCandidate: typing.ClassVar[Qt.Key]  # value = <Key.Key_MultipleCandidate: 16781629>
        Key_Music: typing.ClassVar[Qt.Key]  # value = <Key.Key_Music: 16777469>
        Key_MySites: typing.ClassVar[Qt.Key]  # value = <Key.Key_MySites: 16777438>
        Key_N: typing.ClassVar[Qt.Key]  # value = <Key.Key_N: 78>
        Key_New: typing.ClassVar[Qt.Key]  # value = <Key.Key_New: 16777504>
        Key_News: typing.ClassVar[Qt.Key]  # value = <Key.Key_News: 16777439>
        Key_No: typing.ClassVar[Qt.Key]  # value = <Key.Key_No: 16842754>
        Key_Ntilde: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ntilde: 209>
        Key_NumLock: typing.ClassVar[Qt.Key]  # value = <Key.Key_NumLock: 16777253>
        Key_NumberSign: typing.ClassVar[Qt.Key]  # value = <Key.Key_NumberSign: 35>
        Key_O: typing.ClassVar[Qt.Key]  # value = <Key.Key_O: 79>
        Key_Oacute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Oacute: 211>
        Key_Ocircumflex: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ocircumflex: 212>
        Key_Odiaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_Odiaeresis: 214>
        Key_OfficeHome: typing.ClassVar[Qt.Key]  # value = <Key.Key_OfficeHome: 16777440>
        Key_Ograve: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ograve: 210>
        Key_Ooblique: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ooblique: 216>
        Key_Open: typing.ClassVar[Qt.Key]  # value = <Key.Key_Open: 16777505>
        Key_OpenUrl: typing.ClassVar[Qt.Key]  # value = <Key.Key_OpenUrl: 16777364>
        Key_Option: typing.ClassVar[Qt.Key]  # value = <Key.Key_Option: 16777441>
        Key_Otilde: typing.ClassVar[Qt.Key]  # value = <Key.Key_Otilde: 213>
        Key_P: typing.ClassVar[Qt.Key]  # value = <Key.Key_P: 80>
        Key_PageDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_PageDown: 16777239>
        Key_PageUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_PageUp: 16777238>
        Key_ParenLeft: typing.ClassVar[Qt.Key]  # value = <Key.Key_ParenLeft: 40>
        Key_ParenRight: typing.ClassVar[Qt.Key]  # value = <Key.Key_ParenRight: 41>
        Key_Paste: typing.ClassVar[Qt.Key]  # value = <Key.Key_Paste: 16777442>
        Key_Pause: typing.ClassVar[Qt.Key]  # value = <Key.Key_Pause: 16777224>
        Key_Percent: typing.ClassVar[Qt.Key]  # value = <Key.Key_Percent: 37>
        Key_Period: typing.ClassVar[Qt.Key]  # value = <Key.Key_Period: 46>
        Key_Phone: typing.ClassVar[Qt.Key]  # value = <Key.Key_Phone: 16777443>
        Key_Pictures: typing.ClassVar[Qt.Key]  # value = <Key.Key_Pictures: 16777468>
        Key_Play: typing.ClassVar[Qt.Key]  # value = <Key.Key_Play: 16908293>
        Key_Plus: typing.ClassVar[Qt.Key]  # value = <Key.Key_Plus: 43>
        Key_PowerDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_PowerDown: 16777483>
        Key_PowerOff: typing.ClassVar[Qt.Key]  # value = <Key.Key_PowerOff: 16777399>
        Key_PreviousCandidate: typing.ClassVar[Qt.Key]  # value = <Key.Key_PreviousCandidate: 16781630>
        Key_Print: typing.ClassVar[Qt.Key]  # value = <Key.Key_Print: 16777225>
        Key_Printer: typing.ClassVar[Qt.Key]  # value = <Key.Key_Printer: 16908290>
        Key_Q: typing.ClassVar[Qt.Key]  # value = <Key.Key_Q: 81>
        Key_Question: typing.ClassVar[Qt.Key]  # value = <Key.Key_Question: 63>
        Key_QuoteDbl: typing.ClassVar[Qt.Key]  # value = <Key.Key_QuoteDbl: 34>
        Key_QuoteLeft: typing.ClassVar[Qt.Key]  # value = <Key.Key_QuoteLeft: 96>
        Key_R: typing.ClassVar[Qt.Key]  # value = <Key.Key_R: 82>
        Key_Red: typing.ClassVar[Qt.Key]  # value = <Key.Key_Red: 16777492>
        Key_Redo: typing.ClassVar[Qt.Key]  # value = <Key.Key_Redo: 16777508>
        Key_Refresh: typing.ClassVar[Qt.Key]  # value = <Key.Key_Refresh: 16777316>
        Key_Reload: typing.ClassVar[Qt.Key]  # value = <Key.Key_Reload: 16777446>
        Key_Reply: typing.ClassVar[Qt.Key]  # value = <Key.Key_Reply: 16777445>
        Key_Return: typing.ClassVar[Qt.Key]  # value = <Key.Key_Return: 16777220>
        Key_Right: typing.ClassVar[Qt.Key]  # value = <Key.Key_Right: 16777236>
        Key_Romaji: typing.ClassVar[Qt.Key]  # value = <Key.Key_Romaji: 16781604>
        Key_RotateWindows: typing.ClassVar[Qt.Key]  # value = <Key.Key_RotateWindows: 16777447>
        Key_RotationKB: typing.ClassVar[Qt.Key]  # value = <Key.Key_RotationKB: 16777449>
        Key_RotationPB: typing.ClassVar[Qt.Key]  # value = <Key.Key_RotationPB: 16777448>
        Key_S: typing.ClassVar[Qt.Key]  # value = <Key.Key_S: 83>
        Key_Save: typing.ClassVar[Qt.Key]  # value = <Key.Key_Save: 16777450>
        Key_ScreenSaver: typing.ClassVar[Qt.Key]  # value = <Key.Key_ScreenSaver: 16777402>
        Key_ScrollLock: typing.ClassVar[Qt.Key]  # value = <Key.Key_ScrollLock: 16777254>
        Key_Search: typing.ClassVar[Qt.Key]  # value = <Key.Key_Search: 16777362>
        Key_Select: typing.ClassVar[Qt.Key]  # value = <Key.Key_Select: 16842752>
        Key_Semicolon: typing.ClassVar[Qt.Key]  # value = <Key.Key_Semicolon: 59>
        Key_Send: typing.ClassVar[Qt.Key]  # value = <Key.Key_Send: 16777451>
        Key_Settings: typing.ClassVar[Qt.Key]  # value = <Key.Key_Settings: 16777500>
        Key_Shift: typing.ClassVar[Qt.Key]  # value = <Key.Key_Shift: 16777248>
        Key_Shop: typing.ClassVar[Qt.Key]  # value = <Key.Key_Shop: 16777406>
        Key_SingleCandidate: typing.ClassVar[Qt.Key]  # value = <Key.Key_SingleCandidate: 16781628>
        Key_Slash: typing.ClassVar[Qt.Key]  # value = <Key.Key_Slash: 47>
        Key_Sleep: typing.ClassVar[Qt.Key]  # value = <Key.Key_Sleep: 16908292>
        Key_Space: typing.ClassVar[Qt.Key]  # value = <Key.Key_Space: 32>
        Key_Spell: typing.ClassVar[Qt.Key]  # value = <Key.Key_Spell: 16777452>
        Key_SplitScreen: typing.ClassVar[Qt.Key]  # value = <Key.Key_SplitScreen: 16777453>
        Key_Standby: typing.ClassVar[Qt.Key]  # value = <Key.Key_Standby: 16777363>
        Key_Stop: typing.ClassVar[Qt.Key]  # value = <Key.Key_Stop: 16777315>
        Key_Subtitle: typing.ClassVar[Qt.Key]  # value = <Key.Key_Subtitle: 16777477>
        Key_Super_L: typing.ClassVar[Qt.Key]  # value = <Key.Key_Super_L: 16777299>
        Key_Super_R: typing.ClassVar[Qt.Key]  # value = <Key.Key_Super_R: 16777300>
        Key_Support: typing.ClassVar[Qt.Key]  # value = <Key.Key_Support: 16777454>
        Key_Suspend: typing.ClassVar[Qt.Key]  # value = <Key.Key_Suspend: 16777484>
        Key_SysReq: typing.ClassVar[Qt.Key]  # value = <Key.Key_SysReq: 16777226>
        Key_T: typing.ClassVar[Qt.Key]  # value = <Key.Key_T: 84>
        Key_THORN: typing.ClassVar[Qt.Key]  # value = <Key.Key_THORN: 222>
        Key_Tab: typing.ClassVar[Qt.Key]  # value = <Key.Key_Tab: 16777217>
        Key_TaskPane: typing.ClassVar[Qt.Key]  # value = <Key.Key_TaskPane: 16777455>
        Key_Terminal: typing.ClassVar[Qt.Key]  # value = <Key.Key_Terminal: 16777456>
        Key_Time: typing.ClassVar[Qt.Key]  # value = <Key.Key_Time: 16777479>
        Key_ToDoList: typing.ClassVar[Qt.Key]  # value = <Key.Key_ToDoList: 16777420>
        Key_ToggleCallHangup: typing.ClassVar[Qt.Key]  # value = <Key.Key_ToggleCallHangup: 17825799>
        Key_Tools: typing.ClassVar[Qt.Key]  # value = <Key.Key_Tools: 16777457>
        Key_TopMenu: typing.ClassVar[Qt.Key]  # value = <Key.Key_TopMenu: 16777482>
        Key_TouchpadOff: typing.ClassVar[Qt.Key]  # value = <Key.Key_TouchpadOff: 16777490>
        Key_TouchpadOn: typing.ClassVar[Qt.Key]  # value = <Key.Key_TouchpadOn: 16777489>
        Key_TouchpadToggle: typing.ClassVar[Qt.Key]  # value = <Key.Key_TouchpadToggle: 16777488>
        Key_Touroku: typing.ClassVar[Qt.Key]  # value = <Key.Key_Touroku: 16781611>
        Key_Travel: typing.ClassVar[Qt.Key]  # value = <Key.Key_Travel: 16777458>
        Key_TrebleDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_TrebleDown: 16777335>
        Key_TrebleUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_TrebleUp: 16777334>
        Key_U: typing.ClassVar[Qt.Key]  # value = <Key.Key_U: 85>
        Key_UWB: typing.ClassVar[Qt.Key]  # value = <Key.Key_UWB: 16777473>
        Key_Uacute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Uacute: 218>
        Key_Ucircumflex: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ucircumflex: 219>
        Key_Udiaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_Udiaeresis: 220>
        Key_Ugrave: typing.ClassVar[Qt.Key]  # value = <Key.Key_Ugrave: 217>
        Key_Underscore: typing.ClassVar[Qt.Key]  # value = <Key.Key_Underscore: 95>
        Key_Undo: typing.ClassVar[Qt.Key]  # value = <Key.Key_Undo: 16777507>
        Key_Up: typing.ClassVar[Qt.Key]  # value = <Key.Key_Up: 16777235>
        Key_V: typing.ClassVar[Qt.Key]  # value = <Key.Key_V: 86>
        Key_Video: typing.ClassVar[Qt.Key]  # value = <Key.Key_Video: 16777459>
        Key_View: typing.ClassVar[Qt.Key]  # value = <Key.Key_View: 16777481>
        Key_VoiceDial: typing.ClassVar[Qt.Key]  # value = <Key.Key_VoiceDial: 17825800>
        Key_VolumeDown: typing.ClassVar[Qt.Key]  # value = <Key.Key_VolumeDown: 16777328>
        Key_VolumeMute: typing.ClassVar[Qt.Key]  # value = <Key.Key_VolumeMute: 16777329>
        Key_VolumeUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_VolumeUp: 16777330>
        Key_W: typing.ClassVar[Qt.Key]  # value = <Key.Key_W: 87>
        Key_WLAN: typing.ClassVar[Qt.Key]  # value = <Key.Key_WLAN: 16777472>
        Key_WWW: typing.ClassVar[Qt.Key]  # value = <Key.Key_WWW: 16777403>
        Key_WakeUp: typing.ClassVar[Qt.Key]  # value = <Key.Key_WakeUp: 16777400>
        Key_WebCam: typing.ClassVar[Qt.Key]  # value = <Key.Key_WebCam: 16777466>
        Key_Word: typing.ClassVar[Qt.Key]  # value = <Key.Key_Word: 16777460>
        Key_X: typing.ClassVar[Qt.Key]  # value = <Key.Key_X: 88>
        Key_Xfer: typing.ClassVar[Qt.Key]  # value = <Key.Key_Xfer: 16777461>
        Key_Y: typing.ClassVar[Qt.Key]  # value = <Key.Key_Y: 89>
        Key_Yacute: typing.ClassVar[Qt.Key]  # value = <Key.Key_Yacute: 221>
        Key_Yellow: typing.ClassVar[Qt.Key]  # value = <Key.Key_Yellow: 16777494>
        Key_Yes: typing.ClassVar[Qt.Key]  # value = <Key.Key_Yes: 16842753>
        Key_Z: typing.ClassVar[Qt.Key]  # value = <Key.Key_Z: 90>
        Key_Zenkaku: typing.ClassVar[Qt.Key]  # value = <Key.Key_Zenkaku: 16781608>
        Key_Zenkaku_Hankaku: typing.ClassVar[Qt.Key]  # value = <Key.Key_Zenkaku_Hankaku: 16781610>
        Key_Zoom: typing.ClassVar[Qt.Key]  # value = <Key.Key_Zoom: 16908294>
        Key_ZoomIn: typing.ClassVar[Qt.Key]  # value = <Key.Key_ZoomIn: 16777462>
        Key_ZoomOut: typing.ClassVar[Qt.Key]  # value = <Key.Key_ZoomOut: 16777463>
        Key_acute: typing.ClassVar[Qt.Key]  # value = <Key.Key_acute: 180>
        Key_brokenbar: typing.ClassVar[Qt.Key]  # value = <Key.Key_brokenbar: 166>
        Key_cedilla: typing.ClassVar[Qt.Key]  # value = <Key.Key_cedilla: 184>
        Key_cent: typing.ClassVar[Qt.Key]  # value = <Key.Key_cent: 162>
        Key_copyright: typing.ClassVar[Qt.Key]  # value = <Key.Key_copyright: 169>
        Key_currency: typing.ClassVar[Qt.Key]  # value = <Key.Key_currency: 164>
        Key_degree: typing.ClassVar[Qt.Key]  # value = <Key.Key_degree: 176>
        Key_diaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_diaeresis: 168>
        Key_division: typing.ClassVar[Qt.Key]  # value = <Key.Key_division: 247>
        Key_exclamdown: typing.ClassVar[Qt.Key]  # value = <Key.Key_exclamdown: 161>
        Key_guillemotleft: typing.ClassVar[Qt.Key]  # value = <Key.Key_guillemotleft: 171>
        Key_guillemotright: typing.ClassVar[Qt.Key]  # value = <Key.Key_guillemotright: 187>
        Key_hyphen: typing.ClassVar[Qt.Key]  # value = <Key.Key_hyphen: 173>
        Key_iTouch: typing.ClassVar[Qt.Key]  # value = <Key.Key_iTouch: 16777432>
        Key_macron: typing.ClassVar[Qt.Key]  # value = <Key.Key_macron: 175>
        Key_masculine: typing.ClassVar[Qt.Key]  # value = <Key.Key_masculine: 186>
        Key_mu: typing.ClassVar[Qt.Key]  # value = <Key.Key_mu: 181>
        Key_multiply: typing.ClassVar[Qt.Key]  # value = <Key.Key_multiply: 215>
        Key_nobreakspace: typing.ClassVar[Qt.Key]  # value = <Key.Key_nobreakspace: 160>
        Key_notsign: typing.ClassVar[Qt.Key]  # value = <Key.Key_notsign: 172>
        Key_onehalf: typing.ClassVar[Qt.Key]  # value = <Key.Key_onehalf: 189>
        Key_onequarter: typing.ClassVar[Qt.Key]  # value = <Key.Key_onequarter: 188>
        Key_onesuperior: typing.ClassVar[Qt.Key]  # value = <Key.Key_onesuperior: 185>
        Key_ordfeminine: typing.ClassVar[Qt.Key]  # value = <Key.Key_ordfeminine: 170>
        Key_paragraph: typing.ClassVar[Qt.Key]  # value = <Key.Key_paragraph: 182>
        Key_periodcentered: typing.ClassVar[Qt.Key]  # value = <Key.Key_periodcentered: 183>
        Key_plusminus: typing.ClassVar[Qt.Key]  # value = <Key.Key_plusminus: 177>
        Key_questiondown: typing.ClassVar[Qt.Key]  # value = <Key.Key_questiondown: 191>
        Key_registered: typing.ClassVar[Qt.Key]  # value = <Key.Key_registered: 174>
        Key_section: typing.ClassVar[Qt.Key]  # value = <Key.Key_section: 167>
        Key_ssharp: typing.ClassVar[Qt.Key]  # value = <Key.Key_ssharp: 223>
        Key_sterling: typing.ClassVar[Qt.Key]  # value = <Key.Key_sterling: 163>
        Key_threequarters: typing.ClassVar[Qt.Key]  # value = <Key.Key_threequarters: 190>
        Key_threesuperior: typing.ClassVar[Qt.Key]  # value = <Key.Key_threesuperior: 179>
        Key_twosuperior: typing.ClassVar[Qt.Key]  # value = <Key.Key_twosuperior: 178>
        Key_unknown: typing.ClassVar[Qt.Key]  # value = <Key.Key_unknown: 33554431>
        Key_ydiaeresis: typing.ClassVar[Qt.Key]  # value = <Key.Key_ydiaeresis: 255>
        Key_yen: typing.ClassVar[Qt.Key]  # value = <Key.Key_yen: 165>
        @classmethod
        def __new__(cls, value):
            ...
        def __format__(self, format_spec):
            ...
    class KeyboardModifier(enum.Flag):
        AltModifier: typing.ClassVar[Qt.KeyboardModifier]  # value = <KeyboardModifier.AltModifier: 134217728>
        ControlModifier: typing.ClassVar[Qt.KeyboardModifier]  # value = <KeyboardModifier.ControlModifier: 67108864>
        GroupSwitchModifier: typing.ClassVar[Qt.KeyboardModifier]  # value = <KeyboardModifier.GroupSwitchModifier: 1073741824>
        KeypadModifier: typing.ClassVar[Qt.KeyboardModifier]  # value = <KeyboardModifier.KeypadModifier: 536870912>
        MetaModifier: typing.ClassVar[Qt.KeyboardModifier]  # value = <KeyboardModifier.MetaModifier: 268435456>
        ShiftModifier: typing.ClassVar[Qt.KeyboardModifier]  # value = <KeyboardModifier.ShiftModifier: 33554432>
    class LayoutDirection(enum.Enum):
        LayoutDirectionAuto: typing.ClassVar[Qt.LayoutDirection]  # value = <LayoutDirection.LayoutDirectionAuto: 2>
        LeftToRight: typing.ClassVar[Qt.LayoutDirection]  # value = <LayoutDirection.LeftToRight: 0>
        RightToLeft: typing.ClassVar[Qt.LayoutDirection]  # value = <LayoutDirection.RightToLeft: 1>
    class MaskMode(enum.Enum):
        MaskInColor: typing.ClassVar[Qt.MaskMode]  # value = <MaskMode.MaskInColor: 0>
        MaskOutColor: typing.ClassVar[Qt.MaskMode]  # value = <MaskMode.MaskOutColor: 1>
    class MatchFlag(enum.Flag):
        MatchCaseSensitive: typing.ClassVar[Qt.MatchFlag]  # value = <MatchFlag.MatchCaseSensitive: 16>
        MatchContains: typing.ClassVar[Qt.MatchFlag]  # value = <MatchFlag.MatchContains: 1>
        MatchFixedString: typing.ClassVar[Qt.MatchFlag]  # value = <MatchFlag.MatchFixedString: 8>
        MatchRecursive: typing.ClassVar[Qt.MatchFlag]  # value = <MatchFlag.MatchRecursive: 64>
        MatchRegularExpression: typing.ClassVar[Qt.MatchFlag]  # value = <MatchFlag.MatchRegularExpression: 4>
        MatchStartsWith: typing.ClassVar[Qt.MatchFlag]  # value = <MatchFlag.MatchStartsWith: 2>
        MatchWrap: typing.ClassVar[Qt.MatchFlag]  # value = <MatchFlag.MatchWrap: 32>
    class Modifier(enum.Flag):
        ALT: typing.ClassVar[Qt.Modifier]  # value = <Modifier.ALT: 134217728>
        CTRL: typing.ClassVar[Qt.Modifier]  # value = <Modifier.CTRL: 67108864>
        META: typing.ClassVar[Qt.Modifier]  # value = <Modifier.META: 268435456>
        SHIFT: typing.ClassVar[Qt.Modifier]  # value = <Modifier.SHIFT: 33554432>
    class MouseButton(enum.Flag):
        ExtraButton10: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton10: 4096>
        ExtraButton11: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton11: 8192>
        ExtraButton12: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton12: 16384>
        ExtraButton13: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton13: 32768>
        ExtraButton14: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton14: 65536>
        ExtraButton15: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton15: 131072>
        ExtraButton16: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton16: 262144>
        ExtraButton17: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton17: 524288>
        ExtraButton18: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton18: 1048576>
        ExtraButton19: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton19: 2097152>
        ExtraButton20: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton20: 4194304>
        ExtraButton21: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton21: 8388608>
        ExtraButton22: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton22: 16777216>
        ExtraButton23: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton23: 33554432>
        ExtraButton24: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton24: 67108864>
        ExtraButton4: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton4: 64>
        ExtraButton5: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton5: 128>
        ExtraButton6: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton6: 256>
        ExtraButton7: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton7: 512>
        ExtraButton8: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton8: 1024>
        ExtraButton9: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.ExtraButton9: 2048>
        LeftButton: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.LeftButton: 1>
        MiddleButton: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.MiddleButton: 4>
        RightButton: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.RightButton: 2>
        TaskButton: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.TaskButton: 32>
        XButton1: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.XButton1: 8>
        XButton2: typing.ClassVar[Qt.MouseButton]  # value = <MouseButton.XButton2: 16>
    class MouseEventFlag(enum.Flag):
        MouseEventCreatedDoubleClick: typing.ClassVar[Qt.MouseEventFlag]  # value = <MouseEventFlag.MouseEventCreatedDoubleClick: 1>
    class MouseEventSource(enum.Enum):
        MouseEventNotSynthesized: typing.ClassVar[Qt.MouseEventSource]  # value = <MouseEventSource.MouseEventNotSynthesized: 0>
        MouseEventSynthesizedByApplication: typing.ClassVar[Qt.MouseEventSource]  # value = <MouseEventSource.MouseEventSynthesizedByApplication: 3>
        MouseEventSynthesizedByQt: typing.ClassVar[Qt.MouseEventSource]  # value = <MouseEventSource.MouseEventSynthesizedByQt: 2>
        MouseEventSynthesizedBySystem: typing.ClassVar[Qt.MouseEventSource]  # value = <MouseEventSource.MouseEventSynthesizedBySystem: 1>
    class NativeGestureType(enum.Enum):
        BeginNativeGesture: typing.ClassVar[Qt.NativeGestureType]  # value = <NativeGestureType.BeginNativeGesture: 0>
        EndNativeGesture: typing.ClassVar[Qt.NativeGestureType]  # value = <NativeGestureType.EndNativeGesture: 1>
        PanNativeGesture: typing.ClassVar[Qt.NativeGestureType]  # value = <NativeGestureType.PanNativeGesture: 2>
        RotateNativeGesture: typing.ClassVar[Qt.NativeGestureType]  # value = <NativeGestureType.RotateNativeGesture: 5>
        SmartZoomNativeGesture: typing.ClassVar[Qt.NativeGestureType]  # value = <NativeGestureType.SmartZoomNativeGesture: 4>
        SwipeNativeGesture: typing.ClassVar[Qt.NativeGestureType]  # value = <NativeGestureType.SwipeNativeGesture: 6>
        ZoomNativeGesture: typing.ClassVar[Qt.NativeGestureType]  # value = <NativeGestureType.ZoomNativeGesture: 3>
    class NavigationMode(enum.Enum):
        NavigationModeCursorAuto: typing.ClassVar[Qt.NavigationMode]  # value = <NavigationMode.NavigationModeCursorAuto: 3>
        NavigationModeCursorForceVisible: typing.ClassVar[Qt.NavigationMode]  # value = <NavigationMode.NavigationModeCursorForceVisible: 4>
        NavigationModeKeypadDirectional: typing.ClassVar[Qt.NavigationMode]  # value = <NavigationMode.NavigationModeKeypadDirectional: 2>
        NavigationModeKeypadTabOrder: typing.ClassVar[Qt.NavigationMode]  # value = <NavigationMode.NavigationModeKeypadTabOrder: 1>
        NavigationModeNone: typing.ClassVar[Qt.NavigationMode]  # value = <NavigationMode.NavigationModeNone: 0>
    class Orientation(enum.Flag):
        Horizontal: typing.ClassVar[Qt.Orientation]  # value = <Orientation.Horizontal: 1>
        Vertical: typing.ClassVar[Qt.Orientation]  # value = <Orientation.Vertical: 2>
    class PenCapStyle(enum.Enum):
        FlatCap: typing.ClassVar[Qt.PenCapStyle]  # value = <PenCapStyle.FlatCap: 0>
        RoundCap: typing.ClassVar[Qt.PenCapStyle]  # value = <PenCapStyle.RoundCap: 32>
        SquareCap: typing.ClassVar[Qt.PenCapStyle]  # value = <PenCapStyle.SquareCap: 16>
    class PenJoinStyle(enum.Enum):
        BevelJoin: typing.ClassVar[Qt.PenJoinStyle]  # value = <PenJoinStyle.BevelJoin: 64>
        MPenJoinStyle: typing.ClassVar[Qt.PenJoinStyle]  # value = <PenJoinStyle.MPenJoinStyle: 448>
        MiterJoin: typing.ClassVar[Qt.PenJoinStyle]  # value = <PenJoinStyle.MiterJoin: 0>
        RoundJoin: typing.ClassVar[Qt.PenJoinStyle]  # value = <PenJoinStyle.RoundJoin: 128>
        SvgMiterJoin: typing.ClassVar[Qt.PenJoinStyle]  # value = <PenJoinStyle.SvgMiterJoin: 256>
    class PenStyle(enum.Enum):
        CustomDashLine: typing.ClassVar[Qt.PenStyle]  # value = <PenStyle.CustomDashLine: 6>
        DashDotDotLine: typing.ClassVar[Qt.PenStyle]  # value = <PenStyle.DashDotDotLine: 5>
        DashDotLine: typing.ClassVar[Qt.PenStyle]  # value = <PenStyle.DashDotLine: 4>
        DashLine: typing.ClassVar[Qt.PenStyle]  # value = <PenStyle.DashLine: 2>
        DotLine: typing.ClassVar[Qt.PenStyle]  # value = <PenStyle.DotLine: 3>
        NoPen: typing.ClassVar[Qt.PenStyle]  # value = <PenStyle.NoPen: 0>
        SolidLine: typing.ClassVar[Qt.PenStyle]  # value = <PenStyle.SolidLine: 1>
    class PermissionStatus(enum.Enum):
        Denied: typing.ClassVar[Qt.PermissionStatus]  # value = <PermissionStatus.Denied: 2>
        Granted: typing.ClassVar[Qt.PermissionStatus]  # value = <PermissionStatus.Granted: 1>
        Undetermined: typing.ClassVar[Qt.PermissionStatus]  # value = <PermissionStatus.Undetermined: 0>
    class ScreenOrientation(enum.Flag):
        InvertedLandscapeOrientation: typing.ClassVar[Qt.ScreenOrientation]  # value = <ScreenOrientation.InvertedLandscapeOrientation: 8>
        InvertedPortraitOrientation: typing.ClassVar[Qt.ScreenOrientation]  # value = <ScreenOrientation.InvertedPortraitOrientation: 4>
        LandscapeOrientation: typing.ClassVar[Qt.ScreenOrientation]  # value = <ScreenOrientation.LandscapeOrientation: 2>
        PortraitOrientation: typing.ClassVar[Qt.ScreenOrientation]  # value = <ScreenOrientation.PortraitOrientation: 1>
    class ScrollBarPolicy(enum.Enum):
        ScrollBarAlwaysOff: typing.ClassVar[Qt.ScrollBarPolicy]  # value = <ScrollBarPolicy.ScrollBarAlwaysOff: 1>
        ScrollBarAlwaysOn: typing.ClassVar[Qt.ScrollBarPolicy]  # value = <ScrollBarPolicy.ScrollBarAlwaysOn: 2>
        ScrollBarAsNeeded: typing.ClassVar[Qt.ScrollBarPolicy]  # value = <ScrollBarPolicy.ScrollBarAsNeeded: 0>
    class ScrollPhase(enum.Enum):
        NoScrollPhase: typing.ClassVar[Qt.ScrollPhase]  # value = <ScrollPhase.NoScrollPhase: 0>
        ScrollBegin: typing.ClassVar[Qt.ScrollPhase]  # value = <ScrollPhase.ScrollBegin: 1>
        ScrollEnd: typing.ClassVar[Qt.ScrollPhase]  # value = <ScrollPhase.ScrollEnd: 3>
        ScrollMomentum: typing.ClassVar[Qt.ScrollPhase]  # value = <ScrollPhase.ScrollMomentum: 4>
        ScrollUpdate: typing.ClassVar[Qt.ScrollPhase]  # value = <ScrollPhase.ScrollUpdate: 2>
    class ShortcutContext(enum.Enum):
        ApplicationShortcut: typing.ClassVar[Qt.ShortcutContext]  # value = <ShortcutContext.ApplicationShortcut: 2>
        WidgetShortcut: typing.ClassVar[Qt.ShortcutContext]  # value = <ShortcutContext.WidgetShortcut: 0>
        WidgetWithChildrenShortcut: typing.ClassVar[Qt.ShortcutContext]  # value = <ShortcutContext.WidgetWithChildrenShortcut: 3>
        WindowShortcut: typing.ClassVar[Qt.ShortcutContext]  # value = <ShortcutContext.WindowShortcut: 1>
    class SizeHint(enum.Enum):
        MaximumSize: typing.ClassVar[Qt.SizeHint]  # value = <SizeHint.MaximumSize: 2>
        MinimumDescent: typing.ClassVar[Qt.SizeHint]  # value = <SizeHint.MinimumDescent: 3>
        MinimumSize: typing.ClassVar[Qt.SizeHint]  # value = <SizeHint.MinimumSize: 0>
        PreferredSize: typing.ClassVar[Qt.SizeHint]  # value = <SizeHint.PreferredSize: 1>
    class SizeMode(enum.Enum):
        AbsoluteSize: typing.ClassVar[Qt.SizeMode]  # value = <SizeMode.AbsoluteSize: 0>
        RelativeSize: typing.ClassVar[Qt.SizeMode]  # value = <SizeMode.RelativeSize: 1>
    class SortOrder(enum.Enum):
        AscendingOrder: typing.ClassVar[Qt.SortOrder]  # value = <SortOrder.AscendingOrder: 0>
        DescendingOrder: typing.ClassVar[Qt.SortOrder]  # value = <SortOrder.DescendingOrder: 1>
    class TabFocusBehavior(enum.Enum):
        NoTabFocus: typing.ClassVar[Qt.TabFocusBehavior]  # value = <TabFocusBehavior.NoTabFocus: 0>
        TabFocusAllControls: typing.ClassVar[Qt.TabFocusBehavior]  # value = <TabFocusBehavior.TabFocusAllControls: 255>
        TabFocusListControls: typing.ClassVar[Qt.TabFocusBehavior]  # value = <TabFocusBehavior.TabFocusListControls: 2>
        TabFocusTextControls: typing.ClassVar[Qt.TabFocusBehavior]  # value = <TabFocusBehavior.TabFocusTextControls: 1>
    class TextElideMode(enum.Enum):
        ElideLeft: typing.ClassVar[Qt.TextElideMode]  # value = <TextElideMode.ElideLeft: 0>
        ElideMiddle: typing.ClassVar[Qt.TextElideMode]  # value = <TextElideMode.ElideMiddle: 2>
        ElideNone: typing.ClassVar[Qt.TextElideMode]  # value = <TextElideMode.ElideNone: 3>
        ElideRight: typing.ClassVar[Qt.TextElideMode]  # value = <TextElideMode.ElideRight: 1>
    class TextFlag(enum.IntFlag):
        TextDontClip: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextDontClip: 512>
        TextDontPrint: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextDontPrint: 16384>
        TextExpandTabs: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextExpandTabs: 1024>
        TextHideMnemonic: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextHideMnemonic: 32768>
        TextIncludeTrailingSpaces: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextIncludeTrailingSpaces: 134217728>
        TextJustificationForced: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextJustificationForced: 65536>
        TextShowMnemonic: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextShowMnemonic: 2048>
        TextSingleLine: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextSingleLine: 256>
        TextWordWrap: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextWordWrap: 4096>
        TextWrapAnywhere: typing.ClassVar[Qt.TextFlag]  # value = <TextFlag.TextWrapAnywhere: 8192>
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
    class TextFormat(enum.Enum):
        AutoText: typing.ClassVar[Qt.TextFormat]  # value = <TextFormat.AutoText: 2>
        MarkdownText: typing.ClassVar[Qt.TextFormat]  # value = <TextFormat.MarkdownText: 3>
        PlainText: typing.ClassVar[Qt.TextFormat]  # value = <TextFormat.PlainText: 0>
        RichText: typing.ClassVar[Qt.TextFormat]  # value = <TextFormat.RichText: 1>
    class TextInteractionFlag(enum.Flag):
        LinksAccessibleByKeyboard: typing.ClassVar[Qt.TextInteractionFlag]  # value = <TextInteractionFlag.LinksAccessibleByKeyboard: 8>
        LinksAccessibleByMouse: typing.ClassVar[Qt.TextInteractionFlag]  # value = <TextInteractionFlag.LinksAccessibleByMouse: 4>
        TextEditable: typing.ClassVar[Qt.TextInteractionFlag]  # value = <TextInteractionFlag.TextEditable: 16>
        TextSelectableByKeyboard: typing.ClassVar[Qt.TextInteractionFlag]  # value = <TextInteractionFlag.TextSelectableByKeyboard: 2>
        TextSelectableByMouse: typing.ClassVar[Qt.TextInteractionFlag]  # value = <TextInteractionFlag.TextSelectableByMouse: 1>
    class TileRule(enum.Enum):
        RepeatTile: typing.ClassVar[Qt.TileRule]  # value = <TileRule.RepeatTile: 1>
        RoundTile: typing.ClassVar[Qt.TileRule]  # value = <TileRule.RoundTile: 2>
        StretchTile: typing.ClassVar[Qt.TileRule]  # value = <TileRule.StretchTile: 0>
    class TimeSpec(enum.Enum):
        LocalTime: typing.ClassVar[Qt.TimeSpec]  # value = <TimeSpec.LocalTime: 0>
        OffsetFromUTC: typing.ClassVar[Qt.TimeSpec]  # value = <TimeSpec.OffsetFromUTC: 2>
        TimeZone: typing.ClassVar[Qt.TimeSpec]  # value = <TimeSpec.TimeZone: 3>
        UTC: typing.ClassVar[Qt.TimeSpec]  # value = <TimeSpec.UTC: 1>
    class TimerType(enum.Enum):
        CoarseTimer: typing.ClassVar[Qt.TimerType]  # value = <TimerType.CoarseTimer: 1>
        PreciseTimer: typing.ClassVar[Qt.TimerType]  # value = <TimerType.PreciseTimer: 0>
        VeryCoarseTimer: typing.ClassVar[Qt.TimerType]  # value = <TimerType.VeryCoarseTimer: 2>
    class ToolBarArea(enum.Flag):
        BottomToolBarArea: typing.ClassVar[Qt.ToolBarArea]  # value = <ToolBarArea.BottomToolBarArea: 8>
        LeftToolBarArea: typing.ClassVar[Qt.ToolBarArea]  # value = <ToolBarArea.LeftToolBarArea: 1>
        RightToolBarArea: typing.ClassVar[Qt.ToolBarArea]  # value = <ToolBarArea.RightToolBarArea: 2>
        TopToolBarArea: typing.ClassVar[Qt.ToolBarArea]  # value = <ToolBarArea.TopToolBarArea: 4>
    class ToolButtonStyle(enum.Enum):
        ToolButtonFollowStyle: typing.ClassVar[Qt.ToolButtonStyle]  # value = <ToolButtonStyle.ToolButtonFollowStyle: 4>
        ToolButtonIconOnly: typing.ClassVar[Qt.ToolButtonStyle]  # value = <ToolButtonStyle.ToolButtonIconOnly: 0>
        ToolButtonTextBesideIcon: typing.ClassVar[Qt.ToolButtonStyle]  # value = <ToolButtonStyle.ToolButtonTextBesideIcon: 2>
        ToolButtonTextOnly: typing.ClassVar[Qt.ToolButtonStyle]  # value = <ToolButtonStyle.ToolButtonTextOnly: 1>
        ToolButtonTextUnderIcon: typing.ClassVar[Qt.ToolButtonStyle]  # value = <ToolButtonStyle.ToolButtonTextUnderIcon: 3>
    class TouchPointState(enum.Flag):
        TouchPointMoved: typing.ClassVar[Qt.TouchPointState]  # value = <TouchPointState.TouchPointMoved: 2>
        TouchPointPressed: typing.ClassVar[Qt.TouchPointState]  # value = <TouchPointState.TouchPointPressed: 1>
        TouchPointReleased: typing.ClassVar[Qt.TouchPointState]  # value = <TouchPointState.TouchPointReleased: 8>
        TouchPointStationary: typing.ClassVar[Qt.TouchPointState]  # value = <TouchPointState.TouchPointStationary: 4>
    class TransformationMode(enum.Enum):
        FastTransformation: typing.ClassVar[Qt.TransformationMode]  # value = <TransformationMode.FastTransformation: 0>
        SmoothTransformation: typing.ClassVar[Qt.TransformationMode]  # value = <TransformationMode.SmoothTransformation: 1>
    class UIEffect(enum.Enum):
        UI_AnimateCombo: typing.ClassVar[Qt.UIEffect]  # value = <UIEffect.UI_AnimateCombo: 3>
        UI_AnimateMenu: typing.ClassVar[Qt.UIEffect]  # value = <UIEffect.UI_AnimateMenu: 1>
        UI_AnimateToolBox: typing.ClassVar[Qt.UIEffect]  # value = <UIEffect.UI_AnimateToolBox: 6>
        UI_AnimateTooltip: typing.ClassVar[Qt.UIEffect]  # value = <UIEffect.UI_AnimateTooltip: 4>
        UI_FadeMenu: typing.ClassVar[Qt.UIEffect]  # value = <UIEffect.UI_FadeMenu: 2>
        UI_FadeTooltip: typing.ClassVar[Qt.UIEffect]  # value = <UIEffect.UI_FadeTooltip: 5>
        UI_General: typing.ClassVar[Qt.UIEffect]  # value = <UIEffect.UI_General: 0>
    class WhiteSpaceMode(enum.Enum):
        WhiteSpaceModeUndefined: typing.ClassVar[Qt.WhiteSpaceMode]  # value = <WhiteSpaceMode.WhiteSpaceModeUndefined: -1>
        WhiteSpaceNoWrap: typing.ClassVar[Qt.WhiteSpaceMode]  # value = <WhiteSpaceMode.WhiteSpaceNoWrap: 2>
        WhiteSpaceNormal: typing.ClassVar[Qt.WhiteSpaceMode]  # value = <WhiteSpaceMode.WhiteSpaceNormal: 0>
        WhiteSpacePre: typing.ClassVar[Qt.WhiteSpaceMode]  # value = <WhiteSpaceMode.WhiteSpacePre: 1>
    class WidgetAttribute(enum.Enum):
        WA_AcceptDrops: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_AcceptDrops: 78>
        WA_AcceptTouchEvents: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_AcceptTouchEvents: 121>
        WA_AlwaysShowToolTips: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_AlwaysShowToolTips: 84>
        WA_AlwaysStackOnTop: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_AlwaysStackOnTop: 128>
        WA_AttributeCount: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_AttributeCount: 132>
        WA_ContentsMarginsRespectsSafeArea: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_ContentsMarginsRespectsSafeArea: 130>
        WA_CustomWhatsThis: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_CustomWhatsThis: 47>
        WA_DeleteOnClose: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_DeleteOnClose: 55>
        WA_Disabled: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_Disabled: 0>
        WA_DontCreateNativeAncestors: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_DontCreateNativeAncestors: 101>
        WA_DontShowOnScreen: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_DontShowOnScreen: 103>
        WA_ForceDisabled: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_ForceDisabled: 32>
        WA_ForceUpdatesDisabled: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_ForceUpdatesDisabled: 59>
        WA_GrabbedShortcut: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_GrabbedShortcut: 50>
        WA_Hover: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_Hover: 74>
        WA_InputMethodEnabled: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_InputMethodEnabled: 14>
        WA_InputMethodTransparent: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_InputMethodTransparent: 75>
        WA_InvalidSize: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_InvalidSize: 45>
        WA_KeyCompression: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_KeyCompression: 33>
        WA_KeyboardFocusChange: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_KeyboardFocusChange: 77>
        WA_LaidOut: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_LaidOut: 7>
        WA_LayoutOnEntireRect: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_LayoutOnEntireRect: 48>
        WA_LayoutUsesWidgetRect: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_LayoutUsesWidgetRect: 92>
        WA_MacAlwaysShowToolWindow: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MacAlwaysShowToolWindow: 96>
        WA_MacMiniSize: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MacMiniSize: 91>
        WA_MacNormalSize: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MacNormalSize: 89>
        WA_MacOpaqueSizeGrip: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MacOpaqueSizeGrip: 85>
        WA_MacShowFocusRect: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MacShowFocusRect: 88>
        WA_MacSmallSize: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MacSmallSize: 90>
        WA_Mapped: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_Mapped: 11>
        WA_MouseNoMask: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MouseNoMask: 71>
        WA_MouseTracking: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_MouseTracking: 2>
        WA_Moved: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_Moved: 43>
        WA_NativeWindow: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_NativeWindow: 100>
        WA_NoChildEventsForParent: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_NoChildEventsForParent: 58>
        WA_NoChildEventsFromChildren: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_NoChildEventsFromChildren: 39>
        WA_NoMousePropagation: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_NoMousePropagation: 73>
        WA_NoMouseReplay: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_NoMouseReplay: 54>
        WA_NoSystemBackground: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_NoSystemBackground: 9>
        WA_NoX11EventCompression: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_NoX11EventCompression: 81>
        WA_OpaquePaintEvent: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_OpaquePaintEvent: 4>
        WA_OutsideWSRange: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_OutsideWSRange: 49>
        WA_PaintOnScreen: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_PaintOnScreen: 8>
        WA_PaintUnclipped: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_PaintUnclipped: 52>
        WA_PendingMoveEvent: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_PendingMoveEvent: 34>
        WA_PendingResizeEvent: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_PendingResizeEvent: 35>
        WA_PendingUpdate: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_PendingUpdate: 44>
        WA_QuitOnClose: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_QuitOnClose: 76>
        WA_Resized: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_Resized: 42>
        WA_RightToLeft: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_RightToLeft: 56>
        WA_SetCursor: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_SetCursor: 38>
        WA_SetFont: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_SetFont: 37>
        WA_SetLayoutDirection: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_SetLayoutDirection: 57>
        WA_SetLocale: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_SetLocale: 87>
        WA_SetPalette: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_SetPalette: 36>
        WA_SetStyle: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_SetStyle: 86>
        WA_SetWindowIcon: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_SetWindowIcon: 53>
        WA_ShowWithoutActivating: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_ShowWithoutActivating: 98>
        WA_StaticContents: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_StaticContents: 5>
        WA_StyleSheet: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_StyleSheet: 97>
        WA_StyleSheetTarget: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_StyleSheetTarget: 131>
        WA_StyledBackground: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_StyledBackground: 93>
        WA_TabletTracking: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_TabletTracking: 129>
        WA_TintedBackground: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_TintedBackground: 82>
        WA_TouchPadAcceptSingleTouchEvents: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_TouchPadAcceptSingleTouchEvents: 123>
        WA_TranslucentBackground: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_TranslucentBackground: 120>
        WA_TransparentForMouseEvents: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_TransparentForMouseEvents: 51>
        WA_UnderMouse: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_UnderMouse: 1>
        WA_UpdatesDisabled: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_UpdatesDisabled: 10>
        WA_WState_CompressKeys: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_CompressKeys: 61>
        WA_WState_ConfigPending: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_ConfigPending: 64>
        WA_WState_Created: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_Created: 60>
        WA_WState_ExplicitShowHide: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_ExplicitShowHide: 69>
        WA_WState_Hidden: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_Hidden: 16>
        WA_WState_InPaintEvent: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_InPaintEvent: 62>
        WA_WState_OwnSizePolicy: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_OwnSizePolicy: 68>
        WA_WState_Polished: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_Polished: 66>
        WA_WState_Reparented: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_Reparented: 63>
        WA_WState_Visible: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WState_Visible: 15>
        WA_WindowModified: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WindowModified: 41>
        WA_WindowPropagation: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_WindowPropagation: 80>
        WA_X11DoNotAcceptFocus: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11DoNotAcceptFocus: 126>
        WA_X11NetWmWindowTypeCombo: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeCombo: 115>
        WA_X11NetWmWindowTypeDND: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeDND: 116>
        WA_X11NetWmWindowTypeDesktop: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeDesktop: 104>
        WA_X11NetWmWindowTypeDialog: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeDialog: 110>
        WA_X11NetWmWindowTypeDock: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeDock: 105>
        WA_X11NetWmWindowTypeDropDownMenu: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeDropDownMenu: 111>
        WA_X11NetWmWindowTypeMenu: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeMenu: 107>
        WA_X11NetWmWindowTypeNotification: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeNotification: 114>
        WA_X11NetWmWindowTypePopupMenu: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypePopupMenu: 112>
        WA_X11NetWmWindowTypeSplash: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeSplash: 109>
        WA_X11NetWmWindowTypeToolBar: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeToolBar: 106>
        WA_X11NetWmWindowTypeToolTip: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeToolTip: 113>
        WA_X11NetWmWindowTypeUtility: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11NetWmWindowTypeUtility: 108>
        WA_X11OpenGLOverlay: typing.ClassVar[Qt.WidgetAttribute]  # value = <WidgetAttribute.WA_X11OpenGLOverlay: 83>
    class WindowFrameSection(enum.Enum):
        BottomLeftSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.BottomLeftSection: 8>
        BottomRightSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.BottomRightSection: 6>
        BottomSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.BottomSection: 7>
        LeftSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.LeftSection: 1>
        NoSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.NoSection: 0>
        RightSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.RightSection: 5>
        TitleBarArea: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.TitleBarArea: 9>
        TopLeftSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.TopLeftSection: 2>
        TopRightSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.TopRightSection: 4>
        TopSection: typing.ClassVar[Qt.WindowFrameSection]  # value = <WindowFrameSection.TopSection: 3>
    class WindowModality(enum.Enum):
        ApplicationModal: typing.ClassVar[Qt.WindowModality]  # value = <WindowModality.ApplicationModal: 2>
        NonModal: typing.ClassVar[Qt.WindowModality]  # value = <WindowModality.NonModal: 0>
        WindowModal: typing.ClassVar[Qt.WindowModality]  # value = <WindowModality.WindowModal: 1>
    class WindowState(enum.Flag):
        WindowActive: typing.ClassVar[Qt.WindowState]  # value = <WindowState.WindowActive: 8>
        WindowFullScreen: typing.ClassVar[Qt.WindowState]  # value = <WindowState.WindowFullScreen: 4>
        WindowMaximized: typing.ClassVar[Qt.WindowState]  # value = <WindowState.WindowMaximized: 2>
        WindowMinimized: typing.ClassVar[Qt.WindowState]  # value = <WindowState.WindowMinimized: 1>
    class WindowType(enum.IntFlag):
        BypassGraphicsProxyWidget: typing.ClassVar[Qt.WindowType]  # value = <WindowType.BypassGraphicsProxyWidget: 536870912>
        CustomizeWindowHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.CustomizeWindowHint: 33554432>
        FramelessWindowHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.FramelessWindowHint: 2048>
        MSWindowsFixedSizeDialogHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.MSWindowsFixedSizeDialogHint: 256>
        MSWindowsOwnDC: typing.ClassVar[Qt.WindowType]  # value = <WindowType.MSWindowsOwnDC: 512>
        MacWindowToolBarButtonHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.MacWindowToolBarButtonHint: 268435456>
        MaximizeUsingFullscreenGeometryHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.MaximizeUsingFullscreenGeometryHint: 4194304>
        NoDropShadowWindowHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.NoDropShadowWindowHint: 1073741824>
        Window: typing.ClassVar[Qt.WindowType]  # value = <WindowType.Window: 1>
        WindowCloseButtonHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowCloseButtonHint: 134217728>
        WindowContextHelpButtonHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowContextHelpButtonHint: 65536>
        WindowDoesNotAcceptFocus: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowDoesNotAcceptFocus: 2097152>
        WindowFullscreenButtonHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowFullscreenButtonHint: 2147483648>
        WindowMaximizeButtonHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowMaximizeButtonHint: 32768>
        WindowMinimizeButtonHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowMinimizeButtonHint: 16384>
        WindowOverridesSystemGestures: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowOverridesSystemGestures: 1048576>
        WindowShadeButtonHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowShadeButtonHint: 131072>
        WindowStaysOnBottomHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowStaysOnBottomHint: 67108864>
        WindowStaysOnTopHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowStaysOnTopHint: 262144>
        WindowSystemMenuHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowSystemMenuHint: 8192>
        WindowTitleHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowTitleHint: 4096>
        WindowTransparentForInput: typing.ClassVar[Qt.WindowType]  # value = <WindowType.WindowTransparentForInput: 524288>
        X11BypassWindowManagerHint: typing.ClassVar[Qt.WindowType]  # value = <WindowType.X11BypassWindowManagerHint: 1024>
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
    def bin(*args, **kwargs):
        ...
    @staticmethod
    def bom(*args, **kwargs):
        ...
    @staticmethod
    def center(*args, **kwargs):
        ...
    @staticmethod
    def convertFromPlainText(*args, **kwargs):
        ...
    @staticmethod
    def dec(*args, **kwargs):
        ...
    @staticmethod
    def endl(*args, **kwargs):
        ...
    @staticmethod
    def fixed(*args, **kwargs):
        ...
    @staticmethod
    def flush(*args, **kwargs):
        ...
    @staticmethod
    def forcepoint(*args, **kwargs):
        ...
    @staticmethod
    def forcesign(*args, **kwargs):
        ...
    @staticmethod
    def hex(*args, **kwargs):
        ...
    @staticmethod
    def left(*args, **kwargs):
        ...
    @staticmethod
    def lowercasebase(*args, **kwargs):
        ...
    @staticmethod
    def lowercasedigits(*args, **kwargs):
        ...
    @staticmethod
    def mightBeRichText(*args, **kwargs):
        ...
    @staticmethod
    def noforcepoint(*args, **kwargs):
        ...
    @staticmethod
    def noforcesign(*args, **kwargs):
        ...
    @staticmethod
    def noshowbase(*args, **kwargs):
        ...
    @staticmethod
    def oct(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def right(*args, **kwargs):
        ...
    @staticmethod
    def scientific(*args, **kwargs):
        ...
    @staticmethod
    def showbase(*args, **kwargs):
        ...
    @staticmethod
    def uppercasebase(*args, **kwargs):
        ...
    @staticmethod
    def uppercasedigits(*args, **kwargs):
        ...
    @staticmethod
    def ws(*args, **kwargs):
        ...
class QtMsgType(enum.Enum):
    QtCriticalMsg: typing.ClassVar[QtMsgType]  # value = <QtMsgType.QtCriticalMsg: 2>
    QtDebugMsg: typing.ClassVar[QtMsgType]  # value = <QtMsgType.QtDebugMsg: 0>
    QtFatalMsg: typing.ClassVar[QtMsgType]  # value = <QtMsgType.QtFatalMsg: 3>
    QtInfoMsg: typing.ClassVar[QtMsgType]  # value = <QtMsgType.QtInfoMsg: 4>
    QtWarningMsg: typing.ClassVar[QtMsgType]  # value = <QtMsgType.QtWarningMsg: 1>
class pyqtBoundSignal:
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def connect(slot, type = ..., no_receiver_check = False):
        """
        slot is either a Python callable or another signal.
        type is a Qt.ConnectionType.
        no_receiver_check is True to disable the check that the receiver's C++
        instance still exists when the signal is emitted.
        """
    @staticmethod
    def disconnect(*args, **kwargs):
        """
        slot is an optional Python callable or another signal.  If it is omitted
        then the signal is disconnected from everything it is connected to.
        """
    @staticmethod
    def emit(*args):
        """
        *args are the values that will be passed as arguments to all connected
        slots.
        """
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
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
    def __repr__(self):
        """
        Return repr(self).
        """
class pyqtProperty:
    """
    pyqtProperty(type, fget=None, fset=None, freset=None, fdel=None, doc=None,
            designable=True, scriptable=True, stored=True, user=False,
            constant=False, final=False, notify=None,
            revision=0) -> property attribute
    
    type is the type of the property.  It is either a type object or a string
    that is the name of a C++ type.
    freset is a function for resetting an attribute to its default value.
    designable sets the DESIGNABLE flag (the default is True for writable
    properties and False otherwise).
    scriptable sets the SCRIPTABLE flag.
    stored sets the STORED flag.
    user sets the USER flag.
    constant sets the CONSTANT flag.
    final sets the FINAL flag.
    notify is the NOTIFY signal.
    revision is the REVISION.
    The other parameters are the same as those required by the standard Python
    property type.  Properties defined using pyqtProperty behave as both Python
    and Qt properties.
    Decorators can be used to define new properties or to modify existing ones.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def deleter(*args, **kwargs):
        """
        Descriptor to change the deleter on a property.
        """
    @staticmethod
    def getter(*args, **kwargs):
        """
        Descriptor to change the getter on a property.
        """
    @staticmethod
    def read(*args, **kwargs):
        """
        Descriptor to change the getter on a property.
        """
    @staticmethod
    def reset(*args, **kwargs):
        """
        Descriptor to change the reset on a property.
        """
    @staticmethod
    def setter(*args, **kwargs):
        """
        Descriptor to change the setter on a property.
        """
    @staticmethod
    def write(*args, **kwargs):
        """
        Descriptor to change the setter on a property.
        """
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
        """
    def __delete__(self, instance):
        """
        Delete an attribute of instance.
        """
    def __get__(self, instance, owner = None):
        """
        Return an attribute of instance, which is of type owner.
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __set__(self, instance, value):
        """
        Set an attribute of instance to value.
        """
class pyqtSignal:
    """
    pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
    
    types is normally a sequence of individual types.  Each type is either a
    type object or a string that is the name of a C++ type.  Alternatively
    each type could itself be a sequence of types each describing a different
    overloaded signal.
    name is the optional C++ name of the signal.  If it is not specified then
    the name of the class attribute that is bound to the signal is used.
    revision is the optional revision of the signal that is exported to QML.
    If it is not specified then 0 is used.
    arguments is the optional sequence of the names of the signal's arguments.
    """
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __call__(self, *args, **kwargs):
        """
        Call self as a function.
        """
    def __get__(self, instance, owner = None):
        """
        Return an attribute of instance, which is of type owner.
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __repr__(self):
        """
        Return repr(self).
        """
def QT_TRANSLATE_NOOP(*args, **kwargs):
    ...
def QT_TR_NOOP(*args, **kwargs):
    ...
def Q_ARG(*args, **kwargs):
    ...
def Q_RETURN_ARG(*args, **kwargs):
    ...
def pyqtClassInfo(*args, **kwargs):
    ...
def pyqtEnum(*args, **kwargs):
    ...
def pyqtPickleProtocol(*args, **kwargs):
    ...
def pyqtRemoveInputHook(*args, **kwargs):
    ...
def pyqtRestoreInputHook(*args, **kwargs):
    ...
def pyqtSetPickleProtocol(*args, **kwargs):
    ...
def pyqtSlot(*args, **kwargs):
    """
    @pyqtSlot(*types, name: typing.Optional[str], result: typing.Optional[str])
    
    This is a decorator applied to Python methods of a QObject that marks them
    as Qt slots.
    The non-keyword arguments are the types of the slot arguments and each may
    be a Python type object or a string specifying a C++ type.
    name is the name of the slot and defaults to the name of the method.
    result is type of the value returned by the slot.
    """
def qAbs(*args, **kwargs):
    ...
def qAddPostRoutine(*args, **kwargs):
    ...
def qAddPreRoutine(*args, **kwargs):
    ...
def qChecksum(*args, **kwargs):
    ...
def qCompress(*args, **kwargs):
    ...
def qCritical(*args, **kwargs):
    ...
def qDebug(*args, **kwargs):
    ...
def qEnvironmentVariable(*args, **kwargs):
    ...
def qEnvironmentVariableIntValue(*args, **kwargs):
    ...
def qEnvironmentVariableIsEmpty(*args, **kwargs):
    ...
def qEnvironmentVariableIsSet(*args, **kwargs):
    ...
def qFatal(*args, **kwargs):
    ...
def qFloatDistance(*args, **kwargs):
    ...
def qFormatLogMessage(*args, **kwargs):
    ...
def qFuzzyCompare(*args, **kwargs):
    ...
def qFuzzyIsNull(*args, **kwargs):
    ...
def qInf(*args, **kwargs):
    ...
def qInfo(*args, **kwargs):
    ...
def qInstallMessageHandler(*args, **kwargs):
    ...
def qIsFinite(*args, **kwargs):
    ...
def qIsInf(*args, **kwargs):
    ...
def qIsNaN(*args, **kwargs):
    ...
def qQNaN(*args, **kwargs):
    ...
def qRegisterResourceData(*args, **kwargs):
    ...
def qRemovePostRoutine(*args, **kwargs):
    ...
def qRound(*args, **kwargs):
    ...
def qRound64(*args, **kwargs):
    ...
def qSNaN(*args, **kwargs):
    ...
def qSetFieldWidth(*args, **kwargs):
    ...
def qSetMessagePattern(*args, **kwargs):
    ...
def qSetPadChar(*args, **kwargs):
    ...
def qSetRealNumberPrecision(*args, **kwargs):
    ...
def qUncompress(*args, **kwargs):
    ...
def qUnregisterResourceData(*args, **kwargs):
    ...
def qVersion(*args, **kwargs):
    ...
def qWarning(*args, **kwargs):
    ...
def qYieldCpu(*args, **kwargs):
    ...
PYQT_VERSION: int = 395009
PYQT_VERSION_STR: str = '6.7.1'
QT_VERSION: int = 395010
QT_VERSION_STR: str = '6.7.2'
__license__: mappingproxy  # value = mappingproxy({'Type': 'gpl'})
