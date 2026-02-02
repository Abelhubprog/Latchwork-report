# Publish to GitHub Pages

**Your URL:** https://abelhubprog.github.io/Latchwork-report/

---

## Quick Upload

Run in PowerShell:

```powershell
cd "d:\JOBS\Technical"
git init
git remote add origin https://github.com/Abelhubprog/Latchwork-report.git
git add index.html
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

---

## Enable Pages

1. Go to: https://github.com/Abelhubprog/Latchwork-report/settings/pages
2. Set **Source** → **Deploy from branch** → **main** → **/(root)**
3. Click **Save**

---

## Done

Your report will be live at:
**https://abelhubprog.github.io/Latchwork-report/**

*(Wait 1-2 minutes after pushing)*
