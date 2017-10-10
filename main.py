#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from check_place import run
from configparser import ConfigParser

config = ConfigParser()
config.read("old_place.config")
first_run = config['firstrun']['firstrun']

if first_run == 1:
    run()
else:
    print("please update the config file")