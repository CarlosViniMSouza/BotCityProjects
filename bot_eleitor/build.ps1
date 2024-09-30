$exclude = @("venv", "bot_aval_lg.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_aval_lg.zip" -Force