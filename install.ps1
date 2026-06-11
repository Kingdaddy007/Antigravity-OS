# Anti-Gravity OS — Windows Installer
# Run: .\install.ps1

param(
    [string]$GlobalConfig = $null,
    [string]$IDE = $null
)

# ─── Colors ──────────────────────────────────────────────────────────────────
function Write-Step($msg)    { Write-Host "`n▶ $msg" -ForegroundColor Cyan }
function Write-Success($msg) { Write-Host "  ✓ $msg" -ForegroundColor Green }
function Write-Warn($msg)    { Write-Host "  ⚠ $msg" -ForegroundColor Yellow }
function Write-Question($msg){ Write-Host "`n$msg" -ForegroundColor White }
function Write-Header()      {
    Write-Host "`n" -NoNewline
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkCyan
    Write-Host "   Anti-Gravity OS — Installer v1.2"          -ForegroundColor Cyan
    Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkCyan
}

Write-Header

$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$GlobalSource    = Join-Path $ScriptRoot "global"

# ─── Step 1: Global config target ─────────────────────────────────────────────
if (-not $GlobalConfig) {
    if (-not $IDE) {
        Write-Question @"
Which IDE are you using?

  [1] Google AI Studio / Gemini   → ~/.gemini/antigravity/
  [2] Cursor                      → ~/.cursor/rules/
  [3] Windsurf                    → ~/.codeium/windsurf/memories/
  [4] VS Code (Copilot)           → .github/ in project root
  [5] OpenCode                    → ~/.config/opencode/
  [6] Custom path

Enter 1–6:
"@
        $IDE = Read-Host
    }

    switch ($IDE.Trim()) {
        "1" { $GlobalConfig = Join-Path $env:USERPROFILE ".gemini\antigravity" }
        "2" { $GlobalConfig = Join-Path $env:USERPROFILE ".cursor\rules" }
        "3" { $GlobalConfig = Join-Path $env:USERPROFILE ".codeium\windsurf\memories" }
        "4" {
            $GlobalConfig = Join-Path (Get-Location) ".github\antigravity"
        }
        "5" { $GlobalConfig = Join-Path $env:USERPROFILE ".config\opencode" }
        "6" {
            Write-Question "Enter the full path to your global config folder:"
            $GlobalConfig = (Read-Host).Trim('"')
        }
        default {
            Write-Warn "Unrecognised choice. Defaulting to ~/.gemini/antigravity/"
            $GlobalConfig = Join-Path $env:USERPROFILE ".gemini\antigravity"
        }
    }
}

# ─── Step 2: Install Global Layer ────────────────────────────────────────────
Write-Step "Installing OS → $GlobalConfig"

if (-not (Test-Path $GlobalConfig)) {
    New-Item -ItemType Directory -Path $GlobalConfig -Force | Out-Null
    Write-Success "Created configuration directory: $GlobalConfig"
}

# Clear any existing file in the directory to prevent ghost config files
Write-Step "Cleaning target directory..."
Get-ChildItem -Path $GlobalConfig -Recurse | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

Copy-Item -Path "$GlobalSource\*" -Destination $GlobalConfig -Recurse -Force
Write-Success "Copied OS files successfully."

# ─── Step 2.5: User Personalisation check ─────────────────────────────────────
Write-Question "Enter your name (leave blank for generic setup):"
$UserName = (Read-Host).Trim()

$IsBeloved = $false
if ($UserName -match "(?i)Beloved" -or $UserName -match "(?i)Godswill" -or $UserName -match "(?i)God's sweet" -or $env:USERNAME -match "(?i)godsw") {
    $IsBeloved = $true
}

if ($IsBeloved) {
    Write-Step "Installing custom profile for Beloved..."
    # Replace the generic GEMINI.md in destination with GEMINI-BELOVED.md
    $TargetGemini = Join-Path $GlobalConfig "GEMINI.md"
    $BelovedSource = Join-Path $GlobalConfig "GEMINI-BELOVED.md"
    if (Test-Path $BelovedSource) {
        Copy-Item -Path $BelovedSource -Destination $TargetGemini -Force
        Write-Success "Loaded custom prompt constitution (Beloved configuration)."
    }
}

# Clean up GEMINI-BELOVED.md from target so it doesn't clutter or expose personal info
$TargetBeloved = Join-Path $GlobalConfig "GEMINI-BELOVED.md"
if (Test-Path $TargetBeloved) {
    Remove-Item -Path $TargetBeloved -Force
}


# ─── Step 3: Dynamic Path URI Configuration ────────────────────────────────────
Write-Step "Configuring Absolute System Paths..."
$TargetURI = "file:///" + $GlobalConfig.Replace("\", "/")
Write-Success "Target system URI resolved: $TargetURI"

# Find all markdown files and substitute {{GLOBAL_CONFIG_URI}} with $TargetURI
$mdFiles = Get-ChildItem -Path $GlobalConfig -Filter "*.md" -Recurse
$replaceCount = 0

foreach ($file in $mdFiles) {
    $content = Get-Content $file.FullName -Raw
    if ($content -match "\{\{GLOBAL_CONFIG_URI\}\}") {
        $content = $content -replace "\{\{GLOBAL_CONFIG_URI\}\}", $TargetURI
        Set-Content -Path $file.FullName -Value $content -NoNewline
        $replaceCount++
    }
}

Write-Success "Re-wrote system URIs in $replaceCount configuration files."

# ─── Step 4: Summary ─────────────────────────────────────────────────────────
Write-Host "`n"
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGreen
Write-Host "   Anti-Gravity OS — Installation Complete" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGreen

Write-Host @"
  GLOBAL SYSTEM installed at:
    $GlobalConfig

  Next steps:
    1. Fill in your context files (contexts/stack-context.md, etc.)
    2. Tell your AI: `"Read GEMINI.md`" or configure it as your master prompt.

"@ -ForegroundColor White

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGreen
Write-Host ""
