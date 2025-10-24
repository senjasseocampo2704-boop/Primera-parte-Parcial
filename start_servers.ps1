# Script para ejecutar ambos servidores FastAPI simultáneamente
# ABB en puerto 8000 y AVL en puerto 8001

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Iniciando Servidores FastAPI" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Iniciar servidor ABB en puerto 8000
Write-Host "[ABB] Iniciando servidor en puerto 8000..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot'; uvicorn main_abb:app --reload --port 8000"

# Esperar 2 segundos
Start-Sleep -Seconds 2

# Iniciar servidor AVL en puerto 8001
Write-Host "[AVL] Iniciando servidor en puerto 8001..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PSScriptRoot'; uvicorn main_avl:app --reload --port 8001"

# Esperar 3 segundos para que los servidores inicien
Start-Sleep -Seconds 3

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Servidores Iniciados" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "ABB Server:" -ForegroundColor Green
Write-Host "  - URL: http://127.0.0.1:8000" -ForegroundColor White
Write-Host "  - Swagger: http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host "  - ReDoc: http://127.0.0.1:8000/redoc" -ForegroundColor White
Write-Host ""
Write-Host "AVL Server:" -ForegroundColor Yellow
Write-Host "  - URL: http://127.0.0.1:8001" -ForegroundColor White
Write-Host "  - Swagger: http://127.0.0.1:8001/docs" -ForegroundColor White
Write-Host "  - ReDoc: http://127.0.0.1:8001/redoc" -ForegroundColor White
Write-Host ""
Write-Host "Presiona cualquier tecla para abrir Swagger UI en el navegador..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Abrir Swagger UI en el navegador
Start-Process "http://127.0.0.1:8000/docs"
Start-Process "http://127.0.0.1:8001/docs"

Write-Host ""
Write-Host "Swagger UI abierto en el navegador!" -ForegroundColor Green
Write-Host "Para detener los servidores, cierra las ventanas de PowerShell." -ForegroundColor Red
