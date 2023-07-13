

```console
$ task
task: [default] python3.11 --version
Python 3.11.4
task: [default] python3.11 minimal.py
Hello there ...
task: [default] pipx run --python python3.11 --spec=black==23.3.0 black --diff minimal.py
⚠️  black is already on your PATH and installed at /home/iwana/.local/bin/black. Downloading and running anyway.
All done! ✨ 🍰 ✨
1 file would be left unchanged.
task: [default] pipx run --python python3.11 --spec=black==23.7.0 black --diff minimal.py || :
⚠️  black is already on your PATH and installed at /home/iwana/.local/bin/black. Downloading and running anyway.
error: cannot format minimal.py: Cannot parse: 5:0: match (SomeClass.type):

Oh no! 💥 💔 💥
1 file would fail to reformat.
task: [default] python3.11 badfile.py PASSWORD
2023-07-13T13:29:02.712 967532 140407683544896 020:INFO     root         badfile:26:black_likes_this TRY AGAIN
2023-07-13T13:29:02.712 967532 140407683544896 020:INFO     root         badfile:35:black_does_not_like_this TRY AGAIN
task: [default] python3.11 badfile.py SECRET
2023-07-13T13:29:02.733 967533 140591304501056 020:INFO     root         badfile:24:black_likes_this YOU GOT IT
2023-07-13T13:29:02.733 967533 140591304501056 020:INFO     root         badfile:33:black_does_not_like_this YOU GOT IT
task: [default] pipx run --python python3.11 --spec=black==23.3.0 black --diff badfile.py
⚠️  black is already on your PATH and installed at /home/iwana/.local/bin/black. Downloading and running anyway.
All done! ✨ 🍰 ✨
1 file would be left unchanged.
task: [default] pipx run --python python3.11 --spec=black==23.7.0 black --diff badfile.py || :
⚠️  black is already on your PATH and installed at /home/iwana/.local/bin/black. Downloading and running anyway.
error: cannot format badfile.py: Cannot parse: 31:4:     match (input + SomeClass.type):

Oh no! 💥 💔 💥
1 file would fail to reformat.

```
