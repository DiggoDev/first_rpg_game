from cx_Freeze import setup, Executable

# Replace `main.py` with your main script filename
executables = [Executable("first_rpg_game/main.py")]

setup(
    name="first_rpg_game",
    version="0.1",
    description="Rpg game with pygame",
    executables=executables,
)
