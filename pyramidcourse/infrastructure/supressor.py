import pyramid_handlers


class suppress(pyramid_handlers.action):
    def __init__(self, _, **kw):
        kw['request_method'] = 'NOT_A_HTTP_COMMAND'
        super().__init__(**kw)
