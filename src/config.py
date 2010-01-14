#!/usr/bin/env python
# coding=UTF-8

version = "3.1.0beta2.1" # Don't forget to update upgrade.js too!
in_development = False
publish_babelzilla = False # True = include incomplete locales for babelzilla
only_english = False # True = only include english for beta releases


app = 'updatescan'
name = 'Update Scanner'
description = 'Monitors webpages for updates'
author = 'Pete Burgers'
contributors = ['Karol Misiura (Tango Desktop Project Icons)']
translators = ['PetrTwo (Čeština)',
               'Jørgen (Dansk)',
               '123tp (Dansk)',
               'Archaeopteryx (Deutsch)'
               'Team erweiterungen.de (Deutsch)',
               'Proyecto Nave (Español)',
               'Chuzo (Español)',
               'Olli (Suomeksi)',
               'myahoo (Français)',
               'JZsolt (Magyar)',
               'Almotasim (Italiano)',
               'Jeong Seungwon (한국어)',
               'Funalien (lietuvių kalba)',
               'Lauriote (lietuvių kalba)',
               'Mark Heijl (Nederlands)',
               'Leszek(teo) Życzkowski (Polski)',
               'Raryel Costa Souza (português brasileiro)',
               'Edgard Magalhaes (português brasileiro)',
               'Funalien (Русский)',
               'Slovak Team (Slovenčina)',
               'Kenan Balamir (Türkçe)',
               'Wang King (简化字 - zh-CN)',
               'Peter Pin-Guang Chen (簡化字 - zh-TW)',
#               'stoyan (български език)',
               ]
authorURL = "http://updatescanner.mozdev.org"
uid = 'c07d1a49-9894-49ff-a594-38960ede8fb9'
optionsChrome = 'chrome://updatescan/content/preferences.xul'

if in_development:
    version = version + "+"

homepageURL = "http://updatescanner.mozdev.org"

allowUpdate = False
updateURL = "%(homepageURL)s/update.rdf" % vars()
updateFile = "%(app)s-%(version)s.xpi" % vars()
updateLink = "%(homepageURL)s/%(updateFile)s" % vars()
iconPath = "skin/updatescan_big.png"

firefoxUID = 'ec8030f7-c20a-464f-9b0e-13a3a9e97384'
firefoxMinVersion = '3.0'
firefoxMaxVersion = '3.6.*'

overlays = (
    # overlay this on that
    ('%(app)s/content/browser.xul' % vars(), 'browser/content/browser.xul' % vars()),
)
stylesheets = (
    # overlay this on that
    ('%(app)s/skin/updatescanoverlay.css' % vars(), 'global/content/customizeToolbar.xul' % vars()),
)

skins = {
    'classic': {
        'skin_version': '1.0',
        'display_name': name,
    },
}

locales = {
    'cs-CZ': {
        'locale_version': '1.0',
        'display_name': name,
    },                      
    'da-DK': {
        'locale_version': '1.0',
        'display_name': name,
    },           
    'de-DE': {
        'locale_version': '1.0',
        'display_name': name,
    },           
    'en-US': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'es-ES': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'fi-FI': {
        'locale_version': '1.0',
        'display_name': name,
    },           
    'fr': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'hu-HU': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'it-IT': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'ko-KR': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'lt-LT': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'nl-NL': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'pl-PL': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'pt-BR': {
        'locale_version': '1.0',
        'display_name': name,
    },    
    'ru-RU': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'sk-SK': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'tr-TR': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'zh-CN': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'zh-TW': {
        'locale_version': '1.0',
        'display_name': name,
    },
}

incomplete_locales = {
    'bg-BG': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'ja-JP': {
        'locale_version': '1.0',
        'display_name': name,
    },
    'ms-MY': {
        'locale_version': '1.0',
        'display_name': name,
    },
}

# Only include incomplete locales if we're building for babelzilla
if publish_babelzilla:
    print "*** Babelzilla version - includes incomplete locales ***"
    locales.update(incomplete_locales)

if only_english:
    print "*** English-only version - only use for betas! ***"
    locales = {
        'en-US': {'locale_version': '1.0','display_name': name}
        }
