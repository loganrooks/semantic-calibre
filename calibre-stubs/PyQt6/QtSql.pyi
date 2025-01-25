import PyQt6.QtCore
import PyQt6.QtWidgets
import PyQt6.sip
from __future__ import annotations
import enum
import typing
__all__ = ['QSql', 'QSqlDatabase', 'QSqlDriver', 'QSqlDriverCreatorBase', 'QSqlError', 'QSqlField', 'QSqlIndex', 'QSqlQuery', 'QSqlQueryModel', 'QSqlRecord', 'QSqlRelation', 'QSqlRelationalDelegate', 'QSqlRelationalTableModel', 'QSqlResult', 'QSqlTableModel']
class QSql(PyQt6.sip.simplewrapper):
    class Location(enum.Enum):
        AfterLastRow: typing.ClassVar[QSql.Location]  # value = <Location.AfterLastRow: -2>
        BeforeFirstRow: typing.ClassVar[QSql.Location]  # value = <Location.BeforeFirstRow: -1>
    class NumericalPrecisionPolicy(enum.Enum):
        HighPrecision: typing.ClassVar[QSql.NumericalPrecisionPolicy]  # value = <NumericalPrecisionPolicy.HighPrecision: 0>
        LowPrecisionDouble: typing.ClassVar[QSql.NumericalPrecisionPolicy]  # value = <NumericalPrecisionPolicy.LowPrecisionDouble: 4>
        LowPrecisionInt32: typing.ClassVar[QSql.NumericalPrecisionPolicy]  # value = <NumericalPrecisionPolicy.LowPrecisionInt32: 1>
        LowPrecisionInt64: typing.ClassVar[QSql.NumericalPrecisionPolicy]  # value = <NumericalPrecisionPolicy.LowPrecisionInt64: 2>
    class ParamTypeFlag(enum.Flag):
        Binary: typing.ClassVar[QSql.ParamTypeFlag]  # value = <ParamTypeFlag.Binary: 4>
        In: typing.ClassVar[QSql.ParamTypeFlag]  # value = <ParamTypeFlag.In: 1>
        Out: typing.ClassVar[QSql.ParamTypeFlag]  # value = <ParamTypeFlag.Out: 2>
    class TableType(enum.Enum):
        AllTables: typing.ClassVar[QSql.TableType]  # value = <TableType.AllTables: 255>
        SystemTables: typing.ClassVar[QSql.TableType]  # value = <TableType.SystemTables: 2>
        Tables: typing.ClassVar[QSql.TableType]  # value = <TableType.Tables: 1>
        Views: typing.ClassVar[QSql.TableType]  # value = <TableType.Views: 4>
