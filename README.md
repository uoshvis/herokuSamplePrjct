# herokuSamplePrjct

### Workflow
```
git init

git add .

git commit -a -m "first commit"

heroku login

heroku apps
# see the new process type running
heroku ps

heroku apps:create your_app_name

heroku git:remote -a your_app_name

git remote -v

git push heroku master

heroku config:set KEY=VALUE

# To launch a worker, you need to scale it up to one dyno
heroku ps:scale web=1

heroku ps:scale web=0

heroku logs

# view just the messages from the worker process type
heroku logs --ps worker
```