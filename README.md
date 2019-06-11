# CommandShell-ProgressBar
Command shell progress bar class for use with python CLI apps. percent_complete parameter should always be 0.0 <= percent_complete <= 1.0.

Code sample:

```python
from cliprogressbar import CliProgressBar
from time import sleep

bar = CliProgressBar()

for i in range(101):
	bar.display_progress(i/100)
	sleep(0.1)
```
