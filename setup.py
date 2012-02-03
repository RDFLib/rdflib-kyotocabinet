from setuptools import setup

setup(
    name = 'rdflib-kyotocabinet',
    version = '0.1',
    description = "rdflib extension adding Kyoto Cabinet as back-end store",
    author = "Graham Higgins",
    author_email = "gjhiggins@gmail.com",
    url = "http://github.com/RDFLib/rdflib-kyotocabinet",
    py_modules = ["rdflib_kyotocabinet"],
    test_suite = "test",
    install_requires = ["rdflib>=3.0", 
                        "rdfextras>=0.1", 
                        "Kyoto_Cabinet",
#                        "kyotocabinet-python-legacy>=1.16", # Python 2
#                        "kyotocabinet-python>=1.20", # Python 3
                        ],
    entry_points = {
    	'rdf.plugins.store': [
            'KyotoCabinet = rdfextras.store.KyotoCabinet:KyotoCabinet',
        ],
    }

)
