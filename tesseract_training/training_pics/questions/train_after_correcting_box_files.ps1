
echo "222 "
echo "222 "
echo "222 "
echo "222 "
echo "222 "
echo "222 "



 $trainDir = 'C:\Users\Brandon\Documents\Personal_Projects\HQ_hack\tesseract_training\training_pics\questions'
 $lang = 'eng'
 $bootstraplang = 'HQ_Question_Font'









echo "=== Generating Tesseract language data for language: $lang ==="

$fullPath = Resolve-Path $trainDir
echo "** Your training images should be in ""$fullPath"" directory."

$al = New-Object System.Collections.ArrayList

echo "Make Box Files"
$boxFiles = ""
Foreach ($entry in dir $trainDir) {
    If ($entry.name.toLower().endsWith(".tif") -and $entry.name.startsWith($lang)) 
    {
        echo $entry
        #tesseract pol.ocrb.exp$i.tif pol.ocrb.exp$i nobatch box.train
        $command = 'tesseract ' + $entry + ' ' + $entry.BaseName + ' nobatch box.train'
        iex $command
    }
}
#>

