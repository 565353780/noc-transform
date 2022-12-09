#!/usr/bin/env python
# -*- coding: utf-8 -*-

from noc_transform.Data.obb import OBB
from noc_transform.Method.noc import getNOCOBB
from noc_transform.Method.transform import getNOCTransform


class TransformGenerator(object):

    def __init__(self):
        return

    def getNOCOBB(self, obb):
        return getNOCOBB(obb)

    def getNOCTransform(self, obb):
        return getNOCTransform(obb)
