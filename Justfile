# shows the just list
default:
    @just --list

# creates the environment
install:
    uv sync

# checks for mistakes and formating
check:
    uv run ruff check
    uv run ruff format --check

# fixes the mistakes and formating
fix:
    uv run ruff check --fix
    uv run ruff format