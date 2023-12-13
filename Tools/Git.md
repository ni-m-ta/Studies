# Git

**Git** is a distributed version control system designed to track changes in source code during software development. It allows multiple developers to collaborate on a project simultaneously. Git was created by Linus Torvalds in 2005 and has become the most widely used version control system.

## Key Concepts

### 1. **Repository (Repo):**
   - A collection of files and directories along with the version history. Can be local (on your computer) or remote (on a server).

### 2. **Commit:**
   - A snapshot of changes made to the files in the repository at a specific point in time. Each commit has a unique identifier (SHA-1 hash).

### 3. **Branch:**
   - An independent line of development in Git. Allows developers to work on features or bug fixes without affecting the main codebase.

### 4. **Merge:**
   - Combining changes from one branch (source) into another (target). Resolves conflicts if changes overlap.

### 5. **Pull Request (PR):**
   - A way to propose changes and submit them for review before merging into the main branch. Commonly used in collaborative workflows.

### 6. **Clone:**
   - Creating a copy of a remote repository on your local machine.

### 7. **Push:**
   - Uploading local changes to a remote repository.

### 8. **Pull:**
   - Fetching changes from a remote repository to a local repository.

### 9. **Fork:**
   - Creating a personal copy of someone else's project.

### 10. **Merge Conflict:**
   - Occurs when Git is unable to automatically merge changes. Requires manual resolution by the developer.

## Basic Git Workflow

- clone
```
git clone <repository_url>
```

- create a branch
```
git checkout -b <branch_name>
```

- add and commit
```
git add .
git commit -m "Commit message"
```

- first push
```
git remote add origin git@github.com:{UserName}/{RepositoryName}.git
git branch -M main
git push -u origin main
```

- log
```
git log
```

- delete branch
```
git checkout {AnyOtherBranch}
git branch -d {BranchName}
git branch -D {BranchName}
```

- delete remote branch
```
git push origin --delete {BranchName}
```

- check operation histories
```
git reflog
```

## Tips
- こまめにdevとmainにマージしないと後で面倒
