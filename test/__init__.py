from rdflib import plugin
from rdflib import store

plugin.register(
        'KyotoCabinet', store.Store,
        'rdflib_kyotocabinet.KyotoCabinet', 'KyotoCabinet')
