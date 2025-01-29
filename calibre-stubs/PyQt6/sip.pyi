from __future__ import annotations
import typing
__all__ = ['SIP_VERSION', 'SIP_VERSION_STR', 'array', 'assign', 'cast', 'delete', 'dump', 'enableautoconversion', 'isdeleted', 'ispycreated', 'ispyowned', 'setdeleted', 'settracemask', 'simplewrapper', 'transferback', 'transferto', 'unwrapinstance', 'voidptr', 'wrapinstance', 'wrapper', 'wrappertype']
class array:
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __len__(self):
        """
        Return len(self).
        """
    def __repr__(self):
        """
        Return repr(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class simplewrapper:
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
class voidptr:
    @staticmethod
    def __new__(type, *args, **kwargs):
        """
        Create and return a new object.  See help(type) for accurate signature.
        """
    @staticmethod
    def asarray(*args, **kwargs):
        ...
    @staticmethod
    def ascapsule(*args, **kwargs):
        ...
    @staticmethod
    def asstring(*args, **kwargs):
        ...
    @staticmethod
    def getsize(*args, **kwargs):
        ...
    @staticmethod
    def getwriteable(*args, **kwargs):
        ...
    @staticmethod
    def setsize(*args, **kwargs):
        ...
    @staticmethod
    def setwriteable(*args, **kwargs):
        ...
    def __bool__(self):
        """
        True if self else False
        """
    def __delitem__(self, key):
        """
        Delete self[key].
        """
    def __getitem__(self, key):
        """
        Return self[key].
        """
    def __int__(self):
        """
        int(self)
        """
    def __len__(self):
        """
        Return len(self).
        """
    def __setitem__(self, key, value):
        """
        Set self[key] to value.
        """
class wrapper(simplewrapper):
    pass
class wrappertype(type):
    def __delattr__(self, name):
        """
        Implement delattr(self, name).
        """
    def __getattribute__(self, name):
        """
        Return getattr(self, name).
        """
    def __setattr__(self, name, value):
        """
        Implement setattr(self, name, value).
        """
def _unpickle_type(*args, **kwargs):
    ...
def assign(*args, **kwargs):
    ...
def cast(*args, **kwargs):
    ...
def delete(*args, **kwargs):
    ...
def dump(*args, **kwargs):
    ...
def enableautoconversion(*args, **kwargs):
    ...
def isdeleted(*args, **kwargs):
    ...
def ispycreated(*args, **kwargs):
    ...
def ispyowned(*args, **kwargs):
    ...
def setdeleted(*args, **kwargs):
    ...
def settracemask(*args, **kwargs):
    ...
def transferback(*args, **kwargs):
    ...
def transferto(*args, **kwargs):
    ...
def unwrapinstance(*args, **kwargs):
    ...
def wrapinstance(*args, **kwargs):
    ...
SIP_VERSION: int = 395270
SIP_VERSION_STR: str = '6.8.6'
_C_API: typing.Any  # value = <capsule object "PyQt6.sip._C_API" at 0x7f34ec1c2c40>
