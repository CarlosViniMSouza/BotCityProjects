$exclude = @("venv", "botPythonBoth.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "botPythonBoth.zip" -Force