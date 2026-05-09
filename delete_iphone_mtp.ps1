param (
    [string]$DeletedJson = "deleted.json",
    [string]$DeviceName = "Apple iPhone",
    [string]$StorageName = "Internal Storage"
)

if (-not (Test-Path $DeletedJson)) {
    Write-Error "File $DeletedJson not found."
    exit
}

$toDelete = Get-Content $DeletedJson | ConvertFrom-Json -AsHashtable
if ($toDelete.Count -eq 0) {
    Write-Host "Nothing to delete."
    exit
}

# Access Shell.Application for MTP access
$shell = New-Object -ComObject Shell.Application
$computer = $shell.Namespace(17) # My Computer

$iphone = $computer.Items() | Where-Object { $_.Name -eq $DeviceName }
if (-not $iphone) {
    Write-Error "Device '$DeviceName' not found. Ensure it is plugged in and unlocked."
    exit
}

$storage = $iphone.GetFolder.Items() | Where-Object { $_.Name -eq $StorageName }
if (-not $storage) {
    Write-Error "Storage '$StorageName' not found on device."
    exit
}

$dcim = $storage.GetFolder.Items() | Where-Object { $_.Name -eq "DCIM" }
if (-not $dcim) {
    Write-Error "DCIM folder not found."
    exit
}

# Build recursive map of files on iPhone: Filename -> FolderItem
Write-Host "Scanning iPhone (MTP is slow, please wait)..."
$iphoneFiles = @{}

function Scan-Folder($folderItem) {
    foreach ($item in $folderItem.GetFolder.Items()) {
        if ($item.IsFolder) {
            Scan-Folder($item)
        } else {
            if (-not $iphoneFiles.ContainsKey($item.Name)) {
                $iphoneFiles[$item.Name] = $item
            }
        }
    }
}

Scan-Folder($dcim)

$count = 0
foreach ($relPath in $toDelete.Keys) {
    $filename = Split-Path $relPath -Leaf
    
    if ($iphoneFiles.ContainsKey($filename)) {
        $item = $iphoneFiles[$filename]
        Write-Host "Deleting: $($item.Name)"
        try {
            # Shell.Application delete (moves to Recycle Bin or permanent depending on device)
            # MTP usually deletes permanently
            $item.InvokeVerb("delete")
            $count++
        } catch {
            Write-Error "Failed to delete $filename"
        }
    } else {
        Write-Warning "File $filename not found on iPhone."
    }
}

Write-Host "`nFinished. $count files deleted from iPhone."
