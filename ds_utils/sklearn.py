import numpy as np
from sklearn import cross_validation
from sklearn import metrics
from sklearn import preprocessing


def multiclass_roc_auc_score(y_true, y_score, label_binarizer=None, **kwargs):
    """Compute ROC AUC score for multiclass.
    :param y_true: true multiclass predictions [n_samples]
    :param y_score: multiclass scores [n_samples, n_classes]
    :param label_binarizer: Binarizer to use (sklearn.preprocessing.LabelBinarizer())
    :param kwargs: Additional keyword arguments for sklearn.metrics.roc_auc_score
    :return: Multiclass ROC AUC score
    """
    if label_binarizer is None:
        label_binarizer = preprocessing.LabelBinarizer()
    binarized_true = label_binarizer.fit_transform(y_true)
    score = metrics.roc_auc_score(binarized_true, y_score, **kwargs)
    return score


def split_train_test(y, do_split_stratified=True, **kwargs):
    """Get indexes to split y in train and test sets.
    :param y: Labels of samples
    :param do_split_stratified: Use StratifiedShuffleSplit (else ShuffleSplit)
    :param kwargs: Keyword arguments StratifiedShuffleSplit or ShuffleSplit
    :return: (train indexes, test indexes)
    """
    if do_split_stratified:
        data_splitter = cross_validation.StratifiedShuffleSplit(y, n_iter=1,
                                                                **kwargs)
    else:
        data_splitter = cross_validation.ShuffleSplit(y, n_iter=1, **kwargs)
    train_ix, test_ix = data_splitter.__iter__().next()
    return train_ix, test_ix


class OrderedLabelEncoder(preprocessing.LabelEncoder):
    """Encode labels with value between 0 and n_classes-1 in specified order.
    See also
    --------
    sklearn.preprocessing.LabelEncoder
    """

    def __init__(self, classes):
        self.classes_ = np.array(classes, dtype='O')

    def fit(self, y):
        """ Deprecated method.
        """
        raise Exception('Invalid method: method is deprecated')

    def fit_transform(self, y):
        """ Deprecated method.
        """
        raise Exception('Invalid method: method is deprecated')

    def transform(self, y):
        """Transform labels to normalized encoding.
        Parameters
        ----------
        y : array-like of shape [n_samples]
            Target values.
        Returns
        -------
        y : array-like of shape [n_samples]
        """
        self._check_fitted()

        classes = np.array(np.unique(y), dtype='O')
        preprocessing.label._check_numpy_unicode_bug(classes)
        if len(np.intersect1d(classes, self.classes_)) < len(classes):
            diff = np.setdiff1d(classes, self.classes_)
            raise ValueError("y contains new labels: %s" % str(diff))

        transformed_y = np.zeros_like(y, dtype=int)
        for i_class, current_class in enumerate(self.classes_):
            transformed_y[np.array(y) == current_class] = i_class
        return transformed_y