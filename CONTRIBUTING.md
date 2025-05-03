# Contributing to This Project

We welcome contributions from everyone! Follow the steps below to contribute to this project by creating a branch, making your changes, and submitting a pull request.

### Why We Use Pull Requests
A pull request (PR) is a way to propose changes to a project. When you're working on a GitHub project, you don’t make changes directly to the main codebase. Instead, you create a branch to make your changes, and then submit a pull request to ask the project maintainers to review and merge your changes into the main branch. This process helps ensure that the changes are reviewed, tested, and do not break the code before being added to the main project. Think of it as a "request" to pull your changes into the project, and it's an important part of working collaboratively on coding projects.

## 🚀 Getting Started

To contribute, you need a GitHub account and access to this repository as a collaborator.

### 1. Clone the Repository (Only one time )

First, clone the repository to your local machine:

```bash
git clone https://github.com/anthonydopke/QuantWork.git
cd QuantWork
```

### Create Branch, work on it, create PR and Merge 
2. Create a New Branch
Create a new branch for your work. Use a meaningful name that reflects the purpose of the branch:
```bash
git checkout -b feature/yourname/your-branch-name
```
For example:
```bash
git checkout -b fix/button-alignment
```
3. Make Your Changes
Make the necessary changes or additions to the codebase. Keep your changes small and focused.

4. Commit Your Changes
Once you're happy with your changes, stage and commit them:
```bash
git add .
git commit -m "Brief description of your change"
```
5. Push Your Branch to GitHub
Push the branch to the remote repository:
```bash
git push origin feature/yourname/your-branch-name
```

6. Create a Pull Request (PR) as Draft 
Go to the repository on GitHub.
You’ll see a prompt to open a pull request for your newly pushed branch.
Click "Compare & pull request".
Add a clear title and description of your changes.
Select "Create draft pull request".

7. Keep Your Branch Up to Date with main
Before setting your pull request as ready for review , make sure your branch is up to date with the main branch. This will help avoid merge conflicts and ensure your changes are based on the latest version of the project.

To update your branch with main, follow these steps:

Switch to the main branch:
```bash
git checkout main
```
Pull the latest changes from main:
```bash
git pull origin main
```
Switch back to your feature branch:
```bash
git checkout feature/yourname/your-branch-name
```
Merge main into your feature branch:
```bash
git merge main
```
If there are any conflicts, resolve them. After resolving conflicts, commit the changes:
```bash
git add .
git commit -m "Resolved merge conflicts with main"
```
Push the updated branch to GitHub:
```bash
git push origin feature/yourname/your-branch-name
```
8. Once it is up to date , mark your PR as Ready For Review

9. Participate in the Code Review
Respond to any feedback from reviewers.
Make additional commits to the same branch if updates are needed.

10. Merge the PR
Once approved, you or a maintainer can merge the pull request. (automerge is available)

💡 Tips

Keep PRs small and focused for easier reviews.
Write clear, concise commit messages.
You can of course create different branches to work on differents features at the same time :) 
Use descriptive names for branches and PRs.
Thank you for contributing! 🙌
