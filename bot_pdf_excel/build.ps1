$exclude = @("venv", "bot_pdf_excel.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_pdf_excel.zip" -Force