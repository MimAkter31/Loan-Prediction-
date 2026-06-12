```bash
# Windows PowerShell
$env:MAIL_USERNAME = "Enter your Email"
$env:MAIL_PASSWORD = "Enter your Email app password"

# Windows CMD
set MAIL_USERNAME=Enter your Email
set MAIL_PASSWORD=Enter your Email app password
```

app.config['MAIL_SERVER'] = 'smtp.your-provider.com'
app.config['MAIL_PORT'] = 587 # or 465
app.config['MAIL_USE_TLS'] = True # or False for port 465
app.config['MAIL_USERNAME'] = 'your-email@domain.com'
app.config['MAIL_PASSWORD'] = 'your-password'
