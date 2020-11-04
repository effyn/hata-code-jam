[![Discord](https://img.shields.io/static/v1?label=Python%20Discord&logo=discord&message=%3E40k%20members&color=%237289DA&logoColor=white)](https://discord.gg/2B963hn)
[![License](https://img.shields.io/github/license/python-discord/bot)](LICENSE)
[![Website](https://img.shields.io/badge/website-visit-brightgreen)][7]

### Hata CodeJam!

## Getting Started

### 1. Fork this repository

Start by [forking this repository][3]. If you're working as a team, only one person needs to do this.

### 2. Find your team folder in the repository

The repository should already contain a subdirectory named after your team. **All your project files must be contained within your team's subdirectory**. If you make any changes to files other than those in your team folder, we will not be able to merge your PR, and may have to disqualify your submission.

We are aware some CI/CD solutions require you to have configuration files/folders in the root of the repository; if you're using one of those, either try to use a unique name (e.g. prefix the configuration files with your team name) or remove the files/directories just before the end of the jam.

### 3. Create a pull request

Open a pull request from your fork's `master` to the `master` branch of this repository in order to submit your project. **You should use the name of your team as the name of the pull request.** Please open you Pull Request at the start of the jam and ensure that the "Allow edits by maintainers" option is enabled. 

### 4. Commit to your master branch

The pull request you created will be automatically updated whenever you push code to `master` on your fork, so you can create the pull request whenever you want, and you only have to do it once. You do not need to wait until the very end of the game jam before you do it. Just keep pushing code to your `master` branch and do your best to finish before the game jam ends!

If you are working as a team, you should consider learning about feature branches so that you don't all work directly on the `master` branch and cause each other a bunch of conflicts. For a short explanation of how this works, see [this video][2].

## Things to keep in mind

### Your project should be easy to set-up
You should make sure your project is easy to set up for us, the reviewers. Ideally, it should not take us more than a few steps to get your project up and running, and those steps should be well-documented in your project’s README file. Consider using dependency management tools, like `pipenv` and `npm`, to make installing the dependencies of your projects as easy as possible. We would also encourage you to use `docker` and `docker-compose` to containerize your project, but this isn't a requirement.

### All projects will be merged into this repository
Your project will be merged into this repository at the end of the jam. This means that your project will stay available after the jam ends and that you'll get contributions credits for this repository on your GitHub-account. Do keep in mind that this repository is licensed under the [MIT open source license], which means that all the code and assets you submit for the Code Jam should be compatible with that license. In addition, please make sure to provide credit to the source of all third-party assets, even if the license does not require you to do so. 

Please also make sure you follow the instructions in the [Getting Started](#getting-started) section. We can't merge Pull Requests that (would) create conflicts with the submissions of the other teams.

### Write a good README
Your project has to include documentation. At the very least, it should include instructions on how to set-up and run your projects, but keep in mind that a README is the first thing people typically see when they look at a project on GitHub. A good README includes a short description of the project, installation instructions, and often documents common usage of the application. Browse the team folders in the [Winter Code Jam 2020 repository][4] to get an idea of the kind of READMEs commonly included in Code Jam projects.

### The main language of your project should be English
As English is the only language the judges share, we require you to use English as the main language for your project. This means that your variable names, code comments, `git` commit messages, and documentation should all be in English. The text displayed in your bot application should also be in English, although you are allowed to provide the user with options for internationalization and translation.
