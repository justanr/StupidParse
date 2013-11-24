'''StupidParse for parsing stuff and things simply and stupidly.'''

class StupidParseError(Exception):
    '''Base exception for StupidParse.

    Currently not used, but provided for future use and customization.

    '''
    pass

class StupidRule(object):
    '''Root rule for all StupidParse rules. Custom rules should be derived from this class.

    Rule objects should only be instansiated by a StupidParse.StupidParser instance.

    '''

    def __init__(self, key, trigger, callback):
        self.key = key
        self.trigger = trigger
        self.callback = callback

    def run(self, corpus):
        '''The most important method of StupidRule.'''

        return self.key == self.trigger(corpus)

    def __repr__(self):
        return "<StupidParse.StupidRule Key:{}, Trigger:{} Callback:{}>" \
        .format(self.key, self.trigger, self.callback)

class StupidParser(object):
    '''Root parser class for all StupidParser parsers. Custom parsers should derive from this class.

    '''

    def __init__(self, corpus=None, default=None):
        self.corpus = corpus
        self._rules = []

    def register_rule(self, key, trigger, callback, rule=StupidRule):
        self._rules.append(
                    rule(
                        key=key, 
                        trigger=trigger, 
                        callback=callback
                        )
                    )
    def register_rules(self, rules):
        '''Accepts a list of dictionaries with key, trigger, 
        callback and optionally rule set.

        '''

        for rule in rules:
            self.register_rule(**rule)

    def run(self, corpus=None)
        # Favor this corpus value over the instance corpus
        corpus = corpus or self.corpus
        
        for rule in self._rules:
            if rule.run(corpus):
                return rule.callback

        return self.default