class QSqlDatabase(PyQt6.sip.simplewrapper):
    @staticmethod
    def addDatabase(*args, **kwargs):
        ...
    @staticmethod
    def cloneDatabase(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def commit(*args, **kwargs):
        ...
    @staticmethod
    def connectOptions(*args, **kwargs):
        ...
    @staticmethod
    def connectionName(*args, **kwargs):
        ...
    @staticmethod
    def connectionNames(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def database(*args, **kwargs):
        ...
    @staticmethod
    def databaseName(*args, **kwargs):
        ...
    @staticmethod
    def driver(*args, **kwargs):
        ...
    @staticmethod
    def driverName(*args, **kwargs):
        ...
    @staticmethod
    def drivers(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def hostName(*args, **kwargs):
        ...
    @staticmethod
    def isDriverAvailable(*args, **kwargs):
        ...
    @staticmethod
    def isOpen(*args, **kwargs):
        ...
    @staticmethod
    def isOpenError(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastError(*args, **kwargs):
        ...
    @staticmethod
    def numericalPrecisionPolicy(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def password(*args, **kwargs):
        ...
    @staticmethod
    def port(*args, **kwargs):
        ...
    @staticmethod
    def primaryIndex(*args, **kwargs):
        ...
    @staticmethod
    def record(*args, **kwargs):
        ...
    @staticmethod
    def registerSqlDriver(*args, **kwargs):
        ...
    @staticmethod
    def removeDatabase(*args, **kwargs):
        ...
    @staticmethod
    def rollback(*args, **kwargs):
        ...
    @staticmethod
    def setConnectOptions(*args, **kwargs):
        ...
    @staticmethod
    def setDatabaseName(*args, **kwargs):
        ...
    @staticmethod
    def setHostName(*args, **kwargs):
        ...
    @staticmethod
    def setNumericalPrecisionPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setPassword(*args, **kwargs):
        ...
    @staticmethod
    def setPort(*args, **kwargs):
        ...
    @staticmethod
    def setUserName(*args, **kwargs):
        ...
    @staticmethod
    def tables(*args, **kwargs):
        ...
    @staticmethod
    def transaction(*args, **kwargs):
        ...
    @staticmethod
    def userName(*args, **kwargs):
        ...
class QSqlDriver(PyQt6.QtCore.QObject):
    class DbmsType(enum.Enum):
        DB2: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.DB2: 8>
        Interbase: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.Interbase: 7>
        MSSqlServer: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.MSSqlServer: 1>
        MimerSQL: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.MimerSQL: 9>
        MySqlServer: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.MySqlServer: 2>
        Oracle: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.Oracle: 4>
        PostgreSQL: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.PostgreSQL: 3>
        SQLite: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.SQLite: 6>
        Sybase: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.Sybase: 5>
        UnknownDbms: typing.ClassVar[QSqlDriver.DbmsType]  # value = <DbmsType.UnknownDbms: 0>
    class DriverFeature(enum.Enum):
        BLOB: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.BLOB: 2>
        BatchOperations: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.BatchOperations: 8>
        EventNotifications: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.EventNotifications: 11>
        FinishQuery: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.FinishQuery: 12>
        LastInsertId: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.LastInsertId: 7>
        LowPrecisionNumbers: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.LowPrecisionNumbers: 10>
        MultipleResultSets: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.MultipleResultSets: 13>
        NamedPlaceholders: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.NamedPlaceholders: 5>
        PositionalPlaceholders: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.PositionalPlaceholders: 6>
        PreparedQueries: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.PreparedQueries: 4>
        QuerySize: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.QuerySize: 1>
        SimpleLocking: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.SimpleLocking: 9>
        Transactions: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.Transactions: 0>
        Unicode: typing.ClassVar[QSqlDriver.DriverFeature]  # value = <DriverFeature.Unicode: 3>
    class IdentifierType(enum.Enum):
        FieldName: typing.ClassVar[QSqlDriver.IdentifierType]  # value = <IdentifierType.FieldName: 0>
        TableName: typing.ClassVar[QSqlDriver.IdentifierType]  # value = <IdentifierType.TableName: 1>
    class NotificationSource(enum.Enum):
        OtherSource: typing.ClassVar[QSqlDriver.NotificationSource]  # value = <NotificationSource.OtherSource: 2>
        SelfSource: typing.ClassVar[QSqlDriver.NotificationSource]  # value = <NotificationSource.SelfSource: 1>
        UnknownSource: typing.ClassVar[QSqlDriver.NotificationSource]  # value = <NotificationSource.UnknownSource: 0>
    class StatementType(enum.Enum):
        DeleteStatement: typing.ClassVar[QSqlDriver.StatementType]  # value = <StatementType.DeleteStatement: 4>
        InsertStatement: typing.ClassVar[QSqlDriver.StatementType]  # value = <StatementType.InsertStatement: 3>
        SelectStatement: typing.ClassVar[QSqlDriver.StatementType]  # value = <StatementType.SelectStatement: 1>
        UpdateStatement: typing.ClassVar[QSqlDriver.StatementType]  # value = <StatementType.UpdateStatement: 2>
        WhereStatement: typing.ClassVar[QSqlDriver.StatementType]  # value = <StatementType.WhereStatement: 0>
    @staticmethod
    def beginTransaction(*args, **kwargs):
        ...
    @staticmethod
    def close(*args, **kwargs):
        ...
    @staticmethod
    def commitTransaction(*args, **kwargs):
        ...
    @staticmethod
    def createResult(*args, **kwargs):
        ...
    @staticmethod
    def dbmsType(*args, **kwargs):
        ...
    @staticmethod
    def escapeIdentifier(*args, **kwargs):
        ...
    @staticmethod
    def formatValue(*args, **kwargs):
        ...
    @staticmethod
    def handle(*args, **kwargs):
        ...
    @staticmethod
    def hasFeature(*args, **kwargs):
        ...
    @staticmethod
    def isIdentifierEscaped(*args, **kwargs):
        ...
    @staticmethod
    def isOpen(*args, **kwargs):
        ...
    @staticmethod
    def isOpenError(*args, **kwargs):
        ...
    @staticmethod
    def lastError(*args, **kwargs):
        ...
    @staticmethod
    def maximumIdentifierLength(*args, **kwargs):
        ...
    @staticmethod
    def notification(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def numericalPrecisionPolicy(*args, **kwargs):
        ...
    @staticmethod
    def open(*args, **kwargs):
        ...
    @staticmethod
    def primaryIndex(*args, **kwargs):
        ...
    @staticmethod
    def record(*args, **kwargs):
        ...
    @staticmethod
    def rollbackTransaction(*args, **kwargs):
        ...
    @staticmethod
    def setLastError(*args, **kwargs):
        ...
    @staticmethod
    def setNumericalPrecisionPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setOpen(*args, **kwargs):
        ...
    @staticmethod
    def setOpenError(*args, **kwargs):
        ...
    @staticmethod
    def sqlStatement(*args, **kwargs):
        ...
    @staticmethod
    def stripDelimiters(*args, **kwargs):
        ...
    @staticmethod
    def subscribeToNotification(*args, **kwargs):
        ...
    @staticmethod
    def subscribedToNotifications(*args, **kwargs):
        ...
    @staticmethod
    def tables(*args, **kwargs):
        ...
    @staticmethod
    def unsubscribeFromNotification(*args, **kwargs):
        ...
class QSqlDriverCreatorBase(PyQt6.sip.wrapper):
    @staticmethod
    def createObject(*args, **kwargs):
        ...
class QSqlError(PyQt6.sip.simplewrapper):
    class ErrorType(enum.Enum):
        ConnectionError: typing.ClassVar[QSqlError.ErrorType]  # value = <ErrorType.ConnectionError: 1>
        NoError: typing.ClassVar[QSqlError.ErrorType]  # value = <ErrorType.NoError: 0>
        StatementError: typing.ClassVar[QSqlError.ErrorType]  # value = <ErrorType.StatementError: 2>
        TransactionError: typing.ClassVar[QSqlError.ErrorType]  # value = <ErrorType.TransactionError: 3>
        UnknownError: typing.ClassVar[QSqlError.ErrorType]  # value = <ErrorType.UnknownError: 4>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def databaseText(*args, **kwargs):
        ...
    @staticmethod
    def driverText(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def nativeErrorCode(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def text(*args, **kwargs):
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
class QSqlField(PyQt6.sip.simplewrapper):
    class RequiredStatus(enum.Enum):
        Optional: typing.ClassVar[QSqlField.RequiredStatus]  # value = <RequiredStatus.Optional: 0>
        Required: typing.ClassVar[QSqlField.RequiredStatus]  # value = <RequiredStatus.Required: 1>
        Unknown: typing.ClassVar[QSqlField.RequiredStatus]  # value = <RequiredStatus.Unknown: -1>
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def defaultValue(*args, **kwargs):
        ...
    @staticmethod
    def isAutoValue(*args, **kwargs):
        ...
    @staticmethod
    def isGenerated(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def length(*args, **kwargs):
        ...
    @staticmethod
    def metaType(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def precision(*args, **kwargs):
        ...
    @staticmethod
    def requiredStatus(*args, **kwargs):
        ...
    @staticmethod
    def setAutoValue(*args, **kwargs):
        ...
    @staticmethod
    def setDefaultValue(*args, **kwargs):
        ...
    @staticmethod
    def setGenerated(*args, **kwargs):
        ...
    @staticmethod
    def setLength(*args, **kwargs):
        ...
    @staticmethod
    def setMetaType(*args, **kwargs):
        ...
    @staticmethod
    def setName(*args, **kwargs):
        ...
    @staticmethod
    def setPrecision(*args, **kwargs):
        ...
    @staticmethod
    def setReadOnly(*args, **kwargs):
        ...
    @staticmethod
    def setRequired(*args, **kwargs):
        ...
    @staticmethod
    def setRequiredStatus(*args, **kwargs):
        ...
    @staticmethod
    def setSqlType(*args, **kwargs):
        ...
    @staticmethod
    def setTableName(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def tableName(*args, **kwargs):
        ...
    @staticmethod
    def typeID(*args, **kwargs):
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
class QSqlIndex(QSqlRecord):
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def cursorName(*args, **kwargs):
        ...
    @staticmethod
    def isDescending(*args, **kwargs):
        ...
    @staticmethod
    def name(*args, **kwargs):
        ...
    @staticmethod
    def setCursorName(*args, **kwargs):
        ...
    @staticmethod
    def setDescending(*args, **kwargs):
        ...
    @staticmethod
    def setName(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
class QSqlQuery(PyQt6.sip.simplewrapper):
    class BatchExecutionMode(enum.Enum):
        ValuesAsColumns: typing.ClassVar[QSqlQuery.BatchExecutionMode]  # value = <BatchExecutionMode.ValuesAsColumns: 1>
        ValuesAsRows: typing.ClassVar[QSqlQuery.BatchExecutionMode]  # value = <BatchExecutionMode.ValuesAsRows: 0>
    @staticmethod
    def addBindValue(*args, **kwargs):
        ...
    @staticmethod
    def at(*args, **kwargs):
        ...
    @staticmethod
    def bindValue(*args, **kwargs):
        ...
    @staticmethod
    def boundValue(*args, **kwargs):
        ...
    @staticmethod
    def boundValueName(*args, **kwargs):
        ...
    @staticmethod
    def boundValueNames(*args, **kwargs):
        ...
    @staticmethod
    def boundValues(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def driver(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def execBatch(*args, **kwargs):
        ...
    @staticmethod
    def executedQuery(*args, **kwargs):
        ...
    @staticmethod
    def finish(*args, **kwargs):
        ...
    @staticmethod
    def first(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def isForwardOnly(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isPositionalBindingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isSelect(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def last(*args, **kwargs):
        ...
    @staticmethod
    def lastError(*args, **kwargs):
        ...
    @staticmethod
    def lastInsertId(*args, **kwargs):
        ...
    @staticmethod
    def lastQuery(*args, **kwargs):
        ...
    @staticmethod
    def next(*args, **kwargs):
        ...
    @staticmethod
    def nextResult(*args, **kwargs):
        ...
    @staticmethod
    def numRowsAffected(*args, **kwargs):
        ...
    @staticmethod
    def numericalPrecisionPolicy(*args, **kwargs):
        ...
    @staticmethod
    def prepare(*args, **kwargs):
        ...
    @staticmethod
    def previous(*args, **kwargs):
        ...
    @staticmethod
    def record(*args, **kwargs):
        ...
    @staticmethod
    def result(*args, **kwargs):
        ...
    @staticmethod
    def seek(*args, **kwargs):
        ...
    @staticmethod
    def setForwardOnly(*args, **kwargs):
        ...
    @staticmethod
    def setNumericalPrecisionPolicy(*args, **kwargs):
        ...
    @staticmethod
    def setPositionalBindingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def value(*args, **kwargs):
        ...
class QSqlQueryModel(PyQt6.QtCore.QAbstractTableModel):
    @staticmethod
    def beginInsertColumns(*args, **kwargs):
        ...
    @staticmethod
    def beginInsertRows(*args, **kwargs):
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
    def canFetchMore(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def columnCount(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def endInsertColumns(*args, **kwargs):
        ...
    @staticmethod
    def endInsertRows(*args, **kwargs):
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
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def indexInQuery(*args, **kwargs):
        ...
    @staticmethod
    def insertColumns(*args, **kwargs):
        ...
    @staticmethod
    def lastError(*args, **kwargs):
        ...
    @staticmethod
    def query(*args, **kwargs):
        ...
    @staticmethod
    def queryChange(*args, **kwargs):
        ...
    @staticmethod
    def record(*args, **kwargs):
        ...
    @staticmethod
    def removeColumns(*args, **kwargs):
        ...
    @staticmethod
    def roleNames(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def setHeaderData(*args, **kwargs):
        ...
    @staticmethod
    def setLastError(*args, **kwargs):
        ...
    @staticmethod
    def setQuery(*args, **kwargs):
        ...
class QSqlRecord(PyQt6.sip.simplewrapper):
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def append(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def clearValues(*args, **kwargs):
        ...
    @staticmethod
    def contains(*args, **kwargs):
        ...
    @staticmethod
    def count(*args, **kwargs):
        ...
    @staticmethod
    def field(*args, **kwargs):
        ...
    @staticmethod
    def fieldName(*args, **kwargs):
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
    def isGenerated(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def keyValues(*args, **kwargs):
        ...
    @staticmethod
    def remove(*args, **kwargs):
        ...
    @staticmethod
    def replace(*args, **kwargs):
        ...
    @staticmethod
    def setGenerated(*args, **kwargs):
        ...
    @staticmethod
    def setNull(*args, **kwargs):
        ...
    @staticmethod
    def setValue(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
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
class QSqlRelation(PyQt6.sip.simplewrapper):
    @staticmethod
    def displayColumn(*args, **kwargs):
        ...
    @staticmethod
    def indexColumn(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def swap(*args, **kwargs):
        ...
    @staticmethod
    def tableName(*args, **kwargs):
        ...
class QSqlRelationalDelegate(PyQt6.QtWidgets.QStyledItemDelegate):
    @staticmethod
    def createEditor(*args, **kwargs):
        ...
    @staticmethod
    def setEditorData(*args, **kwargs):
        ...
    @staticmethod
    def setModelData(*args, **kwargs):
        ...
class QSqlRelationalTableModel(QSqlTableModel):
    class JoinMode(enum.Enum):
        InnerJoin: typing.ClassVar[QSqlRelationalTableModel.JoinMode]  # value = <JoinMode.InnerJoin: 0>
        LeftJoin: typing.ClassVar[QSqlRelationalTableModel.JoinMode]  # value = <JoinMode.LeftJoin: 1>
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def insertRowIntoTable(*args, **kwargs):
        ...
    @staticmethod
    def orderByClause(*args, **kwargs):
        ...
    @staticmethod
    def relation(*args, **kwargs):
        ...
    @staticmethod
    def relationModel(*args, **kwargs):
        ...
    @staticmethod
    def removeColumns(*args, **kwargs):
        ...
    @staticmethod
    def revertRow(*args, **kwargs):
        ...
    @staticmethod
    def select(*args, **kwargs):
        ...
    @staticmethod
    def selectStatement(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setJoinMode(*args, **kwargs):
        ...
    @staticmethod
    def setRelation(*args, **kwargs):
        ...
    @staticmethod
    def setTable(*args, **kwargs):
        ...
    @staticmethod
    def updateRowInTable(*args, **kwargs):
        ...
class QSqlResult(PyQt6.sip.wrapper):
    class BindingSyntax(enum.Enum):
        NamedBinding: typing.ClassVar[QSqlResult.BindingSyntax]  # value = <BindingSyntax.NamedBinding: 1>
        PositionalBinding: typing.ClassVar[QSqlResult.BindingSyntax]  # value = <BindingSyntax.PositionalBinding: 0>
    @staticmethod
    def addBindValue(*args, **kwargs):
        ...
    @staticmethod
    def at(*args, **kwargs):
        ...
    @staticmethod
    def bindValue(*args, **kwargs):
        ...
    @staticmethod
    def bindValueType(*args, **kwargs):
        ...
    @staticmethod
    def bindingSyntax(*args, **kwargs):
        ...
    @staticmethod
    def boundValue(*args, **kwargs):
        ...
    @staticmethod
    def boundValueCount(*args, **kwargs):
        ...
    @staticmethod
    def boundValueName(*args, **kwargs):
        ...
    @staticmethod
    def boundValueNames(*args, **kwargs):
        ...
    @staticmethod
    def boundValues(*args, **kwargs):
        ...
    @staticmethod
    def clear(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def driver(*args, **kwargs):
        ...
    @staticmethod
    def exec(*args, **kwargs):
        ...
    @staticmethod
    def executedQuery(*args, **kwargs):
        ...
    @staticmethod
    def fetch(*args, **kwargs):
        ...
    @staticmethod
    def fetchFirst(*args, **kwargs):
        ...
    @staticmethod
    def fetchLast(*args, **kwargs):
        ...
    @staticmethod
    def fetchNext(*args, **kwargs):
        ...
    @staticmethod
    def fetchPrevious(*args, **kwargs):
        ...
    @staticmethod
    def handle(*args, **kwargs):
        ...
    @staticmethod
    def hasOutValues(*args, **kwargs):
        ...
    @staticmethod
    def isActive(*args, **kwargs):
        ...
    @staticmethod
    def isForwardOnly(*args, **kwargs):
        ...
    @staticmethod
    def isNull(*args, **kwargs):
        ...
    @staticmethod
    def isPositionalBindingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def isSelect(*args, **kwargs):
        ...
    @staticmethod
    def isValid(*args, **kwargs):
        ...
    @staticmethod
    def lastError(*args, **kwargs):
        ...
    @staticmethod
    def lastInsertId(*args, **kwargs):
        ...
    @staticmethod
    def lastQuery(*args, **kwargs):
        ...
    @staticmethod
    def numRowsAffected(*args, **kwargs):
        ...
    @staticmethod
    def prepare(*args, **kwargs):
        ...
    @staticmethod
    def record(*args, **kwargs):
        ...
    @staticmethod
    def reset(*args, **kwargs):
        ...
    @staticmethod
    def savePrepare(*args, **kwargs):
        ...
    @staticmethod
    def setActive(*args, **kwargs):
        ...
    @staticmethod
    def setAt(*args, **kwargs):
        ...
    @staticmethod
    def setForwardOnly(*args, **kwargs):
        ...
    @staticmethod
    def setLastError(*args, **kwargs):
        ...
    @staticmethod
    def setPositionalBindingEnabled(*args, **kwargs):
        ...
    @staticmethod
    def setQuery(*args, **kwargs):
        ...
    @staticmethod
    def setSelect(*args, **kwargs):
        ...
    @staticmethod
    def size(*args, **kwargs):
        ...
class QSqlTableModel(QSqlQueryModel):
    class EditStrategy(enum.Enum):
        OnFieldChange: typing.ClassVar[QSqlTableModel.EditStrategy]  # value = <EditStrategy.OnFieldChange: 0>
        OnManualSubmit: typing.ClassVar[QSqlTableModel.EditStrategy]  # value = <EditStrategy.OnManualSubmit: 2>
        OnRowChange: typing.ClassVar[QSqlTableModel.EditStrategy]  # value = <EditStrategy.OnRowChange: 1>
    @staticmethod
    def beforeDelete(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def beforeInsert(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def beforeUpdate(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
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
    def clearItemData(*args, **kwargs):
        ...
    @staticmethod
    def data(*args, **kwargs):
        ...
    @staticmethod
    def database(*args, **kwargs):
        ...
    @staticmethod
    def deleteRowFromTable(*args, **kwargs):
        ...
    @staticmethod
    def editStrategy(*args, **kwargs):
        ...
    @staticmethod
    def fieldIndex(*args, **kwargs):
        ...
    @staticmethod
    def filter(*args, **kwargs):
        ...
    @staticmethod
    def flags(*args, **kwargs):
        ...
    @staticmethod
    def headerData(*args, **kwargs):
        ...
    @staticmethod
    def indexInQuery(*args, **kwargs):
        ...
    @staticmethod
    def insertRecord(*args, **kwargs):
        ...
    @staticmethod
    def insertRowIntoTable(*args, **kwargs):
        ...
    @staticmethod
    def insertRows(*args, **kwargs):
        ...
    @staticmethod
    def isDirty(*args, **kwargs):
        ...
    @staticmethod
    def orderByClause(*args, **kwargs):
        ...
    @staticmethod
    def primaryKey(*args, **kwargs):
        ...
    @staticmethod
    def primaryValues(*args, **kwargs):
        ...
    @staticmethod
    def primeInsert(*args, **kwargs):
        """
        pyqtSignal(*types, name: str = ..., revision: int = ..., arguments: Sequence = ...) -> PYQT_SIGNAL
        
        types is normally a sequence of individual types.  Each type is either a
        type object or a string that is the name of a C++ type.  Alternatively
        each type could itself be a sequence of types each describing a different
        overloaded signal.
        name is the optional C++ name of the signal.  If it is not specified then
        the name of the class attribute that is bound to the signal is used.
        revision is the optional revision of the signal that is exported to QML.
        If it is not specified then 0 is used.
        arguments is the optional sequence of the names of the signal's arguments.
        """
    @staticmethod
    def record(*args, **kwargs):
        ...
    @staticmethod
    def removeColumns(*args, **kwargs):
        ...
    @staticmethod
    def removeRows(*args, **kwargs):
        ...
    @staticmethod
    def revert(*args, **kwargs):
        ...
    @staticmethod
    def revertAll(*args, **kwargs):
        ...
    @staticmethod
    def revertRow(*args, **kwargs):
        ...
    @staticmethod
    def rowCount(*args, **kwargs):
        ...
    @staticmethod
    def select(*args, **kwargs):
        ...
    @staticmethod
    def selectRow(*args, **kwargs):
        ...
    @staticmethod
    def selectStatement(*args, **kwargs):
        ...
    @staticmethod
    def setData(*args, **kwargs):
        ...
    @staticmethod
    def setEditStrategy(*args, **kwargs):
        ...
    @staticmethod
    def setFilter(*args, **kwargs):
        ...
    @staticmethod
    def setPrimaryKey(*args, **kwargs):
        ...
    @staticmethod
    def setRecord(*args, **kwargs):
        ...
    @staticmethod
    def setSort(*args, **kwargs):
        ...
    @staticmethod
    def setTable(*args, **kwargs):
        ...
    @staticmethod
    def sort(*args, **kwargs):
        ...
    @staticmethod
    def submit(*args, **kwargs):
        ...
    @staticmethod
    def submitAll(*args, **kwargs):
        ...
    @staticmethod
    def tableName(*args, **kwargs):
        ...
    @staticmethod
    def updateRowInTable(*args, **kwargs):
        ...
