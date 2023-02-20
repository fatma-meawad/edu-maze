## Using Pylint

pylint graphics.py maze.py main.py cell.py
python3 -m mccabe maze.py 

or pylama *.py
maze.py:66:5 C901 'Maze._break_walls_r' is too complex (11) [mccabe]

## Module graphics
graphics.py:1:0: C0114: Missing module docstring (missing-module-docstring)

graphics.py:4:0: C0115: Missing class docstring (missing-class-docstring)

graphics.py:13:4: C0116: Missing function or method docstring (missing-function-docstring)

graphics.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)

graphics.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)

graphics.py:26:4: C0116: Missing function or method docstring (missing-function-docstring)

graphics.py:30:0: C0115: Missing class docstring (missing-class-docstring)

graphics.py:32:8: C0103: Attribute name "x" doesn't conform to snake_case naming style (invalid-name)

graphics.py:33:8: C0103: Attribute name "y" doesn't conform to snake_case naming style (invalid-name)

graphics.py:31:23: C0103: Argument name "x

graphics.py:31:26: C0103: Argument name "y" doesn't conform to snake_case naming style (invalid-name)

graphics.py:30:0: R0903: Too few public methods (0/2) (too-few-public-methods)

graphics.py:36:0: C0115: Missing class docstring (missing-class-docstring)

graphics.py:42:8: C0103: Attribute name "p1" doesn't conform to snake_case naming style (invalid-name)

graphics.py:43:8: C0103: Attribute name "p2" doesn't conform to snake_case naming style (invalid-name)

graphics.py:39:8: C0103: Argument name "p1" doesn't conform to snake_case naming style (invalid-name)

graphics.py:40:8: C0103: Argument name "p2" doesn't conform to snake_case naming style (invalid-name)

graphics.py:45:4: C0116: Missing function or method docstring 
(missing-function-docstring)

graphics.py:36:0: R0903: Too few public methods (1/2) (too-few-public-methods)

## ************* Module maze
maze.py:1:0: C0114: Missing module docstring (missing-module-docstring)

maze.py:6:0: C0115: Missing class docstring (missing-class-docstring)

maze.py:6:0: R0902: Too many instance attributes (8/7) (too-many-instance-attributes)

maze.py:9:8: C0103: Argument name "x1" doesn't conform to snake_case naming style (invalid-name)

maze.py:10:8: C0103: Argument name "y1" doesn't conform to snake_case naming style (invalid-name)

maze.py:7:4: R0913: Too many arguments (9/5) (too-many-arguments)

maze.py:47:8: C0103: Variable name "x1" doesn't conform to snake_case naming style (invalid-name)

maze.py:48:8: C0103: Variable name "y1" doesn't conform to snake_case naming style (invalid-name)

maze.py:49:8: C0103: Variable name "x2" doesn't conform to snake_case naming style (invalid-name)

maze.py:50:8: C0103: Variable name "y2" doesn't conform to snake_case naming style (invalid-name)

maze.py:146:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

maze.py:158:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

maze.py:170:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

maze.py:182:12: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

maze.py:129:4: R0912: Too many branches (13/12) (too-many-branches)

maze.py:191:4: C0116: Missing function or method docstring (missing-function-docstring)

maze.py:6:0: R0903: Too few public methods (1/2) (too-few-public-methods)

maze.py:2:0: C0411: standard import "import random" should be placed before "from cell import Cell" (wrong-import-order)

maze.py:3:0: C0411: standard import "import time" should be placed before "from cell import Cell" (wrong-import-order)

## Module main
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)

main.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)

main.py:3:0: C0411: standard import "import sys" should be placed before "from graphics import Window" (wrong-import-order)

## Module cell
cell.py:1:0: C0114: Missing module docstring (missing-module-docstring)

cell.py:4:0: C0115: Missing class docstring (missing-class-docstring)

cell.py:4:0: R0902: Too many instance attributes (10/7) (too-many-instance-attributes)

cell.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)

cell.py:17:19: C0103: Argument name "x1" doesn't conform to snake_case naming style (invalid-name)

cell.py:17:23: C0103: Argument name "y1" doesn't conform to snake_case naming style (invalid-name)

cell.py:17:27: C0103: Argument name "x2" doesn't conform to snake_case naming style (invalid-name)

cell.py:17:31: C0103: Argument name "y2" doesn't conform to snake_case naming style (invalid-name)

cell.py:49:4: C0116: Missing function or method docstring (missing-function-docstring)

cell.py:55:20: W0212: Access to a protected member _x1 of a client class (protected-access)

cell.py:55:34: W0212: Access to a protected member _x2 of a client class (protected-access)

cell.py:56:20: W0212: Access to a protected member _y1 of a client class (protected-access)

cell.py:56:34: W0212: Access to a protected member _y2 of a client class (protected-access)

cell.py:63:22: W0212: Access to a protected member _x1 of a client class (protected-access)

cell.py:66:57: W0212: Access to a protected member _x2 of a client class (protected-access)

cell.py:70:24: W0212: Access to a protected member _x1 of a client class (protected-access)

cell.py:73:30: W0212: Access to a protected member _x1 of a client class (protected-access)

cell.py:77:24: W0212: Access to a protected member _y1 of a client class (protected-access)

cell.py:80:40: W0212: Access to a protected member _y2 of a client class (protected-access)

cell.py:84:24: W0212: Access to a protected member _y1 of a client class (protected-access)

cell.py:87:67: W0212: Access to a protected member _y1 of a client class (protected-access)

