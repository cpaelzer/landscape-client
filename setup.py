#!/usr/bin/python

from distutils.core import setup, Extension

from landscape import UPSTREAM_VERSION

from DistUtilsExtra.command import build_i18n


setup(name="Landscape Client",
      version=UPSTREAM_VERSION,
      description="Landscape Client",
      author="Landscape Team",
      author_email="landscape-team@canonical.com",
      url="http://landscape.canonical.com",
      packages=["landscape",
                "landscape.broker",
                "landscape.manager",
                "landscape.monitor",
                "landscape.package",
                "landscape.sysinfo",
                "landscape.upgraders",
                "landscape.user",
                "landscape.lib",
                "landscape.ui",
                "landscape.ui.lib",
                "landscape.ui.model",
                "landscape.ui.model.configuration",
                "landscape.ui.model.registration",
                "landscape.ui.controller",
                "landscape.ui.view"],
      package_data={"landscape.ui.view": [
          "ui/landscape-client-settings.glade"]},
      data_files=[
          ("/usr/share/dbus-1/system-services/",
           ["dbus-1/com.canonical.LandscapeClientSettings.service",
          "dbus-1/com.canonical.LandscapeClientRegistration.service"]),
          ("/usr/share/polkit-1/actions",
           ["polkit-1/com.canonical.LandscapeClientSettings.policy"]),
          ("/etc/dbus-1/system.d/",
           ["dbus-1/com.canonical.LandscapeClientSettings.conf",
            "dbus-1/com.canonical.LandscapeClientRegistration.conf"]),
          ("/usr/share/applications/",
           ["applications/landscape-client-settings.desktop"]),
          ("/usr/share/icons/hicolor/scalable/apps/",
           ["icons/preferences-management-service.svg"]),
          ("/usr/share/glib-2.0/schemas/",
           ["glib-2.0/schemas/com.canonical.landscape-client-settings.gschema.xml"])],
      scripts=["scripts/landscape-client",
               "scripts/landscape-config",
               "scripts/landscape-message",
               "scripts/landscape-broker",
               "scripts/landscape-manager",
               "scripts/landscape-monitor",
               "scripts/landscape-package-changer",
               "scripts/landscape-package-reporter",
               "scripts/landscape-release-upgrader",
               "scripts/landscape-sysinfo",
               "scripts/landscape-is-cloud-managed",
               "scripts/landscape-dbus-proxy",
               "scripts/landscape-client-settings-mechanism",
               "scripts/landscape-client-registration-mechanism",
               "scripts/landscape-client-settings-ui",
               "scripts/landscape-client-ui-install"],
      ext_modules=[Extension("landscape.lib.initgroups",
                             ["landscape/lib/initgroups.c"])],
      cmdclass={"build_i18n":  build_i18n.build_i18n})
