import errno
import os
import sys
import json


def errmsg(code):
  return os.strerror(code)


class BaseError(Exception):
  def __init__(self, message=None):
    self.code = errno.EPERM
    self.message = message

  def __repr__(self):
    return '%s(%s)' % (self.__class__, self.__dict__)

  def __str__(self):
    return '[%s] %s' % (self.code, self.message)

  def as_dict(self):
    return {'code': self.code, 'message': self.message}

  def as_json(self):
    return json.dumps(self.as_dict())


class RuntimeError(BaseError):
  def __init__(self, code, message):
    super(RuntimeError, self).__init__(self)
    self.code = code
    self.message = message


class ConnectionError(BaseError):
  def __init__(self, message):
    super(ConnectionError, self).__init__(self)
    self.code = err.ECONNREFUSED
    self.message = '%s: %s' % (errmsg(self.code), message)
