# AeroGear Android SDK installer Docker image

This is an image that is preconfigured to download Android SDK. Android SDK cannot be included in the container directly because of the license issues.
                                   
Thus, this image contains a "androidctl" script which installs the Android sdk and its related packages that prompts you to accept the license. 
However, keep in mind that it does not automate the "accept license" step (you need to manually accept the android/google license/terms and conditions).

The Android SDK in the container will be reused by the Android slave containers.

## Usage

* Start the Docker container
* Run

```bash
docker exec -d <container_name> androidctl sdk install
docker exec -d <container_name> androidctl sync /opt/tools/sample.cfg
```
