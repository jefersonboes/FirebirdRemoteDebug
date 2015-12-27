# FirebirdRemoteDebug
 Simple remote debugging to Firebird

#### **How to install**
 - Copy the "RemoteDebug.dll" to the Firebird installation of the UDF folder
 - Run the script "RemoteDebug_UDF.sql" in Firebird to install the UDF
 - Run the "debug_server.py" to start debug server

#### **Example**
 To run the log UDF see example:
 ```sql
 select log_msg('this is a example') from rdb$database;
 ```
