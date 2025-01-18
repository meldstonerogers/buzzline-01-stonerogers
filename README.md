# buzzline-01-stonerogers
Streaming Data, Project 1
Melissa Stone Rogers, [GitHub](https://github.com/meldstonerogers/buzzline-01-stonerogers)

## Introduction

This is a professional project introducing the use of streaming data, using Python Version 3.11 and Git. 
The Python language includes generators - this feature will generate some streaming buzzline messages. 
As the code runs, it will continuously update log file. A consumer is used to modify this log file and alert to when a specific message is detected. This project was forked from Dr. Case's project repository found [here](https://github.com/denisecase/buzzline-01-case). Much of the detailed instructions in this README.md were borrowed from Dr. Case's project specifications, and updated for my machine.
Commands were used on a Mac machine running zsh.   

## Task 1. Set Up Your Machine

First, you'll need to set up your machine. 
Detailed instructions by operating system are provided. 

1. Install Git.
2. Install Python **Version 3.11**.
3. Install VS Code.
4. Configure Git with user.name and user.email. 
5. Turn on VS Code File / Autosave.
6. Install VS Code Extensions (see instructions)

For detailed instructions, see:

- [SETUP-MAC-LINUX.md](docs/SETUP-MAC-LINUX.md)
- [SETUP-WINDOWS.md](docs/SETUP-WINDOWS.md)

## Task 2. Copy This Example Project & Customize your Repo Name

Once the tools are installed, copy/fork this project into your GitHub account
and create your own version of this project to run and experiment with. 
Name it **buzzline-01-yourname** where yourname is something unique to you.
Follow the instructions in [FORK-THIS-REPO.md](docs/FORK-THIS-REPO.md).

## Task 3. Manage Local Project Virtual Environment

Python needs a place to keep all the free code we download and use in our projects. 
For this, we create a .venv folder to hold our local project virtual environment. 
We create this folder (just once), activate it, and install additional packages listed in requirements.txt. 

Important: After creating, activating, and installing packages into .venv, 
we must remember to activate .venv every time we open a new terminal. 

Follow the instructions in [MANAGE-VENV.md](docs/MANAGE-VENV.md) to:
1. Create your .venv
2. Activate .venv
3. Install the required dependencies using requirements.txt.

### Initial Project Commit 
Turn on the autosave function in VS Code. Push changes to GitHub freqently to effectively track changes. Update the commit message to a meaningful note for your changes. 
```zsh
git add .
git commit -m "initial"                         
git push origin main
```

## Task 4. Generate Streaming Data (Terminal 1)

In VS Code, open a terminal.
Use the commands below to activate .venv, and run the generator as a module. 
To learn more about why we run our Python file as a module, see [PYTHON-PKG-IMPORTS](docs/PYTHON-PKG-IMPORTS.md) 

```zsh
source .venv/bin/activate
python3 -m producers.basic_producer_stonerogers
```

## Task 5. Monitor an Active Log File (Terminal 2)

In VS Code, open a NEW terminal in your root project folder. 
Use the commands below to activate .venv, and run the file as a module. 

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.basic_consumer_stonerogers
```

### Troubleshooting Consumer Alerts
I ran into an issue running my consumer file, when an alert for a special condition was triggered, the alert would continuously appear, eventually causing VS Code to quit. I troubleshooted various code options consulting with ChatGPT, but either the issue would persist, or the alert would not trigger at all. A classmate had a similar issue and was able to adjust the code to where the error stopped occuring. The following code was borrowed from Justin Kilchenmann's similar [project](https://github.com/jkilchenmann/buzzline-01-kilchenmann/blob/main/consumers/basic_consumer_kilchenmann.py). Below is the adjusted code used within my project. 

```zsh
# monitor and alert on special conditions
if "odd" in message:
    now = datetime.now() 
    if "odd" in alert_times:
            last_alert_time = alert_times["odd"]
            if now - last_alert_time < timedelta(seconds=2):
                # Skip alert if it's too soon after last one
                continue

    # Log and print alert
    print(f"ALERT: An oddity was found!")
    logger.warning(f"An oddity was found!")
    alert_times["odd"] = now # Update the last alert time  
```

## Save Space
To save disk space, you can delete the .venv folder when not actively working on this project.
We can always recreate it, activate it, and reinstall the necessary packages later. 
Managing Python virtual environments is a necessary and valuable skill. 

Additionally, I became unable to commit to GitHub due to the size of the project_log.log file. To work around this, I removed the previous commits of this file from GitHub, then I added this file within .gitignore. From here, I was able to commit to GitHub without issues. I utilized BFG-Repo Cleaner for this task. 

```zsh
brew install bfg
```
```zsh
cd /Users/melissastonerogers/Documents/streamingdata/buzzline-01-stonerogers
```
```zsh
bfg --delete-files 'project_log.log'
```
```zsh
git push --force origin main
```
## Complete Your Project
Save your project and push back to your repository. 
```
git add .
git commit -m "final"                         
git push origin main
```

## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.
