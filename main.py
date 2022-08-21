import json
from flask import Request, Response
from statstest import StatisticalTest


def main(request):
    """Based on the request, performs different statistical tests.

    :param request: Details of a test you want to do
    :type request: Request
    :return: The result of the test
    :rtype: Response
    """
    try:
        request_json = request.get_json()
        test_type = request_json['userDefinedContext']['test_type']
        calls = request_json['calls']
        stat_test = StatisticalTest(test_type, calls)
        replies = stat_test.do()
        return_json = json.dumps({'replies': replies})
        return Response(response=return_json, status=200)

    except Exception as e:
        print(e)
        return_json = json.dumps({'errorMessage': "something unexpected in input"})
        return Response(response=return_json, status=400)
