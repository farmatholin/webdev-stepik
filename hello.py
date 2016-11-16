def application(env, start_response):
    text = ""

    for query in env['QUERY_STRING'].split("&"):
        text += query + "\n"

    body = text.encode("utf-8")

    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [body]
