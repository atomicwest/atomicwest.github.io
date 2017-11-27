<# move multiple files out of multiple folders 
and rename with .png extension #>
 
$dir = "C:\"

Get-ChildItem -Recurse $dir | ForEach-Object {
	#Write-Host $_.Name
	Copy-Item $_.Name -Destination "$($dir)\newroot"
}

