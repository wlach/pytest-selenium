# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import os
import pytest

HOST = os.environ.get('SELENIUM_HOST', 'localhost')
PORT = os.environ.get('SELENIUM_PORT', 4444)


def driver_kwargs(capabilities, firefox_profile, host, port, **kwargs):
    if 'browserName' not in capabilities:
        # remote instances must at least specify a browserName capability
        raise pytest.UsageError('The \'browserName\' capability must be '
                                'specified when using the remote driver.')
    capabilities.setdefault('version', '')  # default to any version
    capabilities.setdefault('platform', 'ANY')  # default to any platform

    executor = 'http://{0}:{1}/wd/hub'.format(host, port)

    kwargs = {
        'command_executor': executor,
        'desired_capabilities': capabilities,
        'browser_profile': firefox_profile}
    return kwargs
