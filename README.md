# LA2Project
Final Project for Linear Algebra 2

How to use git for git Newbies
============

General Workflow
----------
An example workflow for you would look like this:

```git status```

```git add LA2Project/*```

```git commit -m "Did something" ```

```git pull```

```git push```
	

git status
---------
Shows the status of file changes relative to your last commit. Has 3 categories.
* Green: changes staged for commit. These have been git add-ed, but not committed.
* Red 1: Changed files. These files you have edited from your last commit. 
You have not yet git add-ed them to be staged for a commit.
If you commit at this point, these files will not be added.
* Red 2: Untracked Files. These are generally safe as are, as they cannot be overriden since they are not tracked by git.
This is also where any new files will appear when you create a new file. The new files may or may not have to be added.
	
	
git add
---------
**syntax:** ```git add <filepath>```

This command adds files to be staged for a commit. Changes to git-tracked files must be committed in order to git pull.
There are a few tricks to this one to make it go faster so that you don't have to add files one at a time.
1. ```git add .```  will add everything here (current directory) **WARNING:** this leads to trouble.
2. ```git add <directory_path>/*``` will add everything in a directory. This is generally safer.
3. ```git add *.<file_end>``` will add all files of the specified file type. 
	- ex: git add *.cs adds all Csharp files
	
git commit
---------
**syntax:** ``` git commit -m "Commit Message" ```

This saves all changes that were added to someplace magical that is safe from catastrophic events.
However, these changes are not yet part of the branch you are on, as they have not been pushed.
When you commit please add a descriptive message detailing the changes you've made.
In order to pull, local changes must be committed (but not pushed).
	
If you forget to add a message and only ```git commit```, see the section on [Using Vim](#using-vim)
	
git pull
---------
**syntax:** ```git pull``` will pull from the branch set as your git's HEAD.

```git pull origin <branch>``` is a more specific way to pull from a specific branch.
- ex: ```git pull origin dev``` 

Pulling is how we download one another's changes to our local projects.

In order to pull, you must commit local changes or they will be overriden (it will warn you about it, too).
Once local changes have been commited, ```git pull``` to get the new changes. It will try to automerge files, but this may fail.
If it does fail, the terminal output will tell you and you can see which files failed. You will have to manually correct these files.

To find the conflicts in text files, look for places with ```>>>>>>> HEAD``` followed by some stuff then 
``` ========= ``` then your stuff, then a long string on numbers and letters. 
These are the problems it couldn't fix, so look through it and fix it yourself (often its rather easy).
	
git push
---------
**syntax:** ```git push``` will push to the branch you are on.

```git push origin <branch>``` is a more specific way to push to a specific branch (try to make sure you use the branch you are supposed to be on).
This works pretty much the same as pull except you use it to update the online repository to reflect the new changes.
Your branch must be up to date with the repository in order to push. 

**Always pull and fix errors before you push**

*Please only push stable versions of a project to the online repositories.*
	
	
Using VIM	
---------

Occasionally you might ```git pull``` and get thrown into vim to type a commit message as to why you need to merge.
You may also get into here if you forget the ```-m"message"``` and just use ```git commit```.

To begin writing, press **i**. Navigate past the comments with the arrow keys. use **Enter** to make a new line.

After writing your message, press **esc**. Then type ```:wq``` to write and quit the file. 
The text should show up on the bottom line of terminal.
Press **enter** to execute the command.

Make sure to check for merge errors after this. You may also have to restart the workflow. Check with ```git status```.
