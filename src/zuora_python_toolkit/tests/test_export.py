#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import unittest
import logging
from mock import Mock, patch

from zuora_python_toolkit.export import ZuoraExport
from zuora_python_toolkit.tests.test_base import ZuoraBaseTestCase

logger = logging.getLogger("zuora_python_toolkit")
suds_logger = logging.getLogger("suds.client")


class ZuoraExportTestCase(ZuoraBaseTestCase):

    def setUp(self):
        wsdl = 'apisandbox.zuora.a.63.0.wsdl'
        username = 'api@c.co'
        password = 'Asdf1234!'

        kwargs = {
            "wsdl": wsdl,
            "username": username,
            "password": password,
            "session_length_millis": self.session_length_millis,
        }
        self.client = ZuoraExport(**kwargs)

    def test_export__account(self):
        fields = ['Id', 'AccountNumber', 'UpdatedById', 'UpdatedDate']

        results = self.client.export('account', fields)
        print results
            
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.getLogger(__package__)
    logging.getLogger('suds.client').setLevel(logging.CRITICAL)
    unittest.main()