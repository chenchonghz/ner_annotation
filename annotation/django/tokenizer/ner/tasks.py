import json
import pytz
from datetime import datetime, timedelta

from . import models, term_matching

from celery import Celery

app = Celery('tasks', backend='rpc://', broker='amqp://guest@localhost:5672//')

UMLS_LOOKUP_TASK_TIMEOUT_IN_MINUTES = 5

@app.task
def preload_umls_lookup(source):
    result = models.UmlsLookupResult.objects.filter(source = source)
    if len(result) == 0:
        # Not in database yet
        # Put placeholder in database
        result = models.UmlsLookupResult()
        result.source = source
        result.algorithm_version = term_matching.UMLS_LOOKUP_ALGORITHM_VERSION
        result.result = ''
        result.save()
        # Start search
        result.result = json.dumps(term_matching.umls_lookup(source))
        result.save()
    else:
        now = datetime.utcnow()
        now = now.replace(tzinfo=pytz.utc)
        if (now - result[0].last_updated) < timedelta(minutes = UMLS_LOOKUP_TASK_TIMEOUT_IN_MINUTES):
            # Recently attempted by other task
            pass
        else:
            if len(result[0].result) == 0 or result[0].algorithm_version < term_matching.UMLS_LOOKUP_ALGORITHM_VERSION:
                # Empty result, or result with old algorithm
                # Put placeholder in database
                result.algorithm_version = term_matching.UMLS_LOOKUP_ALGORITHM_VERSION
                result.save()
                # Start search
                result.result = json.dumps(term_matching.umls_lookup(source))
                result.save()
