import logging
import logging.config
import os

import htmlmin
import yaml


# Directory management checks
def get_cwd():
    """
    Retrieves the current working directory.

    Returns
    -------
    cwd : str
        The path to the current working directory.
    """
    return os.getcwd()


def get_jackman_dir():
    """
    Retrieves the path to the installation folder of the Jackman module.

    Returns
    -------
    path : str
        The path to the jackman module folder.
    """
    return os.path.dirname(os.path.abspath(__file__))


def set_dir(directory):
    """
    Changes the current directory to the specified directory.

    Parameters
    ----------
    directory : str
        The path to the directory to change to.

    Returns
    -------
    complete : bool
        Whether or not the directory was changed.
    """
    try:
        os.chdir(str(directory))
        return True
    except OSError:
        return False


def cd_is_project():
    """
    Checks whether or not the current directory is a Jackman project.

    Returns
    -------
    project : bool
        Whether or not the current directory can be marked as an initialized jackman project.
    """
    if os.path.isfile('_jackman_config.yaml') or os.path.isfile('_jackman_config.yml'):
        return True
    return False


def setup_logging():
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stream_formatter = logging.Formatter('%(levelname)s - %(message)s')

    file_handler = logging.FileHandler('jackman.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(stream_formatter)

    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[file_handler, stream_handler]
    )


def get_logger(name):
    return logging.getLogger(name)

def load_yaml(file):
    """
    Loads a yaml-file into a dictionary.

    Parameters
    ----------
    file : str
        The path to the file that should be loaded.

    Returns
    -------
    items : dict
        A dict with all the items in the yaml-file.
    """
    if not is_yaml(file):
        # TODO: This should raise a warning in the logging module.
        return {}

    with open(file, 'r') as f:
        items = yaml.load(f, Loader=yaml.FullLoader)

    return items


def is_yaml(file):
    """
    Checks whether or not the specified file is a yaml-file.

    Parameters
    ----------
    file : str
        The relative path to the file that should be checked.

    Returns
    -------
    bool
        Whether or not the specified file is a yaml-file.
    """
    if file.endswith('.yaml') or file.endswith('.yml'):
        return True
    return False


def minify_html(html):
    # TODO: Make settings for minifying customizable
    minified_html = htmlmin.minify(html,
                                   remove_comments=True,
                                   remove_empty_space=True,
                                   remove_all_empty_space=False,
                                   reduce_empty_attributes=True,
                                   reduce_boolean_attributes=False,
                                   remove_optional_attribute_quotes=True,
                                   convert_charrefs=True,
                                   keep_pre=False
                                   )
    return minified_html
