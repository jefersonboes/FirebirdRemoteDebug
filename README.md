# FirebirdRemoteDebug
 Simple remote debugging to Firebird

#### **How to install**
 - Copy the "RemoteDebug.dll" to the Firebird installation of the UDF folder
 - Run the script "RemoteDebug_UDF.sql" in Firebird to install the UDF
 - Restart Firebird
 - Run the "debug_server.py" to start debug server

#### **Example**
 To run the log UDF see example:
 ```sql
 select log_msg('this is a example') from rdb$database;
 ```
 
 Pascal example:
 ```pascal
uses
  ShellAPI;

procedure log_msg(msg: String);
begin
  ShellExecute(0, 'open', PChar('debug_client.py'), Pchar(msg), nil, SW_HIDE);
end;
 ```
 
