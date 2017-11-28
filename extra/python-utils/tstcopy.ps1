<# 
JG
powershell -ExecutionPolicy bypass
- move multiple files out of multiple folders 
- rename with .png extension (assuming files have no ext)
- change search dir and new dir as necessary
#>

$searchdir = "rootdir"
$newdir = "copyroot"

$searchpath = "$($pwd)\$($searchdir)"
$newpath = "$($pwd)\$($newdir)"

If (-Not(Test-Path $newpath)) {
	New-Item -Path $pwd -Name $newdir -ItemType "directory"
}

Get-ChildItem -Recurse $searchpath | ForEach-Object {
	If (-Not($_ -is [System.IO.DirectoryInfo] )) {
		#Write-Host $_.Name
		Copy-Item $_.FullName -Destination "$($newpath)\$($_.Name).png"
	}
}
