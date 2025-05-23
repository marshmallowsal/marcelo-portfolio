# Railway Deployment Guide

## Files Added/Updated for Railway Deployment

- ✅ `Procfile` - Tells Railway how to start your Django app
- ✅ `requirements.txt` - Updated with all necessary packages
- ✅ `portfolio/settings.py` - Production-ready configuration
- ✅ `runtime.txt` - Specifies Python version
- ✅ `railway.json` - Railway-specific configuration

## Required Environment Variables

Set these in your Railway project dashboard:

### Required for Production
```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
```

### Optional (for email functionality)
```
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Automatic (Railway provides these)
```
PORT=8000 (Railway sets this automatically)
```

## Deployment Steps

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Railway deployment configuration"
   git push origin main
   ```

2. **Create Railway Project**
   - Go to [railway.app](https://railway.app)
   - Connect your GitHub repository
   - Railway will automatically detect this is a Django project

3. **Add Environment Variables**
   - In Railway dashboard, go to Variables tab
   - Add the required environment variables listed above

4. **Deploy**
   - Railway will automatically build and deploy your app
   - Your app will be available at `https://your-app-name.up.railway.app`

## Production Features Enabled

- ✅ Static file serving with WhiteNoise
- ✅ SQLite database (simple and reliable)
- ✅ Environment-based configuration
- ✅ Security headers and HTTPS enforcement
- ✅ Automatic migrations on deploy
- ✅ Gunicorn WSGI server

## Database

This setup uses SQLite for both development and production. SQLite is:
- ✅ Perfect for small to medium portfolio sites
- ✅ Zero configuration required
- ✅ Automatically backed up with your Railway deployment
- ✅ No separate database service needed

## Local Development

Your app will work exactly the same locally and in production:

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
```

## Troubleshooting

If deployment fails:
1. Check Railway logs for specific error messages
2. Ensure all environment variables are set correctly
3. Verify your `SECRET_KEY` is set and not the default development key
4. Check that your GitHub repository includes all the new files

## Benefits of This Setup

- 🚀 **Simple**: No database setup required
- 💰 **Cost-effective**: No separate database charges
- 🔧 **Easy maintenance**: SQLite file is part of your deployment
- ⚡ **Fast**: No network latency to external database
- 🛡️ **Reliable**: SQLite is battle-tested and stable 