Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "token_refresh.sh" & Chr(34), 0
Set WshShell = Nothing