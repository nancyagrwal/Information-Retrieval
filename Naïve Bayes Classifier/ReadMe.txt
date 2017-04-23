
extract the textcat.zip into dev, test and rain in the same folder as other files


1) nbTrain.py contains program to train which reads Text catalogue train folder and generates model-file
2) nbTest.py contains actual sentiment analysis probram that reads unread test and model file folder and generates prediction file and lists of 20 Postive-negative and Negative-positive weight words
3) Open shell/command prompt and execute python nbTrain <Train_dir> <model_file_path_name>

python nbtrain.py train model-file.txt

4) open shell/command prompt and execute python nbTest <model_file_path_name> <test_dir> <pre_diction_file_path_name>

python nbTest.py model-file.txt test prediction-file-test.txt
python nbTest.py model-file.txt dev prediction-file-dev.txt

5) It will generate a prediction file and print list of 20 positvie to negative and list of 20 negative_postive highest log weighted words
6) I have provided 2 files as follows:
a) list of the 20 terms with the highest ratio of neg-pos weight.txt
b) list of the 20 terms with the highest ratio of pos-neg weight.txt


Prerequisite:

1) make sure python 2.7 is installed
2) make sure PYTHONPATH is set and env _variable path contains absolute path to python installation directory.

