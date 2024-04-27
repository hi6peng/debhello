#!/usr/bin/python3
"""
debhello command line entry (enable python -m debhello syntax)
"""

import sys
import debhello


def main():  # needed for console script
    print(' ========== Hello Python3 ==========')
    print('argv = {}'.format(sys.argv))
    print('version = {}'.format(debhello.__version__))
    return

if __name__ == "__main__":
    sys.exit(main())
