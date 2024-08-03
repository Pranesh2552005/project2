[app]
title = YourAppTitle
package.name = your.app.package.name
package.domain = com.yourdomain
source.dir = .
source.include_exts = py,kv,atlas,png,jpg,jpeg
version = 1.0
requirements = kivy,plyer

[buildozer]
use_pymodules = whitelist
whitelist = kivy,plyer
android.api = 29
android.ndk = 21.4.7075529
android.arch = armeabi-v7a
android.permissions = INTERNET,ACCESS_FINE_LOCATION
