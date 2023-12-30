---
tags:
  - Introductory
date:
  - 2023-10-31
authors: 
  - Christine Koppel
---

# Obsidian - Writing the Documentation

## Obsidian Guide

***To be written in more user friendly summarised in-depth explanation.***
[Here is the following documentation how to install, use and format Obsidian](https://help.obsidian.md/Getting+started/Download+and+install+Obsidian), which is the application used to write the documentation and publishing them onto the web-server.

### Directory layout 
#### Images
Images should be put towards the `.../Image Folder/*`, with the sensible sub-directory for which purpose it has. For example, PCB schematic screenshots going to the `.../Image Folder/PCB Screenshots`

#### Files
Files other than images should be put into  `.../Files/*`, with the sensible sub-directory for which purpose it has. LTSpice Simulation files like `.asc` extension should be going to the `.../Files/Simulation Files`, sheets into `.../Files/Sheets```.

### Page layout format
As of currently, the page layout is flexible, although with some headers to be written down before being published.
#### Note Page Properties
New note page properties should be initialised with the header properties to document, author and connect notes together.
Here is the following example properties to used here:
```YAML
---
tags:
  - Introductory
date:
  - 2023-10-31
authors: 
  - Christine Koppel
---
```

[There's more reading about the note property documentation here.](https://help.obsidian.md/Editing+and+formatting/Properties)

# GitHub - Committing the contribution
## Login into the GitHub through the Command Line Argument

The following command will start an interactive setup to login into your already made GitHub account.
```sh
gh auth login
```

## Contributing to the repository through a CLI

### Starting up
Download and clone the repository of the ProtoTAU EEES documentation from GitHub.
```sh
git clone https://github.com/Kodalem/prototau.git
```

### Adding changes into the personal repository
Tracking changes of all files in your repository, which has to be done before committing.
```sh
git add .
```

Save updated code to a new commit naming with a summarised description ie. "Contribution Documentation Guide"
```sh
git commit -m "Contribution Documentation Guide"
```

If everything seems to be in order, push it onto the GitHub repository
```sh 
git push --all
```

#### Other useful commands and cheat sheet

##### Staging
Show modified files in working directory, staged for your next commit
```sh
git status
```

Add a file as it looks now to your next commit (stage)
```sh
git add [file]
```

Unstage a file while retaining the changes in working directory
```sh
git reset [file]
```

Difference of what is changed but not staged
```sh
git diff
```

Difference of what is staged but not yet committed
```sh
git diff --staged
```

Commit your staged content as a new commit snapshot
```sh
git commit -m “[descriptive message]”
```

##### Branching and merging
List your branches and they will appear next to the currently active branch.
```sh
git branch
```
Create a new branch at the current commit
```sh
git branch [branch-name]
```
Switch to another branch and check it out into your working directory
```sh
git checkout
```
Merge the specified branch’s history into the current one
```sh
git merge [branch]
```
Show all commits in the current branch’s history
```sh
git log
```

##### Sharing and Updating
Add a git URL as an alias
```sh
git remote add [alias] [url]
```

Fetch down all the branches from that Git remote
```sh
git fetch [alias]
```
Merge a remote branch into your current branch to bring it up to date
```sh
git merge [alias]/[branch]
```
Transmit local branch commits to the remote repository branch
```sh
git push [alias] [branch]
```
Fetch and merge any commits from the tracking remote branch
```sh
git pull
```


## Downloading the repository through Windows

***To be completed and contributed towards.***


# Quartz4 - Updating the Webhost

***To be improved further and might be overhauled as it may be moved over to university's systems.***

[Here is the following documentation page of the Quartz4 as a reference.](https://quartz.jzhao.xyz/)

Logging into the webserver.
```sh
ssh oisu@XXXXXXXXX.kodalem.com
```

### Updating the Webserver Content
Loading into the directory of the web-server content
```sh
cd ~/quartz/content/prototau
```

As the folder content is git of the documentation repository, we can just pull the changes into the webhost server from the main branch.
```sh
git pull
```

### Compiling and running the Webserver

Load into the main quartz directory.
```sh
cd ~/quartz
```

Build and host the website
```sh
npx quartz build --serve
```