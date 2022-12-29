# Linux and Git
## Terminal Commands used
1. git clone
    - Syntax : git clone [url]
    - Used to get a copy of the given repository to the local machine.
    - Used in this task to get TerminalHunt repository available locally.
2. mkdir
    - Syntax : mkdir <dirName>
    - Used to make an empty directory
    - Used this to make the folder 'solution'
3. echo
    - Syntax : echo -e "msg that goes inside the file" >> filename.extension
    - Used to create a file and write into it simultaneously.
    - Used this to create - part1.txt file
4. cp
    - Syntax : cp <file1_path> <file2_path>
    - Used to copy file1 to file 2
    - Used in this task to create - part2.txt, part3.txt and part4.txt
5. mv
    - Syntax : mv <file1_path> <file2_path>
    - Used to Move/Rename file1 to file2
    - Used in this task to crete - part2.txt, part3.txt and part4.txt
6. git log
    - Syntax : git log
    - Used to show all the previous commits
    - Used in this task to get the answer for part3.txt
7. git add
    - Syntax : git add <fileName/dirName>
    - Used to add files or directory into the Staging area before getting committed.
8. git commit
    - Syntax : git commit -m "commitMessage"
    - Used to save changes till this point locally.
9. git branch
    - Syntax : git branch -a
    - Used to to see all the local and remote branches of the repository.
10. git checkout
    - Syntax : git checkout <branch_name>
    - Used to switch from the current branch to <branch_name>
    - Used in switching from main branch to asia branch
11. find
    - Syntax : find . -name <file_name>.extension
    - Used to find files and directories
    - Used to find athens.txt
12. git merge
    - Syntax : git merge <branch_name>
    - Used to combine two independent branches into one.
    - Used in merging asia branch into main branch
13. cat
    - Syntax : cat <file1> <file2>
    - Used to concatenate or add elements inside 2 or more file
    - Used to add result from part1, 2, 3 into password.txt
### Terminal commands used in working with amfoss repository
14. git push
    - Syntax : git push -u origin <branch_name>
    - Used to push all local commits into remote amfoss-tasks repo
15. git pull
    - Syntax : git pull
    - Used in getting all changes made in remote repo to local repo
