# imposer

Lightweight promise library for `threading`.

**Status:** WIP.

## Example

```python
import threading, random
from imposer import Env, Imposer


def accumlate(imp):
    if random.choice([False, True]):
        imp.resolve(42)
    else:
        imp.reject('sorry')


def main():
    env = Env()
    imp = Imposer(env)  # env for message dispathing
    thr = threading.Thread(target=accumulate, args=(imp))
    try:
        print(imp.wait())
    except Exception as e:
        print('oops a rejection!')
        raise e


if __name__ == '__main__':
    main()
```

## License

MIT
