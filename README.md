# AeroGear Android SDK installer Docker image

[![Build Status](https://travis-ci.org/aerogear/digger-android-sdk-image.png)](https://travis-ci.org/aerogear/digger-android-sdk-image)
[![License](https://img.shields.io/:license-Apache2-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

## Projcect Info

|                 | Project Info  |
| --------------- | ------------- |
| License:        | Apache License, Version 2.0  |
| Build:          | Docker  |
| Issue tracker:  | https://issues.jboss.org/browse/AGDIGGER  |
| Mailing lists:  | [aerogear-users](http://aerogear-users.1116366.n5.nabble.com/) ([subscribe](https://lists.jboss.org/mailman/listinfo/aerogear-users))  |
|                 | [aerogear-dev](http://aerogear-dev.1069024.n5.nabble.com/) ([subscribe](https://lists.jboss.org/mailman/listinfo/aerogear-dev))  |
| IRC:            | [#aerogear](https://webchat.freenode.net/?channels=aerogear) channel in the [freenode](http://freenode.net/) network.  |



This is an image that is preconfigured to download Android SDK. Android SDK cannot be included in the container directly because of the license issues.
                                   
Thus, this image uses [digger androidctl](https://github.com/aerogear/androidctl) utility script which installs the Android sdk and its related packages that prompts you to accept the license. 
However, keep in mind that it does not automate the "accept license" step (you need to manually accept the android/google license/terms and conditions).

The Android SDK in the container will be reused by the Android slave containers.

## Usage

* Start the Docker container
* Run

```bash
docker exec -d <container_name> androidctl sdk install
docker exec -d <container_name> androidctl sync /opt/tools/sample.cfg
```
