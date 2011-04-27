#!/usr/bin/env python
# -*- coding: utf8 -*-
#~#######################################################################
#~ Copyright (c) 2008 Burdakov Daniel <kreved@kreved.org>               #
#~                                                                      #
#~ This file is part of FreQ-bot.                                       #
#~                                                                      #
#~ FreQ-bot is free software: you can redistribute it and/or modify     #
#~ it under the terms of the GNU General Public License as published by #
#~ the Free Software Foundation, either version 3 of the License, or    #
#~ (at your option) any later version.                                  #
#~                                                                      #
#~ FreQ-bot is distributed in the hope that it will be useful,          #
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of       #
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
#~ GNU General Public License for more details.                         #
#~                                                                      #
#~ You should have received a copy of the GNU General Public License    #
#~ along with FreQ-bot.  If not, see <http://www.gnu.org/licenses/>.    #
#~#######################################################################

import sys

tw='You need have it installed to use freQ-bot\n=== Visit http://twistedmatrix.com/ to get info about Twisted...\n'

try: import twisted
except:
 sys.stdout.write('=== py-twistedCore not found...\n=== '+tw+'\n')
 sys.exit(1)

try: import twisted.words.protocols.jabber
except:
 sys.stdout.write('=== py-twistedWords not found...\n=== '+tw+'\n')
 sys.exit(1)
 
try: import twisted.web
except:
 sys.stdout.write('=== py-twistedWeb not found...\n=== '+tw+'\n')
 sys.exit(1)

try: from sqlite3 import connect
except:
 sys.stdout.write('=== Warning: cannot "from sqlite3 import connect"\nSome features will not work.\n')
