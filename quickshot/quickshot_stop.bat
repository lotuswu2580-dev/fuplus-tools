@echo off
powershell -NoProfile -Command "Get-CimInstance Win32_Process -Filter \"Name='pythonw.exe'\" | Where-Object { $_.CommandLine -like '*quickshot*' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force; Write-Output ('stopped PID ' + $_.ProcessId) }"
pause
