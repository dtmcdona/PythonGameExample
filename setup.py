import cx_Freeze

executables = [cx_Freeze.Executable("PythonBossFight.py")]

cx_Freeze.setup(
    name="Rogue Boss Fights",
    options={"build_exe": {"packages":["pygame","random","time","sys","os"],
                           "include_files":["archer.png","gargoyle.png","arrow.png","wall.png","fireball.png","firebreath.png","firebite.png"]}},
    executables = executables
    )