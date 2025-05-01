# Contributing to This Project

We welcome contributions from everyone! Follow the steps below to contribute to this project by creating a branch, making your changes, and submitting a pull request.

## 🚀 Getting Started

To contribute, you need a GitHub account and access to this repository as a collaborator.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/anthonydopke/QuantWork.git
cd QuantWork
```
2. Create a New Branch
Create a new branch for your work. Use a meaningful name that reflects the purpose of the branch:
```bash
git checkout -b feature/your-branch-name
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
git push origin feature/your-branch-name
```

6. Keep Your Branch Up to Date with main
Before creating a pull request, make sure your branch is up to date with the main branch. This will help avoid merge conflicts and ensure your changes are based on the latest version of the project.

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
git checkout feature/your-branch-name
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
git push origin feature/your-branch-name
```
6. Create a Pull Request (PR)
Go to the repository on GitHub.
You’ll see a prompt to open a pull request for your newly pushed branch.
Click "Compare & pull request".
Add a clear title and description of your changes.
Click "Create pull request".
7. Participate in the Code Review
Respond to any feedback from reviewers.
Make additional commits to the same branch if updates are needed.
8. Merge the PR
Once approved, you or a maintainer can merge the pull request. (automerge is available)

💡 Tips

Keep PRs small and focused for easier reviews.
Write clear, concise commit messages.
Use descriptive names for branches and PRs.
Thank you for contributing! 🙌
