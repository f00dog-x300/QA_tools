#Requires -RunAsAdministrator

# installing notepad++, git, vscode, postman, node, slack, and scrcpy
$Packages = @('notepadplusplus', 'git', 'vscode', 'postman', 'python', 'nodejs', 'slack', 'scrcpy', 'docker-compose', 'docker-desktop', 'docker-cli')
$ChocoInstalled = $false

# Does a check to see if chocolatey is installed. If not, then will install it
if (Get-Command choco.exe -ErrorAction SilentlyContinue) {
    $ChocoInstalled = $true
    Write-Host('Chocolatey is already installed.')
}
else {
    Write-Host('Chocolatey is not installed. Installing')
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}

# Installs the software under the $Packages array
ForEach ($PackageName in $Packages) {
    choco install $PackageName -y --verbose
}
