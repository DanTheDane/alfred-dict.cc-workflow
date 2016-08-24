#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow
from dictcc import Dict, AVAILABLE_LANGUAGES


def main(wf):

    args = wf.args

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))