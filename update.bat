@echo off
echo ================================
echo Updating website on GitHub...
echo ================================

git pull origin main --rebase

git add .
git commit -m "Auto update"
git push

echo ================================
echo Website updated successfully!
echo Press any key to close...
echo ================================
pause
