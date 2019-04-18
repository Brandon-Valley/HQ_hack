
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
$trFiles = ""
Foreach ($entry in dir $trainDir) {
    If ($entry.name.toLower().endsWith(".png") -and $entry.name.startsWith($lang)) 
    {
        echo $entry
        #tesseract pol.ocrb.exp$i.tif pol.ocrb.exp$i nobatch box.train
        $command = 'tesseract ' + $entry + ' ' + $entry.BaseName + ' nobatch box.train'
        iex $command

        $nameWoExt = [IO.Path]::Combine($trainDir, $entry.BaseName)
        $boxFiles += $nameWoExt + ".box "
        $trFiles += $nameWoExt + ".tr "


    }
}
#>


echo "Compute the Character Set"
Invoke-Expression "unicharset_extractor -D $trainDir $boxFiles"

echo "HQ_Q 0 1 0 0 0" > font_properties # tell Tesseract informations about the font
mftraining -F font_properties -U unicharset -O pol.unicharset `wrap $N "pol.ocrb.exp" ".tr"`

Invoke-Expression "cntraining -D $trainDir $trFiles"

mv normproto HQ_q.normproto

combine_tessdata HQ_q.

<#
echo "ocrb 0 0 1 0 0" > font_properties # tell Tesseract informations about the font
mftraining -F font_properties -U unicharset -O pol.unicharset `wrap $N "pol.ocrb.exp" ".tr"`
cntraining `wrap $N "pol.ocrb.exp" ".tr"`
# rename all files created by mftraing en cntraining, add the prefix pol.:
    mv inttemp pol.inttemp
    mv normproto pol.normproto
    mv pffmtable pol.pffmtable
    mv shapetable pol.shapetable
combine_tessdata pol.

#>






