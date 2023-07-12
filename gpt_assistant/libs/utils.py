import logging


def get_logger(name, level=logging.INFO):
    """Get logger"""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger


def dictify_list_of_base_models(list_of_base_models):
    """Turn a list of BaseModels into a list of dicts"""
    return [base_model.dict() for base_model in list_of_base_models]
