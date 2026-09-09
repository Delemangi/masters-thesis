param([int]$TimeoutSeconds = 240)
$ErrorActionPreference = 'Stop'
$paperRoot = $PSScriptRoot
$compiler = Join-Path $paperRoot 'tools\tectonic.exe'
if (-not (Test-Path -LiteralPath $compiler)) { throw 'Portable compiler missing.' }
$env:TECTONIC_CACHE_DIR = Join-Path $paperRoot 'cache'
$env:FONTCONFIG_FILE = Join-Path $paperRoot 'tools\fonts.conf'
$buildRoot = Join-Path $paperRoot 'build'
New-Item -ItemType Directory -Force -Path $buildRoot | Out-Null
$compilerInfo = [System.Diagnostics.ProcessStartInfo]::new()
$compilerInfo.FileName = $compiler
$compilerInfo.WorkingDirectory = $paperRoot
$compilerInfo.Arguments = '--keep-logs --keep-intermediates --outdir build main.tex'
$compilerInfo.UseShellExecute = $false
$compilerInfo.CreateNoWindow = $true
$compilerInfo.RedirectStandardOutput = $true
$compilerInfo.RedirectStandardError = $true
$compilerProcess = [System.Diagnostics.Process]::new()
$compilerProcess.StartInfo = $compilerInfo
[void]$compilerProcess.Start()
$outTask = $compilerProcess.StandardOutput.ReadToEndAsync()
$errTask = $compilerProcess.StandardError.ReadToEndAsync()
if (-not $compilerProcess.WaitForExit($TimeoutSeconds * 1000)) {
    $compilerProcess.Kill()
    throw "Compiler exceeded $TimeoutSeconds seconds; owned compiler process stopped."
}
$outTask.Result | Set-Content -LiteralPath (Join-Path $buildRoot 'compiler.stdout.txt')
$errTask.Result | Set-Content -LiteralPath (Join-Path $buildRoot 'compiler.stderr.txt')
$outTask.Result
$errTask.Result
if ($compilerProcess.ExitCode -ne 0) { throw "Compiler failed with exit code $($compilerProcess.ExitCode)." }
$paperSourceHashes = @{}
foreach ($paperSourceName in @('main.tex', 'architecture.tex', 'related_work.tex', 'controlled_results.tex', 'references.bib')) {
    $paperSourceHashes[$paperSourceName] = (Get-FileHash -LiteralPath (Join-Path $paperRoot $paperSourceName) -Algorithm SHA256).Hash.ToLowerInvariant()
}
@{
    source_sha256 = $paperSourceHashes
    pdf_sha256 = (Get-FileHash -LiteralPath (Join-Path $buildRoot 'main.pdf') -Algorithm SHA256).Hash.ToLowerInvariant()
    compiled_at_utc = [DateTime]::UtcNow.ToString('o')
} | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $buildRoot 'source-manifest.json') -Encoding utf8

