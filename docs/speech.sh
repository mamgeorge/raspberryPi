#!/bin/bash
link="http://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=en&q=$*"
#say() { local IFS=+;/usr/bin/mplayer -ao alsa -really-quiet -noconsolecontrol link; }
say() { local IFS=+;/usr/bin/mplayer -ao pulse $link; }
say $*