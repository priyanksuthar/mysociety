from __future__ import absolute_import
from http import HTTPStatus
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import json


class APIResponse(object):
    def __init__(self, success=None, meta=None, body=None, error=None,
                 status_code=None):
        if success is not None and isinstance(success, bool):
            self.success = success
        else:
            self.success = False

        if body is not None and isinstance(body, dict):
            self.body = body
        else:
            self.body = {}

        if meta is not None and isinstance(meta, dict):
            self.meta = meta
        else:
            self.meta = {}

        if error is not None:
            self.error = error
        else:
            self.error = ""

        if status_code is not None and status_code in list(HTTPStatus):
            self.status_code = status_code
        else:
            self.status_code = 200

    def http_response(self):
        body = {
            'success': self.success,
            'body': self.body,
            'error': self.error,
            'meta': self.meta
        }
        return HttpResponse(json.dumps(body),
                            content_type="application/json",
                            status=self.status_code
                            )

    def json_response(self, **kwargs):
        body = {
            'success': self.success,
            'body': self.body,
            'error': self.error,
            'meta': self.meta
        }
        return JsonResponse(body,
                            status=self.status_code,
                            **kwargs
                            )

    def api_response(self, **kwargs):
        body = {
            'success': self.success,
            'body': self.body,
            'error': self.error,
            'meta': self.meta
        }
        return Response(body, status=self.status_code, **kwargs)
