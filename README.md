# herokuSamplePrjct

### Workflow
```
git init

git add .

git commit -a -m "first commit"

heroku apps

heroku apps:create your_app_name

heroku git:remote -a your_app_name

git remote -v

git push heroku master

heroku config:set KEY=VALUE

heroku ps:scale web=1

heroku ps:scale web=0
```