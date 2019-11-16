
Many technologies used in development have functionality that far exceeds the needs and demands of the average users. In fact, in my experience, the power of most command line tool can usually be efficiently captured in a very small subset of the total commands and command options.

I find this is true with the Git distributed version control system as well. I am familiar with a fraction of the functionality and optionality of the package, but the part that I am familiar with delivers a satisfactory results and achieves the stated mission of Git as a whole.

This is a natural rather than forced phenomenon, as functionality and options are constantly expanded as a package is built out to first cater to common, standard cases, and further out to handle the fringe.

The fraction of the command functionality that allows a given user to meet his demands of the package I call my <strong>usage system</strong>.

##Git Overview
Git is a <strong>distributed version control (DVC)</strong> and <strong>source code management (SCM)</strong> system

	- allowing developers to work simultaneously on the same codebase
	- managing code addition / deletion
	- protecting against accidental overwrites or omissions of code changes made by others
	- maintaining a history of every version (i.e. every set of file modifications)

Git is <strong>distributed</strong> because code repositories on the managing server is fully mirrored by every client. This characteristic offers the advantages of

	- majority of git functionality is performed fast and performed locally. Most Git operations require only the local files and resources to execute. Modify and commit to local repository without an internet connection; push changes to server when connection is again available.
	- allowing any client can restore the server in event of server failure. Entire project history is stored on every client.
	- no reliance on central server for every operation
	- implicit backup

Other positive features of Git include the branching functionality (add, delete, merge) and built-in security: all files in Git are SHA-1 check-summed when stored and subsequently referred to be that sum (instead of filenames). All modifications or corruptions are detected by Git.
##Git Usage System
####Adding Files for Tracking by Git
<table style="width:100%;border:none;table-layout:fixed;"><colgroup> <col style="width:50%;" span="1" /></colgroup>
<tbody>

command
action


git add *.*
add all files of any filetype to the project (track)


git add .
add all files and directories of any depth to the project (track)


git add *.*
add all files of all extensions in current directory


git add *
add all files, and all files in all subdirectories


git add *.js *.html
add all .js and .html files


git add [subdir]/*.*
add all files of all files extensions in [workingdir]/[subdir]


git add [subdir]/*
add all files at any depth within [workingdir]/[subdir]

</tbody>
</table>
####Working with Branches
<table style="width:100%;border:none;table-layout:fixed;"><colgroup> <col style="width:50%;" span="1" /></colgroup>
<tbody>

command
action


git branch -D [branch_name]
delete branch even if unmerged


git branch -d [branch_name]
deletes merged branch


git checkout -b [branch_name]
create and switch to branch


git checkout [branch_name]
switch to existing branch


git checkout -b [feature_branch] [branch_name]
creates [feature_branch] from [branch_name] and switches to [feature_branch]


git branch
view branches at local repository


git remote show origin
view branches at remote repository


git push origin --delete [branch_name]
delete [branch_name] from remote repository


git push origin [branch_name]
push local [branch_name] to remote repository (creates branch on remote if nonexistant)

</tbody>
</table>
####Merging
<table style="width:100%;border:none;table-layout:fixed;"><colgroup> <col style="width:50%;" span="1" /></colgroup>
<tbody>

command
action


git merge --no-ff [feature_branch]
merge [feature_branch] into active branch without a fast-forward


git merge [feature_branch]
merge [feature_branch] into active branch (with fast-forward)


git cherry-pick COMMIT_HASH_SHA_ID
apply commit w/ COMMIT_HASH_SHA_ID (in another branch) to active branch (only applies changes in specified commit)

</tbody>
</table>
####Utilities
<table style="width:100%;border:none;table-layout:fixed;"><colgroup> <col style="width:50%;" span="1" /></colgroup>
<tbody>

command
action


git log -v
view commit log (date / times, user, comment, and SHA ID)


git status
view project files changed since last commit (unpushed edits in working tree since last commit)


git config --list
view configuration


git reset --hard
reset working tree to last commit (lose all uncommitted changes; to stash local changes )


git status
view project files changed since last commit (unpushed edits in working tree since last commit)

</tbody>
</table>
When cherry-picking or merging, and the automatic merging algorithms are not able to find a deterministic resolution that combines the two sections of code, conflicts are the result. Here's how I resolve them.
####Resolving Conflicts
Open conflicting files.

&nbsp;

Find the conflicting sections, which follow the following form:

[code gutter="false"]
&lt;&lt;&lt;&lt;&lt; HEAD beginning of local repo

[some code here]

========== end of local conflicting section, beginning of remote

[more code here]

&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt;&gt; SHAID end of remote conflicting section
[/code]

Manually edit the entire section, replacing the it with desired final code.

When all conflicts resolved, commit

[code language="bash" gutter="false"]
[branch | CHERRY-PICKING / MERGING] $ git commit -a -m &quot;comment about resolution&quot;
[/code]

Then, the merge or cherry-pick is complete.

If merge was successful, type :<span style="font-weight:bold;">wq </span> to finish automatic merge and write new version of conflicted file.

The functionality and optionality to handle the fringe is obviously not useless; it was built for a reason. However, it's not worth learning, memorizing, or otherwise integrating into the usage system, because it's only referenced for such, cases, which are, by definition, rare.
<blockquote>More about <strong>git stash, git fetch, git init</strong> is to be added in a future version of this post, along with installed on Windows, screenshots of merge resolution, and the <strong>-a -m </strong>options.</blockquote>]]></content:encoded>

