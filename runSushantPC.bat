@echo off
echo Running experiments...
python launcher.py -n 128random_diameter7test.edgelist -c 2 -r 50
python launcher.py -n 128random_diameter7test.edgelist -c 3.3333333333333333333333333333333333333333 -r 50
python launcher.py -n 128random_diameter7test.edgelist -c 10 -r 50
python launcher.py -n 256random_diameter5test.edgelist -c 2.5 -r 50
python launcher.py -n 256random_diameter5test.edgelist -c 3.3333333333333333333333333333333333333333 -r 50
python launcher.py -n 256random_diameter5test.edgelist -c 10 -r 50
python launcher.py -n 512random_diameter4test.edgelist -c 2 -r 50
python launcher.py -n 512random_diameter4test.edgelist -c 10 -r 50
python launcher.py -n 1024random_diameter4test.edgelist -c 2.5 -r 50
python launcher.py -n 1024random_diameter4test.edgelist -c 10 -r 50
python launcher.py -n 1024random_diameter4test.edgelist -c inf -r 50

echo All experiments completed. 
pause