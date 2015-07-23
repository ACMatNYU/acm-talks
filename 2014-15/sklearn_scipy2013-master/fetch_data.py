import os
import urllib
import tarfile
import zipfile


TWENTY_URL = ("http://people.csail.mit.edu/jrennie/"
              "20Newsgroups/20news-bydate.tar.gz")
TWENTY_ARCHIVE_NAME = "20news-bydate.tar.gz"
TWENTY_CACHE_NAME = "20news-bydate.pkz"
TWENTY_TRAIN_FOLDER = "20news-bydate-train"
TWENTY_TEST_FOLDER = "20news-bydate-test"

SENTIMENT140_URL = ("http://cs.stanford.edu/people/alecmgo/"
                    "trainingandtestdata.zip")
SENTIMENT140_ARCHIVE_NAME = "trainingandtestdata.zip"


def get_datasets_folder():
    here = os.path.dirname(__file__)
    notebooks = os.path.join(here, 'notebooks')
    datasets_folder = os.path.abspath(os.path.join(notebooks, 'datasets'))
    datasets_archive = os.path.abspath(os.path.join(notebooks, 'datasets.zip'))

    if not os.path.exists(datasets_folder):
        if os.path.exists(datasets_archive):
            print("Extracting " + datasets_archive)
            zf = zipfile.ZipFile(datasets_archive)
            zf.extractall('.')
            assert os.path.exists(datasets_folder)
        else:
            print("Creating datasets folder: " + datasets_folder)
            os.makedirs(datasets_folder)
    else:
        print("Using existing dataset folder:" + datasets_folder)
    return datasets_folder


def check_twenty_newsgroups(datasets_folder):
    print("Checking availability of the 20 newsgroups dataset")

    archive_path = os.path.join(datasets_folder, TWENTY_ARCHIVE_NAME)
    train_path = os.path.join(datasets_folder, TWENTY_TRAIN_FOLDER)
    test_path = os.path.join(datasets_folder, TWENTY_TEST_FOLDER)

    if not os.path.exists(archive_path):
        print("Downloading dataset from %s (14 MB)" % TWENTY_URL)
        opener = urllib.urlopen(TWENTY_URL)
        open(archive_path, 'wb').write(opener.read())
    else:
        print("Found archive: " + archive_path)

    if not os.path.exists(train_path) or not os.path.exists(test_path):
        print("Decompressing %s" % archive_path)
        tarfile.open(archive_path, "r:gz").extractall(path=datasets_folder)

    print("Checking that the 20 newsgroups files exist...")
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)
    print("=> Success!")


def check_sentiment140(datasets_folder):
    print("Checking availability of the sentiment 140 dataset")
    archive_path = os.path.join(datasets_folder, SENTIMENT140_ARCHIVE_NAME)
    sentiment140_path = os.path.join(datasets_folder, 'sentiment140')
    train_path = os.path.join(sentiment140_path,
                              'training.1600000.processed.noemoticon.csv')
    test_path = os.path.join(sentiment140_path,
                             'testdata.manual.2009.06.14.csv')

    if not os.path.exists(sentiment140_path):
        if not os.path.exists(archive_path):
            print("Downloading dataset from %s (77MB)" % SENTIMENT140_URL)
            opener = urllib.urlopen(SENTIMENT140_URL)
            open(archive_path, 'wb').write(opener.read())
        else:
            print("Found archive: " + archive_path)

        print("Extracting %s to %s" % (archive_path, sentiment140_path))
        zf = zipfile.ZipFile(archive_path)
        zf.extractall(sentiment140_path)
    print("Checking that the sentiment 140 CSV files exist...")
    assert os.path.exists(train_path)
    assert os.path.exists(test_path)
    print("=> Success!")


if __name__ == "__main__":
    datasets_folder = get_datasets_folder()
    check_twenty_newsgroups(datasets_folder)
    check_sentiment140(datasets_folder)

    print "Loading Labeled Faces Data (~200MB)"
    from sklearn.datasets import fetch_lfw_people
    fetch_lfw_people(min_faces_per_person=70, resize=0.4,
                     data_home=datasets_folder)
    print("=> Success!")
