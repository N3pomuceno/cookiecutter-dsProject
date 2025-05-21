# TODO

Possible future plans for this project:

- [x] Re do it with [UV](https://docs.astral.sh/uv/reference/cli/#uv) dependency manager and also [Ruff](https://docs.astral.sh/ruff/) python linter.
    - [x] pyproject.toml - alter to uv.toml
    - [x] Alter a pyproject inside the repository.
    - [x] poetry.lock can go away
    - [x] README.md edit with new manager.
    - [x] Add new ruff.toml or just change .vscode/settings.json  
    - [x] How to install directly, like poetry install. -> Uv sync, but not needed because uv run assert all dependencies are in sync. -> Document this in README.md
    - [x] It create a .venv!

- [x] In the `exec.sh`, ensure it activates venv to execute successfully!

- [x] Create option to ingest data, in a way where we can do a pre work in updating data with a script

- [ ] New tests with:
    - [ ] Using with/without ingestion;
    - [ ] Using with/without project type EDA;

- [ ] Add a way to create a repository directly, which will probably require some pre-configured key on the machine. However, I believe it is feasible to link directly with GitHub/GitLab.  

- [x] Increase the number of libraries, maybe reconsider the *ML_ALL* combination to allow for more library options.  

- [ ] Expand the number of databases we can work with in dbt, as well as in the Dockerfile. Check what we can modify to make this change more practical.  
