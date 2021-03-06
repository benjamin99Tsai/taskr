#
# Copyright 2014-2015 sodastsai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import unicode_literals, division, absolute_import, print_function
import os
import sys


def setup_django(settings=None, project_path=None):
    # Update Python path
    sys.path = [project_path or os.getcwd()] + sys.path
    # Setup django module
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)
    # Setup django
    # noinspection PyPackageRequirements
    import django
    # noinspection PyUnresolvedReferences
    django.setup()
