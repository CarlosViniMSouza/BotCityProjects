$exclude = @("venv", "api_metropolitana_ifam.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "api_metropolitana_ifam.zip" -Force