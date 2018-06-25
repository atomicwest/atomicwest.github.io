--EXECUTE sp_configure;
--enable xp_cmdshell command
EXEC sp_configure 'show advanced options', 1;
GO
RECONFIGURE;
GO

EXEC sp_configure 'xp_cmdshell', 1;
GO
RECONFIGURE;
GO

EXEC xp_cmdshell 'whoami' 
--add file permissions for mssql$sqlexpressvf manually via the pyscript file

select * from glazes2
exec xp_cmdshell 'C:\Python36\python.exe C:\path\to\file.py'
--doesnt even work if there is an existing destination file that has user permissions manually created



