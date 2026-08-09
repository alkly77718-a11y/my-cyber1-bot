[app]
title = BlackArmy
package.name = blackarmy
package.domain = org.zero
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_CONTACTS,READ_SMS,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_CALL_LOG,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,RECEIVE_BOOT_COMPLETED
android.api = 30
android.ndk = 23b
android.sdk = 30
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
