# Virtual Environments

A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.

It is quite important because it allows you to separate different package versions of the code. For example, if you are using `scikit-learn` in one experiment, save your model with that version and later try to open the file with a new version, there may be problems when reading the file.

## Available options

You can use several options to create the virtual environments, some examples are:

* [venv](https://docs.python.org/3/library/venv.html)
* [conda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
* [pyenv](https://github.com/pyenv/pyenv-virtualenv)

In this course, we will be using `venv`.

## Creating virtual environments

Creation of virtual environments is done by executing the command venv:

```bash
python -m venv /path/to/new/virtual/environment
```

Running this command creates the target directory (creating any parent directories that don’t exist already) and places a pyvenv.cfg file in it with a home key pointing to the Python installation from which the command was run (a common name for the target directory is .venv). 

It also creates a bin (or Scripts on Windows) subdirectory containing a copy/symlink of the Python binary/binaries (as appropriate for the platform or arguments used at environment creation time). It also creates an (initially empty) lib/pythonX.Y/site-packages subdirectory (on Windows, this is Lib\site-packages). If an existing directory is specified, it will be re-used.

### Windows

* Create the `venv`

    ```bash
    python3.11 -m venv c:\path\to\myenv
    ```

* Activate the `myenv`
    Once an environment has been created, you may wish to activate it, e.g. by sourcing an activate script in its bin directory.

    ```bash
    <myvenv>\Scripts\activate.bat
    ```

### Mac

* `cd` to your project directory and run `venv` to create the new virtual environment.

* The following commands will create a new virtual environment under my-project/my-venv.

    ```bash
    cd my-project
    python3.11 -m venv venv
    ```

* Activate the `venv`
    Now that we have a virtual environment, we need to activate it.

    ```bash
    source venv/bin/activate
    ```

## Install libraries

Requirements files serve as a list of items to be installed by pip, when using pip install. Files that use this format are often called `requirements.txt`, since requirements.txt is usually what these files are named (although, that is not a requirement). Check [this](https://pip.pypa.io/en/stable/reference/requirements-file-format/) out to learn more about it.

For this section, ensure you have activated the virtual environment, and create a `requirements.txt` file in the `2-python-fundamentals/virtual-environments/script` directory, then, copy and paste the following code and save the file:

```bash
scikit-learn==1.2.2
```

Once the file is created, run the following command to install the required libraries within the virtual environment:

```bash
pip install -r 2-python-fundamentals/virtual-environments/script/requirements.txt
```

After the installation, verify it by running this command:

```bash
pip freeze
```

You should see something like this:

```bash
joblib==1.2.0
numpy==1.25.0
scikit-learn==1.2.2
scipy==1.10.1
threadpoolctl==3.1.0
```

## Run the script

Once you have activated your virtual environment and installed the requirements, just run the command as follows:

```bash
python 2-python-fundamentals/virtual-environments/script/svr.py 
```

You should see something like this:

```bash
[1.5]
```

Congrats! You have run your first script using a virtual environment on a local computer.

## Google Colab

### What is Colab?

Colab, or "Colaboratory", allows you to write and execute Python in your browser, with

* Zero configuration required
* Access to GPUs free of charge
* Easy sharing

Whether you're a student, a data scientist or an AI researcher, Colab can make your work easier. Watch [Introduction to Colab](https://www.youtube.com/watch?v=inN8seMm7UI) to learn more.

### Intro to Colab

Please go to this [notebook](../script/svr.ipynb))to learn more about Google Colab and how the tool will be used in this course.
