$exclude = @("venv", "bot_web_pdf.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_web_pdf.zip" -Force