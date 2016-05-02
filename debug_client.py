"""
 * FirebirdRemoteDebug - Simple remote debugging to Firebird
 * Copyright (C) 2015 Jeferson Boes
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 02111-1307, USA.
"""
 
import socket
import sys

host, port = 'localhost', 6098

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

log = ""
i = 1

if len(sys.argv) > 1:
    while i < len(sys.argv):
        log = log + sys.argv[i] + " "
        i = i + 1

client.send(log.encode())
client.close()
