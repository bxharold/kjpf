still confused.  from ~/Git/kjpf:   I will do   git add -A    et ensuite   git commit -am "Updated README."



OK, this is the transcript:
HiMac2:~/Git/kjpf cat GIT-kjpf-on-Himac2
still confused.  I will do   git add -A    et ensuite   git commit -am "Updated README."

HiMac2:~/Git/kjpf vi GIT-kjpf-on-Himac2
            >>> I added "from ~/Git/kjpf:"

HiMac2:~/Git/kjpf git add -A
HiMac2:~/Git/kjpf git commit -am "Updated README."
[master 13afb3a] Updated README.
 2 files changed, 10 insertions(+), 8 deletions(-)
 create mode 100644 GIT-kjpf-on-Himac2

HiMac2:~/Git/kjpf git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

HiMac2:~/Git/kjpf git push
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 6 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 469 bytes | 36.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/bxharold/kjpf.git
   ebfb581..13afb3a  master -> master

         >>> the change was visible on github.

Now, I'm going to add this file: 
    git add -A
    git push
... and check github.

... No change on github.  maybe a commit?
git commit -am "Updated README."
git push


OK, that was better; 
1. I had to back out and back in to this file on github to see the changes.
2. maybe there was something different with editing an existing file, and adding a new file.
3. this is a markdown thing:  underscores and brackets have special meaning.
   to wit:
   - kjpf.py serves up the client UI  (port __CC__)
         CC should be surrounded by double-underscores
   - The web client browses to http://HiMac2.local:[__CC__]/kfpj.html
         CC is correctly surrounded by double-underscores
   - @app.route("/LED/<LEDid>/<onoff>")
         this should be LED/lt LEDid gt/lt onoff gt
         completely: @app.route("LED/lt LEDid gt/lt onoff gt")
4. Maybe a markdown cheat-sheet would help.

 


