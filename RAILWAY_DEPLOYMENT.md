# Railway Deployment Guide for Smart Factory Floor Assistant

This guide walks you through deploying the Smart Factory Floor Assistant to Railway.app.

---

## 🚀 Quick Deploy (5 Minutes)

### Step 1: Push to GitHub ✅ (Already Done!)

Your code is already on GitHub at:
https://github.com/arushigupta596/Smart-Factory-Floor-Assistant

### Step 2: Sign Up for Railway

1. Go to https://railway.app
2. Click "Login with GitHub"
3. Authorize Railway to access your repositories

### Step 3: Create New Project

1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose: `arushigupta596/Smart-Factory-Floor-Assistant`
4. Railway will automatically detect it's a Python project

### Step 4: Add Environment Variable

**CRITICAL:** Add your Google API key

1. In Railway dashboard, click on your service
2. Go to "Variables" tab
3. Click "Add Variable"
4. Add:
   ```
   Key: GOOGLE_API_KEY
   Value: [Your actual API key from Google AI Studio]
   ```
5. Click "Add"

### Step 5: Deploy! 🎉

Railway will automatically:
- Install dependencies from `requirements.txt`
- Use the `Procfile` to start the ADK web server
- Assign a public URL (e.g., `your-app.up.railway.app`)

**Deployment takes ~2-3 minutes**

---

## 📋 Configuration Files

Railway uses these files (already in your repo):

### `railway.json`
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "adk web --host 0.0.0.0 --port $PORT",
    "healthcheckPath": "/",
    "healthcheckTimeout": 300
  }
}
```

### `Procfile`
```
web: adk web --host 0.0.0.0 --port ${PORT:-8080}
```

### `requirements.txt`
```
google-adk>=0.5.0
```

---

## 🌐 Access Your Deployed App

Once deployed, Railway provides:

1. **Public URL**: `https://your-service-name.up.railway.app`
2. **Custom domain support** (optional)
3. **Automatic HTTPS**
4. **Auto-deploy on git push**

### Using Your App

Visit the Railway URL and you'll see the ADK web UI. Select `factory_floor_agent` and start asking questions!

---

## 💰 Pricing

**Free Tier:**
- $5 of usage credits per month (includes bandwidth, compute)
- Perfect for POCs and demos
- ~500 hours of runtime per month

**Starter Plan ($5/month):**
- $5 credits + $5 additional usage
- Removes execution time limits
- Priority support

**Typical Usage for This App:**
- ~5GB bandwidth/month: ~$0.50
- ~100 hours compute/month: ~$2.00
- **Total: ~$2.50/month** (well within free tier!)

---

## 🔧 Troubleshooting

### Issue: "Application failed to respond"

**Solution:** Check that `GOOGLE_API_KEY` environment variable is set correctly.

```bash
# In Railway dashboard
Variables → GOOGLE_API_KEY → [verify it's set]
```

### Issue: "Module not found: google.adk"

**Solution:** Railway should auto-install from `requirements.txt`. Force a rebuild:

1. Go to Deployments tab
2. Click "..." menu on latest deployment
3. Select "Redeploy"

### Issue: Port binding errors

**Solution:** Railway automatically sets the `$PORT` variable. Our `Procfile` uses it correctly. No action needed.

### Issue: Deployment timeout

**Solution:** Increase healthcheck timeout (already set to 300s in `railway.json`).

---

## 📊 Monitoring

### View Logs

1. Click on your service in Railway dashboard
2. Go to "Deployments" tab
3. Click on active deployment
4. View real-time logs

### Check Metrics

1. Go to "Metrics" tab
2. View CPU, memory, bandwidth usage
3. Monitor request count

---

## 🔄 Auto-Deploy on Git Push

Railway automatically redeploys when you push to GitHub:

```bash
# Make changes locally
git add .
git commit -m "Update agents"
git push

# Railway auto-deploys in ~2 minutes
```

---

## 🎯 Best Practices

### 1. Use Railway for Development/Staging

- Perfect for demos and POCs
- Great for client presentations
- Easy team collaboration

### 2. Environment Variables

Store all secrets in Railway Variables (never in code):
- `GOOGLE_API_KEY` - Your Google AI Studio key
- `GOOGLE_GENAI_USE_VERTEXAI` - Set to `FALSE` for AI Studio

### 3. Custom Domains

Add your own domain:
1. Go to Settings → Domains
2. Click "Add Domain"
3. Enter your domain
4. Add CNAME record to your DNS

### 4. Scaling

Railway auto-scales vertically. For horizontal scaling:
- Upgrade to Pro plan
- Use multiple replicas
- Add load balancer

---

## 🔐 Security

### Recommendations

1. **Restrict Access:**
   - Use Railway's built-in authentication
   - Add basic auth if needed
   - Consider VPN for production

2. **Environment Variables:**
   - Never commit `.env` to Git (already in `.gitignore`)
   - Rotate API keys periodically
   - Use separate keys for dev/prod

3. **HTTPS:**
   - Railway provides free HTTPS
   - Custom domains get Let's Encrypt certs
   - All traffic encrypted

---

## 📱 Mobile Access

Railway URLs work great on mobile:
- Responsive ADK web UI
- Works on iOS/Android
- Save to home screen for quick access

---

## 🆚 Railway vs Other Platforms

| Feature | Railway | Vercel | Cloud Run | Render |
|---------|---------|--------|-----------|--------|
| **Python/ADK Support** | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| **Free Tier** | $5 credits | Functions only | Yes (limits) | Yes (limits) |
| **Auto-deploy** | ✅ Yes | ✅ Yes | Manual | ✅ Yes |
| **Setup Time** | 5 min | N/A | 15 min | 10 min |
| **Custom Domains** | ✅ Free | ✅ Free | ✅ Free | ✅ Free |
| **Best For** | This app! | Frontend | Enterprise | Full-stack |

---

## 🚀 Production Deployment Path

**Phase 1: Railway (Now)**
- Deploy for POC/demos
- Show to stakeholders
- Gather feedback

**Phase 2: Railway Starter ($5/month)**
- Add custom domain
- Increase resources
- Production-ready for small teams

**Phase 3: Migrate to Cloud Run (Later)**
- When you need:
  - Enterprise SLA
  - Multi-region
  - Integration with GCP services
  - Vertex AI instead of AI Studio

---

## 📞 Support

**Railway Support:**
- Discord: https://discord.gg/railway
- Docs: https://docs.railway.app
- Status: https://railway.app/status

**This App:**
- GitHub Issues: https://github.com/arushigupta596/Smart-Factory-Floor-Assistant/issues
- Product Doc: See `PRODUCT_DOCUMENT.md`

---

## ✅ Deployment Checklist

Before deploying, verify:

- [ ] Code pushed to GitHub
- [ ] `railway.json` exists
- [ ] `Procfile` exists
- [ ] `requirements.txt` has `google-adk>=0.5.0`
- [ ] `.gitignore` excludes `.env`
- [ ] Google AI Studio API key ready

After deploying:

- [ ] Set `GOOGLE_API_KEY` environment variable
- [ ] Verify deployment succeeded
- [ ] Test with Query 1: "Which production lines are running?"
- [ ] Share URL with team

---

## 🎉 You're Ready!

Your Smart Factory Floor Assistant is ready to deploy on Railway!

**Next step:** Push these new files to GitHub, then deploy on Railway.

```bash
git add railway.json Procfile RAILWAY_DEPLOYMENT.md
git commit -m "Add Railway deployment configuration"
git push
```

Then follow Step 2-5 above to deploy! 🚀
