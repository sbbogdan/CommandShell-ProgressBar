# CommandShell-ProgressBar
Command shell progress bar class for use with python CLI apps. Code should be self explanatory, inline documented.

Code sample:
`
from cliprogressbar import CliProgressBar
from time import sleep

bar = CliProgressBar()

for i in range(100):
		bar.display_progress(i/100)
    sleep(0.1)
`
