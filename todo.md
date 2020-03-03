# Install python

```
$ sudo apt install python
$ sudo apt install python-tk
```

# Add cronjob

```
$ crontab -e
```
add @reboot sudo python '/<path>/<to>/<script>/stageTimer.py 18 30'