#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

STRFLEMISH = 'Flemish'

INDSPANISH = inquisition.SPANISH.index('Spanish')

FLEMISH = inquisition.SPANISH[:INDSPANISH] + STRFLEMISH\
          + inquisition.SPANISH[INDSPANISH+len('Spanish'):]
