# imposer

Lightweight promise library for `threading`.

**Status:** WIP.

## Example

```python
import threading, random
from imposer import Env, Imposer


def hellothere(imp):
    if random.choice([False, True]):
        imp.resolve('hi good morning')
    else:
        imp.reject('cringe')


def main():
    env = Env()
    imp = Imposer(env)  # env for message dispathing
    thr = threading.Thread(target=hellothere, args=(imp))

    try:
        print(imp.wait())
        thr.join()
    except ImposerError as e:
        print('oops a rejection!')
        raise e


if __name__ == '__main__':
    main()
```

## License

MIT
