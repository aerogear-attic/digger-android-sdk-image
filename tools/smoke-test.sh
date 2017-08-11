#!/bin/bash

which androidctl
which androidctl-sync

androidctl sdk install

which $ANDROID_HOME/tools/bin/sdkmanager

if [[ -x "$ANDROID_HOME/tools/bin/sdkmanager" ]]; then
  echo "sdkmanager cli validated."
else
  echo "sdkmanager does not have execution permissions."
  exit 1;
fi

androidctl-sync -y /opt/tools/sample.cfg

if [[ -d "$ANDROID_HOME/platforms" ]]; then
  echo "Android platforms folder validated."
else
  echo "Could not find $ANDROID_HOME/platforms folder."
  exit 1;
fi

if [[ -z "$(ls -A $ANDROID_HOME/platforms)" ]]; then
   echo "$ANDROID_HOME/platforms folder is empty"
   exit 1;
else
   echo "$ANDROID_HOME/platforms validated."
fi
