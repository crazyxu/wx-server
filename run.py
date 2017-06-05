from app import app
# app.run('127.0.0.1', port=80)
app.run('0.0.0.0', port=443, ssl_context=('/etc/letsencrypt/live/xucan.org/fullchain.pem', '/etc/letsencrypt/live/xucan.org/privkey.pem'))