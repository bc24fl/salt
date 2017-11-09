# -*- coding: utf-8 -*-

# Import Python libs
from __future__ import absolute_import

# Import Salt Testing Libs
from tests.support.case import SSHCase
from tests.support.unit import skipIf

# Import Salt Libs
import salt.utils


@skipIf(salt.utils.is_windows(), 'salt-ssh not available on Windows')
class SSHGrainsTest(SSHCase):
    '''
    testing salt-ssh with raw calls
    '''
    def test_ssh_raw(self):
        '''
        test salt-ssh with -r argument
        '''
        msg = 'running raw msg'
        ret = self.run_function('echo {0}'.format(msg), raw=True)
        self.assertEqual(ret['stdout'], msg + '\n')
