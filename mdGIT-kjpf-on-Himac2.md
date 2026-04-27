HiMac2:~/Git/kjpf vi GIT-kjpf-on-Himac2
            >>> I added "from ~/Git/kjpf:"

HiMac2:~/Git/kjpf git add -A
HiMac2:~/Git/kjpf git commit -am "Updated README."
...
HiMac2:~/Git/kjpf git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working tree clean

HiMac2:~/Git/kjpf git push
...
To https://github.com/bxharold/kjpf.git
   ebfb581..13afb3a  master -> master

         >>> the change was visible on github.

Now, I'm going to add all files I've updated or added:
```
    git add -A
    git commit -am "Updated README."
    git push
```

1. I had to back out and back in to this file on github to see the changes.
3. this is a markdown thing, with awareness in github:  
-- underscores and brackets have special meaning.
-- if the file extension is .md, it's rendered, else, it's plaintext
   to wit:
   - kjpf.py serves up the client UI  (port __CC__)
         CC should be surrounded by double-underscores
   - kjpf.py serves up the client UI  `(port __CC__) backticked`
   - The web client browses to http://HiMac2.local:[__CC__]/kfpj.html
         CC is correctly surrounded by double-underscores
   - @app.route("/LED/<LEDid>/<onoff>")
         this should be LED/lt LEDid gt/lt onoff gt
   `- @app.route("/LED/<LEDid>/<onoff>")`  (using backticks)
4. Maybe a markdown cheat-sheet would help.
https://www.markdownguide.org/basic-syntax/#:~:text=First%20line%20with%20two%20spaces,I%20just%20love%20bold%20text.

`https://www.markdownguide.org/basic-syntax/#:~:text=First%20line%20with%20two%20spaces,I%20just%20love%20bold%20text.`


 


