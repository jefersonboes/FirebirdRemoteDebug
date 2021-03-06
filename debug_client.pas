{
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
}

unit debug_client;

interface

procedure log_msg(msg: String);

implementation

uses
  ShellAPI, Windows;
  
procedure log_msg(msg: String);
begin
  ShellExecute(0, 'open', PChar('debug_client.py'), Pchar(msg), nil, SW_HIDE);
end;

end.
