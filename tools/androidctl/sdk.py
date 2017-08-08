import os
import functools
import subprocess
import sys
import zipfile
import shutil
from urlparse import urlparse

import requests

import props
import errors


sdk_path = os.environ.get('ANDROID_HOME', props.sdk.path)
sdk_url = props.sdk.url
sdk_shell = props.sdk.shell
https_proxy = os.environ.get('HTTPS_PROXY')
if not https_proxy:
  https_proxy = os.environ.get('HTTP_PROXY')


def manager(*args):
  cmd = '%s/tools/bin/sdkmanager' % sdk_path
  cmd_args = [
    sdk_shell,
    cmd
  ]
  proxy_settings = get_proxy_settings(https_proxy)
  if proxy_settings:
    proxy_flags = ['--proxy=http', '--proxy_host=%s' % proxy_settings[0]]
    if proxy_settings[1]:
      proxy_flags.append('--proxy_port=%s' % proxy_settings[1])
    cmd_args.extend(proxy_flags)
  cmd_args.extend(args)
  print 'Running android sdkmanager, this might take a while.'
  code = subprocess.call(cmd_args, stdout=sys.stdout, stderr=sys.stderr)
  if code != 0:
    raise errors.RuntimeError(code, 'SDKManager exited abruptly.')


def download(url=sdk_url, path=sdk_path):
  if not os.path.exists(path):
    print 'Path %s does not exist, creating it...' % path
    try:
      os.mkdir(path)
    except OSError as err:
      raise errors.RuntimeError(err.errno, str(err))
  if os.path.exists('%s/android-sdk-linux.zip' % path):
    print 'Android SDK already downloaded'
    return
  print 'Downloading Android SDK from %s' % url
  try:
    res = requests.get(url, stream=True)
  except requests.exceptions.RequestException as err:
    raise errors.ConnectionError(err.message)
  try:
    with open('%s/android-sdk-linux.zip' % path, 'wb') as f:
      for chunk in res.iter_content(chunk_size=1024):
        if chunk:
          f.write(chunk)
  except IOError as err:
    raise errors.RuntimeError(err.errno, str(err))
  print 'Android SDK downloaded'


def unpack(path=sdk_path):
  print 'Unpacking Android SDK file...'
  try:
    with zipfile.ZipFile('%s/android-sdk-linux.zip' % path, 'r') as zf:
      for info in zf.infolist():
        zf.extract(info.filename, path=path)
        dest = os.path.join(path, info.filename)
        perm = info.external_attr >> 16L
        os.chmod(dest, perm)
  except IOError as err:
    raise errors.RuntimeError(err.errno, str(err))
  print 'Android SDK available at %s' % path


def install(url=sdk_url, path=sdk_path):
  download(url, path)
  unpack(path)


def uninstall(path=sdk_path):
  print 'Uninstalling Android SDK at %s' % path
  try:
    shutil.rmtree(path)
  except OSError as err:
    raise errors.RuntimeError(err.errno, str(err))
  print 'Android SDK deleted from %s' % path


def get_proxy_settings(proxy=https_proxy):
  proxy_settings = None
  if proxy:
    if not '://' in proxy:
      proxy = 'http://%s' %  proxy
    parts = urlparse(proxy)
    proxy_host = parts.hostname
    if parts.port:
      proxy_port = parts.port
    proxy_settings = (proxy_host, proxy_port)
  return proxy_settings
