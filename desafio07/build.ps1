$exclude = @("venv", "desafio05.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "desafio05.zip" -Force