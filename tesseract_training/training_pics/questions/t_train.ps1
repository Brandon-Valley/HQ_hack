<#

Automate Tesseract 3.02 language data pack generation process.

@author: Quan Nguyen
@date: 16 April 2013

The script file should be placed in the same directory as Tesseract's binary executables.
All training data files must be prefixed with the language code -- such as: 
vie.arial.exp0.tif, vie.font_properties, vie.unicharambigs, vie.frequent_words_list, vie.words_list
-- and placed in a trainfolder directory, which could be placed directly under Tesseract directory.

http://code.google.com/p/tesseract-ocr/wiki/TrainingTesseract3

Run PowerShell as Administrator and allow script execution by running the following command:

PS > Set-ExecutionPolicy RemoteSigned

Then execute the script by:

PS > .\train.ps1
or
PS > .\train.ps1 yourlang trainfolder

Windows PowerShell 2.0 Download: http://support.microsoft.com/kb/968929

#>


echo " "
echo " "
echo " "
echo " "
echo " "
echo " "




if ($args[0] -and ($args[0] -eq "-?" -or $args[0] -eq "-h" -or $args[0] -eq "-help")) {
    Write-Host "Usage: .\train.ps1"
    Write-Host "   or  .\train.ps1 trainfolder yourlang [bootstraplang]"
    Write-Host "where trainfolder directory contains all the training data files prefixed with yourlang, e.g.,"
    Write-Host "vie.arial.exp0.tif, vie.font_properties, vie.unicharambigs, vie.frequent_words_list, vie.words_list,"
    Write-Host "and could be placed directly under Tesseract directory"
    exit
}

 $trainDir = 'C:\Users\Brandon\Documents\Personal_Projects\HQ_hack\tesseract_training\training_pics\questions'
 $lang = 'eng'
 $bootstraplang = 'HQ_Question_Font'

<#
$trainDir = $args[0]
if (!$trainDir) {
    $trainDir = Read-Host "Enter location of the training data folder"
}

$lang = $args[1]
if (!$lang) {
    $lang = Read-Host "Enter a language code"
}

if ($lang -eq "" -or $trainDir -eq "") {
     Write-Host "Invalid input"
     exit
}

if (!(test-path $trainDir)) {
    throw "{0} is not a valid path" -f $trainDir
    exit
}

$bootstraplang = $args[2]
if (!$bootstraplang) {
    $bootstraplang = Read-Host "Enter a bootstrap language code (optional)"
}
#>

echo "=== Generating Tesseract language data for language: $lang ==="

$fullPath = Resolve-Path $trainDir
echo "** Your training images should be in ""$fullPath"" directory."

$al = New-Object System.Collections.ArrayList

echo "Make Box Files"
$boxFiles = ""
Foreach ($entry in dir $trainDir) {
   If ($entry.name.toLower().endsWith(".png") -and $entry.name.startsWith($lang)) {
      echo "** Processing image: $entry"
      $nameWoExt = [IO.Path]::Combine($trainDir, $entry.BaseName)
      #echo $entry.BaseName

      #tesseract eng.HQ_Options_Font.exp3.png eng.HQ_Options_Font.exp3 batch.nochop makebox
      $command = 'tesseract ' + $entry + ' ' + $entry.BaseName + ' batch.nochop makebox'
      iex $command

      $boxFiles += $nameWoExt + ".box "
   }
}

echo "** Box files should be edited before continuing. **"
