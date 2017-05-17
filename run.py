from app import app
app.run('0.0.0.0', port=80)
# app.run('0.0.0.0', port=443, ssl_context=('/etc/letsencrypt/live/tongying.design/fullchain.pem', '/etc/letsencrypt/live/tongying.design/privkey.pem'))