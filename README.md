StupidParse
===========

Kind of stupid name, eh? 

Tired of parsing things stupidly with long lists of `if`, `elif` and finally and `else`. Wish Python had a `switch` statement? Well, maybe not a switch statement.

Welcome to `StupidParse`

Here's a quick example of how easy it is:

```
    >>> from StupidParse import StupidParser
    >>> p = StupidParser(corpus="The Knights Who Say Ni!")
    >>> p.register_rule(key=True, trigger=lambda x: "Ni!" in x, callback="It!")
    >>> p.run()
    ... "It!"
```

A more realistic example would be:

```
    from StupidParse import StupidParser
    p = StupidParser(corpus="The Knights Who Say Ni!")
    p.register_rule(key=True, trigger=lambda x: "Ni!" in x, callback=MyCallback)
    action = p.run()
```

API
---

`StupidParse` has a stupid simple API and it's stupid simple to expand on.

###StupidParser

* `StupidParser` accepts a corpus upon creation, though submitting on is optional. It defaults to None. It also accepts a default value to return which also defaults (defaultception) to None.
* `StupidParser.run` also accepts a corpus, which is also optional.
* `StupidParser.run` calls each rule registered to it (through their `run` method) sequentially and returns the first rule that's triggered. Otherwise it returns `StupidParser.default`.
* Rules are registered with (surprise) `StupidParser.register_rule`. This is essentially a factory method. Key, Trigger and Callback are all required arguements. There's also the `rule` arguement if you want to pass a different rule type to register, but defaults to the basic `StupidParse.StupidRule`.

###StupidRule
* `StupidRule` accepts a key, a trigger and a callback upon creation, none of these are optional.
* `StupidRule.trigger` must be callable and return a value comparable to `StupidRule.key`. It also only accepts a corpus as it's only input (see below though)
* `StupidRule.run` returns `StupidRule.callback` if the trigger return value matches the key. Callback can be anything. :)

###StupidParseError
This is currently not implemented. But is included for expansion's sake. Feel free to raise and catch them as you please when using StupidParse.

Other Examples
--------------

###Getting StupidRule.trigger to accept multiple inputs.
You though the trigger could only accept one value? That's true when you register it. But what if you want to run a regex on the corpus. Yeah, you could compile it. But if you're using it once, that's just more overhead. You could use a factory:

```
    >>> import re
    >>> def regex_trigger_factory(pattern):
    ...     def trigger(corpus):
    ...         return re.match(pattern, corpus)
    ...     return trigger
```

Or functools:

```
    >>> import re
    >>> from functools import partial
    >>> trigger = partial(re.match, "\bNi!\b")
```

Or use the `__call__` method on a class:

```
    class MyTrigger(object):
        
        def __init__(self, regex="\bNi!\b"):
            self.regex = regex

        def __call__(self, corpus):
            return re.match(self.regex, corpus)
```

The possibilities are endless.

###Expanding StupidParser

Defining a custom custom parser is easy:

```
    class MyParser(StupidParser):
        pass
```

If you wanted to return all Rules that match your corpus, a simple modification to `StupidParser.run` is needed:

```
    class AllRulesParser(StupidParser):
        
        def run(corpus=None):
            corpus = self.corpus or corpus
            rules = []
            for rule in self._rules:
                if  rule.run(corpus)
                    rules.append(rull.callback)

             return rules or self.default
```

###Expanding StupidRule

If you want to define a custom Rule type, it's easy.

```
    class MyRule(StupidRule):
        pass
```

Let's say you wanted to autoload the corpus into the callback:

```
    class AutoloadCorpusRule(StupidRule):
        
        def run(corpus):
            if self.key == self.trigger(corpus):
                self.callback = callback(corpus)
                return True
            return False
```

You'd register it like this then:

```
    from StupidParse import StupidParser
    from rules import AutoloadCorpusRule
    
    def mycallback(corpus):
        print corpus

    p = StupidParser(corpus="The Knights Who Say Ni!", default=None)
    p.register_rule(key=True, trigger=lambda x: "Ni!" in corpus, callback=mycallback, rule=AutoloadCorpusRule)
    p.run()
```
